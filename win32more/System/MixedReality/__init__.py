from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.System.MixedReality
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
def _define_PERCEPTIONFIELD_StateStream_TimeStamps():
    return Guid('aa886119-f32f-49bf-92-ca-f9-dd-f7-84-d2-97')
def _define_PERCEPTION_PAYLOAD_FIELD_head():
    class PERCEPTION_PAYLOAD_FIELD(Structure):
        pass
    return PERCEPTION_PAYLOAD_FIELD
def _define_PERCEPTION_PAYLOAD_FIELD():
    PERCEPTION_PAYLOAD_FIELD = win32more.System.MixedReality.PERCEPTION_PAYLOAD_FIELD_head
    PERCEPTION_PAYLOAD_FIELD._fields_ = [
        ('FieldId', Guid),
        ('OffsetInBytes', UInt32),
        ('SizeInBytes', UInt32),
    ]
    return PERCEPTION_PAYLOAD_FIELD
def _define_PERCEPTION_STATE_STREAM_TIMESTAMPS_head():
    class PERCEPTION_STATE_STREAM_TIMESTAMPS(Structure):
        pass
    return PERCEPTION_STATE_STREAM_TIMESTAMPS
def _define_PERCEPTION_STATE_STREAM_TIMESTAMPS():
    PERCEPTION_STATE_STREAM_TIMESTAMPS = win32more.System.MixedReality.PERCEPTION_STATE_STREAM_TIMESTAMPS_head
    PERCEPTION_STATE_STREAM_TIMESTAMPS._fields_ = [
        ('InputTimestampInQpcCounts', Int64),
        ('AvailableTimestampInQpcCounts', Int64),
    ]
    return PERCEPTION_STATE_STREAM_TIMESTAMPS
__all__ = [
    "PERCEPTIONFIELD_StateStream_TimeStamps",
    "PERCEPTION_PAYLOAD_FIELD",
    "PERCEPTION_STATE_STREAM_TIMESTAMPS",
]