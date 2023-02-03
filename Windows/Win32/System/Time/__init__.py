from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Time
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
wszW32TimeRegKeyTimeProviders: String = 'System\\CurrentControlSet\\Services\\W32Time\\TimeProviders'
wszW32TimeRegKeyPolicyTimeProviders: String = 'Software\\Policies\\Microsoft\\W32Time\\TimeProviders'
wszW32TimeRegValueEnabled: String = 'Enabled'
wszW32TimeRegValueDllName: String = 'DllName'
wszW32TimeRegValueInputProvider: String = 'InputProvider'
wszW32TimeRegValueMetaDataProvider: String = 'MetaDataProvider'
TSF_Hardware: UInt32 = 1
TSF_Authenticated: UInt32 = 2
TSF_IPv6: UInt32 = 4
TSF_SignatureAuthenticated: UInt32 = 8
TIME_ZONE_ID_INVALID: UInt32 = 4294967295
@winfunctype('KERNEL32.dll')
def SystemTimeToTzSpecificLocalTime(lpTimeZoneInformation: POINTER(Windows.Win32.System.Time.TIME_ZONE_INFORMATION_head), lpUniversalTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head), lpLocalTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TzSpecificLocalTimeToSystemTime(lpTimeZoneInformation: POINTER(Windows.Win32.System.Time.TIME_ZONE_INFORMATION_head), lpLocalTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head), lpUniversalTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FileTimeToSystemTime(lpFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head), lpSystemTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SystemTimeToFileTime(lpSystemTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head), lpFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetTimeZoneInformation(lpTimeZoneInformation: POINTER(Windows.Win32.System.Time.TIME_ZONE_INFORMATION_head)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetTimeZoneInformation(lpTimeZoneInformation: POINTER(Windows.Win32.System.Time.TIME_ZONE_INFORMATION_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDynamicTimeZoneInformation(lpTimeZoneInformation: POINTER(Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDynamicTimeZoneInformation(pTimeZoneInformation: POINTER(Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetTimeZoneInformationForYear(wYear: UInt16, pdtzi: POINTER(Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head), ptzi: POINTER(Windows.Win32.System.Time.TIME_ZONE_INFORMATION_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def EnumDynamicTimeZoneInformation(dwIndex: UInt32, lpTimeZoneInformation: POINTER(Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def GetDynamicTimeZoneInformationEffectiveYears(lpTimeZoneInformation: POINTER(Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head), FirstYear: POINTER(UInt32), LastYear: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SystemTimeToTzSpecificLocalTimeEx(lpTimeZoneInformation: POINTER(Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head), lpUniversalTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head), lpLocalTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TzSpecificLocalTimeToSystemTimeEx(lpTimeZoneInformation: POINTER(Windows.Win32.System.Time.DYNAMIC_TIME_ZONE_INFORMATION_head), lpLocalTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head), lpUniversalTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalFileTimeToLocalSystemTime(timeZoneInformation: POINTER(Windows.Win32.System.Time.TIME_ZONE_INFORMATION_head), localFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head), localSystemTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalSystemTimeToLocalFileTime(timeZoneInformation: POINTER(Windows.Win32.System.Time.TIME_ZONE_INFORMATION_head), localSystemTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head), localFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.BOOL: ...
class DYNAMIC_TIME_ZONE_INFORMATION(Structure):
    Bias: Int32
    StandardName: Char * 32
    StandardDate: Windows.Win32.Foundation.SYSTEMTIME
    StandardBias: Int32
    DaylightName: Char * 32
    DaylightDate: Windows.Win32.Foundation.SYSTEMTIME
    DaylightBias: Int32
    TimeZoneKeyName: Char * 128
    DynamicDaylightTimeDisabled: Windows.Win32.Foundation.BOOLEAN
class TIME_ZONE_INFORMATION(Structure):
    Bias: Int32
    StandardName: Char * 32
    StandardDate: Windows.Win32.Foundation.SYSTEMTIME
    StandardBias: Int32
    DaylightName: Char * 32
    DaylightDate: Windows.Win32.Foundation.SYSTEMTIME
    DaylightBias: Int32
make_head(_module, 'DYNAMIC_TIME_ZONE_INFORMATION')
make_head(_module, 'TIME_ZONE_INFORMATION')
__all__ = [
    "DYNAMIC_TIME_ZONE_INFORMATION",
    "EnumDynamicTimeZoneInformation",
    "FileTimeToSystemTime",
    "GetDynamicTimeZoneInformation",
    "GetDynamicTimeZoneInformationEffectiveYears",
    "GetTimeZoneInformation",
    "GetTimeZoneInformationForYear",
    "LocalFileTimeToLocalSystemTime",
    "LocalSystemTimeToLocalFileTime",
    "SetDynamicTimeZoneInformation",
    "SetTimeZoneInformation",
    "SystemTimeToFileTime",
    "SystemTimeToTzSpecificLocalTime",
    "SystemTimeToTzSpecificLocalTimeEx",
    "TIME_ZONE_ID_INVALID",
    "TIME_ZONE_INFORMATION",
    "TSF_Authenticated",
    "TSF_Hardware",
    "TSF_IPv6",
    "TSF_SignatureAuthenticated",
    "TzSpecificLocalTimeToSystemTime",
    "TzSpecificLocalTimeToSystemTimeEx",
    "wszW32TimeRegKeyPolicyTimeProviders",
    "wszW32TimeRegKeyTimeProviders",
    "wszW32TimeRegValueDllName",
    "wszW32TimeRegValueEnabled",
    "wszW32TimeRegValueInputProvider",
    "wszW32TimeRegValueMetaDataProvider",
]
_arch_optional = [
]