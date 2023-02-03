from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.TpmBaseServices
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
TBS_CONTEXT_VERSION_ONE: UInt32 = 1
TBS_SUCCESS: UInt32 = 0
TBS_OWNERAUTH_TYPE_FULL: UInt32 = 1
TBS_OWNERAUTH_TYPE_ADMIN: UInt32 = 2
TBS_OWNERAUTH_TYPE_USER: UInt32 = 3
TBS_OWNERAUTH_TYPE_ENDORSEMENT: UInt32 = 4
TBS_OWNERAUTH_TYPE_ENDORSEMENT_20: UInt32 = 12
TBS_OWNERAUTH_TYPE_STORAGE_20: UInt32 = 13
TBS_CONTEXT_VERSION_TWO: UInt32 = 2
TPM_WNF_INFO_CLEAR_SUCCESSFUL: UInt32 = 1
TPM_WNF_INFO_OWNERSHIP_SUCCESSFUL: UInt32 = 2
TPM_WNF_INFO_NO_REBOOT_REQUIRED: UInt32 = 1
TPM_VERSION_UNKNOWN: UInt32 = 0
TPM_VERSION_12: UInt32 = 1
TPM_VERSION_20: UInt32 = 2
TPM_IFTYPE_UNKNOWN: UInt32 = 0
TPM_IFTYPE_1: UInt32 = 1
TPM_IFTYPE_TRUSTZONE: UInt32 = 2
TPM_IFTYPE_HW: UInt32 = 3
TPM_IFTYPE_EMULATOR: UInt32 = 4
TPM_IFTYPE_SPB: UInt32 = 5
TBS_TCGLOG_SRTM_CURRENT: UInt32 = 0
TBS_TCGLOG_DRTM_CURRENT: UInt32 = 1
TBS_TCGLOG_SRTM_BOOT: UInt32 = 2
TBS_TCGLOG_SRTM_RESUME: UInt32 = 3
TBS_TCGLOG_DRTM_BOOT: UInt32 = 4
TBS_TCGLOG_DRTM_RESUME: UInt32 = 5
@winfunctype('tbs.dll')
def Tbsi_Context_Create(pContextParams: POINTER(Windows.Win32.System.TpmBaseServices.TBS_CONTEXT_PARAMS_head), phContext: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsip_Context_Close(hContext: c_void_p) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsip_Submit_Command(hContext: c_void_p, Locality: Windows.Win32.System.TpmBaseServices.TBS_COMMAND_LOCALITY, Priority: Windows.Win32.System.TpmBaseServices.TBS_COMMAND_PRIORITY, pabCommand: c_char_p_no, cbCommand: UInt32, pabResult: c_char_p_no, pcbResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsip_Cancel_Commands(hContext: c_void_p) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Physical_Presence_Command(hContext: c_void_p, pabInput: c_char_p_no, cbInput: UInt32, pabOutput: c_char_p_no, pcbOutput: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Get_TCG_Log(hContext: c_void_p, pOutputBuf: c_char_p_no, pOutputBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_GetDeviceInfo(Size: UInt32, Info: c_void_p) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Get_OwnerAuth(hContext: c_void_p, ownerauthType: UInt32, pOutputBuf: c_char_p_no, pOutputBufLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Revoke_Attestation() -> UInt32: ...
@winfunctype('tbs.dll')
def GetDeviceID(pbWindowsAIK: c_char_p_no, cbWindowsAIK: UInt32, pcbResult: POINTER(UInt32), pfProtectedByTPM: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('tbs.dll')
def GetDeviceIDString(pszWindowsAIK: Windows.Win32.Foundation.PWSTR, cchWindowsAIK: UInt32, pcchResult: POINTER(UInt32), pfProtectedByTPM: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('tbs.dll')
def Tbsi_Create_Windows_Key(keyHandle: UInt32) -> UInt32: ...
@winfunctype('tbs.dll')
def Tbsi_Get_TCG_Log_Ex(logType: UInt32, pbOutput: c_char_p_no, pcbOutput: POINTER(UInt32)) -> UInt32: ...
TBS_COMMAND_LOCALITY = UInt32
TBS_COMMAND_LOCALITY_ZERO: TBS_COMMAND_LOCALITY = 0
TBS_COMMAND_LOCALITY_ONE: TBS_COMMAND_LOCALITY = 1
TBS_COMMAND_LOCALITY_TWO: TBS_COMMAND_LOCALITY = 2
TBS_COMMAND_LOCALITY_THREE: TBS_COMMAND_LOCALITY = 3
TBS_COMMAND_LOCALITY_FOUR: TBS_COMMAND_LOCALITY = 4
TBS_COMMAND_PRIORITY = UInt32
TBS_COMMAND_PRIORITY_LOW: TBS_COMMAND_PRIORITY = 100
TBS_COMMAND_PRIORITY_NORMAL: TBS_COMMAND_PRIORITY = 200
TBS_COMMAND_PRIORITY_SYSTEM: TBS_COMMAND_PRIORITY = 400
TBS_COMMAND_PRIORITY_HIGH: TBS_COMMAND_PRIORITY = 300
TBS_COMMAND_PRIORITY_MAX: TBS_COMMAND_PRIORITY = 2147483648
class TBS_CONTEXT_PARAMS(Structure):
    version: UInt32
class TBS_CONTEXT_PARAMS2(Structure):
    version: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        asUINT32: UInt32
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
class TPM_DEVICE_INFO(Structure):
    structVersion: UInt32
    tpmVersion: UInt32
    tpmInterfaceType: UInt32
    tpmImpRevision: UInt32
class TPM_WNF_PROVISIONING(Structure):
    status: UInt32
    message: Byte * 28
make_head(_module, 'TBS_CONTEXT_PARAMS')
make_head(_module, 'TBS_CONTEXT_PARAMS2')
make_head(_module, 'TPM_DEVICE_INFO')
make_head(_module, 'TPM_WNF_PROVISIONING')
__all__ = [
    "GetDeviceID",
    "GetDeviceIDString",
    "TBS_COMMAND_LOCALITY",
    "TBS_COMMAND_LOCALITY_FOUR",
    "TBS_COMMAND_LOCALITY_ONE",
    "TBS_COMMAND_LOCALITY_THREE",
    "TBS_COMMAND_LOCALITY_TWO",
    "TBS_COMMAND_LOCALITY_ZERO",
    "TBS_COMMAND_PRIORITY",
    "TBS_COMMAND_PRIORITY_HIGH",
    "TBS_COMMAND_PRIORITY_LOW",
    "TBS_COMMAND_PRIORITY_MAX",
    "TBS_COMMAND_PRIORITY_NORMAL",
    "TBS_COMMAND_PRIORITY_SYSTEM",
    "TBS_CONTEXT_PARAMS",
    "TBS_CONTEXT_PARAMS2",
    "TBS_CONTEXT_VERSION_ONE",
    "TBS_CONTEXT_VERSION_TWO",
    "TBS_OWNERAUTH_TYPE_ADMIN",
    "TBS_OWNERAUTH_TYPE_ENDORSEMENT",
    "TBS_OWNERAUTH_TYPE_ENDORSEMENT_20",
    "TBS_OWNERAUTH_TYPE_FULL",
    "TBS_OWNERAUTH_TYPE_STORAGE_20",
    "TBS_OWNERAUTH_TYPE_USER",
    "TBS_SUCCESS",
    "TBS_TCGLOG_DRTM_BOOT",
    "TBS_TCGLOG_DRTM_CURRENT",
    "TBS_TCGLOG_DRTM_RESUME",
    "TBS_TCGLOG_SRTM_BOOT",
    "TBS_TCGLOG_SRTM_CURRENT",
    "TBS_TCGLOG_SRTM_RESUME",
    "TPM_DEVICE_INFO",
    "TPM_IFTYPE_1",
    "TPM_IFTYPE_EMULATOR",
    "TPM_IFTYPE_HW",
    "TPM_IFTYPE_SPB",
    "TPM_IFTYPE_TRUSTZONE",
    "TPM_IFTYPE_UNKNOWN",
    "TPM_VERSION_12",
    "TPM_VERSION_20",
    "TPM_VERSION_UNKNOWN",
    "TPM_WNF_INFO_CLEAR_SUCCESSFUL",
    "TPM_WNF_INFO_NO_REBOOT_REQUIRED",
    "TPM_WNF_INFO_OWNERSHIP_SUCCESSFUL",
    "TPM_WNF_PROVISIONING",
    "Tbsi_Context_Create",
    "Tbsi_Create_Windows_Key",
    "Tbsi_GetDeviceInfo",
    "Tbsi_Get_OwnerAuth",
    "Tbsi_Get_TCG_Log",
    "Tbsi_Get_TCG_Log_Ex",
    "Tbsi_Physical_Presence_Command",
    "Tbsi_Revoke_Attestation",
    "Tbsip_Cancel_Commands",
    "Tbsip_Context_Close",
    "Tbsip_Submit_Command",
]
_arch_optional = [
]