from enum import unique, Enum


@unique
class LogSource(Enum):
    Active_Directory_Web_Services = 'Active Directory Web Services'
    Application = 'Application'
    DFS_Replication = 'DFS Replication'
    DNS_Server = 'DNS Server'
    DhcpAdminEvents = 'DhcpAdminEvents'
    Directory_Service = 'Directory Service'
    File_Replication_Service = 'File Replication Service'
    HardwareEvents = 'HardwareEvents'
    Internet_Explorer = 'Internet Explorer'
    Key_Management_Service = 'Key Management Service'
    Microsoft_Rdms_UI_Admin = 'Microsoft-Rdms-UI/Admin'
    Microsoft_Rdms_UI_Operational = 'Microsoft-Rdms-UI/Operational'
    Microsoft_WS_Licensing_Admin = 'Microsoft-WS-Licensing/Admin'
    Microsoft_Windows_All_User_Install_Agent_Admin = 'Microsoft-Windows-All-User-Install-Agent/Admin'
    Microsoft_Windows_AppHost_Admin = 'Microsoft-Windows-AppHost/Admin'
    Microsoft_Windows_AppID_Operational = 'Microsoft-Windows-AppID/Operational'
    Microsoft_Windows_AppLocker_EXE_and_DLL = 'Microsoft-Windows-AppLocker/EXE and DLL'
    Microsoft_Windows_AppLocker_MSI_and_Script = 'Microsoft-Windows-AppLocker/MSI and Script'
    Microsoft_Windows_AppLocker_Packaged_app_Deployment = 'Microsoft-Windows-AppLocker/Packaged app-Deployment'
    Microsoft_Windows_AppLocker_Packaged_app_Execution = 'Microsoft-Windows-AppLocker/Packaged app-Execution'
    Microsoft_Windows_AppModel_Runtime_Admin = 'Microsoft-Windows-AppModel-Runtime/Admin'
    Microsoft_Windows_AppXDeployment_Operational = 'Microsoft-Windows-AppXDeployment/Operational'
    Microsoft_Windows_AppXDeploymentServer_Operational = 'Microsoft-Windows-AppXDeploymentServer/Operational'
    Microsoft_Windows_AppXDeploymentServer_Restricted = 'Microsoft-Windows-AppXDeploymentServer/Restricted'
    Microsoft_Windows_Application_Server_Applications_Admin = 'Microsoft-Windows-Application Server-Applications/Admin'
    Microsoft_Windows_Application_Server_Applications_Operational = 'Microsoft-Windows-Application Server-Applications/Operational'
    Microsoft_Windows_Application_Experience_Program_Compatibility_Assistant = 'Microsoft-Windows-Application-Experience/Program-Compatibility-Assistant'
    Microsoft_Windows_Application_Experience_Program_Compatibility_Troubleshooter = 'Microsoft-Windows-Application-Experience/Program-Compatibility-Troubleshooter'
    Microsoft_Windows_Application_Experience_Program_Inventory = 'Microsoft-Windows-Application-Experience/Program-Inventory'
    Microsoft_Windows_Application_Experience_Program_Telemetry = 'Microsoft-Windows-Application-Experience/Program-Telemetry'
    Microsoft_Windows_Application_Experience_Steps_Recorder = 'Microsoft-Windows-Application-Experience/Steps-Recorder'
    Microsoft_Windows_AppxPackaging_Operational = 'Microsoft-Windows-AppxPackaging/Operational'
    Microsoft_Windows_Audio_CaptureMonitor = 'Microsoft-Windows-Audio/CaptureMonitor'
    Microsoft_Windows_Audio_Operational = 'Microsoft-Windows-Audio/Operational'
    Microsoft_Windows_Audio_PlaybackManager = 'Microsoft-Windows-Audio/PlaybackManager'
    Microsoft_Windows_Authentication_User_Interface_Operational = 'Microsoft-Windows-Authentication User Interface/Operational'
    Microsoft_Windows_BackgroundTaskInfrastructure_Operational = 'Microsoft-Windows-BackgroundTaskInfrastructure/Operational'
    Microsoft_Windows_Backup = 'Microsoft-Windows-Backup'
    Microsoft_Windows_Bits_Client_Operational = 'Microsoft-Windows-Bits-Client/Operational'
    Microsoft_Windows_CertificateServices_Deployment_Operational = 'Microsoft-Windows-CertificateServices-Deployment/Operational'
    Microsoft_Windows_CertificateServicesClient_Lifecycle_System_Operational = 'Microsoft-Windows-CertificateServicesClient-Lifecycle-System/Operational'
    Microsoft_Windows_CertificateServicesClient_Lifecycle_User_Operational = 'Microsoft-Windows-CertificateServicesClient-Lifecycle-User/Operational'
    Microsoft_Windows_CodeIntegrity_Operational = 'Microsoft-Windows-CodeIntegrity/Operational'
    Microsoft_Windows_CorruptedFileRecovery_Client_Operational = 'Microsoft-Windows-CorruptedFileRecovery-Client/Operational'
    Microsoft_Windows_CorruptedFileRecovery_Server_Operational = 'Microsoft-Windows-CorruptedFileRecovery-Server/Operational'
    Microsoft_Windows_Crypto_DPAPI_BackUpKeySvc = 'Microsoft-Windows-Crypto-DPAPI/BackUpKeySvc'
    Microsoft_Windows_Crypto_DPAPI_Operational = 'Microsoft-Windows-Crypto-DPAPI/Operational'
    Microsoft_Windows_DFSN_Server_Admin = 'Microsoft-Windows-DFSN-Server/Admin'
    Microsoft_Windows_DataIntegrityScan_Admin = 'Microsoft-Windows-DataIntegrityScan/Admin'
    Microsoft_Windows_DataIntegrityScan_CrashRecovery = 'Microsoft-Windows-DataIntegrityScan/CrashRecovery'
    Microsoft_Windows_DateTimeControlPanel_Operational = 'Microsoft-Windows-DateTimeControlPanel/Operational'
    Microsoft_Windows_DeviceSetupManager_Admin = 'Microsoft-Windows-DeviceSetupManager/Admin'
    Microsoft_Windows_DeviceSetupManager_Operational = 'Microsoft-Windows-DeviceSetupManager/Operational'
    Microsoft_Windows_DeviceSync_Operational = 'Microsoft-Windows-DeviceSync/Operational'
    Microsoft_Windows_Dhcp_Client_Admin = 'Microsoft-Windows-Dhcp-Client/Admin'
    Microsoft_Windows_Dhcp_Server_FilterNotifications = 'Microsoft-Windows-Dhcp-Server/FilterNotifications'
    Microsoft_Windows_Dhcp_Server_Operational = 'Microsoft-Windows-Dhcp-Server/Operational'
    Microsoft_Windows_DhcpNap_Admin = 'Microsoft-Windows-DhcpNap/Admin'
    Microsoft_Windows_Dhcpv6_Client_Admin = 'Microsoft-Windows-Dhcpv6-Client/Admin'
    Microsoft_Windows_Diagnosis_DPS_Operational = 'Microsoft-Windows-Diagnosis-DPS/Operational'
    Microsoft_Windows_Diagnosis_PCW_Operational = 'Microsoft-Windows-Diagnosis-PCW/Operational'
    Microsoft_Windows_Diagnosis_PLA_Operational = 'Microsoft-Windows-Diagnosis-PLA/Operational'
    Microsoft_Windows_Diagnosis_Scripted_Admin = 'Microsoft-Windows-Diagnosis-Scripted/Admin'
    Microsoft_Windows_Diagnosis_Scripted_Operational = 'Microsoft-Windows-Diagnosis-Scripted/Operational'
    Microsoft_Windows_Diagnosis_ScriptedDiagnosticsProvider_Operational = 'Microsoft-Windows-Diagnosis-ScriptedDiagnosticsProvider/Operational'
    Microsoft_Windows_Diagnostics_Networking_Operational = 'Microsoft-Windows-Diagnostics-Networking/Operational'
    Microsoft_Windows_DirectoryServices_Deployment_Operational = 'Microsoft-Windows-DirectoryServices-Deployment/Operational'
    Microsoft_Windows_EapHost_Operational = 'Microsoft-Windows-EapHost/Operational'
    Microsoft_Windows_EapMethods_Ttls_Operational = 'Microsoft-Windows-EapMethods-Ttls/Operational'
    Microsoft_Windows_EnrollmentPolicyWebService_Admin = 'Microsoft-Windows-EnrollmentPolicyWebService/Admin'
    Microsoft_Windows_EnrollmentWebService_Admin = 'Microsoft-Windows-EnrollmentWebService/Admin'
    Microsoft_Windows_EventCollector_Operational = 'Microsoft-Windows-EventCollector/Operational'
    Microsoft_Windows_FMS_Operational = 'Microsoft-Windows-FMS/Operational'
    Microsoft_Windows_FileServices_ServerManager_EventProvider_Admin = 'Microsoft-Windows-FileServices-ServerManager-EventProvider/Admin'
    Microsoft_Windows_FileServices_ServerManager_EventProvider_Operational = 'Microsoft-Windows-FileServices-ServerManager-EventProvider/Operational'
    Microsoft_Windows_FileShareShadowCopyProvider_Operational = 'Microsoft-Windows-FileShareShadowCopyProvider/Operational'
    Microsoft_Windows_Folder_Redirection_Operational = 'Microsoft-Windows-Folder Redirection/Operational'
    Microsoft_Windows_Forwarding_Operational = 'Microsoft-Windows-Forwarding/Operational'
    Microsoft_Windows_GenericRoaming_Admin = 'Microsoft-Windows-GenericRoaming/Admin'
    Microsoft_Windows_GroupPolicy_Operational = 'Microsoft-Windows-GroupPolicy/Operational'
    Microsoft_Windows_Help_Operational = 'Microsoft-Windows-Help/Operational'
    Microsoft_Windows_HomeGroup_Control_Panel_Operational = 'Microsoft-Windows-HomeGroup Control Panel/Operational'
    Microsoft_Windows_IKE_Operational = 'Microsoft-Windows-IKE/Operational'
    Microsoft_Windows_IdCtrls_Operational = 'Microsoft-Windows-IdCtrls/Operational'
    Microsoft_Windows_International_Operational = 'Microsoft-Windows-International/Operational'
    Microsoft_Windows_International_RegionalOptionsControlPanel_Operational = 'Microsoft-Windows-International-RegionalOptionsControlPanel/Operational'
    Microsoft_Windows_Iphlpsvc_Operational = 'Microsoft-Windows-Iphlpsvc/Operational'
    Microsoft_Windows_KdsSvc_Operational = 'Microsoft-Windows-KdsSvc/Operational'
    Microsoft_Windows_Kernel_EventTracing_Admin = 'Microsoft-Windows-Kernel-EventTracing/Admin'
    Microsoft_Windows_Kernel_PnP_Configuration = 'Microsoft-Windows-Kernel-PnP/Configuration'
    Microsoft_Windows_Kernel_PnPConfig_Configuration = 'Microsoft-Windows-Kernel-PnPConfig/Configuration'
    Microsoft_Windows_Kernel_Power_Thermal_Operational = 'Microsoft-Windows-Kernel-Power/Thermal-Operational'
    Microsoft_Windows_Kernel_ShimEngine_Operational = 'Microsoft-Windows-Kernel-ShimEngine/Operational'
    Microsoft_Windows_Kernel_StoreMgr_Operational = 'Microsoft-Windows-Kernel-StoreMgr/Operational'
    Microsoft_Windows_Kernel_WDI_Operational = 'Microsoft-Windows-Kernel-WDI/Operational'
    Microsoft_Windows_Kernel_WHEA_Errors = 'Microsoft-Windows-Kernel-WHEA/Errors'
    Microsoft_Windows_Kernel_WHEA_Operational = 'Microsoft-Windows-Kernel-WHEA/Operational'
    Microsoft_Windows_Known_Folders_API_Service = 'Microsoft-Windows-Known Folders API Service'
    Microsoft_Windows_LanguagePackSetup_Operational = 'Microsoft-Windows-LanguagePackSetup/Operational'
    Microsoft_Windows_MUI_Admin = 'Microsoft-Windows-MUI/Admin'
    Microsoft_Windows_MUI_Operational = 'Microsoft-Windows-MUI/Operational'
    Microsoft_Windows_MemoryDiagnostics_Results_Debug = 'Microsoft-Windows-MemoryDiagnostics-Results/Debug'
    Microsoft_Windows_Mprddm_Operational = 'Microsoft-Windows-Mprddm/Operational'
    Microsoft_Windows_MsLbfoProvider_Operational = 'Microsoft-Windows-MsLbfoProvider/Operational'
    Microsoft_Windows_NCSI_Operational = 'Microsoft-Windows-NCSI/Operational'
    Microsoft_Windows_NTLM_Operational = 'Microsoft-Windows-NTLM/Operational'
    Microsoft_Windows_NdisImPlatform_Operational = 'Microsoft-Windows-NdisImPlatform/Operational'
    Microsoft_Windows_NetworkAccessProtection_Operational = 'Microsoft-Windows-NetworkAccessProtection/Operational'
    Microsoft_Windows_NetworkAccessProtection_WHC = 'Microsoft-Windows-NetworkAccessProtection/WHC'
    Microsoft_Windows_NetworkLocationWizard_Operational = 'Microsoft-Windows-NetworkLocationWizard/Operational'
    Microsoft_Windows_NetworkProfile_Operational = 'Microsoft-Windows-NetworkProfile/Operational'
    Microsoft_Windows_NetworkProvider_Operational = 'Microsoft-Windows-NetworkProvider/Operational'
    Microsoft_Windows_NlaSvc_Operational = 'Microsoft-Windows-NlaSvc/Operational'
    Microsoft_Windows_Ntfs_Operational = 'Microsoft-Windows-Ntfs/Operational'
    Microsoft_Windows_Ntfs_WHC = 'Microsoft-Windows-Ntfs/WHC'
    Microsoft_Windows_Policy_Operational = 'Microsoft-Windows-Policy/Operational'
    Microsoft_Windows_PowerShell_Admin = 'Microsoft-Windows-PowerShell/Admin'
    Microsoft_Windows_PowerShell_Operational = 'Microsoft-Windows-PowerShell/Operational'
    Microsoft_Windows_PrintBRM_Admin = 'Microsoft-Windows-PrintBRM/Admin'
    Microsoft_Windows_PrintService_Admin = 'Microsoft-Windows-PrintService/Admin'
    Microsoft_Windows_PushNotification_Platform_Admin = 'Microsoft-Windows-PushNotification-Platform/Admin'
    Microsoft_Windows_PushNotification_Platform_Operational = 'Microsoft-Windows-PushNotification-Platform/Operational'
    Microsoft_Windows_ReadyBoost_Operational = 'Microsoft-Windows-ReadyBoost/Operational'
    Microsoft_Windows_Regsvr32_Operational = 'Microsoft-Windows-Regsvr32/Operational'
    Microsoft_Windows_ReliabilityAnalysisComponent_Operational = 'Microsoft-Windows-ReliabilityAnalysisComponent/Operational'
    Microsoft_Windows_RemoteApp_and_Desktop_Connections_Admin = 'Microsoft-Windows-RemoteApp and Desktop Connections/Admin'
    Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_Admin = 'Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Admin'
    Microsoft_Windows_RemoteDesktopServices_RdpCoreTS_Operational = 'Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational'
    Microsoft_Windows_Resource_Exhaustion_Detector_Operational = 'Microsoft-Windows-Resource-Exhaustion-Detector/Operational'
    Microsoft_Windows_RestartManager_Operational = 'Microsoft-Windows-RestartManager/Operational'
    Microsoft_Windows_SMBClient_Operational = 'Microsoft-Windows-SMBClient/Operational'
    Microsoft_Windows_SMBDirect_Admin = 'Microsoft-Windows-SMBDirect/Admin'
    Microsoft_Windows_Security_Audit_Configuration_Client_Operational = 'Microsoft-Windows-Security-Audit-Configuration-Client/Operational'
    Microsoft_Windows_Security_Configuration_Wizard_Operational = 'Microsoft-Windows-Security-Configuration-Wizard/Operational'
    Microsoft_Windows_Security_Netlogon_Operational = 'Microsoft-Windows-Security-Netlogon/Operational'
    Microsoft_Windows_Security_SPP_UX_GenuineCenter_Logging_Operational = 'Microsoft-Windows-Security-SPP-UX-GenuineCenter-Logging/Operational'
    Microsoft_Windows_Security_SPP_UX_Notifications_ActionCenter = 'Microsoft-Windows-Security-SPP-UX-Notifications/ActionCenter'
    Microsoft_Windows_ServerManager_ConfigureSMRemoting_Operational = 'Microsoft-Windows-ServerManager-ConfigureSMRemoting/Operational'
    Microsoft_Windows_ServerManager_DeploymentProvider_Operational = 'Microsoft-Windows-ServerManager-DeploymentProvider/Operational'
    Microsoft_Windows_ServerManager_MgmtProvider_Operational = 'Microsoft-Windows-ServerManager-MgmtProvider/Operational'
    Microsoft_Windows_ServerManager_MultiMachine_Admin = 'Microsoft-Windows-ServerManager-MultiMachine/Admin'
    Microsoft_Windows_ServerManager_MultiMachine_Operational = 'Microsoft-Windows-ServerManager-MultiMachine/Operational'
    Microsoft_Windows_Shell_ConnectedAccountState_ActionCenter = 'Microsoft-Windows-Shell-ConnectedAccountState/ActionCenter'
    Microsoft_Windows_Shell_Core_ActionCenter = 'Microsoft-Windows-Shell-Core/ActionCenter'
    Microsoft_Windows_Shell_Core_Operational = 'Microsoft-Windows-Shell-Core/Operational'
    Microsoft_Windows_SmartCard_Audit_Authentication = 'Microsoft-Windows-SmartCard-Audit/Authentication'
    Microsoft_Windows_SmartCard_TPM_VCard_Module_Admin = 'Microsoft-Windows-SmartCard-TPM-VCard-Module/Admin'
    Microsoft_Windows_SmartCard_TPM_VCard_Module_Operational = 'Microsoft-Windows-SmartCard-TPM-VCard-Module/Operational'
    Microsoft_Windows_SmbClient_Connectivity = 'Microsoft-Windows-SmbClient/Connectivity'
    Microsoft_Windows_SmbClient_Security = 'Microsoft-Windows-SmbClient/Security'
    Microsoft_Windows_SmbServer_Connectivity = 'Microsoft-Windows-SmbServer/Connectivity'
    Microsoft_Windows_SmbServer_Operational = 'Microsoft-Windows-SmbServer/Operational'
    Microsoft_Windows_SmbServer_Security = 'Microsoft-Windows-SmbServer/Security'
    Microsoft_Windows_StorageSpaces_Driver_Operational = 'Microsoft-Windows-StorageSpaces-Driver/Operational'
    Microsoft_Windows_StorageSpaces_ManagementAgent_WHC = 'Microsoft-Windows-StorageSpaces-ManagementAgent/WHC'
    Microsoft_Windows_Superfetch_AgmcOperation = 'Microsoft-Windows-Superfetch/AgmcOperation'
    Microsoft_Windows_TCPIP_Operational = 'Microsoft-Windows-TCPIP/Operational'
    Microsoft_Windows_TWinUI_Operational = 'Microsoft-Windows-TWinUI/Operational'
    Microsoft_Windows_TZUtil_Operational = 'Microsoft-Windows-TZUtil/Operational'
    Microsoft_Windows_TaskScheduler_Maintenance = 'Microsoft-Windows-TaskScheduler/Maintenance'
    Microsoft_Windows_TaskScheduler_Operational = 'Microsoft-Windows-TaskScheduler/Operational'
    Microsoft_Windows_TerminalServices_ClientUSBDevices_Admin = 'Microsoft-Windows-TerminalServices-ClientUSBDevices/Admin'
    Microsoft_Windows_TerminalServices_ClientUSBDevices_Operational = 'Microsoft-Windows-TerminalServices-ClientUSBDevices/Operational'
    Microsoft_Windows_TerminalServices_LocalSessionManager_Admin = 'Microsoft-Windows-TerminalServices-LocalSessionManager/Admin'
    Microsoft_Windows_TerminalServices_LocalSessionManager_Operational = 'Microsoft-Windows-TerminalServices-LocalSessionManager/Operational'
    Microsoft_Windows_TerminalServices_PnPDevices_Admin = 'Microsoft-Windows-TerminalServices-PnPDevices/Admin'
    Microsoft_Windows_TerminalServices_PnPDevices_Operational = 'Microsoft-Windows-TerminalServices-PnPDevices/Operational'
    Microsoft_Windows_TerminalServices_RDPClient_Operational = 'Microsoft-Windows-TerminalServices-RDPClient/Operational'
    Microsoft_Windows_TerminalServices_RemoteConnectionManager_Admin = 'Microsoft-Windows-TerminalServices-RemoteConnectionManager/Admin'
    Microsoft_Windows_TerminalServices_RemoteConnectionManager_Operational = 'Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational'
    Microsoft_Windows_TerminalServices_ServerUSBDevices_Admin = 'Microsoft-Windows-TerminalServices-ServerUSBDevices/Admin'
    Microsoft_Windows_TerminalServices_ServerUSBDevices_Operational = 'Microsoft-Windows-TerminalServices-ServerUSBDevices/Operational'
    Microsoft_Windows_TerminalServices_SessionBroker_Client_Admin = 'Microsoft-Windows-TerminalServices-SessionBroker-Client/Admin'
    Microsoft_Windows_TerminalServices_SessionBroker_Client_Operational = 'Microsoft-Windows-TerminalServices-SessionBroker-Client/Operational'
    Microsoft_Windows_UAC_Operational = 'Microsoft-Windows-UAC/Operational'
    Microsoft_Windows_UAC_FileVirtualization_Operational = 'Microsoft-Windows-UAC-FileVirtualization/Operational'
    Microsoft_Windows_User_Control_Panel_Operational = 'Microsoft-Windows-User Control Panel/Operational'
    Microsoft_Windows_User_Profile_Service_Operational = 'Microsoft-Windows-User Profile Service/Operational'
    Microsoft_Windows_UserPnp_ActionCenter = 'Microsoft-Windows-UserPnp/ActionCenter'
    Microsoft_Windows_UserPnp_DeviceInstall = 'Microsoft-Windows-UserPnp/DeviceInstall'
    Microsoft_Windows_VDRVROOT_Operational = 'Microsoft-Windows-VDRVROOT/Operational'
    Microsoft_Windows_VHDMP_Operational = 'Microsoft-Windows-VHDMP/Operational'
    Microsoft_Windows_WER_Diag_Operational = 'Microsoft-Windows-WER-Diag/Operational'
    Microsoft_Windows_WFP_Operational = 'Microsoft-Windows-WFP/Operational'
    Microsoft_Windows_WMI_Activity_Operational = 'Microsoft-Windows-WMI-Activity/Operational'
    Microsoft_Windows_WinRM_Operational = 'Microsoft-Windows-WinRM/Operational'
    Microsoft_Windows_Windows_Firewall_With_Advanced_Security_ConnectionSecurity = 'Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurity'
    Microsoft_Windows_Windows_Firewall_With_Advanced_Security_Firewall = 'Microsoft-Windows-Windows Firewall With Advanced Security/Firewall'
    Microsoft_Windows_WindowsUpdateClient_Operational = 'Microsoft-Windows-WindowsUpdateClient/Operational'
    Microsoft_Windows_Winlogon_Operational = 'Microsoft-Windows-Winlogon/Operational'
    Microsoft_Windows_Winsock_WS2HELP_Operational = 'Microsoft-Windows-Winsock-WS2HELP/Operational'
    Microsoft_Windows_Wired_AutoConfig_Operational = 'Microsoft-Windows-Wired-AutoConfig/Operational'
    Operational = 'Operational'
    Security = 'Security'
    Setup = 'Setup'
    System = 'System'
    Windows_PowerShell = 'Windows PowerShell'
    WitnessClientAdmin = 'WitnessClientAdmin'