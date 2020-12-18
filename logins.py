"""
logins.py

Parses Security.evtx and correlates logon and logoff events to display a user
session timeline.

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

import functools
import sys
import argparse
from evtx import PyEvtxParser
import xmltodict
from datetime import datetime, timedelta
import progressbar
from enum import Enum
import xml


class LogonType(Enum):
    LOGIN_SUCCESS = 10,
    LOGIN_FAILURE = 11,
    LOGOUT = 20,
    RDP_ACCEPTED_CONNECTION = 110,
    RDP_FAILURE = 111


class EventDescriptor:
    def __init__(self, type: LogonType, **kwargs):
        self.__type = type
        self.__properties = dict()
        self.__properties['logon_type'] = kwargs.get('logon_type')
        self.__properties['workstation_name'] = kwargs.get('workstation_name')
        self.__properties['target_user_name'] = kwargs.get('target_user_name')
        self.__properties['target_user_sid'] = kwargs.get('target_user_sid')
        self.__properties['target_logon_id'] = kwargs.get('target_logon_id')
        self.__properties['ip_address'] = kwargs.get('ip_address')
        self.__properties['description'] = kwargs.get('description')
        self.__values = dict()

    def instantiate(self, event_data: dict):
        instance = EventDescriptor(self.type,**self.__properties)
        for property, event_entry in self.__properties.items():
            instance.__values[property] = event_data.get(event_entry)
        return instance

    @property
    def values(self):
        return self.__values

    @property
    def type(self) -> LogonType:
        return self.__type

    @property
    def description(self) -> str:
        return self.__properties.get('description')

    @property
    def logon_type(self):
        return self.__values['logon_type']

    @property
    def workstation_name(self) -> str:
        return self.__values['workstation_name']

    @property
    def target_user_name(self) -> str:
        return self.__values['target_user_name']

    @property
    def target_user_sid(self) -> str:
        return self.__values['target_user_sid']

    @property
    def target_logon_id(self) -> str:
        return self.__values['target_logon_id']

    @property
    def ip_address(self) -> str:
        return self.__values['ip_address']


EVENT_DESCRIPTORS = {
    # https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624
    4624: EventDescriptor(type=LogonType.LOGIN_SUCCESS,
                          logon_type='LogonType',
                          workstation_name='WorkstationName',
                          target_user_name='TargetUserName',
                          target_user_sid='TargetUserSid',
                          target_logon_id='TargetLogonId',
                          ip_address='IpAddress'),

    # https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4625
    4625: EventDescriptor(type=LogonType.LOGIN_FAILURE,
                          description='An account failed to log on',
                          logon_type='LogonType',
                          workstation_name='WorkstationName',
                          target_user_name='TargetUserName',
                          target_user_sid='TargetUserSid',
                          target_logon_id='TargetLogonId',
                          ip_address='IpAddress'),

    # https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4634
    4634: EventDescriptor(type=LogonType.LOGOUT,
                          target_user_name='TargetUserName',
                          target_user_sid='TargetUserSid',
                          target_logon_id='TargetLogonId'),

    # https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4647
    4647: EventDescriptor(type=LogonType.LOGOUT,
                          target_user_name='TargetUserName',
                          target_user_sid='TargetUserSid',
                          target_logon_id='TargetLogonId'),

    131:  EventDescriptor(type=LogonType.RDP_ACCEPTED_CONNECTION,
                          description='Accepted RDP connection',
                          workstation_name='ClientIP'
                          ),

    140:  EventDescriptor(type=LogonType.RDP_FAILURE,
                          description='RDP connection failed',
                          workstation_name='IPString'
                          )
}

@functools.total_ordering
class LoginSession:
    LOGON_TYPES = {
        2: "Interactive",
        3: "Network",
        4: "Batch",
        5: "Service",
        7: "Unlock",
        8: "NetworkCleartext",
        9: "NewCredentials",
        10: "RemoteInteractive",
        11: "CachedInteractive"
    }
    UNKNOWN_TIME = "????-??-?? ??:??:??"
    NO_TIME      = "                   "

    def __init__(self, event_id: int, timestamp: datetime, event: EventDescriptor):
        self.__login_timestamp = None
        self.__login_event_id = None
        self.__login_event = None
        self.__logout_timestamp = None
        self.__logout_event_id = None
        self.__logout_event = None
        self.__description = None
        self.__can_logout = True

        if event.type == LogonType.LOGIN_SUCCESS:
            self.__login_event_id = event_id
            self.__login_timestamp = timestamp
            self.__login_event = event
        elif event.type == LogonType.LOGOUT:
            self.__logout_event_id = event_id
            self.__logout_timestamp = timestamp
            self.__logout_event = event
        else:
            self.__login_event_id = event_id
            self.__login_timestamp = timestamp
            self.__login_event = event
            self.__can_logout = False
            self.__description = event.description

        assert self.logged_in or self.logged_out

    def merge(self, event_id: int, timestamp: datetime, event: EventDescriptor):
        if self.logged_in and event.type == LogonType.LOGOUT:
            self.__logout_event_id = event_id
            self.__logout_timestamp = timestamp
            self.__logout_event = self.__merge_event_data(self.__logout_event, event)
        elif self.logged_out and event.type == LogonType.LOGIN_SUCCESS:
            self.__login_event_id = event_id
            self.__login_timestamp = timestamp
            self.__login_event = self.__merge_event_data(self.__login_event, event)
        else:
            my_event = self.__login_event if self.logged_in else self.__logout_event
            for key, value in event.values.items():
                if my_event.values.get(key) in (None, '-'):
                    my_event.values[key] = value

    @staticmethod
    def __merge_event_data(my_event: EventDescriptor, new_event: EventDescriptor) -> EventDescriptor:
        if my_event is None:
            return new_event
        for key, value in new_event.values.items():
            if my_event.values.get(key) in (None, '-'):
                my_event.values[key] = value
        return my_event

    @property
    def logged_out(self) -> bool:
        return self.__logout_timestamp is not None

    @property
    def logged_in(self) -> bool:
        return self.__login_timestamp is not None

    def __str__(self):
        if self.__can_logout:
            return "%s - %s (%s): %s login as %s from %s (%s)" % (
                self.login_time,
                self.logout_time,
                self.duration,
                self.login_type,
                self.username,
                self.workstation_name,
                self.ip_address
            )
        else:
            return "%s: %s as %s from %s (%s)" % (
                self.login_time,
                self.__description,
                self.username,
                self.workstation_name,
                self.ip_address
            )

    @property
    def duration(self) -> timedelta:
        if self.__login_timestamp and self.__logout_timestamp:
            return self.__logout_timestamp - self.__login_timestamp
        else:
            return ""

    @property
    def login_time(self):
        return self.__login_timestamp.strftime("%Y-%m-%d %H:%M:%S") if self.__login_timestamp else self.UNKNOWN_TIME

    @property
    def logout_time(self):
        return self.__logout_timestamp.strftime("%Y-%m-%d %H:%M:%S") if self.__logout_timestamp else self.UNKNOWN_TIME

    @property
    def login_type(self):
        return self.LOGON_TYPES[int(self.__login_event.logon_type)] if self.__login_event and self.__login_event.logon_type else "Unknown"

    @property
    def username(self):
        if self.__login_event:
            if self.__login_event.target_user_name:
                return self.__login_event.target_user_name
        if self.__logout_event:
            if self.__logout_event.target_user_name:
                return self.__logout_event.target_user_name
        return "unknown user"

    @property
    def workstation_name(self):
        if self.__login_event:
            if self.__login_event.workstation_name:
                return self.__login_event.workstation_name
        return '-'

    @property
    def ip_address(self):
        if self.__login_event:
            if self.__login_event.ip_address:
                return self.__login_event.ip_address
        return '-'

    @property
    def login_timestamp(self):
        return self.__login_timestamp

    @property
    def logout_timestamp(self):
        return self.__logout_timestamp

    @property
    def session_id(self):
        if self.__login_event:
            return self.__login_event.target_logon_id
        else:
            return self.__logout_event.target_logon_id

    def __eq__(self, other):
        if self.logged_in != other.logged_in:
            return False
        if self.logged_out != other.logged_out:
            return False
        if self.logged_in:
            return self.login_timestamp.__eq__(other.login_timestamp)
        elif self.logged_out:
            return self.logout_timestamp.__eq__(other.logout_timestamp)
        else:
            return False

    def __lt__(self, other):
        if self.logged_in == other.logged_in:
            if self.logged_in:
                return self.login_timestamp.__lt__(other.login_timestamp)
            elif self.logged_out:
                return self.logout_timestamp.__lt__(other.logout_timestamp)
            else:
                return False
        else:
            if other.logged_out:
                return other.logout_timestamp.__lt__(self.__login_timestamp)
            elif other.logged_in:
                return other.login_timestamp.__gt__(self.__logout_timestamp)


def exclude_event(event_data: dict, excluded_accounts: dict) -> bool:
    if 'TargetUserSid' in event_data:
        return event_data['TargetUserSid'] in excluded_accounts

    return False

def parse_record_data(record_data: dict) -> dict:
    idx = record_data.find('\n')
    return xmltodict.parse(record_data[idx:])

def handle_record(activity_id: str, event_data: dict, event_id: int, timestamp: datetime, sessions: dict):

    event = EVENT_DESCRIPTORS.get(event_id).instantiate(event_data)

    session = sessions.get(activity_id)
    if session is None:
        sessions[activity_id] = LoginSession(event_id, timestamp, event)
    else:
        session.merge(event_id, timestamp, event)

def print_logins(secfile, rdpfile, from_date: datetime, to_date: datetime, excluded_acounts: list):
    sessions = dict()

    from_date = datetime.strptime(from_date, "%Y-%m-%d %H:%M:%S") if from_date else datetime.min
    to_date = datetime.strptime(to_date, "%Y-%m-%d %H:%M:%S") if to_date else datetime.max
    assert from_date <= to_date

    if secfile:
        parser = PyEvtxParser(secfile)
        parse_records_from_dict(parser, sessions, from_date, to_date, excluded_acounts)

    if rdpfile:
        parser = PyEvtxParser(rdpfile)
        parse_records_from_dict(parser, sessions, from_date, to_date, excluded_acounts)

    for s in sorted(sessions.values()):
        print(str(s))


def parse_records_from_dict(records, sessions, from_date, to_date, excluded_accounts):
    for record in progressbar.progressbar(records.records()):
        timestamp = datetime.strptime(record['timestamp'], "%Y-%m-%d %H:%M:%S.%f UTC")
        if timestamp < from_date or timestamp > to_date:
            continue

        try:
            record_data = parse_record_data(record['data'])
        except xml.parsers.expat.ExpatError:
            # TODO: print warning
            continue

        event_id = int(record_data['Event']['System']['EventID'])

        if event_id in EVENT_DESCRIPTORS.keys():
            event_data = dict()
            for d in record_data['Event']['EventData']['Data']:
                if isinstance(d, dict):
                    event_data[d['@Name']] = d['#text'] if '#text' in d else '-'
            if not exclude_event(event_data, excluded_accounts):
                activity_id = getCorrelationId(record_data)
                handle_record(activity_id, event_data, event_id, timestamp, sessions)


def getCorrelationId(record_data: dict) -> str:
    correlation = record_data['Event']['System'].get('Correlation')
    if correlation and '@ActivityID' in correlation:
        activity_id = record_data['Event']['System']['Correlation']['@ActivityID']
        if activity_id and len(activity_id) > 0:
            return activity_id

    data = record_data['Event']['EventData'].get('Data')
    if data:
        for d in record_data['Event']['EventData']['Data']:
            if d['@Name'] == 'TargetLogonId':
                return d['#text']
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='analyse user sessions')
    parser.add_argument('--security',
                        dest='secfile',
                        help='path of the Security.evtx file',
                        type=argparse.FileType('rb'))

    parser.add_argument('--rdp',
                        dest='rdpfile',
                        help='path of the RdpCoreTS%4Operational.evtx file',
                        type=argparse.FileType('rb'))

    parser.add_argument('--from',
                        dest='from_date',
                        help='timestamp pattern, where to start',
                        type=str)

    parser.add_argument('--to',
                        dest='to_date',
                        help='timestamp pattern, where to end',
                        type=str)

    parser.add_argument('--include-local-system',
                        dest='include_local_system',
                        help='also show logins of the local system account',
                        action='store_true')

    parser.add_argument('--include-anonymous',
                        dest='include_anonymous',
                        help='also show logins of the anonymous account',
                        action='store_true')

    args = parser.parse_args()
    secfile = args.secfile
    rdpfile = args.rdpfile

    system_accounts = [
        'S-1-5-90-1',  # DWM-1
        'S-1-5-90-4'  # DWM-4
    ]
    if not args.include_local_system:
        system_accounts.append('S-1-5-18')

    if not args.include_anonymous:
        system_accounts.append('S-1-5-7')

    print_logins(secfile, rdpfile, args.from_date, args.to_date, system_accounts)
