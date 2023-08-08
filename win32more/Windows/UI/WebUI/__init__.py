from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.ApplicationModel.Calls
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.ApplicationModel.Contacts.Provider
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.ApplicationModel.DataTransfer.ShareTarget
import win32more.Windows.ApplicationModel.Search
import win32more.Windows.ApplicationModel.UserDataAccounts.Provider
import win32more.Windows.ApplicationModel.Wallet
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Devices.Printers.Extensions
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Printing
import win32more.Windows.Media.SpeechRecognition
import win32more.Windows.Security.Authentication.Web
import win32more.Windows.Security.Authentication.Web.Provider
import win32more.Windows.Storage
import win32more.Windows.Storage.Pickers.Provider
import win32more.Windows.Storage.Provider
import win32more.Windows.Storage.Search
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI
import win32more.Windows.UI.WebUI
import win32more.Windows.Web
import win32more.Windows.Web.Http
import win32more.Windows.Web.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ActivatedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IActivatedDeferral
    _classid_ = 'Windows.UI.WebUI.ActivatedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.WebUI.IActivatedDeferral) -> Void: ...
class ActivatedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{50f1e730-c5d1-4b6b-9adb-8a11756be29c}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable_head, eventArgs: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Void: ...
class ActivatedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IActivatedOperation
    _classid_ = 'Windows.UI.WebUI.ActivatedOperation'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.WebUI.IActivatedOperation) -> win32more.Windows.UI.WebUI.ActivatedDeferral: ...
class BackgroundActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.BackgroundActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskInstance(self: win32more.Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs) -> win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance: ...
    TaskInstance = property(get_TaskInstance, None)
class BackgroundActivatedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{edb19fbb-0761-47cc-9a77-24d7072965ca}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable_head, eventArgs: win32more.Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs) -> Void: ...
class EnteredBackgroundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IEnteredBackgroundEventArgs
    _classid_ = 'Windows.UI.WebUI.EnteredBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.IEnteredBackgroundEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class EnteredBackgroundEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2b09a173-b68e-4def-88c1-8de84e5aab2f}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable_head, e: win32more.Windows.ApplicationModel.IEnteredBackgroundEventArgs) -> Void: ...
class HtmlPrintDocumentSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource
    _classid_ = 'Windows.UI.WebUI.HtmlPrintDocumentSource'
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> win32more.Windows.UI.WebUI.PrintContent: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: win32more.Windows.UI.WebUI.PrintContent) -> Void: ...
    @winrt_mixinmethod
    def get_LeftMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_LeftMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_TopMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RightMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_RightMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_BottomMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_BottomMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_EnableHeaderFooter(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableHeaderFooter(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShrinkToFit(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShrinkToFit(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PercentScale(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_PercentScale(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, scalePercent: Single) -> Void: ...
    @winrt_mixinmethod
    def get_PageRange(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def TrySetPageRange(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, strPageRange: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Content = property(get_Content, put_Content)
    LeftMargin = property(get_LeftMargin, put_LeftMargin)
    TopMargin = property(get_TopMargin, put_TopMargin)
    RightMargin = property(get_RightMargin, put_RightMargin)
    BottomMargin = property(get_BottomMargin, put_BottomMargin)
    EnableHeaderFooter = property(get_EnableHeaderFooter, put_EnableHeaderFooter)
    ShrinkToFit = property(get_ShrinkToFit, put_ShrinkToFit)
    PercentScale = property(get_PercentScale, put_PercentScale)
    PageRange = property(get_PageRange, None)
class IActivatedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IActivatedDeferral'
    _iid_ = Guid('{c3bd1978-a431-49d8-a76a-395a4e03dcf3}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IActivatedEventArgsDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IActivatedEventArgsDeferral'
    _iid_ = Guid('{ca6d5f74-63c2-44a6-b97b-d9a03c20bc9b}')
    @winrt_commethod(6)
    def get_ActivatedOperation(self) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
class IActivatedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IActivatedOperation'
    _iid_ = Guid('{b6a0b4bc-c6ca-42fd-9818-71904e45fed7}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.UI.WebUI.ActivatedDeferral: ...
class IHtmlPrintDocumentSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IHtmlPrintDocumentSource'
    _iid_ = Guid('{cea6469a-0e05-467a-abc9-36ec1d4cdcb6}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.UI.WebUI.PrintContent: ...
    @winrt_commethod(7)
    def put_Content(self, value: win32more.Windows.UI.WebUI.PrintContent) -> Void: ...
    @winrt_commethod(8)
    def get_LeftMargin(self) -> Single: ...
    @winrt_commethod(9)
    def put_LeftMargin(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_TopMargin(self) -> Single: ...
    @winrt_commethod(11)
    def put_TopMargin(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_RightMargin(self) -> Single: ...
    @winrt_commethod(13)
    def put_RightMargin(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_BottomMargin(self) -> Single: ...
    @winrt_commethod(15)
    def put_BottomMargin(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_EnableHeaderFooter(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_EnableHeaderFooter(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_ShrinkToFit(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_ShrinkToFit(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_PercentScale(self) -> Single: ...
    @winrt_commethod(21)
    def put_PercentScale(self, scalePercent: Single) -> Void: ...
    @winrt_commethod(22)
    def get_PageRange(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def TrySetPageRange(self, strPageRange: WinRT_String) -> Boolean: ...
    Content = property(get_Content, put_Content)
    LeftMargin = property(get_LeftMargin, put_LeftMargin)
    TopMargin = property(get_TopMargin, put_TopMargin)
    RightMargin = property(get_RightMargin, put_RightMargin)
    BottomMargin = property(get_BottomMargin, put_BottomMargin)
    EnableHeaderFooter = property(get_EnableHeaderFooter, put_EnableHeaderFooter)
    ShrinkToFit = property(get_ShrinkToFit, put_ShrinkToFit)
    PercentScale = property(get_PercentScale, put_PercentScale)
    PageRange = property(get_PageRange, None)
class INewWebUIViewCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.INewWebUIViewCreatedEventArgs'
    _iid_ = Guid('{e8e1b216-be2b-4c9e-85e7-083143ec4be7}')
    @winrt_commethod(6)
    def get_WebUIView(self) -> win32more.Windows.UI.WebUI.WebUIView: ...
    @winrt_commethod(7)
    def get_ActivatedEventArgs(self) -> win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_commethod(8)
    def get_HasPendingNavigate(self) -> Boolean: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    WebUIView = property(get_WebUIView, None)
    ActivatedEventArgs = property(get_ActivatedEventArgs, None)
    HasPendingNavigate = property(get_HasPendingNavigate, None)
class IWebUIActivationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics'
    _iid_ = Guid('{351b86bd-43b3-482b-85db-35d87b517ad9}')
    @winrt_commethod(6)
    def add_Activated(self, handler: win32more.Windows.UI.WebUI.ActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Suspending(self, handler: win32more.Windows.UI.WebUI.SuspendingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Suspending(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Resuming(self, handler: win32more.Windows.UI.WebUI.ResumingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Resuming(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Navigated(self, handler: win32more.Windows.UI.WebUI.NavigatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Navigated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWebUIActivationStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics2'
    _iid_ = Guid('{c8e88696-4d78-4aa4-8f06-2a9eadc6c40a}')
    @winrt_commethod(6)
    def add_LeavingBackground(self, handler: win32more.Windows.UI.WebUI.LeavingBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_LeavingBackground(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_EnteredBackground(self, handler: win32more.Windows.UI.WebUI.EnteredBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_EnteredBackground(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def EnablePrelaunch(self, value: Boolean) -> Void: ...
class IWebUIActivationStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics3'
    _iid_ = Guid('{91abb686-1af5-4445-b49f-9459f40fc8de}')
    @winrt_commethod(6)
    def RequestRestartAsync(self, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_commethod(7)
    def RequestRestartForUserAsync(self, user: win32more.Windows.System.User, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
class IWebUIActivationStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics4'
    _iid_ = Guid('{5e391429-183f-478d-8a25-67f80d03935b}')
    @winrt_commethod(6)
    def add_NewWebUIViewCreated(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.WebUI.NewWebUIViewCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_NewWebUIViewCreated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_BackgroundActivated(self, handler: win32more.Windows.UI.WebUI.BackgroundActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_BackgroundActivated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWebUIBackgroundTaskInstance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIBackgroundTaskInstance'
    _iid_ = Guid('{23f12c25-e2f7-4741-bc9c-394595de24dc}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Succeeded(self, succeeded: Boolean) -> Void: ...
    Succeeded = property(get_Succeeded, put_Succeeded)
class IWebUIBackgroundTaskInstanceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIBackgroundTaskInstanceStatics'
    _iid_ = Guid('{9c7a5291-19ae-4ca3-b94b-fe4ec744a740}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance: ...
    Current = property(get_Current, None)
class IWebUINavigatedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUINavigatedDeferral'
    _iid_ = Guid('{d804204d-831f-46e2-b432-3afce211f962}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IWebUINavigatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUINavigatedEventArgs'
    _iid_ = Guid('{a75841b8-2499-4030-a69d-15d2d9cfe524}')
    @winrt_commethod(6)
    def get_NavigatedOperation(self) -> win32more.Windows.UI.WebUI.WebUINavigatedOperation: ...
    NavigatedOperation = property(get_NavigatedOperation, None)
class IWebUINavigatedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUINavigatedOperation'
    _iid_ = Guid('{7a965f08-8182-4a89-ab67-8492e8750d4b}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.UI.WebUI.WebUINavigatedDeferral: ...
class IWebUIView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIView'
    _iid_ = Guid('{6783f64f-52da-4fd7-be69-8ef6284b423c}')
    @winrt_commethod(6)
    def get_ApplicationViewId(self) -> Int32: ...
    @winrt_commethod(7)
    def add_Closed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.WebUIView, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Activated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.WebUIView, win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_IgnoreApplicationContentUriRulesNavigationRestrictions(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_IgnoreApplicationContentUriRulesNavigationRestrictions(self, value: Boolean) -> Void: ...
    ApplicationViewId = property(get_ApplicationViewId, None)
    IgnoreApplicationContentUriRulesNavigationRestrictions = property(get_IgnoreApplicationContentUriRulesNavigationRestrictions, put_IgnoreApplicationContentUriRulesNavigationRestrictions)
class IWebUIViewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIViewStatics'
    _iid_ = Guid('{b591e668-8e59-44f9-8803-1b24c9149d30}')
    @winrt_commethod(6)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.WebUI.WebUIView]: ...
    @winrt_commethod(7)
    def CreateWithUriAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.WebUI.WebUIView]: ...
class LeavingBackgroundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ILeavingBackgroundEventArgs
    _classid_ = 'Windows.UI.WebUI.LeavingBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.ILeavingBackgroundEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class LeavingBackgroundEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00b4ccd9-7a9c-4b6b-9ac4-13474f268bc4}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable_head, e: win32more.Windows.ApplicationModel.ILeavingBackgroundEventArgs) -> Void: ...
class NavigatedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7af46fe6-40ca-4e49-a7d6-dbdb330cd1a3}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable_head, e: win32more.Windows.UI.WebUI.IWebUINavigatedEventArgs) -> Void: ...
class NewWebUIViewCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs
    _classid_ = 'Windows.UI.WebUI.NewWebUIViewCreatedEventArgs'
    @winrt_mixinmethod
    def get_WebUIView(self: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> win32more.Windows.UI.WebUI.WebUIView: ...
    @winrt_mixinmethod
    def get_ActivatedEventArgs(self: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_mixinmethod
    def get_HasPendingNavigate(self: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    WebUIView = property(get_WebUIView, None)
    ActivatedEventArgs = property(get_ActivatedEventArgs, None)
    HasPendingNavigate = property(get_HasPendingNavigate, None)
PrintContent = Int32
PrintContent_AllPages: PrintContent = 0
PrintContent_CurrentPage: PrintContent = 1
PrintContent_CustomPageRange: PrintContent = 2
PrintContent_CurrentSelection: PrintContent = 3
class ResumingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{26599ba9-a22d-4806-a728-acadc1d075fa}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
class SuspendingDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ISuspendingDeferral
    _classid_ = 'Windows.UI.WebUI.SuspendingDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.ISuspendingDeferral) -> Void: ...
class SuspendingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ISuspendingEventArgs
    _classid_ = 'Windows.UI.WebUI.SuspendingEventArgs'
    @winrt_mixinmethod
    def get_SuspendingOperation(self: win32more.Windows.ApplicationModel.ISuspendingEventArgs) -> win32more.Windows.ApplicationModel.SuspendingOperation: ...
    SuspendingOperation = property(get_SuspendingOperation, None)
class SuspendingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{509c429c-78e2-4883-abc8-8960dcde1b5c}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable_head, e: win32more.Windows.ApplicationModel.ISuspendingEventArgs) -> Void: ...
class SuspendingOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ISuspendingOperation
    _classid_ = 'Windows.UI.WebUI.SuspendingOperation'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.ISuspendingOperation) -> win32more.Windows.ApplicationModel.SuspendingDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.ApplicationModel.ISuspendingOperation) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class WebUIApplication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.WebUIApplication'
    @winrt_classmethod
    def add_NewWebUIViewCreated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics4, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.WebUI.NewWebUIViewCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_NewWebUIViewCreated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_BackgroundActivated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics4, handler: win32more.Windows.UI.WebUI.BackgroundActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_BackgroundActivated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def RequestRestartAsync(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics3, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def RequestRestartForUserAsync(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics3, user: win32more.Windows.System.User, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def add_LeavingBackground(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, handler: win32more.Windows.UI.WebUI.LeavingBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LeavingBackground(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_EnteredBackground(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, handler: win32more.Windows.UI.WebUI.EnteredBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_EnteredBackground(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def EnablePrelaunch(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def add_Activated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, handler: win32more.Windows.UI.WebUI.ActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Activated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Suspending(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, handler: win32more.Windows.UI.WebUI.SuspendingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Suspending(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Resuming(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, handler: win32more.Windows.UI.WebUI.ResumingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Resuming(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Navigated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, handler: win32more.Windows.UI.WebUI.NavigatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Navigated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class WebUIAppointmentsProviderAddAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderAddAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_AddAppointmentOperation(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    AddAppointmentOperation = property(get_AddAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_RemoveAppointmentOperation(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    RemoveAppointmentOperation = property(get_RemoveAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_ReplaceAppointmentOperation(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ReplaceAppointmentOperation = property(get_ReplaceAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs'
    @winrt_mixinmethod
    def get_InstanceStartDate(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_LocalId(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingId(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    InstanceStartDate = property(get_InstanceStartDate, None)
    LocalId = property(get_LocalId, None)
    RoamingId = property(get_RoamingId, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs'
    @winrt_mixinmethod
    def get_TimeToShow(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    TimeToShow = property(get_TimeToShow, None)
    Duration = property(get_Duration, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class _WebUIBackgroundTaskInstance_Meta_(ComPtr.__class__):
    pass
class WebUIBackgroundTaskInstance(ComPtr, metaclass=_WebUIBackgroundTaskInstance_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.WebUIBackgroundTaskInstance'
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstanceStatics) -> win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance: ...
    _WebUIBackgroundTaskInstance_Meta_.Current = property(get_Current.__wrapped__, None)
class WebUIBackgroundTaskInstanceRuntimeClass(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance
    _classid_ = 'Windows.UI.WebUI.WebUIBackgroundTaskInstanceRuntimeClass'
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance) -> Boolean: ...
    @winrt_mixinmethod
    def put_Succeeded(self: win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance, succeeded: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InstanceId(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Guid: ...
    @winrt_mixinmethod
    def get_Task(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> UInt32: ...
    @winrt_mixinmethod
    def put_Progress(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TriggerDetails(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def add_Canceled(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance, cancelHandler: win32more.Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Canceled(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SuspendedCount(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> UInt32: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskDeferral: ...
    Succeeded = property(get_Succeeded, put_Succeeded)
    InstanceId = property(get_InstanceId, None)
    Task = property(get_Task, None)
    Progress = property(get_Progress, put_Progress)
    TriggerDetails = property(get_TriggerDetails, None)
    SuspendedCount = property(get_SuspendedCount, None)
class WebUIBarcodeScannerPreviewActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIBarcodeScannerPreviewActivatedEventArgs'
    @winrt_mixinmethod
    def get_ConnectionId(self: win32more.Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ConnectionId = property(get_ConnectionId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUICachedFileUpdaterActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUICachedFileUpdaterActivatedEventArgs'
    @winrt_mixinmethod
    def get_CachedFileUpdaterUI(self: win32more.Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs) -> win32more.Windows.Storage.Provider.CachedFileUpdaterUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    CachedFileUpdaterUI = property(get_CachedFileUpdaterUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUICameraSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUICameraSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_VideoDeviceController(self: win32more.Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_VideoDeviceExtension(self: win32more.Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    VideoDeviceController = property(get_VideoDeviceController, None)
    VideoDeviceExtension = property(get_VideoDeviceExtension, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUICommandLineActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUICommandLineActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.CommandLineActivationOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactMapActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactMapActivatedEventArgs'
    @winrt_mixinmethod
    def get_Address(self: win32more.Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.ContactAddress: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    Address = property(get_Address, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactMessageActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactMessageActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactPanelActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactPanelActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPanel(self: win32more.Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.ContactPanel: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ContactPanel = property(get_ContactPanel, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIContactPickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPickerUI(self: win32more.Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Provider.ContactPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ContactPickerUI = property(get_ContactPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactPostActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactPostActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactVideoCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactVideoCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIDeviceActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIDeviceActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformationId(self: win32more.Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    DeviceInformationId = property(get_DeviceInformationId, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIDevicePairingActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIDevicePairingActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    DeviceInformation = property(get_DeviceInformation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIDialReceiverActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIDialReceiverActivatedEventArgs'
    @winrt_mixinmethod
    def get_AppName(self: win32more.Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    AppName = property(get_AppName, None)
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFileActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileActivatedEventArgs'
    @winrt_mixinmethod
    def get_Files(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_NeighboringFilesQuery(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithNeighboringFiles) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Files = property(get_Files, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, None)
    User = property(get_User, None)
class WebUIFileOpenPickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileOpenPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileOpenPickerUI(self: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs) -> win32more.Windows.Storage.Pickers.Provider.FileOpenPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    FileOpenPickerUI = property(get_FileOpenPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFileOpenPickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileOpenPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Files(self: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Files = property(get_Files, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFileSavePickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileSavePickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileSavePickerUI(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs) -> win32more.Windows.Storage.Pickers.Provider.FileSavePickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    FileSavePickerUI = property(get_FileSavePickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFileSavePickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileSavePickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    File = property(get_File, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFolderPickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFolderPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Folder = property(get_Folder, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUILaunchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_PrelaunchActivated(self: win32more.Windows.ApplicationModel.Activation.IPrelaunchActivatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_TileActivatedInfo(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs2) -> win32more.Windows.ApplicationModel.Activation.TileActivatedInfo: ...
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    PrelaunchActivated = property(get_PrelaunchActivated, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
    TileActivatedInfo = property(get_TileActivatedInfo, None)
class WebUILockScreenActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILockScreenActivatedEventArgs'
    @winrt_mixinmethod
    def get_Info(self: win32more.Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Info = property(get_Info, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUILockScreenCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILockScreenCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_CallUI(self: win32more.Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs) -> win32more.Windows.ApplicationModel.Calls.LockScreenCallUI: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    CallUI = property(get_CallUI, None)
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUILockScreenComponentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILockScreenComponentActivatedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUINavigatedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUINavigatedDeferral
    _classid_ = 'Windows.UI.WebUI.WebUINavigatedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.WebUI.IWebUINavigatedDeferral) -> Void: ...
class WebUINavigatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUINavigatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUINavigatedEventArgs'
    @winrt_mixinmethod
    def get_NavigatedOperation(self: win32more.Windows.UI.WebUI.IWebUINavigatedEventArgs) -> win32more.Windows.UI.WebUI.WebUINavigatedOperation: ...
    NavigatedOperation = property(get_NavigatedOperation, None)
class WebUINavigatedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUINavigatedOperation
    _classid_ = 'Windows.UI.WebUI.WebUINavigatedOperation'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.WebUI.IWebUINavigatedOperation) -> win32more.Windows.UI.WebUI.WebUINavigatedDeferral: ...
class WebUIPhoneCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPhoneCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    LineId = property(get_LineId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIPrint3DWorkflowActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPrint3DWorkflowActivatedEventArgs'
    @winrt_mixinmethod
    def get_Workflow(self: win32more.Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs) -> win32more.Windows.Devices.Printers.Extensions.Print3DWorkflow: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    Workflow = property(get_Workflow, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIPrintTaskSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPrintTaskSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs) -> win32more.Windows.Devices.Printers.Extensions.PrintTaskConfiguration: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    Configuration = property(get_Configuration, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIPrintWorkflowForegroundTaskActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPrintWorkflowForegroundTaskActivatedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIProtocolActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIProtocolActivatedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Uri = property(get_Uri, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIProtocolForResultsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIProtocolForResultsActivatedEventArgs'
    @winrt_mixinmethod
    def get_ProtocolForResultsOperation(self: win32more.Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs) -> win32more.Windows.System.ProtocolForResultsOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ProtocolForResultsOperation = property(get_ProtocolForResultsOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Uri = property(get_Uri, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIRestrictedLaunchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIRestrictedLaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_SharedContext(self: win32more.Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    SharedContext = property(get_SharedContext, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUISearchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUISearchActivatedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgsWithLinguisticDetails) -> win32more.Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIShareTargetActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIShareTargetActivatedEventArgs'
    @winrt_mixinmethod
    def get_ShareOperation(self: win32more.Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ShareOperation = property(get_ShareOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIStartupTaskActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIStartupTaskActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    TaskId = property(get_TaskId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIToastNotificationActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIToastNotificationActivatedEventArgs'
    @winrt_mixinmethod
    def get_Argument(self: win32more.Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: win32more.Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIUserDataAccountProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIUserDataAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUIView
    _classid_ = 'Windows.UI.WebUI.WebUIView'
    @winrt_mixinmethod
    def get_ApplicationViewId(self: win32more.Windows.UI.WebUI.IWebUIView) -> Int32: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.UI.WebUI.IWebUIView, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.WebUIView, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.UI.WebUI.IWebUIView, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Activated(self: win32more.Windows.UI.WebUI.IWebUIView, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.WebUIView, win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: win32more.Windows.UI.WebUI.IWebUIView, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IgnoreApplicationContentUriRulesNavigationRestrictions(self: win32more.Windows.UI.WebUI.IWebUIView) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnoreApplicationContentUriRulesNavigationRestrictions(self: win32more.Windows.UI.WebUI.IWebUIView, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.Web.UI.IWebViewControl, source: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_DocumentTitle(self: win32more.Windows.Web.UI.IWebViewControl) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CanGoBack(self: win32more.Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanGoForward(self: win32more.Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_DefaultBackgroundColor(self: win32more.Windows.Web.UI.IWebViewControl, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultBackgroundColor(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_ContainsFullScreenElement(self: win32more.Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Settings(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.Web.UI.WebViewControlSettings: ...
    @winrt_mixinmethod
    def get_DeferredPermissionRequests(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.UI.WebViewControlDeferredPermissionRequest]: ...
    @winrt_mixinmethod
    def GoForward(self: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def GoBack(self: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Refresh(self: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Navigate(self: win32more.Windows.Web.UI.IWebViewControl, source: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def NavigateToString(self: win32more.Windows.Web.UI.IWebViewControl, text: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def NavigateToLocalStreamUri(self: win32more.Windows.Web.UI.IWebViewControl, source: win32more.Windows.Foundation.Uri, streamResolver: win32more.Windows.Web.IUriToStreamResolver) -> Void: ...
    @winrt_mixinmethod
    def NavigateWithHttpRequestMessage(self: win32more.Windows.Web.UI.IWebViewControl, requestMessage: win32more.Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_mixinmethod
    def InvokeScriptAsync(self: win32more.Windows.Web.UI.IWebViewControl, scriptName: WinRT_String, arguments: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def CapturePreviewToStreamAsync(self: win32more.Windows.Web.UI.IWebViewControl, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CaptureSelectedContentToDataPackageAsync(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackage]: ...
    @winrt_mixinmethod
    def BuildLocalStreamUri(self: win32more.Windows.Web.UI.IWebViewControl, contentIdentifier: WinRT_String, relativePath: WinRT_String) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def GetDeferredPermissionRequestById(self: win32more.Windows.Web.UI.IWebViewControl, id: UInt32, result: POINTER(win32more.Windows.Web.UI.WebViewControlDeferredPermissionRequest)) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationStarting(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationStarting(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContentLoading(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentLoading(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DOMContentLoaded(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DOMContentLoaded(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCompleted(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCompleted(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationStarting(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationStarting(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameContentLoading(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameContentLoading(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameDOMContentLoaded(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameDOMContentLoaded(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationCompleted(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationCompleted(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScriptNotify(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlScriptNotifyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScriptNotify(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LongRunningScriptDetected(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlLongRunningScriptDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LongRunningScriptDetected(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnsafeContentWarningDisplaying(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnsafeContentWarningDisplaying(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnviewableContentIdentified(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlUnviewableContentIdentifiedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnviewableContentIdentified(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PermissionRequested(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlPermissionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PermissionRequested(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnsupportedUriSchemeIdentified(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlUnsupportedUriSchemeIdentifiedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnsupportedUriSchemeIdentified(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NewWindowRequested(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNewWindowRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NewWindowRequested(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContainsFullScreenElementChanged(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContainsFullScreenElementChanged(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WebResourceRequested(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlWebResourceRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WebResourceRequested(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddInitializeScript(self: win32more.Windows.Web.UI.IWebViewControl2, script: WinRT_String) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.UI.WebUI.IWebUIViewStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.WebUI.WebUIView]: ...
    @winrt_classmethod
    def CreateWithUriAsync(cls: win32more.Windows.UI.WebUI.IWebUIViewStatics, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.WebUI.WebUIView]: ...
    ApplicationViewId = property(get_ApplicationViewId, None)
    IgnoreApplicationContentUriRulesNavigationRestrictions = property(get_IgnoreApplicationContentUriRulesNavigationRestrictions, put_IgnoreApplicationContentUriRulesNavigationRestrictions)
    Source = property(get_Source, put_Source)
    DocumentTitle = property(get_DocumentTitle, None)
    CanGoBack = property(get_CanGoBack, None)
    CanGoForward = property(get_CanGoForward, None)
    DefaultBackgroundColor = property(get_DefaultBackgroundColor, put_DefaultBackgroundColor)
    ContainsFullScreenElement = property(get_ContainsFullScreenElement, None)
    Settings = property(get_Settings, None)
    DeferredPermissionRequests = property(get_DeferredPermissionRequests, None)
class WebUIVoiceCommandActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIVoiceCommandActivatedEventArgs'
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Result = property(get_Result, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIWalletActionActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIWalletActionActivatedEventArgs'
    @winrt_mixinmethod
    def get_ItemId(self: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActionKind(self: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> win32more.Windows.ApplicationModel.Wallet.WalletActionKind: ...
    @winrt_mixinmethod
    def get_ActionId(self: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ItemId = property(get_ItemId, None)
    ActionKind = property(get_ActionKind, None)
    ActionId = property(get_ActionId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIWebAccountProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIWebAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs) -> win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIWebAuthenticationBrokerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIWebAuthenticationBrokerContinuationEventArgs'
    @winrt_mixinmethod
    def get_WebAuthenticationResult(self: win32more.Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    WebAuthenticationResult = property(get_WebAuthenticationResult, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
make_head(_module, 'ActivatedDeferral')
make_head(_module, 'ActivatedOperation')
make_head(_module, 'BackgroundActivatedEventArgs')
make_head(_module, 'EnteredBackgroundEventArgs')
make_head(_module, 'HtmlPrintDocumentSource')
make_head(_module, 'IActivatedDeferral')
make_head(_module, 'IActivatedEventArgsDeferral')
make_head(_module, 'IActivatedOperation')
make_head(_module, 'IHtmlPrintDocumentSource')
make_head(_module, 'INewWebUIViewCreatedEventArgs')
make_head(_module, 'IWebUIActivationStatics')
make_head(_module, 'IWebUIActivationStatics2')
make_head(_module, 'IWebUIActivationStatics3')
make_head(_module, 'IWebUIActivationStatics4')
make_head(_module, 'IWebUIBackgroundTaskInstance')
make_head(_module, 'IWebUIBackgroundTaskInstanceStatics')
make_head(_module, 'IWebUINavigatedDeferral')
make_head(_module, 'IWebUINavigatedEventArgs')
make_head(_module, 'IWebUINavigatedOperation')
make_head(_module, 'IWebUIView')
make_head(_module, 'IWebUIViewStatics')
make_head(_module, 'LeavingBackgroundEventArgs')
make_head(_module, 'NewWebUIViewCreatedEventArgs')
make_head(_module, 'SuspendingDeferral')
make_head(_module, 'SuspendingEventArgs')
make_head(_module, 'SuspendingOperation')
make_head(_module, 'WebUIApplication')
make_head(_module, 'WebUIAppointmentsProviderAddAppointmentActivatedEventArgs')
make_head(_module, 'WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs')
make_head(_module, 'WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs')
make_head(_module, 'WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs')
make_head(_module, 'WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs')
make_head(_module, 'WebUIBackgroundTaskInstance')
make_head(_module, 'WebUIBackgroundTaskInstanceRuntimeClass')
make_head(_module, 'WebUIBarcodeScannerPreviewActivatedEventArgs')
make_head(_module, 'WebUICachedFileUpdaterActivatedEventArgs')
make_head(_module, 'WebUICameraSettingsActivatedEventArgs')
make_head(_module, 'WebUICommandLineActivatedEventArgs')
make_head(_module, 'WebUIContactCallActivatedEventArgs')
make_head(_module, 'WebUIContactMapActivatedEventArgs')
make_head(_module, 'WebUIContactMessageActivatedEventArgs')
make_head(_module, 'WebUIContactPanelActivatedEventArgs')
make_head(_module, 'WebUIContactPickerActivatedEventArgs')
make_head(_module, 'WebUIContactPostActivatedEventArgs')
make_head(_module, 'WebUIContactVideoCallActivatedEventArgs')
make_head(_module, 'WebUIDeviceActivatedEventArgs')
make_head(_module, 'WebUIDevicePairingActivatedEventArgs')
make_head(_module, 'WebUIDialReceiverActivatedEventArgs')
make_head(_module, 'WebUIFileActivatedEventArgs')
make_head(_module, 'WebUIFileOpenPickerActivatedEventArgs')
make_head(_module, 'WebUIFileOpenPickerContinuationEventArgs')
make_head(_module, 'WebUIFileSavePickerActivatedEventArgs')
make_head(_module, 'WebUIFileSavePickerContinuationEventArgs')
make_head(_module, 'WebUIFolderPickerContinuationEventArgs')
make_head(_module, 'WebUILaunchActivatedEventArgs')
make_head(_module, 'WebUILockScreenActivatedEventArgs')
make_head(_module, 'WebUILockScreenCallActivatedEventArgs')
make_head(_module, 'WebUILockScreenComponentActivatedEventArgs')
make_head(_module, 'WebUINavigatedDeferral')
make_head(_module, 'WebUINavigatedEventArgs')
make_head(_module, 'WebUINavigatedOperation')
make_head(_module, 'WebUIPhoneCallActivatedEventArgs')
make_head(_module, 'WebUIPrint3DWorkflowActivatedEventArgs')
make_head(_module, 'WebUIPrintTaskSettingsActivatedEventArgs')
make_head(_module, 'WebUIPrintWorkflowForegroundTaskActivatedEventArgs')
make_head(_module, 'WebUIProtocolActivatedEventArgs')
make_head(_module, 'WebUIProtocolForResultsActivatedEventArgs')
make_head(_module, 'WebUIRestrictedLaunchActivatedEventArgs')
make_head(_module, 'WebUISearchActivatedEventArgs')
make_head(_module, 'WebUIShareTargetActivatedEventArgs')
make_head(_module, 'WebUIStartupTaskActivatedEventArgs')
make_head(_module, 'WebUIToastNotificationActivatedEventArgs')
make_head(_module, 'WebUIUserDataAccountProviderActivatedEventArgs')
make_head(_module, 'WebUIView')
make_head(_module, 'WebUIVoiceCommandActivatedEventArgs')
make_head(_module, 'WebUIWalletActionActivatedEventArgs')
make_head(_module, 'WebUIWebAccountProviderActivatedEventArgs')
make_head(_module, 'WebUIWebAuthenticationBrokerContinuationEventArgs')