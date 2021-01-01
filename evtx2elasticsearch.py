"""
evtx2sqlite.py

converts evtx files to an elasticsearch index.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""
import sys
from datetime import datetime

import progressbar
from evtx import PyEvtxParser

import el
import evtxtools
import orjson
import coloredlogs, logging
from elasticsearch_dsl import connections, Index, IndexTemplate, Mapping
from elasticsearch.helpers import bulk

class SimpleWindowsEvent:
    SEPARATOR = "/"
    event_id: int
    record_id: int
    level: int
    provider_name: str
    provider_guid: str
    process_id: int
    thread_id: int
    activity_id: str
    related_activity_id: str
    channel: str
    computer: str
    timestamp: datetime
    timecreated: datetime
    user: str
    event_data: dict

    def __init__(self, record: dict):
        self.__values = dict()
        if record['timestamp'][19] == '.':
            self.timestamp = datetime.strptime(record['timestamp'], "%Y-%m-%d %H:%M:%S.%f %Z")
        else:
            self.timestamp = datetime.strptime(record['timestamp'], "%Y-%m-%d %H:%M:%S %Z")

        self.__record = orjson.loads(record['data'])
        self.cache_values(prefix="", dictionary=self.__record['Event'])

        self.event_id = self.safe_int(self["/System/EventID"])
        self.record_id = self.safe_int(self["/System/EventRecordID"])
        self.level = self.safe_int(self["/System/Level"])
        self.provider_name = str(self["/System/Provider/@Name"])
        self.provider_guid = str(self["/System/Provider/@Guid"])
        self.process_id = self.safe_int(self["/System/Execution/@ProcessID"])
        self.thread_id = self.safe_int(self["/System/Execution/@ThreadID"])
        self.activity_id = str(self["/System/Correlation/@ActivityID"])
        self.related_activity_id = str(self["/System/Correlation/@RelatedActivityID"])
        self.channel = str(self["/System/Channel"])
        self.computer = str(self["/System/Computer"])
        self.timecreated = self.get_time_created(self["/System/TimeCreated/@SystemTime"])
        self.user = str(self["/System/Security/@UserID"])
        self.event_data = self.__record['Event'].get('EventData')

    @staticmethod
    def safe_int(item):
        return int(item) if item else None

    @staticmethod
    def get_time_created(timecreated):
        if timecreated[19] == '.':
            return datetime.strptime(timecreated, "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            return datetime.strptime(timecreated, "%Y-%m-%dT%H:%M:%SZ")

    def cache_values(self, prefix: str, dictionary: dict):
        for _key, _value in dictionary.items():
            if _key == '#attributes':
                assert isinstance(_value, dict)
                for _a_key, _a_value in _value.items():
                    assert not isinstance(_a_value, dict)
                    self.__values[prefix + self.SEPARATOR + "@" + _a_key] = _a_value
                continue

            _id = prefix + self.SEPARATOR + _key

            if _key == '#text':
                self.__values[prefix] = _value
                continue

            if isinstance(_value, dict):
                self.cache_values(_id, _value)
            else:
                assert _key not in self.__values
                self.__values[_id] = _value

    def __getitem__(self, item) -> str:
        return self.get_property(item, allow_none=True)

    def get_property(self, path: str, allow_none=False) -> str:
        if allow_none:
            return self.__values.get(path)
        else:
            return self.__values[path]


def event_to_dict(filename: str, swe: SimpleWindowsEvent, index: str):
    event = el.WindowsEvent(
        event={
            'code': swe.event_id,
            'created': swe.timecreated,
            'provider': swe.provider_name,
            'severity': swe.level
        },
        record_id=swe.record_id,
        timestamp=swe.timestamp,
        correlation={'activity_id': swe.activity_id, 'related_activity_id': swe.related_activity_id},
        channel=swe.channel,
        computer=swe.computer,
        user={
            'id': swe.user
        },
        execution={'process_id': swe.process_id, 'thread_id': swe.thread_id},
        event_data=swe.event_data,
        log={
            'file': {
                'path': filename
            },
            'level': swe.level
        }
    )
    return event.to_dict()

class EventGenerator:
    def __init__(self,
                 filename: str,
                 index: str,
                 raw_items: list,
                 progress_bar: progressbar.progressbar):
        self.__filename = filename
        self.__index = index
        self.__raw_items = raw_items
        self.__progress = progress_bar
        self.__counter = 0

    def __iter__(self):
        for r in self.__raw_items:
            self.__counter += 1
            self.__progress.update(self.__counter)
            yield event_to_dict(
                filename=self.__filename,
                swe=SimpleWindowsEvent(r),
                index=self.__index)


def evtx2elasticsearch(evtx_files: set, index: str, template:str, override: False):
    connections.create_connection(hosts=['localhost'], timeout=20)

    create_index(index=index, template=template, override=override)

    el.WindowsEvent.init(index=index)

    for f in evtx_files:

        parser = PyEvtxParser(str(f))
        items = list()
        for e in progressbar.progressbar(parser.records_json(), prefix="parsing " + f.name):
            items.append(e)

        bar = progressbar.ProgressBar(max_value=len(items), prefix=f.name)
        generator = EventGenerator(
            filename=f.name,
            index=index,
            raw_items=items,
            progress_bar=bar
        )
        bulk(connections.get_connection(), generator, index=index)


def create_index(index: str, template: str, override: bool):
    logger = logging.getLogger()
    i = Index(name=index)
    if i.exists():
        if override:
            logger.warning("deleting index '{index}'".format(index=index))
            i.delete()
        else:
            raise ValueError("index '{index}' exists already, "
                             "you must specify '--override' to override this index".format(index=index))
    assert not i.exists()
    index_template = """
        {
          "template": {
            "settings": {},
            "mappings": {
              "dynamic_templates": [
                {
                  "event_data": {
                    "path_match": "event_data.*",
                    "mapping": {
                      "type": "text"
                    }
                  }
                }
              ]
            },
            "aliases": {}
          }
        }
        """
    i.get_or_create_mapping().meta('numeric_detection', False)
    i.create()



def main():
    logger = logging.getLogger()
    logging.getLogger("elasticsearch").setLevel(logging.ERROR)
    coloredlogs.install(
        level='INFO',
        logger=logger,
        fmt="%(levelname)s %(message)s")
    args = evtxtools.parse_evtx2elasticsearch_arguments()

    evtx_files = set()
    for f in args.logsdir.iterdir():
        if f.name.endswith(".evtx"):
            evtx_files.add(f)

    template = args.template or args.index + "-template"
    logger.info("using {template} as index template".format(template=template))

    try:
        evtx2elasticsearch(evtx_files, index=args.index, template=template, override=args.override_index)
    except ValueError as e:
        logger.fatal(str(e))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
