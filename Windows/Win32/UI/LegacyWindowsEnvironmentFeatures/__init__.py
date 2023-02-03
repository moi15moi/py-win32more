from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Ole
import Windows.Win32.System.Registry
import Windows.Win32.UI.LegacyWindowsEnvironmentFeatures
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
EVCCBF_LASTNOTIFICATION: UInt32 = 1
STATEBITS_FLAT: UInt32 = 1
REC_S_IDIDTHEUPDATES: Windows.Win32.Foundation.HRESULT = 266240
REC_S_NOTCOMPLETE: Windows.Win32.Foundation.HRESULT = 266241
REC_S_NOTCOMPLETEBUTPROPAGATE: Windows.Win32.Foundation.HRESULT = 266242
REC_E_ABORTED: Windows.Win32.Foundation.HRESULT = -2147217408
REC_E_NOCALLBACK: Windows.Win32.Foundation.HRESULT = -2147217407
REC_E_NORESIDUES: Windows.Win32.Foundation.HRESULT = -2147217406
REC_E_TOODIFFERENT: Windows.Win32.Foundation.HRESULT = -2147217405
REC_E_INEEDTODOTHEUPDATES: Windows.Win32.Foundation.HRESULT = -2147217404
EMPTY_VOLUME_CACHE_FLAGS = UInt32
EVCF_HASSETTINGS: EMPTY_VOLUME_CACHE_FLAGS = 1
EVCF_ENABLEBYDEFAULT: EMPTY_VOLUME_CACHE_FLAGS = 2
EVCF_REMOVEFROMLIST: EMPTY_VOLUME_CACHE_FLAGS = 4
EVCF_ENABLEBYDEFAULT_AUTO: EMPTY_VOLUME_CACHE_FLAGS = 8
EVCF_DONTSHOWIFZERO: EMPTY_VOLUME_CACHE_FLAGS = 16
EVCF_SETTINGSMODE: EMPTY_VOLUME_CACHE_FLAGS = 32
EVCF_OUTOFDISKSPACE: EMPTY_VOLUME_CACHE_FLAGS = 64
EVCF_USERCONSENTOBTAINED: EMPTY_VOLUME_CACHE_FLAGS = 128
EVCF_SYSTEMAUTORUN: EMPTY_VOLUME_CACHE_FLAGS = 256
class IADesktopP2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b22754e2-4574-11d1-98-88-00-60-97-de-ac-f9')
    @commethod(3)
    def ReReadWallpaper() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetADObjectFlags(pdwFlags: POINTER(UInt32), dwMask: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateAllDesktopSubscriptions() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def MakeDynamicChanges(pOleObj: Windows.Win32.System.Ole.IOleObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IActiveDesktopP(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('52502ee0-ec80-11d0-89-ab-00-c0-4f-c2-97-2d')
    @commethod(3)
    def SetSafeMode(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnsureUpdateHTML() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetScheme(pwszSchemeName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetScheme(pwszSchemeName: Windows.Win32.Foundation.PWSTR, pdwcchBuffer: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IBriefcaseInitiator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('99180164-da16-101a-93-5c-44-45-53-54-00-00')
    @commethod(3)
    def IsMonikerInBriefcase(pmk: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
class IEmptyVolumeCache(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8fce5227-04da-11d1-a0-04-00-80-5f-8a-be-06')
    @commethod(3)
    def Initialize(hkRegKey: Windows.Win32.System.Registry.HKEY, pcwszVolume: Windows.Win32.Foundation.PWSTR, ppwszDisplayName: POINTER(Windows.Win32.Foundation.PWSTR), ppwszDescription: POINTER(Windows.Win32.Foundation.PWSTR), pdwFlags: POINTER(Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSpaceUsed(pdwlSpaceUsed: POINTER(UInt64), picb: Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCacheCallBack_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Purge(dwlSpaceToFree: UInt64, picb: Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCacheCallBack_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ShowProperties(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Deactivate(pdwFlags: POINTER(Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
class IEmptyVolumeCache2(c_void_p):
    extends: Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.IEmptyVolumeCache
    Guid = Guid('02b7e3ba-4db3-11d2-b2-d9-00-c0-4f-8e-ec-8c')
    @commethod(8)
    def InitializeEx(hkRegKey: Windows.Win32.System.Registry.HKEY, pcwszVolume: Windows.Win32.Foundation.PWSTR, pcwszKeyName: Windows.Win32.Foundation.PWSTR, ppwszDisplayName: POINTER(Windows.Win32.Foundation.PWSTR), ppwszDescription: POINTER(Windows.Win32.Foundation.PWSTR), ppwszBtnText: POINTER(Windows.Win32.Foundation.PWSTR), pdwFlags: POINTER(Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.EMPTY_VOLUME_CACHE_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
class IEmptyVolumeCacheCallBack(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6e793361-73c6-11d0-84-69-00-aa-00-44-29-01')
    @commethod(3)
    def ScanProgress(dwlSpaceUsed: UInt64, dwFlags: UInt32, pcwszStatus: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PurgeProgress(dwlSpaceFreed: UInt64, dwlSpaceToFree: UInt64, dwFlags: UInt32, pcwszStatus: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IReconcilableObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('99180162-da16-101a-93-5c-44-45-53-54-00-00')
    @commethod(3)
    def Reconcile(pInitiator: Windows.Win32.UI.LegacyWindowsEnvironmentFeatures.IReconcileInitiator_head, dwFlags: UInt32, hwndOwner: Windows.Win32.Foundation.HWND, hwndProgressFeedback: Windows.Win32.Foundation.HWND, ulcInput: UInt32, rgpmkOtherInput: POINTER(Windows.Win32.System.Com.IMoniker_head), plOutIndex: POINTER(Int32), pstgNewResidues: Windows.Win32.System.Com.StructuredStorage.IStorage_head, pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgressFeedbackMaxEstimate(pulProgressMax: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IReconcileInitiator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('99180161-da16-101a-93-5c-44-45-53-54-00-00')
    @commethod(3)
    def SetAbortCallback(punkForAbort: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetProgressFeedback(ulProgress: UInt32, ulProgressMax: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
RECONCILEF = Int32
RECONCILEF_MAYBOTHERUSER: RECONCILEF = 1
RECONCILEF_FEEDBACKWINDOWVALID: RECONCILEF = 2
RECONCILEF_NORESIDUESOK: RECONCILEF = 4
RECONCILEF_OMITSELFRESIDUE: RECONCILEF = 8
RECONCILEF_RESUMERECONCILIATION: RECONCILEF = 16
RECONCILEF_YOUMAYDOTHEUPDATES: RECONCILEF = 32
RECONCILEF_ONLYYOUWERECHANGED: RECONCILEF = 64
ALL_RECONCILE_FLAGS: RECONCILEF = 127
make_head(_module, 'IADesktopP2')
make_head(_module, 'IActiveDesktopP')
make_head(_module, 'IBriefcaseInitiator')
make_head(_module, 'IEmptyVolumeCache')
make_head(_module, 'IEmptyVolumeCache2')
make_head(_module, 'IEmptyVolumeCacheCallBack')
make_head(_module, 'IReconcilableObject')
make_head(_module, 'IReconcileInitiator')
__all__ = [
    "ALL_RECONCILE_FLAGS",
    "EMPTY_VOLUME_CACHE_FLAGS",
    "EVCCBF_LASTNOTIFICATION",
    "EVCF_DONTSHOWIFZERO",
    "EVCF_ENABLEBYDEFAULT",
    "EVCF_ENABLEBYDEFAULT_AUTO",
    "EVCF_HASSETTINGS",
    "EVCF_OUTOFDISKSPACE",
    "EVCF_REMOVEFROMLIST",
    "EVCF_SETTINGSMODE",
    "EVCF_SYSTEMAUTORUN",
    "EVCF_USERCONSENTOBTAINED",
    "IADesktopP2",
    "IActiveDesktopP",
    "IBriefcaseInitiator",
    "IEmptyVolumeCache",
    "IEmptyVolumeCache2",
    "IEmptyVolumeCacheCallBack",
    "IReconcilableObject",
    "IReconcileInitiator",
    "RECONCILEF",
    "RECONCILEF_FEEDBACKWINDOWVALID",
    "RECONCILEF_MAYBOTHERUSER",
    "RECONCILEF_NORESIDUESOK",
    "RECONCILEF_OMITSELFRESIDUE",
    "RECONCILEF_ONLYYOUWERECHANGED",
    "RECONCILEF_RESUMERECONCILIATION",
    "RECONCILEF_YOUMAYDOTHEUPDATES",
    "REC_E_ABORTED",
    "REC_E_INEEDTODOTHEUPDATES",
    "REC_E_NOCALLBACK",
    "REC_E_NORESIDUES",
    "REC_E_TOODIFFERENT",
    "REC_S_IDIDTHEUPDATES",
    "REC_S_NOTCOMPLETE",
    "REC_S_NOTCOMPLETEBUTPROPAGATE",
    "STATEBITS_FLAT",
]
_arch_optional = [
]