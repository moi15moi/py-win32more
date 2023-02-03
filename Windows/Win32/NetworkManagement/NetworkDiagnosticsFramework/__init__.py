from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework
import Windows.Win32.Networking.WinSock
import Windows.Win32.Security
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
ATTRIBUTE_TYPE = Int32
AT_INVALID: ATTRIBUTE_TYPE = 0
AT_BOOLEAN: ATTRIBUTE_TYPE = 1
AT_INT8: ATTRIBUTE_TYPE = 2
AT_UINT8: ATTRIBUTE_TYPE = 3
AT_INT16: ATTRIBUTE_TYPE = 4
AT_UINT16: ATTRIBUTE_TYPE = 5
AT_INT32: ATTRIBUTE_TYPE = 6
AT_UINT32: ATTRIBUTE_TYPE = 7
AT_INT64: ATTRIBUTE_TYPE = 8
AT_UINT64: ATTRIBUTE_TYPE = 9
AT_STRING: ATTRIBUTE_TYPE = 10
AT_GUID: ATTRIBUTE_TYPE = 11
AT_LIFE_TIME: ATTRIBUTE_TYPE = 12
AT_SOCKADDR: ATTRIBUTE_TYPE = 13
AT_OCTET_STRING: ATTRIBUTE_TYPE = 14
NDF_ERROR_START: UInt32 = 63744
NDF_E_LENGTH_EXCEEDED: Windows.Win32.Foundation.HRESULT = -2146895616
NDF_E_NOHELPERCLASS: Windows.Win32.Foundation.HRESULT = -2146895615
NDF_E_CANCELLED: Windows.Win32.Foundation.HRESULT = -2146895614
NDF_E_DISABLED: Windows.Win32.Foundation.HRESULT = -2146895612
NDF_E_BAD_PARAM: Windows.Win32.Foundation.HRESULT = -2146895611
NDF_E_VALIDATION: Windows.Win32.Foundation.HRESULT = -2146895610
NDF_E_UNKNOWN: Windows.Win32.Foundation.HRESULT = -2146895609
NDF_E_PROBLEM_PRESENT: Windows.Win32.Foundation.HRESULT = -2146895608
RF_WORKAROUND: UInt32 = 536870912
RF_USER_ACTION: UInt32 = 268435456
RF_USER_CONFIRMATION: UInt32 = 134217728
RF_INFORMATION_ONLY: UInt32 = 33554432
RF_UI_ONLY: UInt32 = 16777216
RF_SHOW_EVENTS: UInt32 = 8388608
RF_VALIDATE_HELPTOPIC: UInt32 = 4194304
RF_REPRO: UInt32 = 2097152
RF_CONTACT_ADMIN: UInt32 = 131072
RF_RESERVED: UInt32 = 1073741824
RF_RESERVED_CA: UInt32 = 2147483648
RF_RESERVED_LNI: UInt32 = 65536
RCF_ISLEAF: UInt32 = 1
RCF_ISCONFIRMED: UInt32 = 2
RCF_ISTHIRDPARTY: UInt32 = 4
DF_IMPERSONATION: UInt32 = 2147483648
DF_TRACELESS: UInt32 = 1073741824
NDF_INBOUND_FLAG_EDGETRAVERSAL: UInt32 = 1
NDF_INBOUND_FLAG_HEALTHCHECK: UInt32 = 2
NDF_ADD_CAPTURE_TRACE: UInt32 = 1
NDF_APPLY_INCLUSION_LIST_FILTER: UInt32 = 2
@winfunctype('NDFAPI.dll')
def NdfCreateIncident(helperClassName: Windows.Win32.Foundation.PWSTR, celt: UInt32, attributes: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head), handle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateWinSockIncident(sock: Windows.Win32.Networking.WinSock.SOCKET, host: Windows.Win32.Foundation.PWSTR, port: UInt16, appId: Windows.Win32.Foundation.PWSTR, userId: POINTER(Windows.Win32.Security.SID_head), handle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateWebIncident(url: Windows.Win32.Foundation.PWSTR, handle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateWebIncidentEx(url: Windows.Win32.Foundation.PWSTR, useWinHTTP: Windows.Win32.Foundation.BOOL, moduleName: Windows.Win32.Foundation.PWSTR, handle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateSharingIncident(UNCPath: Windows.Win32.Foundation.PWSTR, handle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateDNSIncident(hostname: Windows.Win32.Foundation.PWSTR, queryType: UInt16, handle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateConnectivityIncident(handle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateNetConnectionIncident(handle: POINTER(c_void_p), id: Guid) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreatePnrpIncident(cloudname: Windows.Win32.Foundation.PWSTR, peername: Windows.Win32.Foundation.PWSTR, diagnosePublish: Windows.Win32.Foundation.BOOL, appId: Windows.Win32.Foundation.PWSTR, handle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCreateGroupingIncident(CloudName: Windows.Win32.Foundation.PWSTR, GroupName: Windows.Win32.Foundation.PWSTR, Identity: Windows.Win32.Foundation.PWSTR, Invitation: Windows.Win32.Foundation.PWSTR, Addresses: POINTER(Windows.Win32.Networking.WinSock.SOCKET_ADDRESS_LIST_head), appId: Windows.Win32.Foundation.PWSTR, handle: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfExecuteDiagnosis(handle: c_void_p, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCloseIncident(handle: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfDiagnoseIncident(Handle: c_void_p, RootCauseCount: POINTER(UInt32), RootCauses: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RootCauseInfo_head)), dwWait: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfRepairIncident(Handle: c_void_p, RepairEx: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfoEx_head), dwWait: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfCancelIncident(Handle: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NDFAPI.dll')
def NdfGetTraceFile(Handle: c_void_p, TraceFileLocation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
DIAGNOSIS_STATUS = Int32
DS_NOT_IMPLEMENTED: DIAGNOSIS_STATUS = 0
DS_CONFIRMED: DIAGNOSIS_STATUS = 1
DS_REJECTED: DIAGNOSIS_STATUS = 2
DS_INDETERMINATE: DIAGNOSIS_STATUS = 3
DS_DEFERRED: DIAGNOSIS_STATUS = 4
DS_PASSTHROUGH: DIAGNOSIS_STATUS = 5
class DIAG_SOCKADDR(Structure):
    family: UInt16
    data: Windows.Win32.Foundation.CHAR * 126
class DiagnosticsInfo(Structure):
    cost: Int32
    flags: UInt32
class HELPER_ATTRIBUTE(Structure):
    pwszName: Windows.Win32.Foundation.PWSTR
    type: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Boolean: Windows.Win32.Foundation.BOOL
        Char: Byte
        Byte: Byte
        Short: Int16
        Word: UInt16
        Int: Int32
        DWord: UInt32
        Int64: Int64
        UInt64: UInt64
        PWStr: Windows.Win32.Foundation.PWSTR
        Guid: Guid
        LifeTime: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME
        Address: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAG_SOCKADDR
        OctetString: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.OCTET_STRING
class HYPOTHESIS(Structure):
    pwszClassName: Windows.Win32.Foundation.PWSTR
    pwszDescription: Windows.Win32.Foundation.PWSTR
    celt: UInt32
    rgAttributes: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head)
class HelperAttributeInfo(Structure):
    pwszName: Windows.Win32.Foundation.PWSTR
    type: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ATTRIBUTE_TYPE
class HypothesisResult(Structure):
    hypothesis: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS
    pathStatus: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS
class INetDiagExtensibleHelper(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c0b35748-ebf5-11d8-bb-e9-50-50-54-50-30-30')
    @commethod(3)
    def ResolveAttributes(celt: UInt32, rgKeyAttributes: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head), pcelt: POINTER(UInt32), prgMatchValues: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head))) -> Windows.Win32.Foundation.HRESULT: ...
class INetDiagHelper(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c0b35746-ebf5-11d8-bb-e9-50-50-54-50-30-30')
    @commethod(3)
    def Initialize(celt: UInt32, rgAttributes: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDiagnosticsInfo(ppInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DiagnosticsInfo_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetKeyAttributes(pcelt: POINTER(UInt32), pprgAttributes: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def LowHealth(pwszInstanceDescription: Windows.Win32.Foundation.PWSTR, ppwszDescription: POINTER(Windows.Win32.Foundation.PWSTR), pDeferredTime: POINTER(Int32), pStatus: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HighUtilization(pwszInstanceDescription: Windows.Win32.Foundation.PWSTR, ppwszDescription: POINTER(Windows.Win32.Foundation.PWSTR), pDeferredTime: POINTER(Int32), pStatus: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLowerHypotheses(pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDownStreamHypotheses(pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetHigherHypotheses(pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetUpStreamHypotheses(pcelt: POINTER(UInt32), pprgHypotheses: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HYPOTHESIS_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Repair(pInfo: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo_head), pDeferredTime: POINTER(Int32), pStatus: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Validate(problem: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE, pDeferredTime: POINTER(Int32), pStatus: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetRepairInfo(problem: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.PROBLEM_TYPE, pcelt: POINTER(UInt32), ppInfo: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetLifeTime(pLifeTime: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetLifeTime(lifeTime: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.LIFE_TIME) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCacheTime(pCacheTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetAttributes(pcelt: POINTER(UInt32), pprgAttributes: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HELPER_ATTRIBUTE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Cancel() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Cleanup() -> Windows.Win32.Foundation.HRESULT: ...
class INetDiagHelperEx(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('972dab4d-e4e3-4fc6-ae-54-5f-65-cc-de-4a-15')
    @commethod(3)
    def ReconfirmLowHealth(celt: UInt32, pResults: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HypothesisResult_head), ppwszUpdatedDescription: POINTER(Windows.Win32.Foundation.PWSTR), pUpdatedStatus: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.DIAGNOSIS_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetUtilities(pUtilities: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.INetDiagHelperUtilFactory_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReproduceFailure() -> Windows.Win32.Foundation.HRESULT: ...
class INetDiagHelperInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c0b35747-ebf5-11d8-bb-e9-50-50-54-50-30-30')
    @commethod(3)
    def GetAttributeInfo(pcelt: POINTER(UInt32), pprgAttributeInfos: POINTER(POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.HelperAttributeInfo_head))) -> Windows.Win32.Foundation.HRESULT: ...
class INetDiagHelperUtilFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('104613fb-bc57-4178-95-ba-88-80-96-98-35-4a')
    @commethod(3)
    def CreateUtilityInstance(riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class LIFE_TIME(Structure):
    startTime: Windows.Win32.Foundation.FILETIME
    endTime: Windows.Win32.Foundation.FILETIME
class OCTET_STRING(Structure):
    dwLength: UInt32
    lpValue: c_char_p_no
PROBLEM_TYPE = Int32
PT_INVALID: PROBLEM_TYPE = 0
PT_LOW_HEALTH: PROBLEM_TYPE = 1
PT_LOWER_HEALTH: PROBLEM_TYPE = 2
PT_DOWN_STREAM_HEALTH: PROBLEM_TYPE = 4
PT_HIGH_UTILIZATION: PROBLEM_TYPE = 8
PT_HIGHER_UTILIZATION: PROBLEM_TYPE = 16
PT_UP_STREAM_UTILIZATION: PROBLEM_TYPE = 32
REPAIR_RISK = Int32
RR_NOROLLBACK: REPAIR_RISK = 0
RR_ROLLBACK: REPAIR_RISK = 1
RR_NORISK: REPAIR_RISK = 2
REPAIR_SCOPE = Int32
RS_SYSTEM: REPAIR_SCOPE = 0
RS_USER: REPAIR_SCOPE = 1
RS_APPLICATION: REPAIR_SCOPE = 2
RS_PROCESS: REPAIR_SCOPE = 3
REPAIR_STATUS = Int32
RS_NOT_IMPLEMENTED: REPAIR_STATUS = 0
RS_REPAIRED: REPAIR_STATUS = 1
RS_UNREPAIRED: REPAIR_STATUS = 2
RS_DEFERRED: REPAIR_STATUS = 3
RS_USER_ACTION: REPAIR_STATUS = 4
class RepairInfo(Structure):
    guid: Guid
    pwszClassName: Windows.Win32.Foundation.PWSTR
    pwszDescription: Windows.Win32.Foundation.PWSTR
    sidType: UInt32
    cost: Int32
    flags: UInt32
    scope: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_SCOPE
    risk: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.REPAIR_RISK
    UiInfo: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.UiInfo
    rootCauseIndex: Int32
class RepairInfoEx(Structure):
    repair: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfo
    repairRank: UInt16
class RootCauseInfo(Structure):
    pwszDescription: Windows.Win32.Foundation.PWSTR
    rootCauseID: Guid
    rootCauseFlags: UInt32
    networkInterfaceID: Guid
    pRepairs: POINTER(Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.RepairInfoEx_head)
    repairCount: UInt16
class ShellCommandInfo(Structure):
    pwszOperation: Windows.Win32.Foundation.PWSTR
    pwszFile: Windows.Win32.Foundation.PWSTR
    pwszParameters: Windows.Win32.Foundation.PWSTR
    pwszDirectory: Windows.Win32.Foundation.PWSTR
    nShowCmd: UInt32
UI_INFO_TYPE = Int32
UIT_INVALID: UI_INFO_TYPE = 0
UIT_NONE: UI_INFO_TYPE = 1
UIT_SHELL_COMMAND: UI_INFO_TYPE = 2
UIT_HELP_PANE: UI_INFO_TYPE = 3
UIT_DUI: UI_INFO_TYPE = 4
class UiInfo(Structure):
    type: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.UI_INFO_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        pwzNull: Windows.Win32.Foundation.PWSTR
        ShellInfo: Windows.Win32.NetworkManagement.NetworkDiagnosticsFramework.ShellCommandInfo
        pwzHelpUrl: Windows.Win32.Foundation.PWSTR
        pwzDui: Windows.Win32.Foundation.PWSTR
make_head(_module, 'DIAG_SOCKADDR')
make_head(_module, 'DiagnosticsInfo')
make_head(_module, 'HELPER_ATTRIBUTE')
make_head(_module, 'HYPOTHESIS')
make_head(_module, 'HelperAttributeInfo')
make_head(_module, 'HypothesisResult')
make_head(_module, 'INetDiagExtensibleHelper')
make_head(_module, 'INetDiagHelper')
make_head(_module, 'INetDiagHelperEx')
make_head(_module, 'INetDiagHelperInfo')
make_head(_module, 'INetDiagHelperUtilFactory')
make_head(_module, 'LIFE_TIME')
make_head(_module, 'OCTET_STRING')
make_head(_module, 'RepairInfo')
make_head(_module, 'RepairInfoEx')
make_head(_module, 'RootCauseInfo')
make_head(_module, 'ShellCommandInfo')
make_head(_module, 'UiInfo')
__all__ = [
    "ATTRIBUTE_TYPE",
    "AT_BOOLEAN",
    "AT_GUID",
    "AT_INT16",
    "AT_INT32",
    "AT_INT64",
    "AT_INT8",
    "AT_INVALID",
    "AT_LIFE_TIME",
    "AT_OCTET_STRING",
    "AT_SOCKADDR",
    "AT_STRING",
    "AT_UINT16",
    "AT_UINT32",
    "AT_UINT64",
    "AT_UINT8",
    "DF_IMPERSONATION",
    "DF_TRACELESS",
    "DIAGNOSIS_STATUS",
    "DIAG_SOCKADDR",
    "DS_CONFIRMED",
    "DS_DEFERRED",
    "DS_INDETERMINATE",
    "DS_NOT_IMPLEMENTED",
    "DS_PASSTHROUGH",
    "DS_REJECTED",
    "DiagnosticsInfo",
    "HELPER_ATTRIBUTE",
    "HYPOTHESIS",
    "HelperAttributeInfo",
    "HypothesisResult",
    "INetDiagExtensibleHelper",
    "INetDiagHelper",
    "INetDiagHelperEx",
    "INetDiagHelperInfo",
    "INetDiagHelperUtilFactory",
    "LIFE_TIME",
    "NDF_ADD_CAPTURE_TRACE",
    "NDF_APPLY_INCLUSION_LIST_FILTER",
    "NDF_ERROR_START",
    "NDF_E_BAD_PARAM",
    "NDF_E_CANCELLED",
    "NDF_E_DISABLED",
    "NDF_E_LENGTH_EXCEEDED",
    "NDF_E_NOHELPERCLASS",
    "NDF_E_PROBLEM_PRESENT",
    "NDF_E_UNKNOWN",
    "NDF_E_VALIDATION",
    "NDF_INBOUND_FLAG_EDGETRAVERSAL",
    "NDF_INBOUND_FLAG_HEALTHCHECK",
    "NdfCancelIncident",
    "NdfCloseIncident",
    "NdfCreateConnectivityIncident",
    "NdfCreateDNSIncident",
    "NdfCreateGroupingIncident",
    "NdfCreateIncident",
    "NdfCreateNetConnectionIncident",
    "NdfCreatePnrpIncident",
    "NdfCreateSharingIncident",
    "NdfCreateWebIncident",
    "NdfCreateWebIncidentEx",
    "NdfCreateWinSockIncident",
    "NdfDiagnoseIncident",
    "NdfExecuteDiagnosis",
    "NdfGetTraceFile",
    "NdfRepairIncident",
    "OCTET_STRING",
    "PROBLEM_TYPE",
    "PT_DOWN_STREAM_HEALTH",
    "PT_HIGHER_UTILIZATION",
    "PT_HIGH_UTILIZATION",
    "PT_INVALID",
    "PT_LOWER_HEALTH",
    "PT_LOW_HEALTH",
    "PT_UP_STREAM_UTILIZATION",
    "RCF_ISCONFIRMED",
    "RCF_ISLEAF",
    "RCF_ISTHIRDPARTY",
    "REPAIR_RISK",
    "REPAIR_SCOPE",
    "REPAIR_STATUS",
    "RF_CONTACT_ADMIN",
    "RF_INFORMATION_ONLY",
    "RF_REPRO",
    "RF_RESERVED",
    "RF_RESERVED_CA",
    "RF_RESERVED_LNI",
    "RF_SHOW_EVENTS",
    "RF_UI_ONLY",
    "RF_USER_ACTION",
    "RF_USER_CONFIRMATION",
    "RF_VALIDATE_HELPTOPIC",
    "RF_WORKAROUND",
    "RR_NORISK",
    "RR_NOROLLBACK",
    "RR_ROLLBACK",
    "RS_APPLICATION",
    "RS_DEFERRED",
    "RS_NOT_IMPLEMENTED",
    "RS_PROCESS",
    "RS_REPAIRED",
    "RS_SYSTEM",
    "RS_UNREPAIRED",
    "RS_USER",
    "RS_USER_ACTION",
    "RepairInfo",
    "RepairInfoEx",
    "RootCauseInfo",
    "ShellCommandInfo",
    "UIT_DUI",
    "UIT_HELP_PANE",
    "UIT_INVALID",
    "UIT_NONE",
    "UIT_SHELL_COMMAND",
    "UI_INFO_TYPE",
    "UiInfo",
]
_arch_optional = [
]