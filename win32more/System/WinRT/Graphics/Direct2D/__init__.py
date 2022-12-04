from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Direct2D
import win32more.System.Com
import win32more.System.WinRT.Graphics.Direct2D
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
GRAPHICS_EFFECT_PROPERTY_MAPPING = Int32
GRAPHICS_EFFECT_PROPERTY_MAPPING_UNKNOWN = 0
GRAPHICS_EFFECT_PROPERTY_MAPPING_DIRECT = 1
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORX = 2
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORY = 3
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORZ = 4
GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORW = 5
GRAPHICS_EFFECT_PROPERTY_MAPPING_RECT_TO_VECTOR4 = 6
GRAPHICS_EFFECT_PROPERTY_MAPPING_RADIANS_TO_DEGREES = 7
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLORMATRIX_ALPHA_MODE = 8
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR3 = 9
GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR4 = 10
def _define_IGeometrySource2DInterop_head():
    class IGeometrySource2DInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('0657af73-53fd-47cf-84-ff-c8-49-2d-2a-80-a3')
    return IGeometrySource2DInterop
def _define_IGeometrySource2DInterop():
    IGeometrySource2DInterop = win32more.System.WinRT.Graphics.Direct2D.IGeometrySource2DInterop_head
    IGeometrySource2DInterop.GetGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1Geometry_head))(3, 'GetGeometry', ((1, 'value'),)))
    IGeometrySource2DInterop.TryGetGeometryUsingFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Factory_head,POINTER(win32more.Graphics.Direct2D.ID2D1Geometry_head))(4, 'TryGetGeometryUsingFactory', ((1, 'factory'),(1, 'value'),)))
    win32more.System.Com.IUnknown
    return IGeometrySource2DInterop
def _define_IGraphicsEffectD2D1Interop_head():
    class IGraphicsEffectD2D1Interop(win32more.System.Com.IUnknown_head):
        Guid = Guid('2fc57384-a068-44d7-a3-31-30-98-2f-cf-71-77')
    return IGraphicsEffectD2D1Interop
def _define_IGraphicsEffectD2D1Interop():
    IGraphicsEffectD2D1Interop = win32more.System.WinRT.Graphics.Direct2D.IGraphicsEffectD2D1Interop_head
    IGraphicsEffectD2D1Interop.GetEffectId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetEffectId', ((1, 'id'),)))
    IGraphicsEffectD2D1Interop.GetNamedPropertyMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.System.WinRT.Graphics.Direct2D.GRAPHICS_EFFECT_PROPERTY_MAPPING))(4, 'GetNamedPropertyMapping', ((1, 'name'),(1, 'index'),(1, 'mapping'),)))
    IGraphicsEffectD2D1Interop.GetPropertyCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetPropertyCount', ((1, 'count'),)))
    IGraphicsEffectD2D1Interop.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(MissingType))(6, 'GetProperty', ((1, 'index'),(1, 'value'),)))
    IGraphicsEffectD2D1Interop.GetSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(MissingType))(7, 'GetSource', ((1, 'index'),(1, 'source'),)))
    IGraphicsEffectD2D1Interop.GetSourceCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'GetSourceCount', ((1, 'count'),)))
    win32more.System.Com.IUnknown
    return IGraphicsEffectD2D1Interop
__all__ = [
    "GRAPHICS_EFFECT_PROPERTY_MAPPING",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_COLORMATRIX_ALPHA_MODE",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR3",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_COLOR_TO_VECTOR4",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_DIRECT",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_RADIANS_TO_DEGREES",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_RECT_TO_VECTOR4",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_UNKNOWN",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORW",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORX",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORY",
    "GRAPHICS_EFFECT_PROPERTY_MAPPING_VECTORZ",
    "IGeometrySource2DInterop",
    "IGraphicsEffectD2D1Interop",
]