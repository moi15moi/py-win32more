from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Performance.HardwareCounterProfiling
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_EnableThreadProfiling():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt64,POINTER(win32more.Foundation.HANDLE))(('EnableThreadProfiling', windll['KERNEL32.dll']), ((1, 'ThreadHandle'),(1, 'Flags'),(1, 'HardwareCounters'),(1, 'PerformanceDataHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DisableThreadProfiling():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('DisableThreadProfiling', windll['KERNEL32.dll']), ((1, 'PerformanceDataHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryThreadProfiling():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOLEAN))(('QueryThreadProfiling', windll['KERNEL32.dll']), ((1, 'ThreadHandle'),(1, 'Enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadThreadProfilingData():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.System.Performance.HardwareCounterProfiling.PERFORMANCE_DATA_head))(('ReadThreadProfilingData', windll['KERNEL32.dll']), ((1, 'PerformanceDataHandle'),(1, 'Flags'),(1, 'PerformanceData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HARDWARE_COUNTER_DATA_head():
    class HARDWARE_COUNTER_DATA(Structure):
        pass
    return HARDWARE_COUNTER_DATA
def _define_HARDWARE_COUNTER_DATA():
    HARDWARE_COUNTER_DATA = win32more.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_DATA_head
    HARDWARE_COUNTER_DATA._fields_ = [
        ('Type', win32more.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_TYPE),
        ('Reserved', UInt32),
        ('Value', UInt64),
    ]
    return HARDWARE_COUNTER_DATA
HARDWARE_COUNTER_TYPE = Int32
HARDWARE_COUNTER_TYPE_PMCCounter = 0
HARDWARE_COUNTER_TYPE_MaxHardwareCounterType = 1
def _define_PERFORMANCE_DATA_head():
    class PERFORMANCE_DATA(Structure):
        pass
    return PERFORMANCE_DATA
def _define_PERFORMANCE_DATA():
    PERFORMANCE_DATA = win32more.System.Performance.HardwareCounterProfiling.PERFORMANCE_DATA_head
    PERFORMANCE_DATA._fields_ = [
        ('Size', UInt16),
        ('Version', Byte),
        ('HwCountersCount', Byte),
        ('ContextSwitchCount', UInt32),
        ('WaitReasonBitMap', UInt64),
        ('CycleTime', UInt64),
        ('RetryCount', UInt32),
        ('Reserved', UInt32),
        ('HwCounters', win32more.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_DATA * 16),
    ]
    return PERFORMANCE_DATA
__all__ = [
    "DisableThreadProfiling",
    "EnableThreadProfiling",
    "HARDWARE_COUNTER_DATA",
    "HARDWARE_COUNTER_TYPE",
    "HARDWARE_COUNTER_TYPE_MaxHardwareCounterType",
    "HARDWARE_COUNTER_TYPE_PMCCounter",
    "PERFORMANCE_DATA",
    "QueryThreadProfiling",
    "ReadThreadProfilingData",
]