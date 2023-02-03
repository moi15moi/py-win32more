from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Data.Xml.MsXml
import Windows.Win32.Foundation
import Windows.Win32.Graphics.DirectComposition
import Windows.Win32.Graphics.Gdi
import Windows.Win32.NetworkManagement.WNet
import Windows.Win32.Security
import Windows.Win32.Storage.FileSystem
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Com.Urlmon
import Windows.Win32.System.Console
import Windows.Win32.System.IO
import Windows.Win32.System.Ole
import Windows.Win32.System.Registry
import Windows.Win32.System.Search
import Windows.Win32.System.SystemServices
import Windows.Win32.System.Threading
import Windows.Win32.UI.Controls
import Windows.Win32.UI.Shell
import Windows.Win32.UI.Shell.Common
import Windows.Win32.UI.Shell.PropertiesSystem
import Windows.Win32.UI.WindowsAndMessaging
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
class AASHELLMENUFILENAME(Structure):
    cbTotal: Int16
    rgbReserved: Byte * 12
    szFileName: Char * 1
class AASHELLMENUITEM(Structure):
    lpReserved1: c_void_p
    iReserved: Int32
    uiReserved: UInt32
    lpName: POINTER(Windows.Win32.UI.Shell.AASHELLMENUFILENAME_head)
    psz: Windows.Win32.Foundation.PWSTR
ACENUMOPTION = Int32
ACEO_NONE: ACENUMOPTION = 0
ACEO_MOSTRECENTFIRST: ACENUMOPTION = 1
ACEO_FIRSTUNUSED: ACENUMOPTION = 65536
ACTIVATEOPTIONS = Int32
AO_NONE: ACTIVATEOPTIONS = 0
AO_DESIGNMODE: ACTIVATEOPTIONS = 1
AO_NOERRORUI: ACTIVATEOPTIONS = 2
AO_NOSPLASHSCREEN: ACTIVATEOPTIONS = 4
AO_PRELAUNCH: ACTIVATEOPTIONS = 33554432
ADJACENT_DISPLAY_EDGES = Int32
ADE_NONE: ADJACENT_DISPLAY_EDGES = 0
ADE_LEFT: ADJACENT_DISPLAY_EDGES = 1
ADE_RIGHT: ADJACENT_DISPLAY_EDGES = 2
AHE_TYPE = Int32
AHE_DESKTOP: AHE_TYPE = 0
AHE_IMMERSIVE: AHE_TYPE = 1
AHTYPE = Int32
AHTYPE_UNDEFINED: AHTYPE = 0
AHTYPE_USER_APPLICATION: AHTYPE = 8
AHTYPE_ANY_APPLICATION: AHTYPE = 16
AHTYPE_MACHINEDEFAULT: AHTYPE = 32
AHTYPE_PROGID: AHTYPE = 64
AHTYPE_APPLICATION: AHTYPE = 128
AHTYPE_CLASS_APPLICATION: AHTYPE = 256
AHTYPE_ANY_PROGID: AHTYPE = 512
APPACTIONFLAGS = Int32
APPACTION_INSTALL: APPACTIONFLAGS = 1
APPACTION_UNINSTALL: APPACTIONFLAGS = 2
APPACTION_MODIFY: APPACTIONFLAGS = 4
APPACTION_REPAIR: APPACTIONFLAGS = 8
APPACTION_UPGRADE: APPACTIONFLAGS = 16
APPACTION_CANGETSIZE: APPACTIONFLAGS = 32
APPACTION_MODIFYREMOVE: APPACTIONFLAGS = 128
APPACTION_ADDLATER: APPACTIONFLAGS = 256
APPACTION_UNSCHEDULE: APPACTIONFLAGS = 512
if ARCH in 'X64,ARM64':
    class APPBARDATA(Structure):
        cbSize: UInt32
        hWnd: Windows.Win32.Foundation.HWND
        uCallbackMessage: UInt32
        uEdge: UInt32
        rc: Windows.Win32.Foundation.RECT
        lParam: Windows.Win32.Foundation.LPARAM
if ARCH in 'X86':
    class APPBARDATA(Structure):
        cbSize: UInt32
        hWnd: Windows.Win32.Foundation.HWND
        uCallbackMessage: UInt32
        uEdge: UInt32
        rc: Windows.Win32.Foundation.RECT
        lParam: Windows.Win32.Foundation.LPARAM
        _pack_ = 1
class APPCATEGORYINFO(Structure):
    Locale: UInt32
    pszDescription: Windows.Win32.Foundation.PWSTR
    AppCategoryId: Guid
class APPCATEGORYINFOLIST(Structure):
    cCategory: UInt32
    pCategoryInfo: POINTER(Windows.Win32.UI.Shell.APPCATEGORYINFO_head)
APPDOCLISTTYPE = Int32
ADLT_RECENT: APPDOCLISTTYPE = 0
ADLT_FREQUENT: APPDOCLISTTYPE = 1
class APPINFODATA(Structure):
    cbSize: UInt32
    dwMask: UInt32
    pszDisplayName: Windows.Win32.Foundation.PWSTR
    pszVersion: Windows.Win32.Foundation.PWSTR
    pszPublisher: Windows.Win32.Foundation.PWSTR
    pszProductID: Windows.Win32.Foundation.PWSTR
    pszRegisteredOwner: Windows.Win32.Foundation.PWSTR
    pszRegisteredCompany: Windows.Win32.Foundation.PWSTR
    pszLanguage: Windows.Win32.Foundation.PWSTR
    pszSupportUrl: Windows.Win32.Foundation.PWSTR
    pszSupportTelephone: Windows.Win32.Foundation.PWSTR
    pszHelpLink: Windows.Win32.Foundation.PWSTR
    pszInstallLocation: Windows.Win32.Foundation.PWSTR
    pszInstallSource: Windows.Win32.Foundation.PWSTR
    pszInstallDate: Windows.Win32.Foundation.PWSTR
    pszContact: Windows.Win32.Foundation.PWSTR
    pszComments: Windows.Win32.Foundation.PWSTR
    pszImage: Windows.Win32.Foundation.PWSTR
    pszReadmeUrl: Windows.Win32.Foundation.PWSTR
    pszUpdateInfoUrl: Windows.Win32.Foundation.PWSTR
APPINFODATAFLAGS = Int32
AIM_DISPLAYNAME: APPINFODATAFLAGS = 1
AIM_VERSION: APPINFODATAFLAGS = 2
AIM_PUBLISHER: APPINFODATAFLAGS = 4
AIM_PRODUCTID: APPINFODATAFLAGS = 8
AIM_REGISTEREDOWNER: APPINFODATAFLAGS = 16
AIM_REGISTEREDCOMPANY: APPINFODATAFLAGS = 32
AIM_LANGUAGE: APPINFODATAFLAGS = 64
AIM_SUPPORTURL: APPINFODATAFLAGS = 128
AIM_SUPPORTTELEPHONE: APPINFODATAFLAGS = 256
AIM_HELPLINK: APPINFODATAFLAGS = 512
AIM_INSTALLLOCATION: APPINFODATAFLAGS = 1024
AIM_INSTALLSOURCE: APPINFODATAFLAGS = 2048
AIM_INSTALLDATE: APPINFODATAFLAGS = 4096
AIM_CONTACT: APPINFODATAFLAGS = 16384
AIM_COMMENTS: APPINFODATAFLAGS = 32768
AIM_IMAGE: APPINFODATAFLAGS = 131072
AIM_READMEURL: APPINFODATAFLAGS = 262144
AIM_UPDATEINFOURL: APPINFODATAFLAGS = 524288
@winfunctype_pointer
def APPLET_PROC(hwndCpl: Windows.Win32.Foundation.HWND, msg: UInt32, lParam1: Windows.Win32.Foundation.LPARAM, lParam2: Windows.Win32.Foundation.LPARAM) -> Int32: ...
APPLICATION_VIEW_MIN_WIDTH = Int32
AVMW_DEFAULT: APPLICATION_VIEW_MIN_WIDTH = 0
AVMW_320: APPLICATION_VIEW_MIN_WIDTH = 1
AVMW_500: APPLICATION_VIEW_MIN_WIDTH = 2
APPLICATION_VIEW_ORIENTATION = Int32
AVO_LANDSCAPE: APPLICATION_VIEW_ORIENTATION = 0
AVO_PORTRAIT: APPLICATION_VIEW_ORIENTATION = 1
APPLICATION_VIEW_SIZE_PREFERENCE = Int32
AVSP_DEFAULT: APPLICATION_VIEW_SIZE_PREFERENCE = 0
AVSP_USE_LESS: APPLICATION_VIEW_SIZE_PREFERENCE = 1
AVSP_USE_HALF: APPLICATION_VIEW_SIZE_PREFERENCE = 2
AVSP_USE_MORE: APPLICATION_VIEW_SIZE_PREFERENCE = 3
AVSP_USE_MINIMUM: APPLICATION_VIEW_SIZE_PREFERENCE = 4
AVSP_USE_NONE: APPLICATION_VIEW_SIZE_PREFERENCE = 5
AVSP_CUSTOM: APPLICATION_VIEW_SIZE_PREFERENCE = 6
APPLICATION_VIEW_STATE = Int32
AVS_FULLSCREEN_LANDSCAPE: APPLICATION_VIEW_STATE = 0
AVS_FILLED: APPLICATION_VIEW_STATE = 1
AVS_SNAPPED: APPLICATION_VIEW_STATE = 2
AVS_FULLSCREEN_PORTRAIT: APPLICATION_VIEW_STATE = 3
ASSOCCLASS = Int32
ASSOCCLASS_SHELL_KEY: ASSOCCLASS = 0
ASSOCCLASS_PROGID_KEY: ASSOCCLASS = 1
ASSOCCLASS_PROGID_STR: ASSOCCLASS = 2
ASSOCCLASS_CLSID_KEY: ASSOCCLASS = 3
ASSOCCLASS_CLSID_STR: ASSOCCLASS = 4
ASSOCCLASS_APP_KEY: ASSOCCLASS = 5
ASSOCCLASS_APP_STR: ASSOCCLASS = 6
ASSOCCLASS_SYSTEM_STR: ASSOCCLASS = 7
ASSOCCLASS_FOLDER: ASSOCCLASS = 8
ASSOCCLASS_STAR: ASSOCCLASS = 9
ASSOCCLASS_FIXED_PROGID_STR: ASSOCCLASS = 10
ASSOCCLASS_PROTOCOL_STR: ASSOCCLASS = 11
ASSOCDATA = Int32
ASSOCDATA_MSIDESCRIPTOR: ASSOCDATA = 1
ASSOCDATA_NOACTIVATEHANDLER: ASSOCDATA = 2
ASSOCDATA_UNUSED1: ASSOCDATA = 3
ASSOCDATA_HASPERUSERASSOC: ASSOCDATA = 4
ASSOCDATA_EDITFLAGS: ASSOCDATA = 5
ASSOCDATA_VALUE: ASSOCDATA = 6
ASSOCDATA_MAX: ASSOCDATA = 7
ASSOCENUM = Int32
ASSOCENUM_NONE: ASSOCENUM = 0
ASSOCF = UInt32
ASSOCF_NONE: ASSOCF = 0
ASSOCF_INIT_NOREMAPCLSID: ASSOCF = 1
ASSOCF_INIT_BYEXENAME: ASSOCF = 2
ASSOCF_OPEN_BYEXENAME: ASSOCF = 2
ASSOCF_INIT_DEFAULTTOSTAR: ASSOCF = 4
ASSOCF_INIT_DEFAULTTOFOLDER: ASSOCF = 8
ASSOCF_NOUSERSETTINGS: ASSOCF = 16
ASSOCF_NOTRUNCATE: ASSOCF = 32
ASSOCF_VERIFY: ASSOCF = 64
ASSOCF_REMAPRUNDLL: ASSOCF = 128
ASSOCF_NOFIXUPS: ASSOCF = 256
ASSOCF_IGNOREBASECLASS: ASSOCF = 512
ASSOCF_INIT_IGNOREUNKNOWN: ASSOCF = 1024
ASSOCF_INIT_FIXED_PROGID: ASSOCF = 2048
ASSOCF_IS_PROTOCOL: ASSOCF = 4096
ASSOCF_INIT_FOR_FILE: ASSOCF = 8192
ASSOCF_IS_FULL_URI: ASSOCF = 16384
ASSOCF_PER_MACHINE_ONLY: ASSOCF = 32768
ASSOCF_APP_TO_APP: ASSOCF = 65536
if ARCH in 'X64,ARM64':
    class ASSOCIATIONELEMENT(Structure):
        ac: Windows.Win32.UI.Shell.ASSOCCLASS
        hkClass: Windows.Win32.System.Registry.HKEY
        pszClass: Windows.Win32.Foundation.PWSTR
if ARCH in 'X86':
    class ASSOCIATIONELEMENT(Structure):
        ac: Windows.Win32.UI.Shell.ASSOCCLASS
        hkClass: Windows.Win32.System.Registry.HKEY
        pszClass: Windows.Win32.Foundation.PWSTR
        _pack_ = 1
ASSOCIATIONLEVEL = Int32
AL_MACHINE: ASSOCIATIONLEVEL = 0
AL_EFFECTIVE: ASSOCIATIONLEVEL = 1
AL_USER: ASSOCIATIONLEVEL = 2
ASSOCIATIONTYPE = Int32
AT_FILEEXTENSION: ASSOCIATIONTYPE = 0
AT_URLPROTOCOL: ASSOCIATIONTYPE = 1
AT_STARTMENUCLIENT: ASSOCIATIONTYPE = 2
AT_MIMETYPE: ASSOCIATIONTYPE = 3
ASSOCKEY = Int32
ASSOCKEY_SHELLEXECCLASS: ASSOCKEY = 1
ASSOCKEY_APP: ASSOCKEY = 2
ASSOCKEY_CLASS: ASSOCKEY = 3
ASSOCKEY_BASECLASS: ASSOCKEY = 4
ASSOCKEY_MAX: ASSOCKEY = 5
ASSOCSTR = Int32
ASSOCSTR_COMMAND: ASSOCSTR = 1
ASSOCSTR_EXECUTABLE: ASSOCSTR = 2
ASSOCSTR_FRIENDLYDOCNAME: ASSOCSTR = 3
ASSOCSTR_FRIENDLYAPPNAME: ASSOCSTR = 4
ASSOCSTR_NOOPEN: ASSOCSTR = 5
ASSOCSTR_SHELLNEWVALUE: ASSOCSTR = 6
ASSOCSTR_DDECOMMAND: ASSOCSTR = 7
ASSOCSTR_DDEIFEXEC: ASSOCSTR = 8
ASSOCSTR_DDEAPPLICATION: ASSOCSTR = 9
ASSOCSTR_DDETOPIC: ASSOCSTR = 10
ASSOCSTR_INFOTIP: ASSOCSTR = 11
ASSOCSTR_QUICKTIP: ASSOCSTR = 12
ASSOCSTR_TILEINFO: ASSOCSTR = 13
ASSOCSTR_CONTENTTYPE: ASSOCSTR = 14
ASSOCSTR_DEFAULTICON: ASSOCSTR = 15
ASSOCSTR_SHELLEXTENSION: ASSOCSTR = 16
ASSOCSTR_DROPTARGET: ASSOCSTR = 17
ASSOCSTR_DELEGATEEXECUTE: ASSOCSTR = 18
ASSOCSTR_SUPPORTED_URI_PROTOCOLS: ASSOCSTR = 19
ASSOCSTR_PROGID: ASSOCSTR = 20
ASSOCSTR_APPID: ASSOCSTR = 21
ASSOCSTR_APPPUBLISHER: ASSOCSTR = 22
ASSOCSTR_APPICONREFERENCE: ASSOCSTR = 23
ASSOCSTR_MAX: ASSOCSTR = 24
ASSOC_FILTER = Int32
ASSOC_FILTER_NONE: ASSOC_FILTER = 0
ASSOC_FILTER_RECOMMENDED: ASSOC_FILTER = 1
ATTACHMENT_ACTION = Int32
ATTACHMENT_ACTION_CANCEL: ATTACHMENT_ACTION = 0
ATTACHMENT_ACTION_SAVE: ATTACHMENT_ACTION = 1
ATTACHMENT_ACTION_EXEC: ATTACHMENT_ACTION = 2
ATTACHMENT_PROMPT = Int32
ATTACHMENT_PROMPT_NONE: ATTACHMENT_PROMPT = 0
ATTACHMENT_PROMPT_SAVE: ATTACHMENT_PROMPT = 1
ATTACHMENT_PROMPT_EXEC: ATTACHMENT_PROMPT = 2
ATTACHMENT_PROMPT_EXEC_OR_SAVE: ATTACHMENT_PROMPT = 3
AUTOCOMPLETELISTOPTIONS = Int32
ACLO_NONE: AUTOCOMPLETELISTOPTIONS = 0
ACLO_CURRENTDIR: AUTOCOMPLETELISTOPTIONS = 1
ACLO_MYCOMPUTER: AUTOCOMPLETELISTOPTIONS = 2
ACLO_DESKTOP: AUTOCOMPLETELISTOPTIONS = 4
ACLO_FAVORITES: AUTOCOMPLETELISTOPTIONS = 8
ACLO_FILESYSONLY: AUTOCOMPLETELISTOPTIONS = 16
ACLO_FILESYSDIRS: AUTOCOMPLETELISTOPTIONS = 32
ACLO_VIRTUALNAMESPACE: AUTOCOMPLETELISTOPTIONS = 64
AUTOCOMPLETEOPTIONS = Int32
ACO_NONE: AUTOCOMPLETEOPTIONS = 0
ACO_AUTOSUGGEST: AUTOCOMPLETEOPTIONS = 1
ACO_AUTOAPPEND: AUTOCOMPLETEOPTIONS = 2
ACO_SEARCH: AUTOCOMPLETEOPTIONS = 4
ACO_FILTERPREFIXES: AUTOCOMPLETEOPTIONS = 8
ACO_USETAB: AUTOCOMPLETEOPTIONS = 16
ACO_UPDOWNKEYDROPSLIST: AUTOCOMPLETEOPTIONS = 32
ACO_RTLREADING: AUTOCOMPLETEOPTIONS = 64
ACO_WORD_FILTER: AUTOCOMPLETEOPTIONS = 128
ACO_NOPREFIXFILTERING: AUTOCOMPLETEOPTIONS = 256
class AUTO_SCROLL_DATA(Structure):
    iNextSample: Int32
    dwLastScroll: UInt32
    bFull: Windows.Win32.Foundation.BOOL
    pts: Windows.Win32.Foundation.POINT * 3
    dwTimes: UInt32 * 3
    _pack_ = 1
AccessibilityDockingService = Guid('29ce1d46-b481-4aa0-a0-8a-d3-eb-c8-ac-a4-02')
AlphabeticalCategorizer = Guid('3c2654c6-7372-4f6b-b3-10-55-d6-12-8f-49-d2')
HLINK_E_FIRST: Windows.Win32.Foundation.HRESULT = -2147221248
HLINK_S_FIRST: Windows.Win32.Foundation.HRESULT = 262400
WM_CPL_LAUNCH: UInt32 = 2024
WM_CPL_LAUNCHED: UInt32 = 2025
CPL_DYNAMIC_RES: UInt32 = 0
CPL_INIT: UInt32 = 1
CPL_GETCOUNT: UInt32 = 2
CPL_INQUIRE: UInt32 = 3
CPL_SELECT: UInt32 = 4
CPL_DBLCLK: UInt32 = 5
CPL_STOP: UInt32 = 6
CPL_EXIT: UInt32 = 7
CPL_NEWINQUIRE: UInt32 = 8
CPL_STARTWPARMSA: UInt32 = 9
CPL_STARTWPARMSW: UInt32 = 10
CPL_STARTWPARMS: UInt32 = 10
CPL_SETUP: UInt32 = 200
HLINK_S_DONTHIDE: Int32 = 262400
FOLDERID_NetworkFolder: Guid = Guid('d20beec4-5ca8-4905-ae-3b-bf-25-1e-a0-9b-53')
FOLDERID_ComputerFolder: Guid = Guid('0ac0837c-bbf8-452a-85-0d-79-d0-8e-66-7c-a7')
FOLDERID_InternetFolder: Guid = Guid('4d9f7874-4e0c-4904-96-7b-40-b0-d2-0c-3e-4b')
FOLDERID_ControlPanelFolder: Guid = Guid('82a74aeb-aeb4-465c-a0-14-d0-97-ee-34-6d-63')
FOLDERID_PrintersFolder: Guid = Guid('76fc4e2d-d6ad-4519-a6-63-37-bd-56-06-81-85')
FOLDERID_SyncManagerFolder: Guid = Guid('43668bf8-c14e-49b2-97-c9-74-77-84-d7-84-b7')
FOLDERID_SyncSetupFolder: Guid = Guid('0f214138-b1d3-4a90-bb-a9-27-cb-c0-c5-38-9a')
FOLDERID_ConflictFolder: Guid = Guid('4bfefb45-347d-4006-a5-be-ac-0c-b0-56-71-92')
FOLDERID_SyncResultsFolder: Guid = Guid('289a9a43-be44-4057-a4-1b-58-7a-76-d7-e7-f9')
FOLDERID_RecycleBinFolder: Guid = Guid('b7534046-3ecb-4c18-be-4e-64-cd-4c-b7-d6-ac')
FOLDERID_ConnectionsFolder: Guid = Guid('6f0cd92b-2e97-45d1-88-ff-b0-d1-86-b8-de-dd')
FOLDERID_Fonts: Guid = Guid('fd228cb7-ae11-4ae3-86-4c-16-f3-91-0a-b8-fe')
FOLDERID_Desktop: Guid = Guid('b4bfcc3a-db2c-424c-b0-29-7f-e9-9a-87-c6-41')
FOLDERID_Startup: Guid = Guid('b97d20bb-f46a-4c97-ba-10-5e-36-08-43-08-54')
FOLDERID_Programs: Guid = Guid('a77f5d77-2e2b-44c3-a6-a2-ab-a6-01-05-4a-51')
FOLDERID_StartMenu: Guid = Guid('625b53c3-ab48-4ec1-ba-1f-a1-ef-41-46-fc-19')
FOLDERID_Recent: Guid = Guid('ae50c081-ebd2-438a-86-55-8a-09-2e-34-98-7a')
FOLDERID_SendTo: Guid = Guid('8983036c-27c0-404b-8f-08-10-2d-10-dc-fd-74')
FOLDERID_Documents: Guid = Guid('fdd39ad0-238f-46af-ad-b4-6c-85-48-03-69-c7')
FOLDERID_Favorites: Guid = Guid('1777f761-68ad-4d8a-87-bd-30-b7-59-fa-33-dd')
FOLDERID_NetHood: Guid = Guid('c5abbf53-e17f-4121-89-00-86-62-6f-c2-c9-73')
FOLDERID_PrintHood: Guid = Guid('9274bd8d-cfd1-41c3-b3-5e-b1-3f-55-a7-58-f4')
FOLDERID_Templates: Guid = Guid('a63293e8-664e-48db-a0-79-df-75-9e-05-09-f7')
FOLDERID_CommonStartup: Guid = Guid('82a5ea35-d9cd-47c5-96-29-e1-5d-2f-71-4e-6e')
FOLDERID_CommonPrograms: Guid = Guid('0139d44e-6afe-49f2-86-90-3d-af-ca-e6-ff-b8')
FOLDERID_CommonStartMenu: Guid = Guid('a4115719-d62e-491d-aa-7c-e7-4b-8b-e3-b0-67')
FOLDERID_PublicDesktop: Guid = Guid('c4aa340d-f20f-4863-af-ef-f8-7e-f2-e6-ba-25')
FOLDERID_ProgramData: Guid = Guid('62ab5d82-fdc1-4dc3-a9-dd-07-0d-1d-49-5d-97')
FOLDERID_CommonTemplates: Guid = Guid('b94237e7-57ac-4347-91-51-b0-8c-6c-32-d1-f7')
FOLDERID_PublicDocuments: Guid = Guid('ed4824af-dce4-45a8-81-e2-fc-79-65-08-36-34')
FOLDERID_RoamingAppData: Guid = Guid('3eb685db-65f9-4cf6-a0-3a-e3-ef-65-72-9f-3d')
FOLDERID_LocalAppData: Guid = Guid('f1b32785-6fba-4fcf-9d-55-7b-8e-7f-15-70-91')
FOLDERID_LocalAppDataLow: Guid = Guid('a520a1a4-1780-4ff6-bd-18-16-73-43-c5-af-16')
FOLDERID_InternetCache: Guid = Guid('352481e8-33be-4251-ba-85-60-07-ca-ed-cf-9d')
FOLDERID_Cookies: Guid = Guid('2b0f765d-c0e9-4171-90-8e-08-a6-11-b8-4f-f6')
FOLDERID_History: Guid = Guid('d9dc8a3b-b784-432e-a7-81-5a-11-30-a7-59-63')
FOLDERID_System: Guid = Guid('1ac14e77-02e7-4e5d-b7-44-2e-b1-ae-51-98-b7')
FOLDERID_SystemX86: Guid = Guid('d65231b0-b2f1-4857-a4-ce-a8-e7-c6-ea-7d-27')
FOLDERID_Windows: Guid = Guid('f38bf404-1d43-42f2-93-05-67-de-0b-28-fc-23')
FOLDERID_Profile: Guid = Guid('5e6c858f-0e22-4760-9a-fe-ea-33-17-b6-71-73')
FOLDERID_Pictures: Guid = Guid('33e28130-4e1e-4676-83-5a-98-39-5c-3b-c3-bb')
FOLDERID_ProgramFilesX86: Guid = Guid('7c5a40ef-a0fb-4bfc-87-4a-c0-f2-e0-b9-fa-8e')
FOLDERID_ProgramFilesCommonX86: Guid = Guid('de974d24-d9c6-4d3e-bf-91-f4-45-51-20-b9-17')
FOLDERID_ProgramFilesX64: Guid = Guid('6d809377-6af0-444b-89-57-a3-77-3f-02-20-0e')
FOLDERID_ProgramFilesCommonX64: Guid = Guid('6365d5a7-0f0d-45e5-87-f6-0d-a5-6b-6a-4f-7d')
FOLDERID_ProgramFiles: Guid = Guid('905e63b6-c1bf-494e-b2-9c-65-b7-32-d3-d2-1a')
FOLDERID_ProgramFilesCommon: Guid = Guid('f7f1ed05-9f6d-47a2-aa-ae-29-d3-17-c6-f0-66')
FOLDERID_UserProgramFiles: Guid = Guid('5cd7aee2-2219-4a67-b8-5d-6c-9c-e1-56-60-cb')
FOLDERID_UserProgramFilesCommon: Guid = Guid('bcbd3057-ca5c-4622-b4-2d-bc-56-db-0a-e5-16')
FOLDERID_AdminTools: Guid = Guid('724ef170-a42d-4fef-9f-26-b6-0e-84-6f-ba-4f')
FOLDERID_CommonAdminTools: Guid = Guid('d0384e7d-bac3-4797-8f-14-cb-a2-29-b3-92-b5')
FOLDERID_Music: Guid = Guid('4bd8d571-6d19-48d3-be-97-42-22-20-08-0e-43')
FOLDERID_Videos: Guid = Guid('18989b1d-99b5-455b-84-1c-ab-7c-74-e4-dd-fc')
FOLDERID_Ringtones: Guid = Guid('c870044b-f49e-4126-a9-c3-b5-2a-1f-f4-11-e8')
FOLDERID_PublicPictures: Guid = Guid('b6ebfb86-6907-413c-9a-f7-4f-c2-ab-f0-7c-c5')
FOLDERID_PublicMusic: Guid = Guid('3214fab5-9757-4298-bb-61-92-a9-de-aa-44-ff')
FOLDERID_PublicVideos: Guid = Guid('2400183a-6185-49fb-a2-d8-4a-39-2a-60-2b-a3')
FOLDERID_PublicRingtones: Guid = Guid('e555ab60-153b-4d17-9f-04-a5-fe-99-fc-15-ec')
FOLDERID_ResourceDir: Guid = Guid('8ad10c31-2adb-4296-a8-f7-e4-70-12-32-c9-72')
FOLDERID_LocalizedResourcesDir: Guid = Guid('2a00375e-224c-49de-b8-d1-44-0d-f7-ef-3d-dc')
FOLDERID_CommonOEMLinks: Guid = Guid('c1bae2d0-10df-4334-be-dd-7a-a2-0b-22-7a-9d')
FOLDERID_CDBurning: Guid = Guid('9e52ab10-f80d-49df-ac-b8-43-30-f5-68-78-55')
FOLDERID_UserProfiles: Guid = Guid('0762d272-c50a-4bb0-a3-82-69-7d-cd-72-9b-80')
FOLDERID_Playlists: Guid = Guid('de92c1c7-837f-4f69-a3-bb-86-e6-31-20-4a-23')
FOLDERID_SamplePlaylists: Guid = Guid('15ca69b3-30ee-49c1-ac-e1-6b-5e-c3-72-af-b5')
FOLDERID_SampleMusic: Guid = Guid('b250c668-f57d-4ee1-a6-3c-29-0e-e7-d1-aa-1f')
FOLDERID_SamplePictures: Guid = Guid('c4900540-2379-4c75-84-4b-64-e6-fa-f8-71-6b')
FOLDERID_SampleVideos: Guid = Guid('859ead94-2e85-48ad-a7-1a-09-69-cb-56-a6-cd')
FOLDERID_PhotoAlbums: Guid = Guid('69d2cf90-fc33-4fb7-9a-0c-eb-b0-f0-fc-b4-3c')
FOLDERID_Public: Guid = Guid('dfdf76a2-c82a-4d63-90-6a-56-44-ac-45-73-85')
FOLDERID_ChangeRemovePrograms: Guid = Guid('df7266ac-9274-4867-8d-55-3b-d6-61-de-87-2d')
FOLDERID_AppUpdates: Guid = Guid('a305ce99-f527-492b-8b-1a-7e-76-fa-98-d6-e4')
FOLDERID_AddNewPrograms: Guid = Guid('de61d971-5ebc-4f02-a3-a9-6c-82-89-5e-5c-04')
FOLDERID_Downloads: Guid = Guid('374de290-123f-4565-91-64-39-c4-92-5e-46-7b')
FOLDERID_PublicDownloads: Guid = Guid('3d644c9b-1fb8-4f30-9b-45-f6-70-23-5f-79-c0')
FOLDERID_SavedSearches: Guid = Guid('7d1d3a04-debb-4115-95-cf-2f-29-da-29-20-da')
FOLDERID_QuickLaunch: Guid = Guid('52a4f021-7b75-48a9-9f-6b-4b-87-a2-10-bc-8f')
FOLDERID_Contacts: Guid = Guid('56784854-c6cb-462b-81-69-88-e3-50-ac-b8-82')
FOLDERID_SidebarParts: Guid = Guid('a75d362e-50fc-4fb7-ac-2c-a8-be-aa-31-44-93')
FOLDERID_SidebarDefaultParts: Guid = Guid('7b396e54-9ec5-4300-be-0a-24-82-eb-ae-1a-26')
FOLDERID_PublicGameTasks: Guid = Guid('debf2536-e1a8-4c59-b6-a2-41-45-86-47-6a-ea')
FOLDERID_GameTasks: Guid = Guid('054fae61-4dd8-4787-80-b6-09-02-20-c4-b7-00')
FOLDERID_SavedGames: Guid = Guid('4c5c32ff-bb9d-43b0-b5-b4-2d-72-e5-4e-aa-a4')
FOLDERID_Games: Guid = Guid('cac52c1a-b53d-4edc-92-d7-6b-2e-8a-c1-94-34')
FOLDERID_SEARCH_MAPI: Guid = Guid('98ec0e18-2098-4d44-86-44-66-97-93-15-a2-81')
FOLDERID_SEARCH_CSC: Guid = Guid('ee32e446-31ca-4aba-81-4f-a5-eb-d2-fd-6d-5e')
FOLDERID_Links: Guid = Guid('bfb9d5e0-c6a9-404c-b2-b2-ae-6d-b6-af-49-68')
FOLDERID_UsersFiles: Guid = Guid('f3ce0f7c-4901-4acc-86-48-d5-d4-4b-04-ef-8f')
FOLDERID_UsersLibraries: Guid = Guid('a302545d-deff-464b-ab-e8-61-c8-64-8d-93-9b')
FOLDERID_SearchHome: Guid = Guid('190337d1-b8ca-4121-a6-39-6d-47-2d-16-97-2a')
FOLDERID_OriginalImages: Guid = Guid('2c36c0aa-5812-4b87-bf-d0-4c-d0-df-b1-9b-39')
FOLDERID_DocumentsLibrary: Guid = Guid('7b0db17d-9cd2-4a93-97-33-46-cc-89-02-2e-7c')
FOLDERID_MusicLibrary: Guid = Guid('2112ab0a-c86a-4ffe-a3-68-0d-e9-6e-47-01-2e')
FOLDERID_PicturesLibrary: Guid = Guid('a990ae9f-a03b-4e80-94-bc-99-12-d7-50-41-04')
FOLDERID_VideosLibrary: Guid = Guid('491e922f-5643-4af4-a7-eb-4e-7a-13-8d-81-74')
FOLDERID_RecordedTVLibrary: Guid = Guid('1a6fdba2-f42d-4358-a7-98-b7-4d-74-59-26-c5')
FOLDERID_HomeGroup: Guid = Guid('52528a6b-b9e3-4add-b6-0d-58-8c-2d-ba-84-2d')
FOLDERID_HomeGroupCurrentUser: Guid = Guid('9b74b6a3-0dfd-4f11-9e-78-5f-78-00-f2-e7-72')
FOLDERID_DeviceMetadataStore: Guid = Guid('5ce4a5e9-e4eb-479d-b8-9f-13-0c-02-88-61-55')
FOLDERID_Libraries: Guid = Guid('1b3ea5dc-b587-4786-b4-ef-bd-1d-c3-32-ae-ae')
FOLDERID_PublicLibraries: Guid = Guid('48daf80b-e6cf-4f4e-b8-00-0e-69-d8-4e-e3-84')
FOLDERID_UserPinned: Guid = Guid('9e3995ab-1f9c-4f13-b8-27-48-b2-4b-6c-71-74')
FOLDERID_ImplicitAppShortcuts: Guid = Guid('bcb5256f-79f6-4cee-b7-25-dc-34-e4-02-fd-46')
FOLDERID_AccountPictures: Guid = Guid('008ca0b1-55b4-4c56-b8-a8-4d-e4-b2-99-d3-be')
FOLDERID_PublicUserTiles: Guid = Guid('0482af6c-08f1-4c34-8c-90-e1-7e-c9-8b-1e-17')
FOLDERID_AppsFolder: Guid = Guid('1e87508d-89c2-42f0-8a-7e-64-5a-0f-50-ca-58')
FOLDERID_StartMenuAllPrograms: Guid = Guid('f26305ef-6948-40b9-b2-55-81-45-3d-09-c7-85')
FOLDERID_CommonStartMenuPlaces: Guid = Guid('a440879f-87a0-4f7d-b7-00-02-07-b9-66-19-4a')
FOLDERID_ApplicationShortcuts: Guid = Guid('a3918781-e5f2-4890-b3-d9-a7-e5-43-32-32-8c')
FOLDERID_RoamingTiles: Guid = Guid('00bcfc5a-ed94-4e48-96-a1-3f-62-17-f2-19-90')
FOLDERID_RoamedTileImages: Guid = Guid('aaa8d5a5-f1d6-4259-ba-a8-78-e7-ef-60-83-5e')
FOLDERID_Screenshots: Guid = Guid('b7bede81-df94-4682-a7-d8-57-a5-26-20-b8-6f')
FOLDERID_CameraRoll: Guid = Guid('ab5fb87b-7ce2-4f83-91-5d-55-08-46-c9-53-7b')
FOLDERID_SkyDrive: Guid = Guid('a52bba46-e9e1-435f-b3-d9-28-da-a6-48-c0-f6')
FOLDERID_OneDrive: Guid = Guid('a52bba46-e9e1-435f-b3-d9-28-da-a6-48-c0-f6')
FOLDERID_SkyDriveDocuments: Guid = Guid('24d89e24-2f19-4534-9d-de-6a-66-71-fb-b8-fe')
FOLDERID_SkyDrivePictures: Guid = Guid('339719b5-8c47-4894-94-c2-d8-f7-7a-dd-44-a6')
FOLDERID_SkyDriveMusic: Guid = Guid('c3f2459e-80d6-45dc-bf-ef-1f-76-9f-2b-e7-30')
FOLDERID_SkyDriveCameraRoll: Guid = Guid('767e6811-49cb-4273-87-c2-20-f3-55-e1-08-5b')
FOLDERID_SearchHistory: Guid = Guid('0d4c3db6-03a3-462f-a0-e6-08-92-4c-41-b5-d4')
FOLDERID_SearchTemplates: Guid = Guid('7e636bfe-dfa9-4d5e-b4-56-d7-b3-98-51-d8-a9')
FOLDERID_CameraRollLibrary: Guid = Guid('2b20df75-1eda-4039-80-97-38-79-82-27-d5-b7')
FOLDERID_SavedPictures: Guid = Guid('3b193882-d3ad-4eab-96-5a-69-82-9d-1f-b5-9f')
FOLDERID_SavedPicturesLibrary: Guid = Guid('e25b5812-be88-4bd9-94-b0-29-23-34-77-b6-c3')
FOLDERID_RetailDemo: Guid = Guid('12d4c69e-24ad-4923-be-19-31-32-1c-43-a7-67')
FOLDERID_Device: Guid = Guid('1c2ac1dc-4358-4b6c-97-33-af-21-15-65-76-f0')
FOLDERID_DevelopmentFiles: Guid = Guid('dbe8e08e-3053-4bbc-b1-83-2a-7b-2b-19-1e-59')
FOLDERID_Objects3D: Guid = Guid('31c0dd25-9439-4f12-bf-41-7f-f4-ed-a3-87-22')
FOLDERID_AppCaptures: Guid = Guid('edc0fe71-98d8-4f4a-b9-20-c8-dc-13-3c-b1-65')
FOLDERID_LocalDocuments: Guid = Guid('f42ee2d3-909f-4907-88-71-4c-22-fc-0b-f7-56')
FOLDERID_LocalPictures: Guid = Guid('0ddd015d-b06c-45d5-8c-4c-f5-97-13-85-46-39')
FOLDERID_LocalVideos: Guid = Guid('35286a68-3c57-41a1-bb-b1-0e-ae-73-d7-6c-95')
FOLDERID_LocalMusic: Guid = Guid('a0c69a99-21c8-4671-87-03-79-34-16-2f-cf-1d')
FOLDERID_LocalDownloads: Guid = Guid('7d83ee9b-2244-4e70-b1-f5-53-93-04-2a-f1-e4')
FOLDERID_RecordedCalls: Guid = Guid('2f8b40c2-83ed-48ee-b3-83-a1-f1-57-ec-6f-9a')
FOLDERID_AllAppMods: Guid = Guid('7ad67899-66af-43ba-91-56-6a-ad-42-e6-c5-96')
FOLDERID_CurrentAppMods: Guid = Guid('3db40b20-2a30-4dbe-91-7e-77-1d-d2-1d-d0-99')
FOLDERID_AppDataDesktop: Guid = Guid('b2c5e279-7add-439f-b2-8c-c4-1f-e1-bb-f6-72')
FOLDERID_AppDataDocuments: Guid = Guid('7be16610-1f7f-44ac-bf-f0-83-e1-5f-2f-fc-a1')
FOLDERID_AppDataFavorites: Guid = Guid('7cfbefbc-de1f-45aa-b8-43-a5-42-ac-53-6c-c9')
FOLDERID_AppDataProgramData: Guid = Guid('559d40a3-a036-40fa-af-61-84-cb-43-0a-4d-34')
FOLDERID_LocalStorage: Guid = Guid('b3eb08d3-a1f3-496b-86-5a-42-b5-36-cd-a0-ec')
CLSID_InternetShortcut: Guid = Guid('fbf23b40-e3f0-101b-84-88-00-aa-00-3e-56-f8')
CLSID_NetworkDomain: Guid = Guid('46e06680-4bf0-11d1-83-ee-00-a0-c9-0d-c8-49')
CLSID_NetworkServer: Guid = Guid('c0542a90-4bf0-11d1-83-ee-00-a0-c9-0d-c8-49')
CLSID_NetworkShare: Guid = Guid('54a754c0-4bf0-11d1-83-ee-00-a0-c9-0d-c8-49')
CLSID_MyComputer: Guid = Guid('20d04fe0-3aea-1069-a2-d8-08-00-2b-30-30-9d')
CLSID_Internet: Guid = Guid('871c5380-42a0-1069-a2-ea-08-00-2b-30-30-9d')
CLSID_RecycleBin: Guid = Guid('645ff040-5081-101b-9f-08-00-aa-00-2f-95-4e')
CLSID_ControlPanel: Guid = Guid('21ec2020-3aea-1069-a2-dd-08-00-2b-30-30-9d')
CLSID_Printers: Guid = Guid('2227a280-3aea-1069-a2-de-08-00-2b-30-30-9d')
CLSID_MyDocuments: Guid = Guid('450d8fba-ad25-11d0-98-a8-08-00-36-1b-11-03')
STR_MYDOCS_CLSID: String = '{450D8FBA-AD25-11D0-98A8-0800361B1103}'
CATID_BrowsableShellExt: Guid = Guid('00021490-0000-0000-c0-00-00-00-00-00-00-46')
CATID_BrowseInPlace: Guid = Guid('00021491-0000-0000-c0-00-00-00-00-00-00-46')
CATID_DeskBand: Guid = Guid('00021492-0000-0000-c0-00-00-00-00-00-00-46')
CATID_InfoBand: Guid = Guid('00021493-0000-0000-c0-00-00-00-00-00-00-46')
CATID_CommBand: Guid = Guid('00021494-0000-0000-c0-00-00-00-00-00-00-46')
FMTID_Intshcut: Guid = Guid('000214a0-0000-0000-c0-00-00-00-00-00-00-46')
FMTID_InternetSite: Guid = Guid('000214a1-0000-0000-c0-00-00-00-00-00-00-46')
CGID_Explorer: Guid = Guid('000214d0-0000-0000-c0-00-00-00-00-00-00-46')
CGID_ShellDocView: Guid = Guid('000214d1-0000-0000-c0-00-00-00-00-00-00-46')
CGID_ShellServiceObject: Guid = Guid('000214d2-0000-0000-c0-00-00-00-00-00-00-46')
CGID_ExplorerBarDoc: Guid = Guid('000214d3-0000-0000-c0-00-00-00-00-00-00-46')
CLSID_FolderShortcut: Guid = Guid('0afaced1-e828-11d1-91-87-b5-32-f1-e9-57-5d')
CLSID_CFSIconOverlayManager: Guid = Guid('63b51f81-c868-11d0-99-9c-00-c0-4f-d6-55-e1')
CLSID_ShellThumbnailDiskCache: Guid = Guid('1ebdcf80-a200-11d0-a3-a4-00-c0-4f-d7-06-ec')
SID_DefView: Guid = Guid('6d12fe80-7911-11cf-95-34-00-00-c0-5b-ae-0b')
CGID_DefView: Guid = Guid('4af07f10-d231-11d0-b9-42-00-a0-c9-03-12-e1')
CLSID_MenuBand: Guid = Guid('5b4dae26-b807-11d0-98-15-00-c0-4f-d9-19-72')
VID_LargeIcons: Guid = Guid('0057d0e0-3573-11cf-ae-69-08-00-2b-2e-12-62')
VID_SmallIcons: Guid = Guid('089000c0-3573-11cf-ae-69-08-00-2b-2e-12-62')
VID_List: Guid = Guid('0e1fa5e0-3573-11cf-ae-69-08-00-2b-2e-12-62')
VID_Details: Guid = Guid('137e7700-3573-11cf-ae-69-08-00-2b-2e-12-62')
VID_Tile: Guid = Guid('65f125e5-7be1-4810-ba-9d-d2-71-c8-43-2c-e3')
VID_Content: Guid = Guid('30c2c434-0889-4c8d-98-5d-a9-f7-18-30-b0-a9')
VID_Thumbnails: Guid = Guid('8bebb290-52d0-11d0-b7-f4-00-c0-4f-d7-06-ec')
VID_ThumbStrip: Guid = Guid('8eefa624-d1e9-445b-94-b7-74-fb-ce-2e-a1-1a')
SID_SInPlaceBrowser: Guid = Guid('1d2ae02b-3655-46cc-b6-3a-28-59-88-15-3b-ca')
SID_SSearchBoxInfo: Guid = Guid('142daa61-516b-4713-b4-9c-fb-98-5e-f8-29-98')
SID_CommandsPropertyBag: Guid = Guid('6e043250-4416-485c-b1-43-e6-2a-76-0d-9f-e5')
CLSID_CUrlHistory: Guid = Guid('3c374a40-bae4-11cf-bf-7d-00-aa-00-69-46-ee')
CLSID_CURLSearchHook: Guid = Guid('cfbfae00-17a6-11d0-99-cb-00-c0-4f-d6-44-97')
CLSID_AutoComplete: Guid = Guid('00bb2763-6a77-11d0-a5-35-00-c0-4f-d7-d0-62')
CLSID_ACLHistory: Guid = Guid('00bb2764-6a77-11d0-a5-35-00-c0-4f-d7-d0-62')
CLSID_ACListISF: Guid = Guid('03c036f1-a186-11d0-82-4a-00-aa-00-5b-43-83')
CLSID_ACLMRU: Guid = Guid('6756a641-de71-11d0-83-1b-00-aa-00-5b-43-83')
CLSID_ACLMulti: Guid = Guid('00bb2765-6a77-11d0-a5-35-00-c0-4f-d7-d0-62')
CLSID_ACLCustomMRU: Guid = Guid('6935db93-21e8-4ccc-be-b9-9f-e3-c7-7a-29-7a')
CLSID_ProgressDialog: Guid = Guid('f8383852-fcd3-11d1-a6-b9-00-60-97-df-5b-d4')
SID_STopLevelBrowser: Guid = Guid('4c96be40-915c-11cf-99-d3-00-aa-00-4a-e8-37')
CLSID_FileTypes: Guid = Guid('b091e540-83e3-11cf-a7-13-00-20-af-d7-97-62')
CLSID_ActiveDesktop: Guid = Guid('75048700-ef1f-11d0-98-88-00-60-97-de-ac-f9')
CLSID_QueryAssociations: Guid = Guid('a07034fd-6caa-4954-ac-3f-97-a2-72-16-f9-8a')
CLSID_LinkColumnProvider: Guid = Guid('24f14f02-7b1c-11d1-83-8f-00-00-f8-04-61-cf')
CGID_ShortCut: Guid = Guid('93a68750-951a-11d1-94-6f-00-00-00-00-00-00')
CLSID_InternetButtons: Guid = Guid('1e796980-9cc5-11d1-a8-3f-00-c0-4f-c9-9d-61')
CLSID_MSOButtons: Guid = Guid('178f34b8-a282-11d2-86-c5-00-c0-4f-8e-ea-99')
CLSID_ToolbarExtButtons: Guid = Guid('2ce4b5d8-a28f-11d2-86-c5-00-c0-4f-8e-ea-99')
CLSID_DarwinAppPublisher: Guid = Guid('cfccc7a0-a282-11d1-90-82-00-60-08-05-93-82')
CLSID_DocHostUIHandler: Guid = Guid('7057e952-bd1b-11d1-89-19-00-c0-4f-c2-c8-36')
FMTID_ShellDetails: Guid = Guid('28636aa6-953d-11d2-b5-d6-00-c0-4f-d9-18-d0')
PID_FINDDATA: UInt32 = 0
PID_NETRESOURCE: UInt32 = 1
PID_DESCRIPTIONID: UInt32 = 2
PID_WHICHFOLDER: UInt32 = 3
PID_NETWORKLOCATION: UInt32 = 4
PID_COMPUTERNAME: UInt32 = 5
FMTID_Storage: Guid = Guid('b725f130-47ef-101a-a5-f1-02-60-8c-9e-eb-ac')
FMTID_ImageProperties: Guid = Guid('14b81da1-0135-4d31-96-d9-6c-bf-c9-67-1a-99')
FMTID_CustomImageProperties: Guid = Guid('7ecd8b0e-c136-4a9b-94-11-4e-bd-66-73-cc-c3')
FMTID_LibraryProperties: Guid = Guid('5d76b67f-9b3d-44bb-b6-ae-25-da-4f-63-8a-67')
FMTID_Displaced: Guid = Guid('9b174b33-40ff-11d2-a2-7e-00-c0-4f-c3-08-71')
PID_DISPLACED_FROM: UInt32 = 2
PID_DISPLACED_DATE: UInt32 = 3
FMTID_Briefcase: Guid = Guid('328d8b21-7729-4bfc-95-4c-90-2b-32-9d-56-b0')
PID_SYNC_COPY_IN: UInt32 = 2
FMTID_Misc: Guid = Guid('9b174b34-40ff-11d2-a2-7e-00-c0-4f-c3-08-71')
PID_MISC_STATUS: UInt32 = 2
PID_MISC_ACCESSCOUNT: UInt32 = 3
PID_MISC_OWNER: UInt32 = 4
PID_HTMLINFOTIPFILE: UInt32 = 5
PID_MISC_PICS: UInt32 = 6
FMTID_WebView: Guid = Guid('f2275480-f782-4291-bd-94-f1-36-93-51-3a-ec')
PID_DISPLAY_PROPERTIES: UInt32 = 0
PID_INTROTEXT: UInt32 = 1
FMTID_MUSIC: Guid = Guid('56a3372e-ce9c-11d2-9f-0e-00-60-97-c6-86-f6')
PIDSI_ARTIST: UInt32 = 2
PIDSI_SONGTITLE: UInt32 = 3
PIDSI_ALBUM: UInt32 = 4
PIDSI_YEAR: UInt32 = 5
PIDSI_COMMENT: UInt32 = 6
PIDSI_TRACK: UInt32 = 7
PIDSI_GENRE: UInt32 = 11
PIDSI_LYRICS: UInt32 = 12
FMTID_DRM: Guid = Guid('aeac19e4-89ae-4508-b9-b7-bb-86-7a-be-e2-ed')
PIDDRSI_PROTECTED: UInt32 = 2
PIDDRSI_DESCRIPTION: UInt32 = 3
PIDDRSI_PLAYCOUNT: UInt32 = 4
PIDDRSI_PLAYSTARTS: UInt32 = 5
PIDDRSI_PLAYEXPIRES: UInt32 = 6
PIDVSI_STREAM_NAME: UInt32 = 2
PIDVSI_FRAME_WIDTH: UInt32 = 3
PIDVSI_FRAME_HEIGHT: UInt32 = 4
PIDVSI_TIMELENGTH: UInt32 = 7
PIDVSI_FRAME_COUNT: UInt32 = 5
PIDVSI_FRAME_RATE: UInt32 = 6
PIDVSI_DATA_RATE: UInt32 = 8
PIDVSI_SAMPLE_SIZE: UInt32 = 9
PIDVSI_COMPRESSION: UInt32 = 10
PIDVSI_STREAM_NUMBER: UInt32 = 11
PIDASI_FORMAT: UInt32 = 2
PIDASI_TIMELENGTH: UInt32 = 3
PIDASI_AVG_DATA_RATE: UInt32 = 4
PIDASI_SAMPLE_RATE: UInt32 = 5
PIDASI_SAMPLE_SIZE: UInt32 = 6
PIDASI_CHANNEL_COUNT: UInt32 = 7
PIDASI_STREAM_NUMBER: UInt32 = 8
PIDASI_STREAM_NAME: UInt32 = 9
PIDASI_COMPRESSION: UInt32 = 10
PID_CONTROLPANEL_CATEGORY: UInt32 = 2
FMTID_Volume: Guid = Guid('9b174b35-40ff-11d2-a2-7e-00-c0-4f-c3-08-71')
PID_VOLUME_FREE: UInt32 = 2
PID_VOLUME_CAPACITY: UInt32 = 3
PID_VOLUME_FILESYSTEM: UInt32 = 4
PID_SHARE_CSC_STATUS: UInt32 = 2
PID_LINK_TARGET: UInt32 = 2
PID_LINK_TARGET_TYPE: UInt32 = 3
FMTID_Query: Guid = Guid('49691c90-7e17-101a-a9-1c-08-00-2b-2e-cd-a9')
PID_QUERY_RANK: UInt32 = 2
CLSID_HWShellExecute: Guid = Guid('ffb8655f-81b9-4fce-b8-9c-9a-6b-a7-6d-13-e7')
CLSID_DragDropHelper: Guid = Guid('4657278a-411b-11d2-83-9a-00-c0-4f-d9-18-d0')
CLSID_CAnchorBrowsePropertyPage: Guid = Guid('3050f3bb-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CLSID_CImageBrowsePropertyPage: Guid = Guid('3050f3b3-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CLSID_CDocBrowsePropertyPage: Guid = Guid('3050f3b4-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
SID_STopWindow: Guid = Guid('49e1b500-4636-11d3-97-f7-00-c0-4f-45-d0-b3')
SID_SGetViewFromViewDual: Guid = Guid('889a935d-971e-4b12-b9-0c-24-df-c9-e1-e5-e8')
CLSID_FolderItemsMultiLevel: Guid = Guid('53c74826-ab99-4d33-ac-a4-31-17-f5-1d-37-88')
CLSID_NewMenu: Guid = Guid('d969a300-e7ff-11d0-a9-3b-00-a0-c9-0f-27-19')
BHID_SFObject: Guid = Guid('3981e224-f559-11d3-8e-3a-00-c0-4f-68-37-d5')
BHID_SFUIObject: Guid = Guid('3981e225-f559-11d3-8e-3a-00-c0-4f-68-37-d5')
BHID_SFViewObject: Guid = Guid('3981e226-f559-11d3-8e-3a-00-c0-4f-68-37-d5')
BHID_Storage: Guid = Guid('3981e227-f559-11d3-8e-3a-00-c0-4f-68-37-d5')
BHID_Stream: Guid = Guid('1cebb3ab-7c10-499a-a4-17-92-ca-16-c4-cb-83')
BHID_RandomAccessStream: Guid = Guid('f16fc93b-77ae-4cfe-bd-a7-a8-66-ee-a6-87-8d')
BHID_LinkTargetItem: Guid = Guid('3981e228-f559-11d3-8e-3a-00-c0-4f-68-37-d5')
BHID_StorageEnum: Guid = Guid('4621a4e3-f0d6-4773-8a-9c-46-e7-7b-17-48-40')
BHID_Transfer: Guid = Guid('d5e346a1-f753-4932-b4-03-45-74-80-0e-24-98')
BHID_PropertyStore: Guid = Guid('0384e1a4-1523-439c-a4-c8-ab-91-10-52-f5-86')
BHID_ThumbnailHandler: Guid = Guid('7b2e650a-8e20-4f4a-b0-9e-65-97-af-c7-2f-b0')
BHID_EnumItems: Guid = Guid('94f60519-2850-4924-aa-5a-d1-5e-84-86-80-39')
BHID_DataObject: Guid = Guid('b8c0bd9f-ed24-455c-83-e6-d5-39-0c-4f-e8-c4')
BHID_AssociationArray: Guid = Guid('bea9ef17-82f1-4f60-92-84-4f-8d-b7-5c-3b-e9')
BHID_Filter: Guid = Guid('38d08778-f557-4690-9e-bf-ba-54-70-6a-d8-f7')
BHID_EnumAssocHandlers: Guid = Guid('b8ab0b9c-c2ec-4f7a-91-8d-31-49-00-e6-28-0a')
BHID_StorageItem: Guid = Guid('404e2109-77d2-4699-a5-a0-4f-df-10-db-98-37')
BHID_FilePlaceholder: Guid = Guid('8677dceb-aae0-4005-8d-3d-54-7f-a8-52-f8-25')
CATID_FilePlaceholderMergeHandler: Guid = Guid('3e9c9a51-d4aa-4870-b4-7c-74-24-b4-91-f1-cc')
SID_CtxQueryAssociations: Guid = Guid('faadfc40-b777-4b69-aa-81-77-03-5e-f0-e6-e8')
CLSID_QuickLinks: Guid = Guid('0e5cbf21-d15f-11d0-83-01-00-aa-00-5b-43-83')
CLSID_ISFBand: Guid = Guid('d82be2b0-5764-11d0-a9-6e-00-c0-4f-d7-05-a2')
CLSID_ShellFldSetExt: Guid = Guid('6d5313c0-8c62-11d1-b2-cd-00-60-97-df-8c-11')
SID_SMenuBandChild: Guid = Guid('ed9cc020-08b9-11d1-98-23-00-c0-4f-d9-19-72')
SID_SMenuBandParent: Guid = Guid('8c278eec-3eab-11d1-8c-b0-00-c0-4f-d9-18-d0')
SID_SMenuPopup: Guid = Guid('d1e7afeb-6a2e-11d0-8c-78-00-c0-4f-d9-18-b4')
SID_SMenuBandBottomSelected: Guid = Guid('165ebaf4-6d51-11d2-83-ad-00-c0-4f-d9-18-d0')
SID_SMenuBandBottom: Guid = Guid('743ca664-0deb-11d1-98-25-00-c0-4f-d9-19-72')
SID_MenuShellFolder: Guid = Guid('a6c17eb4-2d65-11d2-83-8f-00-c0-4f-d9-18-d0')
SID_SMenuBandContextMenuModifier: Guid = Guid('39545874-7162-465e-b7-83-2a-a1-87-4f-ef-81')
SID_SMenuBandBKContextMenu: Guid = Guid('164bbd86-1d0d-4de0-9a-3b-d9-72-96-47-c2-b8')
CGID_MENUDESKBAR: Guid = Guid('5c9f0a12-959e-11d0-a3-a4-00-a0-c9-08-26-36')
SID_SMenuBandTop: Guid = Guid('9493a810-ec38-11d0-bc-46-00-aa-00-6c-e2-f5')
CLSID_MenuToolbarBase: Guid = Guid('40b96610-b522-11d1-b3-b4-00-aa-00-6e-fd-e7')
CLSID_MenuBandSite: Guid = Guid('e13ef4e4-d2f2-11d0-98-16-00-c0-4f-d9-19-72')
SID_SCommDlgBrowser: Guid = Guid('80f30233-b7df-11d2-a3-3b-00-60-97-df-5b-d4')
CPFG_LOGON_USERNAME: Guid = Guid('da15bbe8-954d-4fd3-b0-f4-1f-b5-b9-0b-17-4b')
CPFG_LOGON_PASSWORD: Guid = Guid('60624cfa-a477-47b1-8a-8e-3a-4a-19-98-18-27')
CPFG_SMARTCARD_USERNAME: Guid = Guid('3e1ecf69-568c-4d96-9d-59-46-44-41-74-e2-d6')
CPFG_SMARTCARD_PIN: Guid = Guid('4fe5263b-9181-46c1-b0-a4-9d-ed-d4-db-7d-ea')
CPFG_CREDENTIAL_PROVIDER_LOGO: Guid = Guid('2d837775-f6cd-464e-a7-45-48-2f-d0-b4-74-93')
CPFG_CREDENTIAL_PROVIDER_LABEL: Guid = Guid('286bbff3-bad4-438f-b0-07-79-b7-26-7c-3d-48')
CPFG_STANDALONE_SUBMIT_BUTTON: Guid = Guid('0b7b0ad8-cc36-4d59-80-2b-82-f7-14-fa-70-22')
CPFG_STYLE_LINK_AS_BUTTON: Guid = Guid('088fa508-94a6-4430-a4-cb-6f-c6-e3-c0-b9-e2')
FOLDERTYPEID_Invalid: Guid = Guid('57807898-8c4f-4462-bb-63-71-04-23-80-b1-09')
FOLDERTYPEID_Generic: Guid = Guid('5c4f28b5-f869-4e84-8e-60-f1-1d-b9-7c-5c-c7')
FOLDERTYPEID_GenericSearchResults: Guid = Guid('7fde1a1e-8b31-49a5-93-b8-6b-e1-4c-fa-49-43')
FOLDERTYPEID_GenericLibrary: Guid = Guid('5f4eab9a-6833-4f61-89-9d-31-cf-46-97-9d-49')
FOLDERTYPEID_Documents: Guid = Guid('7d49d726-3c21-4f05-99-aa-fd-c2-c9-47-46-56')
FOLDERTYPEID_Pictures: Guid = Guid('b3690e58-e961-423b-b6-87-38-6e-bf-d8-32-39')
FOLDERTYPEID_Music: Guid = Guid('94d6ddcc-4a68-4175-a3-74-bd-58-4a-51-0b-78')
FOLDERTYPEID_Videos: Guid = Guid('5fa96407-7e77-483c-ac-93-69-1d-05-85-0d-e8')
FOLDERTYPEID_Downloads: Guid = Guid('885a186e-a440-4ada-81-2b-db-87-1b-94-22-59')
FOLDERTYPEID_UserFiles: Guid = Guid('cd0fc69b-71e2-46e5-96-90-5b-cd-9f-57-aa-b3')
FOLDERTYPEID_UsersLibraries: Guid = Guid('c4d98f09-6124-4fe0-99-42-82-64-16-08-2d-a9')
FOLDERTYPEID_OtherUsers: Guid = Guid('b337fd00-9dd5-4635-a6-d4-da-33-fd-10-2b-7a')
FOLDERTYPEID_PublishedItems: Guid = Guid('7f2f5b96-ff74-41da-af-d8-1c-78-a5-f3-ae-a2')
FOLDERTYPEID_Communications: Guid = Guid('91475fe5-586b-4eba-8d-75-d1-74-34-b8-cd-f6')
FOLDERTYPEID_Contacts: Guid = Guid('de2b70ec-9bf7-4a93-bd-3d-24-3f-78-81-d4-92')
FOLDERTYPEID_StartMenu: Guid = Guid('ef87b4cb-f2ce-4785-86-58-4c-a6-c6-3e-38-c6')
FOLDERTYPEID_RecordedTV: Guid = Guid('5557a28f-5da6-4f83-88-09-c2-c9-8a-11-a6-fa')
FOLDERTYPEID_SavedGames: Guid = Guid('d0363307-28cb-4106-9f-23-29-56-e3-e5-e0-e7')
FOLDERTYPEID_OpenSearch: Guid = Guid('8faf9629-1980-46ff-80-23-9d-ce-ab-9c-3e-e3')
FOLDERTYPEID_SearchConnector: Guid = Guid('982725ee-6f47-479e-b4-47-81-2b-fa-7d-2e-8f')
FOLDERTYPEID_AccountPictures: Guid = Guid('db2a5d8f-06e6-4007-ab-a6-af-87-7d-52-6e-a6')
FOLDERTYPEID_Games: Guid = Guid('b689b0d0-76d3-4cbb-87-f7-58-5d-0e-0c-e0-70')
FOLDERTYPEID_ControlPanelCategory: Guid = Guid('de4f0660-fa10-4b8f-a4-94-06-8b-20-b2-23-07')
FOLDERTYPEID_ControlPanelClassic: Guid = Guid('0c3794f3-b545-43aa-a3-29-c3-74-30-c5-8d-2a')
FOLDERTYPEID_Printers: Guid = Guid('2c7bbec6-c844-4a0a-91-fa-ce-f6-f5-9c-fd-a1')
FOLDERTYPEID_RecycleBin: Guid = Guid('d6d9e004-cd87-442b-9d-57-5e-0a-eb-4f-6f-72')
FOLDERTYPEID_SoftwareExplorer: Guid = Guid('d674391b-52d9-4e07-83-4e-67-c9-86-10-f3-9d')
FOLDERTYPEID_CompressedFolder: Guid = Guid('80213e82-bcfd-4c4f-88-17-bb-27-60-12-67-a9')
FOLDERTYPEID_NetworkExplorer: Guid = Guid('25cc242b-9a7c-4f51-80-e0-7a-29-28-fe-be-42')
FOLDERTYPEID_Searches: Guid = Guid('0b0ba2e3-405f-415e-a6-ee-ca-d6-25-20-78-53')
FOLDERTYPEID_SearchHome: Guid = Guid('834d8a44-0974-4ed6-86-6e-f2-03-d8-0b-38-10')
FOLDERTYPEID_StorageProviderGeneric: Guid = Guid('4f01ebc5-2385-41f2-a2-8e-2c-5c-91-fb-56-e0')
FOLDERTYPEID_StorageProviderDocuments: Guid = Guid('dd61bd66-70e8-48dd-96-55-65-c5-e1-aa-c2-d1')
FOLDERTYPEID_StorageProviderPictures: Guid = Guid('71d642a9-f2b1-42cd-ad-92-eb-93-00-c7-cc-0a')
FOLDERTYPEID_StorageProviderMusic: Guid = Guid('672ecd7e-af04-4399-87-5c-02-90-84-5b-62-47')
FOLDERTYPEID_StorageProviderVideos: Guid = Guid('51294da1-d7b1-485b-9e-9a-17-cf-fe-33-e1-87')
SYNCMGR_OBJECTID_Icon: Guid = Guid('6dbc85c3-5d07-4c72-a7-77-7f-ec-78-07-2c-06')
SYNCMGR_OBJECTID_EventStore: Guid = Guid('4bef34b9-a786-4075-ba-88-0c-2b-9d-89-a9-8f')
SYNCMGR_OBJECTID_ConflictStore: Guid = Guid('d78181f4-2389-47e4-a9-60-60-bc-c2-ed-93-0b')
SYNCMGR_OBJECTID_BrowseContent: Guid = Guid('57cbb584-e9b4-47ae-a1-20-c4-df-33-35-de-e2')
SYNCMGR_OBJECTID_ShowSchedule: Guid = Guid('edc6f3e3-8441-4109-ad-f3-6c-1c-a0-b7-de-47')
SYNCMGR_OBJECTID_QueryBeforeActivate: Guid = Guid('d882d80b-e7aa-49ed-86-b7-e6-e1-f7-14-cd-fe')
SYNCMGR_OBJECTID_QueryBeforeDeactivate: Guid = Guid('a0efc282-60e0-460e-93-74-ea-88-51-3c-fc-80')
SYNCMGR_OBJECTID_QueryBeforeEnable: Guid = Guid('04cbf7f0-5beb-4de1-bc-90-90-83-45-c4-80-f6')
SYNCMGR_OBJECTID_QueryBeforeDisable: Guid = Guid('bb5f64aa-f004-4eb5-8e-4d-26-75-19-66-34-4c')
SYNCMGR_OBJECTID_QueryBeforeDelete: Guid = Guid('f76c3397-afb3-45d7-a5-9f-5a-49-e9-05-43-7e')
SYNCMGR_OBJECTID_EventLinkClick: Guid = Guid('2203bdc1-1af1-4082-8c-30-28-39-9f-41-38-4c')
EP_NavPane: Guid = Guid('cb316b22-25f7-42b8-8a-09-54-0d-23-a4-3c-2f')
EP_Commands: Guid = Guid('d9745868-ca5f-4a76-91-cd-f5-a1-29-fb-b0-76')
EP_Commands_Organize: Guid = Guid('72e81700-e3ec-4660-bf-24-3c-3b-7b-64-88-06')
EP_Commands_View: Guid = Guid('21f7c32d-eeaa-439b-bb-51-37-b9-6f-d6-a9-43')
EP_DetailsPane: Guid = Guid('43abf98b-89b8-472d-b9-ce-e6-9b-82-29-f0-19')
EP_PreviewPane: Guid = Guid('893c63d1-45c8-4d17-be-19-22-3b-e7-1b-e3-65')
EP_QueryPane: Guid = Guid('65bcde4f-4f07-4f27-83-a7-1a-fc-a4-df-7d-dd')
EP_AdvQueryPane: Guid = Guid('b4e9db8b-34ba-4c39-b5-cc-16-a1-bd-2c-41-1c')
EP_StatusBar: Guid = Guid('65fe56ce-5cfe-4bc4-ad-8a-7a-e3-fe-7e-8f-7c')
EP_Ribbon: Guid = Guid('d27524a8-c9f2-4834-a1-06-df-88-89-fd-4f-37')
CATID_LocationFactory: Guid = Guid('965c4d51-8b76-4e57-80-b7-56-4d-2e-a4-b5-5e')
CATID_LocationProvider: Guid = Guid('1b3ca474-2614-414b-b8-13-1a-ce-ca-3e-3d-d8')
ItemCount_Property_GUID: Guid = Guid('abbf5c45-5ccc-47b7-bb-4e-87-cb-87-bb-d1-62')
SelectedItemCount_Property_GUID: Guid = Guid('8fe316d2-0e52-460a-9c-1e-48-f2-73-d4-70-a3')
ItemIndex_Property_GUID: Guid = Guid('92a053da-2969-4021-bf-27-51-4c-fc-2e-4a-69')
CATID_SearchableApplication: Guid = Guid('366c292a-d9b3-4dbf-bb-70-e6-2e-c3-d0-bb-bf')
IDD_WIZEXTN_FIRST: UInt32 = 20480
IDD_WIZEXTN_LAST: UInt32 = 20736
SHPWHF_NORECOMPRESS: UInt32 = 1
SHPWHF_NONETPLACECREATE: UInt32 = 2
SHPWHF_NOFILESELECTOR: UInt32 = 4
SHPWHF_USEMRU: UInt32 = 8
SHPWHF_ANYLOCATION: UInt32 = 256
SHPWHF_VALIDATEVIAWEBFOLDERS: UInt32 = 65536
ACDD_VISIBLE: UInt32 = 1
PROPSTR_EXTENSIONCOMPLETIONSTATE: String = 'ExtensionCompletionState'
SID_SCommandBarState: Guid = Guid('b99eaa5c-3850-4400-bc-33-2c-e5-34-04-8b-f8')
NSTCDHPOS_ONTOP: Int32 = -1
FVSIF_RECT: UInt32 = 1
FVSIF_PINNED: UInt32 = 2
FVSIF_NEWFAILED: UInt32 = 134217728
FVSIF_NEWFILE: UInt32 = 2147483648
FVSIF_CANVIEWIT: UInt32 = 1073741824
FCIDM_TOOLBAR: UInt32 = 40960
FCIDM_STATUS: UInt32 = 40961
IDC_OFFLINE_HAND: UInt32 = 103
IDC_PANTOOL_HAND_OPEN: UInt32 = 104
IDC_PANTOOL_HAND_CLOSED: UInt32 = 105
PANE_NONE: UInt32 = 4294967295
PANE_ZONE: UInt32 = 1
PANE_OFFLINE: UInt32 = 2
PANE_PRINTER: UInt32 = 3
PANE_SSL: UInt32 = 4
PANE_NAVIGATION: UInt32 = 5
PANE_PROGRESS: UInt32 = 6
PANE_PRIVACY: UInt32 = 7
DWFRF_NORMAL: UInt32 = 0
DWFRF_DELETECONFIGDATA: UInt32 = 1
DWFAF_HIDDEN: UInt32 = 1
DWFAF_GROUP1: UInt32 = 2
DWFAF_GROUP2: UInt32 = 4
DWFAF_AUTOHIDE: UInt32 = 16
SHIMSTCAPFLAG_LOCKABLE: UInt32 = 1
SHIMSTCAPFLAG_PURGEABLE: UInt32 = 2
ISFB_MASK_STATE: UInt32 = 1
ISFB_MASK_BKCOLOR: UInt32 = 2
ISFB_MASK_VIEWMODE: UInt32 = 4
ISFB_MASK_SHELLFOLDER: UInt32 = 8
ISFB_MASK_IDLIST: UInt32 = 16
ISFB_MASK_COLORS: UInt32 = 32
ISFB_STATE_DEFAULT: UInt32 = 0
ISFB_STATE_DEBOSSED: UInt32 = 1
ISFB_STATE_ALLOWRENAME: UInt32 = 2
ISFB_STATE_NOSHOWTEXT: UInt32 = 4
ISFB_STATE_CHANNELBAR: UInt32 = 16
ISFB_STATE_QLINKSMODE: UInt32 = 32
ISFB_STATE_FULLOPEN: UInt32 = 64
ISFB_STATE_NONAMESORT: UInt32 = 128
ISFB_STATE_BTNMINSIZE: UInt32 = 256
ISFBVIEWMODE_SMALLICONS: UInt32 = 1
ISFBVIEWMODE_LARGEICONS: UInt32 = 2
ISFBVIEWMODE_LOGOS: UInt32 = 3
DBC_GS_IDEAL: UInt32 = 0
DBC_GS_SIZEDOWN: UInt32 = 1
DBC_HIDE: UInt32 = 0
DBC_SHOW: UInt32 = 1
DBC_SHOWOBSCURE: UInt32 = 2
SSM_CLEAR: UInt32 = 0
SSM_SET: UInt32 = 1
SSM_REFRESH: UInt32 = 2
SSM_UPDATE: UInt32 = 4
SCHEME_DISPLAY: UInt32 = 1
SCHEME_EDIT: UInt32 = 2
SCHEME_LOCAL: UInt32 = 4
SCHEME_GLOBAL: UInt32 = 8
SCHEME_REFRESH: UInt32 = 16
SCHEME_UPDATE: UInt32 = 32
SCHEME_DONOTUSE: UInt32 = 64
SCHEME_CREATE: UInt32 = 128
GADOF_DIRTY: UInt32 = 1
SHCDF_UPDATEITEM: UInt32 = 1
PPCF_ADDQUOTES: UInt32 = 1
PPCF_ADDARGUMENTS: UInt32 = 3
PPCF_NODIRECTORIES: UInt32 = 16
PPCF_FORCEQUALIFY: UInt32 = 64
PPCF_LONGESTPOSSIBLE: UInt32 = 128
OPENPROPS_NONE: UInt32 = 0
OPENPROPS_INHIBITPIF: UInt32 = 32768
GETPROPS_NONE: UInt32 = 0
SETPROPS_NONE: UInt32 = 0
CLOSEPROPS_NONE: UInt32 = 0
CLOSEPROPS_DISCARD: UInt32 = 1
TBIF_APPEND: UInt32 = 0
TBIF_PREPEND: UInt32 = 1
TBIF_REPLACE: UInt32 = 2
TBIF_DEFAULT: UInt32 = 0
TBIF_INTERNETBAR: UInt32 = 65536
TBIF_STANDARDTOOLBAR: UInt32 = 131072
TBIF_NOTOOLBAR: UInt32 = 196608
SFVM_REARRANGE: UInt32 = 1
SFVM_ADDOBJECT: UInt32 = 3
SFVM_REMOVEOBJECT: UInt32 = 6
SFVM_UPDATEOBJECT: UInt32 = 7
SFVM_GETSELECTEDOBJECTS: UInt32 = 9
SFVM_SETITEMPOS: UInt32 = 14
SFVM_SETCLIPBOARD: UInt32 = 16
SFVM_SETPOINTS: UInt32 = 23
GIL_OPENICON: UInt32 = 1
GIL_FORSHELL: UInt32 = 2
GIL_ASYNC: UInt32 = 32
GIL_DEFAULTICON: UInt32 = 64
GIL_FORSHORTCUT: UInt32 = 128
GIL_CHECKSHIELD: UInt32 = 512
GIL_SIMULATEDOC: UInt32 = 1
GIL_PERINSTANCE: UInt32 = 2
GIL_PERCLASS: UInt32 = 4
GIL_NOTFILENAME: UInt32 = 8
GIL_DONTCACHE: UInt32 = 16
GIL_SHIELD: UInt32 = 512
GIL_FORCENOSHIELD: UInt32 = 1024
SIOM_OVERLAYINDEX: UInt32 = 1
SIOM_ICONINDEX: UInt32 = 2
SIOM_RESERVED_SHARED: UInt32 = 0
SIOM_RESERVED_LINK: UInt32 = 1
SIOM_RESERVED_SLOWFILE: UInt32 = 2
SIOM_RESERVED_DEFAULT: UInt32 = 3
OI_DEFAULT: UInt32 = 0
OI_ASYNC: UInt32 = 4294962926
IDO_SHGIOI_SHARE: UInt32 = 268435455
IDO_SHGIOI_LINK: UInt32 = 268435454
IDO_SHGIOI_SLOWFILE: UInt64 = 4294967293
IDO_SHGIOI_DEFAULT: UInt64 = 4294967292
NT_CONSOLE_PROPS_SIG: UInt32 = 2684354562
NT_FE_CONSOLE_PROPS_SIG: UInt32 = 2684354564
EXP_DARWIN_ID_SIG: UInt32 = 2684354566
EXP_SPECIAL_FOLDER_SIG: UInt32 = 2684354565
EXP_SZ_LINK_SIG: UInt32 = 2684354561
EXP_SZ_ICON_SIG: UInt32 = 2684354567
EXP_PROPERTYSTORAGE_SIG: UInt32 = 2684354569
FCIDM_SHVIEWFIRST: UInt32 = 0
FCIDM_SHVIEWLAST: UInt32 = 32767
FCIDM_BROWSERFIRST: UInt32 = 40960
FCIDM_BROWSERLAST: UInt32 = 48896
FCIDM_GLOBALFIRST: UInt32 = 32768
FCIDM_GLOBALLAST: UInt32 = 40959
FCIDM_MENU_FILE: UInt32 = 32768
FCIDM_MENU_EDIT: UInt32 = 32832
FCIDM_MENU_VIEW: UInt32 = 32896
FCIDM_MENU_VIEW_SEP_OPTIONS: UInt32 = 32897
FCIDM_MENU_TOOLS: UInt32 = 32960
FCIDM_MENU_TOOLS_SEP_GOTO: UInt32 = 32961
FCIDM_MENU_HELP: UInt32 = 33024
FCIDM_MENU_FIND: UInt32 = 33088
FCIDM_MENU_EXPLORE: UInt32 = 33104
FCIDM_MENU_FAVORITES: UInt32 = 33136
OFASI_EDIT: UInt32 = 1
OFASI_OPENDESKTOP: UInt32 = 2
CSIDL_DESKTOP: UInt32 = 0
CSIDL_INTERNET: UInt32 = 1
CSIDL_PROGRAMS: UInt32 = 2
CSIDL_CONTROLS: UInt32 = 3
CSIDL_PRINTERS: UInt32 = 4
CSIDL_PERSONAL: UInt32 = 5
CSIDL_FAVORITES: UInt32 = 6
CSIDL_STARTUP: UInt32 = 7
CSIDL_RECENT: UInt32 = 8
CSIDL_SENDTO: UInt32 = 9
CSIDL_BITBUCKET: UInt32 = 10
CSIDL_STARTMENU: UInt32 = 11
CSIDL_MYDOCUMENTS: UInt32 = 5
CSIDL_MYMUSIC: UInt32 = 13
CSIDL_MYVIDEO: UInt32 = 14
CSIDL_DESKTOPDIRECTORY: UInt32 = 16
CSIDL_DRIVES: UInt32 = 17
CSIDL_NETWORK: UInt32 = 18
CSIDL_NETHOOD: UInt32 = 19
CSIDL_FONTS: UInt32 = 20
CSIDL_TEMPLATES: UInt32 = 21
CSIDL_COMMON_STARTMENU: UInt32 = 22
CSIDL_COMMON_PROGRAMS: UInt32 = 23
CSIDL_COMMON_STARTUP: UInt32 = 24
CSIDL_COMMON_DESKTOPDIRECTORY: UInt32 = 25
CSIDL_APPDATA: UInt32 = 26
CSIDL_PRINTHOOD: UInt32 = 27
CSIDL_LOCAL_APPDATA: UInt32 = 28
CSIDL_ALTSTARTUP: UInt32 = 29
CSIDL_COMMON_ALTSTARTUP: UInt32 = 30
CSIDL_COMMON_FAVORITES: UInt32 = 31
CSIDL_INTERNET_CACHE: UInt32 = 32
CSIDL_COOKIES: UInt32 = 33
CSIDL_HISTORY: UInt32 = 34
CSIDL_COMMON_APPDATA: UInt32 = 35
CSIDL_WINDOWS: UInt32 = 36
CSIDL_SYSTEM: UInt32 = 37
CSIDL_PROGRAM_FILES: UInt32 = 38
CSIDL_MYPICTURES: UInt32 = 39
CSIDL_PROFILE: UInt32 = 40
CSIDL_SYSTEMX86: UInt32 = 41
CSIDL_PROGRAM_FILESX86: UInt32 = 42
CSIDL_PROGRAM_FILES_COMMON: UInt32 = 43
CSIDL_PROGRAM_FILES_COMMONX86: UInt32 = 44
CSIDL_COMMON_TEMPLATES: UInt32 = 45
CSIDL_COMMON_DOCUMENTS: UInt32 = 46
CSIDL_COMMON_ADMINTOOLS: UInt32 = 47
CSIDL_ADMINTOOLS: UInt32 = 48
CSIDL_CONNECTIONS: UInt32 = 49
CSIDL_COMMON_MUSIC: UInt32 = 53
CSIDL_COMMON_PICTURES: UInt32 = 54
CSIDL_COMMON_VIDEO: UInt32 = 55
CSIDL_RESOURCES: UInt32 = 56
CSIDL_RESOURCES_LOCALIZED: UInt32 = 57
CSIDL_COMMON_OEM_LINKS: UInt32 = 58
CSIDL_CDBURN_AREA: UInt32 = 59
CSIDL_COMPUTERSNEARME: UInt32 = 61
CSIDL_FLAG_CREATE: UInt32 = 32768
CSIDL_FLAG_DONT_VERIFY: UInt32 = 16384
CSIDL_FLAG_DONT_UNEXPAND: UInt32 = 8192
CSIDL_FLAG_NO_ALIAS: UInt32 = 4096
CSIDL_FLAG_PER_USER_INIT: UInt32 = 2048
CSIDL_FLAG_MASK: UInt32 = 65280
FCS_READ: UInt32 = 1
FCS_FORCEWRITE: UInt32 = 2
FCS_FLAG_DRAGDROP: UInt32 = 2
FCSM_VIEWID: UInt32 = 1
FCSM_WEBVIEWTEMPLATE: UInt32 = 2
FCSM_INFOTIP: UInt32 = 4
FCSM_CLSID: UInt32 = 8
FCSM_ICONFILE: UInt32 = 16
FCSM_LOGO: UInt32 = 32
FCSM_FLAGS: UInt32 = 64
BIF_RETURNONLYFSDIRS: UInt32 = 1
BIF_DONTGOBELOWDOMAIN: UInt32 = 2
BIF_STATUSTEXT: UInt32 = 4
BIF_RETURNFSANCESTORS: UInt32 = 8
BIF_EDITBOX: UInt32 = 16
BIF_VALIDATE: UInt32 = 32
BIF_NEWDIALOGSTYLE: UInt32 = 64
BIF_BROWSEINCLUDEURLS: UInt32 = 128
BIF_UAHINT: UInt32 = 256
BIF_NONEWFOLDERBUTTON: UInt32 = 512
BIF_NOTRANSLATETARGETS: UInt32 = 1024
BIF_BROWSEFORCOMPUTER: UInt32 = 4096
BIF_BROWSEFORPRINTER: UInt32 = 8192
BIF_BROWSEINCLUDEFILES: UInt32 = 16384
BIF_SHAREABLE: UInt32 = 32768
BIF_BROWSEFILEJUNCTIONS: UInt32 = 65536
BFFM_INITIALIZED: UInt32 = 1
BFFM_SELCHANGED: UInt32 = 2
BFFM_VALIDATEFAILEDA: UInt32 = 3
BFFM_VALIDATEFAILEDW: UInt32 = 4
BFFM_IUNKNOWN: UInt32 = 5
BFFM_SETSTATUSTEXTA: UInt32 = 1124
BFFM_ENABLEOK: UInt32 = 1125
BFFM_SETSELECTIONA: UInt32 = 1126
BFFM_SETSELECTIONW: UInt32 = 1127
BFFM_SETSTATUSTEXTW: UInt32 = 1128
BFFM_SETOKTEXT: UInt32 = 1129
BFFM_SETEXPANDED: UInt32 = 1130
BFFM_SETSTATUSTEXT: UInt32 = 1128
BFFM_SETSELECTION: UInt32 = 1127
BFFM_VALIDATEFAILED: UInt32 = 4
CMDID_INTSHORTCUTCREATE: Int32 = 1
STR_PARSE_WITH_PROPERTIES: String = 'ParseWithProperties'
STR_PARSE_PARTIAL_IDLIST: String = 'ParseOriginalItem'
PROGDLG_NORMAL: UInt32 = 0
PROGDLG_MODAL: UInt32 = 1
PROGDLG_AUTOTIME: UInt32 = 2
PROGDLG_NOTIME: UInt32 = 4
PROGDLG_NOMINIMIZE: UInt32 = 8
PROGDLG_NOPROGRESSBAR: UInt32 = 16
PROGDLG_MARQUEEPROGRESS: UInt32 = 32
PROGDLG_NOCANCEL: UInt32 = 64
PDTIMER_RESET: UInt32 = 1
PDTIMER_PAUSE: UInt32 = 2
PDTIMER_RESUME: UInt32 = 3
COMPONENT_TOP: UInt32 = 1073741823
COMP_TYPE_HTMLDOC: UInt32 = 0
COMP_TYPE_PICTURE: UInt32 = 1
COMP_TYPE_WEBSITE: UInt32 = 2
COMP_TYPE_CONTROL: UInt32 = 3
COMP_TYPE_CFHTML: UInt32 = 4
COMP_TYPE_MAX: UInt32 = 4
IS_NORMAL: UInt32 = 1
IS_FULLSCREEN: UInt32 = 2
IS_SPLIT: UInt32 = 4
AD_APPLY_SAVE: UInt32 = 1
AD_APPLY_HTMLGEN: UInt32 = 2
AD_APPLY_REFRESH: UInt32 = 4
AD_APPLY_FORCE: UInt32 = 8
AD_APPLY_BUFFERED_REFRESH: UInt32 = 16
AD_APPLY_DYNAMICREFRESH: UInt32 = 32
AD_GETWP_BMP: UInt32 = 0
AD_GETWP_IMAGE: UInt32 = 1
AD_GETWP_LAST_APPLIED: UInt32 = 2
WPSTYLE_CENTER: UInt32 = 0
WPSTYLE_TILE: UInt32 = 1
WPSTYLE_STRETCH: UInt32 = 2
WPSTYLE_KEEPASPECT: UInt32 = 3
WPSTYLE_CROPTOFIT: UInt32 = 4
WPSTYLE_SPAN: UInt32 = 5
WPSTYLE_MAX: UInt32 = 6
COMP_ELEM_TYPE: UInt32 = 1
COMP_ELEM_CHECKED: UInt32 = 2
COMP_ELEM_DIRTY: UInt32 = 4
COMP_ELEM_NOSCROLL: UInt32 = 8
COMP_ELEM_POS_LEFT: UInt32 = 16
COMP_ELEM_POS_TOP: UInt32 = 32
COMP_ELEM_SIZE_WIDTH: UInt32 = 64
COMP_ELEM_SIZE_HEIGHT: UInt32 = 128
COMP_ELEM_POS_ZINDEX: UInt32 = 256
COMP_ELEM_SOURCE: UInt32 = 512
COMP_ELEM_FRIENDLYNAME: UInt32 = 1024
COMP_ELEM_SUBSCRIBEDURL: UInt32 = 2048
COMP_ELEM_ORIGINAL_CSI: UInt32 = 4096
COMP_ELEM_RESTORED_CSI: UInt32 = 8192
COMP_ELEM_CURITEMSTATE: UInt32 = 16384
ADDURL_SILENT: UInt32 = 1
COMPONENT_DEFAULT_LEFT: UInt32 = 65535
COMPONENT_DEFAULT_TOP: UInt32 = 65535
MAX_COLUMN_NAME_LEN: UInt32 = 80
MAX_COLUMN_DESC_LEN: UInt32 = 128
CFSTR_SHELLIDLIST: String = 'Shell IDList Array'
CFSTR_SHELLIDLISTOFFSET: String = 'Shell Object Offsets'
CFSTR_NETRESOURCES: String = 'Net Resource'
CFSTR_FILEDESCRIPTORA: String = 'FileGroupDescriptor'
CFSTR_FILEDESCRIPTORW: String = 'FileGroupDescriptorW'
CFSTR_FILECONTENTS: String = 'FileContents'
CFSTR_FILENAMEA: String = 'FileName'
CFSTR_FILENAMEW: String = 'FileNameW'
CFSTR_PRINTERGROUP: String = 'PrinterFriendlyName'
CFSTR_FILENAMEMAPA: String = 'FileNameMap'
CFSTR_FILENAMEMAPW: String = 'FileNameMapW'
CFSTR_SHELLURL: String = 'UniformResourceLocator'
CFSTR_INETURLA: String = 'UniformResourceLocator'
CFSTR_INETURLW: String = 'UniformResourceLocatorW'
CFSTR_PREFERREDDROPEFFECT: String = 'Preferred DropEffect'
CFSTR_PERFORMEDDROPEFFECT: String = 'Performed DropEffect'
CFSTR_PASTESUCCEEDED: String = 'Paste Succeeded'
CFSTR_INDRAGLOOP: String = 'InShellDragLoop'
CFSTR_MOUNTEDVOLUME: String = 'MountedVolume'
CFSTR_PERSISTEDDATAOBJECT: String = 'PersistedDataObject'
CFSTR_TARGETCLSID: String = 'TargetCLSID'
CFSTR_LOGICALPERFORMEDDROPEFFECT: String = 'Logical Performed DropEffect'
CFSTR_AUTOPLAY_SHELLIDLISTS: String = 'Autoplay Enumerated IDList Array'
CFSTR_UNTRUSTEDDRAGDROP: String = 'UntrustedDragDrop'
CFSTR_FILE_ATTRIBUTES_ARRAY: String = 'File Attributes Array'
CFSTR_INVOKECOMMAND_DROPPARAM: String = 'InvokeCommand DropParam'
CFSTR_SHELLDROPHANDLER: String = 'DropHandlerCLSID'
CFSTR_DROPDESCRIPTION: String = 'DropDescription'
CFSTR_ZONEIDENTIFIER: String = 'ZoneIdentifier'
CFSTR_FILEDESCRIPTOR: String = 'FileGroupDescriptorW'
CFSTR_FILENAME: String = 'FileNameW'
CFSTR_FILENAMEMAP: String = 'FileNameMapW'
CFSTR_INETURL: String = 'UniformResourceLocatorW'
DVASPECT_SHORTNAME: UInt32 = 2
DVASPECT_COPY: UInt32 = 3
DVASPECT_LINK: UInt32 = 4
SHCNEE_ORDERCHANGED: Int32 = 2
SHCNEE_MSI_CHANGE: Int32 = 4
SHCNEE_MSI_UNINSTALL: Int32 = 5
NUM_POINTS: UInt32 = 3
CABINETSTATE_VERSION: UInt32 = 2
PIFNAMESIZE: UInt32 = 30
PIFSTARTLOCSIZE: UInt32 = 63
PIFDEFPATHSIZE: UInt32 = 64
PIFPARAMSSIZE: UInt32 = 64
PIFSHPROGSIZE: UInt32 = 64
PIFSHDATASIZE: UInt32 = 64
PIFDEFFILESIZE: UInt32 = 80
PIFMAXFILEPATH: UInt32 = 260
QCMINFO_PLACE_BEFORE: UInt32 = 0
QCMINFO_PLACE_AFTER: UInt32 = 1
SFVSOC_INVALIDATE_ALL: UInt32 = 1
SFVSOC_NOSCROLL: UInt32 = 2
SHELLSTATEVERSION_IE4: UInt32 = 9
SHELLSTATEVERSION_WIN2K: UInt32 = 10
SHPPFW_NONE: UInt32 = 0
SHPPFW_DIRCREATE: UInt32 = 1
SHPPFW_ASKDIRCREATE: UInt32 = 2
SHPPFW_IGNOREFILENAME: UInt32 = 4
SHPPFW_NOWRITECHECK: UInt32 = 8
SHPPFW_MEDIACHECKONLY: UInt32 = 16
CMF_NORMAL: UInt32 = 0
CMF_DEFAULTONLY: UInt32 = 1
CMF_VERBSONLY: UInt32 = 2
CMF_EXPLORE: UInt32 = 4
CMF_NOVERBS: UInt32 = 8
CMF_CANRENAME: UInt32 = 16
CMF_NODEFAULT: UInt32 = 32
CMF_INCLUDESTATIC: UInt32 = 64
CMF_ITEMMENU: UInt32 = 128
CMF_EXTENDEDVERBS: UInt32 = 256
CMF_DISABLEDVERBS: UInt32 = 512
CMF_ASYNCVERBSTATE: UInt32 = 1024
CMF_OPTIMIZEFORINVOKE: UInt32 = 2048
CMF_SYNCCASCADEMENU: UInt32 = 4096
CMF_DONOTPICKDEFAULT: UInt32 = 8192
CMF_RESERVED: UInt32 = 4294901760
GCS_VERBA: UInt32 = 0
GCS_HELPTEXTA: UInt32 = 1
GCS_VALIDATEA: UInt32 = 2
GCS_VERBW: UInt32 = 4
GCS_HELPTEXTW: UInt32 = 5
GCS_VALIDATEW: UInt32 = 6
GCS_VERBICONW: UInt32 = 20
GCS_UNICODE: UInt32 = 4
GCS_VERB: UInt32 = 4
GCS_HELPTEXT: UInt32 = 5
GCS_VALIDATE: UInt32 = 6
CMDSTR_NEWFOLDERA: String = 'NewFolder'
CMDSTR_VIEWLISTA: String = 'ViewList'
CMDSTR_VIEWDETAILSA: String = 'ViewDetails'
CMDSTR_NEWFOLDERW: String = 'NewFolder'
CMDSTR_VIEWLISTW: String = 'ViewList'
CMDSTR_VIEWDETAILSW: String = 'ViewDetails'
CMDSTR_NEWFOLDER: String = 'NewFolder'
CMDSTR_VIEWLIST: String = 'ViewList'
CMDSTR_VIEWDETAILS: String = 'ViewDetails'
CMIC_MASK_SHIFT_DOWN: UInt32 = 268435456
CMIC_MASK_CONTROL_DOWN: UInt32 = 1073741824
CMIC_MASK_PTINVOKE: UInt32 = 536870912
IRTIR_TASK_NOT_RUNNING: UInt32 = 0
IRTIR_TASK_RUNNING: UInt32 = 1
IRTIR_TASK_SUSPENDED: UInt32 = 2
IRTIR_TASK_PENDING: UInt32 = 3
IRTIR_TASK_FINISHED: UInt32 = 4
ITSAT_DEFAULT_PRIORITY: UInt32 = 268435456
ITSAT_MAX_PRIORITY: UInt32 = 2147483647
ITSAT_MIN_PRIORITY: UInt32 = 0
ITSSFLAG_COMPLETE_ON_DESTROY: UInt32 = 0
ITSSFLAG_KILL_ON_DESTROY: UInt32 = 1
ITSSFLAG_FLAGS_MASK: UInt32 = 3
CSIDL_FLAG_PFTI_TRACKTARGET: UInt32 = 16384
SHCIDS_ALLFIELDS: Int32 = -2147483648
SHCIDS_CANONICALONLY: Int32 = 268435456
SHCIDS_BITMASK: Int32 = -65536
SHCIDS_COLUMNMASK: Int32 = 65535
CONFLICT_RESOLUTION_CLSID_KEY: String = 'ConflictResolutionCLSID'
STR_BIND_FORCE_FOLDER_SHORTCUT_RESOLVE: String = 'Force Folder Shortcut Resolve'
STR_AVOID_DRIVE_RESTRICTION_POLICY: String = 'Avoid Drive Restriction Policy'
STR_SKIP_BINDING_CLSID: String = 'Skip Binding CLSID'
STR_PARSE_PREFER_FOLDER_BROWSING: String = 'Parse Prefer Folder Browsing'
STR_DONT_PARSE_RELATIVE: String = "Don't Parse Relative"
STR_PARSE_TRANSLATE_ALIASES: String = 'Parse Translate Aliases'
STR_PARSE_SKIP_NET_CACHE: String = 'Skip Net Resource Cache'
STR_PARSE_SHELL_PROTOCOL_TO_FILE_OBJECTS: String = 'Parse Shell Protocol To File Objects'
STR_TRACK_CLSID: String = 'Track the CLSID'
STR_INTERNAL_NAVIGATE: String = 'Internal Navigation'
STR_PARSE_PROPERTYSTORE: String = 'DelegateNamedProperties'
STR_NO_VALIDATE_FILENAME_CHARS: String = 'NoValidateFilenameChars'
STR_BIND_DELEGATE_CREATE_OBJECT: String = 'Delegate Object Creation'
STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS: String = 'Allow binding to Internet shell folder handlers and negate STR_PARSE_PREFER_WEB_BROWSING'
STR_PARSE_PREFER_WEB_BROWSING: String = 'Do not bind to Internet shell folder handlers'
STR_PARSE_SHOW_NET_DIAGNOSTICS_UI: String = 'Show network diagnostics UI'
STR_PARSE_DONT_REQUIRE_VALIDATED_URLS: String = 'Do not require validated URLs'
STR_INTERNETFOLDER_PARSE_ONLY_URLMON_BINDABLE: String = 'Validate URL'
BIND_INTERRUPTABLE: UInt32 = 4294967295
STR_BIND_FOLDERS_READ_ONLY: String = 'Folders As Read Only'
STR_BIND_FOLDER_ENUM_MODE: String = 'Folder Enum Mode'
STR_PARSE_WITH_EXPLICIT_PROGID: String = 'ExplicitProgid'
STR_PARSE_WITH_EXPLICIT_ASSOCAPP: String = 'ExplicitAssociationApp'
STR_PARSE_EXPLICIT_ASSOCIATION_SUCCESSFUL: String = 'ExplicitAssociationSuccessful'
STR_PARSE_AND_CREATE_ITEM: String = 'ParseAndCreateItem'
STR_PROPERTYBAG_PARAM: String = 'SHBindCtxPropertyBag'
STR_ENUM_ITEMS_FLAGS: String = 'SHCONTF'
STR_STORAGEITEM_CREATION_FLAGS: String = 'SHGETSTORAGEITEM'
STR_ITEM_CACHE_CONTEXT: String = 'ItemCacheContext'
CDBOSC_SETFOCUS: UInt32 = 0
CDBOSC_KILLFOCUS: UInt32 = 1
CDBOSC_SELCHANGE: UInt32 = 2
CDBOSC_RENAME: UInt32 = 3
CDBOSC_STATECHANGE: UInt32 = 4
CDB2N_CONTEXTMENU_DONE: UInt32 = 1
CDB2N_CONTEXTMENU_START: UInt32 = 2
CDB2GVF_SHOWALLFILES: UInt32 = 1
CDB2GVF_ISFILESAVE: UInt32 = 2
CDB2GVF_ALLOWPREVIEWPANE: UInt32 = 4
CDB2GVF_NOSELECTVERB: UInt32 = 8
CDB2GVF_NOINCLUDEITEM: UInt32 = 16
CDB2GVF_ISFOLDERPICKER: UInt32 = 32
CDB2GVF_ADDSHIELD: UInt32 = 64
SBSP_DEFBROWSER: UInt32 = 0
SBSP_SAMEBROWSER: UInt32 = 1
SBSP_NEWBROWSER: UInt32 = 2
SBSP_DEFMODE: UInt32 = 0
SBSP_OPENMODE: UInt32 = 16
SBSP_EXPLOREMODE: UInt32 = 32
SBSP_HELPMODE: UInt32 = 64
SBSP_NOTRANSFERHIST: UInt32 = 128
SBSP_ABSOLUTE: UInt32 = 0
SBSP_RELATIVE: UInt32 = 4096
SBSP_PARENT: UInt32 = 8192
SBSP_NAVIGATEBACK: UInt32 = 16384
SBSP_NAVIGATEFORWARD: UInt32 = 32768
SBSP_ALLOW_AUTONAVIGATE: UInt32 = 65536
SBSP_KEEPSAMETEMPLATE: UInt32 = 131072
SBSP_KEEPWORDWHEELTEXT: UInt32 = 262144
SBSP_ACTIVATE_NOFOCUS: UInt32 = 524288
SBSP_CREATENOHISTORY: UInt32 = 1048576
SBSP_PLAYNOSOUND: UInt32 = 2097152
SBSP_CALLERUNTRUSTED: UInt32 = 8388608
SBSP_TRUSTFIRSTDOWNLOAD: UInt32 = 16777216
SBSP_UNTRUSTEDFORDOWNLOAD: UInt32 = 33554432
SBSP_NOAUTOSELECT: UInt32 = 67108864
SBSP_WRITENOHISTORY: UInt32 = 134217728
SBSP_TRUSTEDFORACTIVEX: UInt32 = 268435456
SBSP_FEEDNAVIGATION: UInt32 = 536870912
SBSP_REDIRECT: UInt32 = 1073741824
SBSP_INITIATEDBYHLINKFRAME: UInt32 = 2147483648
FCW_STATUS: UInt32 = 1
FCW_TOOLBAR: UInt32 = 2
FCW_TREE: UInt32 = 3
FCW_INTERNETBAR: UInt32 = 6
FCW_PROGRESS: UInt32 = 8
FCT_MERGE: UInt32 = 1
FCT_CONFIGABLE: UInt32 = 2
FCT_ADDTOEND: UInt32 = 4
STR_DONT_RESOLVE_LINK: String = "Don't Resolve Link"
STR_GET_ASYNC_HANDLER: String = 'GetAsyncHandler'
STR_GPS_HANDLERPROPERTIESONLY: String = 'GPS_HANDLERPROPERTIESONLY'
STR_GPS_FASTPROPERTIESONLY: String = 'GPS_FASTPROPERTIESONLY'
STR_GPS_OPENSLOWITEM: String = 'GPS_OPENSLOWITEM'
STR_GPS_DELAYCREATION: String = 'GPS_DELAYCREATION'
STR_GPS_BESTEFFORT: String = 'GPS_BESTEFFORT'
STR_GPS_NO_OPLOCK: String = 'GPS_NO_OPLOCK'
DI_GETDRAGIMAGE: String = 'ShellGetDragImage'
ARCONTENT_AUTORUNINF: UInt32 = 2
ARCONTENT_AUDIOCD: UInt32 = 4
ARCONTENT_DVDMOVIE: UInt32 = 8
ARCONTENT_BLANKCD: UInt32 = 16
ARCONTENT_BLANKDVD: UInt32 = 32
ARCONTENT_UNKNOWNCONTENT: UInt32 = 64
ARCONTENT_AUTOPLAYPIX: UInt32 = 128
ARCONTENT_AUTOPLAYMUSIC: UInt32 = 256
ARCONTENT_AUTOPLAYVIDEO: UInt32 = 512
ARCONTENT_VCD: UInt32 = 1024
ARCONTENT_SVCD: UInt32 = 2048
ARCONTENT_DVDAUDIO: UInt32 = 4096
ARCONTENT_BLANKBD: UInt32 = 8192
ARCONTENT_BLURAY: UInt32 = 16384
ARCONTENT_CAMERASTORAGE: UInt32 = 32768
ARCONTENT_CUSTOMEVENT: UInt32 = 65536
ARCONTENT_NONE: UInt32 = 0
ARCONTENT_MASK: UInt32 = 131070
ARCONTENT_PHASE_UNKNOWN: UInt32 = 0
ARCONTENT_PHASE_PRESNIFF: UInt32 = 268435456
ARCONTENT_PHASE_SNIFFING: UInt32 = 536870912
ARCONTENT_PHASE_FINAL: UInt32 = 1073741824
ARCONTENT_PHASE_MASK: UInt32 = 1879048192
IEI_PRIORITY_MAX: UInt32 = 2147483647
IEI_PRIORITY_MIN: UInt32 = 0
IEIT_PRIORITY_NORMAL: UInt32 = 268435456
IEIFLAG_ASYNC: UInt32 = 1
IEIFLAG_CACHE: UInt32 = 2
IEIFLAG_ASPECT: UInt32 = 4
IEIFLAG_OFFLINE: UInt32 = 8
IEIFLAG_GLEAM: UInt32 = 16
IEIFLAG_SCREEN: UInt32 = 32
IEIFLAG_ORIGSIZE: UInt32 = 64
IEIFLAG_NOSTAMP: UInt32 = 128
IEIFLAG_NOBORDER: UInt32 = 256
IEIFLAG_QUALITY: UInt32 = 512
IEIFLAG_REFRESH: UInt32 = 1024
DBIM_MINSIZE: UInt32 = 1
DBIM_MAXSIZE: UInt32 = 2
DBIM_INTEGRAL: UInt32 = 4
DBIM_ACTUAL: UInt32 = 8
DBIM_TITLE: UInt32 = 16
DBIM_MODEFLAGS: UInt32 = 32
DBIM_BKCOLOR: UInt32 = 64
DBIMF_NORMAL: UInt32 = 0
DBIMF_FIXED: UInt32 = 1
DBIMF_FIXEDBMP: UInt32 = 4
DBIMF_VARIABLEHEIGHT: UInt32 = 8
DBIMF_UNDELETEABLE: UInt32 = 16
DBIMF_DEBOSSED: UInt32 = 32
DBIMF_BKCOLOR: UInt32 = 64
DBIMF_USECHEVRON: UInt32 = 128
DBIMF_BREAK: UInt32 = 256
DBIMF_ADDTOFRONT: UInt32 = 512
DBIMF_TOPALIGN: UInt32 = 1024
DBIMF_NOGRIPPER: UInt32 = 2048
DBIMF_ALWAYSGRIPPER: UInt32 = 4096
DBIMF_NOMARGINS: UInt32 = 8192
DBIF_VIEWMODE_NORMAL: UInt32 = 0
DBIF_VIEWMODE_VERTICAL: UInt32 = 1
DBIF_VIEWMODE_FLOATING: UInt32 = 2
DBIF_VIEWMODE_TRANSPARENT: UInt32 = 4
DBPC_SELECTFIRST: UInt32 = 4294967295
THBN_CLICKED: UInt32 = 6144
FOFX_NOSKIPJUNCTIONS: UInt32 = 65536
FOFX_PREFERHARDLINK: UInt32 = 131072
FOFX_SHOWELEVATIONPROMPT: UInt32 = 262144
FOFX_RECYCLEONDELETE: UInt32 = 524288
FOFX_EARLYFAILURE: UInt32 = 1048576
FOFX_PRESERVEFILEEXTENSIONS: UInt32 = 2097152
FOFX_KEEPNEWERFILE: UInt32 = 4194304
FOFX_NOCOPYHOOKS: UInt32 = 8388608
FOFX_NOMINIMIZEBOX: UInt32 = 16777216
FOFX_MOVEACLSACROSSVOLUMES: UInt32 = 33554432
FOFX_DONTDISPLAYSOURCEPATH: UInt32 = 67108864
FOFX_DONTDISPLAYDESTPATH: UInt32 = 134217728
FOFX_REQUIREELEVATION: UInt32 = 268435456
FOFX_ADDUNDORECORD: UInt32 = 536870912
FOFX_COPYASDOWNLOAD: UInt32 = 1073741824
FOFX_DONTDISPLAYLOCATIONS: UInt32 = 2147483648
BSIM_STATE: UInt32 = 1
BSIM_STYLE: UInt32 = 2
BSSF_VISIBLE: UInt32 = 1
BSSF_NOTITLE: UInt32 = 2
BSSF_UNDELETEABLE: UInt32 = 4096
BSIS_AUTOGRIPPER: UInt32 = 0
BSIS_NOGRIPPER: UInt32 = 1
BSIS_ALWAYSGRIPPER: UInt32 = 2
BSIS_LEFTALIGN: UInt32 = 4
BSIS_SINGLECLICK: UInt32 = 8
BSIS_NOCONTEXTMENU: UInt32 = 16
BSIS_NODROPTARGET: UInt32 = 32
BSIS_NOCAPTION: UInt32 = 64
BSIS_PREFERNOLINEBREAK: UInt32 = 128
BSIS_LOCKED: UInt32 = 256
BSIS_PRESERVEORDERDURINGLAYOUT: UInt32 = 512
BSIS_FIXEDORDER: UInt32 = 1024
OF_CAP_CANSWITCHTO: UInt32 = 1
OF_CAP_CANCLOSE: UInt32 = 2
SMDM_SHELLFOLDER: UInt32 = 1
SMDM_HMENU: UInt32 = 2
SMDM_TOOLBAR: UInt32 = 4
SMC_INITMENU: UInt32 = 1
SMC_CREATE: UInt32 = 2
SMC_EXITMENU: UInt32 = 3
SMC_GETINFO: UInt32 = 5
SMC_GETSFINFO: UInt32 = 6
SMC_GETOBJECT: UInt32 = 7
SMC_GETSFOBJECT: UInt32 = 8
SMC_SFEXEC: UInt32 = 9
SMC_SFSELECTITEM: UInt32 = 10
SMC_REFRESH: UInt32 = 16
SMC_DEMOTE: UInt32 = 17
SMC_PROMOTE: UInt32 = 18
SMC_DEFAULTICON: UInt32 = 22
SMC_NEWITEM: UInt32 = 23
SMC_CHEVRONEXPAND: UInt32 = 25
SMC_DISPLAYCHEVRONTIP: UInt32 = 42
SMC_SETSFOBJECT: UInt32 = 45
SMC_SHCHANGENOTIFY: UInt32 = 46
SMC_CHEVRONGETTIP: UInt32 = 47
SMC_SFDDRESTRICTED: UInt32 = 48
SMC_SFEXEC_MIDDLE: UInt32 = 49
SMC_GETAUTOEXPANDSTATE: UInt32 = 65
SMC_AUTOEXPANDCHANGE: UInt32 = 66
SMC_GETCONTEXTMENUMODIFIER: UInt32 = 67
SMC_GETBKCONTEXTMENU: UInt32 = 68
SMC_OPEN: UInt32 = 69
SMAE_EXPANDED: UInt32 = 1
SMAE_CONTRACTED: UInt32 = 2
SMAE_USER: UInt32 = 4
SMAE_VALID: UInt32 = 7
SMINIT_DEFAULT: UInt32 = 0
SMINIT_RESTRICT_DRAGDROP: UInt32 = 2
SMINIT_TOPLEVEL: UInt32 = 4
SMINIT_CACHED: UInt32 = 16
SMINIT_AUTOEXPAND: UInt32 = 256
SMINIT_AUTOTOOLTIP: UInt32 = 512
SMINIT_DROPONCONTAINER: UInt32 = 1024
SMINIT_VERTICAL: UInt32 = 268435456
SMINIT_HORIZONTAL: UInt32 = 536870912
SMSET_TOP: UInt32 = 268435456
SMSET_BOTTOM: UInt32 = 536870912
SMSET_DONTOWN: UInt32 = 1
SMINV_REFRESH: UInt32 = 1
SMINV_ID: UInt32 = 8
E_PREVIEWHANDLER_DRM_FAIL: Windows.Win32.Foundation.HRESULT = -2042494975
E_PREVIEWHANDLER_NOAUTH: Windows.Win32.Foundation.HRESULT = -2042494974
E_PREVIEWHANDLER_NOTFOUND: Windows.Win32.Foundation.HRESULT = -2042494973
E_PREVIEWHANDLER_CORRUPT: Windows.Win32.Foundation.HRESULT = -2042494972
STR_FILE_SYS_BIND_DATA: String = 'File System Bind Data'
STR_FILE_SYS_BIND_DATA_WIN7_FORMAT: String = 'Win7FileSystemIdList'
HOMEGROUP_SECURITY_GROUP_MULTI: String = 'HUG'
HOMEGROUP_SECURITY_GROUP: String = 'HomeUsers'
PROP_CONTRACT_DELEGATE: String = 'ContractDelegate'
SID_URLExecutionContext: Guid = Guid('fb5f8ebc-bbb6-4d10-a4-61-77-72-91-a0-90-30')
STR_TAB_REUSE_IDENTIFIER: String = 'Tab Reuse Identifier'
STR_REFERRER_IDENTIFIER: String = 'Referrer Identifier'
SID_LaunchSourceViewSizePreference: Guid = Guid('80605492-67d9-414f-af-89-a1-cd-f1-24-2b-c1')
SID_LaunchTargetViewSizePreference: Guid = Guid('26db2472-b7b7-406b-97-02-73-0a-4e-20-d3-bf')
SID_LaunchSourceAppUserModelId: Guid = Guid('2ce78010-74db-48bc-9c-6a-10-f3-72-49-57-23')
SID_ShellExecuteNamedPropertyStore: Guid = Guid('eb84ada2-00ff-4992-83-24-ed-5c-e0-61-cb-29')
ISIOI_ICONFILE: UInt32 = 1
ISIOI_ICONINDEX: UInt32 = 2
ABM_NEW: UInt32 = 0
ABM_REMOVE: UInt32 = 1
ABM_QUERYPOS: UInt32 = 2
ABM_SETPOS: UInt32 = 3
ABM_GETSTATE: UInt32 = 4
ABM_GETTASKBARPOS: UInt32 = 5
ABM_ACTIVATE: UInt32 = 6
ABM_GETAUTOHIDEBAR: UInt32 = 7
ABM_SETAUTOHIDEBAR: UInt32 = 8
ABM_WINDOWPOSCHANGED: UInt32 = 9
ABM_SETSTATE: UInt32 = 10
ABM_GETAUTOHIDEBAREX: UInt32 = 11
ABM_SETAUTOHIDEBAREX: UInt32 = 12
ABN_STATECHANGE: UInt32 = 0
ABN_POSCHANGED: UInt32 = 1
ABN_FULLSCREENAPP: UInt32 = 2
ABN_WINDOWARRANGE: UInt32 = 3
ABS_AUTOHIDE: UInt32 = 1
ABS_ALWAYSONTOP: UInt32 = 2
ABE_LEFT: UInt32 = 0
ABE_TOP: UInt32 = 1
ABE_RIGHT: UInt32 = 2
ABE_BOTTOM: UInt32 = 3
FO_MOVE: UInt32 = 1
FO_COPY: UInt32 = 2
FO_DELETE: UInt32 = 3
FO_RENAME: UInt32 = 4
FOF_MULTIDESTFILES: UInt32 = 1
FOF_CONFIRMMOUSE: UInt32 = 2
FOF_SILENT: UInt32 = 4
FOF_RENAMEONCOLLISION: UInt32 = 8
FOF_NOCONFIRMATION: UInt32 = 16
FOF_WANTMAPPINGHANDLE: UInt32 = 32
FOF_ALLOWUNDO: UInt32 = 64
FOF_FILESONLY: UInt32 = 128
FOF_SIMPLEPROGRESS: UInt32 = 256
FOF_NOCONFIRMMKDIR: UInt32 = 512
FOF_NOERRORUI: UInt32 = 1024
FOF_NOCOPYSECURITYATTRIBS: UInt32 = 2048
FOF_NORECURSION: UInt32 = 4096
FOF_NO_CONNECTED_ELEMENTS: UInt32 = 8192
FOF_WANTNUKEWARNING: UInt32 = 16384
FOF_NORECURSEREPARSE: UInt32 = 32768
PO_DELETE: UInt32 = 19
PO_RENAME: UInt32 = 20
PO_PORTCHANGE: UInt32 = 32
PO_REN_PORT: UInt32 = 52
SE_ERR_FNF: UInt32 = 2
SE_ERR_PNF: UInt32 = 3
SE_ERR_ACCESSDENIED: UInt32 = 5
SE_ERR_OOM: UInt32 = 8
SE_ERR_DLLNOTFOUND: UInt32 = 32
SE_ERR_SHARE: UInt32 = 26
SE_ERR_ASSOCINCOMPLETE: UInt32 = 27
SE_ERR_DDETIMEOUT: UInt32 = 28
SE_ERR_DDEFAIL: UInt32 = 29
SE_ERR_DDEBUSY: UInt32 = 30
SE_ERR_NOASSOC: UInt32 = 31
SEE_MASK_DEFAULT: UInt32 = 0
SEE_MASK_CLASSNAME: UInt32 = 1
SEE_MASK_CLASSKEY: UInt32 = 3
SEE_MASK_IDLIST: UInt32 = 4
SEE_MASK_INVOKEIDLIST: UInt32 = 12
SEE_MASK_ICON: UInt32 = 16
SEE_MASK_HOTKEY: UInt32 = 32
SEE_MASK_NOCLOSEPROCESS: UInt32 = 64
SEE_MASK_CONNECTNETDRV: UInt32 = 128
SEE_MASK_NOASYNC: UInt32 = 256
SEE_MASK_FLAG_DDEWAIT: UInt32 = 256
SEE_MASK_DOENVSUBST: UInt32 = 512
SEE_MASK_FLAG_NO_UI: UInt32 = 1024
SEE_MASK_UNICODE: UInt32 = 16384
SEE_MASK_NO_CONSOLE: UInt32 = 32768
SEE_MASK_ASYNCOK: UInt32 = 1048576
SEE_MASK_HMONITOR: UInt32 = 2097152
SEE_MASK_NOZONECHECKS: UInt32 = 8388608
SEE_MASK_NOQUERYCLASSSTORE: UInt32 = 16777216
SEE_MASK_WAITFORINPUTIDLE: UInt32 = 33554432
SEE_MASK_FLAG_LOG_USAGE: UInt32 = 67108864
SEE_MASK_FLAG_HINST_IS_SITE: UInt32 = 134217728
SHERB_NOCONFIRMATION: UInt32 = 1
SHERB_NOPROGRESSUI: UInt32 = 2
SHERB_NOSOUND: UInt32 = 4
NIN_SELECT: UInt32 = 1024
NINF_KEY: UInt32 = 1
NIN_BALLOONSHOW: UInt32 = 1026
NIN_BALLOONHIDE: UInt32 = 1027
NIN_BALLOONTIMEOUT: UInt32 = 1028
NIN_BALLOONUSERCLICK: UInt32 = 1029
NIN_POPUPOPEN: UInt32 = 1030
NIN_POPUPCLOSE: UInt32 = 1031
NOTIFYICON_VERSION: UInt32 = 3
NOTIFYICON_VERSION_4: UInt32 = 4
SHGNLI_PIDL: UInt64 = 1
SHGNLI_PREFIXNAME: UInt64 = 2
SHGNLI_NOUNIQUE: UInt64 = 4
SHGNLI_NOLNK: UInt64 = 8
SHGNLI_NOLOCNAME: UInt64 = 16
SHGNLI_USEURLEXT: UInt64 = 32
PRINTACTION_OPEN: UInt32 = 0
PRINTACTION_PROPERTIES: UInt32 = 1
PRINTACTION_NETINSTALL: UInt32 = 2
PRINTACTION_NETINSTALLLINK: UInt32 = 3
PRINTACTION_TESTPAGE: UInt32 = 4
PRINTACTION_OPENNETPRN: UInt32 = 5
PRINTACTION_DOCUMENTDEFAULTS: UInt32 = 6
PRINTACTION_SERVERPROPERTIES: UInt32 = 7
PRINT_PROP_FORCE_NAME: UInt32 = 1
OFFLINE_STATUS_LOCAL: UInt32 = 1
OFFLINE_STATUS_REMOTE: UInt32 = 2
OFFLINE_STATUS_INCOMPLETE: UInt32 = 4
SHIL_LARGE: UInt32 = 0
SHIL_SMALL: UInt32 = 1
SHIL_EXTRALARGE: UInt32 = 2
SHIL_SYSSMALL: UInt32 = 3
SHIL_JUMBO: UInt32 = 4
SHIL_LAST: UInt32 = 4
WC_NETADDRESS: String = 'msctls_netaddress'
NCM_GETADDRESS: UInt32 = 1025
NCM_SETALLOWTYPE: UInt32 = 1026
NCM_GETALLOWTYPE: UInt32 = 1027
NCM_DISPLAYERRORTIP: UInt32 = 1028
CREDENTIAL_PROVIDER_NO_DEFAULT: UInt32 = 4294967295
Identity_LocalUserProvider: Guid = Guid('a198529b-730f-4089-b6-46-a1-25-57-f5-66-5e')
MAX_SYNCMGR_ID: UInt32 = 64
MAX_SYNCMGR_PROGRESSTEXT: UInt32 = 260
MAX_SYNCMGR_NAME: UInt32 = 128
STIF_DEFAULT: Int32 = 0
STIF_SUPPORT_HEX: Int32 = 1
SZ_CONTENTTYPE_HTMLA: String = 'text/html'
SZ_CONTENTTYPE_HTMLW: String = 'text/html'
SZ_CONTENTTYPE_CDFA: String = 'application/x-cdf'
SZ_CONTENTTYPE_CDFW: String = 'application/x-cdf'
SZ_CONTENTTYPE_HTML: String = 'text/html'
SZ_CONTENTTYPE_CDF: String = 'application/x-cdf'
GCT_INVALID: UInt32 = 0
GCT_LFNCHAR: UInt32 = 1
GCT_SHORTCHAR: UInt32 = 2
GCT_WILD: UInt32 = 4
GCT_SEPARATOR: UInt32 = 8
PMSF_NORMAL: UInt32 = 0
PMSF_MULTIPLE: UInt32 = 1
PMSF_DONT_STRIP_SPACES: UInt32 = 65536
URL_UNESCAPE: UInt32 = 268435456
URL_ESCAPE_UNSAFE: UInt32 = 536870912
URL_PLUGGABLE_PROTOCOL: UInt32 = 1073741824
URL_WININET_COMPATIBILITY: UInt32 = 2147483648
URL_DONT_ESCAPE_EXTRA_INFO: UInt32 = 33554432
URL_DONT_UNESCAPE_EXTRA_INFO: UInt32 = 33554432
URL_BROWSER_MODE: UInt32 = 33554432
URL_ESCAPE_SPACES_ONLY: UInt32 = 67108864
URL_DONT_SIMPLIFY: UInt32 = 134217728
URL_NO_META: UInt32 = 134217728
URL_UNESCAPE_INPLACE: UInt32 = 1048576
URL_CONVERT_IF_DOSPATH: UInt32 = 2097152
URL_UNESCAPE_HIGH_ANSI_ONLY: UInt32 = 4194304
URL_INTERNAL_PATH: UInt32 = 8388608
URL_FILE_USE_PATHURL: UInt32 = 65536
URL_DONT_UNESCAPE: UInt32 = 131072
URL_ESCAPE_AS_UTF8: UInt32 = 262144
URL_UNESCAPE_AS_UTF8: UInt32 = 262144
URL_ESCAPE_ASCII_URI_COMPONENT: UInt32 = 524288
URL_UNESCAPE_URI_COMPONENT: UInt32 = 262144
URL_ESCAPE_PERCENT: UInt32 = 4096
URL_ESCAPE_SEGMENT_ONLY: UInt32 = 8192
URL_PARTFLAG_KEEPSCHEME: UInt32 = 1
URL_APPLY_DEFAULT: UInt32 = 1
URL_APPLY_GUESSSCHEME: UInt32 = 2
URL_APPLY_GUESSFILE: UInt32 = 4
URL_APPLY_FORCEAPPLY: UInt32 = 8
SRRF_RT_REG_NONE: UInt32 = 1
SRRF_RT_REG_SZ: UInt32 = 2
SRRF_RT_REG_EXPAND_SZ: UInt32 = 4
SRRF_RT_REG_BINARY: UInt32 = 8
SRRF_RT_REG_DWORD: UInt32 = 16
SRRF_RT_REG_MULTI_SZ: UInt32 = 32
SRRF_RT_REG_QWORD: UInt32 = 64
SRRF_RT_ANY: UInt32 = 65535
SRRF_RM_ANY: UInt32 = 0
SRRF_RM_NORMAL: UInt32 = 65536
SRRF_RM_SAFE: UInt32 = 131072
SRRF_RM_SAFENETWORK: UInt32 = 262144
SRRF_NOEXPAND: UInt32 = 268435456
SRRF_ZEROONFAILURE: UInt32 = 536870912
SRRF_NOVIRT: UInt32 = 1073741824
SHREGSET_HKCU: UInt32 = 1
SHREGSET_FORCE_HKCU: UInt32 = 2
SHREGSET_HKLM: UInt32 = 4
SHREGSET_FORCE_HKLM: UInt32 = 8
SPMODE_SHELL: UInt32 = 1
SPMODE_DEBUGOUT: UInt32 = 2
SPMODE_TEST: UInt32 = 4
SPMODE_BROWSER: UInt32 = 8
SPMODE_FLUSH: UInt32 = 16
SPMODE_EVENT: UInt32 = 32
SPMODE_MSVM: UInt32 = 64
SPMODE_FORMATTEXT: UInt32 = 128
SPMODE_PROFILE: UInt32 = 256
SPMODE_DEBUGBREAK: UInt32 = 512
SPMODE_MSGTRACE: UInt32 = 1024
SPMODE_PERFTAGS: UInt32 = 2048
SPMODE_MEMWATCH: UInt32 = 4096
SPMODE_DBMON: UInt32 = 8192
SPMODE_MULTISTOP: UInt32 = 16384
SPMODE_EVENTTRACE: UInt32 = 32768
SHGVSPB_PERUSER: UInt32 = 1
SHGVSPB_ALLUSERS: UInt32 = 2
SHGVSPB_PERFOLDER: UInt32 = 4
SHGVSPB_ALLFOLDERS: UInt32 = 8
SHGVSPB_INHERIT: UInt32 = 16
SHGVSPB_ROAM: UInt32 = 32
SHGVSPB_NOAUTODEFAULTS: UInt32 = 2147483648
FDTF_SHORTTIME: UInt32 = 1
FDTF_SHORTDATE: UInt32 = 2
FDTF_LONGDATE: UInt32 = 4
FDTF_LONGTIME: UInt32 = 8
FDTF_RELATIVE: UInt32 = 16
FDTF_LTRDATE: UInt32 = 256
FDTF_RTLDATE: UInt32 = 512
FDTF_NOAUTOREADINGORDER: UInt32 = 1024
PLATFORM_UNKNOWN: UInt32 = 0
PLATFORM_IE3: UInt32 = 1
PLATFORM_BROWSERONLY: UInt32 = 1
PLATFORM_INTEGRATED: UInt32 = 2
ILMM_IE4: UInt32 = 0
DLLVER_PLATFORM_WINDOWS: UInt32 = 1
DLLVER_PLATFORM_NT: UInt32 = 2
DLLVER_MAJOR_MASK: UInt64 = 18446462598732840960
DLLVER_MINOR_MASK: UInt64 = 281470681743360
DLLVER_BUILD_MASK: UInt64 = 4294901760
DLLVER_QFE_MASK: UInt64 = 65535
WTS_E_FAILEDEXTRACTION: Windows.Win32.Foundation.HRESULT = -2147175936
WTS_E_EXTRACTIONTIMEDOUT: Windows.Win32.Foundation.HRESULT = -2147175935
WTS_E_SURROGATEUNAVAILABLE: Windows.Win32.Foundation.HRESULT = -2147175934
WTS_E_FASTEXTRACTIONNOTSUPPORTED: Windows.Win32.Foundation.HRESULT = -2147175933
WTS_E_DATAFILEUNAVAILABLE: Windows.Win32.Foundation.HRESULT = -2147175932
WTS_E_EXTRACTIONPENDING: Windows.Win32.Foundation.HRESULT = -2147175931
WTS_E_EXTRACTIONBLOCKED: Windows.Win32.Foundation.HRESULT = -2147175930
WTS_E_NOSTORAGEPROVIDERTHUMBNAILHANDLER: Windows.Win32.Foundation.HRESULT = -2147175929
SHIMGKEY_QUALITY: String = 'Compression'
SHIMGKEY_RAWFORMAT: String = 'RawDataFormat'
SHIMGDEC_DEFAULT: UInt32 = 0
SHIMGDEC_THUMBNAIL: UInt32 = 1
SHIMGDEC_LOADFULL: UInt32 = 2
E_NOTVALIDFORANIMATEDIMAGE: Windows.Win32.Foundation.HRESULT = -2147221503
S_SYNCMGR_MISSINGITEMS: Windows.Win32.Foundation.HRESULT = 262657
S_SYNCMGR_RETRYSYNC: Windows.Win32.Foundation.HRESULT = 262658
S_SYNCMGR_CANCELITEM: Windows.Win32.Foundation.HRESULT = 262659
S_SYNCMGR_CANCELALL: Windows.Win32.Foundation.HRESULT = 262660
S_SYNCMGR_ITEMDELETED: Windows.Win32.Foundation.HRESULT = 262672
S_SYNCMGR_ENUMITEMS: Windows.Win32.Foundation.HRESULT = 262673
SYNCMGRPROGRESSITEM_STATUSTEXT: UInt32 = 1
SYNCMGRPROGRESSITEM_STATUSTYPE: UInt32 = 2
SYNCMGRPROGRESSITEM_PROGVALUE: UInt32 = 4
SYNCMGRPROGRESSITEM_MAXVALUE: UInt32 = 8
SYNCMGRLOGERROR_ERRORFLAGS: UInt32 = 1
SYNCMGRLOGERROR_ERRORID: UInt32 = 2
SYNCMGRLOGERROR_ITEMID: UInt32 = 4
SYNCMGRITEM_ITEMFLAGMASK: UInt32 = 127
MAX_SYNCMGRITEMNAME: UInt32 = 128
SYNCMGRHANDLERFLAG_MASK: UInt32 = 15
MAX_SYNCMGRHANDLERNAME: UInt32 = 32
SYNCMGRREGISTERFLAGS_MASK: UInt32 = 7
TLOG_BACK: Int32 = -1
TLOG_CURRENT: UInt32 = 0
TLOG_FORE: UInt32 = 1
TLMENUF_INCLUDECURRENT: UInt32 = 1
TLMENUF_BACK: UInt32 = 16
TLMENUF_FORE: UInt32 = 32
BSF_REGISTERASDROPTARGET: UInt32 = 1
BSF_THEATERMODE: UInt32 = 2
BSF_NOLOCALFILEWARNING: UInt32 = 16
BSF_UISETBYAUTOMATION: UInt32 = 256
BSF_RESIZABLE: UInt32 = 512
BSF_CANMAXIMIZE: UInt32 = 1024
BSF_TOPBROWSER: UInt32 = 2048
BSF_NAVNOHISTORY: UInt32 = 4096
BSF_HTMLNAVCANCELED: UInt32 = 8192
BSF_DONTSHOWNAVCANCELPAGE: UInt32 = 16384
BSF_SETNAVIGATABLECODEPAGE: UInt32 = 32768
BSF_DELEGATEDNAVIGATION: UInt32 = 65536
BSF_TRUSTEDFORACTIVEX: UInt32 = 131072
BSF_MERGEDMENUS: UInt32 = 262144
BSF_FEEDNAVIGATION: UInt32 = 524288
BSF_FEEDSUBSCRIBED: UInt32 = 1048576
HLNF_CALLERUNTRUSTED: UInt32 = 2097152
HLNF_TRUSTEDFORACTIVEX: UInt32 = 4194304
HLNF_DISABLEWINDOWRESTRICTIONS: UInt32 = 8388608
HLNF_TRUSTFIRSTDOWNLOAD: UInt32 = 16777216
HLNF_UNTRUSTEDFORDOWNLOAD: UInt32 = 33554432
SHHLNF_NOAUTOSELECT: UInt32 = 67108864
SHHLNF_WRITENOHISTORY: UInt32 = 134217728
HLNF_EXTERNALNAVIGATE: UInt32 = 268435456
HLNF_ALLOW_AUTONAVIGATE: UInt32 = 536870912
HLNF_NEWWINDOWSMANAGED: UInt32 = 2147483648
INTERNET_MAX_PATH_LENGTH: UInt32 = 2048
INTERNET_MAX_SCHEME_LENGTH: UInt32 = 32
VIEW_PRIORITY_RESTRICTED: UInt32 = 112
VIEW_PRIORITY_CACHEHIT: UInt32 = 80
VIEW_PRIORITY_STALECACHEHIT: UInt32 = 69
VIEW_PRIORITY_USEASDEFAULT: UInt32 = 67
VIEW_PRIORITY_SHELLEXT: UInt32 = 64
VIEW_PRIORITY_CACHEMISS: UInt32 = 48
VIEW_PRIORITY_INHERIT: UInt32 = 32
VIEW_PRIORITY_SHELLEXT_ASBACKUP: UInt32 = 21
VIEW_PRIORITY_DESPERATE: UInt32 = 16
VIEW_PRIORITY_NONE: UInt32 = 0
VOLUME_PREFIX: String = '\\\\?\\Volume'
PATHCCH_MAX_CCH: UInt32 = 32768
IDS_DESCRIPTION: UInt32 = 1
ID_APP: UInt32 = 100
DLG_SCRNSAVECONFIGURE: UInt32 = 2003
idsIsPassword: UInt32 = 1000
idsIniFile: UInt32 = 1001
idsScreenSaver: UInt32 = 1002
idsPassword: UInt32 = 1003
idsDifferentPW: UInt32 = 1004
idsChangePW: UInt32 = 1005
idsBadOldPW: UInt32 = 1006
idsAppName: UInt32 = 1007
idsNoHelpMemory: UInt32 = 1008
idsHelpFile: UInt32 = 1009
idsDefKeyword: UInt32 = 1010
MAXFILELEN: UInt32 = 13
TITLEBARNAMELEN: UInt32 = 40
APPNAMEBUFFERLEN: UInt32 = 40
BUFFLEN: UInt32 = 255
SCRM_VERIFYPW: UInt32 = 32768
E_FLAGS: Windows.Win32.Foundation.HRESULT = -2147217408
IS_E_EXEC_FAILED: Windows.Win32.Foundation.HRESULT = -2147213310
URL_E_INVALID_SYNTAX: Windows.Win32.Foundation.HRESULT = -2147217407
URL_E_UNREGISTERED_PROTOCOL: Windows.Win32.Foundation.HRESULT = -2147217406
CPLPAGE_MOUSE_BUTTONS: UInt32 = 1
CPLPAGE_MOUSE_PTRMOTION: UInt32 = 2
CPLPAGE_MOUSE_WHEEL: UInt32 = 3
CPLPAGE_KEYBOARD_SPEED: UInt32 = 1
CPLPAGE_DISPLAY_BACKGROUND: UInt32 = 1
DISPID_SELECTIONCHANGED: UInt32 = 200
DISPID_FILELISTENUMDONE: UInt32 = 201
DISPID_VERBINVOKED: UInt32 = 202
DISPID_DEFAULTVERBINVOKED: UInt32 = 203
DISPID_BEGINDRAG: UInt32 = 204
DISPID_VIEWMODECHANGED: UInt32 = 205
DISPID_NOITEMSTATE_CHANGED: UInt32 = 206
DISPID_CONTENTSCHANGED: UInt32 = 207
DISPID_FOCUSCHANGED: UInt32 = 208
DISPID_CHECKSTATECHANGED: UInt32 = 209
DISPID_ORDERCHANGED: UInt32 = 210
DISPID_VIEWPAINTDONE: UInt32 = 211
DISPID_COLUMNSCHANGED: UInt32 = 212
DISPID_CTRLMOUSEWHEEL: UInt32 = 213
DISPID_SORTDONE: UInt32 = 214
DISPID_ICONSIZECHANGED: UInt32 = 215
DISPID_FOLDERCHANGED: UInt32 = 217
DISPID_FILTERINVOKED: UInt32 = 218
DISPID_WORDWHEELEDITED: UInt32 = 219
DISPID_SELECTEDITEMCHANGED: UInt32 = 220
DISPID_EXPLORERWINDOWREADY: UInt32 = 221
DISPID_UPDATEIMAGE: UInt32 = 222
DISPID_INITIALENUMERATIONDONE: UInt32 = 223
DISPID_ENTERPRISEIDCHANGED: UInt32 = 224
DISPID_ENTERPRESSED: UInt32 = 200
DISPID_SEARCHCOMMAND_START: UInt32 = 1
DISPID_SEARCHCOMMAND_COMPLETE: UInt32 = 2
DISPID_SEARCHCOMMAND_ABORT: UInt32 = 3
DISPID_SEARCHCOMMAND_UPDATE: UInt32 = 4
DISPID_SEARCHCOMMAND_PROGRESSTEXT: UInt32 = 5
DISPID_SEARCHCOMMAND_ERROR: UInt32 = 6
DISPID_SEARCHCOMMAND_RESTORE: UInt32 = 7
DISPID_IADCCTL_DIRTY: UInt32 = 256
DISPID_IADCCTL_PUBCAT: UInt32 = 257
DISPID_IADCCTL_SORT: UInt32 = 258
DISPID_IADCCTL_FORCEX86: UInt32 = 259
DISPID_IADCCTL_SHOWPOSTSETUP: UInt32 = 260
DISPID_IADCCTL_ONDOMAIN: UInt32 = 261
DISPID_IADCCTL_DEFAULTCAT: UInt32 = 262
COPYENGINE_S_YES: Windows.Win32.Foundation.HRESULT = 2555905
COPYENGINE_S_NOT_HANDLED: Windows.Win32.Foundation.HRESULT = 2555907
COPYENGINE_S_USER_RETRY: Windows.Win32.Foundation.HRESULT = 2555908
COPYENGINE_S_USER_IGNORED: Windows.Win32.Foundation.HRESULT = 2555909
COPYENGINE_S_MERGE: Windows.Win32.Foundation.HRESULT = 2555910
COPYENGINE_S_DONT_PROCESS_CHILDREN: Windows.Win32.Foundation.HRESULT = 2555912
COPYENGINE_S_ALREADY_DONE: Windows.Win32.Foundation.HRESULT = 2555914
COPYENGINE_S_PENDING: Windows.Win32.Foundation.HRESULT = 2555915
COPYENGINE_S_KEEP_BOTH: Windows.Win32.Foundation.HRESULT = 2555916
COPYENGINE_S_CLOSE_PROGRAM: Windows.Win32.Foundation.HRESULT = 2555917
COPYENGINE_S_COLLISIONRESOLVED: Windows.Win32.Foundation.HRESULT = 2555918
COPYENGINE_S_PROGRESS_PAUSE: Windows.Win32.Foundation.HRESULT = 2555919
COPYENGINE_E_USER_CANCELLED: Windows.Win32.Foundation.HRESULT = -2144927744
COPYENGINE_E_CANCELLED: Windows.Win32.Foundation.HRESULT = -2144927743
COPYENGINE_E_REQUIRES_ELEVATION: Windows.Win32.Foundation.HRESULT = -2144927742
COPYENGINE_E_SAME_FILE: Windows.Win32.Foundation.HRESULT = -2144927741
COPYENGINE_E_DIFF_DIR: Windows.Win32.Foundation.HRESULT = -2144927740
COPYENGINE_E_MANY_SRC_1_DEST: Windows.Win32.Foundation.HRESULT = -2144927739
COPYENGINE_E_DEST_SUBTREE: Windows.Win32.Foundation.HRESULT = -2144927735
COPYENGINE_E_DEST_SAME_TREE: Windows.Win32.Foundation.HRESULT = -2144927734
COPYENGINE_E_FLD_IS_FILE_DEST: Windows.Win32.Foundation.HRESULT = -2144927733
COPYENGINE_E_FILE_IS_FLD_DEST: Windows.Win32.Foundation.HRESULT = -2144927732
COPYENGINE_E_FILE_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2144927731
COPYENGINE_E_REMOVABLE_FULL: Windows.Win32.Foundation.HRESULT = -2144927730
COPYENGINE_E_DEST_IS_RO_CD: Windows.Win32.Foundation.HRESULT = -2144927729
COPYENGINE_E_DEST_IS_RW_CD: Windows.Win32.Foundation.HRESULT = -2144927728
COPYENGINE_E_DEST_IS_R_CD: Windows.Win32.Foundation.HRESULT = -2144927727
COPYENGINE_E_DEST_IS_RO_DVD: Windows.Win32.Foundation.HRESULT = -2144927726
COPYENGINE_E_DEST_IS_RW_DVD: Windows.Win32.Foundation.HRESULT = -2144927725
COPYENGINE_E_DEST_IS_R_DVD: Windows.Win32.Foundation.HRESULT = -2144927724
COPYENGINE_E_SRC_IS_RO_CD: Windows.Win32.Foundation.HRESULT = -2144927723
COPYENGINE_E_SRC_IS_RW_CD: Windows.Win32.Foundation.HRESULT = -2144927722
COPYENGINE_E_SRC_IS_R_CD: Windows.Win32.Foundation.HRESULT = -2144927721
COPYENGINE_E_SRC_IS_RO_DVD: Windows.Win32.Foundation.HRESULT = -2144927720
COPYENGINE_E_SRC_IS_RW_DVD: Windows.Win32.Foundation.HRESULT = -2144927719
COPYENGINE_E_SRC_IS_R_DVD: Windows.Win32.Foundation.HRESULT = -2144927718
COPYENGINE_E_INVALID_FILES_SRC: Windows.Win32.Foundation.HRESULT = -2144927717
COPYENGINE_E_INVALID_FILES_DEST: Windows.Win32.Foundation.HRESULT = -2144927716
COPYENGINE_E_PATH_TOO_DEEP_SRC: Windows.Win32.Foundation.HRESULT = -2144927715
COPYENGINE_E_PATH_TOO_DEEP_DEST: Windows.Win32.Foundation.HRESULT = -2144927714
COPYENGINE_E_ROOT_DIR_SRC: Windows.Win32.Foundation.HRESULT = -2144927713
COPYENGINE_E_ROOT_DIR_DEST: Windows.Win32.Foundation.HRESULT = -2144927712
COPYENGINE_E_ACCESS_DENIED_SRC: Windows.Win32.Foundation.HRESULT = -2144927711
COPYENGINE_E_ACCESS_DENIED_DEST: Windows.Win32.Foundation.HRESULT = -2144927710
COPYENGINE_E_PATH_NOT_FOUND_SRC: Windows.Win32.Foundation.HRESULT = -2144927709
COPYENGINE_E_PATH_NOT_FOUND_DEST: Windows.Win32.Foundation.HRESULT = -2144927708
COPYENGINE_E_NET_DISCONNECT_SRC: Windows.Win32.Foundation.HRESULT = -2144927707
COPYENGINE_E_NET_DISCONNECT_DEST: Windows.Win32.Foundation.HRESULT = -2144927706
COPYENGINE_E_SHARING_VIOLATION_SRC: Windows.Win32.Foundation.HRESULT = -2144927705
COPYENGINE_E_SHARING_VIOLATION_DEST: Windows.Win32.Foundation.HRESULT = -2144927704
COPYENGINE_E_ALREADY_EXISTS_NORMAL: Windows.Win32.Foundation.HRESULT = -2144927703
COPYENGINE_E_ALREADY_EXISTS_READONLY: Windows.Win32.Foundation.HRESULT = -2144927702
COPYENGINE_E_ALREADY_EXISTS_SYSTEM: Windows.Win32.Foundation.HRESULT = -2144927701
COPYENGINE_E_ALREADY_EXISTS_FOLDER: Windows.Win32.Foundation.HRESULT = -2144927700
COPYENGINE_E_STREAM_LOSS: Windows.Win32.Foundation.HRESULT = -2144927699
COPYENGINE_E_EA_LOSS: Windows.Win32.Foundation.HRESULT = -2144927698
COPYENGINE_E_PROPERTY_LOSS: Windows.Win32.Foundation.HRESULT = -2144927697
COPYENGINE_E_PROPERTIES_LOSS: Windows.Win32.Foundation.HRESULT = -2144927696
COPYENGINE_E_ENCRYPTION_LOSS: Windows.Win32.Foundation.HRESULT = -2144927695
COPYENGINE_E_DISK_FULL: Windows.Win32.Foundation.HRESULT = -2144927694
COPYENGINE_E_DISK_FULL_CLEAN: Windows.Win32.Foundation.HRESULT = -2144927693
COPYENGINE_E_EA_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2144927692
COPYENGINE_E_CANT_REACH_SOURCE: Windows.Win32.Foundation.HRESULT = -2144927691
COPYENGINE_E_RECYCLE_UNKNOWN_ERROR: Windows.Win32.Foundation.HRESULT = -2144927691
COPYENGINE_E_RECYCLE_FORCE_NUKE: Windows.Win32.Foundation.HRESULT = -2144927690
COPYENGINE_E_RECYCLE_SIZE_TOO_BIG: Windows.Win32.Foundation.HRESULT = -2144927689
COPYENGINE_E_RECYCLE_PATH_TOO_LONG: Windows.Win32.Foundation.HRESULT = -2144927688
COPYENGINE_E_RECYCLE_BIN_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2144927686
COPYENGINE_E_NEWFILE_NAME_TOO_LONG: Windows.Win32.Foundation.HRESULT = -2144927685
COPYENGINE_E_NEWFOLDER_NAME_TOO_LONG: Windows.Win32.Foundation.HRESULT = -2144927684
COPYENGINE_E_DIR_NOT_EMPTY: Windows.Win32.Foundation.HRESULT = -2144927683
COPYENGINE_E_FAT_MAX_IN_ROOT: Windows.Win32.Foundation.HRESULT = -2144927682
COPYENGINE_E_ACCESSDENIED_READONLY: Windows.Win32.Foundation.HRESULT = -2144927681
COPYENGINE_E_REDIRECTED_TO_WEBPAGE: Windows.Win32.Foundation.HRESULT = -2144927680
COPYENGINE_E_SERVER_BAD_FILE_TYPE: Windows.Win32.Foundation.HRESULT = -2144927679
COPYENGINE_E_INTERNET_ITEM_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -2144927678
COPYENGINE_E_CANNOT_MOVE_FROM_RECYCLE_BIN: Windows.Win32.Foundation.HRESULT = -2144927677
COPYENGINE_E_CANNOT_MOVE_SHARED_FOLDER: Windows.Win32.Foundation.HRESULT = -2144927676
COPYENGINE_E_INTERNET_ITEM_STORAGE_PROVIDER_ERROR: Windows.Win32.Foundation.HRESULT = -2144927675
COPYENGINE_E_INTERNET_ITEM_STORAGE_PROVIDER_PAUSED: Windows.Win32.Foundation.HRESULT = -2144927674
COPYENGINE_E_REQUIRES_EDP_CONSENT: Windows.Win32.Foundation.HRESULT = -2144927673
COPYENGINE_E_BLOCKED_BY_EDP_POLICY: Windows.Win32.Foundation.HRESULT = -2144927672
COPYENGINE_E_REQUIRES_EDP_CONSENT_FOR_REMOVABLE_DRIVE: Windows.Win32.Foundation.HRESULT = -2144927671
COPYENGINE_E_BLOCKED_BY_EDP_FOR_REMOVABLE_DRIVE: Windows.Win32.Foundation.HRESULT = -2144927670
COPYENGINE_E_RMS_REQUIRES_EDP_CONSENT_FOR_REMOVABLE_DRIVE: Windows.Win32.Foundation.HRESULT = -2144927669
COPYENGINE_E_RMS_BLOCKED_BY_EDP_FOR_REMOVABLE_DRIVE: Windows.Win32.Foundation.HRESULT = -2144927668
COPYENGINE_E_WARNED_BY_DLP_POLICY: Windows.Win32.Foundation.HRESULT = -2144927667
COPYENGINE_E_BLOCKED_BY_DLP_POLICY: Windows.Win32.Foundation.HRESULT = -2144927666
COPYENGINE_E_SILENT_FAIL_BY_DLP_POLICY: Windows.Win32.Foundation.HRESULT = -2144927665
NETCACHE_E_NEGATIVE_CACHE: Windows.Win32.Foundation.HRESULT = -2144927488
EXECUTE_E_LAUNCH_APPLICATION: Windows.Win32.Foundation.HRESULT = -2144927487
SHELL_E_WRONG_BITDEPTH: Windows.Win32.Foundation.HRESULT = -2144927486
LINK_E_DELETE: Windows.Win32.Foundation.HRESULT = -2144927485
STORE_E_NEWER_VERSION_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2144927484
E_FILE_PLACEHOLDER_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2144927472
E_FILE_PLACEHOLDER_VERSION_MISMATCH: Windows.Win32.Foundation.HRESULT = -2144927471
E_FILE_PLACEHOLDER_SERVER_TIMED_OUT: Windows.Win32.Foundation.HRESULT = -2144927470
E_FILE_PLACEHOLDER_STORAGEPROVIDER_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2144927469
CAMERAROLL_E_NO_DOWNSAMPLING_REQUIRED: Windows.Win32.Foundation.HRESULT = -2144927456
E_ACTIVATIONDENIED_USERCLOSE: Windows.Win32.Foundation.HRESULT = -2144927440
E_ACTIVATIONDENIED_SHELLERROR: Windows.Win32.Foundation.HRESULT = -2144927439
E_ACTIVATIONDENIED_SHELLRESTART: Windows.Win32.Foundation.HRESULT = -2144927438
E_ACTIVATIONDENIED_UNEXPECTED: Windows.Win32.Foundation.HRESULT = -2144927437
E_ACTIVATIONDENIED_SHELLNOTREADY: Windows.Win32.Foundation.HRESULT = -2144927436
LIBRARY_E_NO_SAVE_LOCATION: Windows.Win32.Foundation.HRESULT = -2144927232
LIBRARY_E_NO_ACCESSIBLE_LOCATION: Windows.Win32.Foundation.HRESULT = -2144927231
E_USERTILE_UNSUPPORTEDFILETYPE: Windows.Win32.Foundation.HRESULT = -2144927216
E_USERTILE_CHANGEDISABLED: Windows.Win32.Foundation.HRESULT = -2144927215
E_USERTILE_LARGEORDYNAMIC: Windows.Win32.Foundation.HRESULT = -2144927214
E_USERTILE_VIDEOFRAMESIZE: Windows.Win32.Foundation.HRESULT = -2144927213
E_USERTILE_FILESIZE: Windows.Win32.Foundation.HRESULT = -2144927212
IMM_ACC_DOCKING_E_INSUFFICIENTHEIGHT: Windows.Win32.Foundation.HRESULT = -2144927184
IMM_ACC_DOCKING_E_DOCKOCCUPIED: Windows.Win32.Foundation.HRESULT = -2144927183
IMSC_E_SHELL_COMPONENT_STARTUP_FAILURE: Windows.Win32.Foundation.HRESULT = -2144927181
SHC_E_SHELL_COMPONENT_STARTUP_FAILURE: Windows.Win32.Foundation.HRESULT = -2144927180
E_TILE_NOTIFICATIONS_PLATFORM_FAILURE: Windows.Win32.Foundation.HRESULT = -2144927159
E_SHELL_EXTENSION_BLOCKED: Windows.Win32.Foundation.HRESULT = -2144926975
E_IMAGEFEED_CHANGEDISABLED: Windows.Win32.Foundation.HRESULT = -2144926960
ISHCUTCMDID_DOWNLOADICON: Int32 = 0
ISHCUTCMDID_INTSHORTCUTCREATE: Int32 = 1
ISHCUTCMDID_COMMITHISTORY: Int32 = 2
ISHCUTCMDID_SETUSERAWURL: Int32 = 3
SFBID_PIDLCHANGED: Int32 = 0
DBCID_EMPTY: Int32 = 0
DBCID_ONDRAG: Int32 = 1
DBCID_CLSIDOFBAR: Int32 = 2
DBCID_RESIZE: Int32 = 3
DBCID_GETBAR: Int32 = 4
DBCID_UPDATESIZE: Int32 = 5
BMICON_LARGE: Int32 = 0
BMICON_SMALL: Int32 = 1
CTF_INSIST: Int32 = 1
CTF_THREAD_REF: Int32 = 2
CTF_PROCESS_REF: Int32 = 4
CTF_COINIT_STA: Int32 = 8
CTF_COINIT: Int32 = 8
CTF_FREELIBANDEXIT: Int32 = 16
CTF_REF_COUNTED: Int32 = 32
CTF_WAIT_ALLOWCOM: Int32 = 64
CTF_UNUSED: Int32 = 128
CTF_INHERITWOW64: Int32 = 256
CTF_WAIT_NO_REENTRANCY: Int32 = 512
CTF_KEYBOARD_LOCALE: Int32 = 1024
CTF_OLEINITIALIZE: Int32 = 2048
CTF_COINIT_MTA: Int32 = 4096
CTF_NOADDREFLIB: Int32 = 8192
@winfunctype('USERENV.dll')
def LoadUserProfileA(hToken: Windows.Win32.Foundation.HANDLE, lpProfileInfo: POINTER(Windows.Win32.UI.Shell.PROFILEINFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def LoadUserProfileW(hToken: Windows.Win32.Foundation.HANDLE, lpProfileInfo: POINTER(Windows.Win32.UI.Shell.PROFILEINFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def UnloadUserProfile(hToken: Windows.Win32.Foundation.HANDLE, hProfile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetProfilesDirectoryA(lpProfileDir: Windows.Win32.Foundation.PSTR, lpcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetProfilesDirectoryW(lpProfileDir: Windows.Win32.Foundation.PWSTR, lpcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetProfileType(dwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def DeleteProfileA(lpSidString: Windows.Win32.Foundation.PSTR, lpProfilePath: Windows.Win32.Foundation.PSTR, lpComputerName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def DeleteProfileW(lpSidString: Windows.Win32.Foundation.PWSTR, lpProfilePath: Windows.Win32.Foundation.PWSTR, lpComputerName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def CreateProfile(pszUserSid: Windows.Win32.Foundation.PWSTR, pszUserName: Windows.Win32.Foundation.PWSTR, pszProfilePath: Windows.Win32.Foundation.PWSTR, cchProfilePath: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def GetDefaultUserProfileDirectoryA(lpProfileDir: Windows.Win32.Foundation.PSTR, lpcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetDefaultUserProfileDirectoryW(lpProfileDir: Windows.Win32.Foundation.PWSTR, lpcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetAllUsersProfileDirectoryA(lpProfileDir: Windows.Win32.Foundation.PSTR, lpcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetAllUsersProfileDirectoryW(lpProfileDir: Windows.Win32.Foundation.PWSTR, lpcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetUserProfileDirectoryA(hToken: Windows.Win32.Foundation.HANDLE, lpProfileDir: Windows.Win32.Foundation.PSTR, lpcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetUserProfileDirectoryW(hToken: Windows.Win32.Foundation.HANDLE, lpProfileDir: Windows.Win32.Foundation.PWSTR, lpcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMCTL32.dll')
def SetWindowSubclass(hWnd: Windows.Win32.Foundation.HWND, pfnSubclass: Windows.Win32.UI.Shell.SUBCLASSPROC, uIdSubclass: UIntPtr, dwRefData: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMCTL32.dll')
def GetWindowSubclass(hWnd: Windows.Win32.Foundation.HWND, pfnSubclass: Windows.Win32.UI.Shell.SUBCLASSPROC, uIdSubclass: UIntPtr, pdwRefData: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMCTL32.dll')
def RemoveWindowSubclass(hWnd: Windows.Win32.Foundation.HWND, pfnSubclass: Windows.Win32.UI.Shell.SUBCLASSPROC, uIdSubclass: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMCTL32.dll')
def DefSubclassProc(hWnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('USER32.dll')
def SetWindowContextHelpId(param0: Windows.Win32.Foundation.HWND, param1: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetWindowContextHelpId(param0: Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype('USER32.dll')
def SetMenuContextHelpId(param0: Windows.Win32.UI.WindowsAndMessaging.HMENU, param1: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetMenuContextHelpId(param0: Windows.Win32.UI.WindowsAndMessaging.HMENU) -> UInt32: ...
@winfunctype('USER32.dll')
def WinHelpA(hWndMain: Windows.Win32.Foundation.HWND, lpszHelp: Windows.Win32.Foundation.PSTR, uCommand: UInt32, dwData: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def WinHelpW(hWndMain: Windows.Win32.Foundation.HWND, lpszHelp: Windows.Win32.Foundation.PWSTR, uCommand: UInt32, dwData: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHSimpleIDListFromPath(pszPath: Windows.Win32.Foundation.PWSTR) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def SHCreateItemFromIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateItemFromParsingName(pszPath: Windows.Win32.Foundation.PWSTR, pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateItemWithParent(pidlParent: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), psfParent: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), riid: POINTER(Guid), ppvItem: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateItemFromRelativeName(psiParent: Windows.Win32.UI.Shell.IShellItem_head, pszName: Windows.Win32.Foundation.PWSTR, pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateItemInKnownFolder(kfid: POINTER(Guid), dwKFFlags: UInt32, pszItem: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetIDListFromObject(punk: Windows.Win32.System.Com.IUnknown_head, ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetItemFromObject(punk: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetNameFromIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), sigdnName: Windows.Win32.UI.Shell.SIGDN, ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetItemFromDataObject(pdtobj: Windows.Win32.System.Com.IDataObject_head, dwFlags: Windows.Win32.UI.Shell.DATAOBJ_GET_ITEM_FLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItemArray(pidlParent: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), psf: Windows.Win32.UI.Shell.IShellFolder_head, cidl: UInt32, ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), ppsiItemArray: POINTER(Windows.Win32.UI.Shell.IShellItemArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItemArrayFromDataObject(pdo: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItemArrayFromIDLists(cidl: UInt32, rgpidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), ppsiItemArray: POINTER(Windows.Win32.UI.Shell.IShellItemArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItemArrayFromShellItem(psi: Windows.Win32.UI.Shell.IShellItem_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateAssociationRegistration(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateDefaultExtractIcon(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SetCurrentProcessExplicitAppUserModelID(AppID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def GetCurrentProcessExplicitAppUserModelID(AppID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetTemporaryPropertyForItem(psi: Windows.Win32.UI.Shell.IShellItem_head, propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetTemporaryPropertyForItem(psi: Windows.Win32.UI.Shell.IShellItem_head, propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHShowManageLibraryUI(psiLibrary: Windows.Win32.UI.Shell.IShellItem_head, hwndOwner: Windows.Win32.Foundation.HWND, pszTitle: Windows.Win32.Foundation.PWSTR, pszInstruction: Windows.Win32.Foundation.PWSTR, lmdOptions: Windows.Win32.UI.Shell.LIBRARYMANAGEDIALOGOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHResolveLibrary(psiLibrary: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHAssocEnumHandlers(pszExtra: Windows.Win32.Foundation.PWSTR, afFilter: Windows.Win32.UI.Shell.ASSOC_FILTER, ppEnumHandler: POINTER(Windows.Win32.UI.Shell.IEnumAssocHandlers_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHAssocEnumHandlersForProtocolByApplication(protocol: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), enumHandlers: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserMarshal(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> c_char_p_no: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserUnmarshal(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> c_char_p_no: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> Void: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserMarshal64(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> c_char_p_no: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserUnmarshal64(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> c_char_p_no: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> Void: ...
@winfunctype('SHELL32.dll')
def SHCreateDefaultPropertiesOp(psi: Windows.Win32.UI.Shell.IShellItem_head, ppFileOp: POINTER(Windows.Win32.UI.Shell.IFileOperation_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetDefaultProperties(hwnd: Windows.Win32.Foundation.HWND, psi: Windows.Win32.UI.Shell.IShellItem_head, dwFileOpFlags: UInt32, pfops: Windows.Win32.UI.Shell.IFileOperationProgressSink_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetMalloc(ppMalloc: POINTER(Windows.Win32.System.Com.IMalloc_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHAlloc(cb: UIntPtr) -> c_void_p: ...
@winfunctype('SHELL32.dll')
def SHFree(pv: c_void_p) -> Void: ...
@winfunctype('SHELL32.dll')
def SHGetIconOverlayIndexA(pszIconPath: Windows.Win32.Foundation.PSTR, iIconIndex: Int32) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHGetIconOverlayIndexW(pszIconPath: Windows.Win32.Foundation.PWSTR, iIconIndex: Int32) -> Int32: ...
@winfunctype('SHELL32.dll')
def ILClone(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def ILCloneFirst(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def ILCombine(pidl1: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidl2: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def ILFree(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Void: ...
@winfunctype('SHELL32.dll')
def ILGetNext(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def ILGetSize(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> UInt32: ...
@winfunctype('SHELL32.dll')
def ILFindChild(pidlParent: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidlChild: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def ILFindLastID(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def ILRemoveLastID(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ILIsEqual(pidl1: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidl2: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ILIsParent(pidl1: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidl2: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), fImmediate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ILSaveToStream(pstm: Windows.Win32.System.Com.IStream_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def ILLoadFromStreamEx(pstm: Windows.Win32.System.Com.IStream_head, pidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def ILCreateFromPathA(pszPath: Windows.Win32.Foundation.PSTR) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def ILCreateFromPathW(pszPath: Windows.Win32.Foundation.PWSTR) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def SHILCreateFromPath(pszPath: Windows.Win32.Foundation.PWSTR, ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), rgfInOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def ILAppendID(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pmkid: POINTER(Windows.Win32.UI.Shell.Common.SHITEMID_head), fAppend: Windows.Win32.Foundation.BOOL) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def SHGetPathFromIDListEx(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UInt32, uOpts: Windows.Win32.UI.Shell.GPFIDL_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetPathFromIDListA(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetPathFromIDListW(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHCreateDirectory(hwnd: Windows.Win32.Foundation.HWND, pszPath: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHCreateDirectoryExA(hwnd: Windows.Win32.Foundation.HWND, pszPath: Windows.Win32.Foundation.PSTR, psa: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHCreateDirectoryExW(hwnd: Windows.Win32.Foundation.HWND, pszPath: Windows.Win32.Foundation.PWSTR, psa: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHOpenFolderAndSelectItems(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), cidl: UInt32, apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItem(pidlParent: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), psfParent: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppsi: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetSpecialFolderLocation(hwnd: Windows.Win32.Foundation.HWND, csidl: Int32, ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCloneSpecialIDList(hwnd: Windows.Win32.Foundation.HWND, csidl: Int32, fCreate: Windows.Win32.Foundation.BOOL) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def SHGetSpecialFolderPathA(hwnd: Windows.Win32.Foundation.HWND, pszPath: Windows.Win32.Foundation.PSTR, csidl: Int32, fCreate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetSpecialFolderPathW(hwnd: Windows.Win32.Foundation.HWND, pszPath: Windows.Win32.Foundation.PWSTR, csidl: Int32, fCreate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHFlushSFCache() -> Void: ...
@winfunctype('SHELL32.dll')
def SHGetFolderPathA(hwnd: Windows.Win32.Foundation.HWND, csidl: Int32, hToken: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetFolderPathW(hwnd: Windows.Win32.Foundation.HWND, csidl: Int32, hToken: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetFolderLocation(hwnd: Windows.Win32.Foundation.HWND, csidl: Int32, hToken: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetFolderPathA(csidl: Int32, hToken: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetFolderPathW(csidl: Int32, hToken: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetFolderPathAndSubDirA(hwnd: Windows.Win32.Foundation.HWND, csidl: Int32, hToken: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszSubDir: Windows.Win32.Foundation.PSTR, pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetFolderPathAndSubDirW(hwnd: Windows.Win32.Foundation.HWND, csidl: Int32, hToken: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszSubDir: Windows.Win32.Foundation.PWSTR, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetKnownFolderIDList(rfid: POINTER(Guid), dwFlags: UInt32, hToken: Windows.Win32.Foundation.HANDLE, ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetKnownFolderPath(rfid: POINTER(Guid), dwFlags: UInt32, hToken: Windows.Win32.Foundation.HANDLE, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetKnownFolderPath(rfid: POINTER(Guid), dwFlags: Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG, hToken: Windows.Win32.Foundation.HANDLE, ppszPath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetKnownFolderItem(rfid: POINTER(Guid), flags: Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG, hToken: Windows.Win32.Foundation.HANDLE, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetSetFolderCustomSettings(pfcs: POINTER(Windows.Win32.UI.Shell.SHFOLDERCUSTOMSETTINGS_head), pszPath: Windows.Win32.Foundation.PWSTR, dwReadWrite: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHBrowseForFolderA(lpbi: POINTER(Windows.Win32.UI.Shell.BROWSEINFOA_head)) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def SHBrowseForFolderW(lpbi: POINTER(Windows.Win32.UI.Shell.BROWSEINFOW_head)) -> POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head): ...
@winfunctype('SHELL32.dll')
def SHLoadInProc(rclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetDesktopFolder(ppshf: POINTER(Windows.Win32.UI.Shell.IShellFolder_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHChangeNotify(wEventId: Windows.Win32.UI.Shell.SHCNE_ID, uFlags: Windows.Win32.UI.Shell.SHCNF_FLAGS, dwItem1: c_void_p, dwItem2: c_void_p) -> Void: ...
@winfunctype('SHELL32.dll')
def SHAddToRecentDocs(uFlags: UInt32, pv: c_void_p) -> Void: ...
@winfunctype('SHELL32.dll')
def SHHandleUpdateImage(pidlExtra: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHUpdateImageA(pszHashItem: Windows.Win32.Foundation.PSTR, iIndex: Int32, uFlags: UInt32, iImageIndex: Int32) -> Void: ...
@winfunctype('SHELL32.dll')
def SHUpdateImageW(pszHashItem: Windows.Win32.Foundation.PWSTR, iIndex: Int32, uFlags: UInt32, iImageIndex: Int32) -> Void: ...
@winfunctype('SHELL32.dll')
def SHChangeNotifyRegister(hwnd: Windows.Win32.Foundation.HWND, fSources: Windows.Win32.UI.Shell.SHCNRF_SOURCE, fEvents: Int32, wMsg: UInt32, cEntries: Int32, pshcne: POINTER(Windows.Win32.UI.Shell.SHChangeNotifyEntry_head)) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHChangeNotifyDeregister(ulID: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHChangeNotification_Lock(hChange: Windows.Win32.Foundation.HANDLE, dwProcId: UInt32, pppidl: POINTER(POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))), plEvent: POINTER(Int32)) -> Windows.Win32.UI.Shell.ShFindChangeNotificationHandle: ...
@winfunctype('SHELL32.dll')
def SHChangeNotification_Unlock(hLock: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetRealIDL(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidlSimple: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppidlReal: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetInstanceExplorer(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetDataFromIDListA(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), nFormat: Windows.Win32.UI.Shell.SHGDFIL_FORMAT, pv: c_void_p, cb: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetDataFromIDListW(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), nFormat: Windows.Win32.UI.Shell.SHGDFIL_FORMAT, pv: c_void_p, cb: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def RestartDialog(hwnd: Windows.Win32.Foundation.HWND, pszPrompt: Windows.Win32.Foundation.PWSTR, dwReturn: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def RestartDialogEx(hwnd: Windows.Win32.Foundation.HWND, pszPrompt: Windows.Win32.Foundation.PWSTR, dwReturn: UInt32, dwReasonCode: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHCoCreateInstance(pszCLSID: Windows.Win32.Foundation.PWSTR, pclsid: POINTER(Guid), pUnkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateDataObject(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), cidl: UInt32, apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), pdtInner: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def CIDLData_CreateFromIDArray(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), cidl: UInt32, apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), ppdtobj: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateStdEnumFmtEtc(cfmt: UInt32, afmt: POINTER(Windows.Win32.System.Com.FORMATETC_head), ppenumFormatEtc: POINTER(Windows.Win32.System.Com.IEnumFORMATETC_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHDoDragDrop(hwnd: Windows.Win32.Foundation.HWND, pdata: Windows.Win32.System.Com.IDataObject_head, pdsrc: Windows.Win32.System.Ole.IDropSource_head, dwEffect: Windows.Win32.System.Ole.DROPEFFECT, pdwEffect: POINTER(Windows.Win32.System.Ole.DROPEFFECT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def DAD_SetDragImage(him: Windows.Win32.UI.Controls.HIMAGELIST, pptOffset: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_DragEnterEx(hwndTarget: Windows.Win32.Foundation.HWND, ptStart: Windows.Win32.Foundation.POINT) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_DragEnterEx2(hwndTarget: Windows.Win32.Foundation.HWND, ptStart: Windows.Win32.Foundation.POINT, pdtObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_ShowDragImage(fShow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_DragMove(pt: Windows.Win32.Foundation.POINT) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_DragLeave() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_AutoScroll(hwnd: Windows.Win32.Foundation.HWND, pad: POINTER(Windows.Win32.UI.Shell.AUTO_SCROLL_DATA_head), pptNow: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ReadCabinetState(pcs: POINTER(Windows.Win32.UI.Shell.CABINETSTATE_head), cLength: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def WriteCabinetState(pcs: POINTER(Windows.Win32.UI.Shell.CABINETSTATE_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathMakeUniqueName(pszUniqueName: Windows.Win32.Foundation.PWSTR, cchMax: UInt32, pszTemplate: Windows.Win32.Foundation.PWSTR, pszLongPlate: Windows.Win32.Foundation.PWSTR, pszDir: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathIsExe(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathCleanupSpec(pszDir: Windows.Win32.Foundation.PWSTR, pszSpec: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.UI.Shell.PCS_RET: ...
@winfunctype('SHELL32.dll')
def PathResolve(pszPath: Windows.Win32.Foundation.PWSTR, dirs: POINTER(POINTER(UInt16)), fFlags: Windows.Win32.UI.Shell.PRF_FLAGS) -> Int32: ...
@winfunctype('SHELL32.dll')
def GetFileNameFromBrowse(hwnd: Windows.Win32.Foundation.HWND, pszFilePath: Windows.Win32.Foundation.PWSTR, cchFilePath: UInt32, pszWorkingDir: Windows.Win32.Foundation.PWSTR, pszDefExt: Windows.Win32.Foundation.PWSTR, pszFilters: Windows.Win32.Foundation.PWSTR, pszTitle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DriveType(iDrive: Int32) -> Int32: ...
@winfunctype('SHELL32.dll')
def RealDriveType(iDrive: Int32, fOKToHitNet: Windows.Win32.Foundation.BOOL) -> Int32: ...
@winfunctype('SHELL32.dll')
def IsNetDrive(iDrive: Int32) -> Int32: ...
@winfunctype('SHELL32.dll')
def Shell_MergeMenus(hmDst: Windows.Win32.UI.WindowsAndMessaging.HMENU, hmSrc: Windows.Win32.UI.WindowsAndMessaging.HMENU, uInsert: UInt32, uIDAdjust: UInt32, uIDAdjustMax: UInt32, uFlags: Windows.Win32.UI.Shell.MM_FLAGS) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHObjectProperties(hwnd: Windows.Win32.Foundation.HWND, shopObjectType: Windows.Win32.UI.Shell.SHOP_TYPE, pszObjectName: Windows.Win32.Foundation.PWSTR, pszPropertyPage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHFormatDrive(hwnd: Windows.Win32.Foundation.HWND, drive: UInt32, fmtID: Windows.Win32.UI.Shell.SHFMT_ID, options: Windows.Win32.UI.Shell.SHFMT_OPT) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHDestroyPropSheetExtArray(hpsxa: Windows.Win32.UI.Shell.HPSXA) -> Void: ...
@winfunctype('SHELL32.dll')
def SHAddFromPropSheetExtArray(hpsxa: Windows.Win32.UI.Shell.HPSXA, lpfnAddPage: Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lParam: Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHReplaceFromPropSheetExtArray(hpsxa: Windows.Win32.UI.Shell.HPSXA, uPageID: UInt32, lpfnReplaceWith: Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lParam: Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype('SHELL32.dll')
def OpenRegStream(hkey: Windows.Win32.System.Registry.HKEY, pszSubkey: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR, grfMode: UInt32) -> Windows.Win32.System.Com.IStream_head: ...
@winfunctype('SHELL32.dll')
def SHFindFiles(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidlSaveFile: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathGetShortPath(pszLongPath: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHELL32.dll')
def PathYetAnotherMakeUniqueName(pszUniqueName: Windows.Win32.Foundation.PWSTR, pszPath: Windows.Win32.Foundation.PWSTR, pszShort: Windows.Win32.Foundation.PWSTR, pszFileSpec: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def Win32DeleteFile(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHRestricted(rest: Windows.Win32.UI.Shell.RESTRICTIONS) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SignalFileOpen(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def AssocGetDetailsOfPropKey(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pv: POINTER(Windows.Win32.System.Com.VARIANT_head), pfFoundPropKey: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHStartNetConnectionDialogW(hwnd: Windows.Win32.Foundation.HWND, pszRemoteName: Windows.Win32.Foundation.PWSTR, dwType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHDefExtractIconA(pszIconFile: Windows.Win32.Foundation.PSTR, iIndex: Int32, uFlags: UInt32, phiconLarge: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), nIconSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHDefExtractIconW(pszIconFile: Windows.Win32.Foundation.PWSTR, iIndex: Int32, uFlags: UInt32, phiconLarge: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), nIconSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHOpenWithDialog(hwndParent: Windows.Win32.Foundation.HWND, poainfo: POINTER(Windows.Win32.UI.Shell.OPENASINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def Shell_GetImageLists(phiml: POINTER(Windows.Win32.UI.Controls.HIMAGELIST), phimlSmall: POINTER(Windows.Win32.UI.Controls.HIMAGELIST)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def Shell_GetCachedImageIndex(pwszIconPath: Windows.Win32.Foundation.PWSTR, iIconIndex: Int32, uIconFlags: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def Shell_GetCachedImageIndexA(pszIconPath: Windows.Win32.Foundation.PSTR, iIconIndex: Int32, uIconFlags: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def Shell_GetCachedImageIndexW(pszIconPath: Windows.Win32.Foundation.PWSTR, iIconIndex: Int32, uIconFlags: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHValidateUNC(hwndOwner: Windows.Win32.Foundation.HWND, pszFile: Windows.Win32.Foundation.PWSTR, fConnect: Windows.Win32.UI.Shell.VALIDATEUNC_OPTION) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHSetInstanceExplorer(punk: Windows.Win32.System.Com.IUnknown_head) -> Void: ...
@winfunctype('SHELL32.dll')
def IsUserAnAdmin() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHShellFolderView_Message(hwndMain: Windows.Win32.Foundation.HWND, uMsg: UInt32, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellFolderView(pcsfv: POINTER(Windows.Win32.UI.Shell.SFV_CREATE_head), ppsv: POINTER(Windows.Win32.UI.Shell.IShellView_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def CDefFolderMenu_Create2(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), hwnd: Windows.Win32.Foundation.HWND, cidl: UInt32, apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), psf: Windows.Win32.UI.Shell.IShellFolder_head, pfn: Windows.Win32.UI.Shell.LPFNDFMCALLBACK, nKeys: UInt32, ahkeys: POINTER(Windows.Win32.System.Registry.HKEY), ppcm: POINTER(Windows.Win32.UI.Shell.IContextMenu_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateDefaultContextMenu(pdcm: POINTER(Windows.Win32.UI.Shell.DEFCONTEXTMENU_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHFind_InitMenuPopup(hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, hwndOwner: Windows.Win32.Foundation.HWND, idCmdFirst: UInt32, idCmdLast: UInt32) -> Windows.Win32.UI.Shell.IContextMenu_head: ...
@winfunctype('SHELL32.dll')
def SHCreateShellFolderViewEx(pcsfv: POINTER(Windows.Win32.UI.Shell.CSFV_head), ppsv: POINTER(Windows.Win32.UI.Shell.IShellView_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetSetSettings(lpss: POINTER(Windows.Win32.UI.Shell.SHELLSTATEA_head), dwMask: Windows.Win32.UI.Shell.SSF_MASK, bSet: Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('SHELL32.dll')
def SHGetSettings(psfs: POINTER(Windows.Win32.UI.Shell.SHELLFLAGSTATE_head), dwMask: UInt32) -> Void: ...
@winfunctype('SHELL32.dll')
def SHBindToParent(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), riid: POINTER(Guid), ppv: POINTER(c_void_p), ppidlLast: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHBindToFolderIDListParent(psfRoot: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), riid: POINTER(Guid), ppv: POINTER(c_void_p), ppidlLast: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHBindToFolderIDListParentEx(psfRoot: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppv: POINTER(c_void_p), ppidlLast: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHBindToObject(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHParseDisplayName(pszName: Windows.Win32.Foundation.PWSTR, pbc: Windows.Win32.System.Com.IBindCtx_head, ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), sfgaoIn: UInt32, psfgaoOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPathPrepareForWriteA(hwnd: Windows.Win32.Foundation.HWND, punkEnableModless: Windows.Win32.System.Com.IUnknown_head, pszPath: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPathPrepareForWriteW(hwnd: Windows.Win32.Foundation.HWND, punkEnableModless: Windows.Win32.System.Com.IUnknown_head, pszPath: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateFileExtractIconW(pszFile: Windows.Win32.Foundation.PWSTR, dwFileAttributes: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHLimitInputEdit(hwndEdit: Windows.Win32.Foundation.HWND, psf: Windows.Win32.UI.Shell.IShellFolder_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetAttributesFromDataObject(pdo: Windows.Win32.System.Com.IDataObject_head, dwAttributeMask: UInt32, pdwAttributes: POINTER(UInt32), pcItems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHMapPIDLToSystemImageListIndex(pshf: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), piIndexSel: POINTER(Int32)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHCLSIDFromString(psz: Windows.Win32.Foundation.PWSTR, pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def PickIconDlg(hwnd: Windows.Win32.Foundation.HWND, pszIconPath: Windows.Win32.Foundation.PWSTR, cchIconPath: UInt32, piIconIndex: POINTER(Int32)) -> Int32: ...
@winfunctype('SHELL32.dll')
def StgMakeUniqueName(pstgParent: Windows.Win32.System.Com.StructuredStorage.IStorage_head, pszFileSpec: Windows.Win32.Foundation.PWSTR, grfMode: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHChangeNotifyRegisterThread(status: Windows.Win32.UI.Shell.SCNRT_STATUS) -> Void: ...
@winfunctype('SHELL32.dll')
def PathQualify(psz: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHELL32.dll')
def PathIsSlowA(pszFile: Windows.Win32.Foundation.PSTR, dwAttr: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathIsSlowW(pszFile: Windows.Win32.Foundation.PWSTR, dwAttr: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHCreatePropSheetExtArray(hKey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PWSTR, max_iface: UInt32) -> Windows.Win32.UI.Shell.HPSXA: ...
@winfunctype('SHELL32.dll')
def SHOpenPropSheetW(pszCaption: Windows.Win32.Foundation.PWSTR, ahkeys: POINTER(Windows.Win32.System.Registry.HKEY), ckeys: UInt32, pclsidDefault: POINTER(Guid), pdtobj: Windows.Win32.System.Com.IDataObject_head, psb: Windows.Win32.UI.Shell.IShellBrowser_head, pStartPage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHDOCVW.dll')
def SoftwareUpdateMessageBox(hWnd: Windows.Win32.Foundation.HWND, pszDistUnit: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, psdi: POINTER(Windows.Win32.System.Com.Urlmon.SOFTDISTINFO_head)) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHMultiFileProperties(pdtobj: Windows.Win32.System.Com.IDataObject_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateQueryCancelAutoPlayMoniker(ppmoniker: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHDOCVW.dll')
def ImportPrivacySettings(pszFilename: Windows.Win32.Foundation.PWSTR, pfParsePrivacyPreferences: POINTER(Windows.Win32.Foundation.BOOL), pfParsePerSiteRules: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-0.dll')
def GetScaleFactorForDevice(deviceType: Windows.Win32.UI.Shell.DISPLAY_DEVICE_TYPE) -> Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-0.dll')
def RegisterScaleChangeNotifications(displayDevice: Windows.Win32.UI.Shell.DISPLAY_DEVICE_TYPE, hwndNotify: Windows.Win32.Foundation.HWND, uMsgNotify: UInt32, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-0.dll')
def RevokeScaleChangeNotifications(displayDevice: Windows.Win32.UI.Shell.DISPLAY_DEVICE_TYPE, dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def GetScaleFactorForMonitor(hMon: Windows.Win32.Graphics.Gdi.HMONITOR, pScale: POINTER(Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def RegisterScaleChangeEvent(hEvent: Windows.Win32.Foundation.HANDLE, pdwCookie: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def UnregisterScaleChangeEvent(dwCookie: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-2.dll')
def GetDpiForShellUIComponent(param0: Windows.Win32.UI.Shell.SHELL_UI_COMPONENT) -> UInt32: ...
@winfunctype('SHELL32.dll')
def CommandLineToArgvW(lpCmdLine: Windows.Win32.Foundation.PWSTR, pNumArgs: POINTER(Int32)) -> POINTER(Windows.Win32.Foundation.PWSTR): ...
@winfunctype('SHELL32.dll')
def DragQueryFileA(hDrop: Windows.Win32.UI.Shell.HDROP, iFile: UInt32, lpszFile: Windows.Win32.Foundation.PSTR, cch: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def DragQueryFileW(hDrop: Windows.Win32.UI.Shell.HDROP, iFile: UInt32, lpszFile: Windows.Win32.Foundation.PWSTR, cch: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def DragQueryPoint(hDrop: Windows.Win32.UI.Shell.HDROP, ppt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DragFinish(hDrop: Windows.Win32.UI.Shell.HDROP) -> Void: ...
@winfunctype('SHELL32.dll')
def DragAcceptFiles(hWnd: Windows.Win32.Foundation.HWND, fAccept: Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('SHELL32.dll')
def ShellExecuteA(hwnd: Windows.Win32.Foundation.HWND, lpOperation: Windows.Win32.Foundation.PSTR, lpFile: Windows.Win32.Foundation.PSTR, lpParameters: Windows.Win32.Foundation.PSTR, lpDirectory: Windows.Win32.Foundation.PSTR, nShowCmd: Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('SHELL32.dll')
def ShellExecuteW(hwnd: Windows.Win32.Foundation.HWND, lpOperation: Windows.Win32.Foundation.PWSTR, lpFile: Windows.Win32.Foundation.PWSTR, lpParameters: Windows.Win32.Foundation.PWSTR, lpDirectory: Windows.Win32.Foundation.PWSTR, nShowCmd: Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('SHELL32.dll')
def FindExecutableA(lpFile: Windows.Win32.Foundation.PSTR, lpDirectory: Windows.Win32.Foundation.PSTR, lpResult: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('SHELL32.dll')
def FindExecutableW(lpFile: Windows.Win32.Foundation.PWSTR, lpDirectory: Windows.Win32.Foundation.PWSTR, lpResult: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('SHELL32.dll')
def ShellAboutA(hWnd: Windows.Win32.Foundation.HWND, szApp: Windows.Win32.Foundation.PSTR, szOtherStuff: Windows.Win32.Foundation.PSTR, hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON) -> Int32: ...
@winfunctype('SHELL32.dll')
def ShellAboutW(hWnd: Windows.Win32.Foundation.HWND, szApp: Windows.Win32.Foundation.PWSTR, szOtherStuff: Windows.Win32.Foundation.PWSTR, hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON) -> Int32: ...
@winfunctype('SHELL32.dll')
def DuplicateIcon(hInst: Windows.Win32.Foundation.HINSTANCE, hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON) -> Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractAssociatedIconA(hInst: Windows.Win32.Foundation.HINSTANCE, pszIconPath: Windows.Win32.Foundation.PSTR, piIcon: POINTER(UInt16)) -> Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractAssociatedIconW(hInst: Windows.Win32.Foundation.HINSTANCE, pszIconPath: Windows.Win32.Foundation.PWSTR, piIcon: POINTER(UInt16)) -> Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractAssociatedIconExA(hInst: Windows.Win32.Foundation.HINSTANCE, pszIconPath: Windows.Win32.Foundation.PSTR, piIconIndex: POINTER(UInt16), piIconId: POINTER(UInt16)) -> Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractAssociatedIconExW(hInst: Windows.Win32.Foundation.HINSTANCE, pszIconPath: Windows.Win32.Foundation.PWSTR, piIconIndex: POINTER(UInt16), piIconId: POINTER(UInt16)) -> Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractIconA(hInst: Windows.Win32.Foundation.HINSTANCE, pszExeFileName: Windows.Win32.Foundation.PSTR, nIconIndex: UInt32) -> Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractIconW(hInst: Windows.Win32.Foundation.HINSTANCE, pszExeFileName: Windows.Win32.Foundation.PWSTR, nIconIndex: UInt32) -> Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def SHAppBarMessage(dwMessage: UInt32, pData: POINTER(Windows.Win32.UI.Shell.APPBARDATA_head)) -> UIntPtr: ...
@winfunctype('SHELL32.dll')
def DoEnvironmentSubstA(pszSrc: Windows.Win32.Foundation.PSTR, cchSrc: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def DoEnvironmentSubstW(pszSrc: Windows.Win32.Foundation.PWSTR, cchSrc: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def ExtractIconExA(lpszFile: Windows.Win32.Foundation.PSTR, nIconIndex: Int32, phiconLarge: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), nIcons: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def ExtractIconExW(lpszFile: Windows.Win32.Foundation.PWSTR, nIconIndex: Int32, phiconLarge: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), nIcons: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHFileOperationA(lpFileOp: POINTER(Windows.Win32.UI.Shell.SHFILEOPSTRUCTA_head)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHFileOperationW(lpFileOp: POINTER(Windows.Win32.UI.Shell.SHFILEOPSTRUCTW_head)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHFreeNameMappings(hNameMappings: Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('SHELL32.dll')
def ShellExecuteExA(pExecInfo: POINTER(Windows.Win32.UI.Shell.SHELLEXECUTEINFOA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ShellExecuteExW(pExecInfo: POINTER(Windows.Win32.UI.Shell.SHELLEXECUTEINFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHCreateProcessAsUserW(pscpi: POINTER(Windows.Win32.UI.Shell.SHCREATEPROCESSINFOW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHEvaluateSystemCommandTemplate(pszCmdTemplate: Windows.Win32.Foundation.PWSTR, ppszApplication: POINTER(Windows.Win32.Foundation.PWSTR), ppszCommandLine: POINTER(Windows.Win32.Foundation.PWSTR), ppszParameters: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def AssocCreateForClasses(rgClasses: POINTER(Windows.Win32.UI.Shell.ASSOCIATIONELEMENT_head), cClasses: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHQueryRecycleBinA(pszRootPath: Windows.Win32.Foundation.PSTR, pSHQueryRBInfo: POINTER(Windows.Win32.UI.Shell.SHQUERYRBINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHQueryRecycleBinW(pszRootPath: Windows.Win32.Foundation.PWSTR, pSHQueryRBInfo: POINTER(Windows.Win32.UI.Shell.SHQUERYRBINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHEmptyRecycleBinA(hwnd: Windows.Win32.Foundation.HWND, pszRootPath: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHEmptyRecycleBinW(hwnd: Windows.Win32.Foundation.HWND, pszRootPath: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHQueryUserNotificationState(pquns: POINTER(Windows.Win32.UI.Shell.QUERY_USER_NOTIFICATION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def Shell_NotifyIconA(dwMessage: Windows.Win32.UI.Shell.NOTIFY_ICON_MESSAGE, lpData: POINTER(Windows.Win32.UI.Shell.NOTIFYICONDATAA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def Shell_NotifyIconW(dwMessage: Windows.Win32.UI.Shell.NOTIFY_ICON_MESSAGE, lpData: POINTER(Windows.Win32.UI.Shell.NOTIFYICONDATAW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def Shell_NotifyIconGetRect(identifier: POINTER(Windows.Win32.UI.Shell.NOTIFYICONIDENTIFIER_head), iconLocation: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetFileInfoA(pszPath: Windows.Win32.Foundation.PSTR, dwFileAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, psfi: POINTER(Windows.Win32.UI.Shell.SHFILEINFOA_head), cbFileInfo: UInt32, uFlags: Windows.Win32.UI.Shell.SHGFI_FLAGS) -> UIntPtr: ...
@winfunctype('SHELL32.dll')
def SHGetFileInfoW(pszPath: Windows.Win32.Foundation.PWSTR, dwFileAttributes: Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, psfi: POINTER(Windows.Win32.UI.Shell.SHFILEINFOW_head), cbFileInfo: UInt32, uFlags: Windows.Win32.UI.Shell.SHGFI_FLAGS) -> UIntPtr: ...
@winfunctype('SHELL32.dll')
def SHGetStockIconInfo(siid: Windows.Win32.UI.Shell.SHSTOCKICONID, uFlags: Windows.Win32.UI.Shell.SHGSI_FLAGS, psii: POINTER(Windows.Win32.UI.Shell.SHSTOCKICONINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetDiskFreeSpaceExA(pszDirectoryName: Windows.Win32.Foundation.PSTR, pulFreeBytesAvailableToCaller: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head), pulTotalNumberOfBytes: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head), pulTotalNumberOfFreeBytes: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetDiskFreeSpaceExW(pszDirectoryName: Windows.Win32.Foundation.PWSTR, pulFreeBytesAvailableToCaller: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head), pulTotalNumberOfBytes: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head), pulTotalNumberOfFreeBytes: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetNewLinkInfoA(pszLinkTo: Windows.Win32.Foundation.PSTR, pszDir: Windows.Win32.Foundation.PSTR, pszName: Windows.Win32.Foundation.PSTR, pfMustCopy: POINTER(Windows.Win32.Foundation.BOOL), uFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetNewLinkInfoW(pszLinkTo: Windows.Win32.Foundation.PWSTR, pszDir: Windows.Win32.Foundation.PWSTR, pszName: Windows.Win32.Foundation.PWSTR, pfMustCopy: POINTER(Windows.Win32.Foundation.BOOL), uFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHInvokePrinterCommandA(hwnd: Windows.Win32.Foundation.HWND, uAction: UInt32, lpBuf1: Windows.Win32.Foundation.PSTR, lpBuf2: Windows.Win32.Foundation.PSTR, fModal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHInvokePrinterCommandW(hwnd: Windows.Win32.Foundation.HWND, uAction: UInt32, lpBuf1: Windows.Win32.Foundation.PWSTR, lpBuf2: Windows.Win32.Foundation.PWSTR, fModal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHLoadNonloadedIconOverlayIdentifiers() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHIsFileAvailableOffline(pwszPath: Windows.Win32.Foundation.PWSTR, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetLocalizedName(pszPath: Windows.Win32.Foundation.PWSTR, pszResModule: Windows.Win32.Foundation.PWSTR, idsRes: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHRemoveLocalizedName(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetLocalizedName(pszPath: Windows.Win32.Foundation.PWSTR, pszResModule: Windows.Win32.Foundation.PWSTR, cch: UInt32, pidsRes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@cfunctype('SHLWAPI.dll')
def ShellMessageBoxA(hAppInst: Windows.Win32.Foundation.HINSTANCE, hWnd: Windows.Win32.Foundation.HWND, lpcText: Windows.Win32.Foundation.PSTR, lpcTitle: Windows.Win32.Foundation.PSTR, fuStyle: Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_STYLE) -> Int32: ...
@cfunctype('SHLWAPI.dll')
def ShellMessageBoxW(hAppInst: Windows.Win32.Foundation.HINSTANCE, hWnd: Windows.Win32.Foundation.HWND, lpcText: Windows.Win32.Foundation.PWSTR, lpcTitle: Windows.Win32.Foundation.PWSTR, fuStyle: Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_STYLE) -> Int32: ...
@winfunctype('SHELL32.dll')
def IsLFNDriveA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def IsLFNDriveW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHEnumerateUnreadMailAccountsW(hKeyUser: Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszMailAddress: Windows.Win32.Foundation.PWSTR, cchMailAddress: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetUnreadMailCountW(hKeyUser: Windows.Win32.System.Registry.HKEY, pszMailAddress: Windows.Win32.Foundation.PWSTR, pdwCount: POINTER(UInt32), pFileTime: POINTER(Windows.Win32.Foundation.FILETIME_head), pszShellExecuteCommand: Windows.Win32.Foundation.PWSTR, cchShellExecuteCommand: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetUnreadMailCountW(pszMailAddress: Windows.Win32.Foundation.PWSTR, dwCount: UInt32, pszShellExecuteCommand: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHTestTokenMembership(hToken: Windows.Win32.Foundation.HANDLE, ulRID: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetImageList(iImageList: Int32, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def InitNetworkAddressControl() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetDriveMedia(pszDrive: Windows.Win32.Foundation.PWSTR, pdwMediaContent: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrChrA(pszStart: Windows.Win32.Foundation.PSTR, wMatch: UInt16) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrChrW(pszStart: Windows.Win32.Foundation.PWSTR, wMatch: Char) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrChrIA(pszStart: Windows.Win32.Foundation.PSTR, wMatch: UInt16) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrChrIW(pszStart: Windows.Win32.Foundation.PWSTR, wMatch: Char) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrChrNW(pszStart: Windows.Win32.Foundation.PWSTR, wMatch: Char, cchMax: UInt32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrChrNIW(pszStart: Windows.Win32.Foundation.PWSTR, wMatch: Char, cchMax: UInt32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNA(psz1: Windows.Win32.Foundation.PSTR, psz2: Windows.Win32.Foundation.PSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNW(psz1: Windows.Win32.Foundation.PWSTR, psz2: Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNIA(psz1: Windows.Win32.Foundation.PSTR, psz2: Windows.Win32.Foundation.PSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNIW(psz1: Windows.Win32.Foundation.PWSTR, psz2: Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCSpnA(pszStr: Windows.Win32.Foundation.PSTR, pszSet: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCSpnW(pszStr: Windows.Win32.Foundation.PWSTR, pszSet: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCSpnIA(pszStr: Windows.Win32.Foundation.PSTR, pszSet: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCSpnIW(pszStr: Windows.Win32.Foundation.PWSTR, pszSet: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrDupA(pszSrch: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrDupW(pszSrch: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrFormatByteSizeEx(ull: UInt64, flags: Windows.Win32.UI.Shell.SFBS_FLAGS, pszBuf: Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrFormatByteSizeA(dw: UInt32, pszBuf: Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrFormatByteSize64A(qdw: Int64, pszBuf: Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrFormatByteSizeW(qdw: Int64, pszBuf: Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrFormatKBSizeW(qdw: Int64, pszBuf: Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrFormatKBSizeA(qdw: Int64, pszBuf: Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrFromTimeIntervalA(pszOut: Windows.Win32.Foundation.PSTR, cchMax: UInt32, dwTimeMS: UInt32, digits: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrFromTimeIntervalW(pszOut: Windows.Win32.Foundation.PWSTR, cchMax: UInt32, dwTimeMS: UInt32, digits: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrIsIntlEqualA(fCaseSens: Windows.Win32.Foundation.BOOL, pszString1: Windows.Win32.Foundation.PSTR, pszString2: Windows.Win32.Foundation.PSTR, nChar: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrIsIntlEqualW(fCaseSens: Windows.Win32.Foundation.BOOL, pszString1: Windows.Win32.Foundation.PWSTR, pszString2: Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrNCatA(psz1: Windows.Win32.Foundation.PSTR, psz2: Windows.Win32.Foundation.PSTR, cchMax: Int32) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrNCatW(psz1: Windows.Win32.Foundation.PWSTR, psz2: Windows.Win32.Foundation.PWSTR, cchMax: Int32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrPBrkA(psz: Windows.Win32.Foundation.PSTR, pszSet: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrPBrkW(psz: Windows.Win32.Foundation.PWSTR, pszSet: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrRChrA(pszStart: Windows.Win32.Foundation.PSTR, pszEnd: Windows.Win32.Foundation.PSTR, wMatch: UInt16) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrRChrW(pszStart: Windows.Win32.Foundation.PWSTR, pszEnd: Windows.Win32.Foundation.PWSTR, wMatch: Char) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrRChrIA(pszStart: Windows.Win32.Foundation.PSTR, pszEnd: Windows.Win32.Foundation.PSTR, wMatch: UInt16) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrRChrIW(pszStart: Windows.Win32.Foundation.PWSTR, pszEnd: Windows.Win32.Foundation.PWSTR, wMatch: Char) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrRStrIA(pszSource: Windows.Win32.Foundation.PSTR, pszLast: Windows.Win32.Foundation.PSTR, pszSrch: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrRStrIW(pszSource: Windows.Win32.Foundation.PWSTR, pszLast: Windows.Win32.Foundation.PWSTR, pszSrch: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrSpnA(psz: Windows.Win32.Foundation.PSTR, pszSet: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrSpnW(psz: Windows.Win32.Foundation.PWSTR, pszSet: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrStrA(pszFirst: Windows.Win32.Foundation.PSTR, pszSrch: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrStrW(pszFirst: Windows.Win32.Foundation.PWSTR, pszSrch: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrStrIA(pszFirst: Windows.Win32.Foundation.PSTR, pszSrch: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrStrIW(pszFirst: Windows.Win32.Foundation.PWSTR, pszSrch: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrStrNW(pszFirst: Windows.Win32.Foundation.PWSTR, pszSrch: Windows.Win32.Foundation.PWSTR, cchMax: UInt32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrStrNIW(pszFirst: Windows.Win32.Foundation.PWSTR, pszSrch: Windows.Win32.Foundation.PWSTR, cchMax: UInt32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrToIntA(pszSrc: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrToIntW(pszSrc: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrToIntExA(pszString: Windows.Win32.Foundation.PSTR, dwFlags: Int32, piRet: POINTER(Int32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrToIntExW(pszString: Windows.Win32.Foundation.PWSTR, dwFlags: Int32, piRet: POINTER(Int32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrToInt64ExA(pszString: Windows.Win32.Foundation.PSTR, dwFlags: Int32, pllRet: POINTER(Int64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrToInt64ExW(pszString: Windows.Win32.Foundation.PWSTR, dwFlags: Int32, pllRet: POINTER(Int64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrTrimA(psz: Windows.Win32.Foundation.PSTR, pszTrimChars: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrTrimW(psz: Windows.Win32.Foundation.PWSTR, pszTrimChars: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrCatW(psz1: Windows.Win32.Foundation.PWSTR, psz2: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrCmpW(psz1: Windows.Win32.Foundation.PWSTR, psz2: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpIW(psz1: Windows.Win32.Foundation.PWSTR, psz2: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCpyW(psz1: Windows.Win32.Foundation.PWSTR, psz2: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrCpyNW(pszDst: Windows.Win32.Foundation.PWSTR, pszSrc: Windows.Win32.Foundation.PWSTR, cchMax: Int32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrCatBuffW(pszDest: Windows.Win32.Foundation.PWSTR, pszSrc: Windows.Win32.Foundation.PWSTR, cchDestBuffSize: Int32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrCatBuffA(pszDest: Windows.Win32.Foundation.PSTR, pszSrc: Windows.Win32.Foundation.PSTR, cchDestBuffSize: Int32) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def ChrCmpIA(w1: UInt16, w2: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def ChrCmpIW(w1: Char, w2: Char) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def wvnsprintfA(pszDest: Windows.Win32.Foundation.PSTR, cchDest: Int32, pszFmt: Windows.Win32.Foundation.PSTR, arglist: POINTER(SByte)) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def wvnsprintfW(pszDest: Windows.Win32.Foundation.PWSTR, cchDest: Int32, pszFmt: Windows.Win32.Foundation.PWSTR, arglist: POINTER(SByte)) -> Int32: ...
@cfunctype('SHLWAPI.dll')
def wnsprintfA(pszDest: Windows.Win32.Foundation.PSTR, cchDest: Int32, pszFmt: Windows.Win32.Foundation.PSTR) -> Int32: ...
@cfunctype('SHLWAPI.dll')
def wnsprintfW(pszDest: Windows.Win32.Foundation.PWSTR, cchDest: Int32, pszFmt: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrRetToStrA(pstr: POINTER(Windows.Win32.UI.Shell.Common.STRRET_head), pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppsz: POINTER(Windows.Win32.Foundation.PSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrRetToStrW(pstr: POINTER(Windows.Win32.UI.Shell.Common.STRRET_head), pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppsz: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrRetToBufA(pstr: POINTER(Windows.Win32.UI.Shell.Common.STRRET_head), pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pszBuf: Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrRetToBufW(pstr: POINTER(Windows.Win32.UI.Shell.Common.STRRET_head), pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pszBuf: Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHStrDupA(psz: Windows.Win32.Foundation.PSTR, ppwsz: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHStrDupW(psz: Windows.Win32.Foundation.PWSTR, ppwsz: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrCmpLogicalW(psz1: Windows.Win32.Foundation.PWSTR, psz2: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCatChainW(pszDst: Windows.Win32.Foundation.PWSTR, cchDst: UInt32, ichAt: UInt32, pszSrc: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('SHLWAPI.dll')
def StrRetToBSTR(pstr: POINTER(Windows.Win32.UI.Shell.Common.STRRET_head), pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHLoadIndirectString(pszSource: Windows.Win32.Foundation.PWSTR, pszOutBuf: Windows.Win32.Foundation.PWSTR, cchOutBuf: UInt32, ppvReserved: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IsCharSpaceA(wch: Windows.Win32.Foundation.CHAR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def IsCharSpaceW(wch: Char) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrCmpCA(pszStr1: Windows.Win32.Foundation.PSTR, pszStr2: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpCW(pszStr1: Windows.Win32.Foundation.PWSTR, pszStr2: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpICA(pszStr1: Windows.Win32.Foundation.PSTR, pszStr2: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpICW(pszStr1: Windows.Win32.Foundation.PWSTR, pszStr2: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNCA(pszStr1: Windows.Win32.Foundation.PSTR, pszStr2: Windows.Win32.Foundation.PSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNCW(pszStr1: Windows.Win32.Foundation.PWSTR, pszStr2: Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNICA(pszStr1: Windows.Win32.Foundation.PSTR, pszStr2: Windows.Win32.Foundation.PSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNICW(pszStr1: Windows.Win32.Foundation.PWSTR, pszStr2: Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def IntlStrEqWorkerA(fCaseSens: Windows.Win32.Foundation.BOOL, lpString1: Windows.Win32.Foundation.PSTR, lpString2: Windows.Win32.Foundation.PSTR, nChar: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def IntlStrEqWorkerW(fCaseSens: Windows.Win32.Foundation.BOOL, lpString1: Windows.Win32.Foundation.PWSTR, lpString2: Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathAddBackslashA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathAddBackslashW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathAddExtensionA(pszPath: Windows.Win32.Foundation.PSTR, pszExt: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathAddExtensionW(pszPath: Windows.Win32.Foundation.PWSTR, pszExt: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathAppendA(pszPath: Windows.Win32.Foundation.PSTR, pszMore: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathAppendW(pszPath: Windows.Win32.Foundation.PWSTR, pszMore: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathBuildRootA(pszRoot: Windows.Win32.Foundation.PSTR, iDrive: Int32) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathBuildRootW(pszRoot: Windows.Win32.Foundation.PWSTR, iDrive: Int32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathCanonicalizeA(pszBuf: Windows.Win32.Foundation.PSTR, pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathCanonicalizeW(pszBuf: Windows.Win32.Foundation.PWSTR, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathCombineA(pszDest: Windows.Win32.Foundation.PSTR, pszDir: Windows.Win32.Foundation.PSTR, pszFile: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathCombineW(pszDest: Windows.Win32.Foundation.PWSTR, pszDir: Windows.Win32.Foundation.PWSTR, pszFile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathCompactPathA(hDC: Windows.Win32.Graphics.Gdi.HDC, pszPath: Windows.Win32.Foundation.PSTR, dx: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathCompactPathW(hDC: Windows.Win32.Graphics.Gdi.HDC, pszPath: Windows.Win32.Foundation.PWSTR, dx: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathCompactPathExA(pszOut: Windows.Win32.Foundation.PSTR, pszSrc: Windows.Win32.Foundation.PSTR, cchMax: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathCompactPathExW(pszOut: Windows.Win32.Foundation.PWSTR, pszSrc: Windows.Win32.Foundation.PWSTR, cchMax: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathCommonPrefixA(pszFile1: Windows.Win32.Foundation.PSTR, pszFile2: Windows.Win32.Foundation.PSTR, achPath: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def PathCommonPrefixW(pszFile1: Windows.Win32.Foundation.PWSTR, pszFile2: Windows.Win32.Foundation.PWSTR, achPath: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def PathFileExistsA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathFileExistsW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathFindExtensionA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindExtensionW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindFileNameA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindFileNameW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindNextComponentA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindNextComponentW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindOnPathA(pszPath: Windows.Win32.Foundation.PSTR, ppszOtherDirs: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathFindOnPathW(pszPath: Windows.Win32.Foundation.PWSTR, ppszOtherDirs: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathFindSuffixArrayA(pszPath: Windows.Win32.Foundation.PSTR, apszSuffix: POINTER(Windows.Win32.Foundation.PSTR), iArraySize: Int32) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindSuffixArrayW(pszPath: Windows.Win32.Foundation.PWSTR, apszSuffix: POINTER(Windows.Win32.Foundation.PWSTR), iArraySize: Int32) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathGetArgsA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathGetArgsW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathIsLFNFileSpecA(pszName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsLFNFileSpecW(pszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathGetCharTypeA(ch: Byte) -> UInt32: ...
@winfunctype('SHLWAPI.dll')
def PathGetCharTypeW(ch: Char) -> UInt32: ...
@winfunctype('SHLWAPI.dll')
def PathGetDriveNumberA(pszPath: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def PathGetDriveNumberW(pszPath: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def PathIsDirectoryA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsDirectoryW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsDirectoryEmptyA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsDirectoryEmptyW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsFileSpecA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsFileSpecW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsPrefixA(pszPrefix: Windows.Win32.Foundation.PSTR, pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsPrefixW(pszPrefix: Windows.Win32.Foundation.PWSTR, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsRelativeA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsRelativeW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsRootA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsRootW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsSameRootA(pszPath1: Windows.Win32.Foundation.PSTR, pszPath2: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsSameRootW(pszPath1: Windows.Win32.Foundation.PWSTR, pszPath2: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsUNCA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsUNCW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsNetworkPathA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsNetworkPathW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsUNCServerA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsUNCServerW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsUNCServerShareA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsUNCServerShareW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsContentTypeA(pszPath: Windows.Win32.Foundation.PSTR, pszContentType: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsContentTypeW(pszPath: Windows.Win32.Foundation.PWSTR, pszContentType: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsURLA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsURLW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMakePrettyA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMakePrettyW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMatchSpecA(pszFile: Windows.Win32.Foundation.PSTR, pszSpec: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMatchSpecW(pszFile: Windows.Win32.Foundation.PWSTR, pszSpec: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMatchSpecExA(pszFile: Windows.Win32.Foundation.PSTR, pszSpec: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def PathMatchSpecExW(pszFile: Windows.Win32.Foundation.PWSTR, pszSpec: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def PathParseIconLocationA(pszIconFile: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def PathParseIconLocationW(pszIconFile: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def PathQuoteSpacesA(lpsz: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathQuoteSpacesW(lpsz: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathRelativePathToA(pszPath: Windows.Win32.Foundation.PSTR, pszFrom: Windows.Win32.Foundation.PSTR, dwAttrFrom: UInt32, pszTo: Windows.Win32.Foundation.PSTR, dwAttrTo: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathRelativePathToW(pszPath: Windows.Win32.Foundation.PWSTR, pszFrom: Windows.Win32.Foundation.PWSTR, dwAttrFrom: UInt32, pszTo: Windows.Win32.Foundation.PWSTR, dwAttrTo: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveArgsA(pszPath: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveArgsW(pszPath: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveBackslashA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveBackslashW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveBlanksA(pszPath: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveBlanksW(pszPath: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveExtensionA(pszPath: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveExtensionW(pszPath: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveFileSpecA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveFileSpecW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathRenameExtensionA(pszPath: Windows.Win32.Foundation.PSTR, pszExt: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathRenameExtensionW(pszPath: Windows.Win32.Foundation.PWSTR, pszExt: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathSearchAndQualifyA(pszPath: Windows.Win32.Foundation.PSTR, pszBuf: Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathSearchAndQualifyW(pszPath: Windows.Win32.Foundation.PWSTR, pszBuf: Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathSetDlgItemPathA(hDlg: Windows.Win32.Foundation.HWND, id: Int32, pszPath: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathSetDlgItemPathW(hDlg: Windows.Win32.Foundation.HWND, id: Int32, pszPath: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathSkipRootA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathSkipRootW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def PathStripPathA(pszPath: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathStripPathW(pszPath: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathStripToRootA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathStripToRootW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathUnquoteSpacesA(lpsz: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathUnquoteSpacesW(lpsz: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMakeSystemFolderA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMakeSystemFolderW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathUnmakeSystemFolderA(pszPath: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathUnmakeSystemFolderW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsSystemFolderA(pszPath: Windows.Win32.Foundation.PSTR, dwAttrb: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsSystemFolderW(pszPath: Windows.Win32.Foundation.PWSTR, dwAttrb: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathUndecorateA(pszPath: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathUndecorateW(pszPath: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathUnExpandEnvStringsA(pszPath: Windows.Win32.Foundation.PSTR, pszBuf: Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathUnExpandEnvStringsW(pszPath: Windows.Win32.Foundation.PWSTR, pszBuf: Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlCompareA(psz1: Windows.Win32.Foundation.PSTR, psz2: Windows.Win32.Foundation.PSTR, fIgnoreSlash: Windows.Win32.Foundation.BOOL) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def UrlCompareW(psz1: Windows.Win32.Foundation.PWSTR, psz2: Windows.Win32.Foundation.PWSTR, fIgnoreSlash: Windows.Win32.Foundation.BOOL) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def UrlCombineA(pszBase: Windows.Win32.Foundation.PSTR, pszRelative: Windows.Win32.Foundation.PSTR, pszCombined: Windows.Win32.Foundation.PSTR, pcchCombined: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlCombineW(pszBase: Windows.Win32.Foundation.PWSTR, pszRelative: Windows.Win32.Foundation.PWSTR, pszCombined: Windows.Win32.Foundation.PWSTR, pcchCombined: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlCanonicalizeA(pszUrl: Windows.Win32.Foundation.PSTR, pszCanonicalized: Windows.Win32.Foundation.PSTR, pcchCanonicalized: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlCanonicalizeW(pszUrl: Windows.Win32.Foundation.PWSTR, pszCanonicalized: Windows.Win32.Foundation.PWSTR, pcchCanonicalized: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlIsOpaqueA(pszURL: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlIsOpaqueW(pszURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlIsNoHistoryA(pszURL: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlIsNoHistoryW(pszURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlIsA(pszUrl: Windows.Win32.Foundation.PSTR, UrlIs: Windows.Win32.UI.Shell.URLIS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlIsW(pszUrl: Windows.Win32.Foundation.PWSTR, UrlIs: Windows.Win32.UI.Shell.URLIS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlGetLocationA(pszURL: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def UrlGetLocationW(pszURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def UrlUnescapeA(pszUrl: Windows.Win32.Foundation.PSTR, pszUnescaped: Windows.Win32.Foundation.PSTR, pcchUnescaped: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlUnescapeW(pszUrl: Windows.Win32.Foundation.PWSTR, pszUnescaped: Windows.Win32.Foundation.PWSTR, pcchUnescaped: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlEscapeA(pszUrl: Windows.Win32.Foundation.PSTR, pszEscaped: Windows.Win32.Foundation.PSTR, pcchEscaped: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlEscapeW(pszUrl: Windows.Win32.Foundation.PWSTR, pszEscaped: Windows.Win32.Foundation.PWSTR, pcchEscaped: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlCreateFromPathA(pszPath: Windows.Win32.Foundation.PSTR, pszUrl: Windows.Win32.Foundation.PSTR, pcchUrl: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlCreateFromPathW(pszPath: Windows.Win32.Foundation.PWSTR, pszUrl: Windows.Win32.Foundation.PWSTR, pcchUrl: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def PathCreateFromUrlA(pszUrl: Windows.Win32.Foundation.PSTR, pszPath: Windows.Win32.Foundation.PSTR, pcchPath: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def PathCreateFromUrlW(pszUrl: Windows.Win32.Foundation.PWSTR, pszPath: Windows.Win32.Foundation.PWSTR, pcchPath: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def PathCreateFromUrlAlloc(pszIn: Windows.Win32.Foundation.PWSTR, ppszOut: POINTER(Windows.Win32.Foundation.PWSTR), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlHashA(pszUrl: Windows.Win32.Foundation.PSTR, pbHash: c_char_p_no, cbHash: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlHashW(pszUrl: Windows.Win32.Foundation.PWSTR, pbHash: c_char_p_no, cbHash: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlGetPartW(pszIn: Windows.Win32.Foundation.PWSTR, pszOut: Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32), dwPart: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlGetPartA(pszIn: Windows.Win32.Foundation.PSTR, pszOut: Windows.Win32.Foundation.PSTR, pcchOut: POINTER(UInt32), dwPart: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlApplySchemeA(pszIn: Windows.Win32.Foundation.PSTR, pszOut: Windows.Win32.Foundation.PSTR, pcchOut: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlApplySchemeW(pszIn: Windows.Win32.Foundation.PWSTR, pszOut: Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def HashData(pbData: c_char_p_no, cbData: UInt32, pbHash: c_char_p_no, cbHash: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlFixupW(pcszUrl: Windows.Win32.Foundation.PWSTR, pszTranslatedUrl: Windows.Win32.Foundation.PWSTR, cchMax: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def ParseURLA(pcszURL: Windows.Win32.Foundation.PSTR, ppu: POINTER(Windows.Win32.UI.Shell.PARSEDURLA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def ParseURLW(pcszURL: Windows.Win32.Foundation.PWSTR, ppu: POINTER(Windows.Win32.UI.Shell.PARSEDURLW_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteEmptyKeyA(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteEmptyKeyW(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteKeyA(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteKeyW(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegDuplicateHKey(hkey: Windows.Win32.System.Registry.HKEY) -> Windows.Win32.System.Registry.HKEY: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteValueA(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PSTR, pszValue: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteValueW(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHGetValueA(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PSTR, pszValue: Windows.Win32.Foundation.PSTR, pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHGetValueW(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR, pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHSetValueA(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PSTR, pszValue: Windows.Win32.Foundation.PSTR, dwType: UInt32, pvData: c_void_p, cbData: UInt32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHSetValueW(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR, dwType: UInt32, pvData: c_void_p, cbData: UInt32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetValueA(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PSTR, pszValue: Windows.Win32.Foundation.PSTR, srrfFlags: Int32, pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetValueW(hkey: Windows.Win32.System.Registry.HKEY, pszSubKey: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR, srrfFlags: Int32, pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetValueFromHKCUHKLM(pwszKey: Windows.Win32.Foundation.PWSTR, pwszValue: Windows.Win32.Foundation.PWSTR, srrfFlags: Int32, pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHQueryValueExA(hkey: Windows.Win32.System.Registry.HKEY, pszValue: Windows.Win32.Foundation.PSTR, pdwReserved: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHQueryValueExW(hkey: Windows.Win32.System.Registry.HKEY, pszValue: Windows.Win32.Foundation.PWSTR, pdwReserved: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHEnumKeyExA(hkey: Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszName: Windows.Win32.Foundation.PSTR, pcchName: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHEnumKeyExW(hkey: Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHEnumValueA(hkey: Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszValueName: Windows.Win32.Foundation.PSTR, pcchValueName: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHEnumValueW(hkey: Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszValueName: Windows.Win32.Foundation.PWSTR, pcchValueName: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHQueryInfoKeyA(hkey: Windows.Win32.System.Registry.HKEY, pcSubKeys: POINTER(UInt32), pcchMaxSubKeyLen: POINTER(UInt32), pcValues: POINTER(UInt32), pcchMaxValueNameLen: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHQueryInfoKeyW(hkey: Windows.Win32.System.Registry.HKEY, pcSubKeys: POINTER(UInt32), pcchMaxSubKeyLen: POINTER(UInt32), pcValues: POINTER(UInt32), pcchMaxValueNameLen: POINTER(UInt32)) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHCopyKeyA(hkeySrc: Windows.Win32.System.Registry.HKEY, pszSrcSubKey: Windows.Win32.Foundation.PSTR, hkeyDest: Windows.Win32.System.Registry.HKEY, fReserved: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHCopyKeyW(hkeySrc: Windows.Win32.System.Registry.HKEY, pszSrcSubKey: Windows.Win32.Foundation.PWSTR, hkeyDest: Windows.Win32.System.Registry.HKEY, fReserved: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetPathA(hKey: Windows.Win32.System.Registry.HKEY, pcszSubKey: Windows.Win32.Foundation.PSTR, pcszValue: Windows.Win32.Foundation.PSTR, pszPath: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetPathW(hKey: Windows.Win32.System.Registry.HKEY, pcszSubKey: Windows.Win32.Foundation.PWSTR, pcszValue: Windows.Win32.Foundation.PWSTR, pszPath: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegSetPathA(hKey: Windows.Win32.System.Registry.HKEY, pcszSubKey: Windows.Win32.Foundation.PSTR, pcszValue: Windows.Win32.Foundation.PSTR, pcszPath: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegSetPathW(hKey: Windows.Win32.System.Registry.HKEY, pcszSubKey: Windows.Win32.Foundation.PWSTR, pcszValue: Windows.Win32.Foundation.PWSTR, pcszPath: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegCreateUSKeyA(pszPath: Windows.Win32.Foundation.PSTR, samDesired: UInt32, hRelativeUSKey: IntPtr, phNewUSKey: POINTER(IntPtr), dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegCreateUSKeyW(pwzPath: Windows.Win32.Foundation.PWSTR, samDesired: UInt32, hRelativeUSKey: IntPtr, phNewUSKey: POINTER(IntPtr), dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegOpenUSKeyA(pszPath: Windows.Win32.Foundation.PSTR, samDesired: UInt32, hRelativeUSKey: IntPtr, phNewUSKey: POINTER(IntPtr), fIgnoreHKCU: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegOpenUSKeyW(pwzPath: Windows.Win32.Foundation.PWSTR, samDesired: UInt32, hRelativeUSKey: IntPtr, phNewUSKey: POINTER(IntPtr), fIgnoreHKCU: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegQueryUSValueA(hUSKey: IntPtr, pszValue: Windows.Win32.Foundation.PSTR, pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32), fIgnoreHKCU: Windows.Win32.Foundation.BOOL, pvDefaultData: c_void_p, dwDefaultDataSize: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegQueryUSValueW(hUSKey: IntPtr, pszValue: Windows.Win32.Foundation.PWSTR, pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32), fIgnoreHKCU: Windows.Win32.Foundation.BOOL, pvDefaultData: c_void_p, dwDefaultDataSize: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegWriteUSValueA(hUSKey: IntPtr, pszValue: Windows.Win32.Foundation.PSTR, dwType: UInt32, pvData: c_void_p, cbData: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegWriteUSValueW(hUSKey: IntPtr, pwzValue: Windows.Win32.Foundation.PWSTR, dwType: UInt32, pvData: c_void_p, cbData: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegDeleteUSValueA(hUSKey: IntPtr, pszValue: Windows.Win32.Foundation.PSTR, delRegFlags: Windows.Win32.UI.Shell.SHREGDEL_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegDeleteUSValueW(hUSKey: IntPtr, pwzValue: Windows.Win32.Foundation.PWSTR, delRegFlags: Windows.Win32.UI.Shell.SHREGDEL_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegDeleteEmptyUSKeyW(hUSKey: IntPtr, pwzSubKey: Windows.Win32.Foundation.PWSTR, delRegFlags: Windows.Win32.UI.Shell.SHREGDEL_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegDeleteEmptyUSKeyA(hUSKey: IntPtr, pszSubKey: Windows.Win32.Foundation.PSTR, delRegFlags: Windows.Win32.UI.Shell.SHREGDEL_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegEnumUSKeyA(hUSKey: IntPtr, dwIndex: UInt32, pszName: Windows.Win32.Foundation.PSTR, pcchName: POINTER(UInt32), enumRegFlags: Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegEnumUSKeyW(hUSKey: IntPtr, dwIndex: UInt32, pwzName: Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt32), enumRegFlags: Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegEnumUSValueA(hUSkey: IntPtr, dwIndex: UInt32, pszValueName: Windows.Win32.Foundation.PSTR, pcchValueName: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32), enumRegFlags: Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegEnumUSValueW(hUSkey: IntPtr, dwIndex: UInt32, pszValueName: Windows.Win32.Foundation.PWSTR, pcchValueName: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32), enumRegFlags: Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegQueryInfoUSKeyA(hUSKey: IntPtr, pcSubKeys: POINTER(UInt32), pcchMaxSubKeyLen: POINTER(UInt32), pcValues: POINTER(UInt32), pcchMaxValueNameLen: POINTER(UInt32), enumRegFlags: Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegQueryInfoUSKeyW(hUSKey: IntPtr, pcSubKeys: POINTER(UInt32), pcchMaxSubKeyLen: POINTER(UInt32), pcValues: POINTER(UInt32), pcchMaxValueNameLen: POINTER(UInt32), enumRegFlags: Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegCloseUSKey(hUSKey: IntPtr) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetUSValueA(pszSubKey: Windows.Win32.Foundation.PSTR, pszValue: Windows.Win32.Foundation.PSTR, pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32), fIgnoreHKCU: Windows.Win32.Foundation.BOOL, pvDefaultData: c_void_p, dwDefaultDataSize: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetUSValueW(pszSubKey: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR, pdwType: POINTER(UInt32), pvData: c_void_p, pcbData: POINTER(UInt32), fIgnoreHKCU: Windows.Win32.Foundation.BOOL, pvDefaultData: c_void_p, dwDefaultDataSize: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegSetUSValueA(pszSubKey: Windows.Win32.Foundation.PSTR, pszValue: Windows.Win32.Foundation.PSTR, dwType: UInt32, pvData: c_void_p, cbData: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegSetUSValueW(pwzSubKey: Windows.Win32.Foundation.PWSTR, pwzValue: Windows.Win32.Foundation.PWSTR, dwType: UInt32, pvData: c_void_p, cbData: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetIntW(hk: Windows.Win32.System.Registry.HKEY, pwzKey: Windows.Win32.Foundation.PWSTR, iDefault: Int32) -> Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetBoolUSValueA(pszSubKey: Windows.Win32.Foundation.PSTR, pszValue: Windows.Win32.Foundation.PSTR, fIgnoreHKCU: Windows.Win32.Foundation.BOOL, fDefault: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetBoolUSValueW(pszSubKey: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR, fIgnoreHKCU: Windows.Win32.Foundation.BOOL, fDefault: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def AssocCreate(clsid: Guid, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryStringA(flags: Windows.Win32.UI.Shell.ASSOCF, str: Windows.Win32.UI.Shell.ASSOCSTR, pszAssoc: Windows.Win32.Foundation.PSTR, pszExtra: Windows.Win32.Foundation.PSTR, pszOut: Windows.Win32.Foundation.PSTR, pcchOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryStringW(flags: Windows.Win32.UI.Shell.ASSOCF, str: Windows.Win32.UI.Shell.ASSOCSTR, pszAssoc: Windows.Win32.Foundation.PWSTR, pszExtra: Windows.Win32.Foundation.PWSTR, pszOut: Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryStringByKeyA(flags: Windows.Win32.UI.Shell.ASSOCF, str: Windows.Win32.UI.Shell.ASSOCSTR, hkAssoc: Windows.Win32.System.Registry.HKEY, pszExtra: Windows.Win32.Foundation.PSTR, pszOut: Windows.Win32.Foundation.PSTR, pcchOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryStringByKeyW(flags: Windows.Win32.UI.Shell.ASSOCF, str: Windows.Win32.UI.Shell.ASSOCSTR, hkAssoc: Windows.Win32.System.Registry.HKEY, pszExtra: Windows.Win32.Foundation.PWSTR, pszOut: Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryKeyA(flags: Windows.Win32.UI.Shell.ASSOCF, key: Windows.Win32.UI.Shell.ASSOCKEY, pszAssoc: Windows.Win32.Foundation.PSTR, pszExtra: Windows.Win32.Foundation.PSTR, phkeyOut: POINTER(Windows.Win32.System.Registry.HKEY)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryKeyW(flags: Windows.Win32.UI.Shell.ASSOCF, key: Windows.Win32.UI.Shell.ASSOCKEY, pszAssoc: Windows.Win32.Foundation.PWSTR, pszExtra: Windows.Win32.Foundation.PWSTR, phkeyOut: POINTER(Windows.Win32.System.Registry.HKEY)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocIsDangerous(pszAssoc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def AssocGetPerceivedType(pszExt: Windows.Win32.Foundation.PWSTR, ptype: POINTER(Windows.Win32.UI.Shell.Common.PERCEIVED), pflag: POINTER(UInt32), ppszType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHOpenRegStreamA(hkey: Windows.Win32.System.Registry.HKEY, pszSubkey: Windows.Win32.Foundation.PSTR, pszValue: Windows.Win32.Foundation.PSTR, grfMode: UInt32) -> Windows.Win32.System.Com.IStream_head: ...
@winfunctype('SHLWAPI.dll')
def SHOpenRegStreamW(hkey: Windows.Win32.System.Registry.HKEY, pszSubkey: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR, grfMode: UInt32) -> Windows.Win32.System.Com.IStream_head: ...
@winfunctype('SHLWAPI.dll')
def SHOpenRegStream2A(hkey: Windows.Win32.System.Registry.HKEY, pszSubkey: Windows.Win32.Foundation.PSTR, pszValue: Windows.Win32.Foundation.PSTR, grfMode: UInt32) -> Windows.Win32.System.Com.IStream_head: ...
@winfunctype('SHLWAPI.dll')
def SHOpenRegStream2W(hkey: Windows.Win32.System.Registry.HKEY, pszSubkey: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR, grfMode: UInt32) -> Windows.Win32.System.Com.IStream_head: ...
@winfunctype('SHLWAPI.dll')
def SHCreateStreamOnFileA(pszFile: Windows.Win32.Foundation.PSTR, grfMode: UInt32, ppstm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHCreateStreamOnFileW(pszFile: Windows.Win32.Foundation.PWSTR, grfMode: UInt32, ppstm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHCreateStreamOnFileEx(pszFile: Windows.Win32.Foundation.PWSTR, grfMode: UInt32, dwAttributes: UInt32, fCreate: Windows.Win32.Foundation.BOOL, pstmTemplate: Windows.Win32.System.Com.IStream_head, ppstm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHCreateMemStream(pInit: c_char_p_no, cbInit: UInt32) -> Windows.Win32.System.Com.IStream_head: ...
@winfunctype('SHLWAPI.dll')
def GetAcceptLanguagesA(pszLanguages: Windows.Win32.Foundation.PSTR, pcchLanguages: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def GetAcceptLanguagesW(pszLanguages: Windows.Win32.Foundation.PWSTR, pcchLanguages: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_Set(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head), punk: Windows.Win32.System.Com.IUnknown_head) -> Void: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_AtomicRelease(ppunk: POINTER(c_void_p)) -> Void: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_GetWindow(punk: Windows.Win32.System.Com.IUnknown_head, phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_SetSite(punk: Windows.Win32.System.Com.IUnknown_head, punkSite: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_GetSite(punk: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_QueryService(punk: Windows.Win32.System.Com.IUnknown_head, guidService: POINTER(Guid), riid: POINTER(Guid), ppvOut: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Read(pstm: Windows.Win32.System.Com.IStream_head, pv: c_void_p, cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Write(pstm: Windows.Win32.System.Com.IStream_head, pv: c_void_p, cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Reset(pstm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Size(pstm: Windows.Win32.System.Com.IStream_head, pui: POINTER(Windows.Win32.Foundation.ULARGE_INTEGER_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def ConnectToConnectionPoint(punk: Windows.Win32.System.Com.IUnknown_head, riidEvent: POINTER(Guid), fConnect: Windows.Win32.Foundation.BOOL, punkTarget: Windows.Win32.System.Com.IUnknown_head, pdwCookie: POINTER(UInt32), ppcpOut: POINTER(Windows.Win32.System.Com.IConnectionPoint_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_ReadPidl(pstm: Windows.Win32.System.Com.IStream_head, ppidlOut: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_WritePidl(pstm: Windows.Win32.System.Com.IStream_head, pidlWrite: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_ReadStr(pstm: Windows.Win32.System.Com.IStream_head, ppsz: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_WriteStr(pstm: Windows.Win32.System.Com.IStream_head, psz: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Copy(pstmFrom: Windows.Win32.System.Com.IStream_head, pstmTo: Windows.Win32.System.Com.IStream_head, cb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHGetViewStatePropertyBag(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pszBagName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHFormatDateTimeA(pft: POINTER(Windows.Win32.Foundation.FILETIME_head), pdwFlags: POINTER(UInt32), pszBuf: Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHFormatDateTimeW(pft: POINTER(Windows.Win32.Foundation.FILETIME_head), pdwFlags: POINTER(UInt32), pszBuf: Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHAnsiToUnicode(pszSrc: Windows.Win32.Foundation.PSTR, pwszDst: Windows.Win32.Foundation.PWSTR, cwchBuf: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHAnsiToAnsi(pszSrc: Windows.Win32.Foundation.PSTR, pszDst: Windows.Win32.Foundation.PSTR, cchBuf: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHUnicodeToAnsi(pwszSrc: Windows.Win32.Foundation.PWSTR, pszDst: Windows.Win32.Foundation.PSTR, cchBuf: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHUnicodeToUnicode(pwzSrc: Windows.Win32.Foundation.PWSTR, pwzDst: Windows.Win32.Foundation.PWSTR, cwchBuf: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHMessageBoxCheckA(hwnd: Windows.Win32.Foundation.HWND, pszText: Windows.Win32.Foundation.PSTR, pszCaption: Windows.Win32.Foundation.PSTR, uType: UInt32, iDefault: Int32, pszRegVal: Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHMessageBoxCheckW(hwnd: Windows.Win32.Foundation.HWND, pszText: Windows.Win32.Foundation.PWSTR, pszCaption: Windows.Win32.Foundation.PWSTR, uType: UInt32, iDefault: Int32, pszRegVal: Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHSendMessageBroadcastA(uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHSendMessageBroadcastW(uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHStripMneumonicA(pszMenu: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.CHAR: ...
@winfunctype('SHLWAPI.dll')
def SHStripMneumonicW(pszMenu: Windows.Win32.Foundation.PWSTR) -> Char: ...
@winfunctype('SHLWAPI.dll')
def IsOS(dwOS: Windows.Win32.UI.Shell.OS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHGlobalCounterGetValue(id: Windows.Win32.UI.Shell.SHGLOBALCOUNTER) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHGlobalCounterIncrement(id: Windows.Win32.UI.Shell.SHGLOBALCOUNTER) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHGlobalCounterDecrement(id: Windows.Win32.UI.Shell.SHGLOBALCOUNTER) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHAllocShared(pvData: c_void_p, dwSize: UInt32, dwProcessId: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('SHLWAPI.dll')
def SHFreeShared(hData: Windows.Win32.Foundation.HANDLE, dwProcessId: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHLockShared(hData: Windows.Win32.Foundation.HANDLE, dwProcessId: UInt32) -> c_void_p: ...
@winfunctype('SHLWAPI.dll')
def SHUnlockShared(pvData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def WhichPlatform() -> UInt32: ...
@winfunctype('SHLWAPI.dll')
def QISearch(that: c_void_p, pqit: POINTER(Windows.Win32.UI.Shell.QITAB_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHIsLowMemoryMachine(dwType: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def GetMenuPosFromID(hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, id: UInt32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHGetInverseCMAP(pbMap: c_char_p_no, cbMap: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHAutoComplete(hwndEdit: Windows.Win32.Foundation.HWND, dwFlags: Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHCreateThreadRef(pcRef: POINTER(Int32), ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHSetThreadRef(punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHGetThreadRef(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHSkipJunction(pbc: Windows.Win32.System.Com.IBindCtx_head, pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHCreateThread(pfnThreadProc: Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pData: c_void_p, flags: UInt32, pfnCallback: Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHCreateThreadWithHandle(pfnThreadProc: Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pData: c_void_p, flags: UInt32, pfnCallback: Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHReleaseThreadRef() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHCreateShellPalette(hdc: Windows.Win32.Graphics.Gdi.HDC) -> Windows.Win32.Graphics.Gdi.HPALETTE: ...
@winfunctype('SHLWAPI.dll')
def ColorRGBToHLS(clrRGB: Windows.Win32.Foundation.COLORREF, pwHue: POINTER(UInt16), pwLuminance: POINTER(UInt16), pwSaturation: POINTER(UInt16)) -> Void: ...
@winfunctype('SHLWAPI.dll')
def ColorHLSToRGB(wHue: UInt16, wLuminance: UInt16, wSaturation: UInt16) -> Windows.Win32.Foundation.COLORREF: ...
@winfunctype('SHLWAPI.dll')
def ColorAdjustLuma(clrRGB: Windows.Win32.Foundation.COLORREF, n: Int32, fScale: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.COLORREF: ...
@winfunctype('SHLWAPI.dll')
def IsInternetESCEnabled() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('hlink.dll')
def HlinkCreateFromMoniker(pimkTrgt: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR, pihlsite: Windows.Win32.UI.Shell.IHlinkSite_head, dwSiteData: UInt32, piunkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateFromString(pwzTarget: Windows.Win32.Foundation.PWSTR, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR, pihlsite: Windows.Win32.UI.Shell.IHlinkSite_head, dwSiteData: UInt32, piunkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateFromData(piDataObj: Windows.Win32.System.Com.IDataObject_head, pihlsite: Windows.Win32.UI.Shell.IHlinkSite_head, dwSiteData: UInt32, piunkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkQueryCreateFromData(piDataObj: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkClone(pihl: Windows.Win32.UI.Shell.IHlink_head, riid: POINTER(Guid), pihlsiteForClone: Windows.Win32.UI.Shell.IHlinkSite_head, dwSiteData: UInt32, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateBrowseContext(piunkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkNavigateToStringReference(pwzTarget: Windows.Win32.Foundation.PWSTR, pwzLocation: Windows.Win32.Foundation.PWSTR, pihlsite: Windows.Win32.UI.Shell.IHlinkSite_head, dwSiteData: UInt32, pihlframe: Windows.Win32.UI.Shell.IHlinkFrame_head, grfHLNF: UInt32, pibc: Windows.Win32.System.Com.IBindCtx_head, pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pihlbc: Windows.Win32.UI.Shell.IHlinkBrowseContext_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkNavigate(pihl: Windows.Win32.UI.Shell.IHlink_head, pihlframe: Windows.Win32.UI.Shell.IHlinkFrame_head, grfHLNF: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head, pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pihlbc: Windows.Win32.UI.Shell.IHlinkBrowseContext_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkOnNavigate(pihlframe: Windows.Win32.UI.Shell.IHlinkFrame_head, pihlbc: Windows.Win32.UI.Shell.IHlinkBrowseContext_head, grfHLNF: UInt32, pimkTarget: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR, puHLID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkUpdateStackItem(pihlframe: Windows.Win32.UI.Shell.IHlinkFrame_head, pihlbc: Windows.Win32.UI.Shell.IHlinkBrowseContext_head, uHLID: UInt32, pimkTrgt: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkOnRenameDocument(dwReserved: UInt32, pihlbc: Windows.Win32.UI.Shell.IHlinkBrowseContext_head, pimkOld: Windows.Win32.System.Com.IMoniker_head, pimkNew: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveMonikerForData(pimkReference: Windows.Win32.System.Com.IMoniker_head, reserved: UInt32, pibc: Windows.Win32.System.Com.IBindCtx_head, cFmtetc: UInt32, rgFmtetc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pimkBase: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveStringForData(pwzReference: Windows.Win32.Foundation.PWSTR, reserved: UInt32, pibc: Windows.Win32.System.Com.IBindCtx_head, cFmtetc: UInt32, rgFmtetc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pimkBase: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkParseDisplayName(pibc: Windows.Win32.System.Com.IBindCtx_head, pwzDisplayName: Windows.Win32.Foundation.PWSTR, fNoForceAbs: Windows.Win32.Foundation.BOOL, pcchEaten: POINTER(UInt32), ppimk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateExtensionServices(pwzAdditionalHeaders: Windows.Win32.Foundation.PWSTR, phwnd: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PWSTR, pszPassword: Windows.Win32.Foundation.PWSTR, piunkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkPreprocessMoniker(pibc: Windows.Win32.System.Com.IBindCtx_head, pimkIn: Windows.Win32.System.Com.IMoniker_head, ppimkOut: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def OleSaveToStreamEx(piunk: Windows.Win32.System.Com.IUnknown_head, pistm: Windows.Win32.System.Com.IStream_head, fClearDirty: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkSetSpecialReference(uReference: UInt32, pwzReference: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkGetSpecialReference(uReference: UInt32, ppwzReference: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateShortcut(grfHLSHORTCUTF: UInt32, pihl: Windows.Win32.UI.Shell.IHlink_head, pwzDir: Windows.Win32.Foundation.PWSTR, pwzFileName: Windows.Win32.Foundation.PWSTR, ppwzShortcutFile: POINTER(Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateShortcutFromMoniker(grfHLSHORTCUTF: UInt32, pimkTarget: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzDir: Windows.Win32.Foundation.PWSTR, pwzFileName: Windows.Win32.Foundation.PWSTR, ppwzShortcutFile: POINTER(Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateShortcutFromString(grfHLSHORTCUTF: UInt32, pwzTarget: Windows.Win32.Foundation.PWSTR, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzDir: Windows.Win32.Foundation.PWSTR, pwzFileName: Windows.Win32.Foundation.PWSTR, ppwzShortcutFile: POINTER(Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveShortcut(pwzShortcutFileName: Windows.Win32.Foundation.PWSTR, pihlsite: Windows.Win32.UI.Shell.IHlinkSite_head, dwSiteData: UInt32, piunkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveShortcutToMoniker(pwzShortcutFileName: Windows.Win32.Foundation.PWSTR, ppimkTarget: POINTER(Windows.Win32.System.Com.IMoniker_head), ppwzLocation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveShortcutToString(pwzShortcutFileName: Windows.Win32.Foundation.PWSTR, ppwzTarget: POINTER(Windows.Win32.Foundation.PWSTR), ppwzLocation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkIsShortcut(pwzFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkGetValueFromParams(pwzParams: Windows.Win32.Foundation.PWSTR, pwzName: Windows.Win32.Foundation.PWSTR, ppwzValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkTranslateURL(pwzURL: Windows.Win32.Foundation.PWSTR, grfFlags: UInt32, ppwzTranslatedURL: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathIsUNCEx(pszPath: Windows.Win32.Foundation.PWSTR, ppszServer: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchIsRoot(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAddBackslashEx(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, ppszEnd: POINTER(Windows.Win32.Foundation.PWSTR), pcchRemaining: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAddBackslash(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRemoveBackslashEx(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, ppszEnd: POINTER(Windows.Win32.Foundation.PWSTR), pcchRemaining: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRemoveBackslash(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchSkipRoot(pszPath: Windows.Win32.Foundation.PWSTR, ppszRootEnd: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchStripToRoot(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRemoveFileSpec(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchFindExtension(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, ppszExt: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAddExtension(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, pszExt: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRenameExtension(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, pszExt: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRemoveExtension(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchCanonicalizeEx(pszPathOut: Windows.Win32.Foundation.PWSTR, cchPathOut: UIntPtr, pszPathIn: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.UI.Shell.PATHCCH_OPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchCanonicalize(pszPathOut: Windows.Win32.Foundation.PWSTR, cchPathOut: UIntPtr, pszPathIn: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchCombineEx(pszPathOut: Windows.Win32.Foundation.PWSTR, cchPathOut: UIntPtr, pszPathIn: Windows.Win32.Foundation.PWSTR, pszMore: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.UI.Shell.PATHCCH_OPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchCombine(pszPathOut: Windows.Win32.Foundation.PWSTR, cchPathOut: UIntPtr, pszPathIn: Windows.Win32.Foundation.PWSTR, pszMore: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAppendEx(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, pszMore: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.UI.Shell.PATHCCH_OPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAppend(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, pszMore: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchStripPrefix(pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathAllocCombine(pszPathIn: Windows.Win32.Foundation.PWSTR, pszMore: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.UI.Shell.PATHCCH_OPTIONS, ppszPathOut: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathAllocCanonicalize(pszPathIn: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.UI.Shell.PATHCCH_OPTIONS, ppszPathOut: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-psm-appnotify-l1-1-0.dll')
def RegisterAppStateChangeNotification(Routine: Windows.Win32.UI.Shell.PAPPSTATE_CHANGE_ROUTINE, Context: c_void_p, Registration: POINTER(POINTER(Windows.Win32.UI.Shell._APPSTATE_REGISTRATION_head))) -> UInt32: ...
@winfunctype('api-ms-win-core-psm-appnotify-l1-1-0.dll')
def UnregisterAppStateChangeNotification(Registration: POINTER(Windows.Win32.UI.Shell._APPSTATE_REGISTRATION_head)) -> Void: ...
@winfunctype('api-ms-win-core-psm-appnotify-l1-1-1.dll')
def RegisterAppConstrainedChangeNotification(Routine: Windows.Win32.UI.Shell.PAPPCONSTRAIN_CHANGE_ROUTINE, Context: c_void_p, Registration: POINTER(POINTER(Windows.Win32.UI.Shell._APPCONSTRAIN_REGISTRATION_head))) -> UInt32: ...
@winfunctype('api-ms-win-core-psm-appnotify-l1-1-1.dll')
def UnregisterAppConstrainedChangeNotification(Registration: POINTER(Windows.Win32.UI.Shell._APPCONSTRAIN_REGISTRATION_head)) -> Void: ...
AppShellVerbHandler = Guid('4ed3a719-cea8-4bd9-91-0d-e2-52-f9-97-af-c2')
AppStartupLink = Guid('273eb5e7-88b0-4843-bf-ef-e2-c8-1d-43-aa-e5')
AppVisibility = Guid('7e5fe3d9-985f-4908-91-f9-ee-19-f9-fd-15-14')
ApplicationActivationManager = Guid('45ba127d-10a8-46ea-8a-b7-56-ea-90-78-94-3c')
ApplicationAssociationRegistration = Guid('591209c7-767b-42b2-9f-ba-44-ee-46-15-f2-c7')
ApplicationAssociationRegistrationUI = Guid('1968106d-f3b5-44cf-89-0e-11-6f-cb-9e-ce-f1')
ApplicationDesignModeSettings = Guid('958a6fb5-dcb2-4faf-aa-fd-7f-b0-54-ad-1a-3b')
ApplicationDestinations = Guid('86c14003-4d6b-4ef3-a7-b4-05-06-66-3b-2e-68')
ApplicationDocumentLists = Guid('86bec222-30f2-47e0-9f-25-60-d1-1c-d7-5c-28')
AttachmentServices = Guid('4125dd96-e03a-4103-8f-70-e0-59-7d-80-3b-9c')
class BANDINFOSFB(Structure):
    dwMask: UInt32
    dwStateMask: UInt32
    dwState: UInt32
    crBkgnd: Windows.Win32.Foundation.COLORREF
    crBtnLt: Windows.Win32.Foundation.COLORREF
    crBtnDk: Windows.Win32.Foundation.COLORREF
    wViewMode: UInt16
    wAlign: UInt16
    psf: Windows.Win32.UI.Shell.IShellFolder_head
    pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
BANDSITECID = Int32
BSID_BANDADDED: BANDSITECID = 0
BSID_BANDREMOVED: BANDSITECID = 1
class BANDSITEINFO(Structure):
    dwMask: UInt32
    dwState: UInt32
    dwStyle: UInt32
class BANNER_NOTIFICATION(Structure):
    event: Windows.Win32.UI.Shell.BANNER_NOTIFICATION_EVENT
    providerIdentity: Windows.Win32.Foundation.PWSTR
    contentId: Windows.Win32.Foundation.PWSTR
BANNER_NOTIFICATION_EVENT = Int32
BNE_Rendered: BANNER_NOTIFICATION_EVENT = 0
BNE_Hovered: BANNER_NOTIFICATION_EVENT = 1
BNE_Closed: BANNER_NOTIFICATION_EVENT = 2
BNE_Dismissed: BANNER_NOTIFICATION_EVENT = 3
BNE_Button1Clicked: BANNER_NOTIFICATION_EVENT = 4
BNE_Button2Clicked: BANNER_NOTIFICATION_EVENT = 5
class BASEBROWSERDATALH(Structure):
    _hwnd: Windows.Win32.Foundation.HWND
    _ptl: Windows.Win32.UI.Shell.ITravelLog_head
    _phlf: Windows.Win32.UI.Shell.IHlinkFrame_head
    _pautoWB2: Windows.Win32.UI.Shell.IWebBrowser2_head
    _pautoEDS: Windows.Win32.UI.Shell.IExpDispSupport_head
    _pautoSS: Windows.Win32.UI.Shell.IShellService_head
    _eSecureLockIcon: Int32
    _bitfield: UInt32
    _uActivateState: UInt32
    _pidlViewState: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    _pctView: Windows.Win32.System.Ole.IOleCommandTarget_head
    _pidlCur: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    _psv: Windows.Win32.UI.Shell.IShellView_head
    _psf: Windows.Win32.UI.Shell.IShellFolder_head
    _hwndView: Windows.Win32.Foundation.HWND
    _pszTitleCur: Windows.Win32.Foundation.PWSTR
    _pidlPending: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    _psvPending: Windows.Win32.UI.Shell.IShellView_head
    _psfPending: Windows.Win32.UI.Shell.IShellFolder_head
    _hwndViewPending: Windows.Win32.Foundation.HWND
    _pszTitlePending: Windows.Win32.Foundation.PWSTR
    _fIsViewMSHTML: Windows.Win32.Foundation.BOOL
    _fPrivacyImpacted: Windows.Win32.Foundation.BOOL
    _clsidView: Guid
    _clsidViewPending: Guid
    _hwndFrame: Windows.Win32.Foundation.HWND
    _lPhishingFilterStatus: Int32
class BASEBROWSERDATAXP(Structure):
    _hwnd: Windows.Win32.Foundation.HWND
    _ptl: Windows.Win32.UI.Shell.ITravelLog_head
    _phlf: Windows.Win32.UI.Shell.IHlinkFrame_head
    _pautoWB2: Windows.Win32.UI.Shell.IWebBrowser2_head
    _pautoEDS: Windows.Win32.UI.Shell.IExpDispSupportXP_head
    _pautoSS: Windows.Win32.UI.Shell.IShellService_head
    _eSecureLockIcon: Int32
    _bitfield: UInt32
    _uActivateState: UInt32
    _pidlViewState: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    _pctView: Windows.Win32.System.Ole.IOleCommandTarget_head
    _pidlCur: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    _psv: Windows.Win32.UI.Shell.IShellView_head
    _psf: Windows.Win32.UI.Shell.IShellFolder_head
    _hwndView: Windows.Win32.Foundation.HWND
    _pszTitleCur: Windows.Win32.Foundation.PWSTR
    _pidlPending: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    _psvPending: Windows.Win32.UI.Shell.IShellView_head
    _psfPending: Windows.Win32.UI.Shell.IShellFolder_head
    _hwndViewPending: Windows.Win32.Foundation.HWND
    _pszTitlePending: Windows.Win32.Foundation.PWSTR
    _fIsViewMSHTML: Windows.Win32.Foundation.BOOL
    _fPrivacyImpacted: Windows.Win32.Foundation.BOOL
    _clsidView: Guid
    _clsidViewPending: Guid
    _hwndFrame: Windows.Win32.Foundation.HWND
@winfunctype_pointer
def BFFCALLBACK(hwnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, lParam: Windows.Win32.Foundation.LPARAM, lpData: Windows.Win32.Foundation.LPARAM) -> Int32: ...
BNSTATE = Int32
BNS_NORMAL: BNSTATE = 0
BNS_BEGIN_NAVIGATE: BNSTATE = 1
BNS_NAVIGATE: BNSTATE = 2
class BROWSEINFOA(Structure):
    hwndOwner: Windows.Win32.Foundation.HWND
    pidlRoot: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    pszDisplayName: Windows.Win32.Foundation.PSTR
    lpszTitle: Windows.Win32.Foundation.PSTR
    ulFlags: UInt32
    lpfn: Windows.Win32.UI.Shell.BFFCALLBACK
    lParam: Windows.Win32.Foundation.LPARAM
    iImage: Int32
class BROWSEINFOW(Structure):
    hwndOwner: Windows.Win32.Foundation.HWND
    pidlRoot: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    pszDisplayName: Windows.Win32.Foundation.PWSTR
    lpszTitle: Windows.Win32.Foundation.PWSTR
    ulFlags: UInt32
    lpfn: Windows.Win32.UI.Shell.BFFCALLBACK
    lParam: Windows.Win32.Foundation.LPARAM
    iImage: Int32
BrowserNavConstants = Int32
BrowserNavConstants_navOpenInNewWindow: BrowserNavConstants = 1
BrowserNavConstants_navNoHistory: BrowserNavConstants = 2
BrowserNavConstants_navNoReadFromCache: BrowserNavConstants = 4
BrowserNavConstants_navNoWriteToCache: BrowserNavConstants = 8
BrowserNavConstants_navAllowAutosearch: BrowserNavConstants = 16
BrowserNavConstants_navBrowserBar: BrowserNavConstants = 32
BrowserNavConstants_navHyperlink: BrowserNavConstants = 64
BrowserNavConstants_navEnforceRestricted: BrowserNavConstants = 128
BrowserNavConstants_navNewWindowsManaged: BrowserNavConstants = 256
BrowserNavConstants_navUntrustedForDownload: BrowserNavConstants = 512
BrowserNavConstants_navTrustedForActiveX: BrowserNavConstants = 1024
BrowserNavConstants_navOpenInNewTab: BrowserNavConstants = 2048
BrowserNavConstants_navOpenInBackgroundTab: BrowserNavConstants = 4096
BrowserNavConstants_navKeepWordWheelText: BrowserNavConstants = 8192
BrowserNavConstants_navVirtualTab: BrowserNavConstants = 16384
BrowserNavConstants_navBlockRedirectsXDomain: BrowserNavConstants = 32768
BrowserNavConstants_navOpenNewForegroundTab: BrowserNavConstants = 65536
BrowserNavConstants_navTravelLogScreenshot: BrowserNavConstants = 131072
BrowserNavConstants_navDeferUnload: BrowserNavConstants = 262144
BrowserNavConstants_navSpeculative: BrowserNavConstants = 524288
BrowserNavConstants_navSuggestNewWindow: BrowserNavConstants = 1048576
BrowserNavConstants_navSuggestNewTab: BrowserNavConstants = 2097152
BrowserNavConstants_navReserved1: BrowserNavConstants = 4194304
BrowserNavConstants_navHomepageNavigate: BrowserNavConstants = 8388608
BrowserNavConstants_navRefresh: BrowserNavConstants = 16777216
BrowserNavConstants_navHostNavigation: BrowserNavConstants = 33554432
BrowserNavConstants_navReserved2: BrowserNavConstants = 67108864
BrowserNavConstants_navReserved3: BrowserNavConstants = 134217728
BrowserNavConstants_navReserved4: BrowserNavConstants = 268435456
BrowserNavConstants_navReserved5: BrowserNavConstants = 536870912
BrowserNavConstants_navReserved6: BrowserNavConstants = 1073741824
BrowserNavConstants_navReserved7: BrowserNavConstants = -2147483648
class CABINETSTATE(Structure):
    cLength: UInt16
    nVersion: UInt16
    _bitfield: Int32
    fMenuEnumFilter: UInt32
    _pack_ = 1
CATEGORYINFO_FLAGS = Int32
CATINFO_NORMAL: CATEGORYINFO_FLAGS = 0
CATINFO_COLLAPSED: CATEGORYINFO_FLAGS = 1
CATINFO_HIDDEN: CATEGORYINFO_FLAGS = 2
CATINFO_EXPANDED: CATEGORYINFO_FLAGS = 4
CATINFO_NOHEADER: CATEGORYINFO_FLAGS = 8
CATINFO_NOTCOLLAPSIBLE: CATEGORYINFO_FLAGS = 16
CATINFO_NOHEADERCOUNT: CATEGORYINFO_FLAGS = 32
CATINFO_SUBSETTED: CATEGORYINFO_FLAGS = 64
CATINFO_SEPARATE_IMAGES: CATEGORYINFO_FLAGS = 128
CATINFO_SHOWEMPTY: CATEGORYINFO_FLAGS = 256
class CATEGORY_INFO(Structure):
    cif: Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS
    wszName: Char * 260
CATSORT_FLAGS = Int32
CATSORT_DEFAULT: CATSORT_FLAGS = 0
CATSORT_NAME: CATSORT_FLAGS = 1
CDBURNINGEXTENSIONRET = Int32
CDBE_RET_DEFAULT: CDBURNINGEXTENSIONRET = 0
CDBE_RET_DONTRUNOTHEREXTS: CDBURNINGEXTENSIONRET = 1
CDBE_RET_STOPWIZARD: CDBURNINGEXTENSIONRET = 2
CDBurn = Guid('fbeb8a05-beee-4442-80-4e-40-9d-6c-45-15-e9')
CDCONTROLSTATEF = Int32
CDCS_INACTIVE: CDCONTROLSTATEF = 0
CDCS_ENABLED: CDCONTROLSTATEF = 1
CDCS_VISIBLE: CDCONTROLSTATEF = 2
CDCS_ENABLEDVISIBLE: CDCONTROLSTATEF = 3
class CIDA(Structure):
    cidl: UInt32
    aoffset: UInt32 * 1
    _pack_ = 1
class CIE4ConnectionPoint(c_void_p):
    extends: Windows.Win32.System.Com.IConnectionPoint
    @commethod(8)
    def DoInvokeIE4(pf: POINTER(Windows.Win32.Foundation.BOOL), ppv: POINTER(c_void_p), dispid: Int32, pdispparams: POINTER(Windows.Win32.System.Com.DISPPARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DoInvokePIDLIE4(dispid: Int32, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), fCanCancel: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class CMINVOKECOMMANDINFO(Structure):
    cbSize: UInt32
    fMask: UInt32
    hwnd: Windows.Win32.Foundation.HWND
    lpVerb: Windows.Win32.Foundation.PSTR
    lpParameters: Windows.Win32.Foundation.PSTR
    lpDirectory: Windows.Win32.Foundation.PSTR
    nShow: Int32
    dwHotKey: UInt32
    hIcon: Windows.Win32.Foundation.HANDLE
class CMINVOKECOMMANDINFOEX(Structure):
    cbSize: UInt32
    fMask: UInt32
    hwnd: Windows.Win32.Foundation.HWND
    lpVerb: Windows.Win32.Foundation.PSTR
    lpParameters: Windows.Win32.Foundation.PSTR
    lpDirectory: Windows.Win32.Foundation.PSTR
    nShow: Int32
    dwHotKey: UInt32
    hIcon: Windows.Win32.Foundation.HANDLE
    lpTitle: Windows.Win32.Foundation.PSTR
    lpVerbW: Windows.Win32.Foundation.PWSTR
    lpParametersW: Windows.Win32.Foundation.PWSTR
    lpDirectoryW: Windows.Win32.Foundation.PWSTR
    lpTitleW: Windows.Win32.Foundation.PWSTR
    ptInvoke: Windows.Win32.Foundation.POINT
class CMINVOKECOMMANDINFOEX_REMOTE(Structure):
    cbSize: UInt32
    fMask: UInt32
    hwnd: Windows.Win32.Foundation.HWND
    lpVerbString: Windows.Win32.Foundation.PSTR
    lpParameters: Windows.Win32.Foundation.PSTR
    lpDirectory: Windows.Win32.Foundation.PSTR
    nShow: Int32
    dwHotKey: UInt32
    lpTitle: Windows.Win32.Foundation.PSTR
    lpVerbWString: Windows.Win32.Foundation.PWSTR
    lpParametersW: Windows.Win32.Foundation.PWSTR
    lpDirectoryW: Windows.Win32.Foundation.PWSTR
    lpTitleW: Windows.Win32.Foundation.PWSTR
    ptInvoke: Windows.Win32.Foundation.POINT
    lpVerbInt: UInt32
    lpVerbWInt: UInt32
class CM_COLUMNINFO(Structure):
    cbSize: UInt32
    dwMask: UInt32
    dwState: UInt32
    uWidth: UInt32
    uDefaultWidth: UInt32
    uIdealWidth: UInt32
    wszName: Char * 80
CM_ENUM_FLAGS = Int32
CM_ENUM_ALL: CM_ENUM_FLAGS = 1
CM_ENUM_VISIBLE: CM_ENUM_FLAGS = 2
CM_MASK = Int32
CM_MASK_WIDTH: CM_MASK = 1
CM_MASK_DEFAULTWIDTH: CM_MASK = 2
CM_MASK_IDEALWIDTH: CM_MASK = 4
CM_MASK_NAME: CM_MASK = 8
CM_MASK_STATE: CM_MASK = 16
CM_SET_WIDTH_VALUE = Int32
CM_WIDTH_USEDEFAULT: CM_SET_WIDTH_VALUE = -1
CM_WIDTH_AUTOSIZE: CM_SET_WIDTH_VALUE = -2
CM_STATE = Int32
CM_STATE_NONE: CM_STATE = 0
CM_STATE_VISIBLE: CM_STATE = 1
CM_STATE_FIXEDWIDTH: CM_STATE = 2
CM_STATE_NOSORTBYFOLDERNESS: CM_STATE = 4
CM_STATE_ALWAYSVISIBLE: CM_STATE = 8
class CONFIRM_CONFLICT_ITEM(Structure):
    pShellItem: Windows.Win32.UI.Shell.IShellItem2_head
    pszOriginalName: Windows.Win32.Foundation.PWSTR
    pszAlternateName: Windows.Win32.Foundation.PWSTR
    pszLocationShort: Windows.Win32.Foundation.PWSTR
    pszLocationFull: Windows.Win32.Foundation.PWSTR
    nType: Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ITEM_TYPE
class CONFIRM_CONFLICT_RESULT_INFO(Structure):
    pszNewName: Windows.Win32.Foundation.PWSTR
    iItemIndex: UInt32
class CPLINFO(Structure):
    idIcon: Int32
    idName: Int32
    idInfo: Int32
    lData: IntPtr
    _pack_ = 1
CPVIEW = Int32
CPVIEW_CLASSIC: CPVIEW = 0
CPVIEW_ALLITEMS: CPVIEW = 0
CPVIEW_CATEGORY: CPVIEW = 1
CPVIEW_HOME: CPVIEW = 1
CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS = Int32
CPAO_NONE: CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS = 0
CPAO_EMPTY_LOCAL: CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS = 1
CPAO_EMPTY_CONNECTED: CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS = 2
CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = Int32
CPCFO_NONE: CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 0
CPCFO_ENABLE_PASSWORD_REVEAL: CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 1
CPCFO_IS_EMAIL_ADDRESS: CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 2
CPCFO_ENABLE_TOUCH_KEYBOARD_AUTO_INVOKE: CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 4
CPCFO_NUMBERS_ONLY: CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 8
CPCFO_SHOW_ENGLISH_KEYBOARD: CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 16
class CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION(Structure):
    ulAuthenticationPackage: UInt32
    clsidCredentialProvider: Guid
    cbSerialization: UInt32
    rgbSerialization: c_char_p_no
class CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR(Structure):
    dwFieldID: UInt32
    cpft: Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE
    pszLabel: Windows.Win32.Foundation.PWSTR
    guidFieldType: Guid
CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = Int32
CPFIS_NONE: CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = 0
CPFIS_READONLY: CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = 1
CPFIS_DISABLED: CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = 2
CPFIS_FOCUSED: CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = 3
CREDENTIAL_PROVIDER_FIELD_STATE = Int32
CPFS_HIDDEN: CREDENTIAL_PROVIDER_FIELD_STATE = 0
CPFS_DISPLAY_IN_SELECTED_TILE: CREDENTIAL_PROVIDER_FIELD_STATE = 1
CPFS_DISPLAY_IN_DESELECTED_TILE: CREDENTIAL_PROVIDER_FIELD_STATE = 2
CPFS_DISPLAY_IN_BOTH: CREDENTIAL_PROVIDER_FIELD_STATE = 3
CREDENTIAL_PROVIDER_FIELD_TYPE = Int32
CPFT_INVALID: CREDENTIAL_PROVIDER_FIELD_TYPE = 0
CPFT_LARGE_TEXT: CREDENTIAL_PROVIDER_FIELD_TYPE = 1
CPFT_SMALL_TEXT: CREDENTIAL_PROVIDER_FIELD_TYPE = 2
CPFT_COMMAND_LINK: CREDENTIAL_PROVIDER_FIELD_TYPE = 3
CPFT_EDIT_TEXT: CREDENTIAL_PROVIDER_FIELD_TYPE = 4
CPFT_PASSWORD_TEXT: CREDENTIAL_PROVIDER_FIELD_TYPE = 5
CPFT_TILE_IMAGE: CREDENTIAL_PROVIDER_FIELD_TYPE = 6
CPFT_CHECKBOX: CREDENTIAL_PROVIDER_FIELD_TYPE = 7
CPFT_COMBOBOX: CREDENTIAL_PROVIDER_FIELD_TYPE = 8
CPFT_SUBMIT_BUTTON: CREDENTIAL_PROVIDER_FIELD_TYPE = 9
CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = Int32
CPGSR_NO_CREDENTIAL_NOT_FINISHED: CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = 0
CPGSR_NO_CREDENTIAL_FINISHED: CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = 1
CPGSR_RETURN_CREDENTIAL_FINISHED: CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = 2
CPGSR_RETURN_NO_CREDENTIAL_FINISHED: CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = 3
CREDENTIAL_PROVIDER_STATUS_ICON = Int32
CPSI_NONE: CREDENTIAL_PROVIDER_STATUS_ICON = 0
CPSI_ERROR: CREDENTIAL_PROVIDER_STATUS_ICON = 1
CPSI_WARNING: CREDENTIAL_PROVIDER_STATUS_ICON = 2
CPSI_SUCCESS: CREDENTIAL_PROVIDER_STATUS_ICON = 3
CREDENTIAL_PROVIDER_USAGE_SCENARIO = Int32
CPUS_INVALID: CREDENTIAL_PROVIDER_USAGE_SCENARIO = 0
CPUS_LOGON: CREDENTIAL_PROVIDER_USAGE_SCENARIO = 1
CPUS_UNLOCK_WORKSTATION: CREDENTIAL_PROVIDER_USAGE_SCENARIO = 2
CPUS_CHANGE_PASSWORD: CREDENTIAL_PROVIDER_USAGE_SCENARIO = 3
CPUS_CREDUI: CREDENTIAL_PROVIDER_USAGE_SCENARIO = 4
CPUS_PLAP: CREDENTIAL_PROVIDER_USAGE_SCENARIO = 5
class CSFV(Structure):
    cbSize: UInt32
    pshf: Windows.Win32.UI.Shell.IShellFolder_head
    psvOuter: Windows.Win32.UI.Shell.IShellView_head
    pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    lEvents: Int32
    pfnCallback: Windows.Win32.UI.Shell.LPFNVIEWCALLBACK
    fvm: Windows.Win32.UI.Shell.FOLDERVIEWMODE
CScriptErrorList = Guid('efd01300-160f-11d2-bb-2e-00-80-5f-f7-ef-ca')
CommandStateChangeConstants = Int32
CSC_UPDATECOMMANDS: CommandStateChangeConstants = -1
CSC_NAVIGATEFORWARD: CommandStateChangeConstants = 1
CSC_NAVIGATEBACK: CommandStateChangeConstants = 2
ConflictFolder = Guid('289978ac-a101-4341-a8-17-21-eb-a7-fd-04-6d')
class DATABLOCK_HEADER(Structure):
    cbSize: UInt32
    dwSignature: UInt32
    _pack_ = 1
DATAOBJ_GET_ITEM_FLAGS = Int32
DOGIF_DEFAULT: DATAOBJ_GET_ITEM_FLAGS = 0
DOGIF_TRAVERSE_LINK: DATAOBJ_GET_ITEM_FLAGS = 1
DOGIF_NO_HDROP: DATAOBJ_GET_ITEM_FLAGS = 2
DOGIF_NO_URL: DATAOBJ_GET_ITEM_FLAGS = 4
DOGIF_ONLY_IF_ONE: DATAOBJ_GET_ITEM_FLAGS = 8
DEFAULTSAVEFOLDERTYPE = Int32
DSFT_DETECT: DEFAULTSAVEFOLDERTYPE = 1
DSFT_PRIVATE: DEFAULTSAVEFOLDERTYPE = 2
DSFT_PUBLIC: DEFAULTSAVEFOLDERTYPE = 3
DEFAULT_FOLDER_MENU_RESTRICTIONS = Int32
DFMR_DEFAULT: DEFAULT_FOLDER_MENU_RESTRICTIONS = 0
DFMR_NO_STATIC_VERBS: DEFAULT_FOLDER_MENU_RESTRICTIONS = 8
DFMR_STATIC_VERBS_ONLY: DEFAULT_FOLDER_MENU_RESTRICTIONS = 16
DFMR_NO_RESOURCE_VERBS: DEFAULT_FOLDER_MENU_RESTRICTIONS = 32
DFMR_OPTIN_HANDLERS_ONLY: DEFAULT_FOLDER_MENU_RESTRICTIONS = 64
DFMR_RESOURCE_AND_FOLDER_VERBS_ONLY: DEFAULT_FOLDER_MENU_RESTRICTIONS = 128
DFMR_USE_SPECIFIED_HANDLERS: DEFAULT_FOLDER_MENU_RESTRICTIONS = 256
DFMR_USE_SPECIFIED_VERBS: DEFAULT_FOLDER_MENU_RESTRICTIONS = 512
DFMR_NO_ASYNC_VERBS: DEFAULT_FOLDER_MENU_RESTRICTIONS = 1024
DFMR_NO_NATIVECPU_VERBS: DEFAULT_FOLDER_MENU_RESTRICTIONS = 2048
DFMR_NO_NONWOW_VERBS: DEFAULT_FOLDER_MENU_RESTRICTIONS = 4096
class DEFCONTEXTMENU(Structure):
    hwnd: Windows.Win32.Foundation.HWND
    pcmcb: Windows.Win32.UI.Shell.IContextMenuCB_head
    pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    psf: Windows.Win32.UI.Shell.IShellFolder_head
    cidl: UInt32
    apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))
    punkAssociationInfo: Windows.Win32.System.Com.IUnknown_head
    cKeys: UInt32
    aKeys: POINTER(Windows.Win32.System.Registry.HKEY)
DEF_SHARE_ID = Int32
DEFSHAREID_USERS: DEF_SHARE_ID = 1
DEFSHAREID_PUBLIC: DEF_SHARE_ID = 2
class DELEGATEITEMID(Structure):
    cbSize: UInt16
    wOuter: UInt16
    cbInner: UInt16
    rgb: Byte * 1
    _pack_ = 1
DESKBANDCID = Int32
DBID_BANDINFOCHANGED: DESKBANDCID = 0
DBID_SHOWONLY: DESKBANDCID = 1
DBID_MAXIMIZEBAND: DESKBANDCID = 2
DBID_PUSHCHEVRON: DESKBANDCID = 3
DBID_DELAYINIT: DESKBANDCID = 4
DBID_FINISHINIT: DESKBANDCID = 5
DBID_SETWINDOWTHEME: DESKBANDCID = 6
DBID_PERMITAUTOHIDE: DESKBANDCID = 7
class DESKBANDINFO(Structure):
    dwMask: UInt32
    ptMinSize: Windows.Win32.Foundation.POINTL
    ptMaxSize: Windows.Win32.Foundation.POINTL
    ptIntegral: Windows.Win32.Foundation.POINTL
    ptActual: Windows.Win32.Foundation.POINTL
    wszTitle: Char * 256
    dwModeFlags: UInt32
    crBkgnd: Windows.Win32.Foundation.COLORREF
DESKTOP_SLIDESHOW_DIRECTION = Int32
DSD_FORWARD: DESKTOP_SLIDESHOW_DIRECTION = 0
DSD_BACKWARD: DESKTOP_SLIDESHOW_DIRECTION = 1
DESKTOP_SLIDESHOW_OPTIONS = Int32
DSO_SHUFFLEIMAGES: DESKTOP_SLIDESHOW_OPTIONS = 1
DESKTOP_SLIDESHOW_STATE = Int32
DSS_ENABLED: DESKTOP_SLIDESHOW_STATE = 1
DSS_SLIDESHOW: DESKTOP_SLIDESHOW_STATE = 2
DSS_DISABLED_BY_REMOTE_SESSION: DESKTOP_SLIDESHOW_STATE = 4
DESKTOP_WALLPAPER_POSITION = Int32
DWPOS_CENTER: DESKTOP_WALLPAPER_POSITION = 0
DWPOS_TILE: DESKTOP_WALLPAPER_POSITION = 1
DWPOS_STRETCH: DESKTOP_WALLPAPER_POSITION = 2
DWPOS_FIT: DESKTOP_WALLPAPER_POSITION = 3
DWPOS_FILL: DESKTOP_WALLPAPER_POSITION = 4
DWPOS_SPAN: DESKTOP_WALLPAPER_POSITION = 5
class DETAILSINFO(Structure):
    pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    fmt: Int32
    cxChar: Int32
    str: Windows.Win32.UI.Shell.Common.STRRET
    iImage: Int32
class DFConstraint(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4a3df050-23bd-11d2-93-9f-00-a0-c9-1e-ed-ba')
    @commethod(7)
    def get_Name(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Value(pv: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class DFMICS(Structure):
    cbSize: UInt32
    fMask: UInt32
    lParam: Windows.Win32.Foundation.LPARAM
    idCmdFirst: UInt32
    idDefMax: UInt32
    pici: POINTER(Windows.Win32.UI.Shell.CMINVOKECOMMANDINFO_head)
    punkSite: Windows.Win32.System.Com.IUnknown_head
DFM_CMD = Int32
DFM_CMD_DELETE: DFM_CMD = -1
DFM_CMD_MOVE: DFM_CMD = -2
DFM_CMD_COPY: DFM_CMD = -3
DFM_CMD_LINK: DFM_CMD = -4
DFM_CMD_PROPERTIES: DFM_CMD = -5
DFM_CMD_NEWFOLDER: DFM_CMD = -6
DFM_CMD_PASTE: DFM_CMD = -7
DFM_CMD_VIEWLIST: DFM_CMD = -8
DFM_CMD_VIEWDETAILS: DFM_CMD = -9
DFM_CMD_PASTELINK: DFM_CMD = -10
DFM_CMD_PASTESPECIAL: DFM_CMD = -11
DFM_CMD_MODALPROP: DFM_CMD = -12
DFM_CMD_RENAME: DFM_CMD = -13
DFM_MESSAGE_ID = Int32
DFM_MERGECONTEXTMENU: DFM_MESSAGE_ID = 1
DFM_INVOKECOMMAND: DFM_MESSAGE_ID = 2
DFM_GETHELPTEXT: DFM_MESSAGE_ID = 5
DFM_WM_MEASUREITEM: DFM_MESSAGE_ID = 6
DFM_WM_DRAWITEM: DFM_MESSAGE_ID = 7
DFM_WM_INITMENUPOPUP: DFM_MESSAGE_ID = 8
DFM_VALIDATECMD: DFM_MESSAGE_ID = 9
DFM_MERGECONTEXTMENU_TOP: DFM_MESSAGE_ID = 10
DFM_GETHELPTEXTW: DFM_MESSAGE_ID = 11
DFM_INVOKECOMMANDEX: DFM_MESSAGE_ID = 12
DFM_MAPCOMMANDNAME: DFM_MESSAGE_ID = 13
DFM_GETDEFSTATICID: DFM_MESSAGE_ID = 14
DFM_GETVERBW: DFM_MESSAGE_ID = 15
DFM_GETVERBA: DFM_MESSAGE_ID = 16
DFM_MERGECONTEXTMENU_BOTTOM: DFM_MESSAGE_ID = 17
DFM_MODIFYQCMFLAGS: DFM_MESSAGE_ID = 18
DISPLAY_DEVICE_TYPE = Int32
DEVICE_PRIMARY: DISPLAY_DEVICE_TYPE = 0
DEVICE_IMMERSIVE: DISPLAY_DEVICE_TYPE = 1
@winfunctype_pointer
def DLLGETVERSIONPROC(param0: POINTER(Windows.Win32.UI.Shell.DLLVERSIONINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class DLLVERSIONINFO(Structure):
    cbSize: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    dwPlatformID: UInt32
class DLLVERSIONINFO2(Structure):
    info1: Windows.Win32.UI.Shell.DLLVERSIONINFO
    dwFlags: UInt32
    ullVersion: UInt64
if ARCH in 'X64,ARM64':
    class DRAGINFOA(Structure):
        uSize: UInt32
        pt: Windows.Win32.Foundation.POINT
        fNC: Windows.Win32.Foundation.BOOL
        lpFileList: Windows.Win32.Foundation.PSTR
        grfKeyState: UInt32
if ARCH in 'X86':
    class DRAGINFOA(Structure):
        uSize: UInt32
        pt: Windows.Win32.Foundation.POINT
        fNC: Windows.Win32.Foundation.BOOL
        lpFileList: Windows.Win32.Foundation.PSTR
        grfKeyState: UInt32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class DRAGINFOW(Structure):
        uSize: UInt32
        pt: Windows.Win32.Foundation.POINT
        fNC: Windows.Win32.Foundation.BOOL
        lpFileList: Windows.Win32.Foundation.PWSTR
        grfKeyState: UInt32
if ARCH in 'X86':
    class DRAGINFOW(Structure):
        uSize: UInt32
        pt: Windows.Win32.Foundation.POINT
        fNC: Windows.Win32.Foundation.BOOL
        lpFileList: Windows.Win32.Foundation.PWSTR
        grfKeyState: UInt32
        _pack_ = 1
class DROPDESCRIPTION(Structure):
    type: Windows.Win32.UI.Shell.DROPIMAGETYPE
    szMessage: Char * 260
    szInsert: Char * 260
    _pack_ = 1
class DROPFILES(Structure):
    pFiles: UInt32
    pt: Windows.Win32.Foundation.POINT
    fNC: Windows.Win32.Foundation.BOOL
    fWide: Windows.Win32.Foundation.BOOL
    _pack_ = 1
DROPIMAGETYPE = Int32
DROPIMAGE_INVALID: DROPIMAGETYPE = -1
DROPIMAGE_NONE: DROPIMAGETYPE = 0
DROPIMAGE_COPY: DROPIMAGETYPE = 1
DROPIMAGE_MOVE: DROPIMAGETYPE = 2
DROPIMAGE_LINK: DROPIMAGETYPE = 4
DROPIMAGE_LABEL: DROPIMAGETYPE = 6
DROPIMAGE_WARNING: DROPIMAGETYPE = 7
DROPIMAGE_NOIMAGE: DROPIMAGETYPE = 8
DSH_FLAGS = Int32
DSH_ALLOWDROPDESCRIPTIONTEXT: DSH_FLAGS = 1
class DShellFolderViewEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('62112aa2-ebe4-11cf-a5-fb-00-20-af-e7-29-2d')
class DShellNameSpaceEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('55136806-b2de-11d1-b9-f2-00-a0-c9-8b-c5-47')
class DShellWindowsEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('fe4106e0-399a-11d0-a4-8c-00-a0-c9-0a-8f-39')
class DWebBrowserEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('eab22ac2-30c1-11cf-a7-eb-00-00-c0-5b-ae-0b')
class DWebBrowserEvents2(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('34a715a0-6587-11d0-92-4a-00-20-af-c7-ac-4d')
DefFolderMenu = Guid('c63382be-7933-48d0-9a-c8-85-fb-46-be-2f-dd')
DesktopGadget = Guid('924ccc1b-6562-4c85-86-57-d1-77-92-52-22-b6')
DesktopWallpaper = Guid('c2cf3110-460e-4fc1-b9-d0-8a-1c-0c-9c-c4-bd')
DestinationList = Guid('77f10cf0-3db5-4966-b5-20-b7-c5-4f-d3-5e-d6')
DocPropShellExtension = Guid('883373c3-bf89-11d1-be-35-08-00-36-b1-1a-03')
DriveSizeCategorizer = Guid('94357b53-ca29-4b78-83-ae-e8-fe-74-09-13-4f')
DriveTypeCategorizer = Guid('b0a8f3cf-4333-4bab-88-73-1c-cb-1c-ad-a4-8b')
EC_HOST_UI_MODE = Int32
ECHUIM_DESKTOP: EC_HOST_UI_MODE = 0
ECHUIM_IMMERSIVE: EC_HOST_UI_MODE = 1
ECHUIM_SYSTEM_LAUNCHER: EC_HOST_UI_MODE = 2
EDGE_GESTURE_KIND = Int32
EGK_TOUCH: EDGE_GESTURE_KIND = 0
EGK_KEYBOARD: EDGE_GESTURE_KIND = 1
EGK_MOUSE: EDGE_GESTURE_KIND = 2
EXPLORER_BROWSER_FILL_FLAGS = Int32
EBF_NONE: EXPLORER_BROWSER_FILL_FLAGS = 0
EBF_SELECTFROMDATAOBJECT: EXPLORER_BROWSER_FILL_FLAGS = 256
EBF_NODROPTARGET: EXPLORER_BROWSER_FILL_FLAGS = 512
EXPLORER_BROWSER_OPTIONS = Int32
EBO_NONE: EXPLORER_BROWSER_OPTIONS = 0
EBO_NAVIGATEONCE: EXPLORER_BROWSER_OPTIONS = 1
EBO_SHOWFRAMES: EXPLORER_BROWSER_OPTIONS = 2
EBO_ALWAYSNAVIGATE: EXPLORER_BROWSER_OPTIONS = 4
EBO_NOTRAVELLOG: EXPLORER_BROWSER_OPTIONS = 8
EBO_NOWRAPPERWINDOW: EXPLORER_BROWSER_OPTIONS = 16
EBO_HTMLSHAREPOINTVIEW: EXPLORER_BROWSER_OPTIONS = 32
EBO_NOBORDER: EXPLORER_BROWSER_OPTIONS = 64
EBO_NOPERSISTVIEWSTATE: EXPLORER_BROWSER_OPTIONS = 128
class EXP_DARWIN_LINK(Structure):
    dbh: Windows.Win32.UI.Shell.DATABLOCK_HEADER
    szDarwinID: Windows.Win32.Foundation.CHAR * 260
    szwDarwinID: Char * 260
    _pack_ = 1
class EXP_PROPERTYSTORAGE(Structure):
    cbSize: UInt32
    dwSignature: UInt32
    abPropertyStorage: Byte * 1
    _pack_ = 1
class EXP_SPECIAL_FOLDER(Structure):
    cbSize: UInt32
    dwSignature: UInt32
    idSpecialFolder: UInt32
    cbOffset: UInt32
    _pack_ = 1
class EXP_SZ_LINK(Structure):
    cbSize: UInt32
    dwSignature: UInt32
    szTarget: Windows.Win32.Foundation.CHAR * 260
    swzTarget: Char * 260
    _pack_ = 1
class EXTRASEARCH(Structure):
    guidSearch: Guid
    wszFriendlyName: Char * 80
    wszUrl: Char * 2084
EnumerableObjectCollection = Guid('2d3468c1-36a7-43b6-ac-24-d3-f0-2f-d9-60-7a')
ExecuteFolder = Guid('11dbb47c-a525-400b-9e-80-a5-46-15-a0-90-c0')
ExecuteUnknown = Guid('e44e9428-bdbc-4987-a0-99-40-dc-8f-d2-55-e7')
ExplorerBrowser = Guid('71f96385-ddd6-48d3-a0-c1-ae-06-e8-b0-55-fb')
FDAP = Int32
FDAP_BOTTOM: FDAP = 0
FDAP_TOP: FDAP = 1
FDE_OVERWRITE_RESPONSE = Int32
FDEOR_DEFAULT: FDE_OVERWRITE_RESPONSE = 0
FDEOR_ACCEPT: FDE_OVERWRITE_RESPONSE = 1
FDEOR_REFUSE: FDE_OVERWRITE_RESPONSE = 2
FDE_SHAREVIOLATION_RESPONSE = Int32
FDESVR_DEFAULT: FDE_SHAREVIOLATION_RESPONSE = 0
FDESVR_ACCEPT: FDE_SHAREVIOLATION_RESPONSE = 1
FDESVR_REFUSE: FDE_SHAREVIOLATION_RESPONSE = 2
FD_FLAGS = Int32
FD_CLSID: FD_FLAGS = 1
FD_SIZEPOINT: FD_FLAGS = 2
FD_ATTRIBUTES: FD_FLAGS = 4
FD_CREATETIME: FD_FLAGS = 8
FD_ACCESSTIME: FD_FLAGS = 16
FD_WRITESTIME: FD_FLAGS = 32
FD_FILESIZE: FD_FLAGS = 64
FD_PROGRESSUI: FD_FLAGS = 16384
FD_LINKUI: FD_FLAGS = 32768
FD_UNICODE: FD_FLAGS = -2147483648
FFFP_MODE = Int32
FFFP_EXACTMATCH: FFFP_MODE = 0
FFFP_NEARESTPARENTMATCH: FFFP_MODE = 1
class FILEDESCRIPTORA(Structure):
    dwFlags: UInt32
    clsid: Guid
    sizel: Windows.Win32.Foundation.SIZE
    pointl: Windows.Win32.Foundation.POINTL
    dwFileAttributes: UInt32
    ftCreationTime: Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    cFileName: Windows.Win32.Foundation.CHAR * 260
    _pack_ = 1
class FILEDESCRIPTORW(Structure):
    dwFlags: UInt32
    clsid: Guid
    sizel: Windows.Win32.Foundation.SIZE
    pointl: Windows.Win32.Foundation.POINTL
    dwFileAttributes: UInt32
    ftCreationTime: Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    cFileName: Char * 260
    _pack_ = 1
class FILEGROUPDESCRIPTORA(Structure):
    cItems: UInt32
    fgd: Windows.Win32.UI.Shell.FILEDESCRIPTORA * 1
    _pack_ = 1
class FILEGROUPDESCRIPTORW(Structure):
    cItems: UInt32
    fgd: Windows.Win32.UI.Shell.FILEDESCRIPTORW * 1
    _pack_ = 1
FILEOPENDIALOGOPTIONS = UInt32
FOS_OVERWRITEPROMPT: FILEOPENDIALOGOPTIONS = 2
FOS_STRICTFILETYPES: FILEOPENDIALOGOPTIONS = 4
FOS_NOCHANGEDIR: FILEOPENDIALOGOPTIONS = 8
FOS_PICKFOLDERS: FILEOPENDIALOGOPTIONS = 32
FOS_FORCEFILESYSTEM: FILEOPENDIALOGOPTIONS = 64
FOS_ALLNONSTORAGEITEMS: FILEOPENDIALOGOPTIONS = 128
FOS_NOVALIDATE: FILEOPENDIALOGOPTIONS = 256
FOS_ALLOWMULTISELECT: FILEOPENDIALOGOPTIONS = 512
FOS_PATHMUSTEXIST: FILEOPENDIALOGOPTIONS = 2048
FOS_FILEMUSTEXIST: FILEOPENDIALOGOPTIONS = 4096
FOS_CREATEPROMPT: FILEOPENDIALOGOPTIONS = 8192
FOS_SHAREAWARE: FILEOPENDIALOGOPTIONS = 16384
FOS_NOREADONLYRETURN: FILEOPENDIALOGOPTIONS = 32768
FOS_NOTESTFILECREATE: FILEOPENDIALOGOPTIONS = 65536
FOS_HIDEMRUPLACES: FILEOPENDIALOGOPTIONS = 131072
FOS_HIDEPINNEDPLACES: FILEOPENDIALOGOPTIONS = 262144
FOS_NODEREFERENCELINKS: FILEOPENDIALOGOPTIONS = 1048576
FOS_OKBUTTONNEEDSINTERACTION: FILEOPENDIALOGOPTIONS = 2097152
FOS_DONTADDTORECENT: FILEOPENDIALOGOPTIONS = 33554432
FOS_FORCESHOWHIDDEN: FILEOPENDIALOGOPTIONS = 268435456
FOS_DEFAULTNOMINIMODE: FILEOPENDIALOGOPTIONS = 536870912
FOS_FORCEPREVIEWPANEON: FILEOPENDIALOGOPTIONS = 1073741824
FOS_SUPPORTSTREAMABLEITEMS: FILEOPENDIALOGOPTIONS = 2147483648
FILETYPEATTRIBUTEFLAGS = Int32
FTA_None: FILETYPEATTRIBUTEFLAGS = 0
FTA_Exclude: FILETYPEATTRIBUTEFLAGS = 1
FTA_Show: FILETYPEATTRIBUTEFLAGS = 2
FTA_HasExtension: FILETYPEATTRIBUTEFLAGS = 4
FTA_NoEdit: FILETYPEATTRIBUTEFLAGS = 8
FTA_NoRemove: FILETYPEATTRIBUTEFLAGS = 16
FTA_NoNewVerb: FILETYPEATTRIBUTEFLAGS = 32
FTA_NoEditVerb: FILETYPEATTRIBUTEFLAGS = 64
FTA_NoRemoveVerb: FILETYPEATTRIBUTEFLAGS = 128
FTA_NoEditDesc: FILETYPEATTRIBUTEFLAGS = 256
FTA_NoEditIcon: FILETYPEATTRIBUTEFLAGS = 512
FTA_NoEditDflt: FILETYPEATTRIBUTEFLAGS = 1024
FTA_NoEditVerbCmd: FILETYPEATTRIBUTEFLAGS = 2048
FTA_NoEditVerbExe: FILETYPEATTRIBUTEFLAGS = 4096
FTA_NoDDE: FILETYPEATTRIBUTEFLAGS = 8192
FTA_NoEditMIME: FILETYPEATTRIBUTEFLAGS = 32768
FTA_OpenIsSafe: FILETYPEATTRIBUTEFLAGS = 65536
FTA_AlwaysUnsafe: FILETYPEATTRIBUTEFLAGS = 131072
FTA_NoRecentDocs: FILETYPEATTRIBUTEFLAGS = 1048576
FTA_SafeForElevation: FILETYPEATTRIBUTEFLAGS = 2097152
FTA_AlwaysUseDirectInvoke: FILETYPEATTRIBUTEFLAGS = 4194304
class FILE_ATTRIBUTES_ARRAY(Structure):
    cItems: UInt32
    dwSumFileAttributes: UInt32
    dwProductFileAttributes: UInt32
    rgdwFileAttributes: UInt32 * 1
    _pack_ = 1
FILE_OPERATION_FLAGS2 = Int32
FOF2_NONE: FILE_OPERATION_FLAGS2 = 0
FOF2_MERGEFOLDERSONCOLLISION: FILE_OPERATION_FLAGS2 = 1
FILE_USAGE_TYPE = Int32
FUT_PLAYING: FILE_USAGE_TYPE = 0
FUT_EDITING: FILE_USAGE_TYPE = 1
FUT_GENERIC: FILE_USAGE_TYPE = 2
FLYOUT_PLACEMENT = Int32
FP_DEFAULT: FLYOUT_PLACEMENT = 0
FP_ABOVE: FLYOUT_PLACEMENT = 1
FP_BELOW: FLYOUT_PLACEMENT = 2
FP_LEFT: FLYOUT_PLACEMENT = 3
FP_RIGHT: FLYOUT_PLACEMENT = 4
FOLDERFLAGS = Int32
FWF_NONE: FOLDERFLAGS = 0
FWF_AUTOARRANGE: FOLDERFLAGS = 1
FWF_ABBREVIATEDNAMES: FOLDERFLAGS = 2
FWF_SNAPTOGRID: FOLDERFLAGS = 4
FWF_OWNERDATA: FOLDERFLAGS = 8
FWF_BESTFITWINDOW: FOLDERFLAGS = 16
FWF_DESKTOP: FOLDERFLAGS = 32
FWF_SINGLESEL: FOLDERFLAGS = 64
FWF_NOSUBFOLDERS: FOLDERFLAGS = 128
FWF_TRANSPARENT: FOLDERFLAGS = 256
FWF_NOCLIENTEDGE: FOLDERFLAGS = 512
FWF_NOSCROLL: FOLDERFLAGS = 1024
FWF_ALIGNLEFT: FOLDERFLAGS = 2048
FWF_NOICONS: FOLDERFLAGS = 4096
FWF_SHOWSELALWAYS: FOLDERFLAGS = 8192
FWF_NOVISIBLE: FOLDERFLAGS = 16384
FWF_SINGLECLICKACTIVATE: FOLDERFLAGS = 32768
FWF_NOWEBVIEW: FOLDERFLAGS = 65536
FWF_HIDEFILENAMES: FOLDERFLAGS = 131072
FWF_CHECKSELECT: FOLDERFLAGS = 262144
FWF_NOENUMREFRESH: FOLDERFLAGS = 524288
FWF_NOGROUPING: FOLDERFLAGS = 1048576
FWF_FULLROWSELECT: FOLDERFLAGS = 2097152
FWF_NOFILTERS: FOLDERFLAGS = 4194304
FWF_NOCOLUMNHEADER: FOLDERFLAGS = 8388608
FWF_NOHEADERINALLVIEWS: FOLDERFLAGS = 16777216
FWF_EXTENDEDTILES: FOLDERFLAGS = 33554432
FWF_TRICHECKSELECT: FOLDERFLAGS = 67108864
FWF_AUTOCHECKSELECT: FOLDERFLAGS = 134217728
FWF_NOBROWSERVIEWSTATE: FOLDERFLAGS = 268435456
FWF_SUBSETGROUPS: FOLDERFLAGS = 536870912
FWF_USESEARCHFOLDER: FOLDERFLAGS = 1073741824
FWF_ALLOWRTLREADING: FOLDERFLAGS = -2147483648
FOLDERLOGICALVIEWMODE = Int32
FLVM_UNSPECIFIED: FOLDERLOGICALVIEWMODE = -1
FLVM_FIRST: FOLDERLOGICALVIEWMODE = 1
FLVM_DETAILS: FOLDERLOGICALVIEWMODE = 1
FLVM_TILES: FOLDERLOGICALVIEWMODE = 2
FLVM_ICONS: FOLDERLOGICALVIEWMODE = 3
FLVM_LIST: FOLDERLOGICALVIEWMODE = 4
FLVM_CONTENT: FOLDERLOGICALVIEWMODE = 5
FLVM_LAST: FOLDERLOGICALVIEWMODE = 5
class FOLDERSETDATA(Structure):
    _fs: Windows.Win32.UI.Shell.FOLDERSETTINGS
    _vidRestore: Guid
    _dwViewPriority: UInt32
class FOLDERSETTINGS(Structure):
    ViewMode: UInt32
    fFlags: UInt32
FOLDERVIEWMODE = Int32
FVM_AUTO: FOLDERVIEWMODE = -1
FVM_FIRST: FOLDERVIEWMODE = 1
FVM_ICON: FOLDERVIEWMODE = 1
FVM_SMALLICON: FOLDERVIEWMODE = 2
FVM_LIST: FOLDERVIEWMODE = 3
FVM_DETAILS: FOLDERVIEWMODE = 4
FVM_THUMBNAIL: FOLDERVIEWMODE = 5
FVM_TILE: FOLDERVIEWMODE = 6
FVM_THUMBSTRIP: FOLDERVIEWMODE = 7
FVM_CONTENT: FOLDERVIEWMODE = 8
FVM_LAST: FOLDERVIEWMODE = 8
FOLDERVIEWOPTIONS = Int32
FVO_DEFAULT: FOLDERVIEWOPTIONS = 0
FVO_VISTALAYOUT: FOLDERVIEWOPTIONS = 1
FVO_CUSTOMPOSITION: FOLDERVIEWOPTIONS = 2
FVO_CUSTOMORDERING: FOLDERVIEWOPTIONS = 4
FVO_SUPPORTHYPERLINKS: FOLDERVIEWOPTIONS = 8
FVO_NOANIMATIONS: FOLDERVIEWOPTIONS = 16
FVO_NOSCROLLTIPS: FOLDERVIEWOPTIONS = 32
FOLDER_ENUM_MODE = Int32
FEM_VIEWRESULT: FOLDER_ENUM_MODE = 0
FEM_NAVIGATION: FOLDER_ENUM_MODE = 1
FSCopyHandler = Guid('d197380a-0a79-4dc8-a0-33-ed-88-2c-2f-a1-4b')
FVTEXTTYPE = Int32
FVST_EMPTYTEXT: FVTEXTTYPE = 0
FileOpenDialog = Guid('dc1c5a9c-e88a-4dde-a5-a1-60-f8-2a-20-ae-f7')
FileOperation = Guid('3ad05575-8857-4850-92-77-11-b8-5b-db-8e-09')
FileSaveDialog = Guid('c0b4e2f3-ba21-4773-8d-ba-33-5e-c9-46-eb-8b')
FileSearchBand = Guid('c4ee31f3-4768-11d2-be-5c-00-a0-c9-a8-3d-a1')
class Folder(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('bbcbde60-c3ff-11ce-83-50-44-45-53-54-00-00')
    @commethod(7)
    def get_Title(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Application(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Parent(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ParentFolder(ppsf: POINTER(Windows.Win32.UI.Shell.Folder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Items(ppid: POINTER(Windows.Win32.UI.Shell.FolderItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ParseName(bName: Windows.Win32.Foundation.BSTR, ppid: POINTER(Windows.Win32.UI.Shell.FolderItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def NewFolder(bName: Windows.Win32.Foundation.BSTR, vOptions: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MoveHere(vItem: Windows.Win32.System.Com.VARIANT, vOptions: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CopyHere(vItem: Windows.Win32.System.Com.VARIANT, vOptions: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDetailsOf(vItem: Windows.Win32.System.Com.VARIANT, iColumn: Int32, pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class Folder2(c_void_p):
    extends: Windows.Win32.UI.Shell.Folder
    Guid = Guid('f0d2d8ef-3890-11d2-bf-8b-00-c0-4f-b9-36-61')
    @commethod(17)
    def get_Self(ppfi: POINTER(Windows.Win32.UI.Shell.FolderItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_OfflineStatus(pul: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Synchronize() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_HaveToShowWebViewBarricade(pbHaveToShowWebViewBarricade: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DismissedWebViewBarricade() -> Windows.Win32.Foundation.HRESULT: ...
class Folder3(c_void_p):
    extends: Windows.Win32.UI.Shell.Folder2
    Guid = Guid('a7ae5f64-c4d7-4d7f-93-07-4d-24-ee-54-b8-41')
    @commethod(22)
    def get_ShowWebViewBarricade(pbShowWebViewBarricade: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_ShowWebViewBarricade(bShowWebViewBarricade: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class FolderItem(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('fac32c80-cbe4-11ce-83-50-44-45-53-54-00-00')
    @commethod(7)
    def get_Application(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Parent(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Name(bs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Path(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_GetLink(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_GetFolder(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_IsLink(pb: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsFolder(pb: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsFileSystem(pb: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_IsBrowsable(pb: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ModifyDate(pdt: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_ModifyDate(dt: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Size(pul: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Type(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Verbs(ppfic: POINTER(Windows.Win32.UI.Shell.FolderItemVerbs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def InvokeVerb(vVerb: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class FolderItem2(c_void_p):
    extends: Windows.Win32.UI.Shell.FolderItem
    Guid = Guid('edc817aa-92b8-11d1-b0-75-00-c0-4f-c3-3a-a5')
    @commethod(24)
    def InvokeVerbEx(vVerb: Windows.Win32.System.Com.VARIANT, vArgs: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ExtendedProperty(bstrPropName: Windows.Win32.Foundation.BSTR, pvRet: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class FolderItemVerb(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('08ec3e00-50b0-11cf-96-0c-00-80-c7-f4-ee-85')
    @commethod(7)
    def get_Application(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Parent(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DoIt() -> Windows.Win32.Foundation.HRESULT: ...
class FolderItemVerbs(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('1f8352c0-50b0-11cf-96-0c-00-80-c7-f4-ee-85')
    @commethod(7)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Application(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Parent(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(index: Windows.Win32.System.Com.VARIANT, ppid: POINTER(Windows.Win32.UI.Shell.FolderItemVerb_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def _NewEnum(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class FolderItems(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('744129e0-cbe5-11ce-83-50-44-45-53-54-00-00')
    @commethod(7)
    def get_Count(plCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Application(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Parent(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(index: Windows.Win32.System.Com.VARIANT, ppid: POINTER(Windows.Win32.UI.Shell.FolderItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def _NewEnum(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class FolderItems2(c_void_p):
    extends: Windows.Win32.UI.Shell.FolderItems
    Guid = Guid('c94f0ad0-f363-11d2-a3-27-00-c0-4f-8e-ec-7f')
    @commethod(12)
    def InvokeVerbEx(vVerb: Windows.Win32.System.Com.VARIANT, vArgs: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class FolderItems3(c_void_p):
    extends: Windows.Win32.UI.Shell.FolderItems2
    Guid = Guid('eaa7c309-bbec-49d5-82-1d-64-d9-66-cb-66-7f')
    @commethod(13)
    def Filter(grfFlags: Int32, bstrFileSpec: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Verbs(ppfic: POINTER(Windows.Win32.UI.Shell.FolderItemVerbs_head)) -> Windows.Win32.Foundation.HRESULT: ...
FolderViewHost = Guid('20b1cb23-6968-4eb9-b7-d4-a6-6d-00-d0-7c-ee')
FrameworkInputPane = Guid('d5120aa3-46ba-44c5-82-2d-ca-80-92-c1-fc-72')
FreeSpaceCategorizer = Guid('b5607793-24ac-44c7-82-e2-83-17-26-aa-6c-b7')
GPFIDL_FLAGS = UInt32
GPFIDL_DEFAULT: GPFIDL_FLAGS = 0
GPFIDL_ALTNAME: GPFIDL_FLAGS = 1
GPFIDL_UNCPRINTER: GPFIDL_FLAGS = 2
GenericCredentialProvider = Guid('25cbb996-92ed-457e-b2-8c-47-74-08-4b-d5-62')
HDROP = IntPtr
class HELPINFO(Structure):
    cbSize: UInt32
    iContextType: Windows.Win32.UI.Shell.HELP_INFO_TYPE
    iCtrlId: Int32
    hItemHandle: Windows.Win32.Foundation.HANDLE
    dwContextId: UIntPtr
    MousePos: Windows.Win32.Foundation.POINT
class HELPWININFOA(Structure):
    wStructSize: Int32
    x: Int32
    y: Int32
    dx: Int32
    dy: Int32
    wMax: Int32
    rgchMember: Windows.Win32.Foundation.CHAR * 2
class HELPWININFOW(Structure):
    wStructSize: Int32
    x: Int32
    y: Int32
    dx: Int32
    dy: Int32
    wMax: Int32
    rgchMember: Char * 2
HELP_INFO_TYPE = Int32
HELPINFO_WINDOW: HELP_INFO_TYPE = 1
HELPINFO_MENUITEM: HELP_INFO_TYPE = 2
HLBWIF_FLAGS = UInt32
HLBWIF_HASFRAMEWNDINFO: HLBWIF_FLAGS = 1
HLBWIF_HASDOCWNDINFO: HLBWIF_FLAGS = 2
HLBWIF_FRAMEWNDMAXIMIZED: HLBWIF_FLAGS = 4
HLBWIF_DOCWNDMAXIMIZED: HLBWIF_FLAGS = 8
HLBWIF_HASWEBTOOLBARINFO: HLBWIF_FLAGS = 16
HLBWIF_WEBTOOLBARHIDDEN: HLBWIF_FLAGS = 32
class HLBWINFO(Structure):
    cbSize: UInt32
    grfHLBWIF: UInt32
    rcFramePos: Windows.Win32.Foundation.RECT
    rcDocPos: Windows.Win32.Foundation.RECT
    hltbinfo: Windows.Win32.UI.Shell.HLTBINFO
HLFNAMEF = UInt32
HLFNAMEF_DEFAULT: HLFNAMEF = 0
HLFNAMEF_TRYCACHE: HLFNAMEF = 1
HLFNAMEF_TRYPRETTYTARGET: HLFNAMEF = 2
HLFNAMEF_TRYFULLTARGET: HLFNAMEF = 4
HLFNAMEF_TRYWIN95SHORTCUT: HLFNAMEF = 8
HLID_INFO = UInt32
HLID_INVALID: HLID_INFO = 0
HLID_PREVIOUS: HLID_INFO = 4294967295
HLID_NEXT: HLID_INFO = 4294967294
HLID_CURRENT: HLID_INFO = 4294967293
HLID_STACKBOTTOM: HLID_INFO = 4294967292
HLID_STACKTOP: HLID_INFO = 4294967291
HLINKGETREF = Int32
HLINKGETREF_DEFAULT: HLINKGETREF = 0
HLINKGETREF_ABSOLUTE: HLINKGETREF = 1
HLINKGETREF_RELATIVE: HLINKGETREF = 2
HLINKMISC = Int32
HLINKMISC_RELATIVE: HLINKMISC = 1
HLINKSETF = Int32
HLINKSETF_TARGET: HLINKSETF = 1
HLINKSETF_LOCATION: HLINKSETF = 2
HLINKWHICHMK = Int32
HLINKWHICHMK_CONTAINER: HLINKWHICHMK = 1
HLINKWHICHMK_BASE: HLINKWHICHMK = 2
class HLITEM(Structure):
    uHLID: UInt32
    pwzFriendlyName: Windows.Win32.Foundation.PWSTR
HLNF = UInt32
HLNF_INTERNALJUMP: HLNF = 1
HLNF_OPENINNEWWINDOW: HLNF = 2
HLNF_NAVIGATINGBACK: HLNF = 4
HLNF_NAVIGATINGFORWARD: HLNF = 8
HLNF_NAVIGATINGTOSTACKITEM: HLNF = 16
HLNF_CREATENOHISTORY: HLNF = 32
HLQF_INFO = Int32
HLQF_ISVALID: HLQF_INFO = 1
HLQF_ISCURRENT: HLQF_INFO = 2
HLSHORTCUTF = Int32
HLSHORTCUTF_DEFAULT: HLSHORTCUTF = 0
HLSHORTCUTF_DONTACTUALLYCREATE: HLSHORTCUTF = 1
HLSHORTCUTF_USEFILENAMEFROMFRIENDLYNAME: HLSHORTCUTF = 2
HLSHORTCUTF_USEUNIQUEFILENAME: HLSHORTCUTF = 4
HLSHORTCUTF_MAYUSEEXISTINGSHORTCUT: HLSHORTCUTF = 8
HLSR = Int32
HLSR_HOME: HLSR = 0
HLSR_SEARCHPAGE: HLSR = 1
HLSR_HISTORYFOLDER: HLSR = 2
class HLTBINFO(Structure):
    uDockType: UInt32
    rcTbPos: Windows.Win32.Foundation.RECT
HLTB_INFO = Int32
HLTB_DOCKEDLEFT: HLTB_INFO = 0
HLTB_DOCKEDTOP: HLTB_INFO = 1
HLTB_DOCKEDRIGHT: HLTB_INFO = 2
HLTB_DOCKEDBOTTOM: HLTB_INFO = 3
HLTB_FLOATING: HLTB_INFO = 4
HLTRANSLATEF = Int32
HLTRANSLATEF_DEFAULT: HLTRANSLATEF = 0
HLTRANSLATEF_DONTAPPLYDEFAULTPREFIX: HLTRANSLATEF = 1
HOMEGROUPSHARINGCHOICES = Int32
HGSC_NONE: HOMEGROUPSHARINGCHOICES = 0
HGSC_MUSICLIBRARY: HOMEGROUPSHARINGCHOICES = 1
HGSC_PICTURESLIBRARY: HOMEGROUPSHARINGCHOICES = 2
HGSC_VIDEOSLIBRARY: HOMEGROUPSHARINGCHOICES = 4
HGSC_DOCUMENTSLIBRARY: HOMEGROUPSHARINGCHOICES = 8
HGSC_PRINTERS: HOMEGROUPSHARINGCHOICES = 16
HPSXA = IntPtr
HideInputPaneAnimationCoordinator = Guid('384742b1-2a77-4cb3-8c-f8-11-36-f5-e1-7e-59')
HomeGroup = Guid('de77ba04-3c92-4d11-a1-a5-42-35-2a-53-e0-e3')
class IACList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('77a130b0-94fd-11d0-a5-44-00-c0-4f-d7-d0-62')
    @commethod(3)
    def Expand(pszExpand: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IACList2(c_void_p):
    extends: Windows.Win32.UI.Shell.IACList
    Guid = Guid('470141a0-5186-11d2-bb-b6-00-60-97-7b-46-4c')
    @commethod(4)
    def SetOptions(dwFlag: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOptions(pdwFlag: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAccessibilityDockingService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8849dc22-cedf-4c95-99-8d-05-14-19-dd-3f-76')
    @commethod(3)
    def GetAvailableSize(hMonitor: Windows.Win32.Graphics.Gdi.HMONITOR, pcxFixed: POINTER(UInt32), pcyMax: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DockWindow(hwnd: Windows.Win32.Foundation.HWND, hMonitor: Windows.Win32.Graphics.Gdi.HMONITOR, cyRequested: UInt32, pCallback: Windows.Win32.UI.Shell.IAccessibilityDockingServiceCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UndockWindow(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class IAccessibilityDockingServiceCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('157733fd-a592-42e5-b5-94-24-84-68-c5-a8-1b')
    @commethod(3)
    def Undocked(undockReason: Windows.Win32.UI.Shell.UNDOCK_REASON) -> Windows.Win32.Foundation.HRESULT: ...
class IAccessibleObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('95a391c5-9ed4-4c28-84-01-ab-9e-06-71-9e-11')
    @commethod(3)
    def SetAccessibleName(pszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IActionProgress(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('49ff1173-eadc-446d-92-85-15-64-53-a6-43-1c')
    @commethod(3)
    def Begin(action: Windows.Win32.UI.Shell.SPACTION, flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateProgress(ulCompleted: UInt64, ulTotal: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateText(sptext: Windows.Win32.UI.Shell.SPTEXT, pszText: Windows.Win32.Foundation.PWSTR, fMayCompact: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryCancel(pfCancelled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResetCancel() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def End() -> Windows.Win32.Foundation.HRESULT: ...
class IActionProgressDialog(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('49ff1172-eadc-446d-92-85-15-64-53-a6-43-1c')
    @commethod(3)
    def Initialize(flags: UInt32, pszTitle: Windows.Win32.Foundation.PWSTR, pszCancel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop() -> Windows.Win32.Foundation.HRESULT: ...
class IAppActivationUIInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('abad189d-9fa3-4278-b3-ca-8c-a4-48-a8-8d-cb')
    @commethod(3)
    def GetMonitor(value: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInvokePoint(value: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetShowCommand(value: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetShowUI(value: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetKeyState(value: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppPublisher(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('07250a10-9cf9-11d1-90-76-00-60-08-05-93-82')
    @commethod(3)
    def GetNumberOfCategories(pdwCat: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategories(pAppCategoryList: POINTER(Windows.Win32.UI.Shell.APPCATEGORYINFOLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberOfApps(pdwApps: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumApps(pAppCategoryId: POINTER(Guid), ppepa: POINTER(Windows.Win32.UI.Shell.IEnumPublishedApps_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAppVisibility(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2246ea2d-caea-4444-a3-c4-6d-e8-27-e4-43-13')
    @commethod(3)
    def GetAppVisibilityOnMonitor(hMonitor: Windows.Win32.Graphics.Gdi.HMONITOR, pMode: POINTER(Windows.Win32.UI.Shell.MONITOR_APP_VISIBILITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsLauncherVisible(pfVisible: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Advise(pCallback: Windows.Win32.UI.Shell.IAppVisibilityEvents_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unadvise(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IAppVisibilityEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6584ce6b-7d82-49c2-89-c9-c6-bc-02-ba-8c-38')
    @commethod(3)
    def AppVisibilityOnMonitorChanged(hMonitor: Windows.Win32.Graphics.Gdi.HMONITOR, previousMode: Windows.Win32.UI.Shell.MONITOR_APP_VISIBILITY, currentMode: Windows.Win32.UI.Shell.MONITOR_APP_VISIBILITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LauncherVisibilityChange(currentVisibleState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IApplicationActivationManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2e941141-7f97-4756-ba-1d-9d-ec-de-89-4a-3d')
    @commethod(3)
    def ActivateApplication(appUserModelId: Windows.Win32.Foundation.PWSTR, arguments: Windows.Win32.Foundation.PWSTR, options: Windows.Win32.UI.Shell.ACTIVATEOPTIONS, processId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ActivateForFile(appUserModelId: Windows.Win32.Foundation.PWSTR, itemArray: Windows.Win32.UI.Shell.IShellItemArray_head, verb: Windows.Win32.Foundation.PWSTR, processId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ActivateForProtocol(appUserModelId: Windows.Win32.Foundation.PWSTR, itemArray: Windows.Win32.UI.Shell.IShellItemArray_head, processId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IApplicationAssociationRegistration(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4e530b0a-e611-4c77-a3-ac-90-31-d0-22-28-1b')
    @commethod(3)
    def QueryCurrentDefault(pszQuery: Windows.Win32.Foundation.PWSTR, atQueryType: Windows.Win32.UI.Shell.ASSOCIATIONTYPE, alQueryLevel: Windows.Win32.UI.Shell.ASSOCIATIONLEVEL, ppszAssociation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryAppIsDefault(pszQuery: Windows.Win32.Foundation.PWSTR, atQueryType: Windows.Win32.UI.Shell.ASSOCIATIONTYPE, alQueryLevel: Windows.Win32.UI.Shell.ASSOCIATIONLEVEL, pszAppRegistryName: Windows.Win32.Foundation.PWSTR, pfDefault: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryAppIsDefaultAll(alQueryLevel: Windows.Win32.UI.Shell.ASSOCIATIONLEVEL, pszAppRegistryName: Windows.Win32.Foundation.PWSTR, pfDefault: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAppAsDefault(pszAppRegistryName: Windows.Win32.Foundation.PWSTR, pszSet: Windows.Win32.Foundation.PWSTR, atSetType: Windows.Win32.UI.Shell.ASSOCIATIONTYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAppAsDefaultAll(pszAppRegistryName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ClearUserAssociations() -> Windows.Win32.Foundation.HRESULT: ...
class IApplicationAssociationRegistrationUI(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1f76a169-f994-40ac-8f-c8-09-59-e8-87-47-10')
    @commethod(3)
    def LaunchAdvancedAssociationUI(pszAppRegistryName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IApplicationDesignModeSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2a3dee9a-e31d-46d6-85-08-bc-c5-97-db-35-57')
    @commethod(3)
    def SetNativeDisplaySize(nativeDisplaySizePixels: Windows.Win32.Foundation.SIZE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetScaleFactor(scaleFactor: Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetApplicationViewState(viewState: Windows.Win32.UI.Shell.APPLICATION_VIEW_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ComputeApplicationSize(applicationSizePixels: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsApplicationViewStateSupported(viewState: Windows.Win32.UI.Shell.APPLICATION_VIEW_STATE, nativeDisplaySizePixels: Windows.Win32.Foundation.SIZE, scaleFactor: Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR, supported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def TriggerEdgeGesture(edgeGestureKind: Windows.Win32.UI.Shell.EDGE_GESTURE_KIND) -> Windows.Win32.Foundation.HRESULT: ...
class IApplicationDesignModeSettings2(c_void_p):
    extends: Windows.Win32.UI.Shell.IApplicationDesignModeSettings
    Guid = Guid('490514e1-675a-4d6e-a5-8d-e5-49-01-b4-ca-2f')
    @commethod(9)
    def SetNativeDisplayOrientation(nativeDisplayOrientation: Windows.Win32.UI.Shell.NATIVE_DISPLAY_ORIENTATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetApplicationViewOrientation(viewOrientation: Windows.Win32.UI.Shell.APPLICATION_VIEW_ORIENTATION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetAdjacentDisplayEdges(adjacentDisplayEdges: Windows.Win32.UI.Shell.ADJACENT_DISPLAY_EDGES) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetIsOnLockScreen(isOnLockScreen: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetApplicationViewMinWidth(viewMinWidth: Windows.Win32.UI.Shell.APPLICATION_VIEW_MIN_WIDTH) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetApplicationSizeBounds(minApplicationSizePixels: POINTER(Windows.Win32.Foundation.SIZE_head), maxApplicationSizePixels: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetApplicationViewOrientation(applicationSizePixels: Windows.Win32.Foundation.SIZE, viewOrientation: POINTER(Windows.Win32.UI.Shell.APPLICATION_VIEW_ORIENTATION)) -> Windows.Win32.Foundation.HRESULT: ...
class IApplicationDestinations(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('12337d35-94c6-48a0-bc-e7-6a-9c-69-d4-d6-00')
    @commethod(3)
    def SetAppID(pszAppID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveDestination(punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAllDestinations() -> Windows.Win32.Foundation.HRESULT: ...
class IApplicationDocumentLists(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3c594f9f-9f30-47a1-97-9a-c9-e8-3d-3d-0a-06')
    @commethod(3)
    def SetAppID(pszAppID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetList(listtype: Windows.Win32.UI.Shell.APPDOCLISTTYPE, cItemsDesired: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IAssocHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f04061ac-1659-4a3f-a9-54-77-5a-a5-7f-c0-83')
    @commethod(3)
    def GetName(ppsz: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUIName(ppsz: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetIconLocation(ppszPath: POINTER(Windows.Win32.Foundation.PWSTR), pIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsRecommended() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def MakeDefault(pszDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Invoke(pdo: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateInvoker(pdo: Windows.Win32.System.Com.IDataObject_head, ppInvoker: POINTER(Windows.Win32.UI.Shell.IAssocHandlerInvoker_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAssocHandlerInvoker(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('92218cab-ecaa-4335-81-33-80-7f-d2-34-c2-ee')
    @commethod(3)
    def SupportsSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Invoke() -> Windows.Win32.Foundation.HRESULT: ...
class IAttachmentExecute(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('73db1241-1e85-4581-8e-4f-a8-1e-1d-0f-8c-57')
    @commethod(3)
    def SetClientTitle(pszTitle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetClientGuid(guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetLocalPath(pszLocalPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFileName(pszFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSource(pszSource: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetReferrer(pszReferrer: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CheckPolicy() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Prompt(hwnd: Windows.Win32.Foundation.HWND, prompt: Windows.Win32.UI.Shell.ATTACHMENT_PROMPT, paction: POINTER(Windows.Win32.UI.Shell.ATTACHMENT_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Save() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Execute(hwnd: Windows.Win32.Foundation.HWND, pszVerb: Windows.Win32.Foundation.PWSTR, phProcess: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveWithUI(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ClearClientState() -> Windows.Win32.Foundation.HRESULT: ...
class IAutoComplete(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00bb2762-6a77-11d0-a5-35-00-c0-4f-d7-d0-62')
    @commethod(3)
    def Init(hwndEdit: Windows.Win32.Foundation.HWND, punkACL: Windows.Win32.System.Com.IUnknown_head, pwszRegKeyPath: Windows.Win32.Foundation.PWSTR, pwszQuickComplete: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Enable(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IAutoComplete2(c_void_p):
    extends: Windows.Win32.UI.Shell.IAutoComplete
    Guid = Guid('eac04bc0-3791-11d2-bb-95-00-60-97-7b-46-4c')
    @commethod(5)
    def SetOptions(dwFlag: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOptions(pdwFlag: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAutoCompleteDropDown(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3cd141f4-3c6a-11d2-bc-aa-00-c0-4f-d9-29-db')
    @commethod(3)
    def GetDropDownStatus(pdwFlags: POINTER(UInt32), ppwszString: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResetEnumerator() -> Windows.Win32.Foundation.HRESULT: ...
class IBandHost(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b9075c7c-d48e-403f-ab-99-d6-c7-7a-10-84-ac')
    @commethod(3)
    def CreateBand(rclsidBand: POINTER(Guid), fAvailable: Windows.Win32.Foundation.BOOL, fVisible: Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBandAvailability(rclsidBand: POINTER(Guid), fAvailable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DestroyBand(rclsidBand: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IBandSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4cf504b0-de96-11d0-8b-3f-00-a0-c9-11-e8-e5')
    @commethod(3)
    def AddBand(punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumBands(uBand: UInt32, pdwBandID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryBand(dwBandID: UInt32, ppstb: POINTER(Windows.Win32.UI.Shell.IDeskBand_head), pdwState: POINTER(UInt32), pszName: Windows.Win32.Foundation.PWSTR, cchName: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetBandState(dwBandID: UInt32, dwMask: UInt32, dwState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveBand(dwBandID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBandObject(dwBandID: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBandSiteInfo(pbsinfo: POINTER(Windows.Win32.UI.Shell.BANDSITEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBandSiteInfo(pbsinfo: POINTER(Windows.Win32.UI.Shell.BANDSITEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBannerNotificationHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8d7b2ba7-db05-46a8-82-3c-d2-b6-de-08-ee-91')
    @commethod(3)
    def OnBannerEvent(notification: POINTER(Windows.Win32.UI.Shell.BANNER_NOTIFICATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBanneredBar(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('596a9a94-013e-11d1-8d-34-00-a0-c9-0f-27-19')
    @commethod(3)
    def SetIconSize(iIcon: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIconSize(piIcon: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetBitmap(hBitmap: Windows.Win32.Graphics.Gdi.HBITMAP) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBitmap(phBitmap: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Windows.Win32.Foundation.HRESULT: ...
class IBrowserFrameOptions(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('10df43c8-1dbe-11d3-8b-34-00-60-97-df-5b-d4')
    @commethod(3)
    def GetFrameOptions(dwMask: UInt32, pdwOptions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IBrowserService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('02ba3b52-0547-11d1-b8-33-00-c0-4f-c9-b3-1f')
    @commethod(3)
    def GetParentSite(ppipsite: POINTER(Windows.Win32.System.Ole.IOleInPlaceSite_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTitle(psv: Windows.Win32.UI.Shell.IShellView_head, pszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTitle(psv: Windows.Win32.UI.Shell.IShellView_head, pszName: Windows.Win32.Foundation.PWSTR, cchName: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOleObject(ppobjv: POINTER(Windows.Win32.System.Ole.IOleObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTravelLog(pptl: POINTER(Windows.Win32.UI.Shell.ITravelLog_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ShowControlWindow(id: UInt32, fShow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsControlWindowShown(id: UInt32, pfShown: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IEGetDisplayName(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pwszName: Windows.Win32.Foundation.PWSTR, uFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IEParseDisplayName(uiCP: UInt32, pwszPath: Windows.Win32.Foundation.PWSTR, ppidlOut: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DisplayParseError(hres: Windows.Win32.Foundation.HRESULT, pwszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def NavigateToPidl(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), grfHLNF: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetNavigateState(bnstate: Windows.Win32.UI.Shell.BNSTATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetNavigateState(pbnstate: POINTER(Windows.Win32.UI.Shell.BNSTATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def NotifyRedirect(psv: Windows.Win32.UI.Shell.IShellView_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pfDidBrowse: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def UpdateWindowList() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def UpdateBackForwardState() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFlags(dwFlags: UInt32, dwFlagMask: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetFlags(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CanNavigateNow() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetPidl(ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetReferrer(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetBrowserIndex() -> UInt32: ...
    @commethod(25)
    def GetBrowserByIndex(dwID: UInt32, ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetHistoryObject(ppole: POINTER(Windows.Win32.System.Ole.IOleObject_head), pstm: POINTER(Windows.Win32.System.Com.IStream_head), ppbc: POINTER(Windows.Win32.System.Com.IBindCtx_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetHistoryObject(pole: Windows.Win32.System.Ole.IOleObject_head, fIsLocalAnchor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CacheOLEServer(pole: Windows.Win32.System.Ole.IOleObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetSetCodePage(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarOut: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def OnHttpEquiv(psv: Windows.Win32.UI.Shell.IShellView_head, fDone: Windows.Win32.Foundation.BOOL, pvarargIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarargOut: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetPalette(hpal: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def RegisterWindow(fForceRegister: Windows.Win32.Foundation.BOOL, swc: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IBrowserService2(c_void_p):
    extends: Windows.Win32.UI.Shell.IBrowserService
    Guid = Guid('68bd21cc-438b-11d2-a5-60-00-a0-c9-2d-bf-e8')
    @commethod(33)
    def WndProcBS(hwnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
    @commethod(34)
    def SetAsDefFolderSettings() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetViewRect(prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def OnSize(wParam: Windows.Win32.Foundation.WPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def OnCreate(pcs: POINTER(Windows.Win32.UI.WindowsAndMessaging.CREATESTRUCTW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def OnCommand(wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
    @commethod(39)
    def OnDestroy() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def OnNotify(pnm: POINTER(Windows.Win32.UI.Controls.NMHDR_head)) -> Windows.Win32.Foundation.LRESULT: ...
    @commethod(41)
    def OnSetFocus() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def OnFrameWindowActivateBS(fActive: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def ReleaseShellView() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def ActivatePendingView() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def CreateViewWindow(psvNew: Windows.Win32.UI.Shell.IShellView_head, psvOld: Windows.Win32.UI.Shell.IShellView_head, prcView: POINTER(Windows.Win32.Foundation.RECT_head), phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def CreateBrowserPropSheetExt(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetViewWindow(phwndView: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetBaseBrowserData(pbbd: POINTER(POINTER(Windows.Win32.UI.Shell.BASEBROWSERDATALH_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def PutBaseBrowserData() -> POINTER(Windows.Win32.UI.Shell.BASEBROWSERDATALH_head): ...
    @commethod(50)
    def InitializeTravelLog(ptl: Windows.Win32.UI.Shell.ITravelLog_head, dw: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def SetTopBrowser() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def Offline(iCmd: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def AllowViewResize(f: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SetActivateState(u: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def UpdateSecureLockIcon(eSecureLock: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def InitializeDownloadManager() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def InitializeTransitionSite() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def _Initialize(hwnd: Windows.Win32.Foundation.HWND, pauto: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def _CancelPendingNavigationAsync() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def _CancelPendingView() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def _MaySaveChanges() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def _PauseOrResumeView(fPaused: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def _DisableModeless() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def _NavigateToPidl2(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), grfHLNF: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def _TryShell2Rename(psv: Windows.Win32.UI.Shell.IShellView_head, pidlNew: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def _SwitchActivationNow() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def _ExecChildren(punkBar: Windows.Win32.System.Com.IUnknown_head, fBroadcast: Windows.Win32.Foundation.BOOL, pguidCmdGroup: POINTER(Guid), nCmdID: UInt32, nCmdexecopt: UInt32, pvarargIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarargOut: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def _SendChildren(hwndBar: Windows.Win32.Foundation.HWND, fBroadcast: Windows.Win32.Foundation.BOOL, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetFolderSetData(pfsd: POINTER(Windows.Win32.UI.Shell.FOLDERSETDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def _OnFocusChange(itb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def v_ShowHideChildWindows(fChildOnly: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def _get_itbLastFocus() -> UInt32: ...
    @commethod(73)
    def _put_itbLastFocus(itbLastFocus: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def _UIActivateView(uState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def _GetViewBorderRect(prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def _UpdateViewRectSize() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def _ResizeNextBorder(itb: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def _ResizeView() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def _GetEffectiveClientArea(lprectBorder: POINTER(Windows.Win32.Foundation.RECT_head), hmon: Windows.Win32.Graphics.Gdi.HMONITOR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def v_GetViewStream(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), grfMode: UInt32, pwszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.System.Com.IStream_head: ...
    @commethod(81)
    def ForwardViewMsg(uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
    @commethod(82)
    def SetAcceleratorMenu(hacc: Windows.Win32.UI.WindowsAndMessaging.HACCEL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def _GetToolbarCount() -> Int32: ...
    @commethod(84)
    def _GetToolbarItem(itb: Int32) -> POINTER(Windows.Win32.UI.Shell.TOOLBARITEM_head): ...
    @commethod(85)
    def _SaveToolbars(pstm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def _LoadToolbars(pstm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def _CloseAndReleaseToolbars(fClose: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def v_MayGetNextToolbarFocus(lpMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), itbNext: UInt32, citb: Int32, pptbi: POINTER(POINTER(Windows.Win32.UI.Shell.TOOLBARITEM_head)), phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def _ResizeNextBorderHelper(itb: UInt32, bUseHmonitor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def _FindTBar(punkSrc: Windows.Win32.System.Com.IUnknown_head) -> UInt32: ...
    @commethod(91)
    def _SetFocus(ptbi: POINTER(Windows.Win32.UI.Shell.TOOLBARITEM_head), hwnd: Windows.Win32.Foundation.HWND, lpMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def v_MayTranslateAccelerator(pmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def _GetBorderDWHelper(punkSrc: Windows.Win32.System.Com.IUnknown_head, lprectBorder: POINTER(Windows.Win32.Foundation.RECT_head), bUseHmonitor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def v_CheckZoneCrossing(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IBrowserService3(c_void_p):
    extends: Windows.Win32.UI.Shell.IBrowserService2
    Guid = Guid('27d7ce21-762d-48f3-86-f3-40-e2-fd-37-49-c4')
    @commethod(95)
    def _PositionViewWindow(hwnd: Windows.Win32.Foundation.HWND, prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def IEParseDisplayNameEx(uiCP: UInt32, pwszPath: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppidlOut: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IBrowserService4(c_void_p):
    extends: Windows.Win32.UI.Shell.IBrowserService3
    Guid = Guid('639f1bff-e135-4096-ab-d8-e0-f5-04-d6-49-a4')
    @commethod(97)
    def ActivateView(fPendingView: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def SaveViewState() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def _ResizeAllBorders() -> Windows.Win32.Foundation.HRESULT: ...
class ICDBurn(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3d73a659-e5d0-4d42-af-c0-51-21-ba-42-5c-8d')
    @commethod(3)
    def GetRecorderDriveLetter(pszDrive: Windows.Win32.Foundation.PWSTR, cch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Burn(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HasRecordableDrive(pfHasRecorder: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ICDBurnExt(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2271dcca-74fc-4414-8f-b7-c5-6b-05-ac-e2-d7')
    @commethod(3)
    def GetSupportedActionTypes(pdwActions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ICategorizer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a3b14589-9174-49a8-89-a3-06-a1-ae-2b-9b-a7')
    @commethod(3)
    def GetDescription(pszDesc: Windows.Win32.Foundation.PWSTR, cch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategory(cidl: UInt32, apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), rgCategoryIds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCategoryInfo(dwCategoryId: UInt32, pci: POINTER(Windows.Win32.UI.Shell.CATEGORY_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CompareCategory(csfFlags: Windows.Win32.UI.Shell.CATSORT_FLAGS, dwCategoryId1: UInt32, dwCategoryId2: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ICategoryProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9af64809-5864-4c26-a7-20-c1-f7-8c-08-6e-e3')
    @commethod(3)
    def CanCategorizeOnSCID(pscid: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultCategory(pguid: POINTER(Guid), pscid: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCategoryForSCID(pscid: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumCategories(penum: POINTER(Windows.Win32.System.Com.IEnumGUID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCategoryName(pguid: POINTER(Guid), pszName: Windows.Win32.Foundation.PWSTR, cch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateCategory(pguid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IColumnManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d8ec27bb-3f3b-4042-b1-0a-4a-cf-d9-24-d4-53')
    @commethod(3)
    def SetColumnInfo(propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pcmci: POINTER(Windows.Win32.UI.Shell.CM_COLUMNINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnInfo(propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pcmci: POINTER(Windows.Win32.UI.Shell.CM_COLUMNINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetColumnCount(dwFlags: Windows.Win32.UI.Shell.CM_ENUM_FLAGS, puCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumns(dwFlags: Windows.Win32.UI.Shell.CM_ENUM_FLAGS, rgkeyOrder: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), cColumns: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColumns(rgkeyOrder: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), cVisible: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IColumnProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e8025004-1c42-11d2-be-2c-00-a0-c9-a8-3d-a1')
    @commethod(3)
    def Initialize(psci: POINTER(Windows.Win32.UI.Shell.SHCOLUMNINIT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnInfo(dwIndex: UInt32, psci: POINTER(Windows.Win32.UI.Shell.SHCOLUMNINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetItemData(pscid: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pscd: POINTER(Windows.Win32.UI.Shell.SHCOLUMNDATA_head), pvarData: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICommDlgBrowser(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214f1-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def OnDefaultCommand(ppshv: Windows.Win32.UI.Shell.IShellView_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStateChange(ppshv: Windows.Win32.UI.Shell.IShellView_head, uChange: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IncludeObject(ppshv: Windows.Win32.UI.Shell.IShellView_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICommDlgBrowser2(c_void_p):
    extends: Windows.Win32.UI.Shell.ICommDlgBrowser
    Guid = Guid('10339516-2894-11d2-90-39-00-c0-4f-8e-eb-3e')
    @commethod(6)
    def Notify(ppshv: Windows.Win32.UI.Shell.IShellView_head, dwNotifyType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultMenuText(ppshv: Windows.Win32.UI.Shell.IShellView_head, pszText: Windows.Win32.Foundation.PWSTR, cchMax: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetViewFlags(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ICommDlgBrowser3(c_void_p):
    extends: Windows.Win32.UI.Shell.ICommDlgBrowser2
    Guid = Guid('c8ad25a1-3294-41ee-81-65-71-17-4b-d0-1c-57')
    @commethod(9)
    def OnColumnClicked(ppshv: Windows.Win32.UI.Shell.IShellView_head, iColumn: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentFilter(pszFileSpec: Windows.Win32.Foundation.PWSTR, cchFileSpec: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnPreViewCreated(ppshv: Windows.Win32.UI.Shell.IShellView_head) -> Windows.Win32.Foundation.HRESULT: ...
class IComputerInfoChangeNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0df60d92-6818-46d6-b3-58-d6-61-70-dd-e4-66')
    @commethod(3)
    def ComputerInfoChanged() -> Windows.Win32.Foundation.HRESULT: ...
class IConnectableCredentialProviderCredential(c_void_p):
    extends: Windows.Win32.UI.Shell.ICredentialProviderCredential
    Guid = Guid('9387928b-ac75-4bf9-8a-b2-2b-93-c4-a5-52-90')
    @commethod(20)
    def Connect(pqcws: Windows.Win32.UI.Shell.IQueryContinueWithStatus_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Disconnect() -> Windows.Win32.Foundation.HRESULT: ...
class IContactManagerInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('99eacba7-e073-43b6-a8-96-55-af-e4-8a-08-33')
    @commethod(3)
    def ShowContactCardForWindow(appWindow: Windows.Win32.Foundation.HWND, contact: Windows.Win32.System.Com.IUnknown_head, selection: POINTER(Windows.Win32.Foundation.RECT_head), preferredPlacement: Windows.Win32.UI.Shell.FLYOUT_PLACEMENT) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenu(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214e4-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def QueryContextMenu(hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, indexMenu: UInt32, idCmdFirst: UInt32, idCmdLast: UInt32, uFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeCommand(pici: POINTER(Windows.Win32.UI.Shell.CMINVOKECOMMANDINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCommandString(idCmd: UIntPtr, uType: UInt32, pReserved: POINTER(UInt32), pszName: Windows.Win32.Foundation.PSTR, cchMax: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenu2(c_void_p):
    extends: Windows.Win32.UI.Shell.IContextMenu
    Guid = Guid('000214f4-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(6)
    def HandleMenuMsg(uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenu3(c_void_p):
    extends: Windows.Win32.UI.Shell.IContextMenu2
    Guid = Guid('bcfce0a0-ec17-11d0-8d-10-00-a0-c9-0f-27-19')
    @commethod(7)
    def HandleMenuMsg2(uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenuCB(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3409e930-5a39-11d1-83-fa-00-a0-c9-0d-c8-49')
    @commethod(3)
    def CallBack(psf: Windows.Win32.UI.Shell.IShellFolder_head, hwndOwner: Windows.Win32.Foundation.HWND, pdtobj: Windows.Win32.System.Com.IDataObject_head, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenuSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0811aebe-0b87-4c54-9e-72-54-8c-f6-49-01-6b')
    @commethod(3)
    def DoContextMenuPopup(punkContextMenu: Windows.Win32.System.Com.IUnknown_head, fFlags: UInt32, pt: Windows.Win32.Foundation.POINT) -> Windows.Win32.Foundation.HRESULT: ...
class ICopyHookA(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214ef-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def CopyCallback(hwnd: Windows.Win32.Foundation.HWND, wFunc: UInt32, wFlags: UInt32, pszSrcFile: Windows.Win32.Foundation.PSTR, dwSrcAttribs: UInt32, pszDestFile: Windows.Win32.Foundation.PSTR, dwDestAttribs: UInt32) -> UInt32: ...
class ICopyHookW(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214fc-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def CopyCallback(hwnd: Windows.Win32.Foundation.HWND, wFunc: UInt32, wFlags: UInt32, pszSrcFile: Windows.Win32.Foundation.PWSTR, dwSrcAttribs: UInt32, pszDestFile: Windows.Win32.Foundation.PWSTR, dwDestAttribs: UInt32) -> UInt32: ...
class ICreateProcessInputs(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f6ef6140-e26f-4d82-ba-c4-e9-ba-5f-d2-39-a8')
    @commethod(3)
    def GetCreateFlags(pdwCreationFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCreateFlags(dwCreationFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddCreateFlags(dwCreationFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHotKey(wHotKey: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddStartupFlags(dwStartupInfoFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTitle(pszTitle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetEnvironmentVariable(pszName: Windows.Win32.Foundation.PWSTR, pszValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICreatingProcess(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c2b937a9-3110-4398-8a-56-f3-4c-63-42-d2-44')
    @commethod(3)
    def OnCreating(pcpi: Windows.Win32.UI.Shell.ICreateProcessInputs_head) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d27c3481-5a1c-45b2-8a-aa-c2-0e-bb-e8-22-9e')
    @commethod(3)
    def SetUsageScenario(cpus: Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSerialization(pcpcs: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Advise(pcpe: Windows.Win32.UI.Shell.ICredentialProviderEvents_head, upAdviseContext: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnAdvise() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFieldDescriptorCount(pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFieldDescriptorAt(dwIndex: UInt32, ppcpfd: POINTER(POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCredentialCount(pdwCount: POINTER(UInt32), pdwDefault: POINTER(UInt32), pbAutoLogonWithDefault: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCredentialAt(dwIndex: UInt32, ppcpc: POINTER(Windows.Win32.UI.Shell.ICredentialProviderCredential_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredential(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('63913a93-40c1-481a-81-8d-40-72-ff-8c-70-cc')
    @commethod(3)
    def Advise(pcpce: Windows.Win32.UI.Shell.ICredentialProviderCredentialEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnAdvise() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSelected(pbAutoLogon: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetDeselected() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFieldState(dwFieldID: UInt32, pcpfs: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_STATE), pcpfis: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStringValue(dwFieldID: UInt32, ppsz: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetBitmapValue(dwFieldID: UInt32, phbmp: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCheckboxValue(dwFieldID: UInt32, pbChecked: POINTER(Windows.Win32.Foundation.BOOL), ppszLabel: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSubmitButtonValue(dwFieldID: UInt32, pdwAdjacentTo: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetComboBoxValueCount(dwFieldID: UInt32, pcItems: POINTER(UInt32), pdwSelectedItem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetComboBoxValueAt(dwFieldID: UInt32, dwItem: UInt32, ppszItem: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetStringValue(dwFieldID: UInt32, psz: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetCheckboxValue(dwFieldID: UInt32, bChecked: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetComboBoxSelectedValue(dwFieldID: UInt32, dwSelectedItem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CommandLinkClicked(dwFieldID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSerialization(pcpgsr: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE), pcpcs: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION_head), ppszOptionalStatusText: POINTER(Windows.Win32.Foundation.PWSTR), pcpsiOptionalStatusIcon: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_STATUS_ICON)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ReportResult(ntsStatus: Windows.Win32.Foundation.NTSTATUS, ntsSubstatus: Windows.Win32.Foundation.NTSTATUS, ppszOptionalStatusText: POINTER(Windows.Win32.Foundation.PWSTR), pcpsiOptionalStatusIcon: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_STATUS_ICON)) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredential2(c_void_p):
    extends: Windows.Win32.UI.Shell.ICredentialProviderCredential
    Guid = Guid('fd672c54-40ea-4d6e-9b-49-cf-b1-a7-50-7b-d7')
    @commethod(20)
    def GetUserSid(sid: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredentialEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fa6fa76b-66b7-4b11-95-f1-86-17-11-18-e8-16')
    @commethod(3)
    def SetFieldState(pcpc: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, dwFieldID: UInt32, cpfs: Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFieldInteractiveState(pcpc: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, dwFieldID: UInt32, cpfis: Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFieldString(pcpc: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, dwFieldID: UInt32, psz: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFieldCheckbox(pcpc: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, dwFieldID: UInt32, bChecked: Windows.Win32.Foundation.BOOL, pszLabel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFieldBitmap(pcpc: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, dwFieldID: UInt32, hbmp: Windows.Win32.Graphics.Gdi.HBITMAP) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFieldComboBoxSelectedItem(pcpc: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, dwFieldID: UInt32, dwSelectedItem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteFieldComboBoxItem(pcpc: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, dwFieldID: UInt32, dwItem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AppendFieldComboBoxItem(pcpc: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, dwFieldID: UInt32, pszItem: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetFieldSubmitButton(pcpc: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, dwFieldID: UInt32, dwAdjacentTo: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnCreatingWindow(phwndOwner: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredentialEvents2(c_void_p):
    extends: Windows.Win32.UI.Shell.ICredentialProviderCredentialEvents
    Guid = Guid('b53c00b6-9922-4b78-b1-f4-dd-fe-77-4d-c3-9b')
    @commethod(13)
    def BeginFieldUpdates() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EndFieldUpdates() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetFieldOptions(credential: Windows.Win32.UI.Shell.ICredentialProviderCredential_head, fieldID: UInt32, options: Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredentialWithFieldOptions(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dbc6fb30-c843-49e3-a6-45-57-3e-6f-39-44-6a')
    @commethod(3)
    def GetFieldOptions(fieldID: UInt32, options: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS)) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('34201e5a-a787-41a3-a5-a4-bd-6d-cf-2a-85-4e')
    @commethod(3)
    def CredentialsChanged(upAdviseContext: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a5da53f9-d475-4080-a1-20-91-0c-4a-73-98-80')
    @commethod(3)
    def Filter(cpus: Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO, dwFlags: UInt32, rgclsidProviders: POINTER(Guid), rgbAllow: POINTER(Windows.Win32.Foundation.BOOL), cProviders: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateRemoteCredential(pcpcsIn: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION_head), pcpcsOut: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderSetUserArray(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('095c1484-1c0c-4388-9c-6d-50-0e-61-bf-84-bd')
    @commethod(3)
    def SetUserArray(users: Windows.Win32.UI.Shell.ICredentialProviderUserArray_head) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderUser(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('13793285-3ea6-40fd-b4-20-15-f4-7d-a4-1f-bb')
    @commethod(3)
    def GetSid(sid: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProviderID(providerID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringValue(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), stringValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetValue(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), value: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderUserArray(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('90c119ae-0f18-4520-a1-f1-11-43-66-a4-0f-e8')
    @commethod(3)
    def SetProviderFilter(guidProviderToFilterTo: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAccountOptions(credentialProviderAccountOptions: POINTER(Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCount(userCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAt(userIndex: UInt32, user: POINTER(Windows.Win32.UI.Shell.ICredentialProviderUser_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICurrentItem(c_void_p):
    extends: Windows.Win32.UI.Shell.IRelatedItem
    Guid = Guid('240a7174-d653-4a1d-a6-d3-d4-94-3c-fb-fe-3d')
class ICurrentWorkingDirectory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('91956d21-9276-11d1-92-1a-00-60-97-df-5b-d4')
    @commethod(3)
    def GetDirectory(pwzPath: Windows.Win32.Foundation.PWSTR, cchSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDirectory(pwzPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICustomDestinationList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6332debf-87b5-4670-90-c0-5e-57-b4-08-a4-9e')
    @commethod(3)
    def SetAppID(pszAppID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginList(pcMinSlots: POINTER(UInt32), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AppendCategory(pszCategory: Windows.Win32.Foundation.PWSTR, poa: Windows.Win32.UI.Shell.Common.IObjectArray_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AppendKnownCategory(category: Windows.Win32.UI.Shell.KNOWNDESTCATEGORY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddUserTasks(poa: Windows.Win32.UI.Shell.Common.IObjectArray_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CommitList() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRemovedDestinations(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteList(pszAppID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AbortList() -> Windows.Win32.Foundation.HRESULT: ...
class IDataObjectAsyncCapability(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3d8b0590-f691-11d2-8e-a9-00-60-97-df-5b-d4')
    @commethod(3)
    def SetAsyncMode(fDoOpAsync: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAsyncMode(pfIsOpAsync: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StartOperation(pbcReserved: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InOperation(pfInAsyncOp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EndOperation(hResult: Windows.Win32.Foundation.HRESULT, pbcReserved: Windows.Win32.System.Com.IBindCtx_head, dwEffects: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDataObjectProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3d25f6d6-4b2a-433c-91-84-7c-33-ad-35-d0-01')
    @commethod(3)
    def GetDataObject(dataObject: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDataObject(dataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDataTransferManagerInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3a3dcd6c-3eab-43dc-bc-de-45-67-1c-e8-00-c8')
    @commethod(3)
    def GetForWindow(appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), dataTransferManager: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowShareUIForWindow(appWindow: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class IDefaultExtractIconInit(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('41ded17d-d6b3-4261-99-7d-88-c6-0e-4b-1d-58')
    @commethod(3)
    def SetFlags(uFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetKey(hkey: Windows.Win32.System.Registry.HKEY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNormalIcon(pszFile: Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetOpenIcon(pszFile: Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetShortcutIcon(pszFile: Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDefaultIcon(pszFile: Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IDefaultFolderMenuInitialize(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7690aa79-f8fc-4615-a3-27-36-f7-d1-8f-5d-91')
    @commethod(3)
    def Initialize(hwnd: Windows.Win32.Foundation.HWND, pcmcb: Windows.Win32.UI.Shell.IContextMenuCB_head, pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), psf: Windows.Win32.UI.Shell.IShellFolder_head, cidl: UInt32, apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), punkAssociation: Windows.Win32.System.Com.IUnknown_head, cKeys: UInt32, aKeys: POINTER(Windows.Win32.System.Registry.HKEY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMenuRestrictions(dfmrValues: Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMenuRestrictions(dfmrMask: Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS, pdfmrValues: POINTER(Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHandlerClsid(rclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IDelegateFolder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('add8ba80-002b-11d0-8f-0f-00-c0-4f-d7-d0-62')
    @commethod(3)
    def SetItemAlloc(pmalloc: Windows.Win32.System.Com.IMalloc_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDelegateItem(c_void_p):
    extends: Windows.Win32.UI.Shell.IRelatedItem
    Guid = Guid('3c5a1c94-c951-4cb7-bb-6d-3b-93-f3-0c-ce-93')
class IDeskBand(c_void_p):
    extends: Windows.Win32.UI.Shell.IDockingWindow
    Guid = Guid('eb0fe172-1a3a-11d0-89-b3-00-a0-c9-0a-90-ac')
    @commethod(8)
    def GetBandInfo(dwBandID: UInt32, dwViewMode: UInt32, pdbi: POINTER(Windows.Win32.UI.Shell.DESKBANDINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDeskBand2(c_void_p):
    extends: Windows.Win32.UI.Shell.IDeskBand
    Guid = Guid('79d16de4-abee-4021-8d-9d-91-69-b2-61-d6-57')
    @commethod(9)
    def CanRenderComposited(pfCanRenderComposited: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCompositionState(fCompositionEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCompositionState(pfCompositionEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IDeskBandInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('77e425fc-cbf9-4307-ba-6a-bb-57-27-74-56-61')
    @commethod(3)
    def GetDefaultBandWidth(dwBandID: UInt32, dwViewMode: UInt32, pnWidth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDeskBar(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('eb0fe173-1a3a-11d0-89-b3-00-a0-c9-0a-90-ac')
    @commethod(5)
    def SetClient(punkClient: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClient(ppunkClient: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnPosRectChangeDB(prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDeskBarClient(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('eb0fe175-1a3a-11d0-89-b3-00-a0-c9-0a-90-ac')
    @commethod(5)
    def SetDeskBarSite(punkSite: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetModeDBC(dwMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UIActivateDBC(dwState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSize(dwWhich: UInt32, prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDesktopGadget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c1646bc4-f298-4f91-a2-04-eb-2d-d1-70-9d-1a')
    @commethod(3)
    def RunGadget(gadgetPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IDesktopWallpaper(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b92b56a9-8b55-4e14-9a-89-01-99-bb-b6-f9-3b')
    @commethod(3)
    def SetWallpaper(monitorID: Windows.Win32.Foundation.PWSTR, wallpaper: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWallpaper(monitorID: Windows.Win32.Foundation.PWSTR, wallpaper: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMonitorDevicePathAt(monitorIndex: UInt32, monitorID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMonitorDevicePathCount(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMonitorRECT(monitorID: Windows.Win32.Foundation.PWSTR, displayRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetBackgroundColor(color: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetBackgroundColor(color: POINTER(Windows.Win32.Foundation.COLORREF)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetPosition(position: Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPosition(position: POINTER(Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetSlideshow(items: Windows.Win32.UI.Shell.IShellItemArray_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSlideshow(items: POINTER(Windows.Win32.UI.Shell.IShellItemArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSlideshowOptions(options: Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_OPTIONS, slideshowTick: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetSlideshowOptions(options: POINTER(Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_OPTIONS), slideshowTick: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AdvanceSlideshow(monitorID: Windows.Win32.Foundation.PWSTR, direction: Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_DIRECTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetStatus(state: POINTER(Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Enable(enable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IDestinationStreamFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8a87781b-39a7-4a1f-aa-b3-a3-9b-9c-34-a7-d9')
    @commethod(3)
    def GetDestinationStream(ppstm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDisplayItem(c_void_p):
    extends: Windows.Win32.UI.Shell.IRelatedItem
    Guid = Guid('c6fd5997-9f6b-4888-87-03-94-e8-0e-8c-de-3f')
class IDocViewSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('87d605e0-c511-11cf-89-a9-00-a0-c9-05-41-29')
    @commethod(3)
    def OnSetTitle(pvTitle: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDockingWindow(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('012dd920-7b26-11d0-8c-a9-00-a0-c9-2d-bf-e8')
    @commethod(5)
    def ShowDW(fShow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CloseDW(dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResizeBorderDW(prcBorder: POINTER(Windows.Win32.Foundation.RECT_head), punkToolbarSite: Windows.Win32.System.Com.IUnknown_head, fReserved: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IDockingWindowFrame(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('47d2657a-7b27-11d0-8c-a9-00-a0-c9-2d-bf-e8')
    @commethod(5)
    def AddToolbar(punkSrc: Windows.Win32.System.Com.IUnknown_head, pwszItem: Windows.Win32.Foundation.PWSTR, dwAddFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveToolbar(punkSrc: Windows.Win32.System.Com.IUnknown_head, dwRemoveFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindToolbar(pwszItem: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDockingWindowSite(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('2a342fc2-7b26-11d0-8c-a9-00-a0-c9-2d-bf-e8')
    @commethod(5)
    def GetBorderDW(punkObj: Windows.Win32.System.Com.IUnknown_head, prcBorder: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RequestBorderSpaceDW(punkObj: Windows.Win32.System.Com.IUnknown_head, pbw: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetBorderSpaceDW(punkObj: Windows.Win32.System.Com.IUnknown_head, pbw: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDragSourceHelper(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('de5bf786-477a-11d2-83-9d-00-c0-4f-d9-18-d0')
    @commethod(3)
    def InitializeFromBitmap(pshdi: POINTER(Windows.Win32.UI.Shell.SHDRAGIMAGE_head), pDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeFromWindow(hwnd: Windows.Win32.Foundation.HWND, ppt: POINTER(Windows.Win32.Foundation.POINT_head), pDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDragSourceHelper2(c_void_p):
    extends: Windows.Win32.UI.Shell.IDragSourceHelper
    Guid = Guid('83e07d0d-0c5f-4163-bf-1a-60-b2-74-05-1e-40')
    @commethod(5)
    def SetFlags(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDropTargetHelper(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4657278b-411b-11d2-83-9a-00-c0-4f-d9-18-d0')
    @commethod(3)
    def DragEnter(hwndTarget: Windows.Win32.Foundation.HWND, pDataObject: Windows.Win32.System.Com.IDataObject_head, ppt: POINTER(Windows.Win32.Foundation.POINT_head), dwEffect: Windows.Win32.System.Ole.DROPEFFECT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DragLeave() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DragOver(ppt: POINTER(Windows.Win32.Foundation.POINT_head), dwEffect: Windows.Win32.System.Ole.DROPEFFECT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Drop(pDataObject: Windows.Win32.System.Com.IDataObject_head, ppt: POINTER(Windows.Win32.Foundation.POINT_head), dwEffect: Windows.Win32.System.Ole.DROPEFFECT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Show(fShow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IDynamicHWHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dc2601d7-059e-42fc-a0-9d-2a-fd-21-b6-d5-f7')
    @commethod(3)
    def GetDynamicInfo(pszDeviceID: Windows.Win32.Foundation.PWSTR, dwContentType: UInt32, ppszAction: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
IENamespaceTreeControl = Guid('ace52d03-e5cd-4b20-82-ff-e7-1b-11-be-ae-1d')
IEPDNFLAGS = Int32
IEPDN_BINDINGUI: IEPDNFLAGS = 1
IESHORTCUTFLAGS = Int32
IESHORTCUT_NEWBROWSER: IESHORTCUTFLAGS = 1
IESHORTCUT_OPENNEWTAB: IESHORTCUTFLAGS = 2
IESHORTCUT_FORCENAVIGATE: IESHORTCUTFLAGS = 4
IESHORTCUT_BACKGROUNDTAB: IESHORTCUTFLAGS = 8
class IEnumACString(c_void_p):
    extends: Windows.Win32.System.Com.IEnumString
    Guid = Guid('8e74c210-cf9d-4eaf-a4-03-73-56-42-8f-0a-5a')
    @commethod(7)
    def NextItem(pszUrl: Windows.Win32.Foundation.PWSTR, cchMax: UInt32, pulSortIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetEnumOptions(dwOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEnumOptions(pdwOptions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumAssocHandlers(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('973810ae-9599-4b88-9e-4d-6e-e9-8c-95-52-da')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.UI.Shell.IAssocHandler_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumExplorerCommand(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a88826f8-186f-4987-aa-de-ea-0c-ef-8f-bf-e8')
    @commethod(3)
    def Next(celt: UInt32, pUICommand: POINTER(Windows.Win32.UI.Shell.IExplorerCommand_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumExplorerCommand_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumExtraSearch(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0e700be1-9db6-11d1-a1-ce-00-c0-4f-d7-5d-13')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.UI.Shell.EXTRASEARCH_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumExtraSearch_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumFullIDList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d0191542-7954-4908-bc-06-b2-36-0b-be-45-ba')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumFullIDList_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumHLITEM(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9c6-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.UI.Shell.HLITEM_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppienumhlitem: POINTER(Windows.Win32.UI.Shell.IEnumHLITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumIDList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214f2-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumIDList_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumObjects(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2c1c7e2e-2d0e-4059-83-1e-1e-6f-82-33-5c-2e')
    @commethod(3)
    def Next(celt: UInt32, riid: POINTER(Guid), rgelt: POINTER(c_void_p), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumObjects_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumPublishedApps(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0b124f8c-91f0-11d1-b8-b5-00-60-08-05-93-82')
    @commethod(3)
    def Next(pia: POINTER(Windows.Win32.UI.Shell.IPublishedApp_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
class IEnumReadyCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('61e00d45-8fff-4e60-92-4e-65-37-b6-16-12-dd')
    @commethod(3)
    def EnumReady() -> Windows.Win32.Foundation.HRESULT: ...
class IEnumResources(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2dd81fe3-a83c-4da9-a3-30-47-24-9d-34-5b-a1')
    @commethod(3)
    def Next(celt: UInt32, psir: POINTER(Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenumr: POINTER(Windows.Win32.UI.Shell.IEnumResources_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumShellItems(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('70629033-e363-4a28-a5-67-0d-b7-80-06-e6-d7')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.UI.Shell.IShellItem_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumShellItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncMgrConflict(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('82705914-dda3-4893-ba-99-49-de-6c-8c-80-36')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.UI.Shell.ISyncMgrConflict_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumSyncMgrConflict_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncMgrEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c81a1d4e-8cf7-4683-80-e0-bc-ae-88-d6-77-b6')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.UI.Shell.ISyncMgrEvent_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumSyncMgrEvents_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncMgrSyncItems(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('54b3abf3-f085-4181-b5-46-e2-9c-40-3c-72-6b')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.UI.Shell.ISyncMgrSyncItem_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumSyncMgrSyncItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumTravelLogEntry(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7ebfdd85-ad18-11d3-a4-c5-00-c0-4f-72-d6-b8')
    @commethod(3)
    def Next(cElt: UInt32, rgElt: POINTER(Windows.Win32.UI.Shell.ITravelLogEntry_head), pcEltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cElt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(Windows.Win32.UI.Shell.IEnumTravelLogEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumerableView(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8c8bf236-1aec-495f-98-94-91-d5-7c-3c-68-6f')
    @commethod(3)
    def SetEnumReadyCallback(percb: Windows.Win32.UI.Shell.IEnumReadyCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateEnumIDListFromContents(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), dwEnumFlags: UInt32, ppEnumIDList: POINTER(Windows.Win32.UI.Shell.IEnumIDList_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IExecuteCommand(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7f9185b0-cb92-43c5-80-a9-92-27-7a-4f-7b-54')
    @commethod(3)
    def SetKeyState(grfKeyState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetParameters(pszParameters: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPosition(pt: Windows.Win32.Foundation.POINT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetShowWindow(nShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetNoShowUI(fNoShowUI: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDirectory(pszDirectory: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Execute() -> Windows.Win32.Foundation.HRESULT: ...
class IExecuteCommandApplicationHostEnvironment(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('18b21aa9-e184-4ff0-9f-5e-f8-82-d0-37-71-b3')
    @commethod(3)
    def GetValue(pahe: POINTER(Windows.Win32.UI.Shell.AHE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IExecuteCommandHost(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4b6832a2-5f04-4c9d-b8-9d-72-7a-15-d1-03-e7')
    @commethod(3)
    def GetUIMode(pUIMode: POINTER(Windows.Win32.UI.Shell.EC_HOST_UI_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
class IExpDispSupport(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0d7d1d00-6fc0-11d0-a9-74-00-c0-4f-d7-05-a2')
    @commethod(3)
    def FindConnectionPoint(riid: POINTER(Guid), ppccp: POINTER(Windows.Win32.System.Com.IConnectionPoint_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTranslateAccelerator(pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), grfModifiers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnInvoke(dispidMember: Int32, iid: POINTER(Guid), lcid: UInt32, wFlags: UInt16, pdispparams: POINTER(Windows.Win32.System.Com.DISPPARAMS_head), pVarResult: POINTER(Windows.Win32.System.Com.VARIANT_head), pexcepinfo: POINTER(Windows.Win32.System.Com.EXCEPINFO_head), puArgErr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IExpDispSupportXP(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2f0dd58c-f789-4f14-99-fb-92-93-b3-c9-c2-12')
    @commethod(3)
    def FindCIE4ConnectionPoint(riid: POINTER(Guid), ppccp: POINTER(Windows.Win32.UI.Shell.CIE4ConnectionPoint_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTranslateAccelerator(pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), grfModifiers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnInvoke(dispidMember: Int32, iid: POINTER(Guid), lcid: UInt32, wFlags: UInt16, pdispparams: POINTER(Windows.Win32.System.Com.DISPPARAMS_head), pVarResult: POINTER(Windows.Win32.System.Com.VARIANT_head), pexcepinfo: POINTER(Windows.Win32.System.Com.EXCEPINFO_head), puArgErr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IExplorerBrowser(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dfd3b6b5-c10c-4be9-85-f6-a6-69-69-f4-02-f6')
    @commethod(3)
    def Initialize(hwndParent: Windows.Win32.Foundation.HWND, prc: POINTER(Windows.Win32.Foundation.RECT_head), pfs: POINTER(Windows.Win32.UI.Shell.FOLDERSETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Destroy() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetRect(phdwp: POINTER(Windows.Win32.UI.WindowsAndMessaging.HDWP), rcBrowser: Windows.Win32.Foundation.RECT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPropertyBag(pszPropertyBag: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetEmptyText(pszEmptyText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFolderSettings(pfs: POINTER(Windows.Win32.UI.Shell.FOLDERSETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Advise(psbe: Windows.Win32.UI.Shell.IExplorerBrowserEvents_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Unadvise(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetOptions(dwFlag: Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetOptions(pdwFlag: POINTER(Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def BrowseToIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), uFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def BrowseToObject(punk: Windows.Win32.System.Com.IUnknown_head, uFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def FillFromObject(punk: Windows.Win32.System.Com.IUnknown_head, dwFlags: Windows.Win32.UI.Shell.EXPLORER_BROWSER_FILL_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemoveAll() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCurrentView(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IExplorerBrowserEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('361bbdc7-e6ee-4e13-be-58-58-e2-24-0c-81-0f')
    @commethod(3)
    def OnNavigationPending(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnViewCreated(psv: Windows.Win32.UI.Shell.IShellView_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnNavigationComplete(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnNavigationFailed(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IExplorerCommand(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a08ce4d0-fa25-44ab-b5-7c-c7-b1-c3-23-e0-b9')
    @commethod(3)
    def GetTitle(psiItemArray: Windows.Win32.UI.Shell.IShellItemArray_head, ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIcon(psiItemArray: Windows.Win32.UI.Shell.IShellItemArray_head, ppszIcon: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetToolTip(psiItemArray: Windows.Win32.UI.Shell.IShellItemArray_head, ppszInfotip: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCanonicalName(pguidCommandName: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetState(psiItemArray: Windows.Win32.UI.Shell.IShellItemArray_head, fOkToBeSlow: Windows.Win32.Foundation.BOOL, pCmdState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Invoke(psiItemArray: Windows.Win32.UI.Shell.IShellItemArray_head, pbc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFlags(pFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumSubCommands(ppEnum: POINTER(Windows.Win32.UI.Shell.IEnumExplorerCommand_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IExplorerCommandProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('64961751-0835-43c0-8f-fe-d5-76-86-53-0e-64')
    @commethod(3)
    def GetCommands(punkSite: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCommand(rguidCommandId: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IExplorerCommandState(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bddacb60-7657-47ae-84-45-d2-3e-1a-cf-82-ae')
    @commethod(3)
    def GetState(psiItemArray: Windows.Win32.UI.Shell.IShellItemArray_head, fOkToBeSlow: Windows.Win32.Foundation.BOOL, pCmdState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IExplorerPaneVisibility(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e07010ec-bc17-44c0-97-b0-46-c7-c9-5b-9e-dc')
    @commethod(3)
    def GetPaneState(ep: POINTER(Guid), peps: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IExtensionServices(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9cb-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def SetAdditionalHeaders(pwzAdditionalHeaders: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAuthenticateData(phwnd: Windows.Win32.Foundation.HWND, pwzUsername: Windows.Win32.Foundation.PWSTR, pwzPassword: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IExtractIconA(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214eb-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetIconLocation(uFlags: UInt32, pszIconFile: Windows.Win32.Foundation.PSTR, cchMax: UInt32, piIndex: POINTER(Int32), pwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Extract(pszFile: Windows.Win32.Foundation.PSTR, nIconIndex: UInt32, phiconLarge: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), nIconSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IExtractIconW(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214fa-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetIconLocation(uFlags: UInt32, pszIconFile: Windows.Win32.Foundation.PWSTR, cchMax: UInt32, piIndex: POINTER(Int32), pwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Extract(pszFile: Windows.Win32.Foundation.PWSTR, nIconIndex: UInt32, phiconLarge: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON), nIconSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IExtractImage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bb2e617c-0920-11d1-9a-0b-00-c0-4f-c2-d6-c1')
    @commethod(3)
    def GetLocation(pszPathBuffer: Windows.Win32.Foundation.PWSTR, cch: UInt32, pdwPriority: POINTER(UInt32), prgSize: POINTER(Windows.Win32.Foundation.SIZE_head), dwRecClrDepth: UInt32, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Extract(phBmpThumbnail: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Windows.Win32.Foundation.HRESULT: ...
class IExtractImage2(c_void_p):
    extends: Windows.Win32.UI.Shell.IExtractImage
    Guid = Guid('953bb1ee-93b4-11d1-98-a3-00-c0-4f-b6-87-da')
    @commethod(5)
    def GetDateStamp(pDateStamp: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFileDialog(c_void_p):
    extends: Windows.Win32.UI.Shell.IModalWindow
    Guid = Guid('42f85136-db7e-439c-85-f1-e4-07-5d-13-5f-c8')
    @commethod(4)
    def SetFileTypes(cFileTypes: UInt32, rgFilterSpec: POINTER(Windows.Win32.UI.Shell.Common.COMDLG_FILTERSPEC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFileTypeIndex(iFileType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFileTypeIndex(piFileType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Advise(pfde: Windows.Win32.UI.Shell.IFileDialogEvents_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Unadvise(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOptions(fos: Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetOptions(pfos: POINTER(Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDefaultFolder(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetFolder(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFolder(ppsi: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCurrentSelection(ppsi: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetFileName(pszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetFileName(pszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTitle(pszTitle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetOkButtonLabel(pszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFileNameLabel(pszLabel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetResult(ppsi: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddPlace(psi: Windows.Win32.UI.Shell.IShellItem_head, fdap: Windows.Win32.UI.Shell.FDAP) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetDefaultExtension(pszDefaultExtension: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Close(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetClientGuid(guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ClearClientData() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetFilter(pFilter: Windows.Win32.UI.Shell.IShellItemFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFileDialog2(c_void_p):
    extends: Windows.Win32.UI.Shell.IFileDialog
    Guid = Guid('61744fc7-85b5-4791-a9-b0-27-22-76-30-9b-13')
    @commethod(27)
    def SetCancelButtonLabel(pszLabel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetNavigationRoot(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFileDialogControlEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('36116642-d713-4b97-9b-83-74-84-a9-d0-04-33')
    @commethod(3)
    def OnItemSelected(pfdc: Windows.Win32.UI.Shell.IFileDialogCustomize_head, dwIDCtl: UInt32, dwIDItem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnButtonClicked(pfdc: Windows.Win32.UI.Shell.IFileDialogCustomize_head, dwIDCtl: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnCheckButtonToggled(pfdc: Windows.Win32.UI.Shell.IFileDialogCustomize_head, dwIDCtl: UInt32, bChecked: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnControlActivating(pfdc: Windows.Win32.UI.Shell.IFileDialogCustomize_head, dwIDCtl: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IFileDialogCustomize(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e6fdd21a-163f-4975-9c-8c-a6-9f-1b-a3-70-34')
    @commethod(3)
    def EnableOpenDropDown(dwIDCtl: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddMenu(dwIDCtl: UInt32, pszLabel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddPushButton(dwIDCtl: UInt32, pszLabel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddComboBox(dwIDCtl: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddRadioButtonList(dwIDCtl: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddCheckButton(dwIDCtl: UInt32, pszLabel: Windows.Win32.Foundation.PWSTR, bChecked: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddEditBox(dwIDCtl: UInt32, pszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddSeparator(dwIDCtl: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddText(dwIDCtl: UInt32, pszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetControlLabel(dwIDCtl: UInt32, pszLabel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetControlState(dwIDCtl: UInt32, pdwState: POINTER(Windows.Win32.UI.Shell.CDCONTROLSTATEF)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetControlState(dwIDCtl: UInt32, dwState: Windows.Win32.UI.Shell.CDCONTROLSTATEF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetEditBoxText(dwIDCtl: UInt32, ppszText: POINTER(POINTER(UInt16))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetEditBoxText(dwIDCtl: UInt32, pszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCheckButtonState(dwIDCtl: UInt32, pbChecked: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetCheckButtonState(dwIDCtl: UInt32, bChecked: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddControlItem(dwIDCtl: UInt32, dwIDItem: UInt32, pszLabel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RemoveControlItem(dwIDCtl: UInt32, dwIDItem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def RemoveAllControlItems(dwIDCtl: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetControlItemState(dwIDCtl: UInt32, dwIDItem: UInt32, pdwState: POINTER(Windows.Win32.UI.Shell.CDCONTROLSTATEF)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetControlItemState(dwIDCtl: UInt32, dwIDItem: UInt32, dwState: Windows.Win32.UI.Shell.CDCONTROLSTATEF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetSelectedControlItem(dwIDCtl: UInt32, pdwIDItem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetSelectedControlItem(dwIDCtl: UInt32, dwIDItem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def StartVisualGroup(dwIDCtl: UInt32, pszLabel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def EndVisualGroup() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def MakeProminent(dwIDCtl: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetControlItemText(dwIDCtl: UInt32, dwIDItem: UInt32, pszLabel: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFileDialogEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('973510db-7d7f-452b-89-75-74-a8-58-28-d3-54')
    @commethod(3)
    def OnFileOk(pfd: Windows.Win32.UI.Shell.IFileDialog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnFolderChanging(pfd: Windows.Win32.UI.Shell.IFileDialog_head, psiFolder: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnFolderChange(pfd: Windows.Win32.UI.Shell.IFileDialog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnSelectionChange(pfd: Windows.Win32.UI.Shell.IFileDialog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnShareViolation(pfd: Windows.Win32.UI.Shell.IFileDialog_head, psi: Windows.Win32.UI.Shell.IShellItem_head, pResponse: POINTER(Windows.Win32.UI.Shell.FDE_SHAREVIOLATION_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnTypeChange(pfd: Windows.Win32.UI.Shell.IFileDialog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnOverwrite(pfd: Windows.Win32.UI.Shell.IFileDialog_head, psi: Windows.Win32.UI.Shell.IShellItem_head, pResponse: POINTER(Windows.Win32.UI.Shell.FDE_OVERWRITE_RESPONSE)) -> Windows.Win32.Foundation.HRESULT: ...
class IFileIsInUse(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('64a1cbf0-3a1a-4461-91-58-37-69-69-69-39-50')
    @commethod(3)
    def GetAppName(ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUsage(pfut: POINTER(Windows.Win32.UI.Shell.FILE_USAGE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCapabilities(pdwCapFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSwitchToHWND(phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CloseFile() -> Windows.Win32.Foundation.HRESULT: ...
class IFileOpenDialog(c_void_p):
    extends: Windows.Win32.UI.Shell.IFileDialog
    Guid = Guid('d57c7288-d4ad-4768-be-02-9d-96-95-32-d9-60')
    @commethod(27)
    def GetResults(ppenum: POINTER(Windows.Win32.UI.Shell.IShellItemArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetSelectedItems(ppsai: POINTER(Windows.Win32.UI.Shell.IShellItemArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFileOperation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('947aab5f-0a5c-4c13-b4-d6-4b-f7-83-6f-c9-f8')
    @commethod(3)
    def Advise(pfops: Windows.Win32.UI.Shell.IFileOperationProgressSink_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOperationFlags(dwOperationFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetProgressMessage(pszMessage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetProgressDialog(popd: Windows.Win32.UI.Shell.IOperationsProgressDialog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProperties(pproparray: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChangeArray_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOwnerWindow(hwndOwner: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ApplyPropertiesToItem(psiItem: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ApplyPropertiesToItems(punkItems: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RenameItem(psiItem: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR, pfopsItem: Windows.Win32.UI.Shell.IFileOperationProgressSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RenameItems(pUnkItems: Windows.Win32.System.Com.IUnknown_head, pszNewName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MoveItem(psiItem: Windows.Win32.UI.Shell.IShellItem_head, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR, pfopsItem: Windows.Win32.UI.Shell.IFileOperationProgressSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def MoveItems(punkItems: Windows.Win32.System.Com.IUnknown_head, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CopyItem(psiItem: Windows.Win32.UI.Shell.IShellItem_head, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head, pszCopyName: Windows.Win32.Foundation.PWSTR, pfopsItem: Windows.Win32.UI.Shell.IFileOperationProgressSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CopyItems(punkItems: Windows.Win32.System.Com.IUnknown_head, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteItem(psiItem: Windows.Win32.UI.Shell.IShellItem_head, pfopsItem: Windows.Win32.UI.Shell.IFileOperationProgressSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def DeleteItems(punkItems: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def NewItem(psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head, dwFileAttributes: UInt32, pszName: Windows.Win32.Foundation.PWSTR, pszTemplateName: Windows.Win32.Foundation.PWSTR, pfopsItem: Windows.Win32.UI.Shell.IFileOperationProgressSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def PerformOperations() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetAnyOperationsAborted(pfAnyOperationsAborted: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IFileOperation2(c_void_p):
    extends: Windows.Win32.UI.Shell.IFileOperation
    Guid = Guid('cd8f23c1-8f61-4916-90-9d-55-bd-d0-91-87-53')
    @commethod(23)
    def SetOperationFlags2(operationFlags2: Windows.Win32.UI.Shell.FILE_OPERATION_FLAGS2) -> Windows.Win32.Foundation.HRESULT: ...
class IFileOperationProgressSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('04b0f1a7-9490-44bc-96-e1-42-96-a3-12-52-e2')
    @commethod(3)
    def StartOperations() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FinishOperations(hrResult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PreRenameItem(dwFlags: UInt32, psiItem: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PostRenameItem(dwFlags: UInt32, psiItem: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR, hrRename: Windows.Win32.Foundation.HRESULT, psiNewlyCreated: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PreMoveItem(dwFlags: UInt32, psiItem: Windows.Win32.UI.Shell.IShellItem_head, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PostMoveItem(dwFlags: UInt32, psiItem: Windows.Win32.UI.Shell.IShellItem_head, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR, hrMove: Windows.Win32.Foundation.HRESULT, psiNewlyCreated: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PreCopyItem(dwFlags: UInt32, psiItem: Windows.Win32.UI.Shell.IShellItem_head, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PostCopyItem(dwFlags: UInt32, psiItem: Windows.Win32.UI.Shell.IShellItem_head, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR, hrCopy: Windows.Win32.Foundation.HRESULT, psiNewlyCreated: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def PreDeleteItem(dwFlags: UInt32, psiItem: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def PostDeleteItem(dwFlags: UInt32, psiItem: Windows.Win32.UI.Shell.IShellItem_head, hrDelete: Windows.Win32.Foundation.HRESULT, psiNewlyCreated: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PreNewItem(dwFlags: UInt32, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PostNewItem(dwFlags: UInt32, psiDestinationFolder: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR, pszTemplateName: Windows.Win32.Foundation.PWSTR, dwFileAttributes: UInt32, hrNew: Windows.Win32.Foundation.HRESULT, psiNewItem: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UpdateProgress(iWorkTotal: UInt32, iWorkSoFar: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ResetTimer() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def PauseTimer() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ResumeTimer() -> Windows.Win32.Foundation.HRESULT: ...
class IFileSaveDialog(c_void_p):
    extends: Windows.Win32.UI.Shell.IFileDialog
    Guid = Guid('84bccd23-5fde-4cdb-ae-a4-af-64-b8-3d-78-ab')
    @commethod(27)
    def SetSaveAsItem(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetProperties(pStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetCollectedProperties(pList: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescriptionList_head, fAppendDefault: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetProperties(ppStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ApplyProperties(psi: Windows.Win32.UI.Shell.IShellItem_head, pStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head, hwnd: Windows.Win32.Foundation.HWND, pSink: Windows.Win32.UI.Shell.IFileOperationProgressSink_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFileSearchBand(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2d91eea1-9932-11d2-be-86-00-a0-c9-a8-3d-a1')
    @commethod(7)
    def SetFocus() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSearchParameters(pbstrSearchID: POINTER(Windows.Win32.Foundation.BSTR), bNavToResults: Windows.Win32.Foundation.VARIANT_BOOL, pvarScope: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarQueryFile: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SearchID(pbstrSearchID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Scope(pvarScope: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_QueryFile(pvarFile: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFileSyncMergeHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d97b5aac-c792-433c-97-5d-35-c4-ea-dc-7a-9d')
    @commethod(3)
    def Merge(localFilePath: Windows.Win32.Foundation.PWSTR, serverFilePath: Windows.Win32.Foundation.PWSTR, updateStatus: POINTER(Windows.Win32.UI.Shell.MERGE_UPDATE_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowResolveConflictUIAsync(localFilePath: Windows.Win32.Foundation.PWSTR, monitorToDisplayOn: Windows.Win32.Graphics.Gdi.HMONITOR) -> Windows.Win32.Foundation.HRESULT: ...
class IFileSystemBindData(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('01e18d10-4d8b-11d2-85-5d-00-60-08-05-93-67')
    @commethod(3)
    def SetFindData(pfd: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFindData(pfd: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFileSystemBindData2(c_void_p):
    extends: Windows.Win32.UI.Shell.IFileSystemBindData
    Guid = Guid('3acf075f-71db-4afa-81-f0-3f-c4-fd-f2-a5-b8')
    @commethod(5)
    def SetFileID(liFileID: Windows.Win32.Foundation.LARGE_INTEGER) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFileID(pliFileID: POINTER(Windows.Win32.Foundation.LARGE_INTEGER_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetJunctionCLSID(clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetJunctionCLSID(pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderBandPriv(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('47c01f95-e185-412c-b5-c5-4f-27-df-96-5a-ea')
    @commethod(3)
    def SetCascade(fCascade: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAccelerators(fAccelerators: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNoIcons(fNoIcons: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetNoText(fNoText: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9cc22886-dc8e-11d2-b1-d0-00-c0-4f-8e-eb-3e')
    @commethod(3)
    def ShouldShow(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidlItem: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEnumFlags(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), phwnd: POINTER(Windows.Win32.Foundation.HWND), pgrfFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderFilterSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c0a651f5-b48b-11d2-b5-ed-00-60-97-c6-86-f6')
    @commethod(3)
    def SetFilter(punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderView(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cde725b0-ccc9-4519-91-7e-32-5d-72-fa-b4-ce')
    @commethod(3)
    def GetCurrentViewMode(pViewMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCurrentViewMode(ViewMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFolder(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Item(iItemIndex: Int32, ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ItemCount(uFlags: UInt32, pcItems: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Items(uFlags: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSelectionMarkedItem(piItem: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFocusedItem(piItem: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetItemPosition(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSpacing(ppt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefaultSpacing(ppt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetAutoArrange() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SelectItem(iItem: Int32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SelectAndPositionItems(cidl: UInt32, apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), apt: POINTER(Windows.Win32.Foundation.POINT_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderView2(c_void_p):
    extends: Windows.Win32.UI.Shell.IFolderView
    Guid = Guid('1af3a467-214f-4298-90-8e-06-b0-3e-0b-39-f9')
    @commethod(17)
    def SetGroupBy(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), fAscending: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetGroupBy(pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pfAscending: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetViewProperty(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetViewProperty(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetTileViewProperties(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pszPropList: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetExtendedTileViewProperties(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pszPropList: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetText(iType: Windows.Win32.UI.Shell.FVTEXTTYPE, pwszText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetCurrentFolderFlags(dwMask: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetCurrentFolderFlags(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetSortColumnCount(pcColumns: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetSortColumns(rgSortColumns: POINTER(Windows.Win32.UI.Shell.SORTCOLUMN_head), cColumns: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetSortColumns(rgSortColumns: POINTER(Windows.Win32.UI.Shell.SORTCOLUMN_head), cColumns: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetItem(iItem: Int32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetVisibleItem(iStart: Int32, fPrevious: Windows.Win32.Foundation.BOOL, piItem: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetSelectedItem(iStart: Int32, piItem: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetSelection(fNoneImpliesFolder: Windows.Win32.Foundation.BOOL, ppsia: POINTER(Windows.Win32.UI.Shell.IShellItemArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetSelectionState(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def InvokeVerbOnSelection(pszVerb: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetViewModeAndIconSize(uViewMode: Windows.Win32.UI.Shell.FOLDERVIEWMODE, iImageSize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetViewModeAndIconSize(puViewMode: POINTER(Windows.Win32.UI.Shell.FOLDERVIEWMODE), piImageSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetGroupSubsetCount(cVisibleRows: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetGroupSubsetCount(pcVisibleRows: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetRedraw(fRedrawOn: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def IsMoveInSameFolder() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DoRename() -> Windows.Win32.Foundation.HRESULT: ...
class IFolderViewHost(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1ea58f02-d55a-411d-b0-9e-9e-65-ac-21-60-5b')
    @commethod(3)
    def Initialize(hwndParent: Windows.Win32.Foundation.HWND, pdo: Windows.Win32.System.Com.IDataObject_head, prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderViewOC(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('9ba05970-f6a8-11cf-a4-42-00-a0-c9-0a-8f-39')
    @commethod(7)
    def SetFolderView(pdisp: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderViewOptions(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3cc974d2-b302-4d36-ad-3e-06-d9-3f-69-5d-3f')
    @commethod(3)
    def SetFolderViewOptions(fvoMask: Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS, fvoFlags: Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFolderViewOptions(pfvoFlags: POINTER(Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS)) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderViewSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ae8c987d-8797-4ed3-be-72-2a-47-dd-93-8d-b0')
    @commethod(3)
    def GetColumnPropertyList(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGroupByProperty(pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pfGroupAscending: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetViewMode(plvm: POINTER(Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIconSize(puIconSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFolderFlags(pfolderMask: POINTER(Windows.Win32.UI.Shell.FOLDERFLAGS), pfolderFlags: POINTER(Windows.Win32.UI.Shell.FOLDERFLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSortColumns(rgSortColumns: POINTER(Windows.Win32.UI.Shell.SORTCOLUMN_head), cColumnsIn: UInt32, pcColumnsOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetGroupSubsetCount(pcVisibleRows: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFrameworkInputPane(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5752238b-24f0-495a-82-f1-2f-d5-93-05-67-96')
    @commethod(3)
    def Advise(pWindow: Windows.Win32.System.Com.IUnknown_head, pHandler: Windows.Win32.UI.Shell.IFrameworkInputPaneHandler_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AdviseWithHWND(hwnd: Windows.Win32.Foundation.HWND, pHandler: Windows.Win32.UI.Shell.IFrameworkInputPaneHandler_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Unadvise(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Location(prcInputPaneScreenLocation: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFrameworkInputPaneHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('226c537b-1e76-4d9e-a7-60-33-db-29-92-2f-18')
    @commethod(3)
    def Showing(prcInputPaneScreenLocation: POINTER(Windows.Win32.Foundation.RECT_head), fEnsureFocusedElementInView: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Hiding(fEnsureFocusedElementInView: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IGetServiceIds(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4a073526-6103-4e21-b7-bc-f5-19-d1-52-4e-5d')
    @commethod(3)
    def GetServiceIds(serviceIdCount: POINTER(UInt32), serviceIds: POINTER(POINTER(Guid))) -> Windows.Win32.Foundation.HRESULT: ...
class IHWEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c1fb73d0-ec3a-4ba2-b5-12-8c-db-91-87-b6-d1')
    @commethod(3)
    def Initialize(pszParams: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HandleEvent(pszDeviceID: Windows.Win32.Foundation.PWSTR, pszAltDeviceID: Windows.Win32.Foundation.PWSTR, pszEventType: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HandleEventWithContent(pszDeviceID: Windows.Win32.Foundation.PWSTR, pszAltDeviceID: Windows.Win32.Foundation.PWSTR, pszEventType: Windows.Win32.Foundation.PWSTR, pszContentTypeHandler: Windows.Win32.Foundation.PWSTR, pdataobject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IHWEventHandler2(c_void_p):
    extends: Windows.Win32.UI.Shell.IHWEventHandler
    Guid = Guid('cfcc809f-295d-42e8-9f-fc-42-4b-33-c4-87-e6')
    @commethod(6)
    def HandleEventWithHWND(pszDeviceID: Windows.Win32.Foundation.PWSTR, pszAltDeviceID: Windows.Win32.Foundation.PWSTR, pszEventType: Windows.Win32.Foundation.PWSTR, hwndOwner: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class IHandlerActivationHost(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('35094a87-8bb1-4237-96-c6-c4-17-ee-bd-b0-78')
    @commethod(3)
    def BeforeCoCreateInstance(clsidHandler: POINTER(Guid), itemsBeingActivated: Windows.Win32.UI.Shell.IShellItemArray_head, handlerInfo: Windows.Win32.UI.Shell.IHandlerInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeforeCreateProcess(applicationPath: Windows.Win32.Foundation.PWSTR, commandLine: Windows.Win32.Foundation.PWSTR, handlerInfo: Windows.Win32.UI.Shell.IHandlerInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
class IHandlerInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('997706ef-f880-453b-81-18-39-e1-a2-d2-65-5a')
    @commethod(3)
    def GetApplicationDisplayName(value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetApplicationPublisher(value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetApplicationIconReference(value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHandlerInfo2(c_void_p):
    extends: Windows.Win32.UI.Shell.IHandlerInfo
    Guid = Guid('31cca04c-04d3-4ea9-90-de-97-b1-5e-87-a5-32')
    @commethod(6)
    def GetApplicationId(value: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHlink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9c3-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def SetHlinkSite(pihlSite: Windows.Win32.UI.Shell.IHlinkSite_head, dwSiteData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHlinkSite(ppihlSite: POINTER(Windows.Win32.UI.Shell.IHlinkSite_head), pdwSiteData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMonikerReference(grfHLSETF: UInt32, pimkTarget: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMonikerReference(dwWhichRef: UInt32, ppimkTarget: POINTER(Windows.Win32.System.Com.IMoniker_head), ppwzLocation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetStringReference(grfHLSETF: UInt32, pwzTarget: Windows.Win32.Foundation.PWSTR, pwzLocation: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStringReference(dwWhichRef: UInt32, ppwzTarget: POINTER(Windows.Win32.Foundation.PWSTR), ppwzLocation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetFriendlyName(pwzFriendlyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFriendlyName(grfHLFNAMEF: UInt32, ppwzFriendlyName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetTargetFrameName(pwzTargetFrameName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTargetFrameName(ppwzTargetFrameName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetMiscStatus(pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Navigate(grfHLNF: UInt32, pibc: Windows.Win32.System.Com.IBindCtx_head, pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pihlbc: Windows.Win32.UI.Shell.IHlinkBrowseContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetAdditionalParams(pwzAdditionalParams: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAdditionalParams(ppwzAdditionalParams: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHlinkBrowseContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9c7-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def Register(reserved: UInt32, piunk: Windows.Win32.System.Com.IUnknown_head, pimk: Windows.Win32.System.Com.IMoniker_head, pdwRegister: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObject(pimk: Windows.Win32.System.Com.IMoniker_head, fBindIfRootRegistered: Windows.Win32.Foundation.BOOL, ppiunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Revoke(dwRegister: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetBrowseWindowInfo(phlbwi: POINTER(Windows.Win32.UI.Shell.HLBWINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBrowseWindowInfo(phlbwi: POINTER(Windows.Win32.UI.Shell.HLBWINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetInitialHlink(pimkTarget: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnNavigateHlink(grfHLNF: UInt32, pimkTarget: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR, puHLID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UpdateHlink(uHLID: UInt32, pimkTarget: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumNavigationStack(dwReserved: UInt32, grfHLFNAMEF: UInt32, ppienumhlitem: POINTER(Windows.Win32.UI.Shell.IEnumHLITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def QueryHlink(grfHLQF: UInt32, uHLID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetHlink(uHLID: UInt32, ppihl: POINTER(Windows.Win32.UI.Shell.IHlink_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetCurrentHlink(uHLID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Clone(piunkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppiunkObj: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Close(reserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IHlinkFrame(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9c5-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def SetBrowseContext(pihlbc: Windows.Win32.UI.Shell.IHlinkBrowseContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBrowseContext(ppihlbc: POINTER(Windows.Win32.UI.Shell.IHlinkBrowseContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Navigate(grfHLNF: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head, pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pihlNavigate: Windows.Win32.UI.Shell.IHlink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnNavigate(grfHLNF: UInt32, pimkTarget: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR, dwreserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateHlink(uHLID: UInt32, pimkTarget: Windows.Win32.System.Com.IMoniker_head, pwzLocation: Windows.Win32.Foundation.PWSTR, pwzFriendlyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IHlinkSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9c2-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def QueryService(dwSiteData: UInt32, guidService: POINTER(Guid), riid: POINTER(Guid), ppiunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMoniker(dwSiteData: UInt32, dwAssign: UInt32, dwWhich: UInt32, ppimk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReadyToNavigate(dwSiteData: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnNavigationComplete(dwSiteData: UInt32, dwreserved: UInt32, hrError: Windows.Win32.Foundation.HRESULT, pwzError: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IHlinkTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9c4-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def SetBrowseContext(pihlbc: Windows.Win32.UI.Shell.IHlinkBrowseContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBrowseContext(ppihlbc: POINTER(Windows.Win32.UI.Shell.IHlinkBrowseContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Navigate(grfHLNF: UInt32, pwzJumpLocation: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMoniker(pwzLocation: Windows.Win32.Foundation.PWSTR, dwAssign: UInt32, ppimkLocation: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFriendlyName(pwzLocation: Windows.Win32.Foundation.PWSTR, ppwzFriendlyName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHomeGroup(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7a3bd1d9-35a9-4fb3-a4-67-f4-8c-ac-35-e2-d0')
    @commethod(3)
    def IsMember(member: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowSharingWizard(owner: Windows.Win32.Foundation.HWND, sharingchoices: POINTER(Windows.Win32.UI.Shell.HOMEGROUPSHARINGCHOICES)) -> Windows.Win32.Foundation.HRESULT: ...
class IIOCancelInformation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f5b0bf81-8cb5-4b1b-94-49-1a-15-9e-0c-73-3c')
    @commethod(3)
    def SetCancelInformation(dwThreadID: UInt32, uMsgCancel: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCancelInformation(pdwThreadID: POINTER(UInt32), puMsgCancel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IIdentityName(c_void_p):
    extends: Windows.Win32.UI.Shell.IRelatedItem
    Guid = Guid('7d903fca-d6f9-4810-83-32-94-6c-01-77-e2-47')
class IImageRecompress(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('505f1513-6b3e-4892-a2-72-59-f8-88-9a-4d-3e')
    @commethod(3)
    def RecompressImage(psi: Windows.Win32.UI.Shell.IShellItem_head, cx: Int32, cy: Int32, iQuality: Int32, pstg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppstrmOut: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IInitializeCommand(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85075acf-231f-40ea-96-10-d2-6b-7b-58-f6-38')
    @commethod(3)
    def Initialize(pszCommandName: Windows.Win32.Foundation.PWSTR, ppb: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head) -> Windows.Win32.Foundation.HRESULT: ...
class IInitializeNetworkFolder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6e0f9881-42a8-4f2a-97-f8-8a-f4-e0-26-d9-2d')
    @commethod(3)
    def Initialize(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidlTarget: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), uDisplayType: UInt32, pszResName: Windows.Win32.Foundation.PWSTR, pszProvider: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IInitializeObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4622ad16-ff23-11d0-8d-34-00-a0-c9-0f-27-19')
    @commethod(3)
    def Initialize() -> Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithBindCtx(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('71c0d2bc-726d-45cc-a6-c0-2e-31-c1-db-21-59')
    @commethod(3)
    def Initialize(pbc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7f73be3f-fb79-493c-a6-c7-7e-e1-4e-24-58-41')
    @commethod(3)
    def Initialize(psi: Windows.Win32.UI.Shell.IShellItem_head, grfMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithPropertyStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c3e12eb5-7d8d-44f8-b6-dd-0e-77-b3-4d-6d-e4')
    @commethod(3)
    def Initialize(pps: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithWindow(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3e68d4bd-7135-4d10-80-18-9f-b6-d9-f3-3f-a1')
    @commethod(3)
    def Initialize(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class IInputObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('68284faa-6a48-11d0-8c-78-00-c0-4f-d9-18-b4')
    @commethod(3)
    def UIActivateIO(fActivate: Windows.Win32.Foundation.BOOL, pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HasFocusIO() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TranslateAcceleratorIO(pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IInputObject2(c_void_p):
    extends: Windows.Win32.UI.Shell.IInputObject
    Guid = Guid('6915c085-510b-44cd-94-af-28-df-a5-6c-f9-2b')
    @commethod(6)
    def TranslateAcceleratorGlobal(pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IInputObjectSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f1db8392-7331-11d0-8c-99-00-a0-c9-2d-bf-e8')
    @commethod(3)
    def OnFocusChangeIS(punkObj: Windows.Win32.System.Com.IUnknown_head, fSetFocus: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IInputPaneAnimationCoordinator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2af16ba9-2de5-4b75-82-d9-01-37-2a-fb-ff-b4')
    @commethod(3)
    def AddAnimation(device: Windows.Win32.System.Com.IUnknown_head, animation: Windows.Win32.Graphics.DirectComposition.IDCompositionAnimation_head) -> Windows.Win32.Foundation.HRESULT: ...
class IInputPanelConfiguration(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('41c81592-514c-48bd-a2-2e-e6-af-63-85-21-a6')
    @commethod(3)
    def EnableFocusTracking() -> Windows.Win32.Foundation.HRESULT: ...
class IInputPanelInvocationConfiguration(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a213f136-3b45-4362-a3-32-ef-b6-54-7c-d4-32')
    @commethod(3)
    def RequireTouchInEditControl() -> Windows.Win32.Foundation.HRESULT: ...
class IInsertItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d2b57227-3d23-4b95-93-c0-49-2b-d4-54-c3-56')
    @commethod(3)
    def InsertItem(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IItemNameLimits(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1df0d7f1-b267-4d28-8b-10-12-e2-32-02-a5-c4')
    @commethod(3)
    def GetValidCharacters(ppwszValidChars: POINTER(Windows.Win32.Foundation.PWSTR), ppwszInvalidChars: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMaxLength(pszName: Windows.Win32.Foundation.PWSTR, piMaxNameLen: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IKnownFolder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3aa7af7e-9b36-420c-a8-e3-f7-7d-46-74-a4-88')
    @commethod(3)
    def GetId(pkfid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategory(pCategory: POINTER(Windows.Win32.UI.Shell.KF_CATEGORY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetShellItem(dwFlags: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPath(dwFlags: UInt32, ppszPath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPath(dwFlags: UInt32, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetIDList(dwFlags: UInt32, ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFolderType(pftid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRedirectionCapabilities(pCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFolderDefinition(pKFD: POINTER(Windows.Win32.UI.Shell.KNOWNFOLDER_DEFINITION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IKnownFolderManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8be2d872-86aa-4d47-b7-76-32-cc-a4-0c-70-18')
    @commethod(3)
    def FolderIdFromCsidl(nCsidl: Int32, pfid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FolderIdToCsidl(rfid: POINTER(Guid), pnCsidl: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFolderIds(ppKFId: POINTER(POINTER(Guid)), pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFolder(rfid: POINTER(Guid), ppkf: POINTER(Windows.Win32.UI.Shell.IKnownFolder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFolderByName(pszCanonicalName: Windows.Win32.Foundation.PWSTR, ppkf: POINTER(Windows.Win32.UI.Shell.IKnownFolder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterFolder(rfid: POINTER(Guid), pKFD: POINTER(Windows.Win32.UI.Shell.KNOWNFOLDER_DEFINITION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterFolder(rfid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindFolderFromPath(pszPath: Windows.Win32.Foundation.PWSTR, mode: Windows.Win32.UI.Shell.FFFP_MODE, ppkf: POINTER(Windows.Win32.UI.Shell.IKnownFolder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindFolderFromIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppkf: POINTER(Windows.Win32.UI.Shell.IKnownFolder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Redirect(rfid: POINTER(Guid), hwnd: Windows.Win32.Foundation.HWND, flags: UInt32, pszTargetPath: Windows.Win32.Foundation.PWSTR, cFolders: UInt32, pExclusion: POINTER(Guid), ppszError: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ILaunchSourceAppUserModelId(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('989191ac-28ff-4cf0-95-84-e0-d0-78-bc-23-96')
    @commethod(3)
    def GetAppUserModelId(launchingApp: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ILaunchSourceViewSizePreference(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e5aa01f7-1fb8-4830-87-20-4e-67-34-cb-d5-f3')
    @commethod(3)
    def GetSourceViewToPosition(hwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceViewSizePreference(sourceSizeAfterLaunch: POINTER(Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE)) -> Windows.Win32.Foundation.HRESULT: ...
class ILaunchTargetMonitor(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('266fbc7e-490d-46ed-a9-6b-22-74-db-25-20-03')
    @commethod(3)
    def GetMonitor(monitor: POINTER(Windows.Win32.Graphics.Gdi.HMONITOR)) -> Windows.Win32.Foundation.HRESULT: ...
class ILaunchTargetViewSizePreference(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2f0666c6-12f7-4360-b5-11-a3-94-a0-55-37-25')
    @commethod(3)
    def GetTargetViewSizePreference(targetSizeOnLaunch: POINTER(Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE)) -> Windows.Win32.Foundation.HRESULT: ...
class ILaunchUIContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1791e8f6-21c7-4340-88-2a-a6-a9-3e-3f-d7-3b')
    @commethod(3)
    def SetAssociatedWindow(value: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTabGroupingPreference(value: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ILaunchUIContextProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0d12c4c8-a3d9-4e24-94-c1-0e-20-c5-a9-56-c4')
    @commethod(3)
    def UpdateContext(context: Windows.Win32.UI.Shell.ILaunchUIContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMenuBand(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('568804cd-cbd7-11d0-98-16-00-c0-4f-d9-19-72')
    @commethod(3)
    def IsMenuMessage(pmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TranslateMenuMessage(pmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), plRet: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IMenuPopup(c_void_p):
    extends: Windows.Win32.UI.Shell.IDeskBar
    Guid = Guid('d1e7afeb-6a2e-11d0-8c-78-00-c0-4f-d9-18-b4')
    @commethod(8)
    def Popup(ppt: POINTER(Windows.Win32.Foundation.POINTL_head), prcExclude: POINTER(Windows.Win32.Foundation.RECTL_head), dwFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnSelect(dwSelectType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSubMenu(pmp: Windows.Win32.UI.Shell.IMenuPopup_head, fSet: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IModalWindow(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b4db1657-70d7-485e-8e-3e-6f-cb-5a-5c-18-02')
    @commethod(3)
    def Show(hwndOwner: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeAccessible(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('71f312de-43ed-4190-84-77-e9-53-6b-82-35-0b')
    @commethod(3)
    def OnGetDefaultAccessibilityAction(psi: Windows.Win32.UI.Shell.IShellItem_head, pbstrDefaultAction: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDoDefaultAccessibilityAction(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnGetAccessibilityRole(psi: Windows.Win32.UI.Shell.IShellItem_head, pvarRole: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('028212a3-b627-47e9-88-56-c1-42-65-55-4e-4f')
    @commethod(3)
    def Initialize(hwndParent: Windows.Win32.Foundation.HWND, prc: POINTER(Windows.Win32.Foundation.RECT_head), nsctsFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TreeAdvise(punk: Windows.Win32.System.Com.IUnknown_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TreeUnadvise(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AppendRoot(psiRoot: Windows.Win32.UI.Shell.IShellItem_head, grfEnumFlags: UInt32, grfRootStyle: UInt32, pif: Windows.Win32.UI.Shell.IShellItemFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InsertRoot(iIndex: Int32, psiRoot: Windows.Win32.UI.Shell.IShellItem_head, grfEnumFlags: UInt32, grfRootStyle: UInt32, pif: Windows.Win32.UI.Shell.IShellItemFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveRoot(psiRoot: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveAllRoots() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRootItems(ppsiaRootItems: POINTER(Windows.Win32.UI.Shell.IShellItemArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetItemState(psi: Windows.Win32.UI.Shell.IShellItem_head, nstcisMask: UInt32, nstcisFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetItemState(psi: Windows.Win32.UI.Shell.IShellItem_head, nstcisMask: UInt32, pnstcisFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSelectedItems(psiaItems: POINTER(Windows.Win32.UI.Shell.IShellItemArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetItemCustomState(psi: Windows.Win32.UI.Shell.IShellItem_head, piStateNumber: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetItemCustomState(psi: Windows.Win32.UI.Shell.IShellItem_head, iStateNumber: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnsureItemVisible(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTheme(pszTheme: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetNextItem(psi: Windows.Win32.UI.Shell.IShellItem_head, nstcgi: Windows.Win32.UI.Shell.NSTCGNI, ppsiNext: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def HitTest(ppt: POINTER(Windows.Win32.Foundation.POINT_head), ppsiOut: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetItemRect(psi: Windows.Win32.UI.Shell.IShellItem_head, prect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CollapseAll() -> Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControl2(c_void_p):
    extends: Windows.Win32.UI.Shell.INameSpaceTreeControl
    Guid = Guid('7cc7aed8-290e-49bc-89-45-c1-40-1c-c9-30-6c')
    @commethod(22)
    def SetControlStyle(nstcsMask: UInt32, nstcsStyle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetControlStyle(nstcsMask: UInt32, pnstcsStyle: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetControlStyle2(nstcsMask: Windows.Win32.UI.Shell.NSTCSTYLE2, nstcsStyle: Windows.Win32.UI.Shell.NSTCSTYLE2) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetControlStyle2(nstcsMask: Windows.Win32.UI.Shell.NSTCSTYLE2, pnstcsStyle: POINTER(Windows.Win32.UI.Shell.NSTCSTYLE2)) -> Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControlCustomDraw(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2d3ba758-33ee-42d5-bb-7b-5f-34-31-d8-6c-78')
    @commethod(3)
    def PrePaint(hdc: Windows.Win32.Graphics.Gdi.HDC, prc: POINTER(Windows.Win32.Foundation.RECT_head), plres: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PostPaint(hdc: Windows.Win32.Graphics.Gdi.HDC, prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ItemPrePaint(hdc: Windows.Win32.Graphics.Gdi.HDC, prc: POINTER(Windows.Win32.Foundation.RECT_head), pnstccdItem: POINTER(Windows.Win32.UI.Shell.NSTCCUSTOMDRAW_head), pclrText: POINTER(Windows.Win32.Foundation.COLORREF), pclrTextBk: POINTER(Windows.Win32.Foundation.COLORREF), plres: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ItemPostPaint(hdc: Windows.Win32.Graphics.Gdi.HDC, prc: POINTER(Windows.Win32.Foundation.RECT_head), pnstccdItem: POINTER(Windows.Win32.UI.Shell.NSTCCUSTOMDRAW_head)) -> Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControlDropHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f9c665d6-c2f2-4c19-bf-33-83-22-d7-35-2f-51')
    @commethod(3)
    def OnDragEnter(psiOver: Windows.Win32.UI.Shell.IShellItem_head, psiaData: Windows.Win32.UI.Shell.IShellItemArray_head, fOutsideSource: Windows.Win32.Foundation.BOOL, grfKeyState: UInt32, pdwEffect: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDragOver(psiOver: Windows.Win32.UI.Shell.IShellItem_head, psiaData: Windows.Win32.UI.Shell.IShellItemArray_head, grfKeyState: UInt32, pdwEffect: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDragPosition(psiOver: Windows.Win32.UI.Shell.IShellItem_head, psiaData: Windows.Win32.UI.Shell.IShellItemArray_head, iNewPosition: Int32, iOldPosition: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDrop(psiOver: Windows.Win32.UI.Shell.IShellItem_head, psiaData: Windows.Win32.UI.Shell.IShellItemArray_head, iPosition: Int32, grfKeyState: UInt32, pdwEffect: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnDropPosition(psiOver: Windows.Win32.UI.Shell.IShellItem_head, psiaData: Windows.Win32.UI.Shell.IShellItemArray_head, iNewPosition: Int32, iOldPosition: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnDragLeave(psiOver: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControlEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('93d77985-b3d8-4484-83-18-67-2c-dd-a0-02-ce')
    @commethod(3)
    def OnItemClick(psi: Windows.Win32.UI.Shell.IShellItem_head, nstceHitTest: UInt32, nstceClickType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnPropertyItemCommit(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnItemStateChanging(psi: Windows.Win32.UI.Shell.IShellItem_head, nstcisMask: UInt32, nstcisState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnItemStateChanged(psi: Windows.Win32.UI.Shell.IShellItem_head, nstcisMask: UInt32, nstcisState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnSelectionChanged(psiaSelection: Windows.Win32.UI.Shell.IShellItemArray_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnKeyboardInput(uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnBeforeExpand(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnAfterExpand(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnBeginLabelEdit(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnEndLabelEdit(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnGetToolTip(psi: Windows.Win32.UI.Shell.IShellItem_head, pszTip: Windows.Win32.Foundation.PWSTR, cchTip: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnBeforeItemDelete(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnItemAdded(psi: Windows.Win32.UI.Shell.IShellItem_head, fIsRoot: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnItemDeleted(psi: Windows.Win32.UI.Shell.IShellItem_head, fIsRoot: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnBeforeContextMenu(psi: Windows.Win32.UI.Shell.IShellItem_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def OnAfterContextMenu(psi: Windows.Win32.UI.Shell.IShellItem_head, pcmIn: Windows.Win32.UI.Shell.IContextMenu_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def OnBeforeStateImageChange(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def OnGetDefaultIconIndex(psi: Windows.Win32.UI.Shell.IShellItem_head, piDefaultIcon: POINTER(Int32), piOpenIcon: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControlFolderCapabilities(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e9701183-e6b3-4ff2-85-68-81-36-15-fe-c7-be')
    @commethod(3)
    def GetFolderCapabilities(nfcMask: Windows.Win32.UI.Shell.NSTCFOLDERCAPABILITIES, pnfcValue: POINTER(Windows.Win32.UI.Shell.NSTCFOLDERCAPABILITIES)) -> Windows.Win32.Foundation.HRESULT: ...
class INamedPropertyBag(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fb700430-952c-11d1-94-6f-00-00-00-00-00-00')
    @commethod(3)
    def ReadPropertyNPB(pszBagname: Windows.Win32.Foundation.PWSTR, pszPropName: Windows.Win32.Foundation.PWSTR, pVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WritePropertyNPB(pszBagname: Windows.Win32.Foundation.PWSTR, pszPropName: Windows.Win32.Foundation.PWSTR, pVar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemovePropertyNPB(pszBagname: Windows.Win32.Foundation.PWSTR, pszPropName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class INamespaceWalk(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('57ced8a7-3f4a-432c-93-50-30-f2-44-83-f7-4f')
    @commethod(3)
    def Walk(punkToWalk: Windows.Win32.System.Com.IUnknown_head, dwFlags: UInt32, cDepth: Int32, pnswcb: Windows.Win32.UI.Shell.INamespaceWalkCB_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIDArrayResult(pcItems: POINTER(UInt32), prgpidl: POINTER(POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)))) -> Windows.Win32.Foundation.HRESULT: ...
class INamespaceWalkCB(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d92995f8-cf5e-4a76-bf-59-ea-d3-9e-a2-b9-7e')
    @commethod(3)
    def FoundItem(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnterFolder(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LeaveFolder(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitializeProgressDialog(ppszTitle: POINTER(Windows.Win32.Foundation.PWSTR), ppszCancel: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class INamespaceWalkCB2(c_void_p):
    extends: Windows.Win32.UI.Shell.INamespaceWalkCB
    Guid = Guid('7ac7492b-c38e-438a-87-db-68-73-78-44-ff-70')
    @commethod(7)
    def WalkComplete(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class INetworkFolderInternal(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ceb38218-c971-47bb-a7-03-f0-bc-99-cc-db-81')
    @commethod(3)
    def GetResourceDisplayType(displayType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIDList(idList: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProvider(itemIdCount: UInt32, itemIds: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), providerMaxLength: UInt32, provider: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class INewMenuClient(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dcb07fdc-3bb5-451c-90-be-96-66-44-fe-d7-b0')
    @commethod(3)
    def IncludeItems(pflags: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SelectAndEditItem(pidlItem: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), flags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class INewShortcutHookA(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214e1-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def SetReferent(pcszReferent: Windows.Win32.Foundation.PSTR, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReferent(pszReferent: Windows.Win32.Foundation.PSTR, cchReferent: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFolder(pcszFolder: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFolder(pszFolder: Windows.Win32.Foundation.PSTR, cchFolder: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetName(pszName: Windows.Win32.Foundation.PSTR, cchName: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExtension(pszExtension: Windows.Win32.Foundation.PSTR, cchExtension: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class INewShortcutHookW(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214f7-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def SetReferent(pcszReferent: Windows.Win32.Foundation.PWSTR, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReferent(pszReferent: Windows.Win32.Foundation.PWSTR, cchReferent: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFolder(pcszFolder: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFolder(pszFolder: Windows.Win32.Foundation.PWSTR, cchFolder: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetName(pszName: Windows.Win32.Foundation.PWSTR, cchName: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExtension(pszExtension: Windows.Win32.Foundation.PWSTR, cchExtension: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class INewWDEvents(c_void_p):
    extends: Windows.Win32.UI.Shell.IWebWizardHost
    Guid = Guid('0751c551-7568-41c9-8e-5b-e2-2e-38-91-92-36')
    @commethod(16)
    def PassportAuthenticate(bstrSignInUrl: Windows.Win32.Foundation.BSTR, pvfAuthenitcated: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class INewWindowManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d2bc4c84-3f72-4a52-a6-04-7b-cb-f3-98-2c-bb')
    @commethod(3)
    def EvaluateNewWindow(pszUrl: Windows.Win32.Foundation.PWSTR, pszName: Windows.Win32.Foundation.PWSTR, pszUrlContext: Windows.Win32.Foundation.PWSTR, pszFeatures: Windows.Win32.Foundation.PWSTR, fReplace: Windows.Win32.Foundation.BOOL, dwFlags: UInt32, dwUserActionTime: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class INotifyReplica(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('99180163-da16-101a-93-5c-44-45-53-54-00-00')
    @commethod(3)
    def YouAreAReplica(ulcOtherReplicas: UInt32, rgpmkOtherReplicas: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjMgr(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00bb2761-6a77-11d0-a5-35-00-c0-4f-d7-d0-62')
    @commethod(3)
    def Append(punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a6087428-3be3-4d73-b3-08-7c-04-a5-40-bf-1a')
    @commethod(3)
    def QueryObject(guidObject: POINTER(Guid), riid: POINTER(Guid), ppvOut: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectWithAppUserModelID(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('36db0196-9665-46d1-9b-a7-d3-70-9e-ec-f9-ed')
    @commethod(3)
    def SetAppID(pszAppID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAppID(ppszAppID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectWithBackReferences(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('321a6a6a-d61f-4bf3-97-ae-14-be-29-86-bb-36')
    @commethod(3)
    def RemoveBackReferences() -> Windows.Win32.Foundation.HRESULT: ...
class IObjectWithCancelEvent(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f279b885-0ae9-4b85-ac-06-dd-ec-f9-40-89-41')
    @commethod(3)
    def GetCancelEvent(phEvent: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectWithFolderEnumMode(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6a9d9026-0e6e-464c-b0-00-42-ec-c0-7d-e6-73')
    @commethod(3)
    def SetMode(feMode: Windows.Win32.UI.Shell.FOLDER_ENUM_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMode(pfeMode: POINTER(Windows.Win32.UI.Shell.FOLDER_ENUM_MODE)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectWithProgID(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('71e806fb-8dee-46fc-bf-8c-77-48-a8-a1-ae-13')
    @commethod(3)
    def SetProgID(pszProgID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgID(ppszProgID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectWithSelection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1c9cd5bb-98e9-4491-a6-0f-31-aa-cc-72-b8-3c')
    @commethod(3)
    def SetSelection(psia: Windows.Win32.UI.Shell.IShellItemArray_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSelection(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenControlPanel(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d11ad862-66de-4df4-bf-6c-1f-56-21-99-6a-f1')
    @commethod(3)
    def Open(pszName: Windows.Win32.Foundation.PWSTR, pszPage: Windows.Win32.Foundation.PWSTR, punkSite: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPath(pszName: Windows.Win32.Foundation.PWSTR, pszPath: Windows.Win32.Foundation.PWSTR, cchPath: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentView(pView: POINTER(Windows.Win32.UI.Shell.CPVIEW)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenSearchSource(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f0ee7333-e6fc-479b-9f-25-a8-60-c2-34-a3-8e')
    @commethod(3)
    def GetResults(hwnd: Windows.Win32.Foundation.HWND, pszQuery: Windows.Win32.Foundation.PWSTR, dwStartIndex: UInt32, dwCount: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IOperationsProgressDialog(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0c9fb851-e5c9-43eb-a3-70-f0-67-7b-13-87-4c')
    @commethod(3)
    def StartProgressDialog(hwndOwner: Windows.Win32.Foundation.HWND, flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopProgressDialog() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOperation(action: Windows.Win32.UI.Shell.SPACTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMode(mode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateProgress(ullPointsCurrent: UInt64, ullPointsTotal: UInt64, ullSizeCurrent: UInt64, ullSizeTotal: UInt64, ullItemsCurrent: UInt64, ullItemsTotal: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UpdateLocations(psiSource: Windows.Win32.UI.Shell.IShellItem_head, psiTarget: Windows.Win32.UI.Shell.IShellItem_head, psiItem: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ResetTimer() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PauseTimer() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ResumeTimer() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMilliseconds(pullElapsed: POINTER(UInt64), pullRemaining: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetOperationStatus(popstatus: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PDOPSTATUS)) -> Windows.Win32.Foundation.HRESULT: ...
class IPackageDebugSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f27c3930-8029-4ad1-94-e3-3d-ba-41-78-10-c1')
    @commethod(3)
    def EnableDebugging(packageFullName: Windows.Win32.Foundation.PWSTR, debuggerCommandLine: Windows.Win32.Foundation.PWSTR, environment: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisableDebugging(packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Suspend(packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Resume(packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def TerminateAllProcesses(packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTargetSessionId(sessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumerateBackgroundTasks(packageFullName: Windows.Win32.Foundation.PWSTR, taskCount: POINTER(UInt32), taskIds: POINTER(POINTER(Guid)), taskNames: POINTER(POINTER(Windows.Win32.Foundation.PWSTR))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ActivateBackgroundTask(taskId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def StartServicing(packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StopServicing(packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def StartSessionRedirection(packageFullName: Windows.Win32.Foundation.PWSTR, sessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def StopSessionRedirection(packageFullName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPackageExecutionState(packageFullName: Windows.Win32.Foundation.PWSTR, packageExecutionState: POINTER(Windows.Win32.UI.Shell.PACKAGE_EXECUTION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterForPackageStateChanges(packageFullName: Windows.Win32.Foundation.PWSTR, pPackageExecutionStateChangeNotification: Windows.Win32.UI.Shell.IPackageExecutionStateChangeNotification_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def UnregisterForPackageStateChanges(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IPackageDebugSettings2(c_void_p):
    extends: Windows.Win32.UI.Shell.IPackageDebugSettings
    Guid = Guid('6e3194bb-ab82-4d22-93-f5-fa-bd-a4-0e-7b-16')
    @commethod(18)
    def EnumerateApps(packageFullName: Windows.Win32.Foundation.PWSTR, appCount: POINTER(UInt32), appUserModelIds: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), appDisplayNames: POINTER(POINTER(Windows.Win32.Foundation.PWSTR))) -> Windows.Win32.Foundation.HRESULT: ...
class IPackageExecutionStateChangeNotification(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1bb12a62-2ad8-432b-8c-cf-0c-2c-52-af-cd-5b')
    @commethod(3)
    def OnStateChanged(pszPackageFullName: Windows.Win32.Foundation.PWSTR, pesNewState: Windows.Win32.UI.Shell.PACKAGE_EXECUTION_STATE) -> Windows.Win32.Foundation.HRESULT: ...
class IParentAndItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b3a4b685-b685-4805-99-d9-5d-ea-d2-87-32-36')
    @commethod(3)
    def SetParentAndItem(pidlParent: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), psf: Windows.Win32.UI.Shell.IShellFolder_head, pidlChild: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParentAndItem(ppidlParent: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), ppsf: POINTER(Windows.Win32.UI.Shell.IShellFolder_head), ppidlChild: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IParseAndCreateItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('67efed0e-e827-4408-b4-93-78-f3-98-2b-68-5c')
    @commethod(3)
    def SetItem(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistFolder(c_void_p):
    extends: Windows.Win32.System.Com.IPersist
    Guid = Guid('000214ea-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(4)
    def Initialize(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistFolder2(c_void_p):
    extends: Windows.Win32.UI.Shell.IPersistFolder
    Guid = Guid('1ac3d9f0-175c-11d1-95-be-00-60-97-97-ea-4f')
    @commethod(5)
    def GetCurFolder(ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistFolder3(c_void_p):
    extends: Windows.Win32.UI.Shell.IPersistFolder2
    Guid = Guid('cef04fdf-fe72-11d2-87-a5-00-c0-4f-68-37-cf')
    @commethod(6)
    def InitializeEx(pbc: Windows.Win32.System.Com.IBindCtx_head, pidlRoot: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppfti: POINTER(Windows.Win32.UI.Shell.PERSIST_FOLDER_TARGET_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFolderTargetInfo(ppfti: POINTER(Windows.Win32.UI.Shell.PERSIST_FOLDER_TARGET_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistIDList(c_void_p):
    extends: Windows.Win32.System.Com.IPersist
    Guid = Guid('1079acfc-29bd-11d3-8e-0d-00-c0-4f-68-37-d5')
    @commethod(4)
    def SetIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetIDList(ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IPreviewHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8895b1c6-b41f-4c1c-a5-62-0d-56-42-50-83-6f')
    @commethod(3)
    def SetWindow(hwnd: Windows.Win32.Foundation.HWND, prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetRect(prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DoPreview() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unload() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFocus() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryFocus(phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def TranslateAccelerator(pmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPreviewHandlerFrame(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fec87aaf-35f9-447a-ad-b7-20-23-44-91-40-1a')
    @commethod(3)
    def GetWindowContext(pinfo: POINTER(Windows.Win32.UI.Shell.PREVIEWHANDLERFRAMEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TranslateAccelerator(pmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPreviewHandlerVisuals(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('196bf9a5-b346-4ef0-aa-1e-5d-cd-b7-67-68-b1')
    @commethod(3)
    def SetBackgroundColor(color: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFont(plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetTextColor(color: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
class IPreviewItem(c_void_p):
    extends: Windows.Win32.UI.Shell.IRelatedItem
    Guid = Guid('36149969-0a8f-49c8-8b-00-4a-ec-b2-02-22-fb')
class IPreviousVersionsInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('76e54780-ad74-48e3-a6-95-3b-a9-a0-af-f1-0d')
    @commethod(3)
    def AreSnapshotsAvailable(pszPath: Windows.Win32.Foundation.PWSTR, fOkToBeSlow: Windows.Win32.Foundation.BOOL, pfAvailable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IProfferService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cb728b20-f786-11ce-92-ad-00-aa-00-a7-4c-d0')
    @commethod(3)
    def ProfferService(serviceId: POINTER(Guid), serviceProvider: Windows.Win32.System.Com.IServiceProvider_head, cookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RevokeService(cookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IProgressDialog(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ebbc7c04-315e-11d2-b6-2f-00-60-97-df-5b-d4')
    @commethod(3)
    def StartProgressDialog(hwndParent: Windows.Win32.Foundation.HWND, punkEnableModless: Windows.Win32.System.Com.IUnknown_head, dwFlags: UInt32, pvResevered: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopProgressDialog() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetTitle(pwzTitle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAnimation(hInstAnimation: Windows.Win32.Foundation.HINSTANCE, idAnimation: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HasUserCancelled() -> Windows.Win32.Foundation.BOOL: ...
    @commethod(8)
    def SetProgress(dwCompleted: UInt32, dwTotal: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetProgress64(ullCompleted: UInt64, ullTotal: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetLine(dwLineNum: UInt32, pwzString: Windows.Win32.Foundation.PWSTR, fCompactPath: Windows.Win32.Foundation.BOOL, pvResevered: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetCancelMsg(pwzCancelMsg: Windows.Win32.Foundation.PWSTR, pvResevered: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Timer(dwTimerAction: UInt32, pvResevered: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyKeyStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('75bd59aa-f23b-4963-ab-a4-0b-35-57-52-a9-1b')
    @commethod(3)
    def GetKeyCount(keyCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetKeyAt(index: Int32, pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AppendKey(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteKey(index: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsKeyInStore(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveKey(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPublishedApp(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellApp
    Guid = Guid('1bc752e0-9046-11d1-b8-b3-00-60-08-05-93-82')
    @commethod(8)
    def Install(pstInstall: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPublishedAppInfo(ppai: POINTER(Windows.Win32.UI.Shell.PUBAPPINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Unschedule() -> Windows.Win32.Foundation.HRESULT: ...
class IPublishedApp2(c_void_p):
    extends: Windows.Win32.UI.Shell.IPublishedApp
    Guid = Guid('12b81347-1b3a-4a04-aa-61-3f-76-8b-67-fd-7e')
    @commethod(11)
    def Install2(pstInstall: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head), hwndParent: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class IPublishingWizard(c_void_p):
    extends: Windows.Win32.UI.Shell.IWizardExtension
    Guid = Guid('aa9198bb-ccec-472d-be-ed-19-a4-f6-73-3f-7a')
    @commethod(6)
    def Initialize(pdo: Windows.Win32.System.Com.IDataObject_head, dwOptions: UInt32, pszServiceScope: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransferManifest(phrFromTransfer: POINTER(Windows.Win32.Foundation.HRESULT), pdocManifest: POINTER(Windows.Win32.Data.Xml.MsXml.IXMLDOMDocument_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IQueryAssociations(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c46ca590-3c3f-11d2-be-e6-00-00-f8-05-ca-57')
    @commethod(3)
    def Init(flags: Windows.Win32.UI.Shell.ASSOCF, pszAssoc: Windows.Win32.Foundation.PWSTR, hkProgid: Windows.Win32.System.Registry.HKEY, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetString(flags: Windows.Win32.UI.Shell.ASSOCF, str: Windows.Win32.UI.Shell.ASSOCSTR, pszExtra: Windows.Win32.Foundation.PWSTR, pszOut: Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetKey(flags: Windows.Win32.UI.Shell.ASSOCF, key: Windows.Win32.UI.Shell.ASSOCKEY, pszExtra: Windows.Win32.Foundation.PWSTR, phkeyOut: POINTER(Windows.Win32.System.Registry.HKEY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetData(flags: Windows.Win32.UI.Shell.ASSOCF, data: Windows.Win32.UI.Shell.ASSOCDATA, pszExtra: Windows.Win32.Foundation.PWSTR, pvOut: c_void_p, pcbOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEnum(flags: Windows.Win32.UI.Shell.ASSOCF, assocenum: Windows.Win32.UI.Shell.ASSOCENUM, pszExtra: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppvOut: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IQueryCancelAutoPlay(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ddefe873-6997-4e68-be-26-39-b6-33-ad-be-12')
    @commethod(3)
    def AllowAutoPlay(pszPath: Windows.Win32.Foundation.PWSTR, dwContentType: UInt32, pszLabel: Windows.Win32.Foundation.PWSTR, dwSerialNumber: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IQueryCodePage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c7b236ce-ee80-11d0-98-5f-00-60-08-05-93-82')
    @commethod(3)
    def GetCodePage(puiCodePage: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCodePage(uiCodePage: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IQueryContinue(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7307055c-b24a-486b-9f-25-16-3e-59-7a-28-a9')
    @commethod(3)
    def QueryContinue() -> Windows.Win32.Foundation.HRESULT: ...
class IQueryContinueWithStatus(c_void_p):
    extends: Windows.Win32.UI.Shell.IQueryContinue
    Guid = Guid('9090be5b-502b-41fb-bc-cc-00-49-a6-c7-25-4b')
    @commethod(4)
    def SetStatusMessage(psz: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IQueryInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00021500-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetInfoTip(dwFlags: Windows.Win32.UI.Shell.QITIPF_FLAGS, ppwszTip: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInfoFlags(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRegTreeItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a9521922-0812-4d44-9e-c3-7f-d3-8c-72-6f-3d')
    @commethod(3)
    def GetCheckState(pbCheck: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCheckState(bCheck: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IRelatedItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a73ce67a-8ab1-44f1-8d-43-d2-fc-bf-6b-1c-d0')
    @commethod(3)
    def GetItemIDList(ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(ppsi: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRemoteComputer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214fe-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Initialize(pszMachine: Windows.Win32.Foundation.PWSTR, bEnumerating: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IResolveShellLink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5cd52983-9449-11d2-96-3a-00-c0-4f-79-ad-f0')
    @commethod(3)
    def ResolveShellLink(punkLink: Windows.Win32.System.Com.IUnknown_head, hwnd: Windows.Win32.Foundation.HWND, fFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IResultsFolder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('96e5ae6d-6ae1-4b1c-90-0c-c6-48-0e-aa-88-28')
    @commethod(3)
    def AddItem(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppidlAdded: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveItem(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAll() -> Windows.Win32.Foundation.HRESULT: ...
class IRunnableTask(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85788d00-6807-11d0-b8-10-00-c0-4f-d7-06-ec')
    @commethod(3)
    def Run() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Kill(bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Suspend() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Resume() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsRunning() -> UInt32: ...
class IScriptErrorList(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f3470f24-15fd-11d2-bb-2e-00-80-5f-f7-ef-ca')
    @commethod(7)
    def advanceError() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def retreatError() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def canAdvanceError(pfCanAdvance: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def canRetreatError(pfCanRetreat: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def getErrorLine(plLine: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def getErrorChar(plChar: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def getErrorCode(plCode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def getErrorMsg(pstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def getErrorUrl(pstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def getAlwaysShowLockState(pfAlwaysShowLocked: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def getDetailsPaneOpen(pfDetailsPaneOpen: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def setDetailsPaneOpen(fDetailsPaneOpen: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def getPerErrorDisplay(pfPerErrorDisplay: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def setPerErrorDisplay(fPerErrorDisplay: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISearchBoxInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6af6e03f-d664-4ef4-96-26-f7-e0-ed-36-75-5e')
    @commethod(3)
    def GetCondition(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetText(ppsz: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISearchContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('09f656a2-41af-480c-88-f7-16-cc-0d-16-46-15')
    @commethod(3)
    def GetSearchUrl(pbstrSearchUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSearchText(pbstrSearchText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSearchStyle(pdwSearchStyle: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISearchFolderItemFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a0ffbc28-5482-4366-be-27-3e-81-e7-8e-06-c2')
    @commethod(3)
    def SetDisplayName(pszDisplayName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFolderTypeID(ftid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFolderLogicalViewMode(flvm: Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetIconSize(iIconSize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetVisibleColumns(cVisibleColumns: UInt32, rgKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSortColumns(cSortColumns: UInt32, rgSortColumns: POINTER(Windows.Win32.UI.Shell.SORTCOLUMN_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetGroupColumn(keyGroup: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetStacks(cStackKeys: UInt32, rgStackKeys: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetScope(psiaScope: Windows.Win32.UI.Shell.IShellItemArray_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetCondition(pCondition: Windows.Win32.System.Search.ICondition_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetShellItem(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetIDList(ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class ISharedBitmap(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('091162a4-bc96-411f-aa-e8-c5-12-2c-d0-33-63')
    @commethod(3)
    def GetSharedBitmap(phbm: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSize(pSize: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFormat(pat: POINTER(Windows.Win32.UI.Shell.WTS_ALPHATYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitializeBitmap(hbm: Windows.Win32.Graphics.Gdi.HBITMAP, wtsAT: Windows.Win32.UI.Shell.WTS_ALPHATYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Detach(phbm: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Windows.Win32.Foundation.HRESULT: ...
class ISharingConfigurationManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b4cd448a-9c86-4466-92-01-2e-62-10-5b-87-ae')
    @commethod(3)
    def CreateShare(dsid: Windows.Win32.UI.Shell.DEF_SHARE_ID, role: Windows.Win32.UI.Shell.SHARE_ROLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteShare(dsid: Windows.Win32.UI.Shell.DEF_SHARE_ID) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ShareExists(dsid: Windows.Win32.UI.Shell.DEF_SHARE_ID) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSharePermissions(dsid: Windows.Win32.UI.Shell.DEF_SHARE_ID, pRole: POINTER(Windows.Win32.UI.Shell.SHARE_ROLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SharePrinters() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopSharingPrinters() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ArePrintersShared() -> Windows.Win32.Foundation.HRESULT: ...
class IShellApp(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a3e14960-935f-11d1-b8-b8-00-60-08-05-93-82')
    @commethod(3)
    def GetAppInfo(pai: POINTER(Windows.Win32.UI.Shell.APPINFODATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPossibleActions(pdwActions: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSlowAppInfo(psaid: POINTER(Windows.Win32.UI.Shell.SLOWAPPINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCachedSlowAppInfo(psaid: POINTER(Windows.Win32.UI.Shell.SLOWAPPINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsInstalled() -> Windows.Win32.Foundation.HRESULT: ...
class IShellBrowser(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('000214e2-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(5)
    def InsertMenusSB(hmenuShared: Windows.Win32.UI.WindowsAndMessaging.HMENU, lpMenuWidths: POINTER(Windows.Win32.System.Ole.OLEMENUGROUPWIDTHS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMenuSB(hmenuShared: Windows.Win32.UI.WindowsAndMessaging.HMENU, holemenuRes: IntPtr, hwndActiveObject: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveMenusSB(hmenuShared: Windows.Win32.UI.WindowsAndMessaging.HMENU) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetStatusTextSB(pszStatusText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnableModelessSB(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def TranslateAcceleratorSB(pmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), wID: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def BrowseObject(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), wFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetViewStateStream(grfMode: UInt32, ppStrm: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetControlWindow(id: UInt32, phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SendControlMsg(id: UInt32, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, pret: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def QueryActiveShellView(ppshv: POINTER(Windows.Win32.UI.Shell.IShellView_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnViewWindowActive(pshv: Windows.Win32.UI.Shell.IShellView_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetToolbarItems(lpButtons: POINTER(Windows.Win32.UI.Controls.TBBUTTON_head), nButtons: UInt32, uFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IShellChangeNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d82be2b1-5764-11d0-a9-6e-00-c0-4f-d7-05-a2')
    @commethod(3)
    def OnChange(lEvent: Int32, pidl1: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidl2: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellDetails(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214ec-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetDetailsOf(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), iColumn: UInt32, pDetails: POINTER(Windows.Win32.UI.Shell.Common.SHELLDETAILS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ColumnClick(iColumn: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d8f015c0-c278-11ce-a4-9e-44-45-53-54-00-00')
    @commethod(7)
    def get_Application(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Parent(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def NameSpace(vDir: Windows.Win32.System.Com.VARIANT, ppsdf: POINTER(Windows.Win32.UI.Shell.Folder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BrowseForFolder(Hwnd: Int32, Title: Windows.Win32.Foundation.BSTR, Options: Int32, RootFolder: Windows.Win32.System.Com.VARIANT, ppsdf: POINTER(Windows.Win32.UI.Shell.Folder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Windows(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Open(vDir: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Explore(vDir: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MinimizeAll() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UndoMinimizeALL() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def FileRun() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CascadeWindows() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def TileVertically() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def TileHorizontally() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ShutdownWindows() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Suspend() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EjectPC() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetTime() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def TrayProperties() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Help() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def FindFiles() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def FindComputer() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def RefreshMenu() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ControlPanelItem(bstrDir: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch2(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellDispatch
    Guid = Guid('a4c6892c-3ba9-11d2-9d-ea-00-c0-4f-b1-61-62')
    @commethod(30)
    def IsRestricted(Group: Windows.Win32.Foundation.BSTR, Restriction: Windows.Win32.Foundation.BSTR, plRestrictValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ShellExecute(File: Windows.Win32.Foundation.BSTR, vArgs: Windows.Win32.System.Com.VARIANT, vDir: Windows.Win32.System.Com.VARIANT, vOperation: Windows.Win32.System.Com.VARIANT, vShow: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def FindPrinter(name: Windows.Win32.Foundation.BSTR, location: Windows.Win32.Foundation.BSTR, model: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetSystemInformation(name: Windows.Win32.Foundation.BSTR, pv: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def ServiceStart(ServiceName: Windows.Win32.Foundation.BSTR, Persistent: Windows.Win32.System.Com.VARIANT, pSuccess: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ServiceStop(ServiceName: Windows.Win32.Foundation.BSTR, Persistent: Windows.Win32.System.Com.VARIANT, pSuccess: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def IsServiceRunning(ServiceName: Windows.Win32.Foundation.BSTR, pRunning: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def CanStartStopService(ServiceName: Windows.Win32.Foundation.BSTR, pCanStartStop: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def ShowBrowserBar(bstrClsid: Windows.Win32.Foundation.BSTR, bShow: Windows.Win32.System.Com.VARIANT, pSuccess: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch3(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellDispatch2
    Guid = Guid('177160ca-bb5a-411c-84-1d-bd-38-fa-cd-ea-a0')
    @commethod(39)
    def AddToRecent(varFile: Windows.Win32.System.Com.VARIANT, bstrCategory: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch4(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellDispatch3
    Guid = Guid('efd84b2d-4bcf-4298-be-25-eb-54-2a-59-fb-da')
    @commethod(40)
    def WindowsSecurity() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def ToggleDesktop() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def ExplorerPolicy(bstrPolicyName: Windows.Win32.Foundation.BSTR, pValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def GetSetting(lSetting: Int32, pResult: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch5(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellDispatch4
    Guid = Guid('866738b9-6cf2-4de8-87-67-f7-94-eb-e7-4f-4e')
    @commethod(44)
    def WindowSwitcher() -> Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch6(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellDispatch5
    Guid = Guid('286e6f1b-7113-4355-95-62-96-b7-e9-d6-4c-54')
    @commethod(45)
    def SearchCommand() -> Windows.Win32.Foundation.HRESULT: ...
class IShellExtInit(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214e8-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Initialize(pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pdtobj: Windows.Win32.System.Com.IDataObject_head, hkeyProgID: Windows.Win32.System.Registry.HKEY) -> Windows.Win32.Foundation.HRESULT: ...
class IShellFavoritesNameSpace(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('55136804-b2de-11d1-b9-f2-00-a0-c9-8b-c5-47')
    @commethod(7)
    def MoveSelectionUp() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MoveSelectionDown() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ResetSort() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NewFolder() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Synchronize() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Import() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Export() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def InvokeContextMenuCommand(strCommand: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def MoveSelectionTo() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_SubscriptionsEnabled(pBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateSubscriptionForSelection(pBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteSubscriptionForSelection(pBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetRoot(bstrFullPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IShellFolder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214e6-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def ParseDisplayName(hwnd: Windows.Win32.Foundation.HWND, pbc: Windows.Win32.System.Com.IBindCtx_head, pszDisplayName: Windows.Win32.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), pdwAttributes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumObjects(hwnd: Windows.Win32.Foundation.HWND, grfFlags: UInt32, ppenumIDList: POINTER(Windows.Win32.UI.Shell.IEnumIDList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BindToObject(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BindToStorage(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CompareIDs(lParam: Windows.Win32.Foundation.LPARAM, pidl1: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidl2: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateViewObject(hwndOwner: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttributesOf(cidl: UInt32, apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), rgfInOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetUIObjectOf(hwndOwner: Windows.Win32.Foundation.HWND, cidl: UInt32, apidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), riid: POINTER(Guid), rgfReserved: POINTER(UInt32), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDisplayNameOf(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), uFlags: Windows.Win32.UI.Shell.SHGDNF, pName: POINTER(Windows.Win32.UI.Shell.Common.STRRET_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetNameOf(hwnd: Windows.Win32.Foundation.HWND, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pszName: Windows.Win32.Foundation.PWSTR, uFlags: Windows.Win32.UI.Shell.SHGDNF, ppidlOut: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IShellFolder2(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellFolder
    Guid = Guid('93f2f68c-1d1b-11d3-a3-0e-00-c0-4f-79-ab-d1')
    @commethod(13)
    def GetDefaultSearchGUID(pguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumSearches(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumExtraSearch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDefaultColumn(dwRes: UInt32, pSort: POINTER(UInt32), pDisplay: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDefaultColumnState(iColumn: UInt32, pcsFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDetailsEx(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pscid: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pv: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetDetailsOf(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), iColumn: UInt32, psd: POINTER(Windows.Win32.UI.Shell.Common.SHELLDETAILS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def MapColumnToSCID(iColumn: UInt32, pscid: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellFolderBand(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7fe80cc8-c247-11d0-b9-3a-00-a0-c9-03-12-e1')
    @commethod(3)
    def InitializeSFB(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBandInfoSFB(pbi: POINTER(Windows.Win32.UI.Shell.BANDINFOSFB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBandInfoSFB(pbi: POINTER(Windows.Win32.UI.Shell.BANDINFOSFB_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellFolderView(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('37a378c0-f82d-11ce-ae-65-08-00-2b-2e-12-62')
    @commethod(3)
    def Rearrange(lParamSort: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetArrangeParam(plParamSort: POINTER(Windows.Win32.Foundation.LPARAM)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ArrangeGrid() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AutoArrange() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAutoArrange() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddObject(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), puItem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetObject(ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), uItem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveObject(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), puItem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetObjectCount(puCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetObjectCount(uCount: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def UpdateObject(pidlOld: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pidlNew: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), puItem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RefreshObject(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), puItem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetRedraw(bRedraw: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSelectedCount(puSelected: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSelectedObjects(pppidl: POINTER(POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))), puItems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def IsDropOnSource(pDropTarget: Windows.Win32.System.Ole.IDropTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDragPoint(ppt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDropPoint(ppt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def MoveIcons(pDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetItemPos(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def IsBkDropTarget(pDropTarget: Windows.Win32.System.Ole.IDropTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetClipboard(bMove: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetPoints(pDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetItemSpacing(pSpacing: POINTER(Windows.Win32.UI.Shell.ITEMSPACING_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetCallback(pNewCB: Windows.Win32.UI.Shell.IShellFolderViewCB_head, ppOldCB: POINTER(Windows.Win32.UI.Shell.IShellFolderViewCB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Select(dwFlags: Windows.Win32.UI.Shell.SFVS_SELECT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def QuerySupport(pdwSupport: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetAutomationObject(pdisp: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
class IShellFolderViewCB(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2047e320-f2a9-11ce-ae-65-08-00-2b-2e-12-62')
    @commethod(3)
    def MessageSFVCB(uMsg: Windows.Win32.UI.Shell.SFVM_MESSAGE_ID, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class IShellFolderViewDual(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e7a1af80-4d96-11cf-96-0c-00-80-c7-f4-ee-85')
    @commethod(7)
    def get_Application(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Parent(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Folder(ppid: POINTER(Windows.Win32.UI.Shell.Folder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SelectedItems(ppid: POINTER(Windows.Win32.UI.Shell.FolderItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_FocusedItem(ppid: POINTER(Windows.Win32.UI.Shell.FolderItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SelectItem(pvfi: POINTER(Windows.Win32.System.Com.VARIANT_head), dwFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PopupItemMenu(pfi: Windows.Win32.UI.Shell.FolderItem_head, vx: Windows.Win32.System.Com.VARIANT, vy: Windows.Win32.System.Com.VARIANT, pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Script(ppDisp: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ViewOptions(plViewOptions: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellFolderViewDual2(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellFolderViewDual
    Guid = Guid('31c147b6-0ade-4a3c-b5-14-dd-f9-32-ef-6d-17')
    @commethod(16)
    def get_CurrentViewMode(pViewMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_CurrentViewMode(ViewMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SelectItemRelative(iRelative: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IShellFolderViewDual3(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellFolderViewDual2
    Guid = Guid('29ec8e6c-46d3-411f-ba-aa-61-1a-6c-9c-ac-66')
    @commethod(19)
    def get_GroupBy(pbstrGroupBy: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_GroupBy(bstrGroupBy: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_FolderFlags(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_FolderFlags(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_SortColumns(pbstrSortColumns: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_SortColumns(bstrSortColumns: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_IconSize(iIconSize: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_IconSize(piIconSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def FilterView(bstrFilterText: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IShellIcon(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214e5-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetIconOf(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), flags: UInt32, pIconIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellIconOverlay(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7d688a70-c613-11d0-99-9b-00-c0-4f-d6-55-e1')
    @commethod(3)
    def GetOverlayIndex(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOverlayIconIndex(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pIconIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellIconOverlayIdentifier(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0c6c4200-c589-11d0-99-9a-00-c0-4f-d6-55-e1')
    @commethod(3)
    def IsMemberOf(pwszPath: Windows.Win32.Foundation.PWSTR, dwAttrib: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOverlayInfo(pwszIconFile: Windows.Win32.Foundation.PWSTR, cchMax: Int32, pIndex: POINTER(Int32), pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPriority(pPriority: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellIconOverlayManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f10b5e34-dd3b-42a7-aa-7d-2f-4e-c5-4b-b0-9b')
    @commethod(3)
    def GetFileOverlayInfo(pwszPath: Windows.Win32.Foundation.PWSTR, dwAttrib: UInt32, pIndex: POINTER(Int32), dwflags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReservedOverlayInfo(pwszPath: Windows.Win32.Foundation.PWSTR, dwAttrib: UInt32, pIndex: POINTER(Int32), dwflags: UInt32, iReservedID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RefreshOverlayImages(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def LoadNonloadedOverlayIdentifiers() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OverlayIndexFromImageIndex(iImage: Int32, piIndex: POINTER(Int32), fAdd: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IShellImageData(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bfdeec12-8040-4403-a5-ea-9e-07-da-fc-f5-30')
    @commethod(3)
    def Decode(dwFlags: UInt32, cxDesired: UInt32, cyDesired: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Draw(hdc: Windows.Win32.Graphics.Gdi.HDC, prcDest: POINTER(Windows.Win32.Foundation.RECT_head), prcSrc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NextFrame() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NextPage() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PrevPage() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsTransparent() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsAnimated() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsVector() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsMultipage() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsEditable() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsPrintable() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsDecoded() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCurrentPage(pnPage: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetPageCount(pcPages: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SelectPage(iPage: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSize(pSize: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetRawDataFormat(pDataFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetPixelFormat(pFormat: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetDelay(pdwDelay: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetProperties(dwMode: UInt32, ppPropSet: POINTER(Windows.Win32.System.Com.StructuredStorage.IPropertySetStorage_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Rotate(dwAngle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Scale(cx: UInt32, cy: UInt32, hints: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def DiscardEdit() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetEncoderParams(pbagEnc: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DisplayName(wszName: Windows.Win32.Foundation.PWSTR, cch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetResolution(puResolutionX: POINTER(UInt32), puResolutionY: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetEncoderParams(pguidFmt: POINTER(Guid), ppEncParams: POINTER(c_char_p_no)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def RegisterAbort(pAbort: Windows.Win32.UI.Shell.IShellImageDataAbort_head, ppAbortPrev: POINTER(Windows.Win32.UI.Shell.IShellImageDataAbort_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CloneFrame(ppImg: POINTER(c_char_p_no)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def ReplaceFrame(pImg: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
class IShellImageDataAbort(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('53fb8e58-50c0-4003-b4-aa-0c-8d-f2-8e-7f-3a')
    @commethod(3)
    def QueryAbort() -> Windows.Win32.Foundation.HRESULT: ...
class IShellImageDataFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9be8ed5c-edab-4d75-90-f3-bd-5b-db-b2-1c-82')
    @commethod(3)
    def CreateIShellImageData(ppshimg: POINTER(Windows.Win32.UI.Shell.IShellImageData_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateImageFromFile(pszPath: Windows.Win32.Foundation.PWSTR, ppshimg: POINTER(Windows.Win32.UI.Shell.IShellImageData_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateImageFromStream(pStream: Windows.Win32.System.Com.IStream_head, ppshimg: POINTER(Windows.Win32.UI.Shell.IShellImageData_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDataFormatFromPath(pszPath: Windows.Win32.Foundation.PWSTR, pDataFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('43826d1e-e718-42ee-bc-55-a1-e2-61-c3-7b-fe')
    @commethod(3)
    def BindToHandler(pbc: Windows.Win32.System.Com.IBindCtx_head, bhid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParent(ppsi: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplayName(sigdnName: Windows.Win32.UI.Shell.SIGDN, ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAttributes(sfgaoMask: Windows.Win32.System.SystemServices.SFGAO_FLAGS, psfgaoAttribs: POINTER(Windows.Win32.System.SystemServices.SFGAO_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Compare(psi: Windows.Win32.UI.Shell.IShellItem_head, hint: UInt32, piOrder: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellItem2(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellItem
    Guid = Guid('7e9fb0d3-919f-4307-ab-2e-9b-18-60-31-0c-93')
    @commethod(8)
    def GetPropertyStore(flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPropertyStoreWithCreateObject(flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, punkCreateObject: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPropertyStoreForKeys(rgKeys: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), cKeys: UInt32, flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPropertyDescriptionList(keyType: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Update(pbc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetProperty(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCLSID(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFileTime(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pft: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetInt32(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pi: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetString(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppsz: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetUInt32(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pui: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetUInt64(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pull: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetBool(key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pf: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellItemArray(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b63ea76d-1f85-456f-a1-9c-48-15-9e-fa-85-8b')
    @commethod(3)
    def BindToHandler(pbc: Windows.Win32.System.Com.IBindCtx_head, bhid: POINTER(Guid), riid: POINTER(Guid), ppvOut: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyStore(flags: Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyDescriptionList(keyType: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAttributes(AttribFlags: Windows.Win32.UI.Shell.SIATTRIBFLAGS, sfgaoMask: Windows.Win32.System.SystemServices.SFGAO_FLAGS, psfgaoAttribs: POINTER(Windows.Win32.System.SystemServices.SFGAO_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(pdwNumItems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetItemAt(dwIndex: UInt32, ppsi: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumItems(ppenumShellItems: POINTER(Windows.Win32.UI.Shell.IEnumShellItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellItemFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2659b475-eeb8-48b7-8f-07-b3-78-81-0f-48-cf')
    @commethod(3)
    def IncludeItem(psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEnumFlagsForItem(psi: Windows.Win32.UI.Shell.IShellItem_head, pgrfFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellItemImageFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bcc18b79-ba16-442f-80-c4-8a-59-c3-0c-46-3b')
    @commethod(3)
    def GetImage(size: Windows.Win32.Foundation.SIZE, flags: Windows.Win32.UI.Shell.SIIGBF, phbm: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellItemResources(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ff5693be-2ce0-4d48-b5-c5-40-81-7d-1a-cd-b9')
    @commethod(3)
    def GetAttributes(pdwAttributes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSize(pullSize: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTimes(pftCreation: POINTER(Windows.Win32.Foundation.FILETIME_head), pftWrite: POINTER(Windows.Win32.Foundation.FILETIME_head), pftAccess: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTimes(pftCreation: POINTER(Windows.Win32.Foundation.FILETIME_head), pftWrite: POINTER(Windows.Win32.Foundation.FILETIME_head), pftAccess: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResourceDescription(pcsir: POINTER(Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE_head), ppszDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumResources(ppenumr: POINTER(Windows.Win32.UI.Shell.IEnumResources_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SupportsResource(pcsir: POINTER(Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OpenResource(pcsir: POINTER(Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateResource(pcsir: POINTER(Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MarkForDelete() -> Windows.Win32.Foundation.HRESULT: ...
class IShellLibrary(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('11a66efa-382e-451a-92-34-1e-0e-12-ef-30-85')
    @commethod(3)
    def LoadLibraryFromItem(psiLibrary: Windows.Win32.UI.Shell.IShellItem_head, grfMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadLibraryFromKnownFolder(kfidLibrary: POINTER(Guid), grfMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddFolder(psiLocation: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveFolder(psiLocation: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFolders(lff: Windows.Win32.UI.Shell.LIBRARYFOLDERFILTER, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResolveFolder(psiFolderToResolve: Windows.Win32.UI.Shell.IShellItem_head, dwTimeout: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDefaultSaveFolder(dsft: Windows.Win32.UI.Shell.DEFAULTSAVEFOLDERTYPE, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDefaultSaveFolder(dsft: Windows.Win32.UI.Shell.DEFAULTSAVEFOLDERTYPE, psi: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOptions(plofOptions: POINTER(Windows.Win32.UI.Shell.LIBRARYOPTIONFLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetOptions(lofMask: Windows.Win32.UI.Shell.LIBRARYOPTIONFLAGS, lofOptions: Windows.Win32.UI.Shell.LIBRARYOPTIONFLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFolderType(pftid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetFolderType(ftid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetIcon(ppszIcon: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetIcon(pszIcon: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Commit() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Save(psiFolderToSaveIn: Windows.Win32.UI.Shell.IShellItem_head, pszLibraryName: Windows.Win32.Foundation.PWSTR, lsf: Windows.Win32.UI.Shell.LIBRARYSAVEFLAGS, ppsiSavedTo: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SaveInKnownFolder(kfidToSaveIn: POINTER(Guid), pszLibraryName: Windows.Win32.Foundation.PWSTR, lsf: Windows.Win32.UI.Shell.LIBRARYSAVEFLAGS, ppsiSavedTo: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellLinkA(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214ee-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetPath(pszFile: Windows.Win32.Foundation.PSTR, cch: Int32, pfd: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA_head), fFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIDList(ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescription(pszName: Windows.Win32.Foundation.PSTR, cch: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDescription(pszName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWorkingDirectory(pszDir: Windows.Win32.Foundation.PSTR, cch: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetWorkingDirectory(pszDir: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetArguments(pszArgs: Windows.Win32.Foundation.PSTR, cch: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetArguments(pszArgs: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetHotkey(pwHotkey: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetHotkey(wHotkey: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetShowCmd(piShowCmd: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetShowCmd(iShowCmd: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetIconLocation(pszIconPath: Windows.Win32.Foundation.PSTR, cch: Int32, piIcon: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetIconLocation(pszIconPath: Windows.Win32.Foundation.PSTR, iIcon: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetRelativePath(pszPathRel: Windows.Win32.Foundation.PSTR, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Resolve(hwnd: Windows.Win32.Foundation.HWND, fFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetPath(pszFile: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IShellLinkDataList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('45e2b4ae-b1c3-11d0-b9-2f-00-a0-c9-03-12-e1')
    @commethod(3)
    def AddDataBlock(pDataBlock: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CopyDataBlock(dwSig: UInt32, ppDataBlock: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveDataBlock(dwSig: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFlags(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFlags(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IShellLinkDual(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('88a05c00-f000-11ce-83-50-44-45-53-54-00-00')
    @commethod(7)
    def get_Path(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Path(bs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(bs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_WorkingDirectory(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_WorkingDirectory(bs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Arguments(pbs: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Arguments(bs: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Hotkey(piHK: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Hotkey(iHK: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ShowCommand(piShowCommand: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ShowCommand(iShowCommand: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Resolve(fFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetIconLocation(pbs: POINTER(Windows.Win32.Foundation.BSTR), piIcon: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetIconLocation(bs: Windows.Win32.Foundation.BSTR, iIcon: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save(vWhere: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IShellLinkDual2(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellLinkDual
    Guid = Guid('317ee249-f12e-11d2-b1-e4-00-c0-4f-8e-eb-3e')
    @commethod(23)
    def get_Target(ppfi: POINTER(Windows.Win32.UI.Shell.FolderItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellLinkW(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214f9-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetPath(pszFile: Windows.Win32.Foundation.PWSTR, cch: Int32, pfd: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW_head), fFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIDList(ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIDList(pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescription(pszName: Windows.Win32.Foundation.PWSTR, cch: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDescription(pszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWorkingDirectory(pszDir: Windows.Win32.Foundation.PWSTR, cch: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetWorkingDirectory(pszDir: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetArguments(pszArgs: Windows.Win32.Foundation.PWSTR, cch: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetArguments(pszArgs: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetHotkey(pwHotkey: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetHotkey(wHotkey: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetShowCmd(piShowCmd: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetShowCmd(iShowCmd: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetIconLocation(pszIconPath: Windows.Win32.Foundation.PWSTR, cch: Int32, piIcon: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetIconLocation(pszIconPath: Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetRelativePath(pszPathRel: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Resolve(hwnd: Windows.Win32.Foundation.HWND, fFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetPath(pszFile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IShellMenu(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ee1f7637-e138-11d1-83-79-00-c0-4f-d9-18-d0')
    @commethod(3)
    def Initialize(psmc: Windows.Win32.UI.Shell.IShellMenuCallback_head, uId: UInt32, uIdAncestor: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMenuInfo(ppsmc: POINTER(Windows.Win32.UI.Shell.IShellMenuCallback_head), puId: POINTER(UInt32), puIdAncestor: POINTER(UInt32), pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetShellFolder(psf: Windows.Win32.UI.Shell.IShellFolder_head, pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), hKey: Windows.Win32.System.Registry.HKEY, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetShellFolder(pdwFlags: POINTER(UInt32), ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMenu(hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, hwnd: Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMenu(phmenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU), phwnd: POINTER(Windows.Win32.Foundation.HWND), pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InvalidateItem(psmd: POINTER(Windows.Win32.UI.Shell.SMDATA_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetState(psmd: POINTER(Windows.Win32.UI.Shell.SMDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMenuToolbar(punk: Windows.Win32.System.Com.IUnknown_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IShellMenuCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4ca300a1-9b8d-11d1-8b-22-00-c0-4f-d9-18-d0')
    @commethod(3)
    def CallbackSM(psmd: POINTER(Windows.Win32.UI.Shell.SMDATA_head), uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class IShellNameSpace(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellFavoritesNameSpace
    Guid = Guid('e572d3c9-37be-4ae2-82-5d-d5-21-76-3e-31-08')
    @commethod(20)
    def get_EnumOptions(pgrfEnumFlags: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_EnumOptions(lVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_SelectedItem(pItem: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_SelectedItem(pItem: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Root(pvar: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Root(var: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Depth(piDepth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_Depth(iDepth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Mode(puMode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Mode(uMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Flags(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Flags(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_TVFlags(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_TVFlags(dwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Columns(bstrColumns: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_Columns(bstrColumns: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_CountViewTypes(piTypes: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetViewType(iType: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SelectedItems(ppid: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def Expand(var: Windows.Win32.System.Com.VARIANT, iDepth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def UnselectAll() -> Windows.Win32.Foundation.HRESULT: ...
class IShellPropSheetExt(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('000214e9-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def AddPages(pfnAddPage: Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReplacePage(uPageID: UInt32, pfnReplaceWith: Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class IShellRunDll(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fce4bde0-4b68-4b80-8e-9c-74-26-31-5a-73-88')
    @commethod(3)
    def Run(pszArgs: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IShellService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5836fb00-8187-11cf-a1-2b-00-aa-00-4a-e8-37')
    @commethod(3)
    def SetOwner(punkOwner: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IShellTaskScheduler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6ccb7be0-6807-11d0-b8-10-00-c0-4f-d7-06-ec')
    @commethod(3)
    def AddTask(prt: Windows.Win32.UI.Shell.IRunnableTask_head, rtoid: POINTER(Guid), lParam: UIntPtr, dwPriority: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveTasks(rtoid: POINTER(Guid), lParam: UIntPtr, bWaitIfRunning: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CountTasks(rtoid: POINTER(Guid)) -> UInt32: ...
    @commethod(6)
    def Status(dwReleaseStatus: UInt32, dwThreadTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('729fe2f8-1ea8-11d1-8f-85-00-c0-4f-c2-fb-e1')
    @commethod(7)
    def ResetFirstBootMode() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResetSafeMode() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RefreshOfflineDesktop() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddFavorite(URL: Windows.Win32.Foundation.BSTR, Title: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddChannel(URL: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddDesktopComponent(URL: Windows.Win32.Foundation.BSTR, Type: Windows.Win32.Foundation.BSTR, Left: POINTER(Windows.Win32.System.Com.VARIANT_head), Top: POINTER(Windows.Win32.System.Com.VARIANT_head), Width: POINTER(Windows.Win32.System.Com.VARIANT_head), Height: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsSubscribed(URL: Windows.Win32.Foundation.BSTR, pBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def NavigateAndFind(URL: Windows.Win32.Foundation.BSTR, strQuery: Windows.Win32.Foundation.BSTR, varTargetFrame: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ImportExportFavorites(fImport: Windows.Win32.Foundation.VARIANT_BOOL, strImpExpPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AutoCompleteSaveForm(Form: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AutoScan(strSearch: Windows.Win32.Foundation.BSTR, strFailureUrl: Windows.Win32.Foundation.BSTR, pvarTargetFrame: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def AutoCompleteAttach(Reserved: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ShowBrowserUI(bstrName: Windows.Win32.Foundation.BSTR, pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarOut: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper2(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellUIHelper
    Guid = Guid('a7fe6eda-1932-4281-b8-81-87-b3-1b-8b-c5-2c')
    @commethod(20)
    def AddSearchProvider(URL: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def RunOnceShown() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SkipRunOnce() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CustomizeSettings(fSQM: Windows.Win32.Foundation.VARIANT_BOOL, fPhishing: Windows.Win32.Foundation.VARIANT_BOOL, bstrLocale: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SqmEnabled(pfEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def PhishingEnabled(pfEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def BrandImageUri(pbstrUri: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SkipTabsWelcome() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def DiagnoseConnection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CustomizeClearType(fSet: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def IsSearchProviderInstalled(URL: Windows.Win32.Foundation.BSTR, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def IsSearchMigrated(pfMigrated: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def DefaultSearchProvider(pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RunOnceRequiredSettingsComplete(fComplete: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def RunOnceHasShown(pfShown: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SearchGuideUrl(pbstrUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper3(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellUIHelper2
    Guid = Guid('528df2ec-d419-40bc-9b-6d-dc-db-f9-c1-b2-5d')
    @commethod(36)
    def AddService(URL: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def IsServiceInstalled(URL: Windows.Win32.Foundation.BSTR, Verb: Windows.Win32.Foundation.BSTR, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def InPrivateFilteringEnabled(pfEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def AddToFavoritesBar(URL: Windows.Win32.Foundation.BSTR, Title: Windows.Win32.Foundation.BSTR, Type: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def BuildNewTabPage() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetRecentlyClosedVisible(fVisible: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SetActivitiesVisible(fVisible: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def ContentDiscoveryReset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def IsSuggestedSitesEnabled(pfEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def EnableSuggestedSites(fEnable: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def NavigateToSuggestedSites(bstrRelativeUrl: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def ShowTabsHelp() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def ShowInPrivateHelp() -> Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper4(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellUIHelper3
    Guid = Guid('b36e6a53-8073-499e-82-4c-d7-76-33-0a-33-3e')
    @commethod(49)
    def msIsSiteMode(pfSiteMode: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def msSiteModeShowThumbBar() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def msSiteModeAddThumbBarButton(bstrIconURL: Windows.Win32.Foundation.BSTR, bstrTooltip: Windows.Win32.Foundation.BSTR, pvarButtonID: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def msSiteModeUpdateThumbBarButton(ButtonID: Windows.Win32.System.Com.VARIANT, fEnabled: Windows.Win32.Foundation.VARIANT_BOOL, fVisible: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def msSiteModeSetIconOverlay(IconUrl: Windows.Win32.Foundation.BSTR, pvarDescription: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def msSiteModeClearIconOverlay() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def msAddSiteMode() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def msSiteModeCreateJumpList(bstrHeader: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def msSiteModeAddJumpListItem(bstrName: Windows.Win32.Foundation.BSTR, bstrActionUri: Windows.Win32.Foundation.BSTR, bstrIconUri: Windows.Win32.Foundation.BSTR, pvarWindowType: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def msSiteModeClearJumpList() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def msSiteModeShowJumpList() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def msSiteModeAddButtonStyle(uiButtonID: Windows.Win32.System.Com.VARIANT, bstrIconUrl: Windows.Win32.Foundation.BSTR, bstrTooltip: Windows.Win32.Foundation.BSTR, pvarStyleID: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def msSiteModeShowButtonStyle(uiButtonID: Windows.Win32.System.Com.VARIANT, uiStyleID: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def msSiteModeActivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def msIsSiteModeFirstRun(fPreserveState: Windows.Win32.Foundation.VARIANT_BOOL, puiFirstRun: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def msAddTrackingProtectionList(URL: Windows.Win32.Foundation.BSTR, bstrFilterName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def msTrackingProtectionEnabled(pfEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def msActiveXFilteringEnabled(pfEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper5(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellUIHelper4
    Guid = Guid('a2a08b09-103d-4d3f-b9-1c-ea-45-5c-a8-2e-fa')
    @commethod(67)
    def msProvisionNetworks(bstrProvisioningXml: Windows.Win32.Foundation.BSTR, puiResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def msReportSafeUrl() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def msSiteModeRefreshBadge() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def msSiteModeClearBadge() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def msDiagnoseConnectionUILess() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def msLaunchNetworkClientHelp() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def msChangeDefaultBrowser(fChange: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper6(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellUIHelper5
    Guid = Guid('987a573e-46ee-4e89-96-ab-dd-f7-f8-fd-c9-8c')
    @commethod(74)
    def msStopPeriodicTileUpdate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def msStartPeriodicTileUpdate(pollingUris: Windows.Win32.System.Com.VARIANT, startTime: Windows.Win32.System.Com.VARIANT, uiUpdateRecurrence: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def msStartPeriodicTileUpdateBatch(pollingUris: Windows.Win32.System.Com.VARIANT, startTime: Windows.Win32.System.Com.VARIANT, uiUpdateRecurrence: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def msClearTile() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def msEnableTileNotificationQueue(fChange: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def msPinnedSiteState(pvarSiteState: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def msEnableTileNotificationQueueForSquare150x150(fChange: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def msEnableTileNotificationQueueForWide310x150(fChange: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def msEnableTileNotificationQueueForSquare310x310(fChange: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def msScheduledTileNotification(bstrNotificationXml: Windows.Win32.Foundation.BSTR, bstrNotificationId: Windows.Win32.Foundation.BSTR, bstrNotificationTag: Windows.Win32.Foundation.BSTR, startTime: Windows.Win32.System.Com.VARIANT, expirationTime: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def msRemoveScheduledTileNotification(bstrNotificationId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def msStartPeriodicBadgeUpdate(pollingUri: Windows.Win32.Foundation.BSTR, startTime: Windows.Win32.System.Com.VARIANT, uiUpdateRecurrence: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def msStopPeriodicBadgeUpdate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def msLaunchInternetOptions() -> Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper7(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellUIHelper6
    Guid = Guid('60e567c8-9573-4ab2-a2-64-63-7c-6c-16-1c-b1')
    @commethod(88)
    def SetExperimentalFlag(bstrFlagString: Windows.Win32.Foundation.BSTR, vfFlag: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def GetExperimentalFlag(bstrFlagString: Windows.Win32.Foundation.BSTR, vfFlag: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def SetExperimentalValue(bstrValueString: Windows.Win32.Foundation.BSTR, dwValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def GetExperimentalValue(bstrValueString: Windows.Win32.Foundation.BSTR, pdwValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def ResetAllExperimentalFlagsAndValues() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def GetNeedIEAutoLaunchFlag(bstrUrl: Windows.Win32.Foundation.BSTR, flag: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def SetNeedIEAutoLaunchFlag(bstrUrl: Windows.Win32.Foundation.BSTR, flag: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def HasNeedIEAutoLaunchFlag(bstrUrl: Windows.Win32.Foundation.BSTR, exists: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def LaunchIE(bstrUrl: Windows.Win32.Foundation.BSTR, automated: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper8(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellUIHelper7
    Guid = Guid('66debcf2-05b0-4f07-b4-9b-b9-62-41-a6-5d-b2')
    @commethod(97)
    def GetCVListData(pbstrResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def GetCVListLocalData(pbstrResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def GetEMIEListData(pbstrResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(100)
    def GetEMIEListLocalData(pbstrResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(101)
    def OpenFavoritesPane() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(102)
    def OpenFavoritesSettings() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(103)
    def LaunchInHVSI(bstrUrl: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper9(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellUIHelper8
    Guid = Guid('6cdf73b0-7f2f-451f-bc-0f-63-e0-f3-28-4e-54')
    @commethod(104)
    def GetOSSku(pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellView(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('000214e3-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(5)
    def TranslateAccelerator(pmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnableModeless(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UIActivate(uState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateViewWindow(psvPrevious: Windows.Win32.UI.Shell.IShellView_head, pfs: POINTER(Windows.Win32.UI.Shell.FOLDERSETTINGS_head), psb: Windows.Win32.UI.Shell.IShellBrowser_head, prcView: POINTER(Windows.Win32.Foundation.RECT_head), phWnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DestroyViewWindow() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCurrentInfo(pfs: POINTER(Windows.Win32.UI.Shell.FOLDERSETTINGS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddPropertySheetPages(dwReserved: UInt32, pfn: Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lparam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveViewState() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SelectItem(pidlItem: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), uFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetItemObject(uItem: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellView2(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellView
    Guid = Guid('88e39e80-3578-11cf-ae-69-08-00-2b-2e-12-62')
    @commethod(16)
    def GetView(pvid: POINTER(Guid), uView: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateViewWindow2(lpParams: POINTER(Windows.Win32.UI.Shell.SV2CVW2_PARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def HandleRename(pidlNew: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SelectAndPositionItem(pidlItem: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), uFlags: UInt32, ppt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellView3(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellView2
    Guid = Guid('ec39fa88-f8af-41c5-84-21-38-be-d2-8f-46-73')
    @commethod(20)
    def CreateViewWindow3(psbOwner: Windows.Win32.UI.Shell.IShellBrowser_head, psvPrev: Windows.Win32.UI.Shell.IShellView_head, dwViewFlags: UInt32, dwMask: Windows.Win32.UI.Shell.FOLDERFLAGS, dwFlags: Windows.Win32.UI.Shell.FOLDERFLAGS, fvMode: Windows.Win32.UI.Shell.FOLDERVIEWMODE, pvid: POINTER(Guid), prcView: POINTER(Windows.Win32.Foundation.RECT_head), phwndView: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
class IShellWindows(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('85cb6900-4d95-11cf-96-0c-00-80-c7-f4-ee-85')
    @commethod(7)
    def get_Count(Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(index: Windows.Win32.System.Com.VARIANT, Folder: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def _NewEnum(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Register(pid: Windows.Win32.System.Com.IDispatch_head, hwnd: Int32, swClass: Int32, plCookie: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterPending(lThreadId: Int32, pvarloc: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarlocRoot: POINTER(Windows.Win32.System.Com.VARIANT_head), swClass: Int32, plCookie: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Revoke(lCookie: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnNavigate(lCookie: Int32, pvarLoc: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnActivated(lCookie: Int32, fActive: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def FindWindowSW(pvarLoc: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarLocRoot: POINTER(Windows.Win32.System.Com.VARIANT_head), swClass: Int32, phwnd: POINTER(Int32), swfwOptions: Int32, ppdispOut: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnCreated(lCookie: Int32, punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ProcessAttachDetach(fAttach: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ISortColumnArray(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6dfc60fb-f2e9-459b-be-b5-28-8f-1a-7c-7d-54')
    @commethod(3)
    def GetCount(columnCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(index: UInt32, sortcolumn: POINTER(Windows.Win32.UI.Shell.SORTCOLUMN_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSortType(type: POINTER(Windows.Win32.UI.Shell.SORT_ORDER_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IStartMenuPinnedList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4cd19ada-25a5-4a32-b3-b7-34-7b-ee-5b-e3-6b')
    @commethod(3)
    def RemoveFromList(pitem: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
class IStorageProviderBanners(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5efb46d7-47c0-4b68-ac-da-de-d4-7c-90-ec-91')
    @commethod(3)
    def SetBanner(providerIdentity: Windows.Win32.Foundation.PWSTR, subscriptionId: Windows.Win32.Foundation.PWSTR, contentId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ClearBanner(providerIdentity: Windows.Win32.Foundation.PWSTR, subscriptionId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ClearAllBanners(providerIdentity: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBanner(providerIdentity: Windows.Win32.Foundation.PWSTR, subscriptionId: Windows.Win32.Foundation.PWSTR, contentId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IStorageProviderCopyHook(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7bf992a9-af7a-4dba-b2-e5-4d-08-0b-1e-cb-c6')
    @commethod(3)
    def CopyCallback(hwnd: Windows.Win32.Foundation.HWND, operation: UInt32, flags: UInt32, srcFile: Windows.Win32.Foundation.PWSTR, srcAttribs: UInt32, destFile: Windows.Win32.Foundation.PWSTR, destAttribs: UInt32, result: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IStorageProviderHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('162c6fb5-44d3-435b-90-3d-e6-13-fa-09-3f-b5')
    @commethod(3)
    def GetPropertyHandlerFromPath(path: Windows.Win32.Foundation.PWSTR, propertyHandler: POINTER(Windows.Win32.UI.Shell.IStorageProviderPropertyHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyHandlerFromUri(uri: Windows.Win32.Foundation.PWSTR, propertyHandler: POINTER(Windows.Win32.UI.Shell.IStorageProviderPropertyHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyHandlerFromFileId(fileId: Windows.Win32.Foundation.PWSTR, propertyHandler: POINTER(Windows.Win32.UI.Shell.IStorageProviderPropertyHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IStorageProviderPropertyHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('301dfbe5-524c-4b0f-8b-2d-21-c4-0b-3a-29-88')
    @commethod(3)
    def RetrieveProperties(propertiesToRetrieve: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), propertiesToRetrieveCount: UInt32, retrievedProperties: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SaveProperties(propertiesToSave: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
class IStreamAsync(c_void_p):
    extends: Windows.Win32.System.Com.IStream
    Guid = Guid('fe0b6665-e0ca-49b9-a1-78-2b-5c-b4-8d-92-a5')
    @commethod(14)
    def ReadAsync(pv: c_void_p, cb: UInt32, pcbRead: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def WriteAsync(lpBuffer: c_void_p, cb: UInt32, pcbWritten: POINTER(UInt32), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OverlappedResult(lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), lpNumberOfBytesTransferred: POINTER(UInt32), bWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CancelIo() -> Windows.Win32.Foundation.HRESULT: ...
class IStreamUnbufferedInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8a68fdda-1fdc-4c20-8c-eb-41-66-43-b5-a6-25')
    @commethod(3)
    def GetSectorSize(pcbSectorSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISuspensionDependencyManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('52b83a42-2543-416a-81-d9-c0-de-79-69-c8-b3')
    @commethod(3)
    def RegisterAsChild(processHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GroupChildWithParent(childProcessHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UngroupChildFromParent(childProcessHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflict(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9c204249-c443-4ba4-85-ed-c9-72-68-1d-b1-37')
    @commethod(3)
    def GetProperty(propkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), ppropvar: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConflictIdInfo(pConflictIdInfo: POINTER(Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ID_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetItemsArray(ppArray: POINTER(Windows.Win32.UI.Shell.ISyncMgrConflictItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Resolve(pResolveInfo: Windows.Win32.UI.Shell.ISyncMgrConflictResolveInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResolutionHandler(riid: POINTER(Guid), ppvResolutionHandler: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictFolder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('59287f5e-bc81-4fca-a7-f1-e5-a8-ec-db-1d-69')
    @commethod(3)
    def GetConflictIDList(pConflict: Windows.Win32.UI.Shell.ISyncMgrConflict_head, ppidlConflict: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictItems(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9c7ead52-8023-4936-a4-db-d2-a9-a9-9e-43-6a')
    @commethod(3)
    def GetCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(iIndex: UInt32, pItemInfo: POINTER(Windows.Win32.UI.Shell.CONFIRM_CONFLICT_ITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictPresenter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0b4f5353-fd2b-42cd-87-63-47-79-f2-d5-08-a3')
    @commethod(3)
    def PresentConflict(pConflict: Windows.Win32.UI.Shell.ISyncMgrConflict_head, pResolveInfo: Windows.Win32.UI.Shell.ISyncMgrConflictResolveInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictResolutionItems(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('458725b9-129d-4135-a9-98-9c-ea-fe-c2-70-07')
    @commethod(3)
    def GetCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(iIndex: UInt32, pItemInfo: POINTER(Windows.Win32.UI.Shell.CONFIRM_CONFLICT_RESULT_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictResolveInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c405a219-25a2-442e-87-43-b8-45-a2-ce-e9-3f')
    @commethod(3)
    def GetIterationInfo(pnCurrentConflict: POINTER(UInt32), pcConflicts: POINTER(UInt32), pcRemainingForApplyToAll: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPresenterNextStep(pnPresenterNextStep: POINTER(Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_NEXT_STEP)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPresenterChoice(pnPresenterChoice: POINTER(Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE), pfApplyToAll: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemChoiceCount(pcChoices: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetItemChoice(iChoice: UInt32, piChoiceIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetPresenterNextStep(nPresenterNextStep: Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_NEXT_STEP) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetPresenterChoice(nPresenterChoice: Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE, fApplyToAll: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetItemChoices(prgiConflictItemIndexes: POINTER(UInt32), cChoices: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cf8fc579-c396-4774-85-f1-d9-08-a8-31-15-6e')
    @commethod(3)
    def EnumConflicts(pszHandlerID: Windows.Win32.Foundation.PWSTR, pszItemID: Windows.Win32.Foundation.PWSTR, ppEnum: POINTER(Windows.Win32.UI.Shell.IEnumSyncMgrConflict_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BindToConflict(pConflictIdInfo: POINTER(Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ID_INFO_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveConflicts(rgConflictIdInfo: POINTER(Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ID_INFO_head), cConflicts: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(pszHandlerID: Windows.Win32.Foundation.PWSTR, pszItemID: Windows.Win32.Foundation.PWSTR, pnConflicts: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9b63616c-36b2-46bc-95-9f-c1-59-39-52-d1-9b')
    @commethod(3)
    def StartHandlerSync(pszHandlerID: Windows.Win32.Foundation.PWSTR, hwndOwner: Windows.Win32.Foundation.HWND, punk: Windows.Win32.System.Com.IUnknown_head, nSyncControlFlags: Windows.Win32.UI.Shell.SYNCMGR_SYNC_CONTROL_FLAGS, pResult: Windows.Win32.UI.Shell.ISyncMgrSyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartItemSync(pszHandlerID: Windows.Win32.Foundation.PWSTR, ppszItemIDs: POINTER(Windows.Win32.Foundation.PWSTR), cItems: UInt32, hwndOwner: Windows.Win32.Foundation.HWND, punk: Windows.Win32.System.Com.IUnknown_head, nSyncControlFlags: Windows.Win32.UI.Shell.SYNCMGR_SYNC_CONTROL_FLAGS, pResult: Windows.Win32.UI.Shell.ISyncMgrSyncResult_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StartSyncAll(hwndOwner: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def StopHandlerSync(pszHandlerID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def StopItemSync(pszHandlerID: Windows.Win32.Foundation.PWSTR, ppszItemIDs: POINTER(Windows.Win32.Foundation.PWSTR), cItems: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopSyncAll() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UpdateHandlerCollection(rclsidCollectionID: POINTER(Guid), nControlFlags: Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UpdateHandler(pszHandlerID: Windows.Win32.Foundation.PWSTR, nControlFlags: Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UpdateItem(pszHandlerID: Windows.Win32.Foundation.PWSTR, pszItemID: Windows.Win32.Foundation.PWSTR, nControlFlags: Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UpdateEvents(pszHandlerID: Windows.Win32.Foundation.PWSTR, pszItemID: Windows.Win32.Foundation.PWSTR, nControlFlags: Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def UpdateConflict(pszHandlerID: Windows.Win32.Foundation.PWSTR, pszItemID: Windows.Win32.Foundation.PWSTR, pConflict: Windows.Win32.UI.Shell.ISyncMgrConflict_head, nReason: Windows.Win32.UI.Shell.SYNCMGR_UPDATE_REASON) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UpdateConflicts(pszHandlerID: Windows.Win32.Foundation.PWSTR, pszItemID: Windows.Win32.Foundation.PWSTR, nControlFlags: Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ActivateHandler(fActivate: Windows.Win32.Foundation.BOOL, pszHandlerID: Windows.Win32.Foundation.PWSTR, hwndOwner: Windows.Win32.Foundation.HWND, nControlFlags: Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnableHandler(fEnable: Windows.Win32.Foundation.BOOL, pszHandlerID: Windows.Win32.Foundation.PWSTR, hwndOwner: Windows.Win32.Foundation.HWND, nControlFlags: Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnableItem(fEnable: Windows.Win32.Foundation.BOOL, pszHandlerID: Windows.Win32.Foundation.PWSTR, pszItemID: Windows.Win32.Foundation.PWSTR, hwndOwner: Windows.Win32.Foundation.HWND, nControlFlags: Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrEnumItems(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6295df2a-35ee-11d1-87-07-00-c0-4f-d9-33-27')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.UI.Shell.SYNCMGRITEM_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.UI.Shell.ISyncMgrEnumItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrEvent(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fee0ef8b-46bd-4db4-b7-e6-ff-2c-68-73-13-bc')
    @commethod(3)
    def GetEventID(pguidEventID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHandlerID(ppszHandlerID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetItemID(ppszItemID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLevel(pnLevel: POINTER(Windows.Win32.UI.Shell.SYNCMGR_EVENT_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFlags(pnFlags: POINTER(Windows.Win32.UI.Shell.SYNCMGR_EVENT_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTime(pfCreationTime: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetName(ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDescription(ppszDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLinkText(ppszLinkText: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLinkReference(ppszLinkReference: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetContext(ppszContext: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrEventLinkUIOperation(c_void_p):
    extends: Windows.Win32.UI.Shell.ISyncMgrUIOperation
    Guid = Guid('64522e52-848b-4015-89-ce-5a-36-f0-0b-94-ff')
    @commethod(4)
    def Init(rguidEventID: POINTER(Guid), pEvent: Windows.Win32.UI.Shell.ISyncMgrEvent_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrEventStore(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('37e412f9-016e-44c2-81-ff-db-3a-dd-77-42-66')
    @commethod(3)
    def GetEventEnumerator(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumSyncMgrEvents_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEventCount(pcEvents: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEvent(rguidEventID: POINTER(Guid), ppEvent: POINTER(Windows.Win32.UI.Shell.ISyncMgrEvent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveEvent(pguidEventIDs: POINTER(Guid), cEvents: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('04ec2e43-ac77-49f9-9b-98-03-07-ef-7a-72-a2')
    @commethod(3)
    def GetName(ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHandlerInfo(ppHandlerInfo: POINTER(Windows.Win32.UI.Shell.ISyncMgrHandlerInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetObject(rguidObjectID: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCapabilities(pmCapabilities: POINTER(Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPolicies(pmPolicies: POINTER(Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Activate(fActivate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Enable(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Synchronize(ppszItemIDs: POINTER(Windows.Win32.Foundation.PWSTR), cItems: UInt32, hwndOwner: Windows.Win32.Foundation.HWND, pSessionCreator: Windows.Win32.UI.Shell.ISyncMgrSessionCreator_head, punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrHandlerCollection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a7f337a3-d20b-45cb-9e-d7-87-d0-94-ca-50-45')
    @commethod(3)
    def GetHandlerEnumerator(ppenum: POINTER(Windows.Win32.System.Com.IEnumString_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BindToHandler(pszHandlerID: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrHandlerInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4ff1d798-ecf7-4524-aa-81-1e-36-2a-0a-ef-3a')
    @commethod(3)
    def GetType(pnType: POINTER(Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypeLabel(ppszTypeLabel: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetComment(ppszComment: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLastSyncTime(pftLastSync: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsActive() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsEnabled() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsConnected() -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrRegister(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6295df42-35ee-11d1-87-07-00-c0-4f-d9-33-27')
    @commethod(3)
    def RegisterSyncMgrHandler(clsidHandler: POINTER(Guid), pwszDescription: Windows.Win32.Foundation.PWSTR, dwSyncMgrRegisterFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterSyncMgrHandler(clsidHandler: POINTER(Guid), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHandlerRegistrationInfo(clsidHandler: POINTER(Guid), pdwSyncMgrRegisterFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrResolutionHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('40a3d052-8bff-4c4b-a3-38-d4-a3-95-70-0d-e9')
    @commethod(3)
    def QueryAbilities(pdwAbilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def KeepOther(psiOther: Windows.Win32.UI.Shell.IShellItem_head, pFeedback: POINTER(Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def KeepRecent(pFeedback: POINTER(Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveFromSyncSet(pFeedback: POINTER(Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def KeepItems(pArray: Windows.Win32.UI.Shell.ISyncMgrConflictResolutionItems_head, pFeedback: POINTER(Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrScheduleWizardUIOperation(c_void_p):
    extends: Windows.Win32.UI.Shell.ISyncMgrUIOperation
    Guid = Guid('459a6c84-21d2-4ddc-8a-53-f0-23-a4-60-66-f2')
    @commethod(4)
    def InitWizard(pszHandlerID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSessionCreator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('17f48517-f305-4321-a0-8d-b2-5a-83-49-18-fd')
    @commethod(3)
    def CreateSession(pszHandlerID: Windows.Win32.Foundation.PWSTR, ppszItemIDs: POINTER(Windows.Win32.Foundation.PWSTR), cItems: UInt32, ppCallback: POINTER(Windows.Win32.UI.Shell.ISyncMgrSyncCallback_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('884ccd87-b139-4937-a4-ba-4f-8e-19-51-3f-be')
    @commethod(3)
    def ReportProgress(pszItemID: Windows.Win32.Foundation.PWSTR, pszProgressText: Windows.Win32.Foundation.PWSTR, nStatus: Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS, uCurrentStep: UInt32, uMaxStep: UInt32, pnCancelRequest: POINTER(Windows.Win32.UI.Shell.SYNCMGR_CANCEL_REQUEST)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetHandlerProgressText(pszProgressText: Windows.Win32.Foundation.PWSTR, pnCancelRequest: POINTER(Windows.Win32.UI.Shell.SYNCMGR_CANCEL_REQUEST)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReportEvent(pszItemID: Windows.Win32.Foundation.PWSTR, nLevel: Windows.Win32.UI.Shell.SYNCMGR_EVENT_LEVEL, nFlags: Windows.Win32.UI.Shell.SYNCMGR_EVENT_FLAGS, pszName: Windows.Win32.Foundation.PWSTR, pszDescription: Windows.Win32.Foundation.PWSTR, pszLinkText: Windows.Win32.Foundation.PWSTR, pszLinkReference: Windows.Win32.Foundation.PWSTR, pszContext: Windows.Win32.Foundation.PWSTR, pguidEventID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CanContinue(pszItemID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryForAdditionalItems(ppenumItemIDs: POINTER(Windows.Win32.System.Com.IEnumString_head), ppenumPunks: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddItemToSession(pszItemID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddIUnknownToSession(punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ProposeItem(pNewItem: Windows.Win32.UI.Shell.ISyncMgrSyncItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CommitItem(pszItemID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ReportManualSync() -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncItem(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b20b24ce-2593-4f04-bd-8b-7a-d6-c4-50-51-cd')
    @commethod(3)
    def GetItemID(ppszItemID: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetName(ppszName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetItemInfo(ppItemInfo: POINTER(Windows.Win32.UI.Shell.ISyncMgrSyncItemInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(rguidObjectID: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCapabilities(pmCapabilities: POINTER(Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPolicies(pmPolicies: POINTER(Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Enable(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Delete() -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncItemContainer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('90701133-be32-4129-a6-5c-99-e6-16-ca-ff-f4')
    @commethod(3)
    def GetSyncItem(pszItemID: Windows.Win32.Foundation.PWSTR, ppItem: POINTER(Windows.Win32.UI.Shell.ISyncMgrSyncItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSyncItemEnumerator(ppenum: POINTER(Windows.Win32.UI.Shell.IEnumSyncMgrSyncItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSyncItemCount(pcItems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncItemInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e7fd9502-be0c-4464-90-a1-2b-52-77-03-12-32')
    @commethod(3)
    def GetTypeLabel(ppszTypeLabel: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetComment(ppszComment: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLastSyncTime(pftLastSync: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsEnabled() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsConnected() -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncResult(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2b90f17e-5a3e-4b33-bb-7f-1b-c4-80-56-b9-4d')
    @commethod(3)
    def Result(nStatus: Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS, cError: UInt32, cConflicts: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSynchronize(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6295df40-35ee-11d1-87-07-00-c0-4f-d9-33-27')
    @commethod(3)
    def Initialize(dwReserved: UInt32, dwSyncMgrFlags: UInt32, cbCookie: UInt32, lpCookie: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHandlerInfo(ppSyncMgrHandlerInfo: POINTER(POINTER(Windows.Win32.UI.Shell.SYNCMGRHANDLERINFO_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumSyncMgrItems(ppSyncMgrEnumItems: POINTER(Windows.Win32.UI.Shell.ISyncMgrEnumItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemObject(ItemID: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowProperties(hWndParent: Windows.Win32.Foundation.HWND, ItemID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProgressCallback(lpCallBack: Windows.Win32.UI.Shell.ISyncMgrSynchronizeCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PrepareForSync(cbNumItems: UInt32, pItemIDs: POINTER(Guid), hWndParent: Windows.Win32.Foundation.HWND, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Synchronize(hWndParent: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetItemStatus(pItemID: POINTER(Guid), dwSyncMgrStatus: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ShowError(hWndParent: Windows.Win32.Foundation.HWND, ErrorID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSynchronizeCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6295df41-35ee-11d1-87-07-00-c0-4f-d9-33-27')
    @commethod(3)
    def ShowPropertiesCompleted(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PrepareForSyncCompleted(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SynchronizeCompleted(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ShowErrorCompleted(hr: Windows.Win32.Foundation.HRESULT, cItems: UInt32, pItemIDs: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnableModeless(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Progress(ItemID: POINTER(Guid), pSyncProgressItem: POINTER(Windows.Win32.UI.Shell.SYNCMGRPROGRESSITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def LogError(dwErrorLevel: UInt32, pszErrorText: Windows.Win32.Foundation.PWSTR, pSyncLogError: POINTER(Windows.Win32.UI.Shell.SYNCMGRLOGERRORINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteLogError(ErrorID: POINTER(Guid), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EstablishConnection(pwszConnection: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSynchronizeInvoke(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6295df2c-35ee-11d1-87-07-00-c0-4f-d9-33-27')
    @commethod(3)
    def UpdateItems(dwInvokeFlags: UInt32, clsid: POINTER(Guid), cbCookie: UInt32, pCookie: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateAll() -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrUIOperation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fc7cfa47-dfe1-45b5-a0-49-8c-fd-82-be-c2-71')
    @commethod(3)
    def Run(hwndOwner: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class ITEMSPACING(Structure):
    cxSmall: Int32
    cySmall: Int32
    cxLarge: Int32
    cyLarge: Int32
class ITaskbarList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('56fdf342-fd6d-11d0-95-8a-00-60-97-c9-a0-90')
    @commethod(3)
    def HrInit() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddTab(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteTab(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ActivateTab(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetActiveAlt(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class ITaskbarList2(c_void_p):
    extends: Windows.Win32.UI.Shell.ITaskbarList
    Guid = Guid('602d4995-b13a-429b-a6-6e-19-35-e4-4f-43-17')
    @commethod(8)
    def MarkFullscreenWindow(hwnd: Windows.Win32.Foundation.HWND, fFullscreen: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ITaskbarList3(c_void_p):
    extends: Windows.Win32.UI.Shell.ITaskbarList2
    Guid = Guid('ea1afb91-9e28-4b86-90-e9-9e-9f-8a-5e-ef-af')
    @commethod(9)
    def SetProgressValue(hwnd: Windows.Win32.Foundation.HWND, ullCompleted: UInt64, ullTotal: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetProgressState(hwnd: Windows.Win32.Foundation.HWND, tbpFlags: Windows.Win32.UI.Shell.TBPFLAG) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterTab(hwndTab: Windows.Win32.Foundation.HWND, hwndMDI: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnregisterTab(hwndTab: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetTabOrder(hwndTab: Windows.Win32.Foundation.HWND, hwndInsertBefore: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetTabActive(hwndTab: Windows.Win32.Foundation.HWND, hwndMDI: Windows.Win32.Foundation.HWND, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ThumbBarAddButtons(hwnd: Windows.Win32.Foundation.HWND, cButtons: UInt32, pButton: POINTER(Windows.Win32.UI.Shell.THUMBBUTTON_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ThumbBarUpdateButtons(hwnd: Windows.Win32.Foundation.HWND, cButtons: UInt32, pButton: POINTER(Windows.Win32.UI.Shell.THUMBBUTTON_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ThumbBarSetImageList(hwnd: Windows.Win32.Foundation.HWND, himl: Windows.Win32.UI.Controls.HIMAGELIST) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetOverlayIcon(hwnd: Windows.Win32.Foundation.HWND, hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON, pszDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetThumbnailTooltip(hwnd: Windows.Win32.Foundation.HWND, pszTip: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetThumbnailClip(hwnd: Windows.Win32.Foundation.HWND, prcClip: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITaskbarList4(c_void_p):
    extends: Windows.Win32.UI.Shell.ITaskbarList3
    Guid = Guid('c43dc798-95d1-4bea-90-30-bb-99-e2-98-3a-1a')
    @commethod(21)
    def SetTabProperties(hwndTab: Windows.Win32.Foundation.HWND, stpFlags: Windows.Win32.UI.Shell.STPFLAG) -> Windows.Win32.Foundation.HRESULT: ...
class IThumbnailCache(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f676c15d-596a-4ce2-82-34-33-99-6f-44-5d-b1')
    @commethod(3)
    def GetThumbnail(pShellItem: Windows.Win32.UI.Shell.IShellItem_head, cxyRequestedThumbSize: UInt32, flags: Windows.Win32.UI.Shell.WTS_FLAGS, ppvThumb: POINTER(Windows.Win32.UI.Shell.ISharedBitmap_head), pOutFlags: POINTER(Windows.Win32.UI.Shell.WTS_CACHEFLAGS), pThumbnailID: POINTER(Windows.Win32.UI.Shell.WTS_THUMBNAILID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetThumbnailByID(thumbnailID: Windows.Win32.UI.Shell.WTS_THUMBNAILID, cxyRequestedThumbSize: UInt32, ppvThumb: POINTER(Windows.Win32.UI.Shell.ISharedBitmap_head), pOutFlags: POINTER(Windows.Win32.UI.Shell.WTS_CACHEFLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
class IThumbnailCachePrimer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0f03f8fe-2b26-46f0-96-5a-21-2a-a8-d6-6b-76')
    @commethod(3)
    def PageInThumbnail(psi: Windows.Win32.UI.Shell.IShellItem_head, wtsFlags: Windows.Win32.UI.Shell.WTS_FLAGS, cxyRequestedThumbSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IThumbnailCapture(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4ea39266-7211-409f-b6-22-f6-3d-bd-16-c5-33')
    @commethod(3)
    def CaptureThumbnail(pMaxSize: POINTER(Windows.Win32.Foundation.SIZE_head), pHTMLDoc2: Windows.Win32.System.Com.IUnknown_head, phbmThumbnail: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP)) -> Windows.Win32.Foundation.HRESULT: ...
class IThumbnailHandlerFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e35b4b2e-00da-4bc1-9f-13-38-bc-11-f5-d4-17')
    @commethod(3)
    def GetThumbnailHandler(pidlChild: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IThumbnailProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e357fccd-a995-4576-b0-1f-23-46-30-15-4e-96')
    @commethod(3)
    def GetThumbnail(cx: UInt32, phbmp: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), pdwAlpha: POINTER(Windows.Win32.UI.Shell.WTS_ALPHATYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IThumbnailSettings(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f4376f00-bef5-4d45-80-f3-1e-02-3b-bf-12-09')
    @commethod(3)
    def SetContext(dwContext: Windows.Win32.UI.Shell.WTS_CONTEXTFLAGS) -> Windows.Win32.Foundation.HRESULT: ...
class IThumbnailStreamCache(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('90e11430-9569-41d8-ae-75-6d-4d-2a-e7-cc-a0')
    @commethod(3)
    def GetThumbnailStream(path: Windows.Win32.Foundation.PWSTR, cacheId: UInt64, options: Windows.Win32.UI.Shell.ThumbnailStreamCacheOptions, requestedThumbnailSize: UInt32, thumbnailSize: POINTER(Windows.Win32.Foundation.SIZE_head), thumbnailStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetThumbnailStream(path: Windows.Win32.Foundation.PWSTR, cacheId: UInt64, thumbnailSize: Windows.Win32.Foundation.SIZE, thumbnailStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITrackShellMenu(c_void_p):
    extends: Windows.Win32.UI.Shell.IShellMenu
    Guid = Guid('8278f932-2a3e-11d2-83-8f-00-c0-4f-d9-18-d0')
    @commethod(12)
    def SetObscured(hwndTB: Windows.Win32.Foundation.HWND, punkBand: Windows.Win32.System.Com.IUnknown_head, dwSMSetFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Popup(hwnd: Windows.Win32.Foundation.HWND, ppt: POINTER(Windows.Win32.Foundation.POINTL_head), prcExclude: POINTER(Windows.Win32.Foundation.RECTL_head), dwFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class ITranscodeImage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bae86ddd-dc11-421c-b7-ab-cc-55-d1-d6-5c-44')
    @commethod(3)
    def TranscodeImage(pShellItem: Windows.Win32.UI.Shell.IShellItem_head, uiMaxWidth: UInt32, uiMaxHeight: UInt32, flags: UInt32, pvImage: Windows.Win32.System.Com.IStream_head, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ITransferAdviseSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d594d0d8-8da7-457b-b3-b4-ce-5d-ba-ac-0b-88')
    @commethod(3)
    def UpdateProgress(ullSizeCurrent: UInt64, ullSizeTotal: UInt64, nFilesCurrent: Int32, nFilesTotal: Int32, nFoldersCurrent: Int32, nFoldersTotal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateTransferState(ts: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConfirmOverwrite(psiSource: Windows.Win32.UI.Shell.IShellItem_head, psiDestParent: Windows.Win32.UI.Shell.IShellItem_head, pszName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ConfirmEncryptionLoss(psiSource: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FileFailure(psi: Windows.Win32.UI.Shell.IShellItem_head, pszItem: Windows.Win32.Foundation.PWSTR, hrError: Windows.Win32.Foundation.HRESULT, pszRename: Windows.Win32.Foundation.PWSTR, cchRename: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SubStreamFailure(psi: Windows.Win32.UI.Shell.IShellItem_head, pszStreamName: Windows.Win32.Foundation.PWSTR, hrError: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PropertyFailure(psi: Windows.Win32.UI.Shell.IShellItem_head, pkey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), hrError: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class ITransferDestination(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('48addd32-3ca5-4124-ab-e3-b5-a7-25-31-b2-07')
    @commethod(3)
    def Advise(psink: Windows.Win32.UI.Shell.ITransferAdviseSink_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateItem(pszName: Windows.Win32.Foundation.PWSTR, dwAttributes: UInt32, ullSize: UInt64, flags: UInt32, riidItem: POINTER(Guid), ppvItem: POINTER(c_void_p), riidResources: POINTER(Guid), ppvResources: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ITransferMediumItem(c_void_p):
    extends: Windows.Win32.UI.Shell.IRelatedItem
    Guid = Guid('77f295d5-2d6f-4e19-b8-ae-32-2f-3e-72-1a-b5')
class ITransferSource(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00adb003-bde9-45c6-8e-29-d0-9f-93-53-e1-08')
    @commethod(3)
    def Advise(psink: Windows.Win32.UI.Shell.ITransferAdviseSink_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperties(pproparray: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChangeArray_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenItem(psi: Windows.Win32.UI.Shell.IShellItem_head, flags: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def MoveItem(psi: Windows.Win32.UI.Shell.IShellItem_head, psiParentDst: Windows.Win32.UI.Shell.IShellItem_head, pszNameDst: Windows.Win32.Foundation.PWSTR, flags: UInt32, ppsiNew: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RecycleItem(psiSource: Windows.Win32.UI.Shell.IShellItem_head, psiParentDest: Windows.Win32.UI.Shell.IShellItem_head, flags: UInt32, ppsiNewDest: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveItem(psiSource: Windows.Win32.UI.Shell.IShellItem_head, flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RenameItem(psiSource: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR, flags: UInt32, ppsiNewDest: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def LinkItem(psiSource: Windows.Win32.UI.Shell.IShellItem_head, psiParentDest: Windows.Win32.UI.Shell.IShellItem_head, pszNewName: Windows.Win32.Foundation.PWSTR, flags: UInt32, ppsiNewDest: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ApplyPropertiesToItem(psiSource: Windows.Win32.UI.Shell.IShellItem_head, ppsiNew: POINTER(Windows.Win32.UI.Shell.IShellItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefaultDestinationName(psiSource: Windows.Win32.UI.Shell.IShellItem_head, psiParentDest: Windows.Win32.UI.Shell.IShellItem_head, ppszDestinationName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnterFolder(psiChildFolderDest: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LeaveFolder(psiChildFolderDest: Windows.Win32.UI.Shell.IShellItem_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITravelEntry(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f46edb3b-bc2f-11d0-94-12-00-aa-00-a3-eb-d3')
    @commethod(3)
    def Invoke(punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Update(punk: Windows.Win32.System.Com.IUnknown_head, fIsLocalAnchor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPidl(ppidl: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class ITravelLog(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('66a9cb08-4802-11d2-a5-61-00-a0-c9-2d-bf-e8')
    @commethod(3)
    def AddEntry(punk: Windows.Win32.System.Com.IUnknown_head, fIsLocalAnchor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateEntry(punk: Windows.Win32.System.Com.IUnknown_head, fIsLocalAnchor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateExternal(punk: Windows.Win32.System.Com.IUnknown_head, punkHLBrowseContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Travel(punk: Windows.Win32.System.Com.IUnknown_head, iOffset: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTravelEntry(punk: Windows.Win32.System.Com.IUnknown_head, iOffset: Int32, ppte: POINTER(Windows.Win32.UI.Shell.ITravelEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindTravelEntry(punk: Windows.Win32.System.Com.IUnknown_head, pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppte: POINTER(Windows.Win32.UI.Shell.ITravelEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetToolTipText(punk: Windows.Win32.System.Com.IUnknown_head, iOffset: Int32, idsTemplate: Int32, pwzText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def InsertMenuEntries(punk: Windows.Win32.System.Com.IUnknown_head, hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, nPos: Int32, idFirst: Int32, idLast: Int32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(pptl: POINTER(Windows.Win32.UI.Shell.ITravelLog_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CountEntries(punk: Windows.Win32.System.Com.IUnknown_head) -> UInt32: ...
    @commethod(13)
    def Revert() -> Windows.Win32.Foundation.HRESULT: ...
class ITravelLogClient(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('241c033e-e659-43da-aa-4d-40-86-db-c4-75-8d')
    @commethod(3)
    def FindWindowByIndex(dwID: UInt32, ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWindowData(pStream: Windows.Win32.System.Com.IStream_head, pWinData: POINTER(Windows.Win32.UI.Shell.WINDOWDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadHistoryPosition(pszUrlLocation: Windows.Win32.Foundation.PWSTR, dwPosition: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITravelLogEntry(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7ebfdd87-ad18-11d3-a4-c5-00-c0-4f-72-d6-b8')
    @commethod(3)
    def GetTitle(ppszTitle: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetURL(ppszURL: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ITravelLogStg(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7ebfdd80-ad18-11d3-a4-c5-00-c0-4f-72-d6-b8')
    @commethod(3)
    def CreateEntry(pszUrl: Windows.Win32.Foundation.PWSTR, pszTitle: Windows.Win32.Foundation.PWSTR, ptleRelativeTo: Windows.Win32.UI.Shell.ITravelLogEntry_head, fPrepend: Windows.Win32.Foundation.BOOL, pptle: POINTER(Windows.Win32.UI.Shell.ITravelLogEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TravelTo(ptle: Windows.Win32.UI.Shell.ITravelLogEntry_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumEntries(flags: Windows.Win32.UI.Shell.TLENUMF, ppenum: POINTER(Windows.Win32.UI.Shell.IEnumTravelLogEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindEntries(flags: Windows.Win32.UI.Shell.TLENUMF, pszUrl: Windows.Win32.Foundation.PWSTR, ppenum: POINTER(Windows.Win32.UI.Shell.IEnumTravelLogEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(flags: Windows.Win32.UI.Shell.TLENUMF, pcEntries: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveEntry(ptle: Windows.Win32.UI.Shell.ITravelLogEntry_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRelativeEntry(iOffset: Int32, ptle: POINTER(Windows.Win32.UI.Shell.ITravelLogEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITrayDeskBand(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6d67e846-5b9c-4db8-9c-bc-dd-e1-2f-42-54-f1')
    @commethod(3)
    def ShowDeskBand(clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HideDeskBand(clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsDeskBandShown(clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeskBandRegistrationChanged() -> Windows.Win32.Foundation.HRESULT: ...
class IURLSearchHook(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ac60f6a0-0fd9-11d0-99-cb-00-c0-4f-d6-44-97')
    @commethod(3)
    def Translate(pwszSearchURL: Windows.Win32.Foundation.PWSTR, cchBufferSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IURLSearchHook2(c_void_p):
    extends: Windows.Win32.UI.Shell.IURLSearchHook
    Guid = Guid('5ee44da4-6d32-46e3-86-bc-07-54-0d-ed-d0-e0')
    @commethod(4)
    def TranslateWithSearchContext(pwszSearchURL: Windows.Win32.Foundation.PWSTR, cchBufferSize: UInt32, pSearchContext: Windows.Win32.UI.Shell.ISearchContext_head) -> Windows.Win32.Foundation.HRESULT: ...
IURL_INVOKECOMMAND_FLAGS = Int32
IURL_INVOKECOMMAND_FL_ALLOW_UI: IURL_INVOKECOMMAND_FLAGS = 1
IURL_INVOKECOMMAND_FL_USE_DEFAULT_VERB: IURL_INVOKECOMMAND_FLAGS = 2
IURL_INVOKECOMMAND_FL_DDEWAIT: IURL_INVOKECOMMAND_FLAGS = 4
IURL_INVOKECOMMAND_FL_ASYNCOK: IURL_INVOKECOMMAND_FLAGS = 8
IURL_INVOKECOMMAND_FL_LOG_USAGE: IURL_INVOKECOMMAND_FLAGS = 16
IURL_SETURL_FLAGS = Int32
IURL_SETURL_FL_GUESS_PROTOCOL: IURL_SETURL_FLAGS = 1
IURL_SETURL_FL_USE_DEFAULT_PROTOCOL: IURL_SETURL_FLAGS = 2
class IUniformResourceLocatorA(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fbf23b80-e3f0-101b-84-88-00-aa-00-3e-56-f8')
    @commethod(3)
    def SetURL(pcszURL: Windows.Win32.Foundation.PSTR, dwInFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetURL(ppszURL: POINTER(Windows.Win32.Foundation.PSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InvokeCommand(purlici: POINTER(Windows.Win32.UI.Shell.URLINVOKECOMMANDINFOA_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUniformResourceLocatorW(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cabb0da0-da57-11cf-99-74-00-20-af-d7-97-62')
    @commethod(3)
    def SetURL(pcszURL: Windows.Win32.Foundation.PWSTR, dwInFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetURL(ppszURL: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InvokeCommand(purlici: POINTER(Windows.Win32.UI.Shell.URLINVOKECOMMANDINFOW_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUpdateIDList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6589b6d2-5f8d-4b9e-b7-e0-23-cd-d9-71-7d-8c')
    @commethod(3)
    def Update(pbc: Windows.Win32.System.Com.IBindCtx_head, pidlIn: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head), ppidlOut: POINTER(POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IUseToBrowseItem(c_void_p):
    extends: Windows.Win32.UI.Shell.IRelatedItem
    Guid = Guid('05edda5c-98a3-4717-8a-db-c5-e7-da-99-1e-b1')
class IUserAccountChangeCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a561e69a-b4b8-4113-91-a5-64-c6-bc-ca-34-30')
    @commethod(3)
    def OnPictureChange(pszUserName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IUserNotification(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ba9711ba-5893-4787-a7-e1-41-27-71-51-55-0b')
    @commethod(3)
    def SetBalloonInfo(pszTitle: Windows.Win32.Foundation.PWSTR, pszText: Windows.Win32.Foundation.PWSTR, dwInfoFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBalloonRetry(dwShowTime: UInt32, dwInterval: UInt32, cRetryCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIconInfo(hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON, pszToolTip: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Show(pqc: Windows.Win32.UI.Shell.IQueryContinue_head, dwContinuePollInterval: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PlaySound(pszSoundName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IUserNotification2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('215913cc-57eb-4fab-ab-5a-e5-fa-7b-ea-2a-6c')
    @commethod(3)
    def SetBalloonInfo(pszTitle: Windows.Win32.Foundation.PWSTR, pszText: Windows.Win32.Foundation.PWSTR, dwInfoFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBalloonRetry(dwShowTime: UInt32, dwInterval: UInt32, cRetryCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIconInfo(hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON, pszToolTip: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Show(pqc: Windows.Win32.UI.Shell.IQueryContinue_head, dwContinuePollInterval: UInt32, pSink: Windows.Win32.UI.Shell.IUserNotificationCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PlaySound(pszSoundName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IUserNotificationCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('19108294-0441-4aff-80-13-fa-0a-73-0b-0b-ea')
    @commethod(3)
    def OnBalloonUserClick(pt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnLeftClick(pt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnContextMenu(pt: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IViewStateIdentityItem(c_void_p):
    extends: Windows.Win32.UI.Shell.IRelatedItem
    Guid = Guid('9d264146-a94f-4195-9f-9f-3b-b1-2c-e0-c9-55')
class IVirtualDesktopManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a5cd92ff-29be-454c-8d-04-d8-28-79-fb-3f-1b')
    @commethod(3)
    def IsWindowOnCurrentVirtualDesktop(topLevelWindow: Windows.Win32.Foundation.HWND, onCurrentDesktop: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWindowDesktopId(topLevelWindow: Windows.Win32.Foundation.HWND, desktopId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveWindowToDesktop(topLevelWindow: Windows.Win32.Foundation.HWND, desktopId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IVisualProperties(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e693cf68-d967-4112-87-63-99-17-2a-ee-5e-5a')
    @commethod(3)
    def SetWatermark(hbmp: Windows.Win32.Graphics.Gdi.HBITMAP, vpwf: Windows.Win32.UI.Shell.VPWATERMARKFLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetColor(vpcf: Windows.Win32.UI.Shell.VPCOLORFLAGS, cr: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetColor(vpcf: Windows.Win32.UI.Shell.VPCOLORFLAGS, pcr: POINTER(Windows.Win32.Foundation.COLORREF)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetItemHeight(cyItemInPixels: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetItemHeight(cyItemInPixels: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFont(plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head), bRedraw: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFont(plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetTheme(pszSubAppName: Windows.Win32.Foundation.PWSTR, pszSubIdList: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWebBrowser(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('eab22ac1-30c1-11cf-a7-eb-00-00-c0-5b-ae-0b')
    @commethod(7)
    def GoBack() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GoForward() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GoHome() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GoSearch() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Navigate(URL: Windows.Win32.Foundation.BSTR, Flags: POINTER(Windows.Win32.System.Com.VARIANT_head), TargetFrameName: POINTER(Windows.Win32.System.Com.VARIANT_head), PostData: POINTER(Windows.Win32.System.Com.VARIANT_head), Headers: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Refresh() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Refresh2(Level: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Stop() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Application(ppDisp: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Parent(ppDisp: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Container(ppDisp: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Document(ppDisp: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_TopLevelContainer(pBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Type(Type: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Left(pl: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Left(Left: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Top(pl: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_Top(Top: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Width(pl: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Width(Width: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Height(pl: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Height(Height: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_LocationName(LocationName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_LocationURL(LocationURL: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_Busy(pBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IWebBrowser2(c_void_p):
    extends: Windows.Win32.UI.Shell.IWebBrowserApp
    Guid = Guid('d30c1661-cdaf-11d0-8a-3e-00-c0-4f-c9-e2-6e')
    @commethod(52)
    def Navigate2(URL: POINTER(Windows.Win32.System.Com.VARIANT_head), Flags: POINTER(Windows.Win32.System.Com.VARIANT_head), TargetFrameName: POINTER(Windows.Win32.System.Com.VARIANT_head), PostData: POINTER(Windows.Win32.System.Com.VARIANT_head), Headers: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def QueryStatusWB(cmdID: Windows.Win32.System.Ole.OLECMDID, pcmdf: POINTER(Windows.Win32.System.Ole.OLECMDF)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def ExecWB(cmdID: Windows.Win32.System.Ole.OLECMDID, cmdexecopt: Windows.Win32.System.Ole.OLECMDEXECOPT, pvaIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvaOut: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def ShowBrowserBar(pvaClsid: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarShow: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarSize: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def get_ReadyState(plReadyState: POINTER(Windows.Win32.System.Ole.READYSTATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_Offline(pbOffline: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_Offline(bOffline: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_Silent(pbSilent: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_Silent(bSilent: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def get_RegisterAsBrowser(pbRegister: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def put_RegisterAsBrowser(bRegister: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def get_RegisterAsDropTarget(pbRegister: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def put_RegisterAsDropTarget(bRegister: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_TheaterMode(pbRegister: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def put_TheaterMode(bRegister: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_AddressBar(Value: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def put_AddressBar(Value: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_Resizable(Value: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def put_Resizable(Value: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IWebBrowserApp(c_void_p):
    extends: Windows.Win32.UI.Shell.IWebBrowser
    Guid = Guid('0002df05-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(32)
    def Quit() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def ClientToWindow(pcx: POINTER(Int32), pcy: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def PutProperty(Property: Windows.Win32.Foundation.BSTR, vtValue: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetProperty(Property: Windows.Win32.Foundation.BSTR, pvtValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_Name(Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_HWND(pHWND: POINTER(Windows.Win32.Foundation.SHANDLE_PTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_FullName(FullName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_Path(Path: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_Visible(pBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_Visible(Value: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_StatusBar(pBool: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_StatusBar(Value: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_StatusText(StatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_StatusText(StatusText: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_ToolBar(Value: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_ToolBar(Value: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_MenuBar(Value: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_MenuBar(Value: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_FullScreen(pbFullScreen: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_FullScreen(bFullScreen: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IWebWizardExtension(c_void_p):
    extends: Windows.Win32.UI.Shell.IWizardExtension
    Guid = Guid('0e6b3f66-98d1-48c0-a2-22-fb-de-74-e2-fb-c5')
    @commethod(6)
    def SetInitialURL(pszURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetErrorURL(pszErrorURL: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWebWizardHost(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('18bcc359-4990-4bfb-b9-51-3c-83-70-2b-e5-f9')
    @commethod(7)
    def FinalBack() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FinalNext() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Cancel() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Caption(bstrCaption: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Caption(pbstrCaption: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Property(bstrPropertyName: Windows.Win32.Foundation.BSTR, pvProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Property(bstrPropertyName: Windows.Win32.Foundation.BSTR, pvProperty: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetWizardButtons(vfEnableBack: Windows.Win32.Foundation.VARIANT_BOOL, vfEnableNext: Windows.Win32.Foundation.VARIANT_BOOL, vfLastPage: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetHeaderText(bstrHeaderTitle: Windows.Win32.Foundation.BSTR, bstrHeaderSubtitle: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWebWizardHost2(c_void_p):
    extends: Windows.Win32.UI.Shell.IWebWizardHost
    Guid = Guid('f9c013dc-3c23-4041-8e-39-cf-b4-02-f7-ea-59')
    @commethod(16)
    def SignString(value: Windows.Win32.Foundation.BSTR, signedValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IWizardExtension(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c02ea696-86cc-491e-9b-23-74-39-4a-04-44-a8')
    @commethod(3)
    def AddPages(aPages: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE), cPages: UInt32, pnPagesAdded: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFirstPage(phpage: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLastPage(phpage: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> Windows.Win32.Foundation.HRESULT: ...
class IWizardSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('88960f5b-422f-4e7b-80-13-73-41-53-81-c3-c3')
    @commethod(3)
    def GetPreviousPage(phpage: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNextPage(phpage: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCancelledPage(phpage: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> Windows.Win32.Foundation.HRESULT: ...
ImageProperties = Guid('7ab770c7-0e23-4d7a-8a-a2-19-bf-ad-47-98-29')
ImageRecompress = Guid('6e33091c-d2f8-4740-b5-5e-2e-11-d1-47-7a-2c')
ImageTranscode = Guid('17b75166-928f-417d-96-85-64-aa-13-55-65-c1')
InputPanelConfiguration = Guid('2853add3-f096-4c63-a7-8f-7f-a3-ea-83-7f-b7')
InternetExplorer = Guid('0002df01-0000-0000-c0-00-00-00-00-00-00-46')
InternetExplorerMedium = Guid('d5e8041d-920f-45e9-b8-fb-b1-de-b8-2c-6e-5e')
InternetPrintOrdering = Guid('add36aa8-751a-4579-a2-66-d6-6f-52-02-cc-bb')
KF_CATEGORY = Int32
KF_CATEGORY_VIRTUAL: KF_CATEGORY = 1
KF_CATEGORY_FIXED: KF_CATEGORY = 2
KF_CATEGORY_COMMON: KF_CATEGORY = 3
KF_CATEGORY_PERUSER: KF_CATEGORY = 4
KNOWNDESTCATEGORY = Int32
KDC_FREQUENT: KNOWNDESTCATEGORY = 1
KDC_RECENT: KNOWNDESTCATEGORY = 2
class KNOWNFOLDER_DEFINITION(Structure):
    category: Windows.Win32.UI.Shell.KF_CATEGORY
    pszName: Windows.Win32.Foundation.PWSTR
    pszDescription: Windows.Win32.Foundation.PWSTR
    fidParent: Guid
    pszRelativePath: Windows.Win32.Foundation.PWSTR
    pszParsingName: Windows.Win32.Foundation.PWSTR
    pszTooltip: Windows.Win32.Foundation.PWSTR
    pszLocalizedName: Windows.Win32.Foundation.PWSTR
    pszIcon: Windows.Win32.Foundation.PWSTR
    pszSecurity: Windows.Win32.Foundation.PWSTR
    dwAttributes: UInt32
    kfdFlags: UInt32
    ftidType: Guid
KNOWN_FOLDER_FLAG = Int32
KF_FLAG_DEFAULT: KNOWN_FOLDER_FLAG = 0
KF_FLAG_FORCE_APP_DATA_REDIRECTION: KNOWN_FOLDER_FLAG = 524288
KF_FLAG_RETURN_FILTER_REDIRECTION_TARGET: KNOWN_FOLDER_FLAG = 262144
KF_FLAG_FORCE_PACKAGE_REDIRECTION: KNOWN_FOLDER_FLAG = 131072
KF_FLAG_NO_PACKAGE_REDIRECTION: KNOWN_FOLDER_FLAG = 65536
KF_FLAG_FORCE_APPCONTAINER_REDIRECTION: KNOWN_FOLDER_FLAG = 131072
KF_FLAG_NO_APPCONTAINER_REDIRECTION: KNOWN_FOLDER_FLAG = 65536
KF_FLAG_CREATE: KNOWN_FOLDER_FLAG = 32768
KF_FLAG_DONT_VERIFY: KNOWN_FOLDER_FLAG = 16384
KF_FLAG_DONT_UNEXPAND: KNOWN_FOLDER_FLAG = 8192
KF_FLAG_NO_ALIAS: KNOWN_FOLDER_FLAG = 4096
KF_FLAG_INIT: KNOWN_FOLDER_FLAG = 2048
KF_FLAG_DEFAULT_PATH: KNOWN_FOLDER_FLAG = 1024
KF_FLAG_NOT_PARENT_RELATIVE: KNOWN_FOLDER_FLAG = 512
KF_FLAG_SIMPLE_IDLIST: KNOWN_FOLDER_FLAG = 256
KF_FLAG_ALIAS_ONLY: KNOWN_FOLDER_FLAG = -2147483648
KnownFolderManager = Guid('4df0c730-df9d-4ae3-91-53-aa-6b-82-e9-79-5a')
LIBRARYFOLDERFILTER = Int32
LFF_FORCEFILESYSTEM: LIBRARYFOLDERFILTER = 1
LFF_STORAGEITEMS: LIBRARYFOLDERFILTER = 2
LFF_ALLITEMS: LIBRARYFOLDERFILTER = 3
LIBRARYMANAGEDIALOGOPTIONS = Int32
LMD_DEFAULT: LIBRARYMANAGEDIALOGOPTIONS = 0
LMD_ALLOWUNINDEXABLENETWORKLOCATIONS: LIBRARYMANAGEDIALOGOPTIONS = 1
LIBRARYOPTIONFLAGS = Int32
LOF_DEFAULT: LIBRARYOPTIONFLAGS = 0
LOF_PINNEDTONAVPANE: LIBRARYOPTIONFLAGS = 1
LOF_MASK_ALL: LIBRARYOPTIONFLAGS = 1
LIBRARYSAVEFLAGS = Int32
LSF_FAILIFTHERE: LIBRARYSAVEFLAGS = 0
LSF_OVERRIDEEXISTING: LIBRARYSAVEFLAGS = 1
LSF_MAKEUNIQUENAME: LIBRARYSAVEFLAGS = 2
@winfunctype_pointer
def LPFNDFMCALLBACK(psf: Windows.Win32.UI.Shell.IShellFolder_head, hwnd: Windows.Win32.Foundation.HWND, pdtobj: Windows.Win32.System.Com.IDataObject_head, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNVIEWCALLBACK(psvOuter: Windows.Win32.UI.Shell.IShellView_head, psf: Windows.Win32.UI.Shell.IShellFolder_head, hwndMain: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
LocalThumbnailCache = Guid('50ef4544-ac9f-4a8e-b2-1b-8a-26-18-0d-b1-3f')
MENUBANDHANDLERCID = Int32
MBHANDCID_PIDLSELECT: MENUBANDHANDLERCID = 0
MENUPOPUPPOPUPFLAGS = Int32
MPPF_SETFOCUS: MENUPOPUPPOPUPFLAGS = 1
MPPF_INITIALSELECT: MENUPOPUPPOPUPFLAGS = 2
MPPF_NOANIMATE: MENUPOPUPPOPUPFLAGS = 4
MPPF_KEYBOARD: MENUPOPUPPOPUPFLAGS = 16
MPPF_REPOSITION: MENUPOPUPPOPUPFLAGS = 32
MPPF_FORCEZORDER: MENUPOPUPPOPUPFLAGS = 64
MPPF_FINALSELECT: MENUPOPUPPOPUPFLAGS = 128
MPPF_TOP: MENUPOPUPPOPUPFLAGS = 536870912
MPPF_LEFT: MENUPOPUPPOPUPFLAGS = 1073741824
MPPF_RIGHT: MENUPOPUPPOPUPFLAGS = 1610612736
MPPF_BOTTOM: MENUPOPUPPOPUPFLAGS = -2147483648
MPPF_POS_MASK: MENUPOPUPPOPUPFLAGS = -536870912
MPPF_ALIGN_LEFT: MENUPOPUPPOPUPFLAGS = 33554432
MPPF_ALIGN_RIGHT: MENUPOPUPPOPUPFLAGS = 67108864
MENUPOPUPSELECT = Int32
MPOS_EXECUTE: MENUPOPUPSELECT = 0
MPOS_FULLCANCEL: MENUPOPUPSELECT = 1
MPOS_CANCELLEVEL: MENUPOPUPSELECT = 2
MPOS_SELECTLEFT: MENUPOPUPSELECT = 3
MPOS_SELECTRIGHT: MENUPOPUPSELECT = 4
MPOS_CHILDTRACKING: MENUPOPUPSELECT = 5
MERGE_UPDATE_STATUS = Int32
MUS_COMPLETE: MERGE_UPDATE_STATUS = 0
MUS_USERINPUTNEEDED: MERGE_UPDATE_STATUS = 1
MUS_FAILED: MERGE_UPDATE_STATUS = 2
MIMEASSOCIATIONDIALOG_IN_FLAGS = Int32
MIMEASSOCDLG_FL_REGISTER_ASSOC: MIMEASSOCIATIONDIALOG_IN_FLAGS = 1
MM_FLAGS = UInt32
MM_ADDSEPARATOR: MM_FLAGS = 1
MM_SUBMENUSHAVEIDS: MM_FLAGS = 2
MM_DONTREMOVESEPS: MM_FLAGS = 4
MONITOR_APP_VISIBILITY = Int32
MAV_UNKNOWN: MONITOR_APP_VISIBILITY = 0
MAV_NO_APP_VISIBLE: MONITOR_APP_VISIBILITY = 1
MAV_APP_VISIBLE: MONITOR_APP_VISIBILITY = 2
class MULTIKEYHELPA(Structure):
    mkSize: UInt32
    mkKeylist: Windows.Win32.Foundation.CHAR
    szKeyphrase: Windows.Win32.Foundation.CHAR * 1
class MULTIKEYHELPW(Structure):
    mkSize: UInt32
    mkKeylist: Char
    szKeyphrase: Char * 1
MailRecipient = Guid('9e56be60-c50f-11cf-9a-2c-00-a0-c9-0a-90-ce')
MergedCategorizer = Guid('8e827c11-33e7-4bc1-b2-42-8c-d9-a1-c2-b3-04')
NAMESPACEWALKFLAG = Int32
NSWF_DEFAULT: NAMESPACEWALKFLAG = 0
NSWF_NONE_IMPLIES_ALL: NAMESPACEWALKFLAG = 1
NSWF_ONE_IMPLIES_ALL: NAMESPACEWALKFLAG = 2
NSWF_DONT_TRAVERSE_LINKS: NAMESPACEWALKFLAG = 4
NSWF_DONT_ACCUMULATE_RESULT: NAMESPACEWALKFLAG = 8
NSWF_TRAVERSE_STREAM_JUNCTIONS: NAMESPACEWALKFLAG = 16
NSWF_FILESYSTEM_ONLY: NAMESPACEWALKFLAG = 32
NSWF_SHOW_PROGRESS: NAMESPACEWALKFLAG = 64
NSWF_FLAG_VIEWORDER: NAMESPACEWALKFLAG = 128
NSWF_IGNORE_AUTOPLAY_HIDA: NAMESPACEWALKFLAG = 256
NSWF_ASYNC: NAMESPACEWALKFLAG = 512
NSWF_DONT_RESOLVE_LINKS: NAMESPACEWALKFLAG = 1024
NSWF_ACCUMULATE_FOLDERS: NAMESPACEWALKFLAG = 2048
NSWF_DONT_SORT: NAMESPACEWALKFLAG = 4096
NSWF_USE_TRANSFER_MEDIUM: NAMESPACEWALKFLAG = 8192
NSWF_DONT_TRAVERSE_STREAM_JUNCTIONS: NAMESPACEWALKFLAG = 16384
NSWF_ANY_IMPLIES_ALL: NAMESPACEWALKFLAG = 32768
NATIVE_DISPLAY_ORIENTATION = Int32
NDO_LANDSCAPE: NATIVE_DISPLAY_ORIENTATION = 0
NDO_PORTRAIT: NATIVE_DISPLAY_ORIENTATION = 1
class NC_ADDRESS(Structure):
    pAddrInfo: POINTER(NET_ADDRESS_INFO)
    PortNumber: UInt16
    PrefixLength: Byte
    class NET_ADDRESS_INFO(Structure):
        pass
class NEWCPLINFOA(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwHelpContext: UInt32
    lData: IntPtr
    hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
    szName: Windows.Win32.Foundation.CHAR * 32
    szInfo: Windows.Win32.Foundation.CHAR * 64
    szHelpFile: Windows.Win32.Foundation.CHAR * 128
    _pack_ = 1
class NEWCPLINFOW(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwHelpContext: UInt32
    lData: IntPtr
    hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
    szName: Char * 32
    szInfo: Char * 64
    szHelpFile: Char * 128
    _pack_ = 1
if ARCH in 'X64,ARM64':
    class NOTIFYICONDATAA(Structure):
        cbSize: UInt32
        hWnd: Windows.Win32.Foundation.HWND
        uID: UInt32
        uFlags: Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS
        uCallbackMessage: UInt32
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        szTip: Windows.Win32.Foundation.CHAR * 128
        dwState: Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        dwStateMask: UInt32
        szInfo: Windows.Win32.Foundation.CHAR * 256
        Anonymous: _Anonymous_e__Union
        szInfoTitle: Windows.Win32.Foundation.CHAR * 64
        dwInfoFlags: Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS
        guidItem: Guid
        hBalloonIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        class _Anonymous_e__Union(Union):
            uTimeout: UInt32
            uVersion: UInt32
if ARCH in 'X86':
    class NOTIFYICONDATAA(Structure):
        cbSize: UInt32
        hWnd: Windows.Win32.Foundation.HWND
        uID: UInt32
        uFlags: Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS
        uCallbackMessage: UInt32
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        szTip: Windows.Win32.Foundation.CHAR * 128
        dwState: Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        dwStateMask: UInt32
        szInfo: Windows.Win32.Foundation.CHAR * 256
        Anonymous: _Anonymous_e__Union
        szInfoTitle: Windows.Win32.Foundation.CHAR * 64
        dwInfoFlags: Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS
        guidItem: Guid
        hBalloonIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        _pack_ = 1
        class _Anonymous_e__Union(Union):
            uTimeout: UInt32
            uVersion: UInt32
            _pack_ = 1
if ARCH in 'X64,ARM64':
    class NOTIFYICONDATAW(Structure):
        cbSize: UInt32
        hWnd: Windows.Win32.Foundation.HWND
        uID: UInt32
        uFlags: Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS
        uCallbackMessage: UInt32
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        szTip: Char * 128
        dwState: Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        dwStateMask: UInt32
        szInfo: Char * 256
        Anonymous: _Anonymous_e__Union
        szInfoTitle: Char * 64
        dwInfoFlags: Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS
        guidItem: Guid
        hBalloonIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        class _Anonymous_e__Union(Union):
            uTimeout: UInt32
            uVersion: UInt32
if ARCH in 'X86':
    class NOTIFYICONDATAW(Structure):
        cbSize: UInt32
        hWnd: Windows.Win32.Foundation.HWND
        uID: UInt32
        uFlags: Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS
        uCallbackMessage: UInt32
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        szTip: Char * 128
        dwState: Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        dwStateMask: UInt32
        szInfo: Char * 256
        Anonymous: _Anonymous_e__Union
        szInfoTitle: Char * 64
        dwInfoFlags: Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS
        guidItem: Guid
        hBalloonIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        _pack_ = 1
        class _Anonymous_e__Union(Union):
            uTimeout: UInt32
            uVersion: UInt32
            _pack_ = 1
if ARCH in 'X64,ARM64':
    class NOTIFYICONIDENTIFIER(Structure):
        cbSize: UInt32
        hWnd: Windows.Win32.Foundation.HWND
        uID: UInt32
        guidItem: Guid
if ARCH in 'X86':
    class NOTIFYICONIDENTIFIER(Structure):
        cbSize: UInt32
        hWnd: Windows.Win32.Foundation.HWND
        uID: UInt32
        guidItem: Guid
        _pack_ = 1
NOTIFY_ICON_DATA_FLAGS = UInt32
NIF_MESSAGE: NOTIFY_ICON_DATA_FLAGS = 1
NIF_ICON: NOTIFY_ICON_DATA_FLAGS = 2
NIF_TIP: NOTIFY_ICON_DATA_FLAGS = 4
NIF_STATE: NOTIFY_ICON_DATA_FLAGS = 8
NIF_INFO: NOTIFY_ICON_DATA_FLAGS = 16
NIF_GUID: NOTIFY_ICON_DATA_FLAGS = 32
NIF_REALTIME: NOTIFY_ICON_DATA_FLAGS = 64
NIF_SHOWTIP: NOTIFY_ICON_DATA_FLAGS = 128
NOTIFY_ICON_INFOTIP_FLAGS = UInt32
NIIF_NONE: NOTIFY_ICON_INFOTIP_FLAGS = 0
NIIF_INFO: NOTIFY_ICON_INFOTIP_FLAGS = 1
NIIF_WARNING: NOTIFY_ICON_INFOTIP_FLAGS = 2
NIIF_ERROR: NOTIFY_ICON_INFOTIP_FLAGS = 3
NIIF_USER: NOTIFY_ICON_INFOTIP_FLAGS = 4
NIIF_ICON_MASK: NOTIFY_ICON_INFOTIP_FLAGS = 15
NIIF_NOSOUND: NOTIFY_ICON_INFOTIP_FLAGS = 16
NIIF_LARGE_ICON: NOTIFY_ICON_INFOTIP_FLAGS = 32
NIIF_RESPECT_QUIET_TIME: NOTIFY_ICON_INFOTIP_FLAGS = 128
NOTIFY_ICON_MESSAGE = UInt32
NIM_ADD: NOTIFY_ICON_MESSAGE = 0
NIM_MODIFY: NOTIFY_ICON_MESSAGE = 1
NIM_DELETE: NOTIFY_ICON_MESSAGE = 2
NIM_SETFOCUS: NOTIFY_ICON_MESSAGE = 3
NIM_SETVERSION: NOTIFY_ICON_MESSAGE = 4
NOTIFY_ICON_STATE = UInt32
NIS_HIDDEN: NOTIFY_ICON_STATE = 1
NIS_SHAREDICON: NOTIFY_ICON_STATE = 2
NPCredentialProvider = Guid('3dd6bec0-8193-4ffe-ae-25-e0-8e-39-ea-40-63')
class NRESARRAY(Structure):
    cItems: UInt32
    nr: Windows.Win32.NetworkManagement.WNet.NETRESOURCEA * 1
class NSTCCUSTOMDRAW(Structure):
    psi: Windows.Win32.UI.Shell.IShellItem_head
    uItemState: UInt32
    nstcis: UInt32
    pszText: Windows.Win32.Foundation.PWSTR
    iImage: Int32
    himl: Windows.Win32.UI.Controls.HIMAGELIST
    iLevel: Int32
    iIndent: Int32
NSTCFOLDERCAPABILITIES = Int32
NSTCFC_NONE: NSTCFOLDERCAPABILITIES = 0
NSTCFC_PINNEDITEMFILTERING: NSTCFOLDERCAPABILITIES = 1
NSTCFC_DELAY_REGISTER_NOTIFY: NSTCFOLDERCAPABILITIES = 2
NSTCGNI = Int32
NSTCGNI_NEXT: NSTCGNI = 0
NSTCGNI_NEXTVISIBLE: NSTCGNI = 1
NSTCGNI_PREV: NSTCGNI = 2
NSTCGNI_PREVVISIBLE: NSTCGNI = 3
NSTCGNI_PARENT: NSTCGNI = 4
NSTCGNI_CHILD: NSTCGNI = 5
NSTCGNI_FIRSTVISIBLE: NSTCGNI = 6
NSTCGNI_LASTVISIBLE: NSTCGNI = 7
NSTCSTYLE2 = Int32
NSTCS2_DEFAULT: NSTCSTYLE2 = 0
NSTCS2_INTERRUPTNOTIFICATIONS: NSTCSTYLE2 = 1
NSTCS2_SHOWNULLSPACEMENU: NSTCSTYLE2 = 2
NSTCS2_DISPLAYPADDING: NSTCSTYLE2 = 4
NSTCS2_DISPLAYPINNEDONLY: NSTCSTYLE2 = 8
NTSCS2_NOSINGLETONAUTOEXPAND: NSTCSTYLE2 = 16
NTSCS2_NEVERINSERTNONENUMERATED: NSTCSTYLE2 = 32
class NT_CONSOLE_PROPS(Structure):
    dbh: Windows.Win32.UI.Shell.DATABLOCK_HEADER
    wFillAttribute: UInt16
    wPopupFillAttribute: UInt16
    dwScreenBufferSize: Windows.Win32.System.Console.COORD
    dwWindowSize: Windows.Win32.System.Console.COORD
    dwWindowOrigin: Windows.Win32.System.Console.COORD
    nFont: UInt32
    nInputBufferSize: UInt32
    dwFontSize: Windows.Win32.System.Console.COORD
    uFontFamily: UInt32
    uFontWeight: UInt32
    FaceName: Char * 32
    uCursorSize: UInt32
    bFullScreen: Windows.Win32.Foundation.BOOL
    bQuickEdit: Windows.Win32.Foundation.BOOL
    bInsertMode: Windows.Win32.Foundation.BOOL
    bAutoPosition: Windows.Win32.Foundation.BOOL
    uHistoryBufferSize: UInt32
    uNumberOfHistoryBuffers: UInt32
    bHistoryNoDup: Windows.Win32.Foundation.BOOL
    ColorTable: Windows.Win32.Foundation.COLORREF * 16
    _pack_ = 1
class NT_FE_CONSOLE_PROPS(Structure):
    dbh: Windows.Win32.UI.Shell.DATABLOCK_HEADER
    uCodePage: UInt32
    _pack_ = 1
NWMF = Int32
NWMF_UNLOADING: NWMF = 1
NWMF_USERINITED: NWMF = 2
NWMF_FIRST: NWMF = 4
NWMF_OVERRIDEKEY: NWMF = 8
NWMF_SHOWHELP: NWMF = 16
NWMF_HTMLDIALOG: NWMF = 32
NWMF_FROMDIALOGCHILD: NWMF = 64
NWMF_USERREQUESTED: NWMF = 128
NWMF_USERALLOWED: NWMF = 256
NWMF_FORCEWINDOW: NWMF = 65536
NWMF_FORCETAB: NWMF = 131072
NWMF_SUGGESTWINDOW: NWMF = 262144
NWMF_SUGGESTTAB: NWMF = 524288
NWMF_INACTIVETAB: NWMF = 1048576
NamespaceTreeControl = Guid('ae054212-3535-4430-83-ed-d5-01-aa-66-80-e6')
NamespaceWalker = Guid('72eb61e0-8672-4303-91-75-f2-e4-c6-8b-2e-7c')
NetworkConnections = Guid('7007acc7-3202-11d1-aa-d2-00-80-5f-c1-27-0e')
NetworkExplorerFolder = Guid('f02c1a0d-be21-4350-88-b0-73-67-fc-96-ef-3c')
NetworkPlaces = Guid('208d2c60-3aea-1069-a2-d7-08-00-2b-30-30-9d')
NewProcessCauseConstants = Int32
NewProcessCauseConstants_ProtectedModeRedirect: NewProcessCauseConstants = 1
class OPENASINFO(Structure):
    pcszFile: Windows.Win32.Foundation.PWSTR
    pcszClass: Windows.Win32.Foundation.PWSTR
    oaifInFlags: Windows.Win32.UI.Shell.OPEN_AS_INFO_FLAGS
OPEN_AS_INFO_FLAGS = UInt32
OAIF_ALLOW_REGISTRATION: OPEN_AS_INFO_FLAGS = 1
OAIF_REGISTER_EXT: OPEN_AS_INFO_FLAGS = 2
OAIF_EXEC: OPEN_AS_INFO_FLAGS = 4
OAIF_FORCE_REGISTRATION: OPEN_AS_INFO_FLAGS = 8
OAIF_HIDE_REGISTRATION: OPEN_AS_INFO_FLAGS = 32
OAIF_URL_PROTOCOL: OPEN_AS_INFO_FLAGS = 64
OAIF_FILE_IS_URI: OPEN_AS_INFO_FLAGS = 128
if ARCH in 'X64,ARM64':
    class OPEN_PRINTER_PROPS_INFOA(Structure):
        dwSize: UInt32
        pszSheetName: Windows.Win32.Foundation.PSTR
        uSheetIndex: UInt32
        dwFlags: UInt32
        bModal: Windows.Win32.Foundation.BOOL
if ARCH in 'X86':
    class OPEN_PRINTER_PROPS_INFOA(Structure):
        dwSize: UInt32
        pszSheetName: Windows.Win32.Foundation.PSTR
        uSheetIndex: UInt32
        dwFlags: UInt32
        bModal: Windows.Win32.Foundation.BOOL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OPEN_PRINTER_PROPS_INFOW(Structure):
        dwSize: UInt32
        pszSheetName: Windows.Win32.Foundation.PWSTR
        uSheetIndex: UInt32
        dwFlags: UInt32
        bModal: Windows.Win32.Foundation.BOOL
if ARCH in 'X86':
    class OPEN_PRINTER_PROPS_INFOW(Structure):
        dwSize: UInt32
        pszSheetName: Windows.Win32.Foundation.PWSTR
        uSheetIndex: UInt32
        dwFlags: UInt32
        bModal: Windows.Win32.Foundation.BOOL
        _pack_ = 1
OS = UInt32
OS_WINDOWS: OS = 0
OS_NT: OS = 1
OS_WIN95ORGREATER: OS = 2
OS_NT4ORGREATER: OS = 3
OS_WIN98ORGREATER: OS = 5
OS_WIN98_GOLD: OS = 6
OS_WIN2000ORGREATER: OS = 7
OS_WIN2000PRO: OS = 8
OS_WIN2000SERVER: OS = 9
OS_WIN2000ADVSERVER: OS = 10
OS_WIN2000DATACENTER: OS = 11
OS_WIN2000TERMINAL: OS = 12
OS_EMBEDDED: OS = 13
OS_TERMINALCLIENT: OS = 14
OS_TERMINALREMOTEADMIN: OS = 15
OS_WIN95_GOLD: OS = 16
OS_MEORGREATER: OS = 17
OS_XPORGREATER: OS = 18
OS_HOME: OS = 19
OS_PROFESSIONAL: OS = 20
OS_DATACENTER: OS = 21
OS_ADVSERVER: OS = 22
OS_SERVER: OS = 23
OS_TERMINALSERVER: OS = 24
OS_PERSONALTERMINALSERVER: OS = 25
OS_FASTUSERSWITCHING: OS = 26
OS_WELCOMELOGONUI: OS = 27
OS_DOMAINMEMBER: OS = 28
OS_ANYSERVER: OS = 29
OS_WOW6432: OS = 30
OS_WEBSERVER: OS = 31
OS_SMALLBUSINESSSERVER: OS = 32
OS_TABLETPC: OS = 33
OS_SERVERADMINUI: OS = 34
OS_MEDIACENTER: OS = 35
OS_APPLIANCE: OS = 36
OfflineFolderStatus = Int32
OFS_INACTIVE: OfflineFolderStatus = -1
OFS_ONLINE: OfflineFolderStatus = 0
OFS_OFFLINE: OfflineFolderStatus = 1
OFS_SERVERBACK: OfflineFolderStatus = 2
OFS_DIRTYCACHE: OfflineFolderStatus = 3
OnexCredentialProvider = Guid('07aa0886-cc8d-4e19-a4-10-1c-75-af-68-6e-62')
OnexPlapSmartcardCredentialProvider = Guid('33c86cd6-705f-4ba1-9a-db-67-07-0b-83-77-75')
OpenControlPanel = Guid('06622d85-6856-4460-8d-e1-a8-19-21-b4-1c-4b')
PACKAGE_EXECUTION_STATE = Int32
PES_UNKNOWN: PACKAGE_EXECUTION_STATE = 0
PES_RUNNING: PACKAGE_EXECUTION_STATE = 1
PES_SUSPENDING: PACKAGE_EXECUTION_STATE = 2
PES_SUSPENDED: PACKAGE_EXECUTION_STATE = 3
PES_TERMINATED: PACKAGE_EXECUTION_STATE = 4
@winfunctype_pointer
def PAPPCONSTRAIN_CHANGE_ROUTINE(Constrained: Windows.Win32.Foundation.BOOLEAN, Context: c_void_p) -> Void: ...
@winfunctype_pointer
def PAPPSTATE_CHANGE_ROUTINE(Quiesced: Windows.Win32.Foundation.BOOLEAN, Context: c_void_p) -> Void: ...
class PARSEDURLA(Structure):
    cbSize: UInt32
    pszProtocol: Windows.Win32.Foundation.PSTR
    cchProtocol: UInt32
    pszSuffix: Windows.Win32.Foundation.PSTR
    cchSuffix: UInt32
    nScheme: UInt32
class PARSEDURLW(Structure):
    cbSize: UInt32
    pszProtocol: Windows.Win32.Foundation.PWSTR
    cchProtocol: UInt32
    pszSuffix: Windows.Win32.Foundation.PWSTR
    cchSuffix: UInt32
    nScheme: UInt32
PATHCCH_OPTIONS = UInt32
PATHCCH_NONE: PATHCCH_OPTIONS = 0
PATHCCH_ALLOW_LONG_PATHS: PATHCCH_OPTIONS = 1
PATHCCH_FORCE_ENABLE_LONG_NAME_PROCESS: PATHCCH_OPTIONS = 2
PATHCCH_FORCE_DISABLE_LONG_NAME_PROCESS: PATHCCH_OPTIONS = 4
PATHCCH_DO_NOT_NORMALIZE_SEGMENTS: PATHCCH_OPTIONS = 8
PATHCCH_ENSURE_IS_EXTENDED_LENGTH_PATH: PATHCCH_OPTIONS = 16
PATHCCH_ENSURE_TRAILING_SLASH: PATHCCH_OPTIONS = 32
PATHCCH_CANONICALIZE_SLASHES: PATHCCH_OPTIONS = 64
PCS_RET = UInt32
PCS_FATAL: PCS_RET = 2147483648
PCS_REPLACEDCHAR: PCS_RET = 1
PCS_REMOVEDCHAR: PCS_RET = 2
PCS_TRUNCATED: PCS_RET = 4
PCS_PATHTOOLONG: PCS_RET = 8
class PERSIST_FOLDER_TARGET_INFO(Structure):
    pidlTargetFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    szTargetParsingName: Char * 260
    szNetworkProvider: Char * 260
    dwAttributes: UInt32
    csidl: Int32
@winfunctype_pointer
def PFNCANSHAREFOLDERW(pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNSHOWSHAREFOLDERUIW(hwndParent: Windows.Win32.Foundation.HWND, pszPath: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
PIDISF_FLAGS = Int32
PIDISF_RECENTLYCHANGED: PIDISF_FLAGS = 1
PIDISF_CACHEDSTICKY: PIDISF_FLAGS = 2
PIDISF_CACHEIMAGES: PIDISF_FLAGS = 16
PIDISF_FOLLOWALLLINKS: PIDISF_FLAGS = 32
PIDISM_OPTIONS = Int32
PIDISM_GLOBAL: PIDISM_OPTIONS = 0
PIDISM_WATCH: PIDISM_OPTIONS = 1
PIDISM_DONTWATCH: PIDISM_OPTIONS = 2
PIDISR_INFO = Int32
PIDISR_UP_TO_DATE: PIDISR_INFO = 0
PIDISR_NEEDS_ADD: PIDISR_INFO = 1
PIDISR_NEEDS_UPDATE: PIDISR_INFO = 2
PIDISR_NEEDS_DELETE: PIDISR_INFO = 3
PID_INTSITE = Int32
PID_INTSITE_WHATSNEW: PID_INTSITE = 2
PID_INTSITE_AUTHOR: PID_INTSITE = 3
PID_INTSITE_LASTVISIT: PID_INTSITE = 4
PID_INTSITE_LASTMOD: PID_INTSITE = 5
PID_INTSITE_VISITCOUNT: PID_INTSITE = 6
PID_INTSITE_DESCRIPTION: PID_INTSITE = 7
PID_INTSITE_COMMENT: PID_INTSITE = 8
PID_INTSITE_FLAGS: PID_INTSITE = 9
PID_INTSITE_CONTENTLEN: PID_INTSITE = 10
PID_INTSITE_CONTENTCODE: PID_INTSITE = 11
PID_INTSITE_RECURSE: PID_INTSITE = 12
PID_INTSITE_WATCH: PID_INTSITE = 13
PID_INTSITE_SUBSCRIPTION: PID_INTSITE = 14
PID_INTSITE_URL: PID_INTSITE = 15
PID_INTSITE_TITLE: PID_INTSITE = 16
PID_INTSITE_CODEPAGE: PID_INTSITE = 18
PID_INTSITE_TRACKING: PID_INTSITE = 19
PID_INTSITE_ICONINDEX: PID_INTSITE = 20
PID_INTSITE_ICONFILE: PID_INTSITE = 21
PID_INTSITE_ROAMED: PID_INTSITE = 34
PID_IS = Int32
PID_IS_URL: PID_IS = 2
PID_IS_NAME: PID_IS = 4
PID_IS_WORKINGDIR: PID_IS = 5
PID_IS_HOTKEY: PID_IS = 6
PID_IS_SHOWCMD: PID_IS = 7
PID_IS_ICONINDEX: PID_IS = 8
PID_IS_ICONFILE: PID_IS = 9
PID_IS_WHATSNEW: PID_IS = 10
PID_IS_AUTHOR: PID_IS = 11
PID_IS_DESCRIPTION: PID_IS = 12
PID_IS_COMMENT: PID_IS = 13
PID_IS_ROAMED: PID_IS = 15
PINLogonCredentialProvider = Guid('cb82ea12-9f71-446d-89-e1-8d-09-24-e1-25-6e')
class PREVIEWHANDLERFRAMEINFO(Structure):
    haccel: Windows.Win32.UI.WindowsAndMessaging.HACCEL
    cAccelEntries: UInt32
PRF_FLAGS = Int32
PRF_VERIFYEXISTS: PRF_FLAGS = 1
PRF_TRYPROGRAMEXTENSIONS: PRF_FLAGS = 3
PRF_FIRSTDIRDEF: PRF_FLAGS = 4
PRF_DONTFINDLNK: PRF_FLAGS = 8
PRF_REQUIREABSOLUTE: PRF_FLAGS = 16
class PROFILEINFOA(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    lpUserName: Windows.Win32.Foundation.PSTR
    lpProfilePath: Windows.Win32.Foundation.PSTR
    lpDefaultPath: Windows.Win32.Foundation.PSTR
    lpServerName: Windows.Win32.Foundation.PSTR
    lpPolicyPath: Windows.Win32.Foundation.PSTR
    hProfile: Windows.Win32.Foundation.HANDLE
class PROFILEINFOW(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    lpUserName: Windows.Win32.Foundation.PWSTR
    lpProfilePath: Windows.Win32.Foundation.PWSTR
    lpDefaultPath: Windows.Win32.Foundation.PWSTR
    lpServerName: Windows.Win32.Foundation.PWSTR
    lpPolicyPath: Windows.Win32.Foundation.PWSTR
    hProfile: Windows.Win32.Foundation.HANDLE
class PUBAPPINFO(Structure):
    cbSize: UInt32
    dwMask: UInt32
    pszSource: Windows.Win32.Foundation.PWSTR
    stAssigned: Windows.Win32.Foundation.SYSTEMTIME
    stPublished: Windows.Win32.Foundation.SYSTEMTIME
    stScheduled: Windows.Win32.Foundation.SYSTEMTIME
    stExpire: Windows.Win32.Foundation.SYSTEMTIME
PUBAPPINFOFLAGS = Int32
PAI_SOURCE: PUBAPPINFOFLAGS = 1
PAI_ASSIGNEDTIME: PUBAPPINFOFLAGS = 2
PAI_PUBLISHEDTIME: PUBAPPINFOFLAGS = 4
PAI_SCHEDULEDTIME: PUBAPPINFOFLAGS = 8
PAI_EXPIRETIME: PUBAPPINFOFLAGS = 16
PackageDebugSettings = Guid('b1aec16f-2383-4852-b0-e9-8f-0b-1d-c6-6b-4d')
PasswordCredentialProvider = Guid('60b78e88-ead8-445c-9c-fd-0b-87-f7-4e-a6-cd')
PreviousVersions = Guid('596ab062-b4d2-4215-9f-74-e9-10-9b-0a-81-53')
PropertiesUI = Guid('d912f8cf-0396-4915-88-4e-fb-42-5d-32-94-3b')
PublishDropTarget = Guid('cc6eeffb-43f6-46c5-96-19-51-d5-71-96-7f-7d')
PublishingWizard = Guid('6b33163c-76a5-4b6c-bf-21-45-de-9c-d5-03-a1')
class QCMINFO(Structure):
    hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU
    indexMenu: UInt32
    idCmdFirst: UInt32
    idCmdLast: UInt32
    pIdMap: POINTER(Windows.Win32.UI.Shell.QCMINFO_IDMAP_head)
class QCMINFO_IDMAP(Structure):
    nMaxIds: UInt32
    pIdList: Windows.Win32.UI.Shell.QCMINFO_IDMAP_PLACEMENT * 1
class QCMINFO_IDMAP_PLACEMENT(Structure):
    id: UInt32
    fFlags: UInt32
class QITAB(Structure):
    piid: POINTER(Guid)
    dwOffset: UInt32
QITIPF_FLAGS = Int32
QITIPF_DEFAULT: QITIPF_FLAGS = 0
QITIPF_USENAME: QITIPF_FLAGS = 1
QITIPF_LINKNOTARGET: QITIPF_FLAGS = 2
QITIPF_LINKUSETARGET: QITIPF_FLAGS = 4
QITIPF_USESLOWTIP: QITIPF_FLAGS = 8
QITIPF_SINGLELINE: QITIPF_FLAGS = 16
QIF_CACHED: QITIPF_FLAGS = 1
QIF_DONTEXPANDFOLDER: QITIPF_FLAGS = 2
QUERY_USER_NOTIFICATION_STATE = Int32
QUNS_NOT_PRESENT: QUERY_USER_NOTIFICATION_STATE = 1
QUNS_BUSY: QUERY_USER_NOTIFICATION_STATE = 2
QUNS_RUNNING_D3D_FULL_SCREEN: QUERY_USER_NOTIFICATION_STATE = 3
QUNS_PRESENTATION_MODE: QUERY_USER_NOTIFICATION_STATE = 4
QUNS_ACCEPTS_NOTIFICATIONS: QUERY_USER_NOTIFICATION_STATE = 5
QUNS_QUIET_TIME: QUERY_USER_NOTIFICATION_STATE = 6
QUNS_APP: QUERY_USER_NOTIFICATION_STATE = 7
QueryCancelAutoPlay = Guid('331f1768-05a9-4ddd-b8-6e-da-e3-4d-dc-99-8a')
RASProvider = Guid('5537e283-b1e7-4ef8-9c-6e-7a-b0-af-e5-05-6d')
RESTRICTIONS = Int32
REST_NONE: RESTRICTIONS = 0
REST_NORUN: RESTRICTIONS = 1
REST_NOCLOSE: RESTRICTIONS = 2
REST_NOSAVESET: RESTRICTIONS = 4
REST_NOFILEMENU: RESTRICTIONS = 8
REST_NOSETFOLDERS: RESTRICTIONS = 16
REST_NOSETTASKBAR: RESTRICTIONS = 32
REST_NODESKTOP: RESTRICTIONS = 64
REST_NOFIND: RESTRICTIONS = 128
REST_NODRIVES: RESTRICTIONS = 256
REST_NODRIVEAUTORUN: RESTRICTIONS = 512
REST_NODRIVETYPEAUTORUN: RESTRICTIONS = 1024
REST_NONETHOOD: RESTRICTIONS = 2048
REST_STARTBANNER: RESTRICTIONS = 4096
REST_RESTRICTRUN: RESTRICTIONS = 8192
REST_NOPRINTERTABS: RESTRICTIONS = 16384
REST_NOPRINTERDELETE: RESTRICTIONS = 32768
REST_NOPRINTERADD: RESTRICTIONS = 65536
REST_NOSTARTMENUSUBFOLDERS: RESTRICTIONS = 131072
REST_MYDOCSONNET: RESTRICTIONS = 262144
REST_NOEXITTODOS: RESTRICTIONS = 524288
REST_ENFORCESHELLEXTSECURITY: RESTRICTIONS = 1048576
REST_LINKRESOLVEIGNORELINKINFO: RESTRICTIONS = 2097152
REST_NOCOMMONGROUPS: RESTRICTIONS = 4194304
REST_SEPARATEDESKTOPPROCESS: RESTRICTIONS = 8388608
REST_NOWEB: RESTRICTIONS = 16777216
REST_NOTRAYCONTEXTMENU: RESTRICTIONS = 33554432
REST_NOVIEWCONTEXTMENU: RESTRICTIONS = 67108864
REST_NONETCONNECTDISCONNECT: RESTRICTIONS = 134217728
REST_STARTMENULOGOFF: RESTRICTIONS = 268435456
REST_NOSETTINGSASSIST: RESTRICTIONS = 536870912
REST_NOINTERNETICON: RESTRICTIONS = 1073741825
REST_NORECENTDOCSHISTORY: RESTRICTIONS = 1073741826
REST_NORECENTDOCSMENU: RESTRICTIONS = 1073741827
REST_NOACTIVEDESKTOP: RESTRICTIONS = 1073741828
REST_NOACTIVEDESKTOPCHANGES: RESTRICTIONS = 1073741829
REST_NOFAVORITESMENU: RESTRICTIONS = 1073741830
REST_CLEARRECENTDOCSONEXIT: RESTRICTIONS = 1073741831
REST_CLASSICSHELL: RESTRICTIONS = 1073741832
REST_NOCUSTOMIZEWEBVIEW: RESTRICTIONS = 1073741833
REST_NOHTMLWALLPAPER: RESTRICTIONS = 1073741840
REST_NOCHANGINGWALLPAPER: RESTRICTIONS = 1073741841
REST_NODESKCOMP: RESTRICTIONS = 1073741842
REST_NOADDDESKCOMP: RESTRICTIONS = 1073741843
REST_NODELDESKCOMP: RESTRICTIONS = 1073741844
REST_NOCLOSEDESKCOMP: RESTRICTIONS = 1073741845
REST_NOCLOSE_DRAGDROPBAND: RESTRICTIONS = 1073741846
REST_NOMOVINGBAND: RESTRICTIONS = 1073741847
REST_NOEDITDESKCOMP: RESTRICTIONS = 1073741848
REST_NORESOLVESEARCH: RESTRICTIONS = 1073741849
REST_NORESOLVETRACK: RESTRICTIONS = 1073741850
REST_FORCECOPYACLWITHFILE: RESTRICTIONS = 1073741851
REST_NOFORGETSOFTWAREUPDATE: RESTRICTIONS = 1073741853
REST_NOSETACTIVEDESKTOP: RESTRICTIONS = 1073741854
REST_NOUPDATEWINDOWS: RESTRICTIONS = 1073741855
REST_NOCHANGESTARMENU: RESTRICTIONS = 1073741856
REST_NOFOLDEROPTIONS: RESTRICTIONS = 1073741857
REST_HASFINDCOMPUTERS: RESTRICTIONS = 1073741858
REST_INTELLIMENUS: RESTRICTIONS = 1073741859
REST_RUNDLGMEMCHECKBOX: RESTRICTIONS = 1073741860
REST_ARP_ShowPostSetup: RESTRICTIONS = 1073741861
REST_NOCSC: RESTRICTIONS = 1073741862
REST_NOCONTROLPANEL: RESTRICTIONS = 1073741863
REST_ENUMWORKGROUP: RESTRICTIONS = 1073741864
REST_ARP_NOARP: RESTRICTIONS = 1073741865
REST_ARP_NOREMOVEPAGE: RESTRICTIONS = 1073741866
REST_ARP_NOADDPAGE: RESTRICTIONS = 1073741867
REST_ARP_NOWINSETUPPAGE: RESTRICTIONS = 1073741868
REST_GREYMSIADS: RESTRICTIONS = 1073741869
REST_NOCHANGEMAPPEDDRIVELABEL: RESTRICTIONS = 1073741870
REST_NOCHANGEMAPPEDDRIVECOMMENT: RESTRICTIONS = 1073741871
REST_MaxRecentDocs: RESTRICTIONS = 1073741872
REST_NONETWORKCONNECTIONS: RESTRICTIONS = 1073741873
REST_FORCESTARTMENULOGOFF: RESTRICTIONS = 1073741874
REST_NOWEBVIEW: RESTRICTIONS = 1073741875
REST_NOCUSTOMIZETHISFOLDER: RESTRICTIONS = 1073741876
REST_NOENCRYPTION: RESTRICTIONS = 1073741877
REST_DONTSHOWSUPERHIDDEN: RESTRICTIONS = 1073741879
REST_NOSHELLSEARCHBUTTON: RESTRICTIONS = 1073741880
REST_NOHARDWARETAB: RESTRICTIONS = 1073741881
REST_NORUNASINSTALLPROMPT: RESTRICTIONS = 1073741882
REST_PROMPTRUNASINSTALLNETPATH: RESTRICTIONS = 1073741883
REST_NOMANAGEMYCOMPUTERVERB: RESTRICTIONS = 1073741884
REST_DISALLOWRUN: RESTRICTIONS = 1073741886
REST_NOWELCOMESCREEN: RESTRICTIONS = 1073741887
REST_RESTRICTCPL: RESTRICTIONS = 1073741888
REST_DISALLOWCPL: RESTRICTIONS = 1073741889
REST_NOSMBALLOONTIP: RESTRICTIONS = 1073741890
REST_NOSMHELP: RESTRICTIONS = 1073741891
REST_NOWINKEYS: RESTRICTIONS = 1073741892
REST_NOENCRYPTONMOVE: RESTRICTIONS = 1073741893
REST_NOLOCALMACHINERUN: RESTRICTIONS = 1073741894
REST_NOCURRENTUSERRUN: RESTRICTIONS = 1073741895
REST_NOLOCALMACHINERUNONCE: RESTRICTIONS = 1073741896
REST_NOCURRENTUSERRUNONCE: RESTRICTIONS = 1073741897
REST_FORCEACTIVEDESKTOPON: RESTRICTIONS = 1073741898
REST_NOVIEWONDRIVE: RESTRICTIONS = 1073741900
REST_NONETCRAWL: RESTRICTIONS = 1073741901
REST_NOSHAREDDOCUMENTS: RESTRICTIONS = 1073741902
REST_NOSMMYDOCS: RESTRICTIONS = 1073741903
REST_NOSMMYPICS: RESTRICTIONS = 1073741904
REST_ALLOWBITBUCKDRIVES: RESTRICTIONS = 1073741905
REST_NONLEGACYSHELLMODE: RESTRICTIONS = 1073741906
REST_NOCONTROLPANELBARRICADE: RESTRICTIONS = 1073741907
REST_NOSTARTPAGE: RESTRICTIONS = 1073741908
REST_NOAUTOTRAYNOTIFY: RESTRICTIONS = 1073741909
REST_NOTASKGROUPING: RESTRICTIONS = 1073741910
REST_NOCDBURNING: RESTRICTIONS = 1073741911
REST_MYCOMPNOPROP: RESTRICTIONS = 1073741912
REST_MYDOCSNOPROP: RESTRICTIONS = 1073741913
REST_NOSTARTPANEL: RESTRICTIONS = 1073741914
REST_NODISPLAYAPPEARANCEPAGE: RESTRICTIONS = 1073741915
REST_NOTHEMESTAB: RESTRICTIONS = 1073741916
REST_NOVISUALSTYLECHOICE: RESTRICTIONS = 1073741917
REST_NOSIZECHOICE: RESTRICTIONS = 1073741918
REST_NOCOLORCHOICE: RESTRICTIONS = 1073741919
REST_SETVISUALSTYLE: RESTRICTIONS = 1073741920
REST_STARTRUNNOHOMEPATH: RESTRICTIONS = 1073741921
REST_NOUSERNAMEINSTARTPANEL: RESTRICTIONS = 1073741922
REST_NOMYCOMPUTERICON: RESTRICTIONS = 1073741923
REST_NOSMNETWORKPLACES: RESTRICTIONS = 1073741924
REST_NOSMPINNEDLIST: RESTRICTIONS = 1073741925
REST_NOSMMYMUSIC: RESTRICTIONS = 1073741926
REST_NOSMEJECTPC: RESTRICTIONS = 1073741927
REST_NOSMMOREPROGRAMS: RESTRICTIONS = 1073741928
REST_NOSMMFUPROGRAMS: RESTRICTIONS = 1073741929
REST_NOTRAYITEMSDISPLAY: RESTRICTIONS = 1073741930
REST_NOTOOLBARSONTASKBAR: RESTRICTIONS = 1073741931
REST_NOSMCONFIGUREPROGRAMS: RESTRICTIONS = 1073741935
REST_HIDECLOCK: RESTRICTIONS = 1073741936
REST_NOLOWDISKSPACECHECKS: RESTRICTIONS = 1073741937
REST_NOENTIRENETWORK: RESTRICTIONS = 1073741938
REST_NODESKTOPCLEANUP: RESTRICTIONS = 1073741939
REST_BITBUCKNUKEONDELETE: RESTRICTIONS = 1073741940
REST_BITBUCKCONFIRMDELETE: RESTRICTIONS = 1073741941
REST_BITBUCKNOPROP: RESTRICTIONS = 1073741942
REST_NODISPBACKGROUND: RESTRICTIONS = 1073741943
REST_NODISPSCREENSAVEPG: RESTRICTIONS = 1073741944
REST_NODISPSETTINGSPG: RESTRICTIONS = 1073741945
REST_NODISPSCREENSAVEPREVIEW: RESTRICTIONS = 1073741946
REST_NODISPLAYCPL: RESTRICTIONS = 1073741947
REST_HIDERUNASVERB: RESTRICTIONS = 1073741948
REST_NOTHUMBNAILCACHE: RESTRICTIONS = 1073741949
REST_NOSTRCMPLOGICAL: RESTRICTIONS = 1073741950
REST_NOPUBLISHWIZARD: RESTRICTIONS = 1073741951
REST_NOONLINEPRINTSWIZARD: RESTRICTIONS = 1073741952
REST_NOWEBSERVICES: RESTRICTIONS = 1073741953
REST_ALLOWUNHASHEDWEBVIEW: RESTRICTIONS = 1073741954
REST_ALLOWLEGACYWEBVIEW: RESTRICTIONS = 1073741955
REST_REVERTWEBVIEWSECURITY: RESTRICTIONS = 1073741956
REST_INHERITCONSOLEHANDLES: RESTRICTIONS = 1073741958
REST_NOREMOTERECURSIVEEVENTS: RESTRICTIONS = 1073741961
REST_NOREMOTECHANGENOTIFY: RESTRICTIONS = 1073741969
REST_NOENUMENTIRENETWORK: RESTRICTIONS = 1073741971
REST_NOINTERNETOPENWITH: RESTRICTIONS = 1073741973
REST_DONTRETRYBADNETNAME: RESTRICTIONS = 1073741979
REST_ALLOWFILECLSIDJUNCTIONS: RESTRICTIONS = 1073741980
REST_NOUPNPINSTALL: RESTRICTIONS = 1073741981
REST_ARP_DONTGROUPPATCHES: RESTRICTIONS = 1073741996
REST_ARP_NOCHOOSEPROGRAMSPAGE: RESTRICTIONS = 1073741997
REST_NODISCONNECT: RESTRICTIONS = 1090519041
REST_NOSECURITY: RESTRICTIONS = 1090519042
REST_NOFILEASSOCIATE: RESTRICTIONS = 1090519043
REST_ALLOWCOMMENTTOGGLE: RESTRICTIONS = 1090519044
RefreshConstants = Int32
REFRESH_NORMAL: RefreshConstants = 0
REFRESH_IFEXPIRED: RefreshConstants = 1
REFRESH_COMPLETELY: RefreshConstants = 3
SCALE_CHANGE_FLAGS = UInt32
SCF_VALUE_NONE: SCALE_CHANGE_FLAGS = 0
SCF_SCALE: SCALE_CHANGE_FLAGS = 1
SCF_PHYSICAL: SCALE_CHANGE_FLAGS = 2
SCNRT_STATUS = Int32
SCNRT_ENABLE: SCNRT_STATUS = 0
SCNRT_DISABLE: SCNRT_STATUS = 1
SECURELOCKCODE = Int32
SECURELOCK_NOCHANGE: SECURELOCKCODE = -1
SECURELOCK_SET_UNSECURE: SECURELOCKCODE = 0
SECURELOCK_SET_MIXED: SECURELOCKCODE = 1
SECURELOCK_SET_SECUREUNKNOWNBIT: SECURELOCKCODE = 2
SECURELOCK_SET_SECURE40BIT: SECURELOCKCODE = 3
SECURELOCK_SET_SECURE56BIT: SECURELOCKCODE = 4
SECURELOCK_SET_FORTEZZA: SECURELOCKCODE = 5
SECURELOCK_SET_SECURE128BIT: SECURELOCKCODE = 6
SECURELOCK_FIRSTSUGGEST: SECURELOCKCODE = 7
SECURELOCK_SUGGEST_UNSECURE: SECURELOCKCODE = 7
SECURELOCK_SUGGEST_MIXED: SECURELOCKCODE = 8
SECURELOCK_SUGGEST_SECUREUNKNOWNBIT: SECURELOCKCODE = 9
SECURELOCK_SUGGEST_SECURE40BIT: SECURELOCKCODE = 10
SECURELOCK_SUGGEST_SECURE56BIT: SECURELOCKCODE = 11
SECURELOCK_SUGGEST_FORTEZZA: SECURELOCKCODE = 12
SECURELOCK_SUGGEST_SECURE128BIT: SECURELOCKCODE = 13
SFBS_FLAGS = Int32
SFBS_FLAGS_ROUND_TO_NEAREST_DISPLAYED_DIGIT: SFBS_FLAGS = 1
SFBS_FLAGS_TRUNCATE_UNDISPLAYED_DECIMAL_DIGITS: SFBS_FLAGS = 2
class SFVM_HELPTOPIC_DATA(Structure):
    wszHelpFile: Char * 260
    wszHelpTopic: Char * 260
SFVM_MESSAGE_ID = Int32
SFVM_MERGEMENU: SFVM_MESSAGE_ID = 1
SFVM_INVOKECOMMAND: SFVM_MESSAGE_ID = 2
SFVM_GETHELPTEXT: SFVM_MESSAGE_ID = 3
SFVM_GETTOOLTIPTEXT: SFVM_MESSAGE_ID = 4
SFVM_GETBUTTONINFO: SFVM_MESSAGE_ID = 5
SFVM_GETBUTTONS: SFVM_MESSAGE_ID = 6
SFVM_INITMENUPOPUP: SFVM_MESSAGE_ID = 7
SFVM_FSNOTIFY: SFVM_MESSAGE_ID = 14
SFVM_WINDOWCREATED: SFVM_MESSAGE_ID = 15
SFVM_GETDETAILSOF: SFVM_MESSAGE_ID = 23
SFVM_COLUMNCLICK: SFVM_MESSAGE_ID = 24
SFVM_QUERYFSNOTIFY: SFVM_MESSAGE_ID = 25
SFVM_DEFITEMCOUNT: SFVM_MESSAGE_ID = 26
SFVM_DEFVIEWMODE: SFVM_MESSAGE_ID = 27
SFVM_UNMERGEMENU: SFVM_MESSAGE_ID = 28
SFVM_UPDATESTATUSBAR: SFVM_MESSAGE_ID = 31
SFVM_BACKGROUNDENUM: SFVM_MESSAGE_ID = 32
SFVM_DIDDRAGDROP: SFVM_MESSAGE_ID = 36
SFVM_SETISFV: SFVM_MESSAGE_ID = 39
SFVM_THISIDLIST: SFVM_MESSAGE_ID = 41
SFVM_ADDPROPERTYPAGES: SFVM_MESSAGE_ID = 47
SFVM_BACKGROUNDENUMDONE: SFVM_MESSAGE_ID = 48
SFVM_GETNOTIFY: SFVM_MESSAGE_ID = 49
SFVM_GETSORTDEFAULTS: SFVM_MESSAGE_ID = 53
SFVM_SIZE: SFVM_MESSAGE_ID = 57
SFVM_GETZONE: SFVM_MESSAGE_ID = 58
SFVM_GETPANE: SFVM_MESSAGE_ID = 59
SFVM_GETHELPTOPIC: SFVM_MESSAGE_ID = 63
SFVM_GETANIMATION: SFVM_MESSAGE_ID = 68
class SFVM_PROPPAGE_DATA(Structure):
    dwReserved: UInt32
    pfn: Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE
    lParam: Windows.Win32.Foundation.LPARAM
SFVS_SELECT = Int32
SFVS_SELECT_NONE: SFVS_SELECT = 0
SFVS_SELECT_ALLITEMS: SFVS_SELECT = 1
SFVS_SELECT_INVERT: SFVS_SELECT = 2
class SFV_CREATE(Structure):
    cbSize: UInt32
    pshf: Windows.Win32.UI.Shell.IShellFolder_head
    psvOuter: Windows.Win32.UI.Shell.IShellView_head
    psfvcb: Windows.Win32.UI.Shell.IShellFolderViewCB_head
class SFV_SETITEMPOS(Structure):
    pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    pt: Windows.Win32.Foundation.POINT
SHARD = Int32
SHARD_PIDL: SHARD = 1
SHARD_PATHA: SHARD = 2
SHARD_PATHW: SHARD = 3
SHARD_APPIDINFO: SHARD = 4
SHARD_APPIDINFOIDLIST: SHARD = 5
SHARD_LINK: SHARD = 6
SHARD_APPIDINFOLINK: SHARD = 7
SHARD_SHELLITEM: SHARD = 8
class SHARDAPPIDINFO(Structure):
    psi: Windows.Win32.UI.Shell.IShellItem_head
    pszAppID: Windows.Win32.Foundation.PWSTR
    _pack_ = 1
class SHARDAPPIDINFOIDLIST(Structure):
    pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    pszAppID: Windows.Win32.Foundation.PWSTR
    _pack_ = 1
class SHARDAPPIDINFOLINK(Structure):
    psl: Windows.Win32.UI.Shell.IShellLinkA_head
    pszAppID: Windows.Win32.Foundation.PWSTR
    _pack_ = 1
SHARE_ROLE = Int32
SHARE_ROLE_INVALID: SHARE_ROLE = -1
SHARE_ROLE_READER: SHARE_ROLE = 0
SHARE_ROLE_CONTRIBUTOR: SHARE_ROLE = 1
SHARE_ROLE_CO_OWNER: SHARE_ROLE = 2
SHARE_ROLE_OWNER: SHARE_ROLE = 3
SHARE_ROLE_CUSTOM: SHARE_ROLE = 4
SHARE_ROLE_MIXED: SHARE_ROLE = 5
SHCNE_ID = UInt32
SHCNE_RENAMEITEM: SHCNE_ID = 1
SHCNE_CREATE: SHCNE_ID = 2
SHCNE_DELETE: SHCNE_ID = 4
SHCNE_MKDIR: SHCNE_ID = 8
SHCNE_RMDIR: SHCNE_ID = 16
SHCNE_MEDIAINSERTED: SHCNE_ID = 32
SHCNE_MEDIAREMOVED: SHCNE_ID = 64
SHCNE_DRIVEREMOVED: SHCNE_ID = 128
SHCNE_DRIVEADD: SHCNE_ID = 256
SHCNE_NETSHARE: SHCNE_ID = 512
SHCNE_NETUNSHARE: SHCNE_ID = 1024
SHCNE_ATTRIBUTES: SHCNE_ID = 2048
SHCNE_UPDATEDIR: SHCNE_ID = 4096
SHCNE_UPDATEITEM: SHCNE_ID = 8192
SHCNE_SERVERDISCONNECT: SHCNE_ID = 16384
SHCNE_UPDATEIMAGE: SHCNE_ID = 32768
SHCNE_DRIVEADDGUI: SHCNE_ID = 65536
SHCNE_RENAMEFOLDER: SHCNE_ID = 131072
SHCNE_FREESPACE: SHCNE_ID = 262144
SHCNE_EXTENDED_EVENT: SHCNE_ID = 67108864
SHCNE_ASSOCCHANGED: SHCNE_ID = 134217728
SHCNE_DISKEVENTS: SHCNE_ID = 145439
SHCNE_GLOBALEVENTS: SHCNE_ID = 201687520
SHCNE_ALLEVENTS: SHCNE_ID = 2147483647
SHCNE_INTERRUPT: SHCNE_ID = 2147483648
SHCNF_FLAGS = UInt32
SHCNF_IDLIST: SHCNF_FLAGS = 0
SHCNF_PATHA: SHCNF_FLAGS = 1
SHCNF_PRINTERA: SHCNF_FLAGS = 2
SHCNF_DWORD: SHCNF_FLAGS = 3
SHCNF_PATHW: SHCNF_FLAGS = 5
SHCNF_PRINTERW: SHCNF_FLAGS = 6
SHCNF_TYPE: SHCNF_FLAGS = 255
SHCNF_FLUSH: SHCNF_FLAGS = 4096
SHCNF_FLUSHNOWAIT: SHCNF_FLAGS = 12288
SHCNF_NOTIFYRECURSIVE: SHCNF_FLAGS = 65536
SHCNF_PATH: SHCNF_FLAGS = 5
SHCNF_PRINTER: SHCNF_FLAGS = 6
SHCNRF_SOURCE = Int32
SHCNRF_InterruptLevel: SHCNRF_SOURCE = 1
SHCNRF_ShellLevel: SHCNRF_SOURCE = 2
SHCNRF_RecursiveInterrupt: SHCNRF_SOURCE = 4096
SHCNRF_NewDelivery: SHCNRF_SOURCE = 32768
class SHCOLUMNDATA(Structure):
    dwFlags: UInt32
    dwFileAttributes: UInt32
    dwReserved: UInt32
    pwszExt: Windows.Win32.Foundation.PWSTR
    wszFile: Char * 260
class SHCOLUMNINFO(Structure):
    scid: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY
    vt: Windows.Win32.System.Com.VARENUM
    fmt: UInt32
    cChars: UInt32
    csFlags: UInt32
    wszTitle: Char * 80
    wszDescription: Char * 128
    _pack_ = 1
class SHCOLUMNINIT(Structure):
    dwFlags: UInt32
    dwReserved: UInt32
    wszFolder: Char * 260
if ARCH in 'X64,ARM64':
    class SHCREATEPROCESSINFOW(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: Windows.Win32.Foundation.HWND
        pszFile: Windows.Win32.Foundation.PWSTR
        pszParameters: Windows.Win32.Foundation.PWSTR
        pszCurrentDirectory: Windows.Win32.Foundation.PWSTR
        hUserToken: Windows.Win32.Foundation.HANDLE
        lpProcessAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)
        lpThreadAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)
        bInheritHandles: Windows.Win32.Foundation.BOOL
        dwCreationFlags: UInt32
        lpStartupInfo: POINTER(Windows.Win32.System.Threading.STARTUPINFOW_head)
        lpProcessInformation: POINTER(Windows.Win32.System.Threading.PROCESS_INFORMATION_head)
if ARCH in 'X86':
    class SHCREATEPROCESSINFOW(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: Windows.Win32.Foundation.HWND
        pszFile: Windows.Win32.Foundation.PWSTR
        pszParameters: Windows.Win32.Foundation.PWSTR
        pszCurrentDirectory: Windows.Win32.Foundation.PWSTR
        hUserToken: Windows.Win32.Foundation.HANDLE
        lpProcessAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)
        lpThreadAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)
        bInheritHandles: Windows.Win32.Foundation.BOOL
        dwCreationFlags: UInt32
        lpStartupInfo: POINTER(Windows.Win32.System.Threading.STARTUPINFOW_head)
        lpProcessInformation: POINTER(Windows.Win32.System.Threading.PROCESS_INFORMATION_head)
        _pack_ = 1
class SHChangeDWORDAsIDList(Structure):
    cb: UInt16
    dwItem1: UInt32
    dwItem2: UInt32
    cbZero: UInt16
    _pack_ = 1
class SHChangeNotifyEntry(Structure):
    pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    fRecursive: Windows.Win32.Foundation.BOOL
    _pack_ = 1
class SHChangeProductKeyAsIDList(Structure):
    cb: UInt16
    wszProductKey: Char * 39
    cbZero: UInt16
    _pack_ = 1
class SHChangeUpdateImageIDList(Structure):
    cb: UInt16
    iIconIndex: Int32
    iCurIndex: Int32
    uFlags: UInt32
    dwProcessID: UInt32
    szName: Char * 260
    cbZero: UInt16
    _pack_ = 1
class SHDESCRIPTIONID(Structure):
    dwDescriptionId: Windows.Win32.UI.Shell.SHDID_ID
    clsid: Guid
SHDID_ID = Int32
SHDID_ROOT_REGITEM: SHDID_ID = 1
SHDID_FS_FILE: SHDID_ID = 2
SHDID_FS_DIRECTORY: SHDID_ID = 3
SHDID_FS_OTHER: SHDID_ID = 4
SHDID_COMPUTER_DRIVE35: SHDID_ID = 5
SHDID_COMPUTER_DRIVE525: SHDID_ID = 6
SHDID_COMPUTER_REMOVABLE: SHDID_ID = 7
SHDID_COMPUTER_FIXED: SHDID_ID = 8
SHDID_COMPUTER_NETDRIVE: SHDID_ID = 9
SHDID_COMPUTER_CDROM: SHDID_ID = 10
SHDID_COMPUTER_RAMDISK: SHDID_ID = 11
SHDID_COMPUTER_OTHER: SHDID_ID = 12
SHDID_NET_DOMAIN: SHDID_ID = 13
SHDID_NET_SERVER: SHDID_ID = 14
SHDID_NET_SHARE: SHDID_ID = 15
SHDID_NET_RESTOFNET: SHDID_ID = 16
SHDID_NET_OTHER: SHDID_ID = 17
SHDID_COMPUTER_IMAGING: SHDID_ID = 18
SHDID_COMPUTER_AUDIO: SHDID_ID = 19
SHDID_COMPUTER_SHAREDDOCS: SHDID_ID = 20
SHDID_MOBILE_DEVICE: SHDID_ID = 21
SHDID_REMOTE_DESKTOP_DRIVE: SHDID_ID = 22
class SHDRAGIMAGE(Structure):
    sizeDragImage: Windows.Win32.Foundation.SIZE
    ptOffset: Windows.Win32.Foundation.POINT
    hbmpDragImage: Windows.Win32.Graphics.Gdi.HBITMAP
    crColorKey: Windows.Win32.Foundation.COLORREF
SHELLBROWSERSHOWCONTROL = Int32
SBSC_HIDE: SHELLBROWSERSHOWCONTROL = 0
SBSC_SHOW: SHELLBROWSERSHOWCONTROL = 1
SBSC_TOGGLE: SHELLBROWSERSHOWCONTROL = 2
SBSC_QUERY: SHELLBROWSERSHOWCONTROL = 3
if ARCH in 'X64,ARM64':
    class SHELLEXECUTEINFOA(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: Windows.Win32.Foundation.HWND
        lpVerb: Windows.Win32.Foundation.PSTR
        lpFile: Windows.Win32.Foundation.PSTR
        lpParameters: Windows.Win32.Foundation.PSTR
        lpDirectory: Windows.Win32.Foundation.PSTR
        nShow: Int32
        hInstApp: Windows.Win32.Foundation.HINSTANCE
        lpIDList: c_void_p
        lpClass: Windows.Win32.Foundation.PSTR
        hkeyClass: Windows.Win32.System.Registry.HKEY
        dwHotKey: UInt32
        Anonymous: _Anonymous_e__Union
        hProcess: Windows.Win32.Foundation.HANDLE
        class _Anonymous_e__Union(Union):
            hIcon: Windows.Win32.Foundation.HANDLE
            hMonitor: Windows.Win32.Foundation.HANDLE
if ARCH in 'X86':
    class SHELLEXECUTEINFOA(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: Windows.Win32.Foundation.HWND
        lpVerb: Windows.Win32.Foundation.PSTR
        lpFile: Windows.Win32.Foundation.PSTR
        lpParameters: Windows.Win32.Foundation.PSTR
        lpDirectory: Windows.Win32.Foundation.PSTR
        nShow: Int32
        hInstApp: Windows.Win32.Foundation.HINSTANCE
        lpIDList: c_void_p
        lpClass: Windows.Win32.Foundation.PSTR
        hkeyClass: Windows.Win32.System.Registry.HKEY
        dwHotKey: UInt32
        Anonymous: _Anonymous_e__Union
        hProcess: Windows.Win32.Foundation.HANDLE
        _pack_ = 1
        class _Anonymous_e__Union(Union):
            hIcon: Windows.Win32.Foundation.HANDLE
            hMonitor: Windows.Win32.Foundation.HANDLE
            _pack_ = 1
if ARCH in 'X64,ARM64':
    class SHELLEXECUTEINFOW(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: Windows.Win32.Foundation.HWND
        lpVerb: Windows.Win32.Foundation.PWSTR
        lpFile: Windows.Win32.Foundation.PWSTR
        lpParameters: Windows.Win32.Foundation.PWSTR
        lpDirectory: Windows.Win32.Foundation.PWSTR
        nShow: Int32
        hInstApp: Windows.Win32.Foundation.HINSTANCE
        lpIDList: c_void_p
        lpClass: Windows.Win32.Foundation.PWSTR
        hkeyClass: Windows.Win32.System.Registry.HKEY
        dwHotKey: UInt32
        Anonymous: _Anonymous_e__Union
        hProcess: Windows.Win32.Foundation.HANDLE
        class _Anonymous_e__Union(Union):
            hIcon: Windows.Win32.Foundation.HANDLE
            hMonitor: Windows.Win32.Foundation.HANDLE
if ARCH in 'X86':
    class SHELLEXECUTEINFOW(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: Windows.Win32.Foundation.HWND
        lpVerb: Windows.Win32.Foundation.PWSTR
        lpFile: Windows.Win32.Foundation.PWSTR
        lpParameters: Windows.Win32.Foundation.PWSTR
        lpDirectory: Windows.Win32.Foundation.PWSTR
        nShow: Int32
        hInstApp: Windows.Win32.Foundation.HINSTANCE
        lpIDList: c_void_p
        lpClass: Windows.Win32.Foundation.PWSTR
        hkeyClass: Windows.Win32.System.Registry.HKEY
        dwHotKey: UInt32
        Anonymous: _Anonymous_e__Union
        hProcess: Windows.Win32.Foundation.HANDLE
        _pack_ = 1
        class _Anonymous_e__Union(Union):
            hIcon: Windows.Win32.Foundation.HANDLE
            hMonitor: Windows.Win32.Foundation.HANDLE
            _pack_ = 1
class SHELLFLAGSTATE(Structure):
    _bitfield: Int32
    _pack_ = 1
class SHELLSTATEA(Structure):
    _bitfield1: Int32
    dwWin95Unused: UInt32
    uWin95Unused: UInt32
    lParamSort: Int32
    iSortDirection: Int32
    version: UInt32
    uNotUsed: UInt32
    _bitfield2: Int32
    _pack_ = 1
class SHELLSTATEW(Structure):
    _bitfield1: Int32
    dwWin95Unused: UInt32
    uWin95Unused: UInt32
    lParamSort: Int32
    iSortDirection: Int32
    version: UInt32
    uNotUsed: UInt32
    _bitfield2: Int32
    _pack_ = 1
SHELL_AUTOCOMPLETE_FLAGS = UInt32
SHACF_DEFAULT: SHELL_AUTOCOMPLETE_FLAGS = 0
SHACF_FILESYSTEM: SHELL_AUTOCOMPLETE_FLAGS = 1
SHACF_URLALL: SHELL_AUTOCOMPLETE_FLAGS = 6
SHACF_URLHISTORY: SHELL_AUTOCOMPLETE_FLAGS = 2
SHACF_URLMRU: SHELL_AUTOCOMPLETE_FLAGS = 4
SHACF_USETAB: SHELL_AUTOCOMPLETE_FLAGS = 8
SHACF_FILESYS_ONLY: SHELL_AUTOCOMPLETE_FLAGS = 16
SHACF_FILESYS_DIRS: SHELL_AUTOCOMPLETE_FLAGS = 32
SHACF_VIRTUAL_NAMESPACE: SHELL_AUTOCOMPLETE_FLAGS = 64
SHACF_AUTOSUGGEST_FORCE_ON: SHELL_AUTOCOMPLETE_FLAGS = 268435456
SHACF_AUTOSUGGEST_FORCE_OFF: SHELL_AUTOCOMPLETE_FLAGS = 536870912
SHACF_AUTOAPPEND_FORCE_ON: SHELL_AUTOCOMPLETE_FLAGS = 1073741824
SHACF_AUTOAPPEND_FORCE_OFF: SHELL_AUTOCOMPLETE_FLAGS = 2147483648
class SHELL_ITEM_RESOURCE(Structure):
    guidType: Guid
    szName: Char * 260
SHELL_LINK_DATA_FLAGS = Int32
SLDF_DEFAULT: SHELL_LINK_DATA_FLAGS = 0
SLDF_HAS_ID_LIST: SHELL_LINK_DATA_FLAGS = 1
SLDF_HAS_LINK_INFO: SHELL_LINK_DATA_FLAGS = 2
SLDF_HAS_NAME: SHELL_LINK_DATA_FLAGS = 4
SLDF_HAS_RELPATH: SHELL_LINK_DATA_FLAGS = 8
SLDF_HAS_WORKINGDIR: SHELL_LINK_DATA_FLAGS = 16
SLDF_HAS_ARGS: SHELL_LINK_DATA_FLAGS = 32
SLDF_HAS_ICONLOCATION: SHELL_LINK_DATA_FLAGS = 64
SLDF_UNICODE: SHELL_LINK_DATA_FLAGS = 128
SLDF_FORCE_NO_LINKINFO: SHELL_LINK_DATA_FLAGS = 256
SLDF_HAS_EXP_SZ: SHELL_LINK_DATA_FLAGS = 512
SLDF_RUN_IN_SEPARATE: SHELL_LINK_DATA_FLAGS = 1024
SLDF_HAS_DARWINID: SHELL_LINK_DATA_FLAGS = 4096
SLDF_RUNAS_USER: SHELL_LINK_DATA_FLAGS = 8192
SLDF_HAS_EXP_ICON_SZ: SHELL_LINK_DATA_FLAGS = 16384
SLDF_NO_PIDL_ALIAS: SHELL_LINK_DATA_FLAGS = 32768
SLDF_FORCE_UNCNAME: SHELL_LINK_DATA_FLAGS = 65536
SLDF_RUN_WITH_SHIMLAYER: SHELL_LINK_DATA_FLAGS = 131072
SLDF_FORCE_NO_LINKTRACK: SHELL_LINK_DATA_FLAGS = 262144
SLDF_ENABLE_TARGET_METADATA: SHELL_LINK_DATA_FLAGS = 524288
SLDF_DISABLE_LINK_PATH_TRACKING: SHELL_LINK_DATA_FLAGS = 1048576
SLDF_DISABLE_KNOWNFOLDER_RELATIVE_TRACKING: SHELL_LINK_DATA_FLAGS = 2097152
SLDF_NO_KF_ALIAS: SHELL_LINK_DATA_FLAGS = 4194304
SLDF_ALLOW_LINK_TO_LINK: SHELL_LINK_DATA_FLAGS = 8388608
SLDF_UNALIAS_ON_SAVE: SHELL_LINK_DATA_FLAGS = 16777216
SLDF_PREFER_ENVIRONMENT_PATH: SHELL_LINK_DATA_FLAGS = 33554432
SLDF_KEEP_LOCAL_IDLIST_FOR_UNC_TARGET: SHELL_LINK_DATA_FLAGS = 67108864
SLDF_PERSIST_VOLUME_ID_RELATIVE: SHELL_LINK_DATA_FLAGS = 134217728
SLDF_VALID: SHELL_LINK_DATA_FLAGS = 268433407
SLDF_RESERVED: SHELL_LINK_DATA_FLAGS = -2147483648
SHELL_UI_COMPONENT = Int32
SHELL_UI_COMPONENT_TASKBARS: SHELL_UI_COMPONENT = 0
SHELL_UI_COMPONENT_NOTIFICATIONAREA: SHELL_UI_COMPONENT = 1
SHELL_UI_COMPONENT_DESKBAND: SHELL_UI_COMPONENT = 2
if ARCH in 'X64,ARM64':
    class SHFILEINFOA(Structure):
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        iIcon: Int32
        dwAttributes: UInt32
        szDisplayName: Windows.Win32.Foundation.CHAR * 260
        szTypeName: Windows.Win32.Foundation.CHAR * 80
if ARCH in 'X86':
    class SHFILEINFOA(Structure):
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        iIcon: Int32
        dwAttributes: UInt32
        szDisplayName: Windows.Win32.Foundation.CHAR * 260
        szTypeName: Windows.Win32.Foundation.CHAR * 80
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class SHFILEINFOW(Structure):
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        iIcon: Int32
        dwAttributes: UInt32
        szDisplayName: Char * 260
        szTypeName: Char * 80
if ARCH in 'X86':
    class SHFILEINFOW(Structure):
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        iIcon: Int32
        dwAttributes: UInt32
        szDisplayName: Char * 260
        szTypeName: Char * 80
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class SHFILEOPSTRUCTA(Structure):
        hwnd: Windows.Win32.Foundation.HWND
        wFunc: UInt32
        pFrom: POINTER(SByte)
        pTo: POINTER(SByte)
        fFlags: UInt16
        fAnyOperationsAborted: Windows.Win32.Foundation.BOOL
        hNameMappings: c_void_p
        lpszProgressTitle: Windows.Win32.Foundation.PSTR
if ARCH in 'X86':
    class SHFILEOPSTRUCTA(Structure):
        hwnd: Windows.Win32.Foundation.HWND
        wFunc: UInt32
        pFrom: POINTER(SByte)
        pTo: POINTER(SByte)
        fFlags: UInt16
        fAnyOperationsAborted: Windows.Win32.Foundation.BOOL
        hNameMappings: c_void_p
        lpszProgressTitle: Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class SHFILEOPSTRUCTW(Structure):
        hwnd: Windows.Win32.Foundation.HWND
        wFunc: UInt32
        pFrom: Windows.Win32.Foundation.PWSTR
        pTo: Windows.Win32.Foundation.PWSTR
        fFlags: UInt16
        fAnyOperationsAborted: Windows.Win32.Foundation.BOOL
        hNameMappings: c_void_p
        lpszProgressTitle: Windows.Win32.Foundation.PWSTR
if ARCH in 'X86':
    class SHFILEOPSTRUCTW(Structure):
        hwnd: Windows.Win32.Foundation.HWND
        wFunc: UInt32
        pFrom: Windows.Win32.Foundation.PWSTR
        pTo: Windows.Win32.Foundation.PWSTR
        fFlags: UInt16
        fAnyOperationsAborted: Windows.Win32.Foundation.BOOL
        hNameMappings: c_void_p
        lpszProgressTitle: Windows.Win32.Foundation.PWSTR
        _pack_ = 1
SHFMT_ID = UInt32
SHFMT_ID_DEFAULT: SHFMT_ID = 65535
SHFMT_OPT = Int32
SHFMT_OPT_NONE: SHFMT_OPT = 0
SHFMT_OPT_FULL: SHFMT_OPT = 1
SHFMT_OPT_SYSONLY: SHFMT_OPT = 2
SHFMT_RET = UInt32
SHFMT_ERROR: SHFMT_RET = 4294967295
SHFMT_CANCEL: SHFMT_RET = 4294967294
SHFMT_NOFORMAT: SHFMT_RET = 4294967293
class SHFOLDERCUSTOMSETTINGS(Structure):
    dwSize: UInt32
    dwMask: UInt32
    pvid: POINTER(Guid)
    pszWebViewTemplate: Windows.Win32.Foundation.PWSTR
    cchWebViewTemplate: UInt32
    pszWebViewTemplateVersion: Windows.Win32.Foundation.PWSTR
    pszInfoTip: Windows.Win32.Foundation.PWSTR
    cchInfoTip: UInt32
    pclsid: POINTER(Guid)
    dwFlags: UInt32
    pszIconFile: Windows.Win32.Foundation.PWSTR
    cchIconFile: UInt32
    iIconIndex: Int32
    pszLogo: Windows.Win32.Foundation.PWSTR
    cchLogo: UInt32
SHGDFIL_FORMAT = Int32
SHGDFIL_FINDDATA: SHGDFIL_FORMAT = 1
SHGDFIL_NETRESOURCE: SHGDFIL_FORMAT = 2
SHGDFIL_DESCRIPTIONID: SHGDFIL_FORMAT = 3
SHGDNF = UInt32
SHGDN_NORMAL: SHGDNF = 0
SHGDN_INFOLDER: SHGDNF = 1
SHGDN_FOREDITING: SHGDNF = 4096
SHGDN_FORADDRESSBAR: SHGDNF = 16384
SHGDN_FORPARSING: SHGDNF = 32768
SHGFI_FLAGS = Int32
SHGFI_ADDOVERLAYS: SHGFI_FLAGS = 32
SHGFI_ATTR_SPECIFIED: SHGFI_FLAGS = 131072
SHGFI_ATTRIBUTES: SHGFI_FLAGS = 2048
SHGFI_DISPLAYNAME: SHGFI_FLAGS = 512
SHGFI_EXETYPE: SHGFI_FLAGS = 8192
SHGFI_ICON: SHGFI_FLAGS = 256
SHGFI_ICONLOCATION: SHGFI_FLAGS = 4096
SHGFI_LARGEICON: SHGFI_FLAGS = 0
SHGFI_LINKOVERLAY: SHGFI_FLAGS = 32768
SHGFI_OPENICON: SHGFI_FLAGS = 2
SHGFI_OVERLAYINDEX: SHGFI_FLAGS = 64
SHGFI_PIDL: SHGFI_FLAGS = 8
SHGFI_SELECTED: SHGFI_FLAGS = 65536
SHGFI_SHELLICONSIZE: SHGFI_FLAGS = 4
SHGFI_SMALLICON: SHGFI_FLAGS = 1
SHGFI_SYSICONINDEX: SHGFI_FLAGS = 16384
SHGFI_TYPENAME: SHGFI_FLAGS = 1024
SHGFI_USEFILEATTRIBUTES: SHGFI_FLAGS = 16
SHGFP_TYPE = Int32
SHGFP_TYPE_CURRENT: SHGFP_TYPE = 0
SHGFP_TYPE_DEFAULT: SHGFP_TYPE = 1
SHGLOBALCOUNTER = Int32
GLOBALCOUNTER_SEARCHMANAGER: SHGLOBALCOUNTER = 0
GLOBALCOUNTER_SEARCHOPTIONS: SHGLOBALCOUNTER = 1
GLOBALCOUNTER_FOLDERSETTINGSCHANGE: SHGLOBALCOUNTER = 2
GLOBALCOUNTER_RATINGS: SHGLOBALCOUNTER = 3
GLOBALCOUNTER_APPROVEDSITES: SHGLOBALCOUNTER = 4
GLOBALCOUNTER_RESTRICTIONS: SHGLOBALCOUNTER = 5
GLOBALCOUNTER_SHELLSETTINGSCHANGED: SHGLOBALCOUNTER = 6
GLOBALCOUNTER_SYSTEMPIDLCHANGE: SHGLOBALCOUNTER = 7
GLOBALCOUNTER_OVERLAYMANAGER: SHGLOBALCOUNTER = 8
GLOBALCOUNTER_QUERYASSOCIATIONS: SHGLOBALCOUNTER = 9
GLOBALCOUNTER_IESESSIONS: SHGLOBALCOUNTER = 10
GLOBALCOUNTER_IEONLY_SESSIONS: SHGLOBALCOUNTER = 11
GLOBALCOUNTER_APPLICATION_DESTINATIONS: SHGLOBALCOUNTER = 12
__UNUSED_RECYCLE_WAS_GLOBALCOUNTER_CSCSYNCINPROGRESS: SHGLOBALCOUNTER = 13
GLOBALCOUNTER_BITBUCKETNUMDELETERS: SHGLOBALCOUNTER = 14
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SHARES: SHGLOBALCOUNTER = 15
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_A: SHGLOBALCOUNTER = 16
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_B: SHGLOBALCOUNTER = 17
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_C: SHGLOBALCOUNTER = 18
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_D: SHGLOBALCOUNTER = 19
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_E: SHGLOBALCOUNTER = 20
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_F: SHGLOBALCOUNTER = 21
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_G: SHGLOBALCOUNTER = 22
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_H: SHGLOBALCOUNTER = 23
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_I: SHGLOBALCOUNTER = 24
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_J: SHGLOBALCOUNTER = 25
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_K: SHGLOBALCOUNTER = 26
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_L: SHGLOBALCOUNTER = 27
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_M: SHGLOBALCOUNTER = 28
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_N: SHGLOBALCOUNTER = 29
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_O: SHGLOBALCOUNTER = 30
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_P: SHGLOBALCOUNTER = 31
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Q: SHGLOBALCOUNTER = 32
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_R: SHGLOBALCOUNTER = 33
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_S: SHGLOBALCOUNTER = 34
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_T: SHGLOBALCOUNTER = 35
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_U: SHGLOBALCOUNTER = 36
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_V: SHGLOBALCOUNTER = 37
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_W: SHGLOBALCOUNTER = 38
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_X: SHGLOBALCOUNTER = 39
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Y: SHGLOBALCOUNTER = 40
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Z: SHGLOBALCOUNTER = 41
__UNUSED_RECYCLE_WAS_GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SERVERDRIVE: SHGLOBALCOUNTER = 42
__UNUSED_RECYCLE_WAS_GLOBALCOUNTER_RECYCLEGLOBALDIRTYCOUNT: SHGLOBALCOUNTER = 43
GLOBALCOUNTER_RECYCLEBINENUM: SHGLOBALCOUNTER = 44
GLOBALCOUNTER_RECYCLEBINCORRUPTED: SHGLOBALCOUNTER = 45
GLOBALCOUNTER_RATINGS_STATECOUNTER: SHGLOBALCOUNTER = 46
GLOBALCOUNTER_PRIVATE_PROFILE_CACHE: SHGLOBALCOUNTER = 47
GLOBALCOUNTER_INTERNETTOOLBAR_LAYOUT: SHGLOBALCOUNTER = 48
GLOBALCOUNTER_FOLDERDEFINITION_CACHE: SHGLOBALCOUNTER = 49
GLOBALCOUNTER_COMMONPLACES_LIST_CACHE: SHGLOBALCOUNTER = 50
GLOBALCOUNTER_PRIVATE_PROFILE_CACHE_MACHINEWIDE: SHGLOBALCOUNTER = 51
GLOBALCOUNTER_ASSOCCHANGED: SHGLOBALCOUNTER = 52
GLOBALCOUNTER_APP_ITEMS_STATE_STORE_CACHE: SHGLOBALCOUNTER = 53
GLOBALCOUNTER_SETTINGSYNC_ENABLED: SHGLOBALCOUNTER = 54
GLOBALCOUNTER_APPSFOLDER_FILETYPEASSOCIATION_COUNTER: SHGLOBALCOUNTER = 55
GLOBALCOUNTER_USERINFOCHANGED: SHGLOBALCOUNTER = 56
GLOBALCOUNTER_SYNC_ENGINE_INFORMATION_CACHE_MACHINEWIDE: SHGLOBALCOUNTER = 57
GLOBALCOUNTER_BANNERS_DATAMODEL_CACHE_MACHINEWIDE: SHGLOBALCOUNTER = 58
GLOBALCOUNTER_MAXIMUMVALUE: SHGLOBALCOUNTER = 59
SHGSI_FLAGS = UInt32
SHGSI_ICONLOCATION: SHGSI_FLAGS = 0
SHGSI_ICON: SHGSI_FLAGS = 256
SHGSI_SYSICONINDEX: SHGSI_FLAGS = 16384
SHGSI_LINKOVERLAY: SHGSI_FLAGS = 32768
SHGSI_SELECTED: SHGSI_FLAGS = 65536
SHGSI_LARGEICON: SHGSI_FLAGS = 0
SHGSI_SMALLICON: SHGSI_FLAGS = 1
SHGSI_SHELLICONSIZE: SHGSI_FLAGS = 4
if ARCH in 'X64,ARM64':
    class SHNAMEMAPPINGA(Structure):
        pszOldPath: Windows.Win32.Foundation.PSTR
        pszNewPath: Windows.Win32.Foundation.PSTR
        cchOldPath: Int32
        cchNewPath: Int32
if ARCH in 'X86':
    class SHNAMEMAPPINGA(Structure):
        pszOldPath: Windows.Win32.Foundation.PSTR
        pszNewPath: Windows.Win32.Foundation.PSTR
        cchOldPath: Int32
        cchNewPath: Int32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class SHNAMEMAPPINGW(Structure):
        pszOldPath: Windows.Win32.Foundation.PWSTR
        pszNewPath: Windows.Win32.Foundation.PWSTR
        cchOldPath: Int32
        cchNewPath: Int32
if ARCH in 'X86':
    class SHNAMEMAPPINGW(Structure):
        pszOldPath: Windows.Win32.Foundation.PWSTR
        pszNewPath: Windows.Win32.Foundation.PWSTR
        cchOldPath: Int32
        cchNewPath: Int32
        _pack_ = 1
SHOP_TYPE = Int32
SHOP_PRINTERNAME: SHOP_TYPE = 1
SHOP_FILEPATH: SHOP_TYPE = 2
SHOP_VOLUMEGUID: SHOP_TYPE = 4
if ARCH in 'X64,ARM64':
    class SHQUERYRBINFO(Structure):
        cbSize: UInt32
        i64Size: Int64
        i64NumItems: Int64
if ARCH in 'X86':
    class SHQUERYRBINFO(Structure):
        cbSize: UInt32
        i64Size: Int64
        i64NumItems: Int64
        _pack_ = 1
SHREGDEL_FLAGS = Int32
SHREGDEL_DEFAULT: SHREGDEL_FLAGS = 0
SHREGDEL_HKCU: SHREGDEL_FLAGS = 1
SHREGDEL_HKLM: SHREGDEL_FLAGS = 16
SHREGDEL_BOTH: SHREGDEL_FLAGS = 17
SHREGENUM_FLAGS = Int32
SHREGENUM_DEFAULT: SHREGENUM_FLAGS = 0
SHREGENUM_HKCU: SHREGENUM_FLAGS = 1
SHREGENUM_HKLM: SHREGENUM_FLAGS = 16
SHREGENUM_BOTH: SHREGENUM_FLAGS = 17
SHSTOCKICONID = Int32
SIID_DOCNOASSOC: SHSTOCKICONID = 0
SIID_DOCASSOC: SHSTOCKICONID = 1
SIID_APPLICATION: SHSTOCKICONID = 2
SIID_FOLDER: SHSTOCKICONID = 3
SIID_FOLDEROPEN: SHSTOCKICONID = 4
SIID_DRIVE525: SHSTOCKICONID = 5
SIID_DRIVE35: SHSTOCKICONID = 6
SIID_DRIVEREMOVE: SHSTOCKICONID = 7
SIID_DRIVEFIXED: SHSTOCKICONID = 8
SIID_DRIVENET: SHSTOCKICONID = 9
SIID_DRIVENETDISABLED: SHSTOCKICONID = 10
SIID_DRIVECD: SHSTOCKICONID = 11
SIID_DRIVERAM: SHSTOCKICONID = 12
SIID_WORLD: SHSTOCKICONID = 13
SIID_SERVER: SHSTOCKICONID = 15
SIID_PRINTER: SHSTOCKICONID = 16
SIID_MYNETWORK: SHSTOCKICONID = 17
SIID_FIND: SHSTOCKICONID = 22
SIID_HELP: SHSTOCKICONID = 23
SIID_SHARE: SHSTOCKICONID = 28
SIID_LINK: SHSTOCKICONID = 29
SIID_SLOWFILE: SHSTOCKICONID = 30
SIID_RECYCLER: SHSTOCKICONID = 31
SIID_RECYCLERFULL: SHSTOCKICONID = 32
SIID_MEDIACDAUDIO: SHSTOCKICONID = 40
SIID_LOCK: SHSTOCKICONID = 47
SIID_AUTOLIST: SHSTOCKICONID = 49
SIID_PRINTERNET: SHSTOCKICONID = 50
SIID_SERVERSHARE: SHSTOCKICONID = 51
SIID_PRINTERFAX: SHSTOCKICONID = 52
SIID_PRINTERFAXNET: SHSTOCKICONID = 53
SIID_PRINTERFILE: SHSTOCKICONID = 54
SIID_STACK: SHSTOCKICONID = 55
SIID_MEDIASVCD: SHSTOCKICONID = 56
SIID_STUFFEDFOLDER: SHSTOCKICONID = 57
SIID_DRIVEUNKNOWN: SHSTOCKICONID = 58
SIID_DRIVEDVD: SHSTOCKICONID = 59
SIID_MEDIADVD: SHSTOCKICONID = 60
SIID_MEDIADVDRAM: SHSTOCKICONID = 61
SIID_MEDIADVDRW: SHSTOCKICONID = 62
SIID_MEDIADVDR: SHSTOCKICONID = 63
SIID_MEDIADVDROM: SHSTOCKICONID = 64
SIID_MEDIACDAUDIOPLUS: SHSTOCKICONID = 65
SIID_MEDIACDRW: SHSTOCKICONID = 66
SIID_MEDIACDR: SHSTOCKICONID = 67
SIID_MEDIACDBURN: SHSTOCKICONID = 68
SIID_MEDIABLANKCD: SHSTOCKICONID = 69
SIID_MEDIACDROM: SHSTOCKICONID = 70
SIID_AUDIOFILES: SHSTOCKICONID = 71
SIID_IMAGEFILES: SHSTOCKICONID = 72
SIID_VIDEOFILES: SHSTOCKICONID = 73
SIID_MIXEDFILES: SHSTOCKICONID = 74
SIID_FOLDERBACK: SHSTOCKICONID = 75
SIID_FOLDERFRONT: SHSTOCKICONID = 76
SIID_SHIELD: SHSTOCKICONID = 77
SIID_WARNING: SHSTOCKICONID = 78
SIID_INFO: SHSTOCKICONID = 79
SIID_ERROR: SHSTOCKICONID = 80
SIID_KEY: SHSTOCKICONID = 81
SIID_SOFTWARE: SHSTOCKICONID = 82
SIID_RENAME: SHSTOCKICONID = 83
SIID_DELETE: SHSTOCKICONID = 84
SIID_MEDIAAUDIODVD: SHSTOCKICONID = 85
SIID_MEDIAMOVIEDVD: SHSTOCKICONID = 86
SIID_MEDIAENHANCEDCD: SHSTOCKICONID = 87
SIID_MEDIAENHANCEDDVD: SHSTOCKICONID = 88
SIID_MEDIAHDDVD: SHSTOCKICONID = 89
SIID_MEDIABLURAY: SHSTOCKICONID = 90
SIID_MEDIAVCD: SHSTOCKICONID = 91
SIID_MEDIADVDPLUSR: SHSTOCKICONID = 92
SIID_MEDIADVDPLUSRW: SHSTOCKICONID = 93
SIID_DESKTOPPC: SHSTOCKICONID = 94
SIID_MOBILEPC: SHSTOCKICONID = 95
SIID_USERS: SHSTOCKICONID = 96
SIID_MEDIASMARTMEDIA: SHSTOCKICONID = 97
SIID_MEDIACOMPACTFLASH: SHSTOCKICONID = 98
SIID_DEVICECELLPHONE: SHSTOCKICONID = 99
SIID_DEVICECAMERA: SHSTOCKICONID = 100
SIID_DEVICEVIDEOCAMERA: SHSTOCKICONID = 101
SIID_DEVICEAUDIOPLAYER: SHSTOCKICONID = 102
SIID_NETWORKCONNECT: SHSTOCKICONID = 103
SIID_INTERNET: SHSTOCKICONID = 104
SIID_ZIPFILE: SHSTOCKICONID = 105
SIID_SETTINGS: SHSTOCKICONID = 106
SIID_DRIVEHDDVD: SHSTOCKICONID = 132
SIID_DRIVEBD: SHSTOCKICONID = 133
SIID_MEDIAHDDVDROM: SHSTOCKICONID = 134
SIID_MEDIAHDDVDR: SHSTOCKICONID = 135
SIID_MEDIAHDDVDRAM: SHSTOCKICONID = 136
SIID_MEDIABDROM: SHSTOCKICONID = 137
SIID_MEDIABDR: SHSTOCKICONID = 138
SIID_MEDIABDRE: SHSTOCKICONID = 139
SIID_CLUSTEREDDRIVE: SHSTOCKICONID = 140
SIID_MAX_ICONS: SHSTOCKICONID = 181
if ARCH in 'X64,ARM64':
    class SHSTOCKICONINFO(Structure):
        cbSize: UInt32
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        iSysImageIndex: Int32
        iIcon: Int32
        szPath: Char * 260
if ARCH in 'X86':
    class SHSTOCKICONINFO(Structure):
        cbSize: UInt32
        hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
        iSysImageIndex: Int32
        iIcon: Int32
        szPath: Char * 260
        _pack_ = 1
SIATTRIBFLAGS = Int32
SIATTRIBFLAGS_AND: SIATTRIBFLAGS = 1
SIATTRIBFLAGS_OR: SIATTRIBFLAGS = 2
SIATTRIBFLAGS_APPCOMPAT: SIATTRIBFLAGS = 3
SIATTRIBFLAGS_MASK: SIATTRIBFLAGS = 3
SIATTRIBFLAGS_ALLITEMS: SIATTRIBFLAGS = 16384
SIGDN = Int32
SIGDN_NORMALDISPLAY: SIGDN = 0
SIGDN_PARENTRELATIVEPARSING: SIGDN = -2147385343
SIGDN_DESKTOPABSOLUTEPARSING: SIGDN = -2147319808
SIGDN_PARENTRELATIVEEDITING: SIGDN = -2147282943
SIGDN_DESKTOPABSOLUTEEDITING: SIGDN = -2147172352
SIGDN_FILESYSPATH: SIGDN = -2147123200
SIGDN_URL: SIGDN = -2147057664
SIGDN_PARENTRELATIVEFORADDRESSBAR: SIGDN = -2146975743
SIGDN_PARENTRELATIVE: SIGDN = -2146959359
SIGDN_PARENTRELATIVEFORUI: SIGDN = -2146877439
SIIGBF = Int32
SIIGBF_RESIZETOFIT: SIIGBF = 0
SIIGBF_BIGGERSIZEOK: SIIGBF = 1
SIIGBF_MEMORYONLY: SIIGBF = 2
SIIGBF_ICONONLY: SIIGBF = 4
SIIGBF_THUMBNAILONLY: SIIGBF = 8
SIIGBF_INCACHEONLY: SIIGBF = 16
SIIGBF_CROPTOSQUARE: SIIGBF = 32
SIIGBF_WIDETHUMBNAILS: SIIGBF = 64
SIIGBF_ICONBACKGROUND: SIIGBF = 128
SIIGBF_SCALEUP: SIIGBF = 256
SLGP_FLAGS = Int32
SLGP_SHORTPATH: SLGP_FLAGS = 1
SLGP_UNCPRIORITY: SLGP_FLAGS = 2
SLGP_RAWPATH: SLGP_FLAGS = 4
SLGP_RELATIVEPRIORITY: SLGP_FLAGS = 8
class SLOWAPPINFO(Structure):
    ullSize: UInt64
    ftLastUsed: Windows.Win32.Foundation.FILETIME
    iTimesUsed: Int32
    pszImage: Windows.Win32.Foundation.PWSTR
SLR_FLAGS = Int32
SLR_NONE: SLR_FLAGS = 0
SLR_NO_UI: SLR_FLAGS = 1
SLR_ANY_MATCH: SLR_FLAGS = 2
SLR_UPDATE: SLR_FLAGS = 4
SLR_NOUPDATE: SLR_FLAGS = 8
SLR_NOSEARCH: SLR_FLAGS = 16
SLR_NOTRACK: SLR_FLAGS = 32
SLR_NOLINKINFO: SLR_FLAGS = 64
SLR_INVOKE_MSI: SLR_FLAGS = 128
SLR_NO_UI_WITH_MSG_PUMP: SLR_FLAGS = 257
SLR_OFFER_DELETE_WITHOUT_FILE: SLR_FLAGS = 512
SLR_KNOWNFOLDER: SLR_FLAGS = 1024
SLR_MACHINE_IN_LOCAL_TARGET: SLR_FLAGS = 2048
SLR_UPDATE_MACHINE_AND_SID: SLR_FLAGS = 4096
SLR_NO_OBJECT_ID: SLR_FLAGS = 8192
class SMCSHCHANGENOTIFYSTRUCT(Structure):
    lEvent: Int32
    pidl1: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    pidl2: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
class SMDATA(Structure):
    dwMask: UInt32
    dwFlags: UInt32
    hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU
    hwnd: Windows.Win32.Foundation.HWND
    uId: UInt32
    uIdParent: UInt32
    uIdAncestor: UInt32
    punk: Windows.Win32.System.Com.IUnknown_head
    pidlFolder: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    pidlItem: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    psf: Windows.Win32.UI.Shell.IShellFolder_head
    pvUserData: c_void_p
class SMINFO(Structure):
    dwMask: UInt32
    dwType: UInt32
    dwFlags: UInt32
    iIcon: Int32
SMINFOFLAGS = Int32
SMIF_ICON: SMINFOFLAGS = 1
SMIF_ACCELERATOR: SMINFOFLAGS = 2
SMIF_DROPTARGET: SMINFOFLAGS = 4
SMIF_SUBMENU: SMINFOFLAGS = 8
SMIF_CHECKED: SMINFOFLAGS = 32
SMIF_DROPCASCADE: SMINFOFLAGS = 64
SMIF_HIDDEN: SMINFOFLAGS = 128
SMIF_DISABLED: SMINFOFLAGS = 256
SMIF_TRACKPOPUP: SMINFOFLAGS = 512
SMIF_DEMOTED: SMINFOFLAGS = 1024
SMIF_ALTSTATE: SMINFOFLAGS = 2048
SMIF_DRAGNDROP: SMINFOFLAGS = 4096
SMIF_NEW: SMINFOFLAGS = 8192
SMINFOMASK = Int32
SMIM_TYPE: SMINFOMASK = 1
SMIM_FLAGS: SMINFOMASK = 2
SMIM_ICON: SMINFOMASK = 4
SMINFOTYPE = Int32
SMIT_SEPARATOR: SMINFOTYPE = 1
SMIT_STRING: SMINFOTYPE = 2
class SORTCOLUMN(Structure):
    propkey: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY
    direction: Windows.Win32.UI.Shell.SORTDIRECTION
SORTDIRECTION = Int32
SORT_DESCENDING: SORTDIRECTION = -1
SORT_ASCENDING: SORTDIRECTION = 1
SORT_ORDER_TYPE = Int32
SOT_DEFAULT: SORT_ORDER_TYPE = 0
SOT_IGNORE_FOLDERNESS: SORT_ORDER_TYPE = 1
SPACTION = Int32
SPACTION_NONE: SPACTION = 0
SPACTION_MOVING: SPACTION = 1
SPACTION_COPYING: SPACTION = 2
SPACTION_RECYCLING: SPACTION = 3
SPACTION_APPLYINGATTRIBS: SPACTION = 4
SPACTION_DOWNLOADING: SPACTION = 5
SPACTION_SEARCHING_INTERNET: SPACTION = 6
SPACTION_CALCULATING: SPACTION = 7
SPACTION_UPLOADING: SPACTION = 8
SPACTION_SEARCHING_FILES: SPACTION = 9
SPACTION_DELETING: SPACTION = 10
SPACTION_RENAMING: SPACTION = 11
SPACTION_FORMATTING: SPACTION = 12
SPACTION_COPY_MOVING: SPACTION = 13
SPTEXT = Int32
SPTEXT_ACTIONDESCRIPTION: SPTEXT = 1
SPTEXT_ACTIONDETAIL: SPTEXT = 2
SSF_MASK = UInt32
SSF_SHOWALLOBJECTS: SSF_MASK = 1
SSF_SHOWEXTENSIONS: SSF_MASK = 2
SSF_HIDDENFILEEXTS: SSF_MASK = 4
SSF_SERVERADMINUI: SSF_MASK = 4
SSF_SHOWCOMPCOLOR: SSF_MASK = 8
SSF_SORTCOLUMNS: SSF_MASK = 16
SSF_SHOWSYSFILES: SSF_MASK = 32
SSF_DOUBLECLICKINWEBVIEW: SSF_MASK = 128
SSF_SHOWATTRIBCOL: SSF_MASK = 256
SSF_DESKTOPHTML: SSF_MASK = 512
SSF_WIN95CLASSIC: SSF_MASK = 1024
SSF_DONTPRETTYPATH: SSF_MASK = 2048
SSF_SHOWINFOTIP: SSF_MASK = 8192
SSF_MAPNETDRVBUTTON: SSF_MASK = 4096
SSF_NOCONFIRMRECYCLE: SSF_MASK = 32768
SSF_HIDEICONS: SSF_MASK = 16384
SSF_FILTER: SSF_MASK = 65536
SSF_WEBVIEW: SSF_MASK = 131072
SSF_SHOWSUPERHIDDEN: SSF_MASK = 262144
SSF_SEPPROCESS: SSF_MASK = 524288
SSF_NONETCRAWLING: SSF_MASK = 1048576
SSF_STARTPANELON: SSF_MASK = 2097152
SSF_SHOWSTARTPAGE: SSF_MASK = 4194304
SSF_AUTOCHECKSELECT: SSF_MASK = 8388608
SSF_ICONSONLY: SSF_MASK = 16777216
SSF_SHOWTYPEOVERLAY: SSF_MASK = 33554432
SSF_SHOWSTATUSBAR: SSF_MASK = 67108864
STGOP = Int32
STGOP_MOVE: STGOP = 1
STGOP_COPY: STGOP = 2
STGOP_SYNC: STGOP = 3
STGOP_REMOVE: STGOP = 5
STGOP_RENAME: STGOP = 6
STGOP_APPLYPROPERTIES: STGOP = 8
STGOP_NEW: STGOP = 10
STORAGE_PROVIDER_FILE_FLAGS = Int32
SPFF_NONE: STORAGE_PROVIDER_FILE_FLAGS = 0
SPFF_DOWNLOAD_BY_DEFAULT: STORAGE_PROVIDER_FILE_FLAGS = 1
SPFF_CREATED_ON_THIS_DEVICE: STORAGE_PROVIDER_FILE_FLAGS = 2
STPFLAG = Int32
STPF_NONE: STPFLAG = 0
STPF_USEAPPTHUMBNAILALWAYS: STPFLAG = 1
STPF_USEAPPTHUMBNAILWHENACTIVE: STPFLAG = 2
STPF_USEAPPPEEKALWAYS: STPFLAG = 4
STPF_USEAPPPEEKWHENACTIVE: STPFLAG = 8
@winfunctype_pointer
def SUBCLASSPROC(hWnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, uIdSubclass: UIntPtr, dwRefData: UIntPtr) -> Windows.Win32.Foundation.LRESULT: ...
class SV2CVW2_PARAMS(Structure):
    cbSize: UInt32
    psvPrev: Windows.Win32.UI.Shell.IShellView_head
    pfs: POINTER(Windows.Win32.UI.Shell.FOLDERSETTINGS_head)
    psbOwner: Windows.Win32.UI.Shell.IShellBrowser_head
    prcView: POINTER(Windows.Win32.Foundation.RECT_head)
    pvid: POINTER(Guid)
    hwndView: Windows.Win32.Foundation.HWND
SVUIA_STATUS = Int32
SVUIA_DEACTIVATE: SVUIA_STATUS = 0
SVUIA_ACTIVATE_NOFOCUS: SVUIA_STATUS = 1
SVUIA_ACTIVATE_FOCUS: SVUIA_STATUS = 2
SVUIA_INPLACEACTIVATE: SVUIA_STATUS = 3
SYNCMGRERRORFLAGS = Int32
SYNCMGRERRORFLAG_ENABLEJUMPTEXT: SYNCMGRERRORFLAGS = 1
SYNCMGRFLAG = Int32
SYNCMGRFLAG_CONNECT: SYNCMGRFLAG = 1
SYNCMGRFLAG_PENDINGDISCONNECT: SYNCMGRFLAG = 2
SYNCMGRFLAG_MANUAL: SYNCMGRFLAG = 3
SYNCMGRFLAG_IDLE: SYNCMGRFLAG = 4
SYNCMGRFLAG_INVOKE: SYNCMGRFLAG = 5
SYNCMGRFLAG_SCHEDULED: SYNCMGRFLAG = 6
SYNCMGRFLAG_EVENTMASK: SYNCMGRFLAG = 255
SYNCMGRFLAG_SETTINGS: SYNCMGRFLAG = 256
SYNCMGRFLAG_MAYBOTHERUSER: SYNCMGRFLAG = 512
SYNCMGRHANDLERFLAGS = Int32
SYNCMGRHANDLER_HASPROPERTIES: SYNCMGRHANDLERFLAGS = 1
SYNCMGRHANDLER_MAYESTABLISHCONNECTION: SYNCMGRHANDLERFLAGS = 2
SYNCMGRHANDLER_ALWAYSLISTHANDLER: SYNCMGRHANDLERFLAGS = 4
SYNCMGRHANDLER_HIDDEN: SYNCMGRHANDLERFLAGS = 8
class SYNCMGRHANDLERINFO(Structure):
    cbSize: UInt32
    hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
    SyncMgrHandlerFlags: UInt32
    wszHandlerName: Char * 32
SYNCMGRINVOKEFLAGS = Int32
SYNCMGRINVOKE_STARTSYNC: SYNCMGRINVOKEFLAGS = 2
SYNCMGRINVOKE_MINIMIZED: SYNCMGRINVOKEFLAGS = 4
class SYNCMGRITEM(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    ItemID: Guid
    dwItemState: UInt32
    hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
    wszItemName: Char * 128
    ftLastUpdate: Windows.Win32.Foundation.FILETIME
SYNCMGRITEMFLAGS = Int32
SYNCMGRITEM_HASPROPERTIES: SYNCMGRITEMFLAGS = 1
SYNCMGRITEM_TEMPORARY: SYNCMGRITEMFLAGS = 2
SYNCMGRITEM_ROAMINGUSER: SYNCMGRITEMFLAGS = 4
SYNCMGRITEM_LASTUPDATETIME: SYNCMGRITEMFLAGS = 8
SYNCMGRITEM_MAYDELETEITEM: SYNCMGRITEMFLAGS = 16
SYNCMGRITEM_HIDDEN: SYNCMGRITEMFLAGS = 32
SYNCMGRITEMSTATE = Int32
SYNCMGRITEMSTATE_UNCHECKED: SYNCMGRITEMSTATE = 0
SYNCMGRITEMSTATE_CHECKED: SYNCMGRITEMSTATE = 1
class SYNCMGRLOGERRORINFO(Structure):
    cbSize: UInt32
    mask: UInt32
    dwSyncMgrErrorFlags: UInt32
    ErrorID: Guid
    ItemID: Guid
SYNCMGRLOGLEVEL = Int32
SYNCMGRLOGLEVEL_INFORMATION: SYNCMGRLOGLEVEL = 1
SYNCMGRLOGLEVEL_WARNING: SYNCMGRLOGLEVEL = 2
SYNCMGRLOGLEVEL_ERROR: SYNCMGRLOGLEVEL = 3
SYNCMGRLOGLEVEL_LOGLEVELMAX: SYNCMGRLOGLEVEL = 3
class SYNCMGRPROGRESSITEM(Structure):
    cbSize: UInt32
    mask: UInt32
    lpcStatusText: Windows.Win32.Foundation.PWSTR
    dwStatusType: UInt32
    iProgValue: Int32
    iMaxValue: Int32
SYNCMGRREGISTERFLAGS = Int32
SYNCMGRREGISTERFLAG_CONNECT: SYNCMGRREGISTERFLAGS = 1
SYNCMGRREGISTERFLAG_PENDINGDISCONNECT: SYNCMGRREGISTERFLAGS = 2
SYNCMGRREGISTERFLAG_IDLE: SYNCMGRREGISTERFLAGS = 4
SYNCMGRSTATUS = Int32
SYNCMGRSTATUS_STOPPED: SYNCMGRSTATUS = 0
SYNCMGRSTATUS_SKIPPED: SYNCMGRSTATUS = 1
SYNCMGRSTATUS_PENDING: SYNCMGRSTATUS = 2
SYNCMGRSTATUS_UPDATING: SYNCMGRSTATUS = 3
SYNCMGRSTATUS_SUCCEEDED: SYNCMGRSTATUS = 4
SYNCMGRSTATUS_FAILED: SYNCMGRSTATUS = 5
SYNCMGRSTATUS_PAUSED: SYNCMGRSTATUS = 6
SYNCMGRSTATUS_RESUMING: SYNCMGRSTATUS = 7
SYNCMGRSTATUS_UPDATING_INDETERMINATE: SYNCMGRSTATUS = 8
SYNCMGRSTATUS_DELETED: SYNCMGRSTATUS = 256
SYNCMGR_CANCEL_REQUEST = Int32
SYNCMGR_CR_NONE: SYNCMGR_CANCEL_REQUEST = 0
SYNCMGR_CR_CANCEL_ITEM: SYNCMGR_CANCEL_REQUEST = 1
SYNCMGR_CR_CANCEL_ALL: SYNCMGR_CANCEL_REQUEST = 2
SYNCMGR_CR_MAX: SYNCMGR_CANCEL_REQUEST = 2
class SYNCMGR_CONFLICT_ID_INFO(Structure):
    pblobID: POINTER(Windows.Win32.System.Com.BYTE_BLOB_head)
    pblobExtra: POINTER(Windows.Win32.System.Com.BYTE_BLOB_head)
SYNCMGR_CONFLICT_ITEM_TYPE = Int32
SYNCMGR_CIT_UPDATED: SYNCMGR_CONFLICT_ITEM_TYPE = 1
SYNCMGR_CIT_DELETED: SYNCMGR_CONFLICT_ITEM_TYPE = 2
SYNCMGR_CONTROL_FLAGS = Int32
SYNCMGR_CF_NONE: SYNCMGR_CONTROL_FLAGS = 0
SYNCMGR_CF_NOWAIT: SYNCMGR_CONTROL_FLAGS = 0
SYNCMGR_CF_WAIT: SYNCMGR_CONTROL_FLAGS = 1
SYNCMGR_CF_NOUI: SYNCMGR_CONTROL_FLAGS = 2
SYNCMGR_CF_VALID: SYNCMGR_CONTROL_FLAGS = 3
SYNCMGR_EVENT_FLAGS = Int32
SYNCMGR_EF_NONE: SYNCMGR_EVENT_FLAGS = 0
SYNCMGR_EF_VALID: SYNCMGR_EVENT_FLAGS = 0
SYNCMGR_EVENT_LEVEL = Int32
SYNCMGR_EL_INFORMATION: SYNCMGR_EVENT_LEVEL = 1
SYNCMGR_EL_WARNING: SYNCMGR_EVENT_LEVEL = 2
SYNCMGR_EL_ERROR: SYNCMGR_EVENT_LEVEL = 3
SYNCMGR_EL_MAX: SYNCMGR_EVENT_LEVEL = 3
SYNCMGR_HANDLER_CAPABILITIES = Int32
SYNCMGR_HCM_NONE: SYNCMGR_HANDLER_CAPABILITIES = 0
SYNCMGR_HCM_PROVIDES_ICON: SYNCMGR_HANDLER_CAPABILITIES = 1
SYNCMGR_HCM_EVENT_STORE: SYNCMGR_HANDLER_CAPABILITIES = 2
SYNCMGR_HCM_CONFLICT_STORE: SYNCMGR_HANDLER_CAPABILITIES = 4
SYNCMGR_HCM_SUPPORTS_CONCURRENT_SESSIONS: SYNCMGR_HANDLER_CAPABILITIES = 16
SYNCMGR_HCM_CAN_BROWSE_CONTENT: SYNCMGR_HANDLER_CAPABILITIES = 65536
SYNCMGR_HCM_CAN_SHOW_SCHEDULE: SYNCMGR_HANDLER_CAPABILITIES = 131072
SYNCMGR_HCM_QUERY_BEFORE_ACTIVATE: SYNCMGR_HANDLER_CAPABILITIES = 1048576
SYNCMGR_HCM_QUERY_BEFORE_DEACTIVATE: SYNCMGR_HANDLER_CAPABILITIES = 2097152
SYNCMGR_HCM_QUERY_BEFORE_ENABLE: SYNCMGR_HANDLER_CAPABILITIES = 4194304
SYNCMGR_HCM_QUERY_BEFORE_DISABLE: SYNCMGR_HANDLER_CAPABILITIES = 8388608
SYNCMGR_HCM_VALID_MASK: SYNCMGR_HANDLER_CAPABILITIES = 15925271
SYNCMGR_HANDLER_POLICIES = Int32
SYNCMGR_HPM_NONE: SYNCMGR_HANDLER_POLICIES = 0
SYNCMGR_HPM_PREVENT_ACTIVATE: SYNCMGR_HANDLER_POLICIES = 1
SYNCMGR_HPM_PREVENT_DEACTIVATE: SYNCMGR_HANDLER_POLICIES = 2
SYNCMGR_HPM_PREVENT_ENABLE: SYNCMGR_HANDLER_POLICIES = 4
SYNCMGR_HPM_PREVENT_DISABLE: SYNCMGR_HANDLER_POLICIES = 8
SYNCMGR_HPM_PREVENT_START_SYNC: SYNCMGR_HANDLER_POLICIES = 16
SYNCMGR_HPM_PREVENT_STOP_SYNC: SYNCMGR_HANDLER_POLICIES = 32
SYNCMGR_HPM_DISABLE_ENABLE: SYNCMGR_HANDLER_POLICIES = 256
SYNCMGR_HPM_DISABLE_DISABLE: SYNCMGR_HANDLER_POLICIES = 512
SYNCMGR_HPM_DISABLE_START_SYNC: SYNCMGR_HANDLER_POLICIES = 1024
SYNCMGR_HPM_DISABLE_STOP_SYNC: SYNCMGR_HANDLER_POLICIES = 2048
SYNCMGR_HPM_DISABLE_BROWSE: SYNCMGR_HANDLER_POLICIES = 4096
SYNCMGR_HPM_DISABLE_SCHEDULE: SYNCMGR_HANDLER_POLICIES = 8192
SYNCMGR_HPM_HIDDEN_BY_DEFAULT: SYNCMGR_HANDLER_POLICIES = 65536
SYNCMGR_HPM_BACKGROUND_SYNC_ONLY: SYNCMGR_HANDLER_POLICIES = 48
SYNCMGR_HPM_VALID_MASK: SYNCMGR_HANDLER_POLICIES = 77631
SYNCMGR_HANDLER_TYPE = Int32
SYNCMGR_HT_UNSPECIFIED: SYNCMGR_HANDLER_TYPE = 0
SYNCMGR_HT_APPLICATION: SYNCMGR_HANDLER_TYPE = 1
SYNCMGR_HT_DEVICE: SYNCMGR_HANDLER_TYPE = 2
SYNCMGR_HT_FOLDER: SYNCMGR_HANDLER_TYPE = 3
SYNCMGR_HT_SERVICE: SYNCMGR_HANDLER_TYPE = 4
SYNCMGR_HT_COMPUTER: SYNCMGR_HANDLER_TYPE = 5
SYNCMGR_HT_MIN: SYNCMGR_HANDLER_TYPE = 0
SYNCMGR_HT_MAX: SYNCMGR_HANDLER_TYPE = 5
SYNCMGR_ITEM_CAPABILITIES = Int32
SYNCMGR_ICM_NONE: SYNCMGR_ITEM_CAPABILITIES = 0
SYNCMGR_ICM_PROVIDES_ICON: SYNCMGR_ITEM_CAPABILITIES = 1
SYNCMGR_ICM_EVENT_STORE: SYNCMGR_ITEM_CAPABILITIES = 2
SYNCMGR_ICM_CONFLICT_STORE: SYNCMGR_ITEM_CAPABILITIES = 4
SYNCMGR_ICM_CAN_DELETE: SYNCMGR_ITEM_CAPABILITIES = 16
SYNCMGR_ICM_CAN_BROWSE_CONTENT: SYNCMGR_ITEM_CAPABILITIES = 65536
SYNCMGR_ICM_QUERY_BEFORE_ENABLE: SYNCMGR_ITEM_CAPABILITIES = 1048576
SYNCMGR_ICM_QUERY_BEFORE_DISABLE: SYNCMGR_ITEM_CAPABILITIES = 2097152
SYNCMGR_ICM_QUERY_BEFORE_DELETE: SYNCMGR_ITEM_CAPABILITIES = 4194304
SYNCMGR_ICM_VALID_MASK: SYNCMGR_ITEM_CAPABILITIES = 7405591
SYNCMGR_ITEM_POLICIES = Int32
SYNCMGR_IPM_NONE: SYNCMGR_ITEM_POLICIES = 0
SYNCMGR_IPM_PREVENT_ENABLE: SYNCMGR_ITEM_POLICIES = 1
SYNCMGR_IPM_PREVENT_DISABLE: SYNCMGR_ITEM_POLICIES = 2
SYNCMGR_IPM_PREVENT_START_SYNC: SYNCMGR_ITEM_POLICIES = 4
SYNCMGR_IPM_PREVENT_STOP_SYNC: SYNCMGR_ITEM_POLICIES = 8
SYNCMGR_IPM_DISABLE_ENABLE: SYNCMGR_ITEM_POLICIES = 16
SYNCMGR_IPM_DISABLE_DISABLE: SYNCMGR_ITEM_POLICIES = 32
SYNCMGR_IPM_DISABLE_START_SYNC: SYNCMGR_ITEM_POLICIES = 64
SYNCMGR_IPM_DISABLE_STOP_SYNC: SYNCMGR_ITEM_POLICIES = 128
SYNCMGR_IPM_DISABLE_BROWSE: SYNCMGR_ITEM_POLICIES = 256
SYNCMGR_IPM_DISABLE_DELETE: SYNCMGR_ITEM_POLICIES = 512
SYNCMGR_IPM_HIDDEN_BY_DEFAULT: SYNCMGR_ITEM_POLICIES = 65536
SYNCMGR_IPM_VALID_MASK: SYNCMGR_ITEM_POLICIES = 66303
SYNCMGR_PRESENTER_CHOICE = Int32
SYNCMGR_PC_NO_CHOICE: SYNCMGR_PRESENTER_CHOICE = 0
SYNCMGR_PC_KEEP_ONE: SYNCMGR_PRESENTER_CHOICE = 1
SYNCMGR_PC_KEEP_MULTIPLE: SYNCMGR_PRESENTER_CHOICE = 2
SYNCMGR_PC_KEEP_RECENT: SYNCMGR_PRESENTER_CHOICE = 3
SYNCMGR_PC_REMOVE_FROM_SYNC_SET: SYNCMGR_PRESENTER_CHOICE = 4
SYNCMGR_PC_SKIP: SYNCMGR_PRESENTER_CHOICE = 5
SYNCMGR_PRESENTER_NEXT_STEP = Int32
SYNCMGR_PNS_CONTINUE: SYNCMGR_PRESENTER_NEXT_STEP = 0
SYNCMGR_PNS_DEFAULT: SYNCMGR_PRESENTER_NEXT_STEP = 1
SYNCMGR_PNS_CANCEL: SYNCMGR_PRESENTER_NEXT_STEP = 2
SYNCMGR_PROGRESS_STATUS = Int32
SYNCMGR_PS_UPDATING: SYNCMGR_PROGRESS_STATUS = 1
SYNCMGR_PS_UPDATING_INDETERMINATE: SYNCMGR_PROGRESS_STATUS = 2
SYNCMGR_PS_SUCCEEDED: SYNCMGR_PROGRESS_STATUS = 3
SYNCMGR_PS_FAILED: SYNCMGR_PROGRESS_STATUS = 4
SYNCMGR_PS_CANCELED: SYNCMGR_PROGRESS_STATUS = 5
SYNCMGR_PS_DISCONNECTED: SYNCMGR_PROGRESS_STATUS = 6
SYNCMGR_PS_MAX: SYNCMGR_PROGRESS_STATUS = 6
SYNCMGR_RESOLUTION_ABILITIES = Int32
SYNCMGR_RA_KEEPOTHER: SYNCMGR_RESOLUTION_ABILITIES = 1
SYNCMGR_RA_KEEPRECENT: SYNCMGR_RESOLUTION_ABILITIES = 2
SYNCMGR_RA_REMOVEFROMSYNCSET: SYNCMGR_RESOLUTION_ABILITIES = 4
SYNCMGR_RA_KEEP_SINGLE: SYNCMGR_RESOLUTION_ABILITIES = 8
SYNCMGR_RA_KEEP_MULTIPLE: SYNCMGR_RESOLUTION_ABILITIES = 16
SYNCMGR_RA_VALID: SYNCMGR_RESOLUTION_ABILITIES = 31
SYNCMGR_RESOLUTION_FEEDBACK = Int32
SYNCMGR_RF_CONTINUE: SYNCMGR_RESOLUTION_FEEDBACK = 0
SYNCMGR_RF_REFRESH: SYNCMGR_RESOLUTION_FEEDBACK = 1
SYNCMGR_RF_CANCEL: SYNCMGR_RESOLUTION_FEEDBACK = 2
SYNCMGR_SYNC_CONTROL_FLAGS = Int32
SYNCMGR_SCF_NONE: SYNCMGR_SYNC_CONTROL_FLAGS = 0
SYNCMGR_SCF_IGNORE_IF_ALREADY_SYNCING: SYNCMGR_SYNC_CONTROL_FLAGS = 1
SYNCMGR_SCF_VALID: SYNCMGR_SYNC_CONTROL_FLAGS = 1
SYNCMGR_UPDATE_REASON = Int32
SYNCMGR_UR_ADDED: SYNCMGR_UPDATE_REASON = 0
SYNCMGR_UR_CHANGED: SYNCMGR_UPDATE_REASON = 1
SYNCMGR_UR_REMOVED: SYNCMGR_UPDATE_REASON = 2
SYNCMGR_UR_MAX: SYNCMGR_UPDATE_REASON = 2
ScheduledTasks = Guid('d6277990-4c6a-11cf-8d-87-00-aa-00-60-f5-bf')
SearchFolderItemFactory = Guid('14010e02-bbbd-41f0-88-e3-ed-a3-71-21-65-84')
SecureLockIconConstants = Int32
SecureLockIconConstants_secureLockIconUnsecure: SecureLockIconConstants = 0
SecureLockIconConstants_secureLockIconMixed: SecureLockIconConstants = 1
SecureLockIconConstants_secureLockIconSecureUnknownBits: SecureLockIconConstants = 2
SecureLockIconConstants_secureLockIconSecure40Bit: SecureLockIconConstants = 3
SecureLockIconConstants_secureLockIconSecure56Bit: SecureLockIconConstants = 4
SecureLockIconConstants_secureLockIconSecureFortezza: SecureLockIconConstants = 5
SecureLockIconConstants_secureLockIconSecure128Bit: SecureLockIconConstants = 6
ShFindChangeNotificationHandle = IntPtr
SharedBitmap = Guid('4db26476-6787-4046-b8-36-e8-41-2a-9e-8a-27')
SharingConfigurationManager = Guid('49f371e1-8c5c-4d9c-9a-3b-54-a6-82-7f-51-3c')
Shell = Guid('13709620-c279-11ce-a4-9e-44-45-53-54-00-00')
ShellBrowserWindow = Guid('c08afd90-f2a1-11d1-84-55-00-a0-c9-1f-38-80')
ShellDesktop = Guid('00021400-0000-0000-c0-00-00-00-00-00-00-46')
ShellDispatchInproc = Guid('0a89a860-d7b1-11ce-83-50-44-45-53-54-00-00')
ShellFSFolder = Guid('f3364ba0-65b9-11ce-a9-ba-00-aa-00-4a-e8-37')
ShellFolderItem = Guid('2fe352ea-fd1f-11d2-b1-f4-00-c0-4f-8e-eb-3e')
ShellFolderView = Guid('62112aa1-ebe4-11cf-a5-fb-00-20-af-e7-29-2d')
ShellFolderViewOC = Guid('9ba05971-f6a8-11cf-a4-42-00-a0-c9-0a-8f-39')
ShellFolderViewOptions = Int32
SFVVO_SHOWALLOBJECTS: ShellFolderViewOptions = 1
SFVVO_SHOWEXTENSIONS: ShellFolderViewOptions = 2
SFVVO_SHOWCOMPCOLOR: ShellFolderViewOptions = 8
SFVVO_SHOWSYSFILES: ShellFolderViewOptions = 32
SFVVO_WIN95CLASSIC: ShellFolderViewOptions = 64
SFVVO_DOUBLECLICKINWEBVIEW: ShellFolderViewOptions = 128
SFVVO_DESKTOPHTML: ShellFolderViewOptions = 512
ShellImageDataFactory = Guid('66e4e4fb-f385-4dd0-8d-74-a2-ef-d1-bc-61-78')
ShellItem = Guid('9ac9fbe1-e0a2-4ad6-b4-ee-e2-12-01-3e-a9-17')
ShellLibrary = Guid('d9b3211d-e57f-4426-aa-ef-30-a8-06-ad-d3-97')
ShellLink = Guid('00021401-0000-0000-c0-00-00-00-00-00-00-46')
ShellLinkObject = Guid('11219420-1768-11d1-95-be-00-60-97-97-ea-4f')
ShellNameSpace = Guid('55136805-b2de-11d1-b9-f2-00-a0-c9-8b-c5-47')
ShellSpecialFolderConstants = Int32
ShellSpecialFolderConstants_ssfDESKTOP: ShellSpecialFolderConstants = 0
ShellSpecialFolderConstants_ssfPROGRAMS: ShellSpecialFolderConstants = 2
ShellSpecialFolderConstants_ssfCONTROLS: ShellSpecialFolderConstants = 3
ShellSpecialFolderConstants_ssfPRINTERS: ShellSpecialFolderConstants = 4
ShellSpecialFolderConstants_ssfPERSONAL: ShellSpecialFolderConstants = 5
ShellSpecialFolderConstants_ssfFAVORITES: ShellSpecialFolderConstants = 6
ShellSpecialFolderConstants_ssfSTARTUP: ShellSpecialFolderConstants = 7
ShellSpecialFolderConstants_ssfRECENT: ShellSpecialFolderConstants = 8
ShellSpecialFolderConstants_ssfSENDTO: ShellSpecialFolderConstants = 9
ShellSpecialFolderConstants_ssfBITBUCKET: ShellSpecialFolderConstants = 10
ShellSpecialFolderConstants_ssfSTARTMENU: ShellSpecialFolderConstants = 11
ShellSpecialFolderConstants_ssfDESKTOPDIRECTORY: ShellSpecialFolderConstants = 16
ShellSpecialFolderConstants_ssfDRIVES: ShellSpecialFolderConstants = 17
ShellSpecialFolderConstants_ssfNETWORK: ShellSpecialFolderConstants = 18
ShellSpecialFolderConstants_ssfNETHOOD: ShellSpecialFolderConstants = 19
ShellSpecialFolderConstants_ssfFONTS: ShellSpecialFolderConstants = 20
ShellSpecialFolderConstants_ssfTEMPLATES: ShellSpecialFolderConstants = 21
ShellSpecialFolderConstants_ssfCOMMONSTARTMENU: ShellSpecialFolderConstants = 22
ShellSpecialFolderConstants_ssfCOMMONPROGRAMS: ShellSpecialFolderConstants = 23
ShellSpecialFolderConstants_ssfCOMMONSTARTUP: ShellSpecialFolderConstants = 24
ShellSpecialFolderConstants_ssfCOMMONDESKTOPDIR: ShellSpecialFolderConstants = 25
ShellSpecialFolderConstants_ssfAPPDATA: ShellSpecialFolderConstants = 26
ShellSpecialFolderConstants_ssfPRINTHOOD: ShellSpecialFolderConstants = 27
ShellSpecialFolderConstants_ssfLOCALAPPDATA: ShellSpecialFolderConstants = 28
ShellSpecialFolderConstants_ssfALTSTARTUP: ShellSpecialFolderConstants = 29
ShellSpecialFolderConstants_ssfCOMMONALTSTARTUP: ShellSpecialFolderConstants = 30
ShellSpecialFolderConstants_ssfCOMMONFAVORITES: ShellSpecialFolderConstants = 31
ShellSpecialFolderConstants_ssfINTERNETCACHE: ShellSpecialFolderConstants = 32
ShellSpecialFolderConstants_ssfCOOKIES: ShellSpecialFolderConstants = 33
ShellSpecialFolderConstants_ssfHISTORY: ShellSpecialFolderConstants = 34
ShellSpecialFolderConstants_ssfCOMMONAPPDATA: ShellSpecialFolderConstants = 35
ShellSpecialFolderConstants_ssfWINDOWS: ShellSpecialFolderConstants = 36
ShellSpecialFolderConstants_ssfSYSTEM: ShellSpecialFolderConstants = 37
ShellSpecialFolderConstants_ssfPROGRAMFILES: ShellSpecialFolderConstants = 38
ShellSpecialFolderConstants_ssfMYPICTURES: ShellSpecialFolderConstants = 39
ShellSpecialFolderConstants_ssfPROFILE: ShellSpecialFolderConstants = 40
ShellSpecialFolderConstants_ssfSYSTEMx86: ShellSpecialFolderConstants = 41
ShellSpecialFolderConstants_ssfPROGRAMFILESx86: ShellSpecialFolderConstants = 48
ShellUIHelper = Guid('64ab4bb7-111e-11d1-8f-79-00-c0-4f-c2-fb-e1')
ShellWindowFindWindowOptions = Int32
SWFO_NEEDDISPATCH: ShellWindowFindWindowOptions = 1
SWFO_INCLUDEPENDING: ShellWindowFindWindowOptions = 2
SWFO_COOKIEPASSED: ShellWindowFindWindowOptions = 4
ShellWindowTypeConstants = Int32
SWC_EXPLORER: ShellWindowTypeConstants = 0
SWC_BROWSER: ShellWindowTypeConstants = 1
SWC_3RDPARTY: ShellWindowTypeConstants = 2
SWC_CALLBACK: ShellWindowTypeConstants = 4
SWC_DESKTOP: ShellWindowTypeConstants = 8
ShellWindows = Guid('9ba05972-f6a8-11cf-a4-42-00-a0-c9-0a-8f-39')
ShowInputPaneAnimationCoordinator = Guid('1f046abf-3202-4dc1-8c-b5-3c-67-61-7c-e1-fa')
SimpleConflictPresenter = Guid('7a0f6ab7-ed84-46b6-b4-7e-02-aa-15-9a-15-2b')
SizeCategorizer = Guid('55d7b852-f6d1-42f2-aa-75-87-28-a1-b2-d2-64')
SmartcardCredentialProvider = Guid('8fd7e19c-3bf7-489b-a7-2c-84-6a-b3-67-8c-96')
SmartcardPinProvider = Guid('94596c7e-3744-41ce-89-3e-bb-f0-91-22-f7-6a')
SmartcardReaderSelectionProvider = Guid('1b283861-754f-4022-ad-47-a5-ea-aa-61-88-94')
SmartcardWinRTProvider = Guid('1ee7337f-85ac-45e2-a2-3c-37-c7-53-20-97-69')
StartMenuPin = Guid('a2a9545d-a0c2-42b4-97-08-a0-b2-ba-dd-77-c8')
StorageProviderBanners = Guid('7ccdf9f4-e576-455a-8b-c7-f6-ec-68-d6-f0-63')
SuspensionDependencyManager = Guid('6b273fc5-61fd-4918-95-a2-c3-b5-e9-d7-f5-81')
SyncMgr = Guid('6295df27-35ee-11d1-87-07-00-c0-4f-d9-33-27')
SyncMgrClient = Guid('1202db60-1dac-42c5-ae-d5-1a-bd-d4-32-24-8e')
SyncMgrControl = Guid('1a1f4206-0688-4e7f-be-03-d8-2e-c6-9d-f9-a5')
SyncMgrFolder = Guid('9c73f5e5-7ae7-4e32-a8-e8-8d-23-b8-52-55-bf')
SyncMgrScheduleWizard = Guid('8d8b8e30-c451-421b-85-53-d2-97-6a-fa-64-8c')
SyncResultsFolder = Guid('71d99464-3b6b-475c-b2-41-e1-58-83-20-75-29')
SyncSetupFolder = Guid('2e9e59c0-b437-4981-a6-47-9c-34-b9-b9-08-91')
class TBINFO(Structure):
    cbuttons: UInt32
    uFlags: UInt32
TBPFLAG = Int32
TBPF_NOPROGRESS: TBPFLAG = 0
TBPF_INDETERMINATE: TBPFLAG = 1
TBPF_NORMAL: TBPFLAG = 2
TBPF_ERROR: TBPFLAG = 4
TBPF_PAUSED: TBPFLAG = 8
class THUMBBUTTON(Structure):
    dwMask: Windows.Win32.UI.Shell.THUMBBUTTONMASK
    iId: UInt32
    iBitmap: UInt32
    hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
    szTip: Char * 260
    dwFlags: Windows.Win32.UI.Shell.THUMBBUTTONFLAGS
THUMBBUTTONFLAGS = Int32
THBF_ENABLED: THUMBBUTTONFLAGS = 0
THBF_DISABLED: THUMBBUTTONFLAGS = 1
THBF_DISMISSONCLICK: THUMBBUTTONFLAGS = 2
THBF_NOBACKGROUND: THUMBBUTTONFLAGS = 4
THBF_HIDDEN: THUMBBUTTONFLAGS = 8
THBF_NONINTERACTIVE: THUMBBUTTONFLAGS = 16
THUMBBUTTONMASK = Int32
THB_BITMAP: THUMBBUTTONMASK = 1
THB_ICON: THUMBBUTTONMASK = 2
THB_TOOLTIP: THUMBBUTTONMASK = 4
THB_FLAGS: THUMBBUTTONMASK = 8
TI_FLAGS = Int32
TI_BITMAP: TI_FLAGS = 1
TI_JPEG: TI_FLAGS = 2
TLENUMF = Int32
TLEF_RELATIVE_INCLUDE_CURRENT: TLENUMF = 1
TLEF_RELATIVE_BACK: TLENUMF = 16
TLEF_RELATIVE_FORE: TLENUMF = 32
TLEF_INCLUDE_UNINVOKEABLE: TLENUMF = 64
TLEF_ABSOLUTE: TLENUMF = 49
TLEF_EXCLUDE_SUBFRAME_ENTRIES: TLENUMF = 128
TLEF_EXCLUDE_ABOUT_PAGES: TLENUMF = 256
class TOOLBARITEM(Structure):
    ptbar: Windows.Win32.UI.Shell.IDockingWindow_head
    rcBorderTool: Windows.Win32.Foundation.RECT
    pwszItem: Windows.Win32.Foundation.PWSTR
    fShow: Windows.Win32.Foundation.BOOL
    hMon: Windows.Win32.Graphics.Gdi.HMONITOR
TRANSLATEURL_IN_FLAGS = Int32
TRANSLATEURL_FL_GUESS_PROTOCOL: TRANSLATEURL_IN_FLAGS = 1
TRANSLATEURL_FL_USE_DEFAULT_PROTOCOL: TRANSLATEURL_IN_FLAGS = 2
TaskbarList = Guid('56fdf344-fd6d-11d0-95-8a-00-60-97-c9-a0-90')
ThumbnailStreamCache = Guid('cbe0fed3-4b91-4e90-83-54-8a-8c-84-ec-68-72')
ThumbnailStreamCacheOptions = Int32
ThumbnailStreamCacheOptions_ExtractIfNotCached: ThumbnailStreamCacheOptions = 0
ThumbnailStreamCacheOptions_ReturnOnlyIfCached: ThumbnailStreamCacheOptions = 1
ThumbnailStreamCacheOptions_ResizeThumbnail: ThumbnailStreamCacheOptions = 2
ThumbnailStreamCacheOptions_AllowSmallerSize: ThumbnailStreamCacheOptions = 4
TimeCategorizer = Guid('3bb4118f-ddfd-4d30-a3-48-9f-b5-d6-bf-1a-fe')
TrackShellMenu = Guid('8278f931-2a3e-11d2-83-8f-00-c0-4f-d9-18-d0')
TrayBandSiteService = Guid('f60ad0a0-e5e1-45cb-b5-1a-e1-5b-9f-8b-29-34')
TrayDeskBand = Guid('e6442437-6c68-4f52-94-dd-2c-fe-d2-67-ef-b9')
UNDOCK_REASON = Int32
UR_RESOLUTION_CHANGE: UNDOCK_REASON = 0
UR_MONITOR_DISCONNECT: UNDOCK_REASON = 1
URLASSOCIATIONDIALOG_IN_FLAGS = Int32
URLASSOCDLG_FL_USE_DEFAULT_NAME: URLASSOCIATIONDIALOG_IN_FLAGS = 1
URLASSOCDLG_FL_REGISTER_ASSOC: URLASSOCIATIONDIALOG_IN_FLAGS = 2
class URLINVOKECOMMANDINFOA(Structure):
    dwcbSize: UInt32
    dwFlags: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    pcszVerb: Windows.Win32.Foundation.PSTR
class URLINVOKECOMMANDINFOW(Structure):
    dwcbSize: UInt32
    dwFlags: UInt32
    hwndParent: Windows.Win32.Foundation.HWND
    pcszVerb: Windows.Win32.Foundation.PWSTR
URLIS = Int32
URLIS_URL: URLIS = 0
URLIS_OPAQUE: URLIS = 1
URLIS_NOHISTORY: URLIS = 2
URLIS_FILEURL: URLIS = 3
URLIS_APPLIABLE: URLIS = 4
URLIS_DIRECTORY: URLIS = 5
URLIS_HASQUERY: URLIS = 6
URL_PART = Int32
URL_PART_NONE: URL_PART = 0
URL_PART_SCHEME: URL_PART = 1
URL_PART_HOSTNAME: URL_PART = 2
URL_PART_USERNAME: URL_PART = 3
URL_PART_PASSWORD: URL_PART = 4
URL_PART_PORT: URL_PART = 5
URL_PART_QUERY: URL_PART = 6
URL_SCHEME = Int32
URL_SCHEME_INVALID: URL_SCHEME = -1
URL_SCHEME_UNKNOWN: URL_SCHEME = 0
URL_SCHEME_FTP: URL_SCHEME = 1
URL_SCHEME_HTTP: URL_SCHEME = 2
URL_SCHEME_GOPHER: URL_SCHEME = 3
URL_SCHEME_MAILTO: URL_SCHEME = 4
URL_SCHEME_NEWS: URL_SCHEME = 5
URL_SCHEME_NNTP: URL_SCHEME = 6
URL_SCHEME_TELNET: URL_SCHEME = 7
URL_SCHEME_WAIS: URL_SCHEME = 8
URL_SCHEME_FILE: URL_SCHEME = 9
URL_SCHEME_MK: URL_SCHEME = 10
URL_SCHEME_HTTPS: URL_SCHEME = 11
URL_SCHEME_SHELL: URL_SCHEME = 12
URL_SCHEME_SNEWS: URL_SCHEME = 13
URL_SCHEME_LOCAL: URL_SCHEME = 14
URL_SCHEME_JAVASCRIPT: URL_SCHEME = 15
URL_SCHEME_VBSCRIPT: URL_SCHEME = 16
URL_SCHEME_ABOUT: URL_SCHEME = 17
URL_SCHEME_RES: URL_SCHEME = 18
URL_SCHEME_MSSHELLROOTED: URL_SCHEME = 19
URL_SCHEME_MSSHELLIDLIST: URL_SCHEME = 20
URL_SCHEME_MSHELP: URL_SCHEME = 21
URL_SCHEME_MSSHELLDEVICE: URL_SCHEME = 22
URL_SCHEME_WILDCARD: URL_SCHEME = 23
URL_SCHEME_SEARCH_MS: URL_SCHEME = 24
URL_SCHEME_SEARCH: URL_SCHEME = 25
URL_SCHEME_KNOWNFOLDER: URL_SCHEME = 26
URL_SCHEME_MAXVALUE: URL_SCHEME = 27
UserNotification = Guid('0010890e-8789-413c-ad-bc-48-f5-b5-11-b3-af')
V1PasswordCredentialProvider = Guid('6f45dc1e-5384-457a-bc-13-2c-d8-1b-0d-28-ed')
V1SmartcardCredentialProvider = Guid('8bf9a910-a8ff-457f-99-9f-a5-ca-10-b4-a8-85')
V1WinBioCredentialProvider = Guid('ac3ac249-e820-4343-a6-5b-37-7a-c6-34-dc-09')
VALIDATEUNC_OPTION = Int32
VALIDATEUNC_CONNECT: VALIDATEUNC_OPTION = 1
VALIDATEUNC_NOUI: VALIDATEUNC_OPTION = 2
VALIDATEUNC_PRINT: VALIDATEUNC_OPTION = 4
VALIDATEUNC_PERSIST: VALIDATEUNC_OPTION = 8
VALIDATEUNC_VALID: VALIDATEUNC_OPTION = 15
VPCOLORFLAGS = Int32
VPCF_TEXT: VPCOLORFLAGS = 1
VPCF_BACKGROUND: VPCOLORFLAGS = 2
VPCF_SORTCOLUMN: VPCOLORFLAGS = 3
VPCF_SUBTEXT: VPCOLORFLAGS = 4
VPCF_TEXTBACKGROUND: VPCOLORFLAGS = 5
VPWATERMARKFLAGS = Int32
VPWF_DEFAULT: VPWATERMARKFLAGS = 0
VPWF_ALPHABLEND: VPWATERMARKFLAGS = 1
VaultProvider = Guid('503739d0-4c5e-4cfd-b3-ba-d8-81-33-4f-0d-f2')
VirtualDesktopManager = Guid('aa509086-5ca9-4c25-8f-95-58-9d-3c-07-b4-8a')
class WINDOWDATA(Structure):
    dwWindowID: UInt32
    uiCP: UInt32
    pidl: POINTER(Windows.Win32.UI.Shell.Common.ITEMIDLIST_head)
    lpszUrl: Windows.Win32.Foundation.PWSTR
    lpszUrlLocation: Windows.Win32.Foundation.PWSTR
    lpszTitle: Windows.Win32.Foundation.PWSTR
WTS_ALPHATYPE = Int32
WTSAT_UNKNOWN: WTS_ALPHATYPE = 0
WTSAT_RGB: WTS_ALPHATYPE = 1
WTSAT_ARGB: WTS_ALPHATYPE = 2
WTS_CACHEFLAGS = Int32
WTS_DEFAULT: WTS_CACHEFLAGS = 0
WTS_LOWQUALITY: WTS_CACHEFLAGS = 1
WTS_CACHED: WTS_CACHEFLAGS = 2
WTS_CONTEXTFLAGS = Int32
WTSCF_DEFAULT: WTS_CONTEXTFLAGS = 0
WTSCF_APPSTYLE: WTS_CONTEXTFLAGS = 1
WTSCF_SQUARE: WTS_CONTEXTFLAGS = 2
WTSCF_WIDE: WTS_CONTEXTFLAGS = 4
WTSCF_FAST: WTS_CONTEXTFLAGS = 8
WTS_FLAGS = Int32
WTS_NONE: WTS_FLAGS = 0
WTS_EXTRACT: WTS_FLAGS = 0
WTS_INCACHEONLY: WTS_FLAGS = 1
WTS_FASTEXTRACT: WTS_FLAGS = 2
WTS_FORCEEXTRACTION: WTS_FLAGS = 4
WTS_SLOWRECLAIM: WTS_FLAGS = 8
WTS_EXTRACTDONOTCACHE: WTS_FLAGS = 32
WTS_SCALETOREQUESTEDSIZE: WTS_FLAGS = 64
WTS_SKIPFASTEXTRACT: WTS_FLAGS = 128
WTS_EXTRACTINPROC: WTS_FLAGS = 256
WTS_CROPTOSQUARE: WTS_FLAGS = 512
WTS_INSTANCESURROGATE: WTS_FLAGS = 1024
WTS_REQUIRESURROGATE: WTS_FLAGS = 2048
WTS_APPSTYLE: WTS_FLAGS = 8192
WTS_WIDETHUMBNAILS: WTS_FLAGS = 16384
WTS_IDEALCACHESIZEONLY: WTS_FLAGS = 32768
WTS_SCALEUP: WTS_FLAGS = 65536
class WTS_THUMBNAILID(Structure):
    rgbKey: Byte * 16
WebBrowser = Guid('8856f961-340a-11d0-a9-6b-00-c0-4f-d7-05-a2')
WebBrowser_V1 = Guid('eab22ac3-30c1-11cf-a7-eb-00-00-c0-5b-ae-0b')
WebWizardHost = Guid('c827f149-55c1-4d28-93-5e-57-e4-7c-ae-d9-73')
WinBioCredentialProvider = Guid('bec09223-b018-416d-a0-ac-52-39-71-b6-39-f5')
class _APPCONSTRAIN_REGISTRATION(Structure):
    pass
class _APPSTATE_REGISTRATION(Structure):
    pass
_BROWSERFRAMEOPTIONS = Int32
BFO_NONE: _BROWSERFRAMEOPTIONS = 0
BFO_BROWSER_PERSIST_SETTINGS: _BROWSERFRAMEOPTIONS = 1
BFO_RENAME_FOLDER_OPTIONS_TOINTERNET: _BROWSERFRAMEOPTIONS = 2
BFO_BOTH_OPTIONS: _BROWSERFRAMEOPTIONS = 4
BIF_PREFER_INTERNET_SHORTCUT: _BROWSERFRAMEOPTIONS = 8
BFO_BROWSE_NO_IN_NEW_PROCESS: _BROWSERFRAMEOPTIONS = 16
BFO_ENABLE_HYPERLINK_TRACKING: _BROWSERFRAMEOPTIONS = 32
BFO_USE_IE_OFFLINE_SUPPORT: _BROWSERFRAMEOPTIONS = 64
BFO_SUBSTITUE_INTERNET_START_PAGE: _BROWSERFRAMEOPTIONS = 128
BFO_USE_IE_LOGOBANDING: _BROWSERFRAMEOPTIONS = 256
BFO_ADD_IE_TOCAPTIONBAR: _BROWSERFRAMEOPTIONS = 512
BFO_USE_DIALUP_REF: _BROWSERFRAMEOPTIONS = 1024
BFO_USE_IE_TOOLBAR: _BROWSERFRAMEOPTIONS = 2048
BFO_NO_PARENT_FOLDER_SUPPORT: _BROWSERFRAMEOPTIONS = 4096
BFO_NO_REOPEN_NEXT_RESTART: _BROWSERFRAMEOPTIONS = 8192
BFO_GO_HOME_PAGE: _BROWSERFRAMEOPTIONS = 16384
BFO_PREFER_IEPROCESS: _BROWSERFRAMEOPTIONS = 32768
BFO_SHOW_NAVIGATION_CANCELLED: _BROWSERFRAMEOPTIONS = 65536
BFO_USE_IE_STATUSBAR: _BROWSERFRAMEOPTIONS = 131072
BFO_QUERY_ALL: _BROWSERFRAMEOPTIONS = -1
_CDBE_ACTIONS = Int32
CDBE_TYPE_MUSIC: _CDBE_ACTIONS = 1
CDBE_TYPE_DATA: _CDBE_ACTIONS = 2
CDBE_TYPE_ALL: _CDBE_ACTIONS = -1
_EXPCMDFLAGS = Int32
ECF_DEFAULT: _EXPCMDFLAGS = 0
ECF_HASSUBCOMMANDS: _EXPCMDFLAGS = 1
ECF_HASSPLITBUTTON: _EXPCMDFLAGS = 2
ECF_HIDELABEL: _EXPCMDFLAGS = 4
ECF_ISSEPARATOR: _EXPCMDFLAGS = 8
ECF_HASLUASHIELD: _EXPCMDFLAGS = 16
ECF_SEPARATORBEFORE: _EXPCMDFLAGS = 32
ECF_SEPARATORAFTER: _EXPCMDFLAGS = 64
ECF_ISDROPDOWN: _EXPCMDFLAGS = 128
ECF_TOGGLEABLE: _EXPCMDFLAGS = 256
ECF_AUTOMENUICONS: _EXPCMDFLAGS = 512
_EXPCMDSTATE = Int32
ECS_ENABLED: _EXPCMDSTATE = 0
ECS_DISABLED: _EXPCMDSTATE = 1
ECS_HIDDEN: _EXPCMDSTATE = 2
ECS_CHECKBOX: _EXPCMDSTATE = 4
ECS_CHECKED: _EXPCMDSTATE = 8
ECS_RADIOCHECK: _EXPCMDSTATE = 16
_EXPLORERPANESTATE = Int32
EPS_DONTCARE: _EXPLORERPANESTATE = 0
EPS_DEFAULT_ON: _EXPLORERPANESTATE = 1
EPS_DEFAULT_OFF: _EXPLORERPANESTATE = 2
EPS_STATEMASK: _EXPLORERPANESTATE = 65535
EPS_INITIALSTATE: _EXPLORERPANESTATE = 65536
EPS_FORCE: _EXPLORERPANESTATE = 131072
_EXPPS = Int32
EXPPS_FILETYPES: _EXPPS = 1
_KF_DEFINITION_FLAGS = Int32
KFDF_LOCAL_REDIRECT_ONLY: _KF_DEFINITION_FLAGS = 2
KFDF_ROAMABLE: _KF_DEFINITION_FLAGS = 4
KFDF_PRECREATE: _KF_DEFINITION_FLAGS = 8
KFDF_STREAM: _KF_DEFINITION_FLAGS = 16
KFDF_PUBLISHEXPANDEDPATH: _KF_DEFINITION_FLAGS = 32
KFDF_NO_REDIRECT_UI: _KF_DEFINITION_FLAGS = 64
_KF_REDIRECTION_CAPABILITIES = Int32
KF_REDIRECTION_CAPABILITIES_ALLOW_ALL: _KF_REDIRECTION_CAPABILITIES = 255
KF_REDIRECTION_CAPABILITIES_REDIRECTABLE: _KF_REDIRECTION_CAPABILITIES = 1
KF_REDIRECTION_CAPABILITIES_DENY_ALL: _KF_REDIRECTION_CAPABILITIES = 1048320
KF_REDIRECTION_CAPABILITIES_DENY_POLICY_REDIRECTED: _KF_REDIRECTION_CAPABILITIES = 256
KF_REDIRECTION_CAPABILITIES_DENY_POLICY: _KF_REDIRECTION_CAPABILITIES = 512
KF_REDIRECTION_CAPABILITIES_DENY_PERMISSIONS: _KF_REDIRECTION_CAPABILITIES = 1024
_KF_REDIRECT_FLAGS = Int32
KF_REDIRECT_USER_EXCLUSIVE: _KF_REDIRECT_FLAGS = 1
KF_REDIRECT_COPY_SOURCE_DACL: _KF_REDIRECT_FLAGS = 2
KF_REDIRECT_OWNER_USER: _KF_REDIRECT_FLAGS = 4
KF_REDIRECT_SET_OWNER_EXPLICIT: _KF_REDIRECT_FLAGS = 8
KF_REDIRECT_CHECK_ONLY: _KF_REDIRECT_FLAGS = 16
KF_REDIRECT_WITH_UI: _KF_REDIRECT_FLAGS = 32
KF_REDIRECT_UNPIN: _KF_REDIRECT_FLAGS = 64
KF_REDIRECT_PIN: _KF_REDIRECT_FLAGS = 128
KF_REDIRECT_COPY_CONTENTS: _KF_REDIRECT_FLAGS = 512
KF_REDIRECT_DEL_SOURCE_CONTENTS: _KF_REDIRECT_FLAGS = 1024
KF_REDIRECT_EXCLUDE_ALL_KNOWN_SUBFOLDERS: _KF_REDIRECT_FLAGS = 2048
_NMCII_FLAGS = Int32
NMCII_NONE: _NMCII_FLAGS = 0
NMCII_ITEMS: _NMCII_FLAGS = 1
NMCII_FOLDERS: _NMCII_FLAGS = 2
_NMCSAEI_FLAGS = Int32
NMCSAEI_SELECT: _NMCSAEI_FLAGS = 0
NMCSAEI_EDIT: _NMCSAEI_FLAGS = 1
_NSTCECLICKTYPE = Int32
NSTCECT_LBUTTON: _NSTCECLICKTYPE = 1
NSTCECT_MBUTTON: _NSTCECLICKTYPE = 2
NSTCECT_RBUTTON: _NSTCECLICKTYPE = 3
NSTCECT_BUTTON: _NSTCECLICKTYPE = 3
NSTCECT_DBLCLICK: _NSTCECLICKTYPE = 4
_NSTCEHITTEST = Int32
NSTCEHT_NOWHERE: _NSTCEHITTEST = 1
NSTCEHT_ONITEMICON: _NSTCEHITTEST = 2
NSTCEHT_ONITEMLABEL: _NSTCEHITTEST = 4
NSTCEHT_ONITEMINDENT: _NSTCEHITTEST = 8
NSTCEHT_ONITEMBUTTON: _NSTCEHITTEST = 16
NSTCEHT_ONITEMRIGHT: _NSTCEHITTEST = 32
NSTCEHT_ONITEMSTATEICON: _NSTCEHITTEST = 64
NSTCEHT_ONITEM: _NSTCEHITTEST = 70
NSTCEHT_ONITEMTABBUTTON: _NSTCEHITTEST = 4096
_NSTCITEMSTATE = Int32
NSTCIS_NONE: _NSTCITEMSTATE = 0
NSTCIS_SELECTED: _NSTCITEMSTATE = 1
NSTCIS_EXPANDED: _NSTCITEMSTATE = 2
NSTCIS_BOLD: _NSTCITEMSTATE = 4
NSTCIS_DISABLED: _NSTCITEMSTATE = 8
NSTCIS_SELECTEDNOEXPAND: _NSTCITEMSTATE = 16
_NSTCROOTSTYLE = Int32
NSTCRS_VISIBLE: _NSTCROOTSTYLE = 0
NSTCRS_HIDDEN: _NSTCROOTSTYLE = 1
NSTCRS_EXPANDED: _NSTCROOTSTYLE = 2
_NSTCSTYLE = Int32
NSTCS_HASEXPANDOS: _NSTCSTYLE = 1
NSTCS_HASLINES: _NSTCSTYLE = 2
NSTCS_SINGLECLICKEXPAND: _NSTCSTYLE = 4
NSTCS_FULLROWSELECT: _NSTCSTYLE = 8
NSTCS_SPRINGEXPAND: _NSTCSTYLE = 16
NSTCS_HORIZONTALSCROLL: _NSTCSTYLE = 32
NSTCS_ROOTHASEXPANDO: _NSTCSTYLE = 64
NSTCS_SHOWSELECTIONALWAYS: _NSTCSTYLE = 128
NSTCS_NOINFOTIP: _NSTCSTYLE = 512
NSTCS_EVENHEIGHT: _NSTCSTYLE = 1024
NSTCS_NOREPLACEOPEN: _NSTCSTYLE = 2048
NSTCS_DISABLEDRAGDROP: _NSTCSTYLE = 4096
NSTCS_NOORDERSTREAM: _NSTCSTYLE = 8192
NSTCS_RICHTOOLTIP: _NSTCSTYLE = 16384
NSTCS_BORDER: _NSTCSTYLE = 32768
NSTCS_NOEDITLABELS: _NSTCSTYLE = 65536
NSTCS_TABSTOP: _NSTCSTYLE = 131072
NSTCS_FAVORITESMODE: _NSTCSTYLE = 524288
NSTCS_AUTOHSCROLL: _NSTCSTYLE = 1048576
NSTCS_FADEINOUTEXPANDOS: _NSTCSTYLE = 2097152
NSTCS_EMPTYTEXT: _NSTCSTYLE = 4194304
NSTCS_CHECKBOXES: _NSTCSTYLE = 8388608
NSTCS_PARTIALCHECKBOXES: _NSTCSTYLE = 16777216
NSTCS_EXCLUSIONCHECKBOXES: _NSTCSTYLE = 33554432
NSTCS_DIMMEDCHECKBOXES: _NSTCSTYLE = 67108864
NSTCS_NOINDENTCHECKS: _NSTCSTYLE = 134217728
NSTCS_ALLOWJUNCTIONS: _NSTCSTYLE = 268435456
NSTCS_SHOWTABSBUTTON: _NSTCSTYLE = 536870912
NSTCS_SHOWDELETEBUTTON: _NSTCSTYLE = 1073741824
NSTCS_SHOWREFRESHBUTTON: _NSTCSTYLE = -2147483648
_OPPROGDLGF = Int32
OPPROGDLG_DEFAULT: _OPPROGDLGF = 0
OPPROGDLG_ENABLEPAUSE: _OPPROGDLGF = 128
OPPROGDLG_ALLOWUNDO: _OPPROGDLGF = 256
OPPROGDLG_DONTDISPLAYSOURCEPATH: _OPPROGDLGF = 512
OPPROGDLG_DONTDISPLAYDESTPATH: _OPPROGDLGF = 1024
OPPROGDLG_NOMULTIDAYESTIMATES: _OPPROGDLGF = 2048
OPPROGDLG_DONTDISPLAYLOCATIONS: _OPPROGDLGF = 4096
_PDMODE = Int32
PDM_DEFAULT: _PDMODE = 0
PDM_RUN: _PDMODE = 1
PDM_PREFLIGHT: _PDMODE = 2
PDM_UNDOING: _PDMODE = 4
PDM_ERRORSBLOCKING: _PDMODE = 8
PDM_INDETERMINATE: _PDMODE = 16
_SHCONTF = Int32
SHCONTF_CHECKING_FOR_CHILDREN: _SHCONTF = 16
SHCONTF_FOLDERS: _SHCONTF = 32
SHCONTF_NONFOLDERS: _SHCONTF = 64
SHCONTF_INCLUDEHIDDEN: _SHCONTF = 128
SHCONTF_INIT_ON_FIRST_NEXT: _SHCONTF = 256
SHCONTF_NETPRINTERSRCH: _SHCONTF = 512
SHCONTF_SHAREABLE: _SHCONTF = 1024
SHCONTF_STORAGE: _SHCONTF = 2048
SHCONTF_NAVIGATION_ENUM: _SHCONTF = 4096
SHCONTF_FASTITEMS: _SHCONTF = 8192
SHCONTF_FLATLIST: _SHCONTF = 16384
SHCONTF_ENABLE_ASYNC: _SHCONTF = 32768
SHCONTF_INCLUDESUPERHIDDEN: _SHCONTF = 65536
_SICHINTF = Int32
SICHINT_DISPLAY: _SICHINTF = 0
SICHINT_ALLFIELDS: _SICHINTF = -2147483648
SICHINT_CANONICAL: _SICHINTF = 268435456
SICHINT_TEST_FILESYSPATH_IF_NOT_EQUAL: _SICHINTF = 536870912
_SPBEGINF = Int32
SPBEGINF_NORMAL: _SPBEGINF = 0
SPBEGINF_AUTOTIME: _SPBEGINF = 2
SPBEGINF_NOPROGRESSBAR: _SPBEGINF = 16
SPBEGINF_MARQUEEPROGRESS: _SPBEGINF = 32
SPBEGINF_NOCANCELBUTTON: _SPBEGINF = 64
_SPINITF = Int32
SPINITF_NORMAL: _SPINITF = 0
SPINITF_MODAL: _SPINITF = 1
SPINITF_NOMINIMIZE: _SPINITF = 8
_SV3CVW3_FLAGS = Int32
SV3CVW3_DEFAULT: _SV3CVW3_FLAGS = 0
SV3CVW3_NONINTERACTIVE: _SV3CVW3_FLAGS = 1
SV3CVW3_FORCEVIEWMODE: _SV3CVW3_FLAGS = 2
SV3CVW3_FORCEFOLDERFLAGS: _SV3CVW3_FLAGS = 4
_SVGIO = Int32
SVGIO_BACKGROUND: _SVGIO = 0
SVGIO_SELECTION: _SVGIO = 1
SVGIO_ALLVIEW: _SVGIO = 2
SVGIO_CHECKED: _SVGIO = 3
SVGIO_TYPE_MASK: _SVGIO = 15
SVGIO_FLAG_VIEWORDER: _SVGIO = -2147483648
_SVSIF = Int32
SVSI_DESELECT: _SVSIF = 0
SVSI_SELECT: _SVSIF = 1
SVSI_EDIT: _SVSIF = 3
SVSI_DESELECTOTHERS: _SVSIF = 4
SVSI_ENSUREVISIBLE: _SVSIF = 8
SVSI_FOCUSED: _SVSIF = 16
SVSI_TRANSLATEPT: _SVSIF = 32
SVSI_SELECTIONMARK: _SVSIF = 64
SVSI_POSITIONITEM: _SVSIF = 128
SVSI_CHECK: _SVSIF = 256
SVSI_CHECK2: _SVSIF = 512
SVSI_KEYBOARDSELECT: _SVSIF = 1025
SVSI_NOTAKEFOCUS: _SVSIF = 1073741824
_TRANSFER_ADVISE_STATE = Int32
TS_NONE: _TRANSFER_ADVISE_STATE = 0
TS_PERFORMING: _TRANSFER_ADVISE_STATE = 1
TS_PREPARING: _TRANSFER_ADVISE_STATE = 2
TS_INDETERMINATE: _TRANSFER_ADVISE_STATE = 4
_TRANSFER_SOURCE_FLAGS = Int32
TSF_NORMAL: _TRANSFER_SOURCE_FLAGS = 0
TSF_FAIL_EXIST: _TRANSFER_SOURCE_FLAGS = 0
TSF_RENAME_EXIST: _TRANSFER_SOURCE_FLAGS = 1
TSF_OVERWRITE_EXIST: _TRANSFER_SOURCE_FLAGS = 2
TSF_ALLOW_DECRYPTION: _TRANSFER_SOURCE_FLAGS = 4
TSF_NO_SECURITY: _TRANSFER_SOURCE_FLAGS = 8
TSF_COPY_CREATION_TIME: _TRANSFER_SOURCE_FLAGS = 16
TSF_COPY_WRITE_TIME: _TRANSFER_SOURCE_FLAGS = 32
TSF_USE_FULL_ACCESS: _TRANSFER_SOURCE_FLAGS = 64
TSF_DELETE_RECYCLE_IF_POSSIBLE: _TRANSFER_SOURCE_FLAGS = 128
TSF_COPY_HARD_LINK: _TRANSFER_SOURCE_FLAGS = 256
TSF_COPY_LOCALIZED_NAME: _TRANSFER_SOURCE_FLAGS = 512
TSF_MOVE_AS_COPY_DELETE: _TRANSFER_SOURCE_FLAGS = 1024
TSF_SUSPEND_SHELLEVENTS: _TRANSFER_SOURCE_FLAGS = 2048
make_head(_module, 'AASHELLMENUFILENAME')
make_head(_module, 'AASHELLMENUITEM')
if ARCH in 'X64,ARM64':
    make_head(_module, 'APPBARDATA')
if ARCH in 'X86':
    make_head(_module, 'APPBARDATA')
make_head(_module, 'APPCATEGORYINFO')
make_head(_module, 'APPCATEGORYINFOLIST')
make_head(_module, 'APPINFODATA')
make_head(_module, 'APPLET_PROC')
if ARCH in 'X64,ARM64':
    make_head(_module, 'ASSOCIATIONELEMENT')
if ARCH in 'X86':
    make_head(_module, 'ASSOCIATIONELEMENT')
make_head(_module, 'AUTO_SCROLL_DATA')
make_head(_module, 'BANDINFOSFB')
make_head(_module, 'BANDSITEINFO')
make_head(_module, 'BANNER_NOTIFICATION')
make_head(_module, 'BASEBROWSERDATALH')
make_head(_module, 'BASEBROWSERDATAXP')
make_head(_module, 'BFFCALLBACK')
make_head(_module, 'BROWSEINFOA')
make_head(_module, 'BROWSEINFOW')
make_head(_module, 'CABINETSTATE')
make_head(_module, 'CATEGORY_INFO')
make_head(_module, 'CIDA')
make_head(_module, 'CIE4ConnectionPoint')
make_head(_module, 'CMINVOKECOMMANDINFO')
make_head(_module, 'CMINVOKECOMMANDINFOEX')
make_head(_module, 'CMINVOKECOMMANDINFOEX_REMOTE')
make_head(_module, 'CM_COLUMNINFO')
make_head(_module, 'CONFIRM_CONFLICT_ITEM')
make_head(_module, 'CONFIRM_CONFLICT_RESULT_INFO')
make_head(_module, 'CPLINFO')
make_head(_module, 'CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION')
make_head(_module, 'CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR')
make_head(_module, 'CSFV')
make_head(_module, 'DATABLOCK_HEADER')
make_head(_module, 'DEFCONTEXTMENU')
make_head(_module, 'DELEGATEITEMID')
make_head(_module, 'DESKBANDINFO')
make_head(_module, 'DETAILSINFO')
make_head(_module, 'DFConstraint')
make_head(_module, 'DFMICS')
make_head(_module, 'DLLGETVERSIONPROC')
make_head(_module, 'DLLVERSIONINFO')
make_head(_module, 'DLLVERSIONINFO2')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DRAGINFOA')
if ARCH in 'X86':
    make_head(_module, 'DRAGINFOA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DRAGINFOW')
if ARCH in 'X86':
    make_head(_module, 'DRAGINFOW')
make_head(_module, 'DROPDESCRIPTION')
make_head(_module, 'DROPFILES')
make_head(_module, 'DShellFolderViewEvents')
make_head(_module, 'DShellNameSpaceEvents')
make_head(_module, 'DShellWindowsEvents')
make_head(_module, 'DWebBrowserEvents')
make_head(_module, 'DWebBrowserEvents2')
make_head(_module, 'EXP_DARWIN_LINK')
make_head(_module, 'EXP_PROPERTYSTORAGE')
make_head(_module, 'EXP_SPECIAL_FOLDER')
make_head(_module, 'EXP_SZ_LINK')
make_head(_module, 'EXTRASEARCH')
make_head(_module, 'FILEDESCRIPTORA')
make_head(_module, 'FILEDESCRIPTORW')
make_head(_module, 'FILEGROUPDESCRIPTORA')
make_head(_module, 'FILEGROUPDESCRIPTORW')
make_head(_module, 'FILE_ATTRIBUTES_ARRAY')
make_head(_module, 'FOLDERSETDATA')
make_head(_module, 'FOLDERSETTINGS')
make_head(_module, 'Folder')
make_head(_module, 'Folder2')
make_head(_module, 'Folder3')
make_head(_module, 'FolderItem')
make_head(_module, 'FolderItem2')
make_head(_module, 'FolderItemVerb')
make_head(_module, 'FolderItemVerbs')
make_head(_module, 'FolderItems')
make_head(_module, 'FolderItems2')
make_head(_module, 'FolderItems3')
make_head(_module, 'HELPINFO')
make_head(_module, 'HELPWININFOA')
make_head(_module, 'HELPWININFOW')
make_head(_module, 'HLBWINFO')
make_head(_module, 'HLITEM')
make_head(_module, 'HLTBINFO')
make_head(_module, 'IACList')
make_head(_module, 'IACList2')
make_head(_module, 'IAccessibilityDockingService')
make_head(_module, 'IAccessibilityDockingServiceCallback')
make_head(_module, 'IAccessibleObject')
make_head(_module, 'IActionProgress')
make_head(_module, 'IActionProgressDialog')
make_head(_module, 'IAppActivationUIInfo')
make_head(_module, 'IAppPublisher')
make_head(_module, 'IAppVisibility')
make_head(_module, 'IAppVisibilityEvents')
make_head(_module, 'IApplicationActivationManager')
make_head(_module, 'IApplicationAssociationRegistration')
make_head(_module, 'IApplicationAssociationRegistrationUI')
make_head(_module, 'IApplicationDesignModeSettings')
make_head(_module, 'IApplicationDesignModeSettings2')
make_head(_module, 'IApplicationDestinations')
make_head(_module, 'IApplicationDocumentLists')
make_head(_module, 'IAssocHandler')
make_head(_module, 'IAssocHandlerInvoker')
make_head(_module, 'IAttachmentExecute')
make_head(_module, 'IAutoComplete')
make_head(_module, 'IAutoComplete2')
make_head(_module, 'IAutoCompleteDropDown')
make_head(_module, 'IBandHost')
make_head(_module, 'IBandSite')
make_head(_module, 'IBannerNotificationHandler')
make_head(_module, 'IBanneredBar')
make_head(_module, 'IBrowserFrameOptions')
make_head(_module, 'IBrowserService')
make_head(_module, 'IBrowserService2')
make_head(_module, 'IBrowserService3')
make_head(_module, 'IBrowserService4')
make_head(_module, 'ICDBurn')
make_head(_module, 'ICDBurnExt')
make_head(_module, 'ICategorizer')
make_head(_module, 'ICategoryProvider')
make_head(_module, 'IColumnManager')
make_head(_module, 'IColumnProvider')
make_head(_module, 'ICommDlgBrowser')
make_head(_module, 'ICommDlgBrowser2')
make_head(_module, 'ICommDlgBrowser3')
make_head(_module, 'IComputerInfoChangeNotify')
make_head(_module, 'IConnectableCredentialProviderCredential')
make_head(_module, 'IContactManagerInterop')
make_head(_module, 'IContextMenu')
make_head(_module, 'IContextMenu2')
make_head(_module, 'IContextMenu3')
make_head(_module, 'IContextMenuCB')
make_head(_module, 'IContextMenuSite')
make_head(_module, 'ICopyHookA')
make_head(_module, 'ICopyHookW')
make_head(_module, 'ICreateProcessInputs')
make_head(_module, 'ICreatingProcess')
make_head(_module, 'ICredentialProvider')
make_head(_module, 'ICredentialProviderCredential')
make_head(_module, 'ICredentialProviderCredential2')
make_head(_module, 'ICredentialProviderCredentialEvents')
make_head(_module, 'ICredentialProviderCredentialEvents2')
make_head(_module, 'ICredentialProviderCredentialWithFieldOptions')
make_head(_module, 'ICredentialProviderEvents')
make_head(_module, 'ICredentialProviderFilter')
make_head(_module, 'ICredentialProviderSetUserArray')
make_head(_module, 'ICredentialProviderUser')
make_head(_module, 'ICredentialProviderUserArray')
make_head(_module, 'ICurrentItem')
make_head(_module, 'ICurrentWorkingDirectory')
make_head(_module, 'ICustomDestinationList')
make_head(_module, 'IDataObjectAsyncCapability')
make_head(_module, 'IDataObjectProvider')
make_head(_module, 'IDataTransferManagerInterop')
make_head(_module, 'IDefaultExtractIconInit')
make_head(_module, 'IDefaultFolderMenuInitialize')
make_head(_module, 'IDelegateFolder')
make_head(_module, 'IDelegateItem')
make_head(_module, 'IDeskBand')
make_head(_module, 'IDeskBand2')
make_head(_module, 'IDeskBandInfo')
make_head(_module, 'IDeskBar')
make_head(_module, 'IDeskBarClient')
make_head(_module, 'IDesktopGadget')
make_head(_module, 'IDesktopWallpaper')
make_head(_module, 'IDestinationStreamFactory')
make_head(_module, 'IDisplayItem')
make_head(_module, 'IDocViewSite')
make_head(_module, 'IDockingWindow')
make_head(_module, 'IDockingWindowFrame')
make_head(_module, 'IDockingWindowSite')
make_head(_module, 'IDragSourceHelper')
make_head(_module, 'IDragSourceHelper2')
make_head(_module, 'IDropTargetHelper')
make_head(_module, 'IDynamicHWHandler')
make_head(_module, 'IEnumACString')
make_head(_module, 'IEnumAssocHandlers')
make_head(_module, 'IEnumExplorerCommand')
make_head(_module, 'IEnumExtraSearch')
make_head(_module, 'IEnumFullIDList')
make_head(_module, 'IEnumHLITEM')
make_head(_module, 'IEnumIDList')
make_head(_module, 'IEnumObjects')
make_head(_module, 'IEnumPublishedApps')
make_head(_module, 'IEnumReadyCallback')
make_head(_module, 'IEnumResources')
make_head(_module, 'IEnumShellItems')
make_head(_module, 'IEnumSyncMgrConflict')
make_head(_module, 'IEnumSyncMgrEvents')
make_head(_module, 'IEnumSyncMgrSyncItems')
make_head(_module, 'IEnumTravelLogEntry')
make_head(_module, 'IEnumerableView')
make_head(_module, 'IExecuteCommand')
make_head(_module, 'IExecuteCommandApplicationHostEnvironment')
make_head(_module, 'IExecuteCommandHost')
make_head(_module, 'IExpDispSupport')
make_head(_module, 'IExpDispSupportXP')
make_head(_module, 'IExplorerBrowser')
make_head(_module, 'IExplorerBrowserEvents')
make_head(_module, 'IExplorerCommand')
make_head(_module, 'IExplorerCommandProvider')
make_head(_module, 'IExplorerCommandState')
make_head(_module, 'IExplorerPaneVisibility')
make_head(_module, 'IExtensionServices')
make_head(_module, 'IExtractIconA')
make_head(_module, 'IExtractIconW')
make_head(_module, 'IExtractImage')
make_head(_module, 'IExtractImage2')
make_head(_module, 'IFileDialog')
make_head(_module, 'IFileDialog2')
make_head(_module, 'IFileDialogControlEvents')
make_head(_module, 'IFileDialogCustomize')
make_head(_module, 'IFileDialogEvents')
make_head(_module, 'IFileIsInUse')
make_head(_module, 'IFileOpenDialog')
make_head(_module, 'IFileOperation')
make_head(_module, 'IFileOperation2')
make_head(_module, 'IFileOperationProgressSink')
make_head(_module, 'IFileSaveDialog')
make_head(_module, 'IFileSearchBand')
make_head(_module, 'IFileSyncMergeHandler')
make_head(_module, 'IFileSystemBindData')
make_head(_module, 'IFileSystemBindData2')
make_head(_module, 'IFolderBandPriv')
make_head(_module, 'IFolderFilter')
make_head(_module, 'IFolderFilterSite')
make_head(_module, 'IFolderView')
make_head(_module, 'IFolderView2')
make_head(_module, 'IFolderViewHost')
make_head(_module, 'IFolderViewOC')
make_head(_module, 'IFolderViewOptions')
make_head(_module, 'IFolderViewSettings')
make_head(_module, 'IFrameworkInputPane')
make_head(_module, 'IFrameworkInputPaneHandler')
make_head(_module, 'IGetServiceIds')
make_head(_module, 'IHWEventHandler')
make_head(_module, 'IHWEventHandler2')
make_head(_module, 'IHandlerActivationHost')
make_head(_module, 'IHandlerInfo')
make_head(_module, 'IHandlerInfo2')
make_head(_module, 'IHlink')
make_head(_module, 'IHlinkBrowseContext')
make_head(_module, 'IHlinkFrame')
make_head(_module, 'IHlinkSite')
make_head(_module, 'IHlinkTarget')
make_head(_module, 'IHomeGroup')
make_head(_module, 'IIOCancelInformation')
make_head(_module, 'IIdentityName')
make_head(_module, 'IImageRecompress')
make_head(_module, 'IInitializeCommand')
make_head(_module, 'IInitializeNetworkFolder')
make_head(_module, 'IInitializeObject')
make_head(_module, 'IInitializeWithBindCtx')
make_head(_module, 'IInitializeWithItem')
make_head(_module, 'IInitializeWithPropertyStore')
make_head(_module, 'IInitializeWithWindow')
make_head(_module, 'IInputObject')
make_head(_module, 'IInputObject2')
make_head(_module, 'IInputObjectSite')
make_head(_module, 'IInputPaneAnimationCoordinator')
make_head(_module, 'IInputPanelConfiguration')
make_head(_module, 'IInputPanelInvocationConfiguration')
make_head(_module, 'IInsertItem')
make_head(_module, 'IItemNameLimits')
make_head(_module, 'IKnownFolder')
make_head(_module, 'IKnownFolderManager')
make_head(_module, 'ILaunchSourceAppUserModelId')
make_head(_module, 'ILaunchSourceViewSizePreference')
make_head(_module, 'ILaunchTargetMonitor')
make_head(_module, 'ILaunchTargetViewSizePreference')
make_head(_module, 'ILaunchUIContext')
make_head(_module, 'ILaunchUIContextProvider')
make_head(_module, 'IMenuBand')
make_head(_module, 'IMenuPopup')
make_head(_module, 'IModalWindow')
make_head(_module, 'INameSpaceTreeAccessible')
make_head(_module, 'INameSpaceTreeControl')
make_head(_module, 'INameSpaceTreeControl2')
make_head(_module, 'INameSpaceTreeControlCustomDraw')
make_head(_module, 'INameSpaceTreeControlDropHandler')
make_head(_module, 'INameSpaceTreeControlEvents')
make_head(_module, 'INameSpaceTreeControlFolderCapabilities')
make_head(_module, 'INamedPropertyBag')
make_head(_module, 'INamespaceWalk')
make_head(_module, 'INamespaceWalkCB')
make_head(_module, 'INamespaceWalkCB2')
make_head(_module, 'INetworkFolderInternal')
make_head(_module, 'INewMenuClient')
make_head(_module, 'INewShortcutHookA')
make_head(_module, 'INewShortcutHookW')
make_head(_module, 'INewWDEvents')
make_head(_module, 'INewWindowManager')
make_head(_module, 'INotifyReplica')
make_head(_module, 'IObjMgr')
make_head(_module, 'IObjectProvider')
make_head(_module, 'IObjectWithAppUserModelID')
make_head(_module, 'IObjectWithBackReferences')
make_head(_module, 'IObjectWithCancelEvent')
make_head(_module, 'IObjectWithFolderEnumMode')
make_head(_module, 'IObjectWithProgID')
make_head(_module, 'IObjectWithSelection')
make_head(_module, 'IOpenControlPanel')
make_head(_module, 'IOpenSearchSource')
make_head(_module, 'IOperationsProgressDialog')
make_head(_module, 'IPackageDebugSettings')
make_head(_module, 'IPackageDebugSettings2')
make_head(_module, 'IPackageExecutionStateChangeNotification')
make_head(_module, 'IParentAndItem')
make_head(_module, 'IParseAndCreateItem')
make_head(_module, 'IPersistFolder')
make_head(_module, 'IPersistFolder2')
make_head(_module, 'IPersistFolder3')
make_head(_module, 'IPersistIDList')
make_head(_module, 'IPreviewHandler')
make_head(_module, 'IPreviewHandlerFrame')
make_head(_module, 'IPreviewHandlerVisuals')
make_head(_module, 'IPreviewItem')
make_head(_module, 'IPreviousVersionsInfo')
make_head(_module, 'IProfferService')
make_head(_module, 'IProgressDialog')
make_head(_module, 'IPropertyKeyStore')
make_head(_module, 'IPublishedApp')
make_head(_module, 'IPublishedApp2')
make_head(_module, 'IPublishingWizard')
make_head(_module, 'IQueryAssociations')
make_head(_module, 'IQueryCancelAutoPlay')
make_head(_module, 'IQueryCodePage')
make_head(_module, 'IQueryContinue')
make_head(_module, 'IQueryContinueWithStatus')
make_head(_module, 'IQueryInfo')
make_head(_module, 'IRegTreeItem')
make_head(_module, 'IRelatedItem')
make_head(_module, 'IRemoteComputer')
make_head(_module, 'IResolveShellLink')
make_head(_module, 'IResultsFolder')
make_head(_module, 'IRunnableTask')
make_head(_module, 'IScriptErrorList')
make_head(_module, 'ISearchBoxInfo')
make_head(_module, 'ISearchContext')
make_head(_module, 'ISearchFolderItemFactory')
make_head(_module, 'ISharedBitmap')
make_head(_module, 'ISharingConfigurationManager')
make_head(_module, 'IShellApp')
make_head(_module, 'IShellBrowser')
make_head(_module, 'IShellChangeNotify')
make_head(_module, 'IShellDetails')
make_head(_module, 'IShellDispatch')
make_head(_module, 'IShellDispatch2')
make_head(_module, 'IShellDispatch3')
make_head(_module, 'IShellDispatch4')
make_head(_module, 'IShellDispatch5')
make_head(_module, 'IShellDispatch6')
make_head(_module, 'IShellExtInit')
make_head(_module, 'IShellFavoritesNameSpace')
make_head(_module, 'IShellFolder')
make_head(_module, 'IShellFolder2')
make_head(_module, 'IShellFolderBand')
make_head(_module, 'IShellFolderView')
make_head(_module, 'IShellFolderViewCB')
make_head(_module, 'IShellFolderViewDual')
make_head(_module, 'IShellFolderViewDual2')
make_head(_module, 'IShellFolderViewDual3')
make_head(_module, 'IShellIcon')
make_head(_module, 'IShellIconOverlay')
make_head(_module, 'IShellIconOverlayIdentifier')
make_head(_module, 'IShellIconOverlayManager')
make_head(_module, 'IShellImageData')
make_head(_module, 'IShellImageDataAbort')
make_head(_module, 'IShellImageDataFactory')
make_head(_module, 'IShellItem')
make_head(_module, 'IShellItem2')
make_head(_module, 'IShellItemArray')
make_head(_module, 'IShellItemFilter')
make_head(_module, 'IShellItemImageFactory')
make_head(_module, 'IShellItemResources')
make_head(_module, 'IShellLibrary')
make_head(_module, 'IShellLinkA')
make_head(_module, 'IShellLinkDataList')
make_head(_module, 'IShellLinkDual')
make_head(_module, 'IShellLinkDual2')
make_head(_module, 'IShellLinkW')
make_head(_module, 'IShellMenu')
make_head(_module, 'IShellMenuCallback')
make_head(_module, 'IShellNameSpace')
make_head(_module, 'IShellPropSheetExt')
make_head(_module, 'IShellRunDll')
make_head(_module, 'IShellService')
make_head(_module, 'IShellTaskScheduler')
make_head(_module, 'IShellUIHelper')
make_head(_module, 'IShellUIHelper2')
make_head(_module, 'IShellUIHelper3')
make_head(_module, 'IShellUIHelper4')
make_head(_module, 'IShellUIHelper5')
make_head(_module, 'IShellUIHelper6')
make_head(_module, 'IShellUIHelper7')
make_head(_module, 'IShellUIHelper8')
make_head(_module, 'IShellUIHelper9')
make_head(_module, 'IShellView')
make_head(_module, 'IShellView2')
make_head(_module, 'IShellView3')
make_head(_module, 'IShellWindows')
make_head(_module, 'ISortColumnArray')
make_head(_module, 'IStartMenuPinnedList')
make_head(_module, 'IStorageProviderBanners')
make_head(_module, 'IStorageProviderCopyHook')
make_head(_module, 'IStorageProviderHandler')
make_head(_module, 'IStorageProviderPropertyHandler')
make_head(_module, 'IStreamAsync')
make_head(_module, 'IStreamUnbufferedInfo')
make_head(_module, 'ISuspensionDependencyManager')
make_head(_module, 'ISyncMgrConflict')
make_head(_module, 'ISyncMgrConflictFolder')
make_head(_module, 'ISyncMgrConflictItems')
make_head(_module, 'ISyncMgrConflictPresenter')
make_head(_module, 'ISyncMgrConflictResolutionItems')
make_head(_module, 'ISyncMgrConflictResolveInfo')
make_head(_module, 'ISyncMgrConflictStore')
make_head(_module, 'ISyncMgrControl')
make_head(_module, 'ISyncMgrEnumItems')
make_head(_module, 'ISyncMgrEvent')
make_head(_module, 'ISyncMgrEventLinkUIOperation')
make_head(_module, 'ISyncMgrEventStore')
make_head(_module, 'ISyncMgrHandler')
make_head(_module, 'ISyncMgrHandlerCollection')
make_head(_module, 'ISyncMgrHandlerInfo')
make_head(_module, 'ISyncMgrRegister')
make_head(_module, 'ISyncMgrResolutionHandler')
make_head(_module, 'ISyncMgrScheduleWizardUIOperation')
make_head(_module, 'ISyncMgrSessionCreator')
make_head(_module, 'ISyncMgrSyncCallback')
make_head(_module, 'ISyncMgrSyncItem')
make_head(_module, 'ISyncMgrSyncItemContainer')
make_head(_module, 'ISyncMgrSyncItemInfo')
make_head(_module, 'ISyncMgrSyncResult')
make_head(_module, 'ISyncMgrSynchronize')
make_head(_module, 'ISyncMgrSynchronizeCallback')
make_head(_module, 'ISyncMgrSynchronizeInvoke')
make_head(_module, 'ISyncMgrUIOperation')
make_head(_module, 'ITEMSPACING')
make_head(_module, 'ITaskbarList')
make_head(_module, 'ITaskbarList2')
make_head(_module, 'ITaskbarList3')
make_head(_module, 'ITaskbarList4')
make_head(_module, 'IThumbnailCache')
make_head(_module, 'IThumbnailCachePrimer')
make_head(_module, 'IThumbnailCapture')
make_head(_module, 'IThumbnailHandlerFactory')
make_head(_module, 'IThumbnailProvider')
make_head(_module, 'IThumbnailSettings')
make_head(_module, 'IThumbnailStreamCache')
make_head(_module, 'ITrackShellMenu')
make_head(_module, 'ITranscodeImage')
make_head(_module, 'ITransferAdviseSink')
make_head(_module, 'ITransferDestination')
make_head(_module, 'ITransferMediumItem')
make_head(_module, 'ITransferSource')
make_head(_module, 'ITravelEntry')
make_head(_module, 'ITravelLog')
make_head(_module, 'ITravelLogClient')
make_head(_module, 'ITravelLogEntry')
make_head(_module, 'ITravelLogStg')
make_head(_module, 'ITrayDeskBand')
make_head(_module, 'IURLSearchHook')
make_head(_module, 'IURLSearchHook2')
make_head(_module, 'IUniformResourceLocatorA')
make_head(_module, 'IUniformResourceLocatorW')
make_head(_module, 'IUpdateIDList')
make_head(_module, 'IUseToBrowseItem')
make_head(_module, 'IUserAccountChangeCallback')
make_head(_module, 'IUserNotification')
make_head(_module, 'IUserNotification2')
make_head(_module, 'IUserNotificationCallback')
make_head(_module, 'IViewStateIdentityItem')
make_head(_module, 'IVirtualDesktopManager')
make_head(_module, 'IVisualProperties')
make_head(_module, 'IWebBrowser')
make_head(_module, 'IWebBrowser2')
make_head(_module, 'IWebBrowserApp')
make_head(_module, 'IWebWizardExtension')
make_head(_module, 'IWebWizardHost')
make_head(_module, 'IWebWizardHost2')
make_head(_module, 'IWizardExtension')
make_head(_module, 'IWizardSite')
make_head(_module, 'KNOWNFOLDER_DEFINITION')
make_head(_module, 'LPFNDFMCALLBACK')
make_head(_module, 'LPFNVIEWCALLBACK')
make_head(_module, 'MULTIKEYHELPA')
make_head(_module, 'MULTIKEYHELPW')
make_head(_module, 'NC_ADDRESS')
make_head(_module, 'NEWCPLINFOA')
make_head(_module, 'NEWCPLINFOW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'NOTIFYICONDATAA')
if ARCH in 'X86':
    make_head(_module, 'NOTIFYICONDATAA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'NOTIFYICONDATAW')
if ARCH in 'X86':
    make_head(_module, 'NOTIFYICONDATAW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'NOTIFYICONIDENTIFIER')
if ARCH in 'X86':
    make_head(_module, 'NOTIFYICONIDENTIFIER')
make_head(_module, 'NRESARRAY')
make_head(_module, 'NSTCCUSTOMDRAW')
make_head(_module, 'NT_CONSOLE_PROPS')
make_head(_module, 'NT_FE_CONSOLE_PROPS')
make_head(_module, 'OPENASINFO')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OPEN_PRINTER_PROPS_INFOA')
if ARCH in 'X86':
    make_head(_module, 'OPEN_PRINTER_PROPS_INFOA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OPEN_PRINTER_PROPS_INFOW')
if ARCH in 'X86':
    make_head(_module, 'OPEN_PRINTER_PROPS_INFOW')
make_head(_module, 'PAPPCONSTRAIN_CHANGE_ROUTINE')
make_head(_module, 'PAPPSTATE_CHANGE_ROUTINE')
make_head(_module, 'PARSEDURLA')
make_head(_module, 'PARSEDURLW')
make_head(_module, 'PERSIST_FOLDER_TARGET_INFO')
make_head(_module, 'PFNCANSHAREFOLDERW')
make_head(_module, 'PFNSHOWSHAREFOLDERUIW')
make_head(_module, 'PREVIEWHANDLERFRAMEINFO')
make_head(_module, 'PROFILEINFOA')
make_head(_module, 'PROFILEINFOW')
make_head(_module, 'PUBAPPINFO')
make_head(_module, 'QCMINFO')
make_head(_module, 'QCMINFO_IDMAP')
make_head(_module, 'QCMINFO_IDMAP_PLACEMENT')
make_head(_module, 'QITAB')
make_head(_module, 'SFVM_HELPTOPIC_DATA')
make_head(_module, 'SFVM_PROPPAGE_DATA')
make_head(_module, 'SFV_CREATE')
make_head(_module, 'SFV_SETITEMPOS')
make_head(_module, 'SHARDAPPIDINFO')
make_head(_module, 'SHARDAPPIDINFOIDLIST')
make_head(_module, 'SHARDAPPIDINFOLINK')
make_head(_module, 'SHCOLUMNDATA')
make_head(_module, 'SHCOLUMNINFO')
make_head(_module, 'SHCOLUMNINIT')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHCREATEPROCESSINFOW')
if ARCH in 'X86':
    make_head(_module, 'SHCREATEPROCESSINFOW')
make_head(_module, 'SHChangeDWORDAsIDList')
make_head(_module, 'SHChangeNotifyEntry')
make_head(_module, 'SHChangeProductKeyAsIDList')
make_head(_module, 'SHChangeUpdateImageIDList')
make_head(_module, 'SHDESCRIPTIONID')
make_head(_module, 'SHDRAGIMAGE')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHELLEXECUTEINFOA')
if ARCH in 'X86':
    make_head(_module, 'SHELLEXECUTEINFOA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHELLEXECUTEINFOW')
if ARCH in 'X86':
    make_head(_module, 'SHELLEXECUTEINFOW')
make_head(_module, 'SHELLFLAGSTATE')
make_head(_module, 'SHELLSTATEA')
make_head(_module, 'SHELLSTATEW')
make_head(_module, 'SHELL_ITEM_RESOURCE')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHFILEINFOA')
if ARCH in 'X86':
    make_head(_module, 'SHFILEINFOA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHFILEINFOW')
if ARCH in 'X86':
    make_head(_module, 'SHFILEINFOW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHFILEOPSTRUCTA')
if ARCH in 'X86':
    make_head(_module, 'SHFILEOPSTRUCTA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHFILEOPSTRUCTW')
if ARCH in 'X86':
    make_head(_module, 'SHFILEOPSTRUCTW')
make_head(_module, 'SHFOLDERCUSTOMSETTINGS')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHNAMEMAPPINGA')
if ARCH in 'X86':
    make_head(_module, 'SHNAMEMAPPINGA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHNAMEMAPPINGW')
if ARCH in 'X86':
    make_head(_module, 'SHNAMEMAPPINGW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHQUERYRBINFO')
if ARCH in 'X86':
    make_head(_module, 'SHQUERYRBINFO')
if ARCH in 'X64,ARM64':
    make_head(_module, 'SHSTOCKICONINFO')
if ARCH in 'X86':
    make_head(_module, 'SHSTOCKICONINFO')
make_head(_module, 'SLOWAPPINFO')
make_head(_module, 'SMCSHCHANGENOTIFYSTRUCT')
make_head(_module, 'SMDATA')
make_head(_module, 'SMINFO')
make_head(_module, 'SORTCOLUMN')
make_head(_module, 'SUBCLASSPROC')
make_head(_module, 'SV2CVW2_PARAMS')
make_head(_module, 'SYNCMGRHANDLERINFO')
make_head(_module, 'SYNCMGRITEM')
make_head(_module, 'SYNCMGRLOGERRORINFO')
make_head(_module, 'SYNCMGRPROGRESSITEM')
make_head(_module, 'SYNCMGR_CONFLICT_ID_INFO')
make_head(_module, 'TBINFO')
make_head(_module, 'THUMBBUTTON')
make_head(_module, 'TOOLBARITEM')
make_head(_module, 'URLINVOKECOMMANDINFOA')
make_head(_module, 'URLINVOKECOMMANDINFOW')
make_head(_module, 'WINDOWDATA')
make_head(_module, 'WTS_THUMBNAILID')
make_head(_module, '_APPCONSTRAIN_REGISTRATION')
make_head(_module, '_APPSTATE_REGISTRATION')
__all__ = [
    "AASHELLMENUFILENAME",
    "AASHELLMENUITEM",
    "ABE_BOTTOM",
    "ABE_LEFT",
    "ABE_RIGHT",
    "ABE_TOP",
    "ABM_ACTIVATE",
    "ABM_GETAUTOHIDEBAR",
    "ABM_GETAUTOHIDEBAREX",
    "ABM_GETSTATE",
    "ABM_GETTASKBARPOS",
    "ABM_NEW",
    "ABM_QUERYPOS",
    "ABM_REMOVE",
    "ABM_SETAUTOHIDEBAR",
    "ABM_SETAUTOHIDEBAREX",
    "ABM_SETPOS",
    "ABM_SETSTATE",
    "ABM_WINDOWPOSCHANGED",
    "ABN_FULLSCREENAPP",
    "ABN_POSCHANGED",
    "ABN_STATECHANGE",
    "ABN_WINDOWARRANGE",
    "ABS_ALWAYSONTOP",
    "ABS_AUTOHIDE",
    "ACDD_VISIBLE",
    "ACENUMOPTION",
    "ACEO_FIRSTUNUSED",
    "ACEO_MOSTRECENTFIRST",
    "ACEO_NONE",
    "ACLO_CURRENTDIR",
    "ACLO_DESKTOP",
    "ACLO_FAVORITES",
    "ACLO_FILESYSDIRS",
    "ACLO_FILESYSONLY",
    "ACLO_MYCOMPUTER",
    "ACLO_NONE",
    "ACLO_VIRTUALNAMESPACE",
    "ACO_AUTOAPPEND",
    "ACO_AUTOSUGGEST",
    "ACO_FILTERPREFIXES",
    "ACO_NONE",
    "ACO_NOPREFIXFILTERING",
    "ACO_RTLREADING",
    "ACO_SEARCH",
    "ACO_UPDOWNKEYDROPSLIST",
    "ACO_USETAB",
    "ACO_WORD_FILTER",
    "ACTIVATEOPTIONS",
    "ADDURL_SILENT",
    "ADE_LEFT",
    "ADE_NONE",
    "ADE_RIGHT",
    "ADJACENT_DISPLAY_EDGES",
    "ADLT_FREQUENT",
    "ADLT_RECENT",
    "AD_APPLY_BUFFERED_REFRESH",
    "AD_APPLY_DYNAMICREFRESH",
    "AD_APPLY_FORCE",
    "AD_APPLY_HTMLGEN",
    "AD_APPLY_REFRESH",
    "AD_APPLY_SAVE",
    "AD_GETWP_BMP",
    "AD_GETWP_IMAGE",
    "AD_GETWP_LAST_APPLIED",
    "AHE_DESKTOP",
    "AHE_IMMERSIVE",
    "AHE_TYPE",
    "AHTYPE",
    "AHTYPE_ANY_APPLICATION",
    "AHTYPE_ANY_PROGID",
    "AHTYPE_APPLICATION",
    "AHTYPE_CLASS_APPLICATION",
    "AHTYPE_MACHINEDEFAULT",
    "AHTYPE_PROGID",
    "AHTYPE_UNDEFINED",
    "AHTYPE_USER_APPLICATION",
    "AIM_COMMENTS",
    "AIM_CONTACT",
    "AIM_DISPLAYNAME",
    "AIM_HELPLINK",
    "AIM_IMAGE",
    "AIM_INSTALLDATE",
    "AIM_INSTALLLOCATION",
    "AIM_INSTALLSOURCE",
    "AIM_LANGUAGE",
    "AIM_PRODUCTID",
    "AIM_PUBLISHER",
    "AIM_READMEURL",
    "AIM_REGISTEREDCOMPANY",
    "AIM_REGISTEREDOWNER",
    "AIM_SUPPORTTELEPHONE",
    "AIM_SUPPORTURL",
    "AIM_UPDATEINFOURL",
    "AIM_VERSION",
    "AL_EFFECTIVE",
    "AL_MACHINE",
    "AL_USER",
    "AO_DESIGNMODE",
    "AO_NOERRORUI",
    "AO_NONE",
    "AO_NOSPLASHSCREEN",
    "AO_PRELAUNCH",
    "APPACTIONFLAGS",
    "APPACTION_ADDLATER",
    "APPACTION_CANGETSIZE",
    "APPACTION_INSTALL",
    "APPACTION_MODIFY",
    "APPACTION_MODIFYREMOVE",
    "APPACTION_REPAIR",
    "APPACTION_UNINSTALL",
    "APPACTION_UNSCHEDULE",
    "APPACTION_UPGRADE",
    "APPBARDATA",
    "APPCATEGORYINFO",
    "APPCATEGORYINFOLIST",
    "APPDOCLISTTYPE",
    "APPINFODATA",
    "APPINFODATAFLAGS",
    "APPLET_PROC",
    "APPLICATION_VIEW_MIN_WIDTH",
    "APPLICATION_VIEW_ORIENTATION",
    "APPLICATION_VIEW_SIZE_PREFERENCE",
    "APPLICATION_VIEW_STATE",
    "APPNAMEBUFFERLEN",
    "ARCONTENT_AUDIOCD",
    "ARCONTENT_AUTOPLAYMUSIC",
    "ARCONTENT_AUTOPLAYPIX",
    "ARCONTENT_AUTOPLAYVIDEO",
    "ARCONTENT_AUTORUNINF",
    "ARCONTENT_BLANKBD",
    "ARCONTENT_BLANKCD",
    "ARCONTENT_BLANKDVD",
    "ARCONTENT_BLURAY",
    "ARCONTENT_CAMERASTORAGE",
    "ARCONTENT_CUSTOMEVENT",
    "ARCONTENT_DVDAUDIO",
    "ARCONTENT_DVDMOVIE",
    "ARCONTENT_MASK",
    "ARCONTENT_NONE",
    "ARCONTENT_PHASE_FINAL",
    "ARCONTENT_PHASE_MASK",
    "ARCONTENT_PHASE_PRESNIFF",
    "ARCONTENT_PHASE_SNIFFING",
    "ARCONTENT_PHASE_UNKNOWN",
    "ARCONTENT_SVCD",
    "ARCONTENT_UNKNOWNCONTENT",
    "ARCONTENT_VCD",
    "ASSOCCLASS",
    "ASSOCCLASS_APP_KEY",
    "ASSOCCLASS_APP_STR",
    "ASSOCCLASS_CLSID_KEY",
    "ASSOCCLASS_CLSID_STR",
    "ASSOCCLASS_FIXED_PROGID_STR",
    "ASSOCCLASS_FOLDER",
    "ASSOCCLASS_PROGID_KEY",
    "ASSOCCLASS_PROGID_STR",
    "ASSOCCLASS_PROTOCOL_STR",
    "ASSOCCLASS_SHELL_KEY",
    "ASSOCCLASS_STAR",
    "ASSOCCLASS_SYSTEM_STR",
    "ASSOCDATA",
    "ASSOCDATA_EDITFLAGS",
    "ASSOCDATA_HASPERUSERASSOC",
    "ASSOCDATA_MAX",
    "ASSOCDATA_MSIDESCRIPTOR",
    "ASSOCDATA_NOACTIVATEHANDLER",
    "ASSOCDATA_UNUSED1",
    "ASSOCDATA_VALUE",
    "ASSOCENUM",
    "ASSOCENUM_NONE",
    "ASSOCF",
    "ASSOCF_APP_TO_APP",
    "ASSOCF_IGNOREBASECLASS",
    "ASSOCF_INIT_BYEXENAME",
    "ASSOCF_INIT_DEFAULTTOFOLDER",
    "ASSOCF_INIT_DEFAULTTOSTAR",
    "ASSOCF_INIT_FIXED_PROGID",
    "ASSOCF_INIT_FOR_FILE",
    "ASSOCF_INIT_IGNOREUNKNOWN",
    "ASSOCF_INIT_NOREMAPCLSID",
    "ASSOCF_IS_FULL_URI",
    "ASSOCF_IS_PROTOCOL",
    "ASSOCF_NOFIXUPS",
    "ASSOCF_NONE",
    "ASSOCF_NOTRUNCATE",
    "ASSOCF_NOUSERSETTINGS",
    "ASSOCF_OPEN_BYEXENAME",
    "ASSOCF_PER_MACHINE_ONLY",
    "ASSOCF_REMAPRUNDLL",
    "ASSOCF_VERIFY",
    "ASSOCIATIONELEMENT",
    "ASSOCIATIONLEVEL",
    "ASSOCIATIONTYPE",
    "ASSOCKEY",
    "ASSOCKEY_APP",
    "ASSOCKEY_BASECLASS",
    "ASSOCKEY_CLASS",
    "ASSOCKEY_MAX",
    "ASSOCKEY_SHELLEXECCLASS",
    "ASSOCSTR",
    "ASSOCSTR_APPICONREFERENCE",
    "ASSOCSTR_APPID",
    "ASSOCSTR_APPPUBLISHER",
    "ASSOCSTR_COMMAND",
    "ASSOCSTR_CONTENTTYPE",
    "ASSOCSTR_DDEAPPLICATION",
    "ASSOCSTR_DDECOMMAND",
    "ASSOCSTR_DDEIFEXEC",
    "ASSOCSTR_DDETOPIC",
    "ASSOCSTR_DEFAULTICON",
    "ASSOCSTR_DELEGATEEXECUTE",
    "ASSOCSTR_DROPTARGET",
    "ASSOCSTR_EXECUTABLE",
    "ASSOCSTR_FRIENDLYAPPNAME",
    "ASSOCSTR_FRIENDLYDOCNAME",
    "ASSOCSTR_INFOTIP",
    "ASSOCSTR_MAX",
    "ASSOCSTR_NOOPEN",
    "ASSOCSTR_PROGID",
    "ASSOCSTR_QUICKTIP",
    "ASSOCSTR_SHELLEXTENSION",
    "ASSOCSTR_SHELLNEWVALUE",
    "ASSOCSTR_SUPPORTED_URI_PROTOCOLS",
    "ASSOCSTR_TILEINFO",
    "ASSOC_FILTER",
    "ASSOC_FILTER_NONE",
    "ASSOC_FILTER_RECOMMENDED",
    "ATTACHMENT_ACTION",
    "ATTACHMENT_ACTION_CANCEL",
    "ATTACHMENT_ACTION_EXEC",
    "ATTACHMENT_ACTION_SAVE",
    "ATTACHMENT_PROMPT",
    "ATTACHMENT_PROMPT_EXEC",
    "ATTACHMENT_PROMPT_EXEC_OR_SAVE",
    "ATTACHMENT_PROMPT_NONE",
    "ATTACHMENT_PROMPT_SAVE",
    "AT_FILEEXTENSION",
    "AT_MIMETYPE",
    "AT_STARTMENUCLIENT",
    "AT_URLPROTOCOL",
    "AUTOCOMPLETELISTOPTIONS",
    "AUTOCOMPLETEOPTIONS",
    "AUTO_SCROLL_DATA",
    "AVMW_320",
    "AVMW_500",
    "AVMW_DEFAULT",
    "AVO_LANDSCAPE",
    "AVO_PORTRAIT",
    "AVSP_CUSTOM",
    "AVSP_DEFAULT",
    "AVSP_USE_HALF",
    "AVSP_USE_LESS",
    "AVSP_USE_MINIMUM",
    "AVSP_USE_MORE",
    "AVSP_USE_NONE",
    "AVS_FILLED",
    "AVS_FULLSCREEN_LANDSCAPE",
    "AVS_FULLSCREEN_PORTRAIT",
    "AVS_SNAPPED",
    "AccessibilityDockingService",
    "AlphabeticalCategorizer",
    "AppShellVerbHandler",
    "AppStartupLink",
    "AppVisibility",
    "ApplicationActivationManager",
    "ApplicationAssociationRegistration",
    "ApplicationAssociationRegistrationUI",
    "ApplicationDesignModeSettings",
    "ApplicationDestinations",
    "ApplicationDocumentLists",
    "AssocCreate",
    "AssocCreateForClasses",
    "AssocGetDetailsOfPropKey",
    "AssocGetPerceivedType",
    "AssocIsDangerous",
    "AssocQueryKeyA",
    "AssocQueryKeyW",
    "AssocQueryStringA",
    "AssocQueryStringByKeyA",
    "AssocQueryStringByKeyW",
    "AssocQueryStringW",
    "AttachmentServices",
    "BANDINFOSFB",
    "BANDSITECID",
    "BANDSITEINFO",
    "BANNER_NOTIFICATION",
    "BANNER_NOTIFICATION_EVENT",
    "BASEBROWSERDATALH",
    "BASEBROWSERDATAXP",
    "BFFCALLBACK",
    "BFFM_ENABLEOK",
    "BFFM_INITIALIZED",
    "BFFM_IUNKNOWN",
    "BFFM_SELCHANGED",
    "BFFM_SETEXPANDED",
    "BFFM_SETOKTEXT",
    "BFFM_SETSELECTION",
    "BFFM_SETSELECTIONA",
    "BFFM_SETSELECTIONW",
    "BFFM_SETSTATUSTEXT",
    "BFFM_SETSTATUSTEXTA",
    "BFFM_SETSTATUSTEXTW",
    "BFFM_VALIDATEFAILED",
    "BFFM_VALIDATEFAILEDA",
    "BFFM_VALIDATEFAILEDW",
    "BFO_ADD_IE_TOCAPTIONBAR",
    "BFO_BOTH_OPTIONS",
    "BFO_BROWSER_PERSIST_SETTINGS",
    "BFO_BROWSE_NO_IN_NEW_PROCESS",
    "BFO_ENABLE_HYPERLINK_TRACKING",
    "BFO_GO_HOME_PAGE",
    "BFO_NONE",
    "BFO_NO_PARENT_FOLDER_SUPPORT",
    "BFO_NO_REOPEN_NEXT_RESTART",
    "BFO_PREFER_IEPROCESS",
    "BFO_QUERY_ALL",
    "BFO_RENAME_FOLDER_OPTIONS_TOINTERNET",
    "BFO_SHOW_NAVIGATION_CANCELLED",
    "BFO_SUBSTITUE_INTERNET_START_PAGE",
    "BFO_USE_DIALUP_REF",
    "BFO_USE_IE_LOGOBANDING",
    "BFO_USE_IE_OFFLINE_SUPPORT",
    "BFO_USE_IE_STATUSBAR",
    "BFO_USE_IE_TOOLBAR",
    "BHID_AssociationArray",
    "BHID_DataObject",
    "BHID_EnumAssocHandlers",
    "BHID_EnumItems",
    "BHID_FilePlaceholder",
    "BHID_Filter",
    "BHID_LinkTargetItem",
    "BHID_PropertyStore",
    "BHID_RandomAccessStream",
    "BHID_SFObject",
    "BHID_SFUIObject",
    "BHID_SFViewObject",
    "BHID_Storage",
    "BHID_StorageEnum",
    "BHID_StorageItem",
    "BHID_Stream",
    "BHID_ThumbnailHandler",
    "BHID_Transfer",
    "BIF_BROWSEFILEJUNCTIONS",
    "BIF_BROWSEFORCOMPUTER",
    "BIF_BROWSEFORPRINTER",
    "BIF_BROWSEINCLUDEFILES",
    "BIF_BROWSEINCLUDEURLS",
    "BIF_DONTGOBELOWDOMAIN",
    "BIF_EDITBOX",
    "BIF_NEWDIALOGSTYLE",
    "BIF_NONEWFOLDERBUTTON",
    "BIF_NOTRANSLATETARGETS",
    "BIF_PREFER_INTERNET_SHORTCUT",
    "BIF_RETURNFSANCESTORS",
    "BIF_RETURNONLYFSDIRS",
    "BIF_SHAREABLE",
    "BIF_STATUSTEXT",
    "BIF_UAHINT",
    "BIF_VALIDATE",
    "BIND_INTERRUPTABLE",
    "BMICON_LARGE",
    "BMICON_SMALL",
    "BNE_Button1Clicked",
    "BNE_Button2Clicked",
    "BNE_Closed",
    "BNE_Dismissed",
    "BNE_Hovered",
    "BNE_Rendered",
    "BNSTATE",
    "BNS_BEGIN_NAVIGATE",
    "BNS_NAVIGATE",
    "BNS_NORMAL",
    "BROWSEINFOA",
    "BROWSEINFOW",
    "BSF_CANMAXIMIZE",
    "BSF_DELEGATEDNAVIGATION",
    "BSF_DONTSHOWNAVCANCELPAGE",
    "BSF_FEEDNAVIGATION",
    "BSF_FEEDSUBSCRIBED",
    "BSF_HTMLNAVCANCELED",
    "BSF_MERGEDMENUS",
    "BSF_NAVNOHISTORY",
    "BSF_NOLOCALFILEWARNING",
    "BSF_REGISTERASDROPTARGET",
    "BSF_RESIZABLE",
    "BSF_SETNAVIGATABLECODEPAGE",
    "BSF_THEATERMODE",
    "BSF_TOPBROWSER",
    "BSF_TRUSTEDFORACTIVEX",
    "BSF_UISETBYAUTOMATION",
    "BSID_BANDADDED",
    "BSID_BANDREMOVED",
    "BSIM_STATE",
    "BSIM_STYLE",
    "BSIS_ALWAYSGRIPPER",
    "BSIS_AUTOGRIPPER",
    "BSIS_FIXEDORDER",
    "BSIS_LEFTALIGN",
    "BSIS_LOCKED",
    "BSIS_NOCAPTION",
    "BSIS_NOCONTEXTMENU",
    "BSIS_NODROPTARGET",
    "BSIS_NOGRIPPER",
    "BSIS_PREFERNOLINEBREAK",
    "BSIS_PRESERVEORDERDURINGLAYOUT",
    "BSIS_SINGLECLICK",
    "BSSF_NOTITLE",
    "BSSF_UNDELETEABLE",
    "BSSF_VISIBLE",
    "BUFFLEN",
    "BrowserNavConstants",
    "BrowserNavConstants_navAllowAutosearch",
    "BrowserNavConstants_navBlockRedirectsXDomain",
    "BrowserNavConstants_navBrowserBar",
    "BrowserNavConstants_navDeferUnload",
    "BrowserNavConstants_navEnforceRestricted",
    "BrowserNavConstants_navHomepageNavigate",
    "BrowserNavConstants_navHostNavigation",
    "BrowserNavConstants_navHyperlink",
    "BrowserNavConstants_navKeepWordWheelText",
    "BrowserNavConstants_navNewWindowsManaged",
    "BrowserNavConstants_navNoHistory",
    "BrowserNavConstants_navNoReadFromCache",
    "BrowserNavConstants_navNoWriteToCache",
    "BrowserNavConstants_navOpenInBackgroundTab",
    "BrowserNavConstants_navOpenInNewTab",
    "BrowserNavConstants_navOpenInNewWindow",
    "BrowserNavConstants_navOpenNewForegroundTab",
    "BrowserNavConstants_navRefresh",
    "BrowserNavConstants_navReserved1",
    "BrowserNavConstants_navReserved2",
    "BrowserNavConstants_navReserved3",
    "BrowserNavConstants_navReserved4",
    "BrowserNavConstants_navReserved5",
    "BrowserNavConstants_navReserved6",
    "BrowserNavConstants_navReserved7",
    "BrowserNavConstants_navSpeculative",
    "BrowserNavConstants_navSuggestNewTab",
    "BrowserNavConstants_navSuggestNewWindow",
    "BrowserNavConstants_navTravelLogScreenshot",
    "BrowserNavConstants_navTrustedForActiveX",
    "BrowserNavConstants_navUntrustedForDownload",
    "BrowserNavConstants_navVirtualTab",
    "CABINETSTATE",
    "CABINETSTATE_VERSION",
    "CAMERAROLL_E_NO_DOWNSAMPLING_REQUIRED",
    "CATEGORYINFO_FLAGS",
    "CATEGORY_INFO",
    "CATID_BrowsableShellExt",
    "CATID_BrowseInPlace",
    "CATID_CommBand",
    "CATID_DeskBand",
    "CATID_FilePlaceholderMergeHandler",
    "CATID_InfoBand",
    "CATID_LocationFactory",
    "CATID_LocationProvider",
    "CATID_SearchableApplication",
    "CATINFO_COLLAPSED",
    "CATINFO_EXPANDED",
    "CATINFO_HIDDEN",
    "CATINFO_NOHEADER",
    "CATINFO_NOHEADERCOUNT",
    "CATINFO_NORMAL",
    "CATINFO_NOTCOLLAPSIBLE",
    "CATINFO_SEPARATE_IMAGES",
    "CATINFO_SHOWEMPTY",
    "CATINFO_SUBSETTED",
    "CATSORT_DEFAULT",
    "CATSORT_FLAGS",
    "CATSORT_NAME",
    "CDB2GVF_ADDSHIELD",
    "CDB2GVF_ALLOWPREVIEWPANE",
    "CDB2GVF_ISFILESAVE",
    "CDB2GVF_ISFOLDERPICKER",
    "CDB2GVF_NOINCLUDEITEM",
    "CDB2GVF_NOSELECTVERB",
    "CDB2GVF_SHOWALLFILES",
    "CDB2N_CONTEXTMENU_DONE",
    "CDB2N_CONTEXTMENU_START",
    "CDBE_RET_DEFAULT",
    "CDBE_RET_DONTRUNOTHEREXTS",
    "CDBE_RET_STOPWIZARD",
    "CDBE_TYPE_ALL",
    "CDBE_TYPE_DATA",
    "CDBE_TYPE_MUSIC",
    "CDBOSC_KILLFOCUS",
    "CDBOSC_RENAME",
    "CDBOSC_SELCHANGE",
    "CDBOSC_SETFOCUS",
    "CDBOSC_STATECHANGE",
    "CDBURNINGEXTENSIONRET",
    "CDBurn",
    "CDCONTROLSTATEF",
    "CDCS_ENABLED",
    "CDCS_ENABLEDVISIBLE",
    "CDCS_INACTIVE",
    "CDCS_VISIBLE",
    "CDefFolderMenu_Create2",
    "CFSTR_AUTOPLAY_SHELLIDLISTS",
    "CFSTR_DROPDESCRIPTION",
    "CFSTR_FILECONTENTS",
    "CFSTR_FILEDESCRIPTOR",
    "CFSTR_FILEDESCRIPTORA",
    "CFSTR_FILEDESCRIPTORW",
    "CFSTR_FILENAME",
    "CFSTR_FILENAMEA",
    "CFSTR_FILENAMEMAP",
    "CFSTR_FILENAMEMAPA",
    "CFSTR_FILENAMEMAPW",
    "CFSTR_FILENAMEW",
    "CFSTR_FILE_ATTRIBUTES_ARRAY",
    "CFSTR_INDRAGLOOP",
    "CFSTR_INETURL",
    "CFSTR_INETURLA",
    "CFSTR_INETURLW",
    "CFSTR_INVOKECOMMAND_DROPPARAM",
    "CFSTR_LOGICALPERFORMEDDROPEFFECT",
    "CFSTR_MOUNTEDVOLUME",
    "CFSTR_NETRESOURCES",
    "CFSTR_PASTESUCCEEDED",
    "CFSTR_PERFORMEDDROPEFFECT",
    "CFSTR_PERSISTEDDATAOBJECT",
    "CFSTR_PREFERREDDROPEFFECT",
    "CFSTR_PRINTERGROUP",
    "CFSTR_SHELLDROPHANDLER",
    "CFSTR_SHELLIDLIST",
    "CFSTR_SHELLIDLISTOFFSET",
    "CFSTR_SHELLURL",
    "CFSTR_TARGETCLSID",
    "CFSTR_UNTRUSTEDDRAGDROP",
    "CFSTR_ZONEIDENTIFIER",
    "CGID_DefView",
    "CGID_Explorer",
    "CGID_ExplorerBarDoc",
    "CGID_MENUDESKBAR",
    "CGID_ShellDocView",
    "CGID_ShellServiceObject",
    "CGID_ShortCut",
    "CIDA",
    "CIDLData_CreateFromIDArray",
    "CIE4ConnectionPoint",
    "CLOSEPROPS_DISCARD",
    "CLOSEPROPS_NONE",
    "CLSID_ACLCustomMRU",
    "CLSID_ACLHistory",
    "CLSID_ACLMRU",
    "CLSID_ACLMulti",
    "CLSID_ACListISF",
    "CLSID_ActiveDesktop",
    "CLSID_AutoComplete",
    "CLSID_CAnchorBrowsePropertyPage",
    "CLSID_CDocBrowsePropertyPage",
    "CLSID_CFSIconOverlayManager",
    "CLSID_CImageBrowsePropertyPage",
    "CLSID_CURLSearchHook",
    "CLSID_CUrlHistory",
    "CLSID_ControlPanel",
    "CLSID_DarwinAppPublisher",
    "CLSID_DocHostUIHandler",
    "CLSID_DragDropHelper",
    "CLSID_FileTypes",
    "CLSID_FolderItemsMultiLevel",
    "CLSID_FolderShortcut",
    "CLSID_HWShellExecute",
    "CLSID_ISFBand",
    "CLSID_Internet",
    "CLSID_InternetButtons",
    "CLSID_InternetShortcut",
    "CLSID_LinkColumnProvider",
    "CLSID_MSOButtons",
    "CLSID_MenuBand",
    "CLSID_MenuBandSite",
    "CLSID_MenuToolbarBase",
    "CLSID_MyComputer",
    "CLSID_MyDocuments",
    "CLSID_NetworkDomain",
    "CLSID_NetworkServer",
    "CLSID_NetworkShare",
    "CLSID_NewMenu",
    "CLSID_Printers",
    "CLSID_ProgressDialog",
    "CLSID_QueryAssociations",
    "CLSID_QuickLinks",
    "CLSID_RecycleBin",
    "CLSID_ShellFldSetExt",
    "CLSID_ShellThumbnailDiskCache",
    "CLSID_ToolbarExtButtons",
    "CMDID_INTSHORTCUTCREATE",
    "CMDSTR_NEWFOLDER",
    "CMDSTR_NEWFOLDERA",
    "CMDSTR_NEWFOLDERW",
    "CMDSTR_VIEWDETAILS",
    "CMDSTR_VIEWDETAILSA",
    "CMDSTR_VIEWDETAILSW",
    "CMDSTR_VIEWLIST",
    "CMDSTR_VIEWLISTA",
    "CMDSTR_VIEWLISTW",
    "CMF_ASYNCVERBSTATE",
    "CMF_CANRENAME",
    "CMF_DEFAULTONLY",
    "CMF_DISABLEDVERBS",
    "CMF_DONOTPICKDEFAULT",
    "CMF_EXPLORE",
    "CMF_EXTENDEDVERBS",
    "CMF_INCLUDESTATIC",
    "CMF_ITEMMENU",
    "CMF_NODEFAULT",
    "CMF_NORMAL",
    "CMF_NOVERBS",
    "CMF_OPTIMIZEFORINVOKE",
    "CMF_RESERVED",
    "CMF_SYNCCASCADEMENU",
    "CMF_VERBSONLY",
    "CMIC_MASK_CONTROL_DOWN",
    "CMIC_MASK_PTINVOKE",
    "CMIC_MASK_SHIFT_DOWN",
    "CMINVOKECOMMANDINFO",
    "CMINVOKECOMMANDINFOEX",
    "CMINVOKECOMMANDINFOEX_REMOTE",
    "CM_COLUMNINFO",
    "CM_ENUM_ALL",
    "CM_ENUM_FLAGS",
    "CM_ENUM_VISIBLE",
    "CM_MASK",
    "CM_MASK_DEFAULTWIDTH",
    "CM_MASK_IDEALWIDTH",
    "CM_MASK_NAME",
    "CM_MASK_STATE",
    "CM_MASK_WIDTH",
    "CM_SET_WIDTH_VALUE",
    "CM_STATE",
    "CM_STATE_ALWAYSVISIBLE",
    "CM_STATE_FIXEDWIDTH",
    "CM_STATE_NONE",
    "CM_STATE_NOSORTBYFOLDERNESS",
    "CM_STATE_VISIBLE",
    "CM_WIDTH_AUTOSIZE",
    "CM_WIDTH_USEDEFAULT",
    "COMPONENT_DEFAULT_LEFT",
    "COMPONENT_DEFAULT_TOP",
    "COMPONENT_TOP",
    "COMP_ELEM_CHECKED",
    "COMP_ELEM_CURITEMSTATE",
    "COMP_ELEM_DIRTY",
    "COMP_ELEM_FRIENDLYNAME",
    "COMP_ELEM_NOSCROLL",
    "COMP_ELEM_ORIGINAL_CSI",
    "COMP_ELEM_POS_LEFT",
    "COMP_ELEM_POS_TOP",
    "COMP_ELEM_POS_ZINDEX",
    "COMP_ELEM_RESTORED_CSI",
    "COMP_ELEM_SIZE_HEIGHT",
    "COMP_ELEM_SIZE_WIDTH",
    "COMP_ELEM_SOURCE",
    "COMP_ELEM_SUBSCRIBEDURL",
    "COMP_ELEM_TYPE",
    "COMP_TYPE_CFHTML",
    "COMP_TYPE_CONTROL",
    "COMP_TYPE_HTMLDOC",
    "COMP_TYPE_MAX",
    "COMP_TYPE_PICTURE",
    "COMP_TYPE_WEBSITE",
    "CONFIRM_CONFLICT_ITEM",
    "CONFIRM_CONFLICT_RESULT_INFO",
    "CONFLICT_RESOLUTION_CLSID_KEY",
    "COPYENGINE_E_ACCESSDENIED_READONLY",
    "COPYENGINE_E_ACCESS_DENIED_DEST",
    "COPYENGINE_E_ACCESS_DENIED_SRC",
    "COPYENGINE_E_ALREADY_EXISTS_FOLDER",
    "COPYENGINE_E_ALREADY_EXISTS_NORMAL",
    "COPYENGINE_E_ALREADY_EXISTS_READONLY",
    "COPYENGINE_E_ALREADY_EXISTS_SYSTEM",
    "COPYENGINE_E_BLOCKED_BY_DLP_POLICY",
    "COPYENGINE_E_BLOCKED_BY_EDP_FOR_REMOVABLE_DRIVE",
    "COPYENGINE_E_BLOCKED_BY_EDP_POLICY",
    "COPYENGINE_E_CANCELLED",
    "COPYENGINE_E_CANNOT_MOVE_FROM_RECYCLE_BIN",
    "COPYENGINE_E_CANNOT_MOVE_SHARED_FOLDER",
    "COPYENGINE_E_CANT_REACH_SOURCE",
    "COPYENGINE_E_DEST_IS_RO_CD",
    "COPYENGINE_E_DEST_IS_RO_DVD",
    "COPYENGINE_E_DEST_IS_RW_CD",
    "COPYENGINE_E_DEST_IS_RW_DVD",
    "COPYENGINE_E_DEST_IS_R_CD",
    "COPYENGINE_E_DEST_IS_R_DVD",
    "COPYENGINE_E_DEST_SAME_TREE",
    "COPYENGINE_E_DEST_SUBTREE",
    "COPYENGINE_E_DIFF_DIR",
    "COPYENGINE_E_DIR_NOT_EMPTY",
    "COPYENGINE_E_DISK_FULL",
    "COPYENGINE_E_DISK_FULL_CLEAN",
    "COPYENGINE_E_EA_LOSS",
    "COPYENGINE_E_EA_NOT_SUPPORTED",
    "COPYENGINE_E_ENCRYPTION_LOSS",
    "COPYENGINE_E_FAT_MAX_IN_ROOT",
    "COPYENGINE_E_FILE_IS_FLD_DEST",
    "COPYENGINE_E_FILE_TOO_LARGE",
    "COPYENGINE_E_FLD_IS_FILE_DEST",
    "COPYENGINE_E_INTERNET_ITEM_STORAGE_PROVIDER_ERROR",
    "COPYENGINE_E_INTERNET_ITEM_STORAGE_PROVIDER_PAUSED",
    "COPYENGINE_E_INTERNET_ITEM_UNAVAILABLE",
    "COPYENGINE_E_INVALID_FILES_DEST",
    "COPYENGINE_E_INVALID_FILES_SRC",
    "COPYENGINE_E_MANY_SRC_1_DEST",
    "COPYENGINE_E_NET_DISCONNECT_DEST",
    "COPYENGINE_E_NET_DISCONNECT_SRC",
    "COPYENGINE_E_NEWFILE_NAME_TOO_LONG",
    "COPYENGINE_E_NEWFOLDER_NAME_TOO_LONG",
    "COPYENGINE_E_PATH_NOT_FOUND_DEST",
    "COPYENGINE_E_PATH_NOT_FOUND_SRC",
    "COPYENGINE_E_PATH_TOO_DEEP_DEST",
    "COPYENGINE_E_PATH_TOO_DEEP_SRC",
    "COPYENGINE_E_PROPERTIES_LOSS",
    "COPYENGINE_E_PROPERTY_LOSS",
    "COPYENGINE_E_RECYCLE_BIN_NOT_FOUND",
    "COPYENGINE_E_RECYCLE_FORCE_NUKE",
    "COPYENGINE_E_RECYCLE_PATH_TOO_LONG",
    "COPYENGINE_E_RECYCLE_SIZE_TOO_BIG",
    "COPYENGINE_E_RECYCLE_UNKNOWN_ERROR",
    "COPYENGINE_E_REDIRECTED_TO_WEBPAGE",
    "COPYENGINE_E_REMOVABLE_FULL",
    "COPYENGINE_E_REQUIRES_EDP_CONSENT",
    "COPYENGINE_E_REQUIRES_EDP_CONSENT_FOR_REMOVABLE_DRIVE",
    "COPYENGINE_E_REQUIRES_ELEVATION",
    "COPYENGINE_E_RMS_BLOCKED_BY_EDP_FOR_REMOVABLE_DRIVE",
    "COPYENGINE_E_RMS_REQUIRES_EDP_CONSENT_FOR_REMOVABLE_DRIVE",
    "COPYENGINE_E_ROOT_DIR_DEST",
    "COPYENGINE_E_ROOT_DIR_SRC",
    "COPYENGINE_E_SAME_FILE",
    "COPYENGINE_E_SERVER_BAD_FILE_TYPE",
    "COPYENGINE_E_SHARING_VIOLATION_DEST",
    "COPYENGINE_E_SHARING_VIOLATION_SRC",
    "COPYENGINE_E_SILENT_FAIL_BY_DLP_POLICY",
    "COPYENGINE_E_SRC_IS_RO_CD",
    "COPYENGINE_E_SRC_IS_RO_DVD",
    "COPYENGINE_E_SRC_IS_RW_CD",
    "COPYENGINE_E_SRC_IS_RW_DVD",
    "COPYENGINE_E_SRC_IS_R_CD",
    "COPYENGINE_E_SRC_IS_R_DVD",
    "COPYENGINE_E_STREAM_LOSS",
    "COPYENGINE_E_USER_CANCELLED",
    "COPYENGINE_E_WARNED_BY_DLP_POLICY",
    "COPYENGINE_S_ALREADY_DONE",
    "COPYENGINE_S_CLOSE_PROGRAM",
    "COPYENGINE_S_COLLISIONRESOLVED",
    "COPYENGINE_S_DONT_PROCESS_CHILDREN",
    "COPYENGINE_S_KEEP_BOTH",
    "COPYENGINE_S_MERGE",
    "COPYENGINE_S_NOT_HANDLED",
    "COPYENGINE_S_PENDING",
    "COPYENGINE_S_PROGRESS_PAUSE",
    "COPYENGINE_S_USER_IGNORED",
    "COPYENGINE_S_USER_RETRY",
    "COPYENGINE_S_YES",
    "CPAO_EMPTY_CONNECTED",
    "CPAO_EMPTY_LOCAL",
    "CPAO_NONE",
    "CPCFO_ENABLE_PASSWORD_REVEAL",
    "CPCFO_ENABLE_TOUCH_KEYBOARD_AUTO_INVOKE",
    "CPCFO_IS_EMAIL_ADDRESS",
    "CPCFO_NONE",
    "CPCFO_NUMBERS_ONLY",
    "CPCFO_SHOW_ENGLISH_KEYBOARD",
    "CPFG_CREDENTIAL_PROVIDER_LABEL",
    "CPFG_CREDENTIAL_PROVIDER_LOGO",
    "CPFG_LOGON_PASSWORD",
    "CPFG_LOGON_USERNAME",
    "CPFG_SMARTCARD_PIN",
    "CPFG_SMARTCARD_USERNAME",
    "CPFG_STANDALONE_SUBMIT_BUTTON",
    "CPFG_STYLE_LINK_AS_BUTTON",
    "CPFIS_DISABLED",
    "CPFIS_FOCUSED",
    "CPFIS_NONE",
    "CPFIS_READONLY",
    "CPFS_DISPLAY_IN_BOTH",
    "CPFS_DISPLAY_IN_DESELECTED_TILE",
    "CPFS_DISPLAY_IN_SELECTED_TILE",
    "CPFS_HIDDEN",
    "CPFT_CHECKBOX",
    "CPFT_COMBOBOX",
    "CPFT_COMMAND_LINK",
    "CPFT_EDIT_TEXT",
    "CPFT_INVALID",
    "CPFT_LARGE_TEXT",
    "CPFT_PASSWORD_TEXT",
    "CPFT_SMALL_TEXT",
    "CPFT_SUBMIT_BUTTON",
    "CPFT_TILE_IMAGE",
    "CPGSR_NO_CREDENTIAL_FINISHED",
    "CPGSR_NO_CREDENTIAL_NOT_FINISHED",
    "CPGSR_RETURN_CREDENTIAL_FINISHED",
    "CPGSR_RETURN_NO_CREDENTIAL_FINISHED",
    "CPLINFO",
    "CPLPAGE_DISPLAY_BACKGROUND",
    "CPLPAGE_KEYBOARD_SPEED",
    "CPLPAGE_MOUSE_BUTTONS",
    "CPLPAGE_MOUSE_PTRMOTION",
    "CPLPAGE_MOUSE_WHEEL",
    "CPL_DBLCLK",
    "CPL_DYNAMIC_RES",
    "CPL_EXIT",
    "CPL_GETCOUNT",
    "CPL_INIT",
    "CPL_INQUIRE",
    "CPL_NEWINQUIRE",
    "CPL_SELECT",
    "CPL_SETUP",
    "CPL_STARTWPARMS",
    "CPL_STARTWPARMSA",
    "CPL_STARTWPARMSW",
    "CPL_STOP",
    "CPSI_ERROR",
    "CPSI_NONE",
    "CPSI_SUCCESS",
    "CPSI_WARNING",
    "CPUS_CHANGE_PASSWORD",
    "CPUS_CREDUI",
    "CPUS_INVALID",
    "CPUS_LOGON",
    "CPUS_PLAP",
    "CPUS_UNLOCK_WORKSTATION",
    "CPVIEW",
    "CPVIEW_ALLITEMS",
    "CPVIEW_CATEGORY",
    "CPVIEW_CLASSIC",
    "CPVIEW_HOME",
    "CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS",
    "CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS",
    "CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION",
    "CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR",
    "CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE",
    "CREDENTIAL_PROVIDER_FIELD_STATE",
    "CREDENTIAL_PROVIDER_FIELD_TYPE",
    "CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE",
    "CREDENTIAL_PROVIDER_NO_DEFAULT",
    "CREDENTIAL_PROVIDER_STATUS_ICON",
    "CREDENTIAL_PROVIDER_USAGE_SCENARIO",
    "CSC_NAVIGATEBACK",
    "CSC_NAVIGATEFORWARD",
    "CSC_UPDATECOMMANDS",
    "CSFV",
    "CSIDL_ADMINTOOLS",
    "CSIDL_ALTSTARTUP",
    "CSIDL_APPDATA",
    "CSIDL_BITBUCKET",
    "CSIDL_CDBURN_AREA",
    "CSIDL_COMMON_ADMINTOOLS",
    "CSIDL_COMMON_ALTSTARTUP",
    "CSIDL_COMMON_APPDATA",
    "CSIDL_COMMON_DESKTOPDIRECTORY",
    "CSIDL_COMMON_DOCUMENTS",
    "CSIDL_COMMON_FAVORITES",
    "CSIDL_COMMON_MUSIC",
    "CSIDL_COMMON_OEM_LINKS",
    "CSIDL_COMMON_PICTURES",
    "CSIDL_COMMON_PROGRAMS",
    "CSIDL_COMMON_STARTMENU",
    "CSIDL_COMMON_STARTUP",
    "CSIDL_COMMON_TEMPLATES",
    "CSIDL_COMMON_VIDEO",
    "CSIDL_COMPUTERSNEARME",
    "CSIDL_CONNECTIONS",
    "CSIDL_CONTROLS",
    "CSIDL_COOKIES",
    "CSIDL_DESKTOP",
    "CSIDL_DESKTOPDIRECTORY",
    "CSIDL_DRIVES",
    "CSIDL_FAVORITES",
    "CSIDL_FLAG_CREATE",
    "CSIDL_FLAG_DONT_UNEXPAND",
    "CSIDL_FLAG_DONT_VERIFY",
    "CSIDL_FLAG_MASK",
    "CSIDL_FLAG_NO_ALIAS",
    "CSIDL_FLAG_PER_USER_INIT",
    "CSIDL_FLAG_PFTI_TRACKTARGET",
    "CSIDL_FONTS",
    "CSIDL_HISTORY",
    "CSIDL_INTERNET",
    "CSIDL_INTERNET_CACHE",
    "CSIDL_LOCAL_APPDATA",
    "CSIDL_MYDOCUMENTS",
    "CSIDL_MYMUSIC",
    "CSIDL_MYPICTURES",
    "CSIDL_MYVIDEO",
    "CSIDL_NETHOOD",
    "CSIDL_NETWORK",
    "CSIDL_PERSONAL",
    "CSIDL_PRINTERS",
    "CSIDL_PRINTHOOD",
    "CSIDL_PROFILE",
    "CSIDL_PROGRAMS",
    "CSIDL_PROGRAM_FILES",
    "CSIDL_PROGRAM_FILESX86",
    "CSIDL_PROGRAM_FILES_COMMON",
    "CSIDL_PROGRAM_FILES_COMMONX86",
    "CSIDL_RECENT",
    "CSIDL_RESOURCES",
    "CSIDL_RESOURCES_LOCALIZED",
    "CSIDL_SENDTO",
    "CSIDL_STARTMENU",
    "CSIDL_STARTUP",
    "CSIDL_SYSTEM",
    "CSIDL_SYSTEMX86",
    "CSIDL_TEMPLATES",
    "CSIDL_WINDOWS",
    "CScriptErrorList",
    "CTF_COINIT",
    "CTF_COINIT_MTA",
    "CTF_COINIT_STA",
    "CTF_FREELIBANDEXIT",
    "CTF_INHERITWOW64",
    "CTF_INSIST",
    "CTF_KEYBOARD_LOCALE",
    "CTF_NOADDREFLIB",
    "CTF_OLEINITIALIZE",
    "CTF_PROCESS_REF",
    "CTF_REF_COUNTED",
    "CTF_THREAD_REF",
    "CTF_UNUSED",
    "CTF_WAIT_ALLOWCOM",
    "CTF_WAIT_NO_REENTRANCY",
    "ChrCmpIA",
    "ChrCmpIW",
    "ColorAdjustLuma",
    "ColorHLSToRGB",
    "ColorRGBToHLS",
    "CommandLineToArgvW",
    "CommandStateChangeConstants",
    "ConflictFolder",
    "ConnectToConnectionPoint",
    "CreateProfile",
    "DAD_AutoScroll",
    "DAD_DragEnterEx",
    "DAD_DragEnterEx2",
    "DAD_DragLeave",
    "DAD_DragMove",
    "DAD_SetDragImage",
    "DAD_ShowDragImage",
    "DATABLOCK_HEADER",
    "DATAOBJ_GET_ITEM_FLAGS",
    "DBCID_CLSIDOFBAR",
    "DBCID_EMPTY",
    "DBCID_GETBAR",
    "DBCID_ONDRAG",
    "DBCID_RESIZE",
    "DBCID_UPDATESIZE",
    "DBC_GS_IDEAL",
    "DBC_GS_SIZEDOWN",
    "DBC_HIDE",
    "DBC_SHOW",
    "DBC_SHOWOBSCURE",
    "DBID_BANDINFOCHANGED",
    "DBID_DELAYINIT",
    "DBID_FINISHINIT",
    "DBID_MAXIMIZEBAND",
    "DBID_PERMITAUTOHIDE",
    "DBID_PUSHCHEVRON",
    "DBID_SETWINDOWTHEME",
    "DBID_SHOWONLY",
    "DBIF_VIEWMODE_FLOATING",
    "DBIF_VIEWMODE_NORMAL",
    "DBIF_VIEWMODE_TRANSPARENT",
    "DBIF_VIEWMODE_VERTICAL",
    "DBIMF_ADDTOFRONT",
    "DBIMF_ALWAYSGRIPPER",
    "DBIMF_BKCOLOR",
    "DBIMF_BREAK",
    "DBIMF_DEBOSSED",
    "DBIMF_FIXED",
    "DBIMF_FIXEDBMP",
    "DBIMF_NOGRIPPER",
    "DBIMF_NOMARGINS",
    "DBIMF_NORMAL",
    "DBIMF_TOPALIGN",
    "DBIMF_UNDELETEABLE",
    "DBIMF_USECHEVRON",
    "DBIMF_VARIABLEHEIGHT",
    "DBIM_ACTUAL",
    "DBIM_BKCOLOR",
    "DBIM_INTEGRAL",
    "DBIM_MAXSIZE",
    "DBIM_MINSIZE",
    "DBIM_MODEFLAGS",
    "DBIM_TITLE",
    "DBPC_SELECTFIRST",
    "DEFAULTSAVEFOLDERTYPE",
    "DEFAULT_FOLDER_MENU_RESTRICTIONS",
    "DEFCONTEXTMENU",
    "DEFSHAREID_PUBLIC",
    "DEFSHAREID_USERS",
    "DEF_SHARE_ID",
    "DELEGATEITEMID",
    "DESKBANDCID",
    "DESKBANDINFO",
    "DESKTOP_SLIDESHOW_DIRECTION",
    "DESKTOP_SLIDESHOW_OPTIONS",
    "DESKTOP_SLIDESHOW_STATE",
    "DESKTOP_WALLPAPER_POSITION",
    "DETAILSINFO",
    "DEVICE_IMMERSIVE",
    "DEVICE_PRIMARY",
    "DFConstraint",
    "DFMICS",
    "DFMR_DEFAULT",
    "DFMR_NO_ASYNC_VERBS",
    "DFMR_NO_NATIVECPU_VERBS",
    "DFMR_NO_NONWOW_VERBS",
    "DFMR_NO_RESOURCE_VERBS",
    "DFMR_NO_STATIC_VERBS",
    "DFMR_OPTIN_HANDLERS_ONLY",
    "DFMR_RESOURCE_AND_FOLDER_VERBS_ONLY",
    "DFMR_STATIC_VERBS_ONLY",
    "DFMR_USE_SPECIFIED_HANDLERS",
    "DFMR_USE_SPECIFIED_VERBS",
    "DFM_CMD",
    "DFM_CMD_COPY",
    "DFM_CMD_DELETE",
    "DFM_CMD_LINK",
    "DFM_CMD_MODALPROP",
    "DFM_CMD_MOVE",
    "DFM_CMD_NEWFOLDER",
    "DFM_CMD_PASTE",
    "DFM_CMD_PASTELINK",
    "DFM_CMD_PASTESPECIAL",
    "DFM_CMD_PROPERTIES",
    "DFM_CMD_RENAME",
    "DFM_CMD_VIEWDETAILS",
    "DFM_CMD_VIEWLIST",
    "DFM_GETDEFSTATICID",
    "DFM_GETHELPTEXT",
    "DFM_GETHELPTEXTW",
    "DFM_GETVERBA",
    "DFM_GETVERBW",
    "DFM_INVOKECOMMAND",
    "DFM_INVOKECOMMANDEX",
    "DFM_MAPCOMMANDNAME",
    "DFM_MERGECONTEXTMENU",
    "DFM_MERGECONTEXTMENU_BOTTOM",
    "DFM_MERGECONTEXTMENU_TOP",
    "DFM_MESSAGE_ID",
    "DFM_MODIFYQCMFLAGS",
    "DFM_VALIDATECMD",
    "DFM_WM_DRAWITEM",
    "DFM_WM_INITMENUPOPUP",
    "DFM_WM_MEASUREITEM",
    "DISPID_BEGINDRAG",
    "DISPID_CHECKSTATECHANGED",
    "DISPID_COLUMNSCHANGED",
    "DISPID_CONTENTSCHANGED",
    "DISPID_CTRLMOUSEWHEEL",
    "DISPID_DEFAULTVERBINVOKED",
    "DISPID_ENTERPRESSED",
    "DISPID_ENTERPRISEIDCHANGED",
    "DISPID_EXPLORERWINDOWREADY",
    "DISPID_FILELISTENUMDONE",
    "DISPID_FILTERINVOKED",
    "DISPID_FOCUSCHANGED",
    "DISPID_FOLDERCHANGED",
    "DISPID_IADCCTL_DEFAULTCAT",
    "DISPID_IADCCTL_DIRTY",
    "DISPID_IADCCTL_FORCEX86",
    "DISPID_IADCCTL_ONDOMAIN",
    "DISPID_IADCCTL_PUBCAT",
    "DISPID_IADCCTL_SHOWPOSTSETUP",
    "DISPID_IADCCTL_SORT",
    "DISPID_ICONSIZECHANGED",
    "DISPID_INITIALENUMERATIONDONE",
    "DISPID_NOITEMSTATE_CHANGED",
    "DISPID_ORDERCHANGED",
    "DISPID_SEARCHCOMMAND_ABORT",
    "DISPID_SEARCHCOMMAND_COMPLETE",
    "DISPID_SEARCHCOMMAND_ERROR",
    "DISPID_SEARCHCOMMAND_PROGRESSTEXT",
    "DISPID_SEARCHCOMMAND_RESTORE",
    "DISPID_SEARCHCOMMAND_START",
    "DISPID_SEARCHCOMMAND_UPDATE",
    "DISPID_SELECTEDITEMCHANGED",
    "DISPID_SELECTIONCHANGED",
    "DISPID_SORTDONE",
    "DISPID_UPDATEIMAGE",
    "DISPID_VERBINVOKED",
    "DISPID_VIEWMODECHANGED",
    "DISPID_VIEWPAINTDONE",
    "DISPID_WORDWHEELEDITED",
    "DISPLAY_DEVICE_TYPE",
    "DI_GETDRAGIMAGE",
    "DLG_SCRNSAVECONFIGURE",
    "DLLGETVERSIONPROC",
    "DLLVERSIONINFO",
    "DLLVERSIONINFO2",
    "DLLVER_BUILD_MASK",
    "DLLVER_MAJOR_MASK",
    "DLLVER_MINOR_MASK",
    "DLLVER_PLATFORM_NT",
    "DLLVER_PLATFORM_WINDOWS",
    "DLLVER_QFE_MASK",
    "DOGIF_DEFAULT",
    "DOGIF_NO_HDROP",
    "DOGIF_NO_URL",
    "DOGIF_ONLY_IF_ONE",
    "DOGIF_TRAVERSE_LINK",
    "DRAGINFOA",
    "DRAGINFOW",
    "DROPDESCRIPTION",
    "DROPFILES",
    "DROPIMAGETYPE",
    "DROPIMAGE_COPY",
    "DROPIMAGE_INVALID",
    "DROPIMAGE_LABEL",
    "DROPIMAGE_LINK",
    "DROPIMAGE_MOVE",
    "DROPIMAGE_NOIMAGE",
    "DROPIMAGE_NONE",
    "DROPIMAGE_WARNING",
    "DSD_BACKWARD",
    "DSD_FORWARD",
    "DSFT_DETECT",
    "DSFT_PRIVATE",
    "DSFT_PUBLIC",
    "DSH_ALLOWDROPDESCRIPTIONTEXT",
    "DSH_FLAGS",
    "DSO_SHUFFLEIMAGES",
    "DSS_DISABLED_BY_REMOTE_SESSION",
    "DSS_ENABLED",
    "DSS_SLIDESHOW",
    "DShellFolderViewEvents",
    "DShellNameSpaceEvents",
    "DShellWindowsEvents",
    "DVASPECT_COPY",
    "DVASPECT_LINK",
    "DVASPECT_SHORTNAME",
    "DWFAF_AUTOHIDE",
    "DWFAF_GROUP1",
    "DWFAF_GROUP2",
    "DWFAF_HIDDEN",
    "DWFRF_DELETECONFIGDATA",
    "DWFRF_NORMAL",
    "DWPOS_CENTER",
    "DWPOS_FILL",
    "DWPOS_FIT",
    "DWPOS_SPAN",
    "DWPOS_STRETCH",
    "DWPOS_TILE",
    "DWebBrowserEvents",
    "DWebBrowserEvents2",
    "DefFolderMenu",
    "DefSubclassProc",
    "DeleteProfileA",
    "DeleteProfileW",
    "DesktopGadget",
    "DesktopWallpaper",
    "DestinationList",
    "DoEnvironmentSubstA",
    "DoEnvironmentSubstW",
    "DocPropShellExtension",
    "DragAcceptFiles",
    "DragFinish",
    "DragQueryFileA",
    "DragQueryFileW",
    "DragQueryPoint",
    "DriveSizeCategorizer",
    "DriveType",
    "DriveTypeCategorizer",
    "DuplicateIcon",
    "EBF_NODROPTARGET",
    "EBF_NONE",
    "EBF_SELECTFROMDATAOBJECT",
    "EBO_ALWAYSNAVIGATE",
    "EBO_HTMLSHAREPOINTVIEW",
    "EBO_NAVIGATEONCE",
    "EBO_NOBORDER",
    "EBO_NONE",
    "EBO_NOPERSISTVIEWSTATE",
    "EBO_NOTRAVELLOG",
    "EBO_NOWRAPPERWINDOW",
    "EBO_SHOWFRAMES",
    "ECF_AUTOMENUICONS",
    "ECF_DEFAULT",
    "ECF_HASLUASHIELD",
    "ECF_HASSPLITBUTTON",
    "ECF_HASSUBCOMMANDS",
    "ECF_HIDELABEL",
    "ECF_ISDROPDOWN",
    "ECF_ISSEPARATOR",
    "ECF_SEPARATORAFTER",
    "ECF_SEPARATORBEFORE",
    "ECF_TOGGLEABLE",
    "ECHUIM_DESKTOP",
    "ECHUIM_IMMERSIVE",
    "ECHUIM_SYSTEM_LAUNCHER",
    "ECS_CHECKBOX",
    "ECS_CHECKED",
    "ECS_DISABLED",
    "ECS_ENABLED",
    "ECS_HIDDEN",
    "ECS_RADIOCHECK",
    "EC_HOST_UI_MODE",
    "EDGE_GESTURE_KIND",
    "EGK_KEYBOARD",
    "EGK_MOUSE",
    "EGK_TOUCH",
    "EPS_DEFAULT_OFF",
    "EPS_DEFAULT_ON",
    "EPS_DONTCARE",
    "EPS_FORCE",
    "EPS_INITIALSTATE",
    "EPS_STATEMASK",
    "EP_AdvQueryPane",
    "EP_Commands",
    "EP_Commands_Organize",
    "EP_Commands_View",
    "EP_DetailsPane",
    "EP_NavPane",
    "EP_PreviewPane",
    "EP_QueryPane",
    "EP_Ribbon",
    "EP_StatusBar",
    "EXECUTE_E_LAUNCH_APPLICATION",
    "EXPLORER_BROWSER_FILL_FLAGS",
    "EXPLORER_BROWSER_OPTIONS",
    "EXPPS_FILETYPES",
    "EXP_DARWIN_ID_SIG",
    "EXP_DARWIN_LINK",
    "EXP_PROPERTYSTORAGE",
    "EXP_PROPERTYSTORAGE_SIG",
    "EXP_SPECIAL_FOLDER",
    "EXP_SPECIAL_FOLDER_SIG",
    "EXP_SZ_ICON_SIG",
    "EXP_SZ_LINK",
    "EXP_SZ_LINK_SIG",
    "EXTRASEARCH",
    "E_ACTIVATIONDENIED_SHELLERROR",
    "E_ACTIVATIONDENIED_SHELLNOTREADY",
    "E_ACTIVATIONDENIED_SHELLRESTART",
    "E_ACTIVATIONDENIED_UNEXPECTED",
    "E_ACTIVATIONDENIED_USERCLOSE",
    "E_FILE_PLACEHOLDER_NOT_INITIALIZED",
    "E_FILE_PLACEHOLDER_SERVER_TIMED_OUT",
    "E_FILE_PLACEHOLDER_STORAGEPROVIDER_NOT_FOUND",
    "E_FILE_PLACEHOLDER_VERSION_MISMATCH",
    "E_FLAGS",
    "E_IMAGEFEED_CHANGEDISABLED",
    "E_NOTVALIDFORANIMATEDIMAGE",
    "E_PREVIEWHANDLER_CORRUPT",
    "E_PREVIEWHANDLER_DRM_FAIL",
    "E_PREVIEWHANDLER_NOAUTH",
    "E_PREVIEWHANDLER_NOTFOUND",
    "E_SHELL_EXTENSION_BLOCKED",
    "E_TILE_NOTIFICATIONS_PLATFORM_FAILURE",
    "E_USERTILE_CHANGEDISABLED",
    "E_USERTILE_FILESIZE",
    "E_USERTILE_LARGEORDYNAMIC",
    "E_USERTILE_UNSUPPORTEDFILETYPE",
    "E_USERTILE_VIDEOFRAMESIZE",
    "EnumerableObjectCollection",
    "ExecuteFolder",
    "ExecuteUnknown",
    "ExplorerBrowser",
    "ExtractAssociatedIconA",
    "ExtractAssociatedIconExA",
    "ExtractAssociatedIconExW",
    "ExtractAssociatedIconW",
    "ExtractIconA",
    "ExtractIconExA",
    "ExtractIconExW",
    "ExtractIconW",
    "FCIDM_BROWSERFIRST",
    "FCIDM_BROWSERLAST",
    "FCIDM_GLOBALFIRST",
    "FCIDM_GLOBALLAST",
    "FCIDM_MENU_EDIT",
    "FCIDM_MENU_EXPLORE",
    "FCIDM_MENU_FAVORITES",
    "FCIDM_MENU_FILE",
    "FCIDM_MENU_FIND",
    "FCIDM_MENU_HELP",
    "FCIDM_MENU_TOOLS",
    "FCIDM_MENU_TOOLS_SEP_GOTO",
    "FCIDM_MENU_VIEW",
    "FCIDM_MENU_VIEW_SEP_OPTIONS",
    "FCIDM_SHVIEWFIRST",
    "FCIDM_SHVIEWLAST",
    "FCIDM_STATUS",
    "FCIDM_TOOLBAR",
    "FCSM_CLSID",
    "FCSM_FLAGS",
    "FCSM_ICONFILE",
    "FCSM_INFOTIP",
    "FCSM_LOGO",
    "FCSM_VIEWID",
    "FCSM_WEBVIEWTEMPLATE",
    "FCS_FLAG_DRAGDROP",
    "FCS_FORCEWRITE",
    "FCS_READ",
    "FCT_ADDTOEND",
    "FCT_CONFIGABLE",
    "FCT_MERGE",
    "FCW_INTERNETBAR",
    "FCW_PROGRESS",
    "FCW_STATUS",
    "FCW_TOOLBAR",
    "FCW_TREE",
    "FDAP",
    "FDAP_BOTTOM",
    "FDAP_TOP",
    "FDEOR_ACCEPT",
    "FDEOR_DEFAULT",
    "FDEOR_REFUSE",
    "FDESVR_ACCEPT",
    "FDESVR_DEFAULT",
    "FDESVR_REFUSE",
    "FDE_OVERWRITE_RESPONSE",
    "FDE_SHAREVIOLATION_RESPONSE",
    "FDTF_LONGDATE",
    "FDTF_LONGTIME",
    "FDTF_LTRDATE",
    "FDTF_NOAUTOREADINGORDER",
    "FDTF_RELATIVE",
    "FDTF_RTLDATE",
    "FDTF_SHORTDATE",
    "FDTF_SHORTTIME",
    "FD_ACCESSTIME",
    "FD_ATTRIBUTES",
    "FD_CLSID",
    "FD_CREATETIME",
    "FD_FILESIZE",
    "FD_FLAGS",
    "FD_LINKUI",
    "FD_PROGRESSUI",
    "FD_SIZEPOINT",
    "FD_UNICODE",
    "FD_WRITESTIME",
    "FEM_NAVIGATION",
    "FEM_VIEWRESULT",
    "FFFP_EXACTMATCH",
    "FFFP_MODE",
    "FFFP_NEARESTPARENTMATCH",
    "FILEDESCRIPTORA",
    "FILEDESCRIPTORW",
    "FILEGROUPDESCRIPTORA",
    "FILEGROUPDESCRIPTORW",
    "FILEOPENDIALOGOPTIONS",
    "FILETYPEATTRIBUTEFLAGS",
    "FILE_ATTRIBUTES_ARRAY",
    "FILE_OPERATION_FLAGS2",
    "FILE_USAGE_TYPE",
    "FLVM_CONTENT",
    "FLVM_DETAILS",
    "FLVM_FIRST",
    "FLVM_ICONS",
    "FLVM_LAST",
    "FLVM_LIST",
    "FLVM_TILES",
    "FLVM_UNSPECIFIED",
    "FLYOUT_PLACEMENT",
    "FMTID_Briefcase",
    "FMTID_CustomImageProperties",
    "FMTID_DRM",
    "FMTID_Displaced",
    "FMTID_ImageProperties",
    "FMTID_InternetSite",
    "FMTID_Intshcut",
    "FMTID_LibraryProperties",
    "FMTID_MUSIC",
    "FMTID_Misc",
    "FMTID_Query",
    "FMTID_ShellDetails",
    "FMTID_Storage",
    "FMTID_Volume",
    "FMTID_WebView",
    "FOF2_MERGEFOLDERSONCOLLISION",
    "FOF2_NONE",
    "FOFX_ADDUNDORECORD",
    "FOFX_COPYASDOWNLOAD",
    "FOFX_DONTDISPLAYDESTPATH",
    "FOFX_DONTDISPLAYLOCATIONS",
    "FOFX_DONTDISPLAYSOURCEPATH",
    "FOFX_EARLYFAILURE",
    "FOFX_KEEPNEWERFILE",
    "FOFX_MOVEACLSACROSSVOLUMES",
    "FOFX_NOCOPYHOOKS",
    "FOFX_NOMINIMIZEBOX",
    "FOFX_NOSKIPJUNCTIONS",
    "FOFX_PREFERHARDLINK",
    "FOFX_PRESERVEFILEEXTENSIONS",
    "FOFX_RECYCLEONDELETE",
    "FOFX_REQUIREELEVATION",
    "FOFX_SHOWELEVATIONPROMPT",
    "FOF_ALLOWUNDO",
    "FOF_CONFIRMMOUSE",
    "FOF_FILESONLY",
    "FOF_MULTIDESTFILES",
    "FOF_NOCONFIRMATION",
    "FOF_NOCONFIRMMKDIR",
    "FOF_NOCOPYSECURITYATTRIBS",
    "FOF_NOERRORUI",
    "FOF_NORECURSEREPARSE",
    "FOF_NORECURSION",
    "FOF_NO_CONNECTED_ELEMENTS",
    "FOF_RENAMEONCOLLISION",
    "FOF_SILENT",
    "FOF_SIMPLEPROGRESS",
    "FOF_WANTMAPPINGHANDLE",
    "FOF_WANTNUKEWARNING",
    "FOLDERFLAGS",
    "FOLDERID_AccountPictures",
    "FOLDERID_AddNewPrograms",
    "FOLDERID_AdminTools",
    "FOLDERID_AllAppMods",
    "FOLDERID_AppCaptures",
    "FOLDERID_AppDataDesktop",
    "FOLDERID_AppDataDocuments",
    "FOLDERID_AppDataFavorites",
    "FOLDERID_AppDataProgramData",
    "FOLDERID_AppUpdates",
    "FOLDERID_ApplicationShortcuts",
    "FOLDERID_AppsFolder",
    "FOLDERID_CDBurning",
    "FOLDERID_CameraRoll",
    "FOLDERID_CameraRollLibrary",
    "FOLDERID_ChangeRemovePrograms",
    "FOLDERID_CommonAdminTools",
    "FOLDERID_CommonOEMLinks",
    "FOLDERID_CommonPrograms",
    "FOLDERID_CommonStartMenu",
    "FOLDERID_CommonStartMenuPlaces",
    "FOLDERID_CommonStartup",
    "FOLDERID_CommonTemplates",
    "FOLDERID_ComputerFolder",
    "FOLDERID_ConflictFolder",
    "FOLDERID_ConnectionsFolder",
    "FOLDERID_Contacts",
    "FOLDERID_ControlPanelFolder",
    "FOLDERID_Cookies",
    "FOLDERID_CurrentAppMods",
    "FOLDERID_Desktop",
    "FOLDERID_DevelopmentFiles",
    "FOLDERID_Device",
    "FOLDERID_DeviceMetadataStore",
    "FOLDERID_Documents",
    "FOLDERID_DocumentsLibrary",
    "FOLDERID_Downloads",
    "FOLDERID_Favorites",
    "FOLDERID_Fonts",
    "FOLDERID_GameTasks",
    "FOLDERID_Games",
    "FOLDERID_History",
    "FOLDERID_HomeGroup",
    "FOLDERID_HomeGroupCurrentUser",
    "FOLDERID_ImplicitAppShortcuts",
    "FOLDERID_InternetCache",
    "FOLDERID_InternetFolder",
    "FOLDERID_Libraries",
    "FOLDERID_Links",
    "FOLDERID_LocalAppData",
    "FOLDERID_LocalAppDataLow",
    "FOLDERID_LocalDocuments",
    "FOLDERID_LocalDownloads",
    "FOLDERID_LocalMusic",
    "FOLDERID_LocalPictures",
    "FOLDERID_LocalStorage",
    "FOLDERID_LocalVideos",
    "FOLDERID_LocalizedResourcesDir",
    "FOLDERID_Music",
    "FOLDERID_MusicLibrary",
    "FOLDERID_NetHood",
    "FOLDERID_NetworkFolder",
    "FOLDERID_Objects3D",
    "FOLDERID_OneDrive",
    "FOLDERID_OriginalImages",
    "FOLDERID_PhotoAlbums",
    "FOLDERID_Pictures",
    "FOLDERID_PicturesLibrary",
    "FOLDERID_Playlists",
    "FOLDERID_PrintHood",
    "FOLDERID_PrintersFolder",
    "FOLDERID_Profile",
    "FOLDERID_ProgramData",
    "FOLDERID_ProgramFiles",
    "FOLDERID_ProgramFilesCommon",
    "FOLDERID_ProgramFilesCommonX64",
    "FOLDERID_ProgramFilesCommonX86",
    "FOLDERID_ProgramFilesX64",
    "FOLDERID_ProgramFilesX86",
    "FOLDERID_Programs",
    "FOLDERID_Public",
    "FOLDERID_PublicDesktop",
    "FOLDERID_PublicDocuments",
    "FOLDERID_PublicDownloads",
    "FOLDERID_PublicGameTasks",
    "FOLDERID_PublicLibraries",
    "FOLDERID_PublicMusic",
    "FOLDERID_PublicPictures",
    "FOLDERID_PublicRingtones",
    "FOLDERID_PublicUserTiles",
    "FOLDERID_PublicVideos",
    "FOLDERID_QuickLaunch",
    "FOLDERID_Recent",
    "FOLDERID_RecordedCalls",
    "FOLDERID_RecordedTVLibrary",
    "FOLDERID_RecycleBinFolder",
    "FOLDERID_ResourceDir",
    "FOLDERID_RetailDemo",
    "FOLDERID_Ringtones",
    "FOLDERID_RoamedTileImages",
    "FOLDERID_RoamingAppData",
    "FOLDERID_RoamingTiles",
    "FOLDERID_SEARCH_CSC",
    "FOLDERID_SEARCH_MAPI",
    "FOLDERID_SampleMusic",
    "FOLDERID_SamplePictures",
    "FOLDERID_SamplePlaylists",
    "FOLDERID_SampleVideos",
    "FOLDERID_SavedGames",
    "FOLDERID_SavedPictures",
    "FOLDERID_SavedPicturesLibrary",
    "FOLDERID_SavedSearches",
    "FOLDERID_Screenshots",
    "FOLDERID_SearchHistory",
    "FOLDERID_SearchHome",
    "FOLDERID_SearchTemplates",
    "FOLDERID_SendTo",
    "FOLDERID_SidebarDefaultParts",
    "FOLDERID_SidebarParts",
    "FOLDERID_SkyDrive",
    "FOLDERID_SkyDriveCameraRoll",
    "FOLDERID_SkyDriveDocuments",
    "FOLDERID_SkyDriveMusic",
    "FOLDERID_SkyDrivePictures",
    "FOLDERID_StartMenu",
    "FOLDERID_StartMenuAllPrograms",
    "FOLDERID_Startup",
    "FOLDERID_SyncManagerFolder",
    "FOLDERID_SyncResultsFolder",
    "FOLDERID_SyncSetupFolder",
    "FOLDERID_System",
    "FOLDERID_SystemX86",
    "FOLDERID_Templates",
    "FOLDERID_UserPinned",
    "FOLDERID_UserProfiles",
    "FOLDERID_UserProgramFiles",
    "FOLDERID_UserProgramFilesCommon",
    "FOLDERID_UsersFiles",
    "FOLDERID_UsersLibraries",
    "FOLDERID_Videos",
    "FOLDERID_VideosLibrary",
    "FOLDERID_Windows",
    "FOLDERLOGICALVIEWMODE",
    "FOLDERSETDATA",
    "FOLDERSETTINGS",
    "FOLDERTYPEID_AccountPictures",
    "FOLDERTYPEID_Communications",
    "FOLDERTYPEID_CompressedFolder",
    "FOLDERTYPEID_Contacts",
    "FOLDERTYPEID_ControlPanelCategory",
    "FOLDERTYPEID_ControlPanelClassic",
    "FOLDERTYPEID_Documents",
    "FOLDERTYPEID_Downloads",
    "FOLDERTYPEID_Games",
    "FOLDERTYPEID_Generic",
    "FOLDERTYPEID_GenericLibrary",
    "FOLDERTYPEID_GenericSearchResults",
    "FOLDERTYPEID_Invalid",
    "FOLDERTYPEID_Music",
    "FOLDERTYPEID_NetworkExplorer",
    "FOLDERTYPEID_OpenSearch",
    "FOLDERTYPEID_OtherUsers",
    "FOLDERTYPEID_Pictures",
    "FOLDERTYPEID_Printers",
    "FOLDERTYPEID_PublishedItems",
    "FOLDERTYPEID_RecordedTV",
    "FOLDERTYPEID_RecycleBin",
    "FOLDERTYPEID_SavedGames",
    "FOLDERTYPEID_SearchConnector",
    "FOLDERTYPEID_SearchHome",
    "FOLDERTYPEID_Searches",
    "FOLDERTYPEID_SoftwareExplorer",
    "FOLDERTYPEID_StartMenu",
    "FOLDERTYPEID_StorageProviderDocuments",
    "FOLDERTYPEID_StorageProviderGeneric",
    "FOLDERTYPEID_StorageProviderMusic",
    "FOLDERTYPEID_StorageProviderPictures",
    "FOLDERTYPEID_StorageProviderVideos",
    "FOLDERTYPEID_UserFiles",
    "FOLDERTYPEID_UsersLibraries",
    "FOLDERTYPEID_Videos",
    "FOLDERVIEWMODE",
    "FOLDERVIEWOPTIONS",
    "FOLDER_ENUM_MODE",
    "FOS_ALLNONSTORAGEITEMS",
    "FOS_ALLOWMULTISELECT",
    "FOS_CREATEPROMPT",
    "FOS_DEFAULTNOMINIMODE",
    "FOS_DONTADDTORECENT",
    "FOS_FILEMUSTEXIST",
    "FOS_FORCEFILESYSTEM",
    "FOS_FORCEPREVIEWPANEON",
    "FOS_FORCESHOWHIDDEN",
    "FOS_HIDEMRUPLACES",
    "FOS_HIDEPINNEDPLACES",
    "FOS_NOCHANGEDIR",
    "FOS_NODEREFERENCELINKS",
    "FOS_NOREADONLYRETURN",
    "FOS_NOTESTFILECREATE",
    "FOS_NOVALIDATE",
    "FOS_OKBUTTONNEEDSINTERACTION",
    "FOS_OVERWRITEPROMPT",
    "FOS_PATHMUSTEXIST",
    "FOS_PICKFOLDERS",
    "FOS_SHAREAWARE",
    "FOS_STRICTFILETYPES",
    "FOS_SUPPORTSTREAMABLEITEMS",
    "FO_COPY",
    "FO_DELETE",
    "FO_MOVE",
    "FO_RENAME",
    "FP_ABOVE",
    "FP_BELOW",
    "FP_DEFAULT",
    "FP_LEFT",
    "FP_RIGHT",
    "FSCopyHandler",
    "FTA_AlwaysUnsafe",
    "FTA_AlwaysUseDirectInvoke",
    "FTA_Exclude",
    "FTA_HasExtension",
    "FTA_NoDDE",
    "FTA_NoEdit",
    "FTA_NoEditDesc",
    "FTA_NoEditDflt",
    "FTA_NoEditIcon",
    "FTA_NoEditMIME",
    "FTA_NoEditVerb",
    "FTA_NoEditVerbCmd",
    "FTA_NoEditVerbExe",
    "FTA_NoNewVerb",
    "FTA_NoRecentDocs",
    "FTA_NoRemove",
    "FTA_NoRemoveVerb",
    "FTA_None",
    "FTA_OpenIsSafe",
    "FTA_SafeForElevation",
    "FTA_Show",
    "FUT_EDITING",
    "FUT_GENERIC",
    "FUT_PLAYING",
    "FVM_AUTO",
    "FVM_CONTENT",
    "FVM_DETAILS",
    "FVM_FIRST",
    "FVM_ICON",
    "FVM_LAST",
    "FVM_LIST",
    "FVM_SMALLICON",
    "FVM_THUMBNAIL",
    "FVM_THUMBSTRIP",
    "FVM_TILE",
    "FVO_CUSTOMORDERING",
    "FVO_CUSTOMPOSITION",
    "FVO_DEFAULT",
    "FVO_NOANIMATIONS",
    "FVO_NOSCROLLTIPS",
    "FVO_SUPPORTHYPERLINKS",
    "FVO_VISTALAYOUT",
    "FVSIF_CANVIEWIT",
    "FVSIF_NEWFAILED",
    "FVSIF_NEWFILE",
    "FVSIF_PINNED",
    "FVSIF_RECT",
    "FVST_EMPTYTEXT",
    "FVTEXTTYPE",
    "FWF_ABBREVIATEDNAMES",
    "FWF_ALIGNLEFT",
    "FWF_ALLOWRTLREADING",
    "FWF_AUTOARRANGE",
    "FWF_AUTOCHECKSELECT",
    "FWF_BESTFITWINDOW",
    "FWF_CHECKSELECT",
    "FWF_DESKTOP",
    "FWF_EXTENDEDTILES",
    "FWF_FULLROWSELECT",
    "FWF_HIDEFILENAMES",
    "FWF_NOBROWSERVIEWSTATE",
    "FWF_NOCLIENTEDGE",
    "FWF_NOCOLUMNHEADER",
    "FWF_NOENUMREFRESH",
    "FWF_NOFILTERS",
    "FWF_NOGROUPING",
    "FWF_NOHEADERINALLVIEWS",
    "FWF_NOICONS",
    "FWF_NONE",
    "FWF_NOSCROLL",
    "FWF_NOSUBFOLDERS",
    "FWF_NOVISIBLE",
    "FWF_NOWEBVIEW",
    "FWF_OWNERDATA",
    "FWF_SHOWSELALWAYS",
    "FWF_SINGLECLICKACTIVATE",
    "FWF_SINGLESEL",
    "FWF_SNAPTOGRID",
    "FWF_SUBSETGROUPS",
    "FWF_TRANSPARENT",
    "FWF_TRICHECKSELECT",
    "FWF_USESEARCHFOLDER",
    "FileOpenDialog",
    "FileOperation",
    "FileSaveDialog",
    "FileSearchBand",
    "FindExecutableA",
    "FindExecutableW",
    "Folder",
    "Folder2",
    "Folder3",
    "FolderItem",
    "FolderItem2",
    "FolderItemVerb",
    "FolderItemVerbs",
    "FolderItems",
    "FolderItems2",
    "FolderItems3",
    "FolderViewHost",
    "FrameworkInputPane",
    "FreeSpaceCategorizer",
    "GADOF_DIRTY",
    "GCS_HELPTEXT",
    "GCS_HELPTEXTA",
    "GCS_HELPTEXTW",
    "GCS_UNICODE",
    "GCS_VALIDATE",
    "GCS_VALIDATEA",
    "GCS_VALIDATEW",
    "GCS_VERB",
    "GCS_VERBA",
    "GCS_VERBICONW",
    "GCS_VERBW",
    "GCT_INVALID",
    "GCT_LFNCHAR",
    "GCT_SEPARATOR",
    "GCT_SHORTCHAR",
    "GCT_WILD",
    "GETPROPS_NONE",
    "GIL_ASYNC",
    "GIL_CHECKSHIELD",
    "GIL_DEFAULTICON",
    "GIL_DONTCACHE",
    "GIL_FORCENOSHIELD",
    "GIL_FORSHELL",
    "GIL_FORSHORTCUT",
    "GIL_NOTFILENAME",
    "GIL_OPENICON",
    "GIL_PERCLASS",
    "GIL_PERINSTANCE",
    "GIL_SHIELD",
    "GIL_SIMULATEDOC",
    "GLOBALCOUNTER_APPLICATION_DESTINATIONS",
    "GLOBALCOUNTER_APPROVEDSITES",
    "GLOBALCOUNTER_APPSFOLDER_FILETYPEASSOCIATION_COUNTER",
    "GLOBALCOUNTER_APP_ITEMS_STATE_STORE_CACHE",
    "GLOBALCOUNTER_ASSOCCHANGED",
    "GLOBALCOUNTER_BANNERS_DATAMODEL_CACHE_MACHINEWIDE",
    "GLOBALCOUNTER_BITBUCKETNUMDELETERS",
    "GLOBALCOUNTER_COMMONPLACES_LIST_CACHE",
    "GLOBALCOUNTER_FOLDERDEFINITION_CACHE",
    "GLOBALCOUNTER_FOLDERSETTINGSCHANGE",
    "GLOBALCOUNTER_IEONLY_SESSIONS",
    "GLOBALCOUNTER_IESESSIONS",
    "GLOBALCOUNTER_INTERNETTOOLBAR_LAYOUT",
    "GLOBALCOUNTER_MAXIMUMVALUE",
    "GLOBALCOUNTER_OVERLAYMANAGER",
    "GLOBALCOUNTER_PRIVATE_PROFILE_CACHE",
    "GLOBALCOUNTER_PRIVATE_PROFILE_CACHE_MACHINEWIDE",
    "GLOBALCOUNTER_QUERYASSOCIATIONS",
    "GLOBALCOUNTER_RATINGS",
    "GLOBALCOUNTER_RATINGS_STATECOUNTER",
    "GLOBALCOUNTER_RECYCLEBINCORRUPTED",
    "GLOBALCOUNTER_RECYCLEBINENUM",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_A",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_B",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_C",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_D",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_E",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_F",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_G",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_H",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_I",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_J",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_K",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_L",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_M",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_N",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_O",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_P",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Q",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_R",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_S",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_T",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_U",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_V",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_W",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_X",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Y",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Z",
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SHARES",
    "GLOBALCOUNTER_RESTRICTIONS",
    "GLOBALCOUNTER_SEARCHMANAGER",
    "GLOBALCOUNTER_SEARCHOPTIONS",
    "GLOBALCOUNTER_SETTINGSYNC_ENABLED",
    "GLOBALCOUNTER_SHELLSETTINGSCHANGED",
    "GLOBALCOUNTER_SYNC_ENGINE_INFORMATION_CACHE_MACHINEWIDE",
    "GLOBALCOUNTER_SYSTEMPIDLCHANGE",
    "GLOBALCOUNTER_USERINFOCHANGED",
    "GPFIDL_ALTNAME",
    "GPFIDL_DEFAULT",
    "GPFIDL_FLAGS",
    "GPFIDL_UNCPRINTER",
    "GenericCredentialProvider",
    "GetAcceptLanguagesA",
    "GetAcceptLanguagesW",
    "GetAllUsersProfileDirectoryA",
    "GetAllUsersProfileDirectoryW",
    "GetCurrentProcessExplicitAppUserModelID",
    "GetDefaultUserProfileDirectoryA",
    "GetDefaultUserProfileDirectoryW",
    "GetDpiForShellUIComponent",
    "GetFileNameFromBrowse",
    "GetMenuContextHelpId",
    "GetMenuPosFromID",
    "GetProfileType",
    "GetProfilesDirectoryA",
    "GetProfilesDirectoryW",
    "GetScaleFactorForDevice",
    "GetScaleFactorForMonitor",
    "GetUserProfileDirectoryA",
    "GetUserProfileDirectoryW",
    "GetWindowContextHelpId",
    "GetWindowSubclass",
    "HDROP",
    "HELPINFO",
    "HELPINFO_MENUITEM",
    "HELPINFO_WINDOW",
    "HELPWININFOA",
    "HELPWININFOW",
    "HELP_INFO_TYPE",
    "HGSC_DOCUMENTSLIBRARY",
    "HGSC_MUSICLIBRARY",
    "HGSC_NONE",
    "HGSC_PICTURESLIBRARY",
    "HGSC_PRINTERS",
    "HGSC_VIDEOSLIBRARY",
    "HLBWIF_DOCWNDMAXIMIZED",
    "HLBWIF_FLAGS",
    "HLBWIF_FRAMEWNDMAXIMIZED",
    "HLBWIF_HASDOCWNDINFO",
    "HLBWIF_HASFRAMEWNDINFO",
    "HLBWIF_HASWEBTOOLBARINFO",
    "HLBWIF_WEBTOOLBARHIDDEN",
    "HLBWINFO",
    "HLFNAMEF",
    "HLFNAMEF_DEFAULT",
    "HLFNAMEF_TRYCACHE",
    "HLFNAMEF_TRYFULLTARGET",
    "HLFNAMEF_TRYPRETTYTARGET",
    "HLFNAMEF_TRYWIN95SHORTCUT",
    "HLID_CURRENT",
    "HLID_INFO",
    "HLID_INVALID",
    "HLID_NEXT",
    "HLID_PREVIOUS",
    "HLID_STACKBOTTOM",
    "HLID_STACKTOP",
    "HLINKGETREF",
    "HLINKGETREF_ABSOLUTE",
    "HLINKGETREF_DEFAULT",
    "HLINKGETREF_RELATIVE",
    "HLINKMISC",
    "HLINKMISC_RELATIVE",
    "HLINKSETF",
    "HLINKSETF_LOCATION",
    "HLINKSETF_TARGET",
    "HLINKWHICHMK",
    "HLINKWHICHMK_BASE",
    "HLINKWHICHMK_CONTAINER",
    "HLINK_E_FIRST",
    "HLINK_S_DONTHIDE",
    "HLINK_S_FIRST",
    "HLITEM",
    "HLNF",
    "HLNF_ALLOW_AUTONAVIGATE",
    "HLNF_CALLERUNTRUSTED",
    "HLNF_CREATENOHISTORY",
    "HLNF_DISABLEWINDOWRESTRICTIONS",
    "HLNF_EXTERNALNAVIGATE",
    "HLNF_INTERNALJUMP",
    "HLNF_NAVIGATINGBACK",
    "HLNF_NAVIGATINGFORWARD",
    "HLNF_NAVIGATINGTOSTACKITEM",
    "HLNF_NEWWINDOWSMANAGED",
    "HLNF_OPENINNEWWINDOW",
    "HLNF_TRUSTEDFORACTIVEX",
    "HLNF_TRUSTFIRSTDOWNLOAD",
    "HLNF_UNTRUSTEDFORDOWNLOAD",
    "HLQF_INFO",
    "HLQF_ISCURRENT",
    "HLQF_ISVALID",
    "HLSHORTCUTF",
    "HLSHORTCUTF_DEFAULT",
    "HLSHORTCUTF_DONTACTUALLYCREATE",
    "HLSHORTCUTF_MAYUSEEXISTINGSHORTCUT",
    "HLSHORTCUTF_USEFILENAMEFROMFRIENDLYNAME",
    "HLSHORTCUTF_USEUNIQUEFILENAME",
    "HLSR",
    "HLSR_HISTORYFOLDER",
    "HLSR_HOME",
    "HLSR_SEARCHPAGE",
    "HLTBINFO",
    "HLTB_DOCKEDBOTTOM",
    "HLTB_DOCKEDLEFT",
    "HLTB_DOCKEDRIGHT",
    "HLTB_DOCKEDTOP",
    "HLTB_FLOATING",
    "HLTB_INFO",
    "HLTRANSLATEF",
    "HLTRANSLATEF_DEFAULT",
    "HLTRANSLATEF_DONTAPPLYDEFAULTPREFIX",
    "HMONITOR_UserFree",
    "HMONITOR_UserFree64",
    "HMONITOR_UserMarshal",
    "HMONITOR_UserMarshal64",
    "HMONITOR_UserSize",
    "HMONITOR_UserSize64",
    "HMONITOR_UserUnmarshal",
    "HMONITOR_UserUnmarshal64",
    "HOMEGROUPSHARINGCHOICES",
    "HOMEGROUP_SECURITY_GROUP",
    "HOMEGROUP_SECURITY_GROUP_MULTI",
    "HPSXA",
    "HashData",
    "HideInputPaneAnimationCoordinator",
    "HlinkClone",
    "HlinkCreateBrowseContext",
    "HlinkCreateExtensionServices",
    "HlinkCreateFromData",
    "HlinkCreateFromMoniker",
    "HlinkCreateFromString",
    "HlinkCreateShortcut",
    "HlinkCreateShortcutFromMoniker",
    "HlinkCreateShortcutFromString",
    "HlinkGetSpecialReference",
    "HlinkGetValueFromParams",
    "HlinkIsShortcut",
    "HlinkNavigate",
    "HlinkNavigateToStringReference",
    "HlinkOnNavigate",
    "HlinkOnRenameDocument",
    "HlinkParseDisplayName",
    "HlinkPreprocessMoniker",
    "HlinkQueryCreateFromData",
    "HlinkResolveMonikerForData",
    "HlinkResolveShortcut",
    "HlinkResolveShortcutToMoniker",
    "HlinkResolveShortcutToString",
    "HlinkResolveStringForData",
    "HlinkSetSpecialReference",
    "HlinkTranslateURL",
    "HlinkUpdateStackItem",
    "HomeGroup",
    "IACList",
    "IACList2",
    "IAccessibilityDockingService",
    "IAccessibilityDockingServiceCallback",
    "IAccessibleObject",
    "IActionProgress",
    "IActionProgressDialog",
    "IAppActivationUIInfo",
    "IAppPublisher",
    "IAppVisibility",
    "IAppVisibilityEvents",
    "IApplicationActivationManager",
    "IApplicationAssociationRegistration",
    "IApplicationAssociationRegistrationUI",
    "IApplicationDesignModeSettings",
    "IApplicationDesignModeSettings2",
    "IApplicationDestinations",
    "IApplicationDocumentLists",
    "IAssocHandler",
    "IAssocHandlerInvoker",
    "IAttachmentExecute",
    "IAutoComplete",
    "IAutoComplete2",
    "IAutoCompleteDropDown",
    "IBandHost",
    "IBandSite",
    "IBannerNotificationHandler",
    "IBanneredBar",
    "IBrowserFrameOptions",
    "IBrowserService",
    "IBrowserService2",
    "IBrowserService3",
    "IBrowserService4",
    "ICDBurn",
    "ICDBurnExt",
    "ICategorizer",
    "ICategoryProvider",
    "IColumnManager",
    "IColumnProvider",
    "ICommDlgBrowser",
    "ICommDlgBrowser2",
    "ICommDlgBrowser3",
    "IComputerInfoChangeNotify",
    "IConnectableCredentialProviderCredential",
    "IContactManagerInterop",
    "IContextMenu",
    "IContextMenu2",
    "IContextMenu3",
    "IContextMenuCB",
    "IContextMenuSite",
    "ICopyHookA",
    "ICopyHookW",
    "ICreateProcessInputs",
    "ICreatingProcess",
    "ICredentialProvider",
    "ICredentialProviderCredential",
    "ICredentialProviderCredential2",
    "ICredentialProviderCredentialEvents",
    "ICredentialProviderCredentialEvents2",
    "ICredentialProviderCredentialWithFieldOptions",
    "ICredentialProviderEvents",
    "ICredentialProviderFilter",
    "ICredentialProviderSetUserArray",
    "ICredentialProviderUser",
    "ICredentialProviderUserArray",
    "ICurrentItem",
    "ICurrentWorkingDirectory",
    "ICustomDestinationList",
    "IDC_OFFLINE_HAND",
    "IDC_PANTOOL_HAND_CLOSED",
    "IDC_PANTOOL_HAND_OPEN",
    "IDD_WIZEXTN_FIRST",
    "IDD_WIZEXTN_LAST",
    "IDO_SHGIOI_DEFAULT",
    "IDO_SHGIOI_LINK",
    "IDO_SHGIOI_SHARE",
    "IDO_SHGIOI_SLOWFILE",
    "IDS_DESCRIPTION",
    "ID_APP",
    "IDataObjectAsyncCapability",
    "IDataObjectProvider",
    "IDataTransferManagerInterop",
    "IDefaultExtractIconInit",
    "IDefaultFolderMenuInitialize",
    "IDelegateFolder",
    "IDelegateItem",
    "IDeskBand",
    "IDeskBand2",
    "IDeskBandInfo",
    "IDeskBar",
    "IDeskBarClient",
    "IDesktopGadget",
    "IDesktopWallpaper",
    "IDestinationStreamFactory",
    "IDisplayItem",
    "IDocViewSite",
    "IDockingWindow",
    "IDockingWindowFrame",
    "IDockingWindowSite",
    "IDragSourceHelper",
    "IDragSourceHelper2",
    "IDropTargetHelper",
    "IDynamicHWHandler",
    "IEIFLAG_ASPECT",
    "IEIFLAG_ASYNC",
    "IEIFLAG_CACHE",
    "IEIFLAG_GLEAM",
    "IEIFLAG_NOBORDER",
    "IEIFLAG_NOSTAMP",
    "IEIFLAG_OFFLINE",
    "IEIFLAG_ORIGSIZE",
    "IEIFLAG_QUALITY",
    "IEIFLAG_REFRESH",
    "IEIFLAG_SCREEN",
    "IEIT_PRIORITY_NORMAL",
    "IEI_PRIORITY_MAX",
    "IEI_PRIORITY_MIN",
    "IENamespaceTreeControl",
    "IEPDNFLAGS",
    "IEPDN_BINDINGUI",
    "IESHORTCUTFLAGS",
    "IESHORTCUT_BACKGROUNDTAB",
    "IESHORTCUT_FORCENAVIGATE",
    "IESHORTCUT_NEWBROWSER",
    "IESHORTCUT_OPENNEWTAB",
    "IEnumACString",
    "IEnumAssocHandlers",
    "IEnumExplorerCommand",
    "IEnumExtraSearch",
    "IEnumFullIDList",
    "IEnumHLITEM",
    "IEnumIDList",
    "IEnumObjects",
    "IEnumPublishedApps",
    "IEnumReadyCallback",
    "IEnumResources",
    "IEnumShellItems",
    "IEnumSyncMgrConflict",
    "IEnumSyncMgrEvents",
    "IEnumSyncMgrSyncItems",
    "IEnumTravelLogEntry",
    "IEnumerableView",
    "IExecuteCommand",
    "IExecuteCommandApplicationHostEnvironment",
    "IExecuteCommandHost",
    "IExpDispSupport",
    "IExpDispSupportXP",
    "IExplorerBrowser",
    "IExplorerBrowserEvents",
    "IExplorerCommand",
    "IExplorerCommandProvider",
    "IExplorerCommandState",
    "IExplorerPaneVisibility",
    "IExtensionServices",
    "IExtractIconA",
    "IExtractIconW",
    "IExtractImage",
    "IExtractImage2",
    "IFileDialog",
    "IFileDialog2",
    "IFileDialogControlEvents",
    "IFileDialogCustomize",
    "IFileDialogEvents",
    "IFileIsInUse",
    "IFileOpenDialog",
    "IFileOperation",
    "IFileOperation2",
    "IFileOperationProgressSink",
    "IFileSaveDialog",
    "IFileSearchBand",
    "IFileSyncMergeHandler",
    "IFileSystemBindData",
    "IFileSystemBindData2",
    "IFolderBandPriv",
    "IFolderFilter",
    "IFolderFilterSite",
    "IFolderView",
    "IFolderView2",
    "IFolderViewHost",
    "IFolderViewOC",
    "IFolderViewOptions",
    "IFolderViewSettings",
    "IFrameworkInputPane",
    "IFrameworkInputPaneHandler",
    "IGetServiceIds",
    "IHWEventHandler",
    "IHWEventHandler2",
    "IHandlerActivationHost",
    "IHandlerInfo",
    "IHandlerInfo2",
    "IHlink",
    "IHlinkBrowseContext",
    "IHlinkFrame",
    "IHlinkSite",
    "IHlinkTarget",
    "IHomeGroup",
    "IIOCancelInformation",
    "IIdentityName",
    "IImageRecompress",
    "IInitializeCommand",
    "IInitializeNetworkFolder",
    "IInitializeObject",
    "IInitializeWithBindCtx",
    "IInitializeWithItem",
    "IInitializeWithPropertyStore",
    "IInitializeWithWindow",
    "IInputObject",
    "IInputObject2",
    "IInputObjectSite",
    "IInputPaneAnimationCoordinator",
    "IInputPanelConfiguration",
    "IInputPanelInvocationConfiguration",
    "IInsertItem",
    "IItemNameLimits",
    "IKnownFolder",
    "IKnownFolderManager",
    "ILAppendID",
    "ILClone",
    "ILCloneFirst",
    "ILCombine",
    "ILCreateFromPathA",
    "ILCreateFromPathW",
    "ILFindChild",
    "ILFindLastID",
    "ILFree",
    "ILGetNext",
    "ILGetSize",
    "ILIsEqual",
    "ILIsParent",
    "ILLoadFromStreamEx",
    "ILMM_IE4",
    "ILRemoveLastID",
    "ILSaveToStream",
    "ILaunchSourceAppUserModelId",
    "ILaunchSourceViewSizePreference",
    "ILaunchTargetMonitor",
    "ILaunchTargetViewSizePreference",
    "ILaunchUIContext",
    "ILaunchUIContextProvider",
    "IMM_ACC_DOCKING_E_DOCKOCCUPIED",
    "IMM_ACC_DOCKING_E_INSUFFICIENTHEIGHT",
    "IMSC_E_SHELL_COMPONENT_STARTUP_FAILURE",
    "IMenuBand",
    "IMenuPopup",
    "IModalWindow",
    "INTERNET_MAX_PATH_LENGTH",
    "INTERNET_MAX_SCHEME_LENGTH",
    "INameSpaceTreeAccessible",
    "INameSpaceTreeControl",
    "INameSpaceTreeControl2",
    "INameSpaceTreeControlCustomDraw",
    "INameSpaceTreeControlDropHandler",
    "INameSpaceTreeControlEvents",
    "INameSpaceTreeControlFolderCapabilities",
    "INamedPropertyBag",
    "INamespaceWalk",
    "INamespaceWalkCB",
    "INamespaceWalkCB2",
    "INetworkFolderInternal",
    "INewMenuClient",
    "INewShortcutHookA",
    "INewShortcutHookW",
    "INewWDEvents",
    "INewWindowManager",
    "INotifyReplica",
    "IObjMgr",
    "IObjectProvider",
    "IObjectWithAppUserModelID",
    "IObjectWithBackReferences",
    "IObjectWithCancelEvent",
    "IObjectWithFolderEnumMode",
    "IObjectWithProgID",
    "IObjectWithSelection",
    "IOpenControlPanel",
    "IOpenSearchSource",
    "IOperationsProgressDialog",
    "IPackageDebugSettings",
    "IPackageDebugSettings2",
    "IPackageExecutionStateChangeNotification",
    "IParentAndItem",
    "IParseAndCreateItem",
    "IPersistFolder",
    "IPersistFolder2",
    "IPersistFolder3",
    "IPersistIDList",
    "IPreviewHandler",
    "IPreviewHandlerFrame",
    "IPreviewHandlerVisuals",
    "IPreviewItem",
    "IPreviousVersionsInfo",
    "IProfferService",
    "IProgressDialog",
    "IPropertyKeyStore",
    "IPublishedApp",
    "IPublishedApp2",
    "IPublishingWizard",
    "IQueryAssociations",
    "IQueryCancelAutoPlay",
    "IQueryCodePage",
    "IQueryContinue",
    "IQueryContinueWithStatus",
    "IQueryInfo",
    "IRTIR_TASK_FINISHED",
    "IRTIR_TASK_NOT_RUNNING",
    "IRTIR_TASK_PENDING",
    "IRTIR_TASK_RUNNING",
    "IRTIR_TASK_SUSPENDED",
    "IRegTreeItem",
    "IRelatedItem",
    "IRemoteComputer",
    "IResolveShellLink",
    "IResultsFolder",
    "IRunnableTask",
    "ISFBVIEWMODE_LARGEICONS",
    "ISFBVIEWMODE_LOGOS",
    "ISFBVIEWMODE_SMALLICONS",
    "ISFB_MASK_BKCOLOR",
    "ISFB_MASK_COLORS",
    "ISFB_MASK_IDLIST",
    "ISFB_MASK_SHELLFOLDER",
    "ISFB_MASK_STATE",
    "ISFB_MASK_VIEWMODE",
    "ISFB_STATE_ALLOWRENAME",
    "ISFB_STATE_BTNMINSIZE",
    "ISFB_STATE_CHANNELBAR",
    "ISFB_STATE_DEBOSSED",
    "ISFB_STATE_DEFAULT",
    "ISFB_STATE_FULLOPEN",
    "ISFB_STATE_NONAMESORT",
    "ISFB_STATE_NOSHOWTEXT",
    "ISFB_STATE_QLINKSMODE",
    "ISHCUTCMDID_COMMITHISTORY",
    "ISHCUTCMDID_DOWNLOADICON",
    "ISHCUTCMDID_INTSHORTCUTCREATE",
    "ISHCUTCMDID_SETUSERAWURL",
    "ISIOI_ICONFILE",
    "ISIOI_ICONINDEX",
    "IS_E_EXEC_FAILED",
    "IS_FULLSCREEN",
    "IS_NORMAL",
    "IS_SPLIT",
    "IScriptErrorList",
    "ISearchBoxInfo",
    "ISearchContext",
    "ISearchFolderItemFactory",
    "ISharedBitmap",
    "ISharingConfigurationManager",
    "IShellApp",
    "IShellBrowser",
    "IShellChangeNotify",
    "IShellDetails",
    "IShellDispatch",
    "IShellDispatch2",
    "IShellDispatch3",
    "IShellDispatch4",
    "IShellDispatch5",
    "IShellDispatch6",
    "IShellExtInit",
    "IShellFavoritesNameSpace",
    "IShellFolder",
    "IShellFolder2",
    "IShellFolderBand",
    "IShellFolderView",
    "IShellFolderViewCB",
    "IShellFolderViewDual",
    "IShellFolderViewDual2",
    "IShellFolderViewDual3",
    "IShellIcon",
    "IShellIconOverlay",
    "IShellIconOverlayIdentifier",
    "IShellIconOverlayManager",
    "IShellImageData",
    "IShellImageDataAbort",
    "IShellImageDataFactory",
    "IShellItem",
    "IShellItem2",
    "IShellItemArray",
    "IShellItemFilter",
    "IShellItemImageFactory",
    "IShellItemResources",
    "IShellLibrary",
    "IShellLinkA",
    "IShellLinkDataList",
    "IShellLinkDual",
    "IShellLinkDual2",
    "IShellLinkW",
    "IShellMenu",
    "IShellMenuCallback",
    "IShellNameSpace",
    "IShellPropSheetExt",
    "IShellRunDll",
    "IShellService",
    "IShellTaskScheduler",
    "IShellUIHelper",
    "IShellUIHelper2",
    "IShellUIHelper3",
    "IShellUIHelper4",
    "IShellUIHelper5",
    "IShellUIHelper6",
    "IShellUIHelper7",
    "IShellUIHelper8",
    "IShellUIHelper9",
    "IShellView",
    "IShellView2",
    "IShellView3",
    "IShellWindows",
    "ISortColumnArray",
    "IStartMenuPinnedList",
    "IStorageProviderBanners",
    "IStorageProviderCopyHook",
    "IStorageProviderHandler",
    "IStorageProviderPropertyHandler",
    "IStreamAsync",
    "IStreamUnbufferedInfo",
    "IStream_Copy",
    "IStream_Read",
    "IStream_ReadPidl",
    "IStream_ReadStr",
    "IStream_Reset",
    "IStream_Size",
    "IStream_Write",
    "IStream_WritePidl",
    "IStream_WriteStr",
    "ISuspensionDependencyManager",
    "ISyncMgrConflict",
    "ISyncMgrConflictFolder",
    "ISyncMgrConflictItems",
    "ISyncMgrConflictPresenter",
    "ISyncMgrConflictResolutionItems",
    "ISyncMgrConflictResolveInfo",
    "ISyncMgrConflictStore",
    "ISyncMgrControl",
    "ISyncMgrEnumItems",
    "ISyncMgrEvent",
    "ISyncMgrEventLinkUIOperation",
    "ISyncMgrEventStore",
    "ISyncMgrHandler",
    "ISyncMgrHandlerCollection",
    "ISyncMgrHandlerInfo",
    "ISyncMgrRegister",
    "ISyncMgrResolutionHandler",
    "ISyncMgrScheduleWizardUIOperation",
    "ISyncMgrSessionCreator",
    "ISyncMgrSyncCallback",
    "ISyncMgrSyncItem",
    "ISyncMgrSyncItemContainer",
    "ISyncMgrSyncItemInfo",
    "ISyncMgrSyncResult",
    "ISyncMgrSynchronize",
    "ISyncMgrSynchronizeCallback",
    "ISyncMgrSynchronizeInvoke",
    "ISyncMgrUIOperation",
    "ITEMSPACING",
    "ITSAT_DEFAULT_PRIORITY",
    "ITSAT_MAX_PRIORITY",
    "ITSAT_MIN_PRIORITY",
    "ITSSFLAG_COMPLETE_ON_DESTROY",
    "ITSSFLAG_FLAGS_MASK",
    "ITSSFLAG_KILL_ON_DESTROY",
    "ITaskbarList",
    "ITaskbarList2",
    "ITaskbarList3",
    "ITaskbarList4",
    "IThumbnailCache",
    "IThumbnailCachePrimer",
    "IThumbnailCapture",
    "IThumbnailHandlerFactory",
    "IThumbnailProvider",
    "IThumbnailSettings",
    "IThumbnailStreamCache",
    "ITrackShellMenu",
    "ITranscodeImage",
    "ITransferAdviseSink",
    "ITransferDestination",
    "ITransferMediumItem",
    "ITransferSource",
    "ITravelEntry",
    "ITravelLog",
    "ITravelLogClient",
    "ITravelLogEntry",
    "ITravelLogStg",
    "ITrayDeskBand",
    "IURLSearchHook",
    "IURLSearchHook2",
    "IURL_INVOKECOMMAND_FLAGS",
    "IURL_INVOKECOMMAND_FL_ALLOW_UI",
    "IURL_INVOKECOMMAND_FL_ASYNCOK",
    "IURL_INVOKECOMMAND_FL_DDEWAIT",
    "IURL_INVOKECOMMAND_FL_LOG_USAGE",
    "IURL_INVOKECOMMAND_FL_USE_DEFAULT_VERB",
    "IURL_SETURL_FLAGS",
    "IURL_SETURL_FL_GUESS_PROTOCOL",
    "IURL_SETURL_FL_USE_DEFAULT_PROTOCOL",
    "IUniformResourceLocatorA",
    "IUniformResourceLocatorW",
    "IUnknown_AtomicRelease",
    "IUnknown_GetSite",
    "IUnknown_GetWindow",
    "IUnknown_QueryService",
    "IUnknown_Set",
    "IUnknown_SetSite",
    "IUpdateIDList",
    "IUseToBrowseItem",
    "IUserAccountChangeCallback",
    "IUserNotification",
    "IUserNotification2",
    "IUserNotificationCallback",
    "IViewStateIdentityItem",
    "IVirtualDesktopManager",
    "IVisualProperties",
    "IWebBrowser",
    "IWebBrowser2",
    "IWebBrowserApp",
    "IWebWizardExtension",
    "IWebWizardHost",
    "IWebWizardHost2",
    "IWizardExtension",
    "IWizardSite",
    "Identity_LocalUserProvider",
    "ImageProperties",
    "ImageRecompress",
    "ImageTranscode",
    "ImportPrivacySettings",
    "InitNetworkAddressControl",
    "InputPanelConfiguration",
    "InternetExplorer",
    "InternetExplorerMedium",
    "InternetPrintOrdering",
    "IntlStrEqWorkerA",
    "IntlStrEqWorkerW",
    "IsCharSpaceA",
    "IsCharSpaceW",
    "IsInternetESCEnabled",
    "IsLFNDriveA",
    "IsLFNDriveW",
    "IsNetDrive",
    "IsOS",
    "IsUserAnAdmin",
    "ItemCount_Property_GUID",
    "ItemIndex_Property_GUID",
    "KDC_FREQUENT",
    "KDC_RECENT",
    "KFDF_LOCAL_REDIRECT_ONLY",
    "KFDF_NO_REDIRECT_UI",
    "KFDF_PRECREATE",
    "KFDF_PUBLISHEXPANDEDPATH",
    "KFDF_ROAMABLE",
    "KFDF_STREAM",
    "KF_CATEGORY",
    "KF_CATEGORY_COMMON",
    "KF_CATEGORY_FIXED",
    "KF_CATEGORY_PERUSER",
    "KF_CATEGORY_VIRTUAL",
    "KF_FLAG_ALIAS_ONLY",
    "KF_FLAG_CREATE",
    "KF_FLAG_DEFAULT",
    "KF_FLAG_DEFAULT_PATH",
    "KF_FLAG_DONT_UNEXPAND",
    "KF_FLAG_DONT_VERIFY",
    "KF_FLAG_FORCE_APPCONTAINER_REDIRECTION",
    "KF_FLAG_FORCE_APP_DATA_REDIRECTION",
    "KF_FLAG_FORCE_PACKAGE_REDIRECTION",
    "KF_FLAG_INIT",
    "KF_FLAG_NOT_PARENT_RELATIVE",
    "KF_FLAG_NO_ALIAS",
    "KF_FLAG_NO_APPCONTAINER_REDIRECTION",
    "KF_FLAG_NO_PACKAGE_REDIRECTION",
    "KF_FLAG_RETURN_FILTER_REDIRECTION_TARGET",
    "KF_FLAG_SIMPLE_IDLIST",
    "KF_REDIRECTION_CAPABILITIES_ALLOW_ALL",
    "KF_REDIRECTION_CAPABILITIES_DENY_ALL",
    "KF_REDIRECTION_CAPABILITIES_DENY_PERMISSIONS",
    "KF_REDIRECTION_CAPABILITIES_DENY_POLICY",
    "KF_REDIRECTION_CAPABILITIES_DENY_POLICY_REDIRECTED",
    "KF_REDIRECTION_CAPABILITIES_REDIRECTABLE",
    "KF_REDIRECT_CHECK_ONLY",
    "KF_REDIRECT_COPY_CONTENTS",
    "KF_REDIRECT_COPY_SOURCE_DACL",
    "KF_REDIRECT_DEL_SOURCE_CONTENTS",
    "KF_REDIRECT_EXCLUDE_ALL_KNOWN_SUBFOLDERS",
    "KF_REDIRECT_OWNER_USER",
    "KF_REDIRECT_PIN",
    "KF_REDIRECT_SET_OWNER_EXPLICIT",
    "KF_REDIRECT_UNPIN",
    "KF_REDIRECT_USER_EXCLUSIVE",
    "KF_REDIRECT_WITH_UI",
    "KNOWNDESTCATEGORY",
    "KNOWNFOLDER_DEFINITION",
    "KNOWN_FOLDER_FLAG",
    "KnownFolderManager",
    "LFF_ALLITEMS",
    "LFF_FORCEFILESYSTEM",
    "LFF_STORAGEITEMS",
    "LIBRARYFOLDERFILTER",
    "LIBRARYMANAGEDIALOGOPTIONS",
    "LIBRARYOPTIONFLAGS",
    "LIBRARYSAVEFLAGS",
    "LIBRARY_E_NO_ACCESSIBLE_LOCATION",
    "LIBRARY_E_NO_SAVE_LOCATION",
    "LINK_E_DELETE",
    "LMD_ALLOWUNINDEXABLENETWORKLOCATIONS",
    "LMD_DEFAULT",
    "LOF_DEFAULT",
    "LOF_MASK_ALL",
    "LOF_PINNEDTONAVPANE",
    "LPFNDFMCALLBACK",
    "LPFNVIEWCALLBACK",
    "LSF_FAILIFTHERE",
    "LSF_MAKEUNIQUENAME",
    "LSF_OVERRIDEEXISTING",
    "LoadUserProfileA",
    "LoadUserProfileW",
    "LocalThumbnailCache",
    "MAV_APP_VISIBLE",
    "MAV_NO_APP_VISIBLE",
    "MAV_UNKNOWN",
    "MAXFILELEN",
    "MAX_COLUMN_DESC_LEN",
    "MAX_COLUMN_NAME_LEN",
    "MAX_SYNCMGRHANDLERNAME",
    "MAX_SYNCMGRITEMNAME",
    "MAX_SYNCMGR_ID",
    "MAX_SYNCMGR_NAME",
    "MAX_SYNCMGR_PROGRESSTEXT",
    "MBHANDCID_PIDLSELECT",
    "MENUBANDHANDLERCID",
    "MENUPOPUPPOPUPFLAGS",
    "MENUPOPUPSELECT",
    "MERGE_UPDATE_STATUS",
    "MIMEASSOCDLG_FL_REGISTER_ASSOC",
    "MIMEASSOCIATIONDIALOG_IN_FLAGS",
    "MM_ADDSEPARATOR",
    "MM_DONTREMOVESEPS",
    "MM_FLAGS",
    "MM_SUBMENUSHAVEIDS",
    "MONITOR_APP_VISIBILITY",
    "MPOS_CANCELLEVEL",
    "MPOS_CHILDTRACKING",
    "MPOS_EXECUTE",
    "MPOS_FULLCANCEL",
    "MPOS_SELECTLEFT",
    "MPOS_SELECTRIGHT",
    "MPPF_ALIGN_LEFT",
    "MPPF_ALIGN_RIGHT",
    "MPPF_BOTTOM",
    "MPPF_FINALSELECT",
    "MPPF_FORCEZORDER",
    "MPPF_INITIALSELECT",
    "MPPF_KEYBOARD",
    "MPPF_LEFT",
    "MPPF_NOANIMATE",
    "MPPF_POS_MASK",
    "MPPF_REPOSITION",
    "MPPF_RIGHT",
    "MPPF_SETFOCUS",
    "MPPF_TOP",
    "MULTIKEYHELPA",
    "MULTIKEYHELPW",
    "MUS_COMPLETE",
    "MUS_FAILED",
    "MUS_USERINPUTNEEDED",
    "MailRecipient",
    "MergedCategorizer",
    "NAMESPACEWALKFLAG",
    "NATIVE_DISPLAY_ORIENTATION",
    "NCM_DISPLAYERRORTIP",
    "NCM_GETADDRESS",
    "NCM_GETALLOWTYPE",
    "NCM_SETALLOWTYPE",
    "NC_ADDRESS",
    "NDO_LANDSCAPE",
    "NDO_PORTRAIT",
    "NETCACHE_E_NEGATIVE_CACHE",
    "NEWCPLINFOA",
    "NEWCPLINFOW",
    "NIF_GUID",
    "NIF_ICON",
    "NIF_INFO",
    "NIF_MESSAGE",
    "NIF_REALTIME",
    "NIF_SHOWTIP",
    "NIF_STATE",
    "NIF_TIP",
    "NIIF_ERROR",
    "NIIF_ICON_MASK",
    "NIIF_INFO",
    "NIIF_LARGE_ICON",
    "NIIF_NONE",
    "NIIF_NOSOUND",
    "NIIF_RESPECT_QUIET_TIME",
    "NIIF_USER",
    "NIIF_WARNING",
    "NIM_ADD",
    "NIM_DELETE",
    "NIM_MODIFY",
    "NIM_SETFOCUS",
    "NIM_SETVERSION",
    "NINF_KEY",
    "NIN_BALLOONHIDE",
    "NIN_BALLOONSHOW",
    "NIN_BALLOONTIMEOUT",
    "NIN_BALLOONUSERCLICK",
    "NIN_POPUPCLOSE",
    "NIN_POPUPOPEN",
    "NIN_SELECT",
    "NIS_HIDDEN",
    "NIS_SHAREDICON",
    "NMCII_FOLDERS",
    "NMCII_ITEMS",
    "NMCII_NONE",
    "NMCSAEI_EDIT",
    "NMCSAEI_SELECT",
    "NOTIFYICONDATAA",
    "NOTIFYICONDATAW",
    "NOTIFYICONIDENTIFIER",
    "NOTIFYICON_VERSION",
    "NOTIFYICON_VERSION_4",
    "NOTIFY_ICON_DATA_FLAGS",
    "NOTIFY_ICON_INFOTIP_FLAGS",
    "NOTIFY_ICON_MESSAGE",
    "NOTIFY_ICON_STATE",
    "NPCredentialProvider",
    "NRESARRAY",
    "NSTCCUSTOMDRAW",
    "NSTCDHPOS_ONTOP",
    "NSTCECT_BUTTON",
    "NSTCECT_DBLCLICK",
    "NSTCECT_LBUTTON",
    "NSTCECT_MBUTTON",
    "NSTCECT_RBUTTON",
    "NSTCEHT_NOWHERE",
    "NSTCEHT_ONITEM",
    "NSTCEHT_ONITEMBUTTON",
    "NSTCEHT_ONITEMICON",
    "NSTCEHT_ONITEMINDENT",
    "NSTCEHT_ONITEMLABEL",
    "NSTCEHT_ONITEMRIGHT",
    "NSTCEHT_ONITEMSTATEICON",
    "NSTCEHT_ONITEMTABBUTTON",
    "NSTCFC_DELAY_REGISTER_NOTIFY",
    "NSTCFC_NONE",
    "NSTCFC_PINNEDITEMFILTERING",
    "NSTCFOLDERCAPABILITIES",
    "NSTCGNI",
    "NSTCGNI_CHILD",
    "NSTCGNI_FIRSTVISIBLE",
    "NSTCGNI_LASTVISIBLE",
    "NSTCGNI_NEXT",
    "NSTCGNI_NEXTVISIBLE",
    "NSTCGNI_PARENT",
    "NSTCGNI_PREV",
    "NSTCGNI_PREVVISIBLE",
    "NSTCIS_BOLD",
    "NSTCIS_DISABLED",
    "NSTCIS_EXPANDED",
    "NSTCIS_NONE",
    "NSTCIS_SELECTED",
    "NSTCIS_SELECTEDNOEXPAND",
    "NSTCRS_EXPANDED",
    "NSTCRS_HIDDEN",
    "NSTCRS_VISIBLE",
    "NSTCS2_DEFAULT",
    "NSTCS2_DISPLAYPADDING",
    "NSTCS2_DISPLAYPINNEDONLY",
    "NSTCS2_INTERRUPTNOTIFICATIONS",
    "NSTCS2_SHOWNULLSPACEMENU",
    "NSTCSTYLE2",
    "NSTCS_ALLOWJUNCTIONS",
    "NSTCS_AUTOHSCROLL",
    "NSTCS_BORDER",
    "NSTCS_CHECKBOXES",
    "NSTCS_DIMMEDCHECKBOXES",
    "NSTCS_DISABLEDRAGDROP",
    "NSTCS_EMPTYTEXT",
    "NSTCS_EVENHEIGHT",
    "NSTCS_EXCLUSIONCHECKBOXES",
    "NSTCS_FADEINOUTEXPANDOS",
    "NSTCS_FAVORITESMODE",
    "NSTCS_FULLROWSELECT",
    "NSTCS_HASEXPANDOS",
    "NSTCS_HASLINES",
    "NSTCS_HORIZONTALSCROLL",
    "NSTCS_NOEDITLABELS",
    "NSTCS_NOINDENTCHECKS",
    "NSTCS_NOINFOTIP",
    "NSTCS_NOORDERSTREAM",
    "NSTCS_NOREPLACEOPEN",
    "NSTCS_PARTIALCHECKBOXES",
    "NSTCS_RICHTOOLTIP",
    "NSTCS_ROOTHASEXPANDO",
    "NSTCS_SHOWDELETEBUTTON",
    "NSTCS_SHOWREFRESHBUTTON",
    "NSTCS_SHOWSELECTIONALWAYS",
    "NSTCS_SHOWTABSBUTTON",
    "NSTCS_SINGLECLICKEXPAND",
    "NSTCS_SPRINGEXPAND",
    "NSTCS_TABSTOP",
    "NSWF_ACCUMULATE_FOLDERS",
    "NSWF_ANY_IMPLIES_ALL",
    "NSWF_ASYNC",
    "NSWF_DEFAULT",
    "NSWF_DONT_ACCUMULATE_RESULT",
    "NSWF_DONT_RESOLVE_LINKS",
    "NSWF_DONT_SORT",
    "NSWF_DONT_TRAVERSE_LINKS",
    "NSWF_DONT_TRAVERSE_STREAM_JUNCTIONS",
    "NSWF_FILESYSTEM_ONLY",
    "NSWF_FLAG_VIEWORDER",
    "NSWF_IGNORE_AUTOPLAY_HIDA",
    "NSWF_NONE_IMPLIES_ALL",
    "NSWF_ONE_IMPLIES_ALL",
    "NSWF_SHOW_PROGRESS",
    "NSWF_TRAVERSE_STREAM_JUNCTIONS",
    "NSWF_USE_TRANSFER_MEDIUM",
    "NTSCS2_NEVERINSERTNONENUMERATED",
    "NTSCS2_NOSINGLETONAUTOEXPAND",
    "NT_CONSOLE_PROPS",
    "NT_CONSOLE_PROPS_SIG",
    "NT_FE_CONSOLE_PROPS",
    "NT_FE_CONSOLE_PROPS_SIG",
    "NUM_POINTS",
    "NWMF",
    "NWMF_FIRST",
    "NWMF_FORCETAB",
    "NWMF_FORCEWINDOW",
    "NWMF_FROMDIALOGCHILD",
    "NWMF_HTMLDIALOG",
    "NWMF_INACTIVETAB",
    "NWMF_OVERRIDEKEY",
    "NWMF_SHOWHELP",
    "NWMF_SUGGESTTAB",
    "NWMF_SUGGESTWINDOW",
    "NWMF_UNLOADING",
    "NWMF_USERALLOWED",
    "NWMF_USERINITED",
    "NWMF_USERREQUESTED",
    "NamespaceTreeControl",
    "NamespaceWalker",
    "NetworkConnections",
    "NetworkExplorerFolder",
    "NetworkPlaces",
    "NewProcessCauseConstants",
    "NewProcessCauseConstants_ProtectedModeRedirect",
    "OAIF_ALLOW_REGISTRATION",
    "OAIF_EXEC",
    "OAIF_FILE_IS_URI",
    "OAIF_FORCE_REGISTRATION",
    "OAIF_HIDE_REGISTRATION",
    "OAIF_REGISTER_EXT",
    "OAIF_URL_PROTOCOL",
    "OFASI_EDIT",
    "OFASI_OPENDESKTOP",
    "OFFLINE_STATUS_INCOMPLETE",
    "OFFLINE_STATUS_LOCAL",
    "OFFLINE_STATUS_REMOTE",
    "OFS_DIRTYCACHE",
    "OFS_INACTIVE",
    "OFS_OFFLINE",
    "OFS_ONLINE",
    "OFS_SERVERBACK",
    "OF_CAP_CANCLOSE",
    "OF_CAP_CANSWITCHTO",
    "OI_ASYNC",
    "OI_DEFAULT",
    "OPENASINFO",
    "OPENPROPS_INHIBITPIF",
    "OPENPROPS_NONE",
    "OPEN_AS_INFO_FLAGS",
    "OPEN_PRINTER_PROPS_INFOA",
    "OPEN_PRINTER_PROPS_INFOW",
    "OPPROGDLG_ALLOWUNDO",
    "OPPROGDLG_DEFAULT",
    "OPPROGDLG_DONTDISPLAYDESTPATH",
    "OPPROGDLG_DONTDISPLAYLOCATIONS",
    "OPPROGDLG_DONTDISPLAYSOURCEPATH",
    "OPPROGDLG_ENABLEPAUSE",
    "OPPROGDLG_NOMULTIDAYESTIMATES",
    "OS",
    "OS_ADVSERVER",
    "OS_ANYSERVER",
    "OS_APPLIANCE",
    "OS_DATACENTER",
    "OS_DOMAINMEMBER",
    "OS_EMBEDDED",
    "OS_FASTUSERSWITCHING",
    "OS_HOME",
    "OS_MEDIACENTER",
    "OS_MEORGREATER",
    "OS_NT",
    "OS_NT4ORGREATER",
    "OS_PERSONALTERMINALSERVER",
    "OS_PROFESSIONAL",
    "OS_SERVER",
    "OS_SERVERADMINUI",
    "OS_SMALLBUSINESSSERVER",
    "OS_TABLETPC",
    "OS_TERMINALCLIENT",
    "OS_TERMINALREMOTEADMIN",
    "OS_TERMINALSERVER",
    "OS_WEBSERVER",
    "OS_WELCOMELOGONUI",
    "OS_WIN2000ADVSERVER",
    "OS_WIN2000DATACENTER",
    "OS_WIN2000ORGREATER",
    "OS_WIN2000PRO",
    "OS_WIN2000SERVER",
    "OS_WIN2000TERMINAL",
    "OS_WIN95ORGREATER",
    "OS_WIN95_GOLD",
    "OS_WIN98ORGREATER",
    "OS_WIN98_GOLD",
    "OS_WINDOWS",
    "OS_WOW6432",
    "OS_XPORGREATER",
    "OfflineFolderStatus",
    "OleSaveToStreamEx",
    "OnexCredentialProvider",
    "OnexPlapSmartcardCredentialProvider",
    "OpenControlPanel",
    "OpenRegStream",
    "PACKAGE_EXECUTION_STATE",
    "PAI_ASSIGNEDTIME",
    "PAI_EXPIRETIME",
    "PAI_PUBLISHEDTIME",
    "PAI_SCHEDULEDTIME",
    "PAI_SOURCE",
    "PANE_NAVIGATION",
    "PANE_NONE",
    "PANE_OFFLINE",
    "PANE_PRINTER",
    "PANE_PRIVACY",
    "PANE_PROGRESS",
    "PANE_SSL",
    "PANE_ZONE",
    "PAPPCONSTRAIN_CHANGE_ROUTINE",
    "PAPPSTATE_CHANGE_ROUTINE",
    "PARSEDURLA",
    "PARSEDURLW",
    "PATHCCH_ALLOW_LONG_PATHS",
    "PATHCCH_CANONICALIZE_SLASHES",
    "PATHCCH_DO_NOT_NORMALIZE_SEGMENTS",
    "PATHCCH_ENSURE_IS_EXTENDED_LENGTH_PATH",
    "PATHCCH_ENSURE_TRAILING_SLASH",
    "PATHCCH_FORCE_DISABLE_LONG_NAME_PROCESS",
    "PATHCCH_FORCE_ENABLE_LONG_NAME_PROCESS",
    "PATHCCH_MAX_CCH",
    "PATHCCH_NONE",
    "PATHCCH_OPTIONS",
    "PCS_FATAL",
    "PCS_PATHTOOLONG",
    "PCS_REMOVEDCHAR",
    "PCS_REPLACEDCHAR",
    "PCS_RET",
    "PCS_TRUNCATED",
    "PDM_DEFAULT",
    "PDM_ERRORSBLOCKING",
    "PDM_INDETERMINATE",
    "PDM_PREFLIGHT",
    "PDM_RUN",
    "PDM_UNDOING",
    "PDTIMER_PAUSE",
    "PDTIMER_RESET",
    "PDTIMER_RESUME",
    "PERSIST_FOLDER_TARGET_INFO",
    "PES_RUNNING",
    "PES_SUSPENDED",
    "PES_SUSPENDING",
    "PES_TERMINATED",
    "PES_UNKNOWN",
    "PFNCANSHAREFOLDERW",
    "PFNSHOWSHAREFOLDERUIW",
    "PIDASI_AVG_DATA_RATE",
    "PIDASI_CHANNEL_COUNT",
    "PIDASI_COMPRESSION",
    "PIDASI_FORMAT",
    "PIDASI_SAMPLE_RATE",
    "PIDASI_SAMPLE_SIZE",
    "PIDASI_STREAM_NAME",
    "PIDASI_STREAM_NUMBER",
    "PIDASI_TIMELENGTH",
    "PIDDRSI_DESCRIPTION",
    "PIDDRSI_PLAYCOUNT",
    "PIDDRSI_PLAYEXPIRES",
    "PIDDRSI_PLAYSTARTS",
    "PIDDRSI_PROTECTED",
    "PIDISF_CACHEDSTICKY",
    "PIDISF_CACHEIMAGES",
    "PIDISF_FLAGS",
    "PIDISF_FOLLOWALLLINKS",
    "PIDISF_RECENTLYCHANGED",
    "PIDISM_DONTWATCH",
    "PIDISM_GLOBAL",
    "PIDISM_OPTIONS",
    "PIDISM_WATCH",
    "PIDISR_INFO",
    "PIDISR_NEEDS_ADD",
    "PIDISR_NEEDS_DELETE",
    "PIDISR_NEEDS_UPDATE",
    "PIDISR_UP_TO_DATE",
    "PIDSI_ALBUM",
    "PIDSI_ARTIST",
    "PIDSI_COMMENT",
    "PIDSI_GENRE",
    "PIDSI_LYRICS",
    "PIDSI_SONGTITLE",
    "PIDSI_TRACK",
    "PIDSI_YEAR",
    "PIDVSI_COMPRESSION",
    "PIDVSI_DATA_RATE",
    "PIDVSI_FRAME_COUNT",
    "PIDVSI_FRAME_HEIGHT",
    "PIDVSI_FRAME_RATE",
    "PIDVSI_FRAME_WIDTH",
    "PIDVSI_SAMPLE_SIZE",
    "PIDVSI_STREAM_NAME",
    "PIDVSI_STREAM_NUMBER",
    "PIDVSI_TIMELENGTH",
    "PID_COMPUTERNAME",
    "PID_CONTROLPANEL_CATEGORY",
    "PID_DESCRIPTIONID",
    "PID_DISPLACED_DATE",
    "PID_DISPLACED_FROM",
    "PID_DISPLAY_PROPERTIES",
    "PID_FINDDATA",
    "PID_HTMLINFOTIPFILE",
    "PID_INTROTEXT",
    "PID_INTSITE",
    "PID_INTSITE_AUTHOR",
    "PID_INTSITE_CODEPAGE",
    "PID_INTSITE_COMMENT",
    "PID_INTSITE_CONTENTCODE",
    "PID_INTSITE_CONTENTLEN",
    "PID_INTSITE_DESCRIPTION",
    "PID_INTSITE_FLAGS",
    "PID_INTSITE_ICONFILE",
    "PID_INTSITE_ICONINDEX",
    "PID_INTSITE_LASTMOD",
    "PID_INTSITE_LASTVISIT",
    "PID_INTSITE_RECURSE",
    "PID_INTSITE_ROAMED",
    "PID_INTSITE_SUBSCRIPTION",
    "PID_INTSITE_TITLE",
    "PID_INTSITE_TRACKING",
    "PID_INTSITE_URL",
    "PID_INTSITE_VISITCOUNT",
    "PID_INTSITE_WATCH",
    "PID_INTSITE_WHATSNEW",
    "PID_IS",
    "PID_IS_AUTHOR",
    "PID_IS_COMMENT",
    "PID_IS_DESCRIPTION",
    "PID_IS_HOTKEY",
    "PID_IS_ICONFILE",
    "PID_IS_ICONINDEX",
    "PID_IS_NAME",
    "PID_IS_ROAMED",
    "PID_IS_SHOWCMD",
    "PID_IS_URL",
    "PID_IS_WHATSNEW",
    "PID_IS_WORKINGDIR",
    "PID_LINK_TARGET",
    "PID_LINK_TARGET_TYPE",
    "PID_MISC_ACCESSCOUNT",
    "PID_MISC_OWNER",
    "PID_MISC_PICS",
    "PID_MISC_STATUS",
    "PID_NETRESOURCE",
    "PID_NETWORKLOCATION",
    "PID_QUERY_RANK",
    "PID_SHARE_CSC_STATUS",
    "PID_SYNC_COPY_IN",
    "PID_VOLUME_CAPACITY",
    "PID_VOLUME_FILESYSTEM",
    "PID_VOLUME_FREE",
    "PID_WHICHFOLDER",
    "PIFDEFFILESIZE",
    "PIFDEFPATHSIZE",
    "PIFMAXFILEPATH",
    "PIFNAMESIZE",
    "PIFPARAMSSIZE",
    "PIFSHDATASIZE",
    "PIFSHPROGSIZE",
    "PIFSTARTLOCSIZE",
    "PINLogonCredentialProvider",
    "PLATFORM_BROWSERONLY",
    "PLATFORM_IE3",
    "PLATFORM_INTEGRATED",
    "PLATFORM_UNKNOWN",
    "PMSF_DONT_STRIP_SPACES",
    "PMSF_MULTIPLE",
    "PMSF_NORMAL",
    "PO_DELETE",
    "PO_PORTCHANGE",
    "PO_RENAME",
    "PO_REN_PORT",
    "PPCF_ADDARGUMENTS",
    "PPCF_ADDQUOTES",
    "PPCF_FORCEQUALIFY",
    "PPCF_LONGESTPOSSIBLE",
    "PPCF_NODIRECTORIES",
    "PREVIEWHANDLERFRAMEINFO",
    "PRF_DONTFINDLNK",
    "PRF_FIRSTDIRDEF",
    "PRF_FLAGS",
    "PRF_REQUIREABSOLUTE",
    "PRF_TRYPROGRAMEXTENSIONS",
    "PRF_VERIFYEXISTS",
    "PRINTACTION_DOCUMENTDEFAULTS",
    "PRINTACTION_NETINSTALL",
    "PRINTACTION_NETINSTALLLINK",
    "PRINTACTION_OPEN",
    "PRINTACTION_OPENNETPRN",
    "PRINTACTION_PROPERTIES",
    "PRINTACTION_SERVERPROPERTIES",
    "PRINTACTION_TESTPAGE",
    "PRINT_PROP_FORCE_NAME",
    "PROFILEINFOA",
    "PROFILEINFOW",
    "PROGDLG_AUTOTIME",
    "PROGDLG_MARQUEEPROGRESS",
    "PROGDLG_MODAL",
    "PROGDLG_NOCANCEL",
    "PROGDLG_NOMINIMIZE",
    "PROGDLG_NOPROGRESSBAR",
    "PROGDLG_NORMAL",
    "PROGDLG_NOTIME",
    "PROPSTR_EXTENSIONCOMPLETIONSTATE",
    "PROP_CONTRACT_DELEGATE",
    "PUBAPPINFO",
    "PUBAPPINFOFLAGS",
    "PackageDebugSettings",
    "ParseURLA",
    "ParseURLW",
    "PasswordCredentialProvider",
    "PathAddBackslashA",
    "PathAddBackslashW",
    "PathAddExtensionA",
    "PathAddExtensionW",
    "PathAllocCanonicalize",
    "PathAllocCombine",
    "PathAppendA",
    "PathAppendW",
    "PathBuildRootA",
    "PathBuildRootW",
    "PathCanonicalizeA",
    "PathCanonicalizeW",
    "PathCchAddBackslash",
    "PathCchAddBackslashEx",
    "PathCchAddExtension",
    "PathCchAppend",
    "PathCchAppendEx",
    "PathCchCanonicalize",
    "PathCchCanonicalizeEx",
    "PathCchCombine",
    "PathCchCombineEx",
    "PathCchFindExtension",
    "PathCchIsRoot",
    "PathCchRemoveBackslash",
    "PathCchRemoveBackslashEx",
    "PathCchRemoveExtension",
    "PathCchRemoveFileSpec",
    "PathCchRenameExtension",
    "PathCchSkipRoot",
    "PathCchStripPrefix",
    "PathCchStripToRoot",
    "PathCleanupSpec",
    "PathCombineA",
    "PathCombineW",
    "PathCommonPrefixA",
    "PathCommonPrefixW",
    "PathCompactPathA",
    "PathCompactPathExA",
    "PathCompactPathExW",
    "PathCompactPathW",
    "PathCreateFromUrlA",
    "PathCreateFromUrlAlloc",
    "PathCreateFromUrlW",
    "PathFileExistsA",
    "PathFileExistsW",
    "PathFindExtensionA",
    "PathFindExtensionW",
    "PathFindFileNameA",
    "PathFindFileNameW",
    "PathFindNextComponentA",
    "PathFindNextComponentW",
    "PathFindOnPathA",
    "PathFindOnPathW",
    "PathFindSuffixArrayA",
    "PathFindSuffixArrayW",
    "PathGetArgsA",
    "PathGetArgsW",
    "PathGetCharTypeA",
    "PathGetCharTypeW",
    "PathGetDriveNumberA",
    "PathGetDriveNumberW",
    "PathGetShortPath",
    "PathIsContentTypeA",
    "PathIsContentTypeW",
    "PathIsDirectoryA",
    "PathIsDirectoryEmptyA",
    "PathIsDirectoryEmptyW",
    "PathIsDirectoryW",
    "PathIsExe",
    "PathIsFileSpecA",
    "PathIsFileSpecW",
    "PathIsLFNFileSpecA",
    "PathIsLFNFileSpecW",
    "PathIsNetworkPathA",
    "PathIsNetworkPathW",
    "PathIsPrefixA",
    "PathIsPrefixW",
    "PathIsRelativeA",
    "PathIsRelativeW",
    "PathIsRootA",
    "PathIsRootW",
    "PathIsSameRootA",
    "PathIsSameRootW",
    "PathIsSlowA",
    "PathIsSlowW",
    "PathIsSystemFolderA",
    "PathIsSystemFolderW",
    "PathIsUNCA",
    "PathIsUNCEx",
    "PathIsUNCServerA",
    "PathIsUNCServerShareA",
    "PathIsUNCServerShareW",
    "PathIsUNCServerW",
    "PathIsUNCW",
    "PathIsURLA",
    "PathIsURLW",
    "PathMakePrettyA",
    "PathMakePrettyW",
    "PathMakeSystemFolderA",
    "PathMakeSystemFolderW",
    "PathMakeUniqueName",
    "PathMatchSpecA",
    "PathMatchSpecExA",
    "PathMatchSpecExW",
    "PathMatchSpecW",
    "PathParseIconLocationA",
    "PathParseIconLocationW",
    "PathQualify",
    "PathQuoteSpacesA",
    "PathQuoteSpacesW",
    "PathRelativePathToA",
    "PathRelativePathToW",
    "PathRemoveArgsA",
    "PathRemoveArgsW",
    "PathRemoveBackslashA",
    "PathRemoveBackslashW",
    "PathRemoveBlanksA",
    "PathRemoveBlanksW",
    "PathRemoveExtensionA",
    "PathRemoveExtensionW",
    "PathRemoveFileSpecA",
    "PathRemoveFileSpecW",
    "PathRenameExtensionA",
    "PathRenameExtensionW",
    "PathResolve",
    "PathSearchAndQualifyA",
    "PathSearchAndQualifyW",
    "PathSetDlgItemPathA",
    "PathSetDlgItemPathW",
    "PathSkipRootA",
    "PathSkipRootW",
    "PathStripPathA",
    "PathStripPathW",
    "PathStripToRootA",
    "PathStripToRootW",
    "PathUnExpandEnvStringsA",
    "PathUnExpandEnvStringsW",
    "PathUndecorateA",
    "PathUndecorateW",
    "PathUnmakeSystemFolderA",
    "PathUnmakeSystemFolderW",
    "PathUnquoteSpacesA",
    "PathUnquoteSpacesW",
    "PathYetAnotherMakeUniqueName",
    "PickIconDlg",
    "PreviousVersions",
    "PropertiesUI",
    "PublishDropTarget",
    "PublishingWizard",
    "QCMINFO",
    "QCMINFO_IDMAP",
    "QCMINFO_IDMAP_PLACEMENT",
    "QCMINFO_PLACE_AFTER",
    "QCMINFO_PLACE_BEFORE",
    "QIF_CACHED",
    "QIF_DONTEXPANDFOLDER",
    "QISearch",
    "QITAB",
    "QITIPF_DEFAULT",
    "QITIPF_FLAGS",
    "QITIPF_LINKNOTARGET",
    "QITIPF_LINKUSETARGET",
    "QITIPF_SINGLELINE",
    "QITIPF_USENAME",
    "QITIPF_USESLOWTIP",
    "QUERY_USER_NOTIFICATION_STATE",
    "QUNS_ACCEPTS_NOTIFICATIONS",
    "QUNS_APP",
    "QUNS_BUSY",
    "QUNS_NOT_PRESENT",
    "QUNS_PRESENTATION_MODE",
    "QUNS_QUIET_TIME",
    "QUNS_RUNNING_D3D_FULL_SCREEN",
    "QueryCancelAutoPlay",
    "RASProvider",
    "REFRESH_COMPLETELY",
    "REFRESH_IFEXPIRED",
    "REFRESH_NORMAL",
    "RESTRICTIONS",
    "REST_ALLOWBITBUCKDRIVES",
    "REST_ALLOWCOMMENTTOGGLE",
    "REST_ALLOWFILECLSIDJUNCTIONS",
    "REST_ALLOWLEGACYWEBVIEW",
    "REST_ALLOWUNHASHEDWEBVIEW",
    "REST_ARP_DONTGROUPPATCHES",
    "REST_ARP_NOADDPAGE",
    "REST_ARP_NOARP",
    "REST_ARP_NOCHOOSEPROGRAMSPAGE",
    "REST_ARP_NOREMOVEPAGE",
    "REST_ARP_NOWINSETUPPAGE",
    "REST_ARP_ShowPostSetup",
    "REST_BITBUCKCONFIRMDELETE",
    "REST_BITBUCKNOPROP",
    "REST_BITBUCKNUKEONDELETE",
    "REST_CLASSICSHELL",
    "REST_CLEARRECENTDOCSONEXIT",
    "REST_DISALLOWCPL",
    "REST_DISALLOWRUN",
    "REST_DONTRETRYBADNETNAME",
    "REST_DONTSHOWSUPERHIDDEN",
    "REST_ENFORCESHELLEXTSECURITY",
    "REST_ENUMWORKGROUP",
    "REST_FORCEACTIVEDESKTOPON",
    "REST_FORCECOPYACLWITHFILE",
    "REST_FORCESTARTMENULOGOFF",
    "REST_GREYMSIADS",
    "REST_HASFINDCOMPUTERS",
    "REST_HIDECLOCK",
    "REST_HIDERUNASVERB",
    "REST_INHERITCONSOLEHANDLES",
    "REST_INTELLIMENUS",
    "REST_LINKRESOLVEIGNORELINKINFO",
    "REST_MYCOMPNOPROP",
    "REST_MYDOCSNOPROP",
    "REST_MYDOCSONNET",
    "REST_MaxRecentDocs",
    "REST_NOACTIVEDESKTOP",
    "REST_NOACTIVEDESKTOPCHANGES",
    "REST_NOADDDESKCOMP",
    "REST_NOAUTOTRAYNOTIFY",
    "REST_NOCDBURNING",
    "REST_NOCHANGEMAPPEDDRIVECOMMENT",
    "REST_NOCHANGEMAPPEDDRIVELABEL",
    "REST_NOCHANGESTARMENU",
    "REST_NOCHANGINGWALLPAPER",
    "REST_NOCLOSE",
    "REST_NOCLOSEDESKCOMP",
    "REST_NOCLOSE_DRAGDROPBAND",
    "REST_NOCOLORCHOICE",
    "REST_NOCOMMONGROUPS",
    "REST_NOCONTROLPANEL",
    "REST_NOCONTROLPANELBARRICADE",
    "REST_NOCSC",
    "REST_NOCURRENTUSERRUN",
    "REST_NOCURRENTUSERRUNONCE",
    "REST_NOCUSTOMIZETHISFOLDER",
    "REST_NOCUSTOMIZEWEBVIEW",
    "REST_NODELDESKCOMP",
    "REST_NODESKCOMP",
    "REST_NODESKTOP",
    "REST_NODESKTOPCLEANUP",
    "REST_NODISCONNECT",
    "REST_NODISPBACKGROUND",
    "REST_NODISPLAYAPPEARANCEPAGE",
    "REST_NODISPLAYCPL",
    "REST_NODISPSCREENSAVEPG",
    "REST_NODISPSCREENSAVEPREVIEW",
    "REST_NODISPSETTINGSPG",
    "REST_NODRIVEAUTORUN",
    "REST_NODRIVES",
    "REST_NODRIVETYPEAUTORUN",
    "REST_NOEDITDESKCOMP",
    "REST_NOENCRYPTION",
    "REST_NOENCRYPTONMOVE",
    "REST_NOENTIRENETWORK",
    "REST_NOENUMENTIRENETWORK",
    "REST_NOEXITTODOS",
    "REST_NOFAVORITESMENU",
    "REST_NOFILEASSOCIATE",
    "REST_NOFILEMENU",
    "REST_NOFIND",
    "REST_NOFOLDEROPTIONS",
    "REST_NOFORGETSOFTWAREUPDATE",
    "REST_NOHARDWARETAB",
    "REST_NOHTMLWALLPAPER",
    "REST_NOINTERNETICON",
    "REST_NOINTERNETOPENWITH",
    "REST_NOLOCALMACHINERUN",
    "REST_NOLOCALMACHINERUNONCE",
    "REST_NOLOWDISKSPACECHECKS",
    "REST_NOMANAGEMYCOMPUTERVERB",
    "REST_NOMOVINGBAND",
    "REST_NOMYCOMPUTERICON",
    "REST_NONE",
    "REST_NONETCONNECTDISCONNECT",
    "REST_NONETCRAWL",
    "REST_NONETHOOD",
    "REST_NONETWORKCONNECTIONS",
    "REST_NONLEGACYSHELLMODE",
    "REST_NOONLINEPRINTSWIZARD",
    "REST_NOPRINTERADD",
    "REST_NOPRINTERDELETE",
    "REST_NOPRINTERTABS",
    "REST_NOPUBLISHWIZARD",
    "REST_NORECENTDOCSHISTORY",
    "REST_NORECENTDOCSMENU",
    "REST_NOREMOTECHANGENOTIFY",
    "REST_NOREMOTERECURSIVEEVENTS",
    "REST_NORESOLVESEARCH",
    "REST_NORESOLVETRACK",
    "REST_NORUN",
    "REST_NORUNASINSTALLPROMPT",
    "REST_NOSAVESET",
    "REST_NOSECURITY",
    "REST_NOSETACTIVEDESKTOP",
    "REST_NOSETFOLDERS",
    "REST_NOSETTASKBAR",
    "REST_NOSETTINGSASSIST",
    "REST_NOSHAREDDOCUMENTS",
    "REST_NOSHELLSEARCHBUTTON",
    "REST_NOSIZECHOICE",
    "REST_NOSMBALLOONTIP",
    "REST_NOSMCONFIGUREPROGRAMS",
    "REST_NOSMEJECTPC",
    "REST_NOSMHELP",
    "REST_NOSMMFUPROGRAMS",
    "REST_NOSMMOREPROGRAMS",
    "REST_NOSMMYDOCS",
    "REST_NOSMMYMUSIC",
    "REST_NOSMMYPICS",
    "REST_NOSMNETWORKPLACES",
    "REST_NOSMPINNEDLIST",
    "REST_NOSTARTMENUSUBFOLDERS",
    "REST_NOSTARTPAGE",
    "REST_NOSTARTPANEL",
    "REST_NOSTRCMPLOGICAL",
    "REST_NOTASKGROUPING",
    "REST_NOTHEMESTAB",
    "REST_NOTHUMBNAILCACHE",
    "REST_NOTOOLBARSONTASKBAR",
    "REST_NOTRAYCONTEXTMENU",
    "REST_NOTRAYITEMSDISPLAY",
    "REST_NOUPDATEWINDOWS",
    "REST_NOUPNPINSTALL",
    "REST_NOUSERNAMEINSTARTPANEL",
    "REST_NOVIEWCONTEXTMENU",
    "REST_NOVIEWONDRIVE",
    "REST_NOVISUALSTYLECHOICE",
    "REST_NOWEB",
    "REST_NOWEBSERVICES",
    "REST_NOWEBVIEW",
    "REST_NOWELCOMESCREEN",
    "REST_NOWINKEYS",
    "REST_PROMPTRUNASINSTALLNETPATH",
    "REST_RESTRICTCPL",
    "REST_RESTRICTRUN",
    "REST_REVERTWEBVIEWSECURITY",
    "REST_RUNDLGMEMCHECKBOX",
    "REST_SEPARATEDESKTOPPROCESS",
    "REST_SETVISUALSTYLE",
    "REST_STARTBANNER",
    "REST_STARTMENULOGOFF",
    "REST_STARTRUNNOHOMEPATH",
    "ReadCabinetState",
    "RealDriveType",
    "RefreshConstants",
    "RegisterAppConstrainedChangeNotification",
    "RegisterAppStateChangeNotification",
    "RegisterScaleChangeEvent",
    "RegisterScaleChangeNotifications",
    "RemoveWindowSubclass",
    "RestartDialog",
    "RestartDialogEx",
    "RevokeScaleChangeNotifications",
    "SBSC_HIDE",
    "SBSC_QUERY",
    "SBSC_SHOW",
    "SBSC_TOGGLE",
    "SBSP_ABSOLUTE",
    "SBSP_ACTIVATE_NOFOCUS",
    "SBSP_ALLOW_AUTONAVIGATE",
    "SBSP_CALLERUNTRUSTED",
    "SBSP_CREATENOHISTORY",
    "SBSP_DEFBROWSER",
    "SBSP_DEFMODE",
    "SBSP_EXPLOREMODE",
    "SBSP_FEEDNAVIGATION",
    "SBSP_HELPMODE",
    "SBSP_INITIATEDBYHLINKFRAME",
    "SBSP_KEEPSAMETEMPLATE",
    "SBSP_KEEPWORDWHEELTEXT",
    "SBSP_NAVIGATEBACK",
    "SBSP_NAVIGATEFORWARD",
    "SBSP_NEWBROWSER",
    "SBSP_NOAUTOSELECT",
    "SBSP_NOTRANSFERHIST",
    "SBSP_OPENMODE",
    "SBSP_PARENT",
    "SBSP_PLAYNOSOUND",
    "SBSP_REDIRECT",
    "SBSP_RELATIVE",
    "SBSP_SAMEBROWSER",
    "SBSP_TRUSTEDFORACTIVEX",
    "SBSP_TRUSTFIRSTDOWNLOAD",
    "SBSP_UNTRUSTEDFORDOWNLOAD",
    "SBSP_WRITENOHISTORY",
    "SCALE_CHANGE_FLAGS",
    "SCF_PHYSICAL",
    "SCF_SCALE",
    "SCF_VALUE_NONE",
    "SCHEME_CREATE",
    "SCHEME_DISPLAY",
    "SCHEME_DONOTUSE",
    "SCHEME_EDIT",
    "SCHEME_GLOBAL",
    "SCHEME_LOCAL",
    "SCHEME_REFRESH",
    "SCHEME_UPDATE",
    "SCNRT_DISABLE",
    "SCNRT_ENABLE",
    "SCNRT_STATUS",
    "SCRM_VERIFYPW",
    "SECURELOCKCODE",
    "SECURELOCK_FIRSTSUGGEST",
    "SECURELOCK_NOCHANGE",
    "SECURELOCK_SET_FORTEZZA",
    "SECURELOCK_SET_MIXED",
    "SECURELOCK_SET_SECURE128BIT",
    "SECURELOCK_SET_SECURE40BIT",
    "SECURELOCK_SET_SECURE56BIT",
    "SECURELOCK_SET_SECUREUNKNOWNBIT",
    "SECURELOCK_SET_UNSECURE",
    "SECURELOCK_SUGGEST_FORTEZZA",
    "SECURELOCK_SUGGEST_MIXED",
    "SECURELOCK_SUGGEST_SECURE128BIT",
    "SECURELOCK_SUGGEST_SECURE40BIT",
    "SECURELOCK_SUGGEST_SECURE56BIT",
    "SECURELOCK_SUGGEST_SECUREUNKNOWNBIT",
    "SECURELOCK_SUGGEST_UNSECURE",
    "SEE_MASK_ASYNCOK",
    "SEE_MASK_CLASSKEY",
    "SEE_MASK_CLASSNAME",
    "SEE_MASK_CONNECTNETDRV",
    "SEE_MASK_DEFAULT",
    "SEE_MASK_DOENVSUBST",
    "SEE_MASK_FLAG_DDEWAIT",
    "SEE_MASK_FLAG_HINST_IS_SITE",
    "SEE_MASK_FLAG_LOG_USAGE",
    "SEE_MASK_FLAG_NO_UI",
    "SEE_MASK_HMONITOR",
    "SEE_MASK_HOTKEY",
    "SEE_MASK_ICON",
    "SEE_MASK_IDLIST",
    "SEE_MASK_INVOKEIDLIST",
    "SEE_MASK_NOASYNC",
    "SEE_MASK_NOCLOSEPROCESS",
    "SEE_MASK_NOQUERYCLASSSTORE",
    "SEE_MASK_NOZONECHECKS",
    "SEE_MASK_NO_CONSOLE",
    "SEE_MASK_UNICODE",
    "SEE_MASK_WAITFORINPUTIDLE",
    "SETPROPS_NONE",
    "SE_ERR_ACCESSDENIED",
    "SE_ERR_ASSOCINCOMPLETE",
    "SE_ERR_DDEBUSY",
    "SE_ERR_DDEFAIL",
    "SE_ERR_DDETIMEOUT",
    "SE_ERR_DLLNOTFOUND",
    "SE_ERR_FNF",
    "SE_ERR_NOASSOC",
    "SE_ERR_OOM",
    "SE_ERR_PNF",
    "SE_ERR_SHARE",
    "SFBID_PIDLCHANGED",
    "SFBS_FLAGS",
    "SFBS_FLAGS_ROUND_TO_NEAREST_DISPLAYED_DIGIT",
    "SFBS_FLAGS_TRUNCATE_UNDISPLAYED_DECIMAL_DIGITS",
    "SFVM_ADDOBJECT",
    "SFVM_ADDPROPERTYPAGES",
    "SFVM_BACKGROUNDENUM",
    "SFVM_BACKGROUNDENUMDONE",
    "SFVM_COLUMNCLICK",
    "SFVM_DEFITEMCOUNT",
    "SFVM_DEFVIEWMODE",
    "SFVM_DIDDRAGDROP",
    "SFVM_FSNOTIFY",
    "SFVM_GETANIMATION",
    "SFVM_GETBUTTONINFO",
    "SFVM_GETBUTTONS",
    "SFVM_GETDETAILSOF",
    "SFVM_GETHELPTEXT",
    "SFVM_GETHELPTOPIC",
    "SFVM_GETNOTIFY",
    "SFVM_GETPANE",
    "SFVM_GETSELECTEDOBJECTS",
    "SFVM_GETSORTDEFAULTS",
    "SFVM_GETTOOLTIPTEXT",
    "SFVM_GETZONE",
    "SFVM_HELPTOPIC_DATA",
    "SFVM_INITMENUPOPUP",
    "SFVM_INVOKECOMMAND",
    "SFVM_MERGEMENU",
    "SFVM_MESSAGE_ID",
    "SFVM_PROPPAGE_DATA",
    "SFVM_QUERYFSNOTIFY",
    "SFVM_REARRANGE",
    "SFVM_REMOVEOBJECT",
    "SFVM_SETCLIPBOARD",
    "SFVM_SETISFV",
    "SFVM_SETITEMPOS",
    "SFVM_SETPOINTS",
    "SFVM_SIZE",
    "SFVM_THISIDLIST",
    "SFVM_UNMERGEMENU",
    "SFVM_UPDATEOBJECT",
    "SFVM_UPDATESTATUSBAR",
    "SFVM_WINDOWCREATED",
    "SFVSOC_INVALIDATE_ALL",
    "SFVSOC_NOSCROLL",
    "SFVS_SELECT",
    "SFVS_SELECT_ALLITEMS",
    "SFVS_SELECT_INVERT",
    "SFVS_SELECT_NONE",
    "SFVVO_DESKTOPHTML",
    "SFVVO_DOUBLECLICKINWEBVIEW",
    "SFVVO_SHOWALLOBJECTS",
    "SFVVO_SHOWCOMPCOLOR",
    "SFVVO_SHOWEXTENSIONS",
    "SFVVO_SHOWSYSFILES",
    "SFVVO_WIN95CLASSIC",
    "SFV_CREATE",
    "SFV_SETITEMPOS",
    "SHACF_AUTOAPPEND_FORCE_OFF",
    "SHACF_AUTOAPPEND_FORCE_ON",
    "SHACF_AUTOSUGGEST_FORCE_OFF",
    "SHACF_AUTOSUGGEST_FORCE_ON",
    "SHACF_DEFAULT",
    "SHACF_FILESYSTEM",
    "SHACF_FILESYS_DIRS",
    "SHACF_FILESYS_ONLY",
    "SHACF_URLALL",
    "SHACF_URLHISTORY",
    "SHACF_URLMRU",
    "SHACF_USETAB",
    "SHACF_VIRTUAL_NAMESPACE",
    "SHARD",
    "SHARDAPPIDINFO",
    "SHARDAPPIDINFOIDLIST",
    "SHARDAPPIDINFOLINK",
    "SHARD_APPIDINFO",
    "SHARD_APPIDINFOIDLIST",
    "SHARD_APPIDINFOLINK",
    "SHARD_LINK",
    "SHARD_PATHA",
    "SHARD_PATHW",
    "SHARD_PIDL",
    "SHARD_SHELLITEM",
    "SHARE_ROLE",
    "SHARE_ROLE_CONTRIBUTOR",
    "SHARE_ROLE_CO_OWNER",
    "SHARE_ROLE_CUSTOM",
    "SHARE_ROLE_INVALID",
    "SHARE_ROLE_MIXED",
    "SHARE_ROLE_OWNER",
    "SHARE_ROLE_READER",
    "SHAddFromPropSheetExtArray",
    "SHAddToRecentDocs",
    "SHAlloc",
    "SHAllocShared",
    "SHAnsiToAnsi",
    "SHAnsiToUnicode",
    "SHAppBarMessage",
    "SHAssocEnumHandlers",
    "SHAssocEnumHandlersForProtocolByApplication",
    "SHAutoComplete",
    "SHBindToFolderIDListParent",
    "SHBindToFolderIDListParentEx",
    "SHBindToObject",
    "SHBindToParent",
    "SHBrowseForFolderA",
    "SHBrowseForFolderW",
    "SHCDF_UPDATEITEM",
    "SHCIDS_ALLFIELDS",
    "SHCIDS_BITMASK",
    "SHCIDS_CANONICALONLY",
    "SHCIDS_COLUMNMASK",
    "SHCLSIDFromString",
    "SHCNEE_MSI_CHANGE",
    "SHCNEE_MSI_UNINSTALL",
    "SHCNEE_ORDERCHANGED",
    "SHCNE_ALLEVENTS",
    "SHCNE_ASSOCCHANGED",
    "SHCNE_ATTRIBUTES",
    "SHCNE_CREATE",
    "SHCNE_DELETE",
    "SHCNE_DISKEVENTS",
    "SHCNE_DRIVEADD",
    "SHCNE_DRIVEADDGUI",
    "SHCNE_DRIVEREMOVED",
    "SHCNE_EXTENDED_EVENT",
    "SHCNE_FREESPACE",
    "SHCNE_GLOBALEVENTS",
    "SHCNE_ID",
    "SHCNE_INTERRUPT",
    "SHCNE_MEDIAINSERTED",
    "SHCNE_MEDIAREMOVED",
    "SHCNE_MKDIR",
    "SHCNE_NETSHARE",
    "SHCNE_NETUNSHARE",
    "SHCNE_RENAMEFOLDER",
    "SHCNE_RENAMEITEM",
    "SHCNE_RMDIR",
    "SHCNE_SERVERDISCONNECT",
    "SHCNE_UPDATEDIR",
    "SHCNE_UPDATEIMAGE",
    "SHCNE_UPDATEITEM",
    "SHCNF_DWORD",
    "SHCNF_FLAGS",
    "SHCNF_FLUSH",
    "SHCNF_FLUSHNOWAIT",
    "SHCNF_IDLIST",
    "SHCNF_NOTIFYRECURSIVE",
    "SHCNF_PATH",
    "SHCNF_PATHA",
    "SHCNF_PATHW",
    "SHCNF_PRINTER",
    "SHCNF_PRINTERA",
    "SHCNF_PRINTERW",
    "SHCNF_TYPE",
    "SHCNRF_InterruptLevel",
    "SHCNRF_NewDelivery",
    "SHCNRF_RecursiveInterrupt",
    "SHCNRF_SOURCE",
    "SHCNRF_ShellLevel",
    "SHCOLUMNDATA",
    "SHCOLUMNINFO",
    "SHCOLUMNINIT",
    "SHCONTF_CHECKING_FOR_CHILDREN",
    "SHCONTF_ENABLE_ASYNC",
    "SHCONTF_FASTITEMS",
    "SHCONTF_FLATLIST",
    "SHCONTF_FOLDERS",
    "SHCONTF_INCLUDEHIDDEN",
    "SHCONTF_INCLUDESUPERHIDDEN",
    "SHCONTF_INIT_ON_FIRST_NEXT",
    "SHCONTF_NAVIGATION_ENUM",
    "SHCONTF_NETPRINTERSRCH",
    "SHCONTF_NONFOLDERS",
    "SHCONTF_SHAREABLE",
    "SHCONTF_STORAGE",
    "SHCREATEPROCESSINFOW",
    "SHC_E_SHELL_COMPONENT_STARTUP_FAILURE",
    "SHChangeDWORDAsIDList",
    "SHChangeNotification_Lock",
    "SHChangeNotification_Unlock",
    "SHChangeNotify",
    "SHChangeNotifyDeregister",
    "SHChangeNotifyEntry",
    "SHChangeNotifyRegister",
    "SHChangeNotifyRegisterThread",
    "SHChangeProductKeyAsIDList",
    "SHChangeUpdateImageIDList",
    "SHCloneSpecialIDList",
    "SHCoCreateInstance",
    "SHCopyKeyA",
    "SHCopyKeyW",
    "SHCreateAssociationRegistration",
    "SHCreateDataObject",
    "SHCreateDefaultContextMenu",
    "SHCreateDefaultExtractIcon",
    "SHCreateDefaultPropertiesOp",
    "SHCreateDirectory",
    "SHCreateDirectoryExA",
    "SHCreateDirectoryExW",
    "SHCreateFileExtractIconW",
    "SHCreateItemFromIDList",
    "SHCreateItemFromParsingName",
    "SHCreateItemFromRelativeName",
    "SHCreateItemInKnownFolder",
    "SHCreateItemWithParent",
    "SHCreateMemStream",
    "SHCreateProcessAsUserW",
    "SHCreatePropSheetExtArray",
    "SHCreateQueryCancelAutoPlayMoniker",
    "SHCreateShellFolderView",
    "SHCreateShellFolderViewEx",
    "SHCreateShellItem",
    "SHCreateShellItemArray",
    "SHCreateShellItemArrayFromDataObject",
    "SHCreateShellItemArrayFromIDLists",
    "SHCreateShellItemArrayFromShellItem",
    "SHCreateShellPalette",
    "SHCreateStdEnumFmtEtc",
    "SHCreateStreamOnFileA",
    "SHCreateStreamOnFileEx",
    "SHCreateStreamOnFileW",
    "SHCreateThread",
    "SHCreateThreadRef",
    "SHCreateThreadWithHandle",
    "SHDESCRIPTIONID",
    "SHDID_COMPUTER_AUDIO",
    "SHDID_COMPUTER_CDROM",
    "SHDID_COMPUTER_DRIVE35",
    "SHDID_COMPUTER_DRIVE525",
    "SHDID_COMPUTER_FIXED",
    "SHDID_COMPUTER_IMAGING",
    "SHDID_COMPUTER_NETDRIVE",
    "SHDID_COMPUTER_OTHER",
    "SHDID_COMPUTER_RAMDISK",
    "SHDID_COMPUTER_REMOVABLE",
    "SHDID_COMPUTER_SHAREDDOCS",
    "SHDID_FS_DIRECTORY",
    "SHDID_FS_FILE",
    "SHDID_FS_OTHER",
    "SHDID_ID",
    "SHDID_MOBILE_DEVICE",
    "SHDID_NET_DOMAIN",
    "SHDID_NET_OTHER",
    "SHDID_NET_RESTOFNET",
    "SHDID_NET_SERVER",
    "SHDID_NET_SHARE",
    "SHDID_REMOTE_DESKTOP_DRIVE",
    "SHDID_ROOT_REGITEM",
    "SHDRAGIMAGE",
    "SHDefExtractIconA",
    "SHDefExtractIconW",
    "SHDeleteEmptyKeyA",
    "SHDeleteEmptyKeyW",
    "SHDeleteKeyA",
    "SHDeleteKeyW",
    "SHDeleteValueA",
    "SHDeleteValueW",
    "SHDestroyPropSheetExtArray",
    "SHDoDragDrop",
    "SHELLBROWSERSHOWCONTROL",
    "SHELLEXECUTEINFOA",
    "SHELLEXECUTEINFOW",
    "SHELLFLAGSTATE",
    "SHELLSTATEA",
    "SHELLSTATEVERSION_IE4",
    "SHELLSTATEVERSION_WIN2K",
    "SHELLSTATEW",
    "SHELL_AUTOCOMPLETE_FLAGS",
    "SHELL_E_WRONG_BITDEPTH",
    "SHELL_ITEM_RESOURCE",
    "SHELL_LINK_DATA_FLAGS",
    "SHELL_UI_COMPONENT",
    "SHELL_UI_COMPONENT_DESKBAND",
    "SHELL_UI_COMPONENT_NOTIFICATIONAREA",
    "SHELL_UI_COMPONENT_TASKBARS",
    "SHERB_NOCONFIRMATION",
    "SHERB_NOPROGRESSUI",
    "SHERB_NOSOUND",
    "SHEmptyRecycleBinA",
    "SHEmptyRecycleBinW",
    "SHEnumKeyExA",
    "SHEnumKeyExW",
    "SHEnumValueA",
    "SHEnumValueW",
    "SHEnumerateUnreadMailAccountsW",
    "SHEvaluateSystemCommandTemplate",
    "SHFILEINFOA",
    "SHFILEINFOW",
    "SHFILEOPSTRUCTA",
    "SHFILEOPSTRUCTW",
    "SHFMT_CANCEL",
    "SHFMT_ERROR",
    "SHFMT_ID",
    "SHFMT_ID_DEFAULT",
    "SHFMT_NOFORMAT",
    "SHFMT_OPT",
    "SHFMT_OPT_FULL",
    "SHFMT_OPT_NONE",
    "SHFMT_OPT_SYSONLY",
    "SHFMT_RET",
    "SHFOLDERCUSTOMSETTINGS",
    "SHFileOperationA",
    "SHFileOperationW",
    "SHFindFiles",
    "SHFind_InitMenuPopup",
    "SHFlushSFCache",
    "SHFormatDateTimeA",
    "SHFormatDateTimeW",
    "SHFormatDrive",
    "SHFree",
    "SHFreeNameMappings",
    "SHFreeShared",
    "SHGDFIL_DESCRIPTIONID",
    "SHGDFIL_FINDDATA",
    "SHGDFIL_FORMAT",
    "SHGDFIL_NETRESOURCE",
    "SHGDNF",
    "SHGDN_FORADDRESSBAR",
    "SHGDN_FOREDITING",
    "SHGDN_FORPARSING",
    "SHGDN_INFOLDER",
    "SHGDN_NORMAL",
    "SHGFI_ADDOVERLAYS",
    "SHGFI_ATTRIBUTES",
    "SHGFI_ATTR_SPECIFIED",
    "SHGFI_DISPLAYNAME",
    "SHGFI_EXETYPE",
    "SHGFI_FLAGS",
    "SHGFI_ICON",
    "SHGFI_ICONLOCATION",
    "SHGFI_LARGEICON",
    "SHGFI_LINKOVERLAY",
    "SHGFI_OPENICON",
    "SHGFI_OVERLAYINDEX",
    "SHGFI_PIDL",
    "SHGFI_SELECTED",
    "SHGFI_SHELLICONSIZE",
    "SHGFI_SMALLICON",
    "SHGFI_SYSICONINDEX",
    "SHGFI_TYPENAME",
    "SHGFI_USEFILEATTRIBUTES",
    "SHGFP_TYPE",
    "SHGFP_TYPE_CURRENT",
    "SHGFP_TYPE_DEFAULT",
    "SHGLOBALCOUNTER",
    "SHGNLI_NOLNK",
    "SHGNLI_NOLOCNAME",
    "SHGNLI_NOUNIQUE",
    "SHGNLI_PIDL",
    "SHGNLI_PREFIXNAME",
    "SHGNLI_USEURLEXT",
    "SHGSI_FLAGS",
    "SHGSI_ICON",
    "SHGSI_ICONLOCATION",
    "SHGSI_LARGEICON",
    "SHGSI_LINKOVERLAY",
    "SHGSI_SELECTED",
    "SHGSI_SHELLICONSIZE",
    "SHGSI_SMALLICON",
    "SHGSI_SYSICONINDEX",
    "SHGVSPB_ALLFOLDERS",
    "SHGVSPB_ALLUSERS",
    "SHGVSPB_INHERIT",
    "SHGVSPB_NOAUTODEFAULTS",
    "SHGVSPB_PERFOLDER",
    "SHGVSPB_PERUSER",
    "SHGVSPB_ROAM",
    "SHGetAttributesFromDataObject",
    "SHGetDataFromIDListA",
    "SHGetDataFromIDListW",
    "SHGetDesktopFolder",
    "SHGetDiskFreeSpaceExA",
    "SHGetDiskFreeSpaceExW",
    "SHGetDriveMedia",
    "SHGetFileInfoA",
    "SHGetFileInfoW",
    "SHGetFolderLocation",
    "SHGetFolderPathA",
    "SHGetFolderPathAndSubDirA",
    "SHGetFolderPathAndSubDirW",
    "SHGetFolderPathW",
    "SHGetIDListFromObject",
    "SHGetIconOverlayIndexA",
    "SHGetIconOverlayIndexW",
    "SHGetImageList",
    "SHGetInstanceExplorer",
    "SHGetInverseCMAP",
    "SHGetItemFromDataObject",
    "SHGetItemFromObject",
    "SHGetKnownFolderIDList",
    "SHGetKnownFolderItem",
    "SHGetKnownFolderPath",
    "SHGetLocalizedName",
    "SHGetMalloc",
    "SHGetNameFromIDList",
    "SHGetNewLinkInfoA",
    "SHGetNewLinkInfoW",
    "SHGetPathFromIDListA",
    "SHGetPathFromIDListEx",
    "SHGetPathFromIDListW",
    "SHGetRealIDL",
    "SHGetSetFolderCustomSettings",
    "SHGetSetSettings",
    "SHGetSettings",
    "SHGetSpecialFolderLocation",
    "SHGetSpecialFolderPathA",
    "SHGetSpecialFolderPathW",
    "SHGetStockIconInfo",
    "SHGetTemporaryPropertyForItem",
    "SHGetThreadRef",
    "SHGetUnreadMailCountW",
    "SHGetValueA",
    "SHGetValueW",
    "SHGetViewStatePropertyBag",
    "SHGlobalCounterDecrement",
    "SHGlobalCounterGetValue",
    "SHGlobalCounterIncrement",
    "SHHLNF_NOAUTOSELECT",
    "SHHLNF_WRITENOHISTORY",
    "SHHandleUpdateImage",
    "SHILCreateFromPath",
    "SHIL_EXTRALARGE",
    "SHIL_JUMBO",
    "SHIL_LARGE",
    "SHIL_LAST",
    "SHIL_SMALL",
    "SHIL_SYSSMALL",
    "SHIMGDEC_DEFAULT",
    "SHIMGDEC_LOADFULL",
    "SHIMGDEC_THUMBNAIL",
    "SHIMGKEY_QUALITY",
    "SHIMGKEY_RAWFORMAT",
    "SHIMSTCAPFLAG_LOCKABLE",
    "SHIMSTCAPFLAG_PURGEABLE",
    "SHInvokePrinterCommandA",
    "SHInvokePrinterCommandW",
    "SHIsFileAvailableOffline",
    "SHIsLowMemoryMachine",
    "SHLimitInputEdit",
    "SHLoadInProc",
    "SHLoadIndirectString",
    "SHLoadNonloadedIconOverlayIdentifiers",
    "SHLockShared",
    "SHMapPIDLToSystemImageListIndex",
    "SHMessageBoxCheckA",
    "SHMessageBoxCheckW",
    "SHMultiFileProperties",
    "SHNAMEMAPPINGA",
    "SHNAMEMAPPINGW",
    "SHOP_FILEPATH",
    "SHOP_PRINTERNAME",
    "SHOP_TYPE",
    "SHOP_VOLUMEGUID",
    "SHObjectProperties",
    "SHOpenFolderAndSelectItems",
    "SHOpenPropSheetW",
    "SHOpenRegStream2A",
    "SHOpenRegStream2W",
    "SHOpenRegStreamA",
    "SHOpenRegStreamW",
    "SHOpenWithDialog",
    "SHPPFW_ASKDIRCREATE",
    "SHPPFW_DIRCREATE",
    "SHPPFW_IGNOREFILENAME",
    "SHPPFW_MEDIACHECKONLY",
    "SHPPFW_NONE",
    "SHPPFW_NOWRITECHECK",
    "SHPWHF_ANYLOCATION",
    "SHPWHF_NOFILESELECTOR",
    "SHPWHF_NONETPLACECREATE",
    "SHPWHF_NORECOMPRESS",
    "SHPWHF_USEMRU",
    "SHPWHF_VALIDATEVIAWEBFOLDERS",
    "SHParseDisplayName",
    "SHPathPrepareForWriteA",
    "SHPathPrepareForWriteW",
    "SHQUERYRBINFO",
    "SHQueryInfoKeyA",
    "SHQueryInfoKeyW",
    "SHQueryRecycleBinA",
    "SHQueryRecycleBinW",
    "SHQueryUserNotificationState",
    "SHQueryValueExA",
    "SHQueryValueExW",
    "SHREGDEL_BOTH",
    "SHREGDEL_DEFAULT",
    "SHREGDEL_FLAGS",
    "SHREGDEL_HKCU",
    "SHREGDEL_HKLM",
    "SHREGENUM_BOTH",
    "SHREGENUM_DEFAULT",
    "SHREGENUM_FLAGS",
    "SHREGENUM_HKCU",
    "SHREGENUM_HKLM",
    "SHREGSET_FORCE_HKCU",
    "SHREGSET_FORCE_HKLM",
    "SHREGSET_HKCU",
    "SHREGSET_HKLM",
    "SHRegCloseUSKey",
    "SHRegCreateUSKeyA",
    "SHRegCreateUSKeyW",
    "SHRegDeleteEmptyUSKeyA",
    "SHRegDeleteEmptyUSKeyW",
    "SHRegDeleteUSValueA",
    "SHRegDeleteUSValueW",
    "SHRegDuplicateHKey",
    "SHRegEnumUSKeyA",
    "SHRegEnumUSKeyW",
    "SHRegEnumUSValueA",
    "SHRegEnumUSValueW",
    "SHRegGetBoolUSValueA",
    "SHRegGetBoolUSValueW",
    "SHRegGetIntW",
    "SHRegGetPathA",
    "SHRegGetPathW",
    "SHRegGetUSValueA",
    "SHRegGetUSValueW",
    "SHRegGetValueA",
    "SHRegGetValueFromHKCUHKLM",
    "SHRegGetValueW",
    "SHRegOpenUSKeyA",
    "SHRegOpenUSKeyW",
    "SHRegQueryInfoUSKeyA",
    "SHRegQueryInfoUSKeyW",
    "SHRegQueryUSValueA",
    "SHRegQueryUSValueW",
    "SHRegSetPathA",
    "SHRegSetPathW",
    "SHRegSetUSValueA",
    "SHRegSetUSValueW",
    "SHRegWriteUSValueA",
    "SHRegWriteUSValueW",
    "SHReleaseThreadRef",
    "SHRemoveLocalizedName",
    "SHReplaceFromPropSheetExtArray",
    "SHResolveLibrary",
    "SHRestricted",
    "SHSTOCKICONID",
    "SHSTOCKICONINFO",
    "SHSendMessageBroadcastA",
    "SHSendMessageBroadcastW",
    "SHSetDefaultProperties",
    "SHSetFolderPathA",
    "SHSetFolderPathW",
    "SHSetInstanceExplorer",
    "SHSetKnownFolderPath",
    "SHSetLocalizedName",
    "SHSetTemporaryPropertyForItem",
    "SHSetThreadRef",
    "SHSetUnreadMailCountW",
    "SHSetValueA",
    "SHSetValueW",
    "SHShellFolderView_Message",
    "SHShowManageLibraryUI",
    "SHSimpleIDListFromPath",
    "SHSkipJunction",
    "SHStartNetConnectionDialogW",
    "SHStrDupA",
    "SHStrDupW",
    "SHStripMneumonicA",
    "SHStripMneumonicW",
    "SHTestTokenMembership",
    "SHUnicodeToAnsi",
    "SHUnicodeToUnicode",
    "SHUnlockShared",
    "SHUpdateImageA",
    "SHUpdateImageW",
    "SHValidateUNC",
    "SIATTRIBFLAGS",
    "SIATTRIBFLAGS_ALLITEMS",
    "SIATTRIBFLAGS_AND",
    "SIATTRIBFLAGS_APPCOMPAT",
    "SIATTRIBFLAGS_MASK",
    "SIATTRIBFLAGS_OR",
    "SICHINT_ALLFIELDS",
    "SICHINT_CANONICAL",
    "SICHINT_DISPLAY",
    "SICHINT_TEST_FILESYSPATH_IF_NOT_EQUAL",
    "SID_CommandsPropertyBag",
    "SID_CtxQueryAssociations",
    "SID_DefView",
    "SID_LaunchSourceAppUserModelId",
    "SID_LaunchSourceViewSizePreference",
    "SID_LaunchTargetViewSizePreference",
    "SID_MenuShellFolder",
    "SID_SCommDlgBrowser",
    "SID_SCommandBarState",
    "SID_SGetViewFromViewDual",
    "SID_SInPlaceBrowser",
    "SID_SMenuBandBKContextMenu",
    "SID_SMenuBandBottom",
    "SID_SMenuBandBottomSelected",
    "SID_SMenuBandChild",
    "SID_SMenuBandContextMenuModifier",
    "SID_SMenuBandParent",
    "SID_SMenuBandTop",
    "SID_SMenuPopup",
    "SID_SSearchBoxInfo",
    "SID_STopLevelBrowser",
    "SID_STopWindow",
    "SID_ShellExecuteNamedPropertyStore",
    "SID_URLExecutionContext",
    "SIGDN",
    "SIGDN_DESKTOPABSOLUTEEDITING",
    "SIGDN_DESKTOPABSOLUTEPARSING",
    "SIGDN_FILESYSPATH",
    "SIGDN_NORMALDISPLAY",
    "SIGDN_PARENTRELATIVE",
    "SIGDN_PARENTRELATIVEEDITING",
    "SIGDN_PARENTRELATIVEFORADDRESSBAR",
    "SIGDN_PARENTRELATIVEFORUI",
    "SIGDN_PARENTRELATIVEPARSING",
    "SIGDN_URL",
    "SIID_APPLICATION",
    "SIID_AUDIOFILES",
    "SIID_AUTOLIST",
    "SIID_CLUSTEREDDRIVE",
    "SIID_DELETE",
    "SIID_DESKTOPPC",
    "SIID_DEVICEAUDIOPLAYER",
    "SIID_DEVICECAMERA",
    "SIID_DEVICECELLPHONE",
    "SIID_DEVICEVIDEOCAMERA",
    "SIID_DOCASSOC",
    "SIID_DOCNOASSOC",
    "SIID_DRIVE35",
    "SIID_DRIVE525",
    "SIID_DRIVEBD",
    "SIID_DRIVECD",
    "SIID_DRIVEDVD",
    "SIID_DRIVEFIXED",
    "SIID_DRIVEHDDVD",
    "SIID_DRIVENET",
    "SIID_DRIVENETDISABLED",
    "SIID_DRIVERAM",
    "SIID_DRIVEREMOVE",
    "SIID_DRIVEUNKNOWN",
    "SIID_ERROR",
    "SIID_FIND",
    "SIID_FOLDER",
    "SIID_FOLDERBACK",
    "SIID_FOLDERFRONT",
    "SIID_FOLDEROPEN",
    "SIID_HELP",
    "SIID_IMAGEFILES",
    "SIID_INFO",
    "SIID_INTERNET",
    "SIID_KEY",
    "SIID_LINK",
    "SIID_LOCK",
    "SIID_MAX_ICONS",
    "SIID_MEDIAAUDIODVD",
    "SIID_MEDIABDR",
    "SIID_MEDIABDRE",
    "SIID_MEDIABDROM",
    "SIID_MEDIABLANKCD",
    "SIID_MEDIABLURAY",
    "SIID_MEDIACDAUDIO",
    "SIID_MEDIACDAUDIOPLUS",
    "SIID_MEDIACDBURN",
    "SIID_MEDIACDR",
    "SIID_MEDIACDROM",
    "SIID_MEDIACDRW",
    "SIID_MEDIACOMPACTFLASH",
    "SIID_MEDIADVD",
    "SIID_MEDIADVDPLUSR",
    "SIID_MEDIADVDPLUSRW",
    "SIID_MEDIADVDR",
    "SIID_MEDIADVDRAM",
    "SIID_MEDIADVDROM",
    "SIID_MEDIADVDRW",
    "SIID_MEDIAENHANCEDCD",
    "SIID_MEDIAENHANCEDDVD",
    "SIID_MEDIAHDDVD",
    "SIID_MEDIAHDDVDR",
    "SIID_MEDIAHDDVDRAM",
    "SIID_MEDIAHDDVDROM",
    "SIID_MEDIAMOVIEDVD",
    "SIID_MEDIASMARTMEDIA",
    "SIID_MEDIASVCD",
    "SIID_MEDIAVCD",
    "SIID_MIXEDFILES",
    "SIID_MOBILEPC",
    "SIID_MYNETWORK",
    "SIID_NETWORKCONNECT",
    "SIID_PRINTER",
    "SIID_PRINTERFAX",
    "SIID_PRINTERFAXNET",
    "SIID_PRINTERFILE",
    "SIID_PRINTERNET",
    "SIID_RECYCLER",
    "SIID_RECYCLERFULL",
    "SIID_RENAME",
    "SIID_SERVER",
    "SIID_SERVERSHARE",
    "SIID_SETTINGS",
    "SIID_SHARE",
    "SIID_SHIELD",
    "SIID_SLOWFILE",
    "SIID_SOFTWARE",
    "SIID_STACK",
    "SIID_STUFFEDFOLDER",
    "SIID_USERS",
    "SIID_VIDEOFILES",
    "SIID_WARNING",
    "SIID_WORLD",
    "SIID_ZIPFILE",
    "SIIGBF",
    "SIIGBF_BIGGERSIZEOK",
    "SIIGBF_CROPTOSQUARE",
    "SIIGBF_ICONBACKGROUND",
    "SIIGBF_ICONONLY",
    "SIIGBF_INCACHEONLY",
    "SIIGBF_MEMORYONLY",
    "SIIGBF_RESIZETOFIT",
    "SIIGBF_SCALEUP",
    "SIIGBF_THUMBNAILONLY",
    "SIIGBF_WIDETHUMBNAILS",
    "SIOM_ICONINDEX",
    "SIOM_OVERLAYINDEX",
    "SIOM_RESERVED_DEFAULT",
    "SIOM_RESERVED_LINK",
    "SIOM_RESERVED_SHARED",
    "SIOM_RESERVED_SLOWFILE",
    "SLDF_ALLOW_LINK_TO_LINK",
    "SLDF_DEFAULT",
    "SLDF_DISABLE_KNOWNFOLDER_RELATIVE_TRACKING",
    "SLDF_DISABLE_LINK_PATH_TRACKING",
    "SLDF_ENABLE_TARGET_METADATA",
    "SLDF_FORCE_NO_LINKINFO",
    "SLDF_FORCE_NO_LINKTRACK",
    "SLDF_FORCE_UNCNAME",
    "SLDF_HAS_ARGS",
    "SLDF_HAS_DARWINID",
    "SLDF_HAS_EXP_ICON_SZ",
    "SLDF_HAS_EXP_SZ",
    "SLDF_HAS_ICONLOCATION",
    "SLDF_HAS_ID_LIST",
    "SLDF_HAS_LINK_INFO",
    "SLDF_HAS_NAME",
    "SLDF_HAS_RELPATH",
    "SLDF_HAS_WORKINGDIR",
    "SLDF_KEEP_LOCAL_IDLIST_FOR_UNC_TARGET",
    "SLDF_NO_KF_ALIAS",
    "SLDF_NO_PIDL_ALIAS",
    "SLDF_PERSIST_VOLUME_ID_RELATIVE",
    "SLDF_PREFER_ENVIRONMENT_PATH",
    "SLDF_RESERVED",
    "SLDF_RUNAS_USER",
    "SLDF_RUN_IN_SEPARATE",
    "SLDF_RUN_WITH_SHIMLAYER",
    "SLDF_UNALIAS_ON_SAVE",
    "SLDF_UNICODE",
    "SLDF_VALID",
    "SLGP_FLAGS",
    "SLGP_RAWPATH",
    "SLGP_RELATIVEPRIORITY",
    "SLGP_SHORTPATH",
    "SLGP_UNCPRIORITY",
    "SLOWAPPINFO",
    "SLR_ANY_MATCH",
    "SLR_FLAGS",
    "SLR_INVOKE_MSI",
    "SLR_KNOWNFOLDER",
    "SLR_MACHINE_IN_LOCAL_TARGET",
    "SLR_NOLINKINFO",
    "SLR_NONE",
    "SLR_NOSEARCH",
    "SLR_NOTRACK",
    "SLR_NOUPDATE",
    "SLR_NO_OBJECT_ID",
    "SLR_NO_UI",
    "SLR_NO_UI_WITH_MSG_PUMP",
    "SLR_OFFER_DELETE_WITHOUT_FILE",
    "SLR_UPDATE",
    "SLR_UPDATE_MACHINE_AND_SID",
    "SMAE_CONTRACTED",
    "SMAE_EXPANDED",
    "SMAE_USER",
    "SMAE_VALID",
    "SMCSHCHANGENOTIFYSTRUCT",
    "SMC_AUTOEXPANDCHANGE",
    "SMC_CHEVRONEXPAND",
    "SMC_CHEVRONGETTIP",
    "SMC_CREATE",
    "SMC_DEFAULTICON",
    "SMC_DEMOTE",
    "SMC_DISPLAYCHEVRONTIP",
    "SMC_EXITMENU",
    "SMC_GETAUTOEXPANDSTATE",
    "SMC_GETBKCONTEXTMENU",
    "SMC_GETCONTEXTMENUMODIFIER",
    "SMC_GETINFO",
    "SMC_GETOBJECT",
    "SMC_GETSFINFO",
    "SMC_GETSFOBJECT",
    "SMC_INITMENU",
    "SMC_NEWITEM",
    "SMC_OPEN",
    "SMC_PROMOTE",
    "SMC_REFRESH",
    "SMC_SETSFOBJECT",
    "SMC_SFDDRESTRICTED",
    "SMC_SFEXEC",
    "SMC_SFEXEC_MIDDLE",
    "SMC_SFSELECTITEM",
    "SMC_SHCHANGENOTIFY",
    "SMDATA",
    "SMDM_HMENU",
    "SMDM_SHELLFOLDER",
    "SMDM_TOOLBAR",
    "SMIF_ACCELERATOR",
    "SMIF_ALTSTATE",
    "SMIF_CHECKED",
    "SMIF_DEMOTED",
    "SMIF_DISABLED",
    "SMIF_DRAGNDROP",
    "SMIF_DROPCASCADE",
    "SMIF_DROPTARGET",
    "SMIF_HIDDEN",
    "SMIF_ICON",
    "SMIF_NEW",
    "SMIF_SUBMENU",
    "SMIF_TRACKPOPUP",
    "SMIM_FLAGS",
    "SMIM_ICON",
    "SMIM_TYPE",
    "SMINFO",
    "SMINFOFLAGS",
    "SMINFOMASK",
    "SMINFOTYPE",
    "SMINIT_AUTOEXPAND",
    "SMINIT_AUTOTOOLTIP",
    "SMINIT_CACHED",
    "SMINIT_DEFAULT",
    "SMINIT_DROPONCONTAINER",
    "SMINIT_HORIZONTAL",
    "SMINIT_RESTRICT_DRAGDROP",
    "SMINIT_TOPLEVEL",
    "SMINIT_VERTICAL",
    "SMINV_ID",
    "SMINV_REFRESH",
    "SMIT_SEPARATOR",
    "SMIT_STRING",
    "SMSET_BOTTOM",
    "SMSET_DONTOWN",
    "SMSET_TOP",
    "SORTCOLUMN",
    "SORTDIRECTION",
    "SORT_ASCENDING",
    "SORT_DESCENDING",
    "SORT_ORDER_TYPE",
    "SOT_DEFAULT",
    "SOT_IGNORE_FOLDERNESS",
    "SPACTION",
    "SPACTION_APPLYINGATTRIBS",
    "SPACTION_CALCULATING",
    "SPACTION_COPYING",
    "SPACTION_COPY_MOVING",
    "SPACTION_DELETING",
    "SPACTION_DOWNLOADING",
    "SPACTION_FORMATTING",
    "SPACTION_MOVING",
    "SPACTION_NONE",
    "SPACTION_RECYCLING",
    "SPACTION_RENAMING",
    "SPACTION_SEARCHING_FILES",
    "SPACTION_SEARCHING_INTERNET",
    "SPACTION_UPLOADING",
    "SPBEGINF_AUTOTIME",
    "SPBEGINF_MARQUEEPROGRESS",
    "SPBEGINF_NOCANCELBUTTON",
    "SPBEGINF_NOPROGRESSBAR",
    "SPBEGINF_NORMAL",
    "SPFF_CREATED_ON_THIS_DEVICE",
    "SPFF_DOWNLOAD_BY_DEFAULT",
    "SPFF_NONE",
    "SPINITF_MODAL",
    "SPINITF_NOMINIMIZE",
    "SPINITF_NORMAL",
    "SPMODE_BROWSER",
    "SPMODE_DBMON",
    "SPMODE_DEBUGBREAK",
    "SPMODE_DEBUGOUT",
    "SPMODE_EVENT",
    "SPMODE_EVENTTRACE",
    "SPMODE_FLUSH",
    "SPMODE_FORMATTEXT",
    "SPMODE_MEMWATCH",
    "SPMODE_MSGTRACE",
    "SPMODE_MSVM",
    "SPMODE_MULTISTOP",
    "SPMODE_PERFTAGS",
    "SPMODE_PROFILE",
    "SPMODE_SHELL",
    "SPMODE_TEST",
    "SPTEXT",
    "SPTEXT_ACTIONDESCRIPTION",
    "SPTEXT_ACTIONDETAIL",
    "SRRF_NOEXPAND",
    "SRRF_NOVIRT",
    "SRRF_RM_ANY",
    "SRRF_RM_NORMAL",
    "SRRF_RM_SAFE",
    "SRRF_RM_SAFENETWORK",
    "SRRF_RT_ANY",
    "SRRF_RT_REG_BINARY",
    "SRRF_RT_REG_DWORD",
    "SRRF_RT_REG_EXPAND_SZ",
    "SRRF_RT_REG_MULTI_SZ",
    "SRRF_RT_REG_NONE",
    "SRRF_RT_REG_QWORD",
    "SRRF_RT_REG_SZ",
    "SRRF_ZEROONFAILURE",
    "SSF_AUTOCHECKSELECT",
    "SSF_DESKTOPHTML",
    "SSF_DONTPRETTYPATH",
    "SSF_DOUBLECLICKINWEBVIEW",
    "SSF_FILTER",
    "SSF_HIDDENFILEEXTS",
    "SSF_HIDEICONS",
    "SSF_ICONSONLY",
    "SSF_MAPNETDRVBUTTON",
    "SSF_MASK",
    "SSF_NOCONFIRMRECYCLE",
    "SSF_NONETCRAWLING",
    "SSF_SEPPROCESS",
    "SSF_SERVERADMINUI",
    "SSF_SHOWALLOBJECTS",
    "SSF_SHOWATTRIBCOL",
    "SSF_SHOWCOMPCOLOR",
    "SSF_SHOWEXTENSIONS",
    "SSF_SHOWINFOTIP",
    "SSF_SHOWSTARTPAGE",
    "SSF_SHOWSTATUSBAR",
    "SSF_SHOWSUPERHIDDEN",
    "SSF_SHOWSYSFILES",
    "SSF_SHOWTYPEOVERLAY",
    "SSF_SORTCOLUMNS",
    "SSF_STARTPANELON",
    "SSF_WEBVIEW",
    "SSF_WIN95CLASSIC",
    "SSM_CLEAR",
    "SSM_REFRESH",
    "SSM_SET",
    "SSM_UPDATE",
    "STGOP",
    "STGOP_APPLYPROPERTIES",
    "STGOP_COPY",
    "STGOP_MOVE",
    "STGOP_NEW",
    "STGOP_REMOVE",
    "STGOP_RENAME",
    "STGOP_SYNC",
    "STIF_DEFAULT",
    "STIF_SUPPORT_HEX",
    "STORAGE_PROVIDER_FILE_FLAGS",
    "STORE_E_NEWER_VERSION_AVAILABLE",
    "STPFLAG",
    "STPF_NONE",
    "STPF_USEAPPPEEKALWAYS",
    "STPF_USEAPPPEEKWHENACTIVE",
    "STPF_USEAPPTHUMBNAILALWAYS",
    "STPF_USEAPPTHUMBNAILWHENACTIVE",
    "STR_AVOID_DRIVE_RESTRICTION_POLICY",
    "STR_BIND_DELEGATE_CREATE_OBJECT",
    "STR_BIND_FOLDERS_READ_ONLY",
    "STR_BIND_FOLDER_ENUM_MODE",
    "STR_BIND_FORCE_FOLDER_SHORTCUT_RESOLVE",
    "STR_DONT_PARSE_RELATIVE",
    "STR_DONT_RESOLVE_LINK",
    "STR_ENUM_ITEMS_FLAGS",
    "STR_FILE_SYS_BIND_DATA",
    "STR_FILE_SYS_BIND_DATA_WIN7_FORMAT",
    "STR_GET_ASYNC_HANDLER",
    "STR_GPS_BESTEFFORT",
    "STR_GPS_DELAYCREATION",
    "STR_GPS_FASTPROPERTIESONLY",
    "STR_GPS_HANDLERPROPERTIESONLY",
    "STR_GPS_NO_OPLOCK",
    "STR_GPS_OPENSLOWITEM",
    "STR_INTERNAL_NAVIGATE",
    "STR_INTERNETFOLDER_PARSE_ONLY_URLMON_BINDABLE",
    "STR_ITEM_CACHE_CONTEXT",
    "STR_MYDOCS_CLSID",
    "STR_NO_VALIDATE_FILENAME_CHARS",
    "STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS",
    "STR_PARSE_AND_CREATE_ITEM",
    "STR_PARSE_DONT_REQUIRE_VALIDATED_URLS",
    "STR_PARSE_EXPLICIT_ASSOCIATION_SUCCESSFUL",
    "STR_PARSE_PARTIAL_IDLIST",
    "STR_PARSE_PREFER_FOLDER_BROWSING",
    "STR_PARSE_PREFER_WEB_BROWSING",
    "STR_PARSE_PROPERTYSTORE",
    "STR_PARSE_SHELL_PROTOCOL_TO_FILE_OBJECTS",
    "STR_PARSE_SHOW_NET_DIAGNOSTICS_UI",
    "STR_PARSE_SKIP_NET_CACHE",
    "STR_PARSE_TRANSLATE_ALIASES",
    "STR_PARSE_WITH_EXPLICIT_ASSOCAPP",
    "STR_PARSE_WITH_EXPLICIT_PROGID",
    "STR_PARSE_WITH_PROPERTIES",
    "STR_PROPERTYBAG_PARAM",
    "STR_REFERRER_IDENTIFIER",
    "STR_SKIP_BINDING_CLSID",
    "STR_STORAGEITEM_CREATION_FLAGS",
    "STR_TAB_REUSE_IDENTIFIER",
    "STR_TRACK_CLSID",
    "SUBCLASSPROC",
    "SV2CVW2_PARAMS",
    "SV3CVW3_DEFAULT",
    "SV3CVW3_FORCEFOLDERFLAGS",
    "SV3CVW3_FORCEVIEWMODE",
    "SV3CVW3_NONINTERACTIVE",
    "SVGIO_ALLVIEW",
    "SVGIO_BACKGROUND",
    "SVGIO_CHECKED",
    "SVGIO_FLAG_VIEWORDER",
    "SVGIO_SELECTION",
    "SVGIO_TYPE_MASK",
    "SVSI_CHECK",
    "SVSI_CHECK2",
    "SVSI_DESELECT",
    "SVSI_DESELECTOTHERS",
    "SVSI_EDIT",
    "SVSI_ENSUREVISIBLE",
    "SVSI_FOCUSED",
    "SVSI_KEYBOARDSELECT",
    "SVSI_NOTAKEFOCUS",
    "SVSI_POSITIONITEM",
    "SVSI_SELECT",
    "SVSI_SELECTIONMARK",
    "SVSI_TRANSLATEPT",
    "SVUIA_ACTIVATE_FOCUS",
    "SVUIA_ACTIVATE_NOFOCUS",
    "SVUIA_DEACTIVATE",
    "SVUIA_INPLACEACTIVATE",
    "SVUIA_STATUS",
    "SWC_3RDPARTY",
    "SWC_BROWSER",
    "SWC_CALLBACK",
    "SWC_DESKTOP",
    "SWC_EXPLORER",
    "SWFO_COOKIEPASSED",
    "SWFO_INCLUDEPENDING",
    "SWFO_NEEDDISPATCH",
    "SYNCMGRERRORFLAGS",
    "SYNCMGRERRORFLAG_ENABLEJUMPTEXT",
    "SYNCMGRFLAG",
    "SYNCMGRFLAG_CONNECT",
    "SYNCMGRFLAG_EVENTMASK",
    "SYNCMGRFLAG_IDLE",
    "SYNCMGRFLAG_INVOKE",
    "SYNCMGRFLAG_MANUAL",
    "SYNCMGRFLAG_MAYBOTHERUSER",
    "SYNCMGRFLAG_PENDINGDISCONNECT",
    "SYNCMGRFLAG_SCHEDULED",
    "SYNCMGRFLAG_SETTINGS",
    "SYNCMGRHANDLERFLAGS",
    "SYNCMGRHANDLERFLAG_MASK",
    "SYNCMGRHANDLERINFO",
    "SYNCMGRHANDLER_ALWAYSLISTHANDLER",
    "SYNCMGRHANDLER_HASPROPERTIES",
    "SYNCMGRHANDLER_HIDDEN",
    "SYNCMGRHANDLER_MAYESTABLISHCONNECTION",
    "SYNCMGRINVOKEFLAGS",
    "SYNCMGRINVOKE_MINIMIZED",
    "SYNCMGRINVOKE_STARTSYNC",
    "SYNCMGRITEM",
    "SYNCMGRITEMFLAGS",
    "SYNCMGRITEMSTATE",
    "SYNCMGRITEMSTATE_CHECKED",
    "SYNCMGRITEMSTATE_UNCHECKED",
    "SYNCMGRITEM_HASPROPERTIES",
    "SYNCMGRITEM_HIDDEN",
    "SYNCMGRITEM_ITEMFLAGMASK",
    "SYNCMGRITEM_LASTUPDATETIME",
    "SYNCMGRITEM_MAYDELETEITEM",
    "SYNCMGRITEM_ROAMINGUSER",
    "SYNCMGRITEM_TEMPORARY",
    "SYNCMGRLOGERRORINFO",
    "SYNCMGRLOGERROR_ERRORFLAGS",
    "SYNCMGRLOGERROR_ERRORID",
    "SYNCMGRLOGERROR_ITEMID",
    "SYNCMGRLOGLEVEL",
    "SYNCMGRLOGLEVEL_ERROR",
    "SYNCMGRLOGLEVEL_INFORMATION",
    "SYNCMGRLOGLEVEL_LOGLEVELMAX",
    "SYNCMGRLOGLEVEL_WARNING",
    "SYNCMGRPROGRESSITEM",
    "SYNCMGRPROGRESSITEM_MAXVALUE",
    "SYNCMGRPROGRESSITEM_PROGVALUE",
    "SYNCMGRPROGRESSITEM_STATUSTEXT",
    "SYNCMGRPROGRESSITEM_STATUSTYPE",
    "SYNCMGRREGISTERFLAGS",
    "SYNCMGRREGISTERFLAGS_MASK",
    "SYNCMGRREGISTERFLAG_CONNECT",
    "SYNCMGRREGISTERFLAG_IDLE",
    "SYNCMGRREGISTERFLAG_PENDINGDISCONNECT",
    "SYNCMGRSTATUS",
    "SYNCMGRSTATUS_DELETED",
    "SYNCMGRSTATUS_FAILED",
    "SYNCMGRSTATUS_PAUSED",
    "SYNCMGRSTATUS_PENDING",
    "SYNCMGRSTATUS_RESUMING",
    "SYNCMGRSTATUS_SKIPPED",
    "SYNCMGRSTATUS_STOPPED",
    "SYNCMGRSTATUS_SUCCEEDED",
    "SYNCMGRSTATUS_UPDATING",
    "SYNCMGRSTATUS_UPDATING_INDETERMINATE",
    "SYNCMGR_CANCEL_REQUEST",
    "SYNCMGR_CF_NONE",
    "SYNCMGR_CF_NOUI",
    "SYNCMGR_CF_NOWAIT",
    "SYNCMGR_CF_VALID",
    "SYNCMGR_CF_WAIT",
    "SYNCMGR_CIT_DELETED",
    "SYNCMGR_CIT_UPDATED",
    "SYNCMGR_CONFLICT_ID_INFO",
    "SYNCMGR_CONFLICT_ITEM_TYPE",
    "SYNCMGR_CONTROL_FLAGS",
    "SYNCMGR_CR_CANCEL_ALL",
    "SYNCMGR_CR_CANCEL_ITEM",
    "SYNCMGR_CR_MAX",
    "SYNCMGR_CR_NONE",
    "SYNCMGR_EF_NONE",
    "SYNCMGR_EF_VALID",
    "SYNCMGR_EL_ERROR",
    "SYNCMGR_EL_INFORMATION",
    "SYNCMGR_EL_MAX",
    "SYNCMGR_EL_WARNING",
    "SYNCMGR_EVENT_FLAGS",
    "SYNCMGR_EVENT_LEVEL",
    "SYNCMGR_HANDLER_CAPABILITIES",
    "SYNCMGR_HANDLER_POLICIES",
    "SYNCMGR_HANDLER_TYPE",
    "SYNCMGR_HCM_CAN_BROWSE_CONTENT",
    "SYNCMGR_HCM_CAN_SHOW_SCHEDULE",
    "SYNCMGR_HCM_CONFLICT_STORE",
    "SYNCMGR_HCM_EVENT_STORE",
    "SYNCMGR_HCM_NONE",
    "SYNCMGR_HCM_PROVIDES_ICON",
    "SYNCMGR_HCM_QUERY_BEFORE_ACTIVATE",
    "SYNCMGR_HCM_QUERY_BEFORE_DEACTIVATE",
    "SYNCMGR_HCM_QUERY_BEFORE_DISABLE",
    "SYNCMGR_HCM_QUERY_BEFORE_ENABLE",
    "SYNCMGR_HCM_SUPPORTS_CONCURRENT_SESSIONS",
    "SYNCMGR_HCM_VALID_MASK",
    "SYNCMGR_HPM_BACKGROUND_SYNC_ONLY",
    "SYNCMGR_HPM_DISABLE_BROWSE",
    "SYNCMGR_HPM_DISABLE_DISABLE",
    "SYNCMGR_HPM_DISABLE_ENABLE",
    "SYNCMGR_HPM_DISABLE_SCHEDULE",
    "SYNCMGR_HPM_DISABLE_START_SYNC",
    "SYNCMGR_HPM_DISABLE_STOP_SYNC",
    "SYNCMGR_HPM_HIDDEN_BY_DEFAULT",
    "SYNCMGR_HPM_NONE",
    "SYNCMGR_HPM_PREVENT_ACTIVATE",
    "SYNCMGR_HPM_PREVENT_DEACTIVATE",
    "SYNCMGR_HPM_PREVENT_DISABLE",
    "SYNCMGR_HPM_PREVENT_ENABLE",
    "SYNCMGR_HPM_PREVENT_START_SYNC",
    "SYNCMGR_HPM_PREVENT_STOP_SYNC",
    "SYNCMGR_HPM_VALID_MASK",
    "SYNCMGR_HT_APPLICATION",
    "SYNCMGR_HT_COMPUTER",
    "SYNCMGR_HT_DEVICE",
    "SYNCMGR_HT_FOLDER",
    "SYNCMGR_HT_MAX",
    "SYNCMGR_HT_MIN",
    "SYNCMGR_HT_SERVICE",
    "SYNCMGR_HT_UNSPECIFIED",
    "SYNCMGR_ICM_CAN_BROWSE_CONTENT",
    "SYNCMGR_ICM_CAN_DELETE",
    "SYNCMGR_ICM_CONFLICT_STORE",
    "SYNCMGR_ICM_EVENT_STORE",
    "SYNCMGR_ICM_NONE",
    "SYNCMGR_ICM_PROVIDES_ICON",
    "SYNCMGR_ICM_QUERY_BEFORE_DELETE",
    "SYNCMGR_ICM_QUERY_BEFORE_DISABLE",
    "SYNCMGR_ICM_QUERY_BEFORE_ENABLE",
    "SYNCMGR_ICM_VALID_MASK",
    "SYNCMGR_IPM_DISABLE_BROWSE",
    "SYNCMGR_IPM_DISABLE_DELETE",
    "SYNCMGR_IPM_DISABLE_DISABLE",
    "SYNCMGR_IPM_DISABLE_ENABLE",
    "SYNCMGR_IPM_DISABLE_START_SYNC",
    "SYNCMGR_IPM_DISABLE_STOP_SYNC",
    "SYNCMGR_IPM_HIDDEN_BY_DEFAULT",
    "SYNCMGR_IPM_NONE",
    "SYNCMGR_IPM_PREVENT_DISABLE",
    "SYNCMGR_IPM_PREVENT_ENABLE",
    "SYNCMGR_IPM_PREVENT_START_SYNC",
    "SYNCMGR_IPM_PREVENT_STOP_SYNC",
    "SYNCMGR_IPM_VALID_MASK",
    "SYNCMGR_ITEM_CAPABILITIES",
    "SYNCMGR_ITEM_POLICIES",
    "SYNCMGR_OBJECTID_BrowseContent",
    "SYNCMGR_OBJECTID_ConflictStore",
    "SYNCMGR_OBJECTID_EventLinkClick",
    "SYNCMGR_OBJECTID_EventStore",
    "SYNCMGR_OBJECTID_Icon",
    "SYNCMGR_OBJECTID_QueryBeforeActivate",
    "SYNCMGR_OBJECTID_QueryBeforeDeactivate",
    "SYNCMGR_OBJECTID_QueryBeforeDelete",
    "SYNCMGR_OBJECTID_QueryBeforeDisable",
    "SYNCMGR_OBJECTID_QueryBeforeEnable",
    "SYNCMGR_OBJECTID_ShowSchedule",
    "SYNCMGR_PC_KEEP_MULTIPLE",
    "SYNCMGR_PC_KEEP_ONE",
    "SYNCMGR_PC_KEEP_RECENT",
    "SYNCMGR_PC_NO_CHOICE",
    "SYNCMGR_PC_REMOVE_FROM_SYNC_SET",
    "SYNCMGR_PC_SKIP",
    "SYNCMGR_PNS_CANCEL",
    "SYNCMGR_PNS_CONTINUE",
    "SYNCMGR_PNS_DEFAULT",
    "SYNCMGR_PRESENTER_CHOICE",
    "SYNCMGR_PRESENTER_NEXT_STEP",
    "SYNCMGR_PROGRESS_STATUS",
    "SYNCMGR_PS_CANCELED",
    "SYNCMGR_PS_DISCONNECTED",
    "SYNCMGR_PS_FAILED",
    "SYNCMGR_PS_MAX",
    "SYNCMGR_PS_SUCCEEDED",
    "SYNCMGR_PS_UPDATING",
    "SYNCMGR_PS_UPDATING_INDETERMINATE",
    "SYNCMGR_RA_KEEPOTHER",
    "SYNCMGR_RA_KEEPRECENT",
    "SYNCMGR_RA_KEEP_MULTIPLE",
    "SYNCMGR_RA_KEEP_SINGLE",
    "SYNCMGR_RA_REMOVEFROMSYNCSET",
    "SYNCMGR_RA_VALID",
    "SYNCMGR_RESOLUTION_ABILITIES",
    "SYNCMGR_RESOLUTION_FEEDBACK",
    "SYNCMGR_RF_CANCEL",
    "SYNCMGR_RF_CONTINUE",
    "SYNCMGR_RF_REFRESH",
    "SYNCMGR_SCF_IGNORE_IF_ALREADY_SYNCING",
    "SYNCMGR_SCF_NONE",
    "SYNCMGR_SCF_VALID",
    "SYNCMGR_SYNC_CONTROL_FLAGS",
    "SYNCMGR_UPDATE_REASON",
    "SYNCMGR_UR_ADDED",
    "SYNCMGR_UR_CHANGED",
    "SYNCMGR_UR_MAX",
    "SYNCMGR_UR_REMOVED",
    "SZ_CONTENTTYPE_CDF",
    "SZ_CONTENTTYPE_CDFA",
    "SZ_CONTENTTYPE_CDFW",
    "SZ_CONTENTTYPE_HTML",
    "SZ_CONTENTTYPE_HTMLA",
    "SZ_CONTENTTYPE_HTMLW",
    "S_SYNCMGR_CANCELALL",
    "S_SYNCMGR_CANCELITEM",
    "S_SYNCMGR_ENUMITEMS",
    "S_SYNCMGR_ITEMDELETED",
    "S_SYNCMGR_MISSINGITEMS",
    "S_SYNCMGR_RETRYSYNC",
    "ScheduledTasks",
    "SearchFolderItemFactory",
    "SecureLockIconConstants",
    "SecureLockIconConstants_secureLockIconMixed",
    "SecureLockIconConstants_secureLockIconSecure128Bit",
    "SecureLockIconConstants_secureLockIconSecure40Bit",
    "SecureLockIconConstants_secureLockIconSecure56Bit",
    "SecureLockIconConstants_secureLockIconSecureFortezza",
    "SecureLockIconConstants_secureLockIconSecureUnknownBits",
    "SecureLockIconConstants_secureLockIconUnsecure",
    "SelectedItemCount_Property_GUID",
    "SetCurrentProcessExplicitAppUserModelID",
    "SetMenuContextHelpId",
    "SetWindowContextHelpId",
    "SetWindowSubclass",
    "ShFindChangeNotificationHandle",
    "SharedBitmap",
    "SharingConfigurationManager",
    "Shell",
    "ShellAboutA",
    "ShellAboutW",
    "ShellBrowserWindow",
    "ShellDesktop",
    "ShellDispatchInproc",
    "ShellExecuteA",
    "ShellExecuteExA",
    "ShellExecuteExW",
    "ShellExecuteW",
    "ShellFSFolder",
    "ShellFolderItem",
    "ShellFolderView",
    "ShellFolderViewOC",
    "ShellFolderViewOptions",
    "ShellImageDataFactory",
    "ShellItem",
    "ShellLibrary",
    "ShellLink",
    "ShellLinkObject",
    "ShellMessageBoxA",
    "ShellMessageBoxW",
    "ShellNameSpace",
    "ShellSpecialFolderConstants",
    "ShellSpecialFolderConstants_ssfALTSTARTUP",
    "ShellSpecialFolderConstants_ssfAPPDATA",
    "ShellSpecialFolderConstants_ssfBITBUCKET",
    "ShellSpecialFolderConstants_ssfCOMMONALTSTARTUP",
    "ShellSpecialFolderConstants_ssfCOMMONAPPDATA",
    "ShellSpecialFolderConstants_ssfCOMMONDESKTOPDIR",
    "ShellSpecialFolderConstants_ssfCOMMONFAVORITES",
    "ShellSpecialFolderConstants_ssfCOMMONPROGRAMS",
    "ShellSpecialFolderConstants_ssfCOMMONSTARTMENU",
    "ShellSpecialFolderConstants_ssfCOMMONSTARTUP",
    "ShellSpecialFolderConstants_ssfCONTROLS",
    "ShellSpecialFolderConstants_ssfCOOKIES",
    "ShellSpecialFolderConstants_ssfDESKTOP",
    "ShellSpecialFolderConstants_ssfDESKTOPDIRECTORY",
    "ShellSpecialFolderConstants_ssfDRIVES",
    "ShellSpecialFolderConstants_ssfFAVORITES",
    "ShellSpecialFolderConstants_ssfFONTS",
    "ShellSpecialFolderConstants_ssfHISTORY",
    "ShellSpecialFolderConstants_ssfINTERNETCACHE",
    "ShellSpecialFolderConstants_ssfLOCALAPPDATA",
    "ShellSpecialFolderConstants_ssfMYPICTURES",
    "ShellSpecialFolderConstants_ssfNETHOOD",
    "ShellSpecialFolderConstants_ssfNETWORK",
    "ShellSpecialFolderConstants_ssfPERSONAL",
    "ShellSpecialFolderConstants_ssfPRINTERS",
    "ShellSpecialFolderConstants_ssfPRINTHOOD",
    "ShellSpecialFolderConstants_ssfPROFILE",
    "ShellSpecialFolderConstants_ssfPROGRAMFILES",
    "ShellSpecialFolderConstants_ssfPROGRAMFILESx86",
    "ShellSpecialFolderConstants_ssfPROGRAMS",
    "ShellSpecialFolderConstants_ssfRECENT",
    "ShellSpecialFolderConstants_ssfSENDTO",
    "ShellSpecialFolderConstants_ssfSTARTMENU",
    "ShellSpecialFolderConstants_ssfSTARTUP",
    "ShellSpecialFolderConstants_ssfSYSTEM",
    "ShellSpecialFolderConstants_ssfSYSTEMx86",
    "ShellSpecialFolderConstants_ssfTEMPLATES",
    "ShellSpecialFolderConstants_ssfWINDOWS",
    "ShellUIHelper",
    "ShellWindowFindWindowOptions",
    "ShellWindowTypeConstants",
    "ShellWindows",
    "Shell_GetCachedImageIndex",
    "Shell_GetCachedImageIndexA",
    "Shell_GetCachedImageIndexW",
    "Shell_GetImageLists",
    "Shell_MergeMenus",
    "Shell_NotifyIconA",
    "Shell_NotifyIconGetRect",
    "Shell_NotifyIconW",
    "ShowInputPaneAnimationCoordinator",
    "SignalFileOpen",
    "SimpleConflictPresenter",
    "SizeCategorizer",
    "SmartcardCredentialProvider",
    "SmartcardPinProvider",
    "SmartcardReaderSelectionProvider",
    "SmartcardWinRTProvider",
    "SoftwareUpdateMessageBox",
    "StartMenuPin",
    "StgMakeUniqueName",
    "StorageProviderBanners",
    "StrCSpnA",
    "StrCSpnIA",
    "StrCSpnIW",
    "StrCSpnW",
    "StrCatBuffA",
    "StrCatBuffW",
    "StrCatChainW",
    "StrCatW",
    "StrChrA",
    "StrChrIA",
    "StrChrIW",
    "StrChrNIW",
    "StrChrNW",
    "StrChrW",
    "StrCmpCA",
    "StrCmpCW",
    "StrCmpICA",
    "StrCmpICW",
    "StrCmpIW",
    "StrCmpLogicalW",
    "StrCmpNA",
    "StrCmpNCA",
    "StrCmpNCW",
    "StrCmpNIA",
    "StrCmpNICA",
    "StrCmpNICW",
    "StrCmpNIW",
    "StrCmpNW",
    "StrCmpW",
    "StrCpyNW",
    "StrCpyW",
    "StrDupA",
    "StrDupW",
    "StrFormatByteSize64A",
    "StrFormatByteSizeA",
    "StrFormatByteSizeEx",
    "StrFormatByteSizeW",
    "StrFormatKBSizeA",
    "StrFormatKBSizeW",
    "StrFromTimeIntervalA",
    "StrFromTimeIntervalW",
    "StrIsIntlEqualA",
    "StrIsIntlEqualW",
    "StrNCatA",
    "StrNCatW",
    "StrPBrkA",
    "StrPBrkW",
    "StrRChrA",
    "StrRChrIA",
    "StrRChrIW",
    "StrRChrW",
    "StrRStrIA",
    "StrRStrIW",
    "StrRetToBSTR",
    "StrRetToBufA",
    "StrRetToBufW",
    "StrRetToStrA",
    "StrRetToStrW",
    "StrSpnA",
    "StrSpnW",
    "StrStrA",
    "StrStrIA",
    "StrStrIW",
    "StrStrNIW",
    "StrStrNW",
    "StrStrW",
    "StrToInt64ExA",
    "StrToInt64ExW",
    "StrToIntA",
    "StrToIntExA",
    "StrToIntExW",
    "StrToIntW",
    "StrTrimA",
    "StrTrimW",
    "SuspensionDependencyManager",
    "SyncMgr",
    "SyncMgrClient",
    "SyncMgrControl",
    "SyncMgrFolder",
    "SyncMgrScheduleWizard",
    "SyncResultsFolder",
    "SyncSetupFolder",
    "TBIF_APPEND",
    "TBIF_DEFAULT",
    "TBIF_INTERNETBAR",
    "TBIF_NOTOOLBAR",
    "TBIF_PREPEND",
    "TBIF_REPLACE",
    "TBIF_STANDARDTOOLBAR",
    "TBINFO",
    "TBPFLAG",
    "TBPF_ERROR",
    "TBPF_INDETERMINATE",
    "TBPF_NOPROGRESS",
    "TBPF_NORMAL",
    "TBPF_PAUSED",
    "THBF_DISABLED",
    "THBF_DISMISSONCLICK",
    "THBF_ENABLED",
    "THBF_HIDDEN",
    "THBF_NOBACKGROUND",
    "THBF_NONINTERACTIVE",
    "THBN_CLICKED",
    "THB_BITMAP",
    "THB_FLAGS",
    "THB_ICON",
    "THB_TOOLTIP",
    "THUMBBUTTON",
    "THUMBBUTTONFLAGS",
    "THUMBBUTTONMASK",
    "TITLEBARNAMELEN",
    "TI_BITMAP",
    "TI_FLAGS",
    "TI_JPEG",
    "TLEF_ABSOLUTE",
    "TLEF_EXCLUDE_ABOUT_PAGES",
    "TLEF_EXCLUDE_SUBFRAME_ENTRIES",
    "TLEF_INCLUDE_UNINVOKEABLE",
    "TLEF_RELATIVE_BACK",
    "TLEF_RELATIVE_FORE",
    "TLEF_RELATIVE_INCLUDE_CURRENT",
    "TLENUMF",
    "TLMENUF_BACK",
    "TLMENUF_FORE",
    "TLMENUF_INCLUDECURRENT",
    "TLOG_BACK",
    "TLOG_CURRENT",
    "TLOG_FORE",
    "TOOLBARITEM",
    "TRANSLATEURL_FL_GUESS_PROTOCOL",
    "TRANSLATEURL_FL_USE_DEFAULT_PROTOCOL",
    "TRANSLATEURL_IN_FLAGS",
    "TSF_ALLOW_DECRYPTION",
    "TSF_COPY_CREATION_TIME",
    "TSF_COPY_HARD_LINK",
    "TSF_COPY_LOCALIZED_NAME",
    "TSF_COPY_WRITE_TIME",
    "TSF_DELETE_RECYCLE_IF_POSSIBLE",
    "TSF_FAIL_EXIST",
    "TSF_MOVE_AS_COPY_DELETE",
    "TSF_NORMAL",
    "TSF_NO_SECURITY",
    "TSF_OVERWRITE_EXIST",
    "TSF_RENAME_EXIST",
    "TSF_SUSPEND_SHELLEVENTS",
    "TSF_USE_FULL_ACCESS",
    "TS_INDETERMINATE",
    "TS_NONE",
    "TS_PERFORMING",
    "TS_PREPARING",
    "TaskbarList",
    "ThumbnailStreamCache",
    "ThumbnailStreamCacheOptions",
    "ThumbnailStreamCacheOptions_AllowSmallerSize",
    "ThumbnailStreamCacheOptions_ExtractIfNotCached",
    "ThumbnailStreamCacheOptions_ResizeThumbnail",
    "ThumbnailStreamCacheOptions_ReturnOnlyIfCached",
    "TimeCategorizer",
    "TrackShellMenu",
    "TrayBandSiteService",
    "TrayDeskBand",
    "UNDOCK_REASON",
    "URLASSOCDLG_FL_REGISTER_ASSOC",
    "URLASSOCDLG_FL_USE_DEFAULT_NAME",
    "URLASSOCIATIONDIALOG_IN_FLAGS",
    "URLINVOKECOMMANDINFOA",
    "URLINVOKECOMMANDINFOW",
    "URLIS",
    "URLIS_APPLIABLE",
    "URLIS_DIRECTORY",
    "URLIS_FILEURL",
    "URLIS_HASQUERY",
    "URLIS_NOHISTORY",
    "URLIS_OPAQUE",
    "URLIS_URL",
    "URL_APPLY_DEFAULT",
    "URL_APPLY_FORCEAPPLY",
    "URL_APPLY_GUESSFILE",
    "URL_APPLY_GUESSSCHEME",
    "URL_BROWSER_MODE",
    "URL_CONVERT_IF_DOSPATH",
    "URL_DONT_ESCAPE_EXTRA_INFO",
    "URL_DONT_SIMPLIFY",
    "URL_DONT_UNESCAPE",
    "URL_DONT_UNESCAPE_EXTRA_INFO",
    "URL_ESCAPE_ASCII_URI_COMPONENT",
    "URL_ESCAPE_AS_UTF8",
    "URL_ESCAPE_PERCENT",
    "URL_ESCAPE_SEGMENT_ONLY",
    "URL_ESCAPE_SPACES_ONLY",
    "URL_ESCAPE_UNSAFE",
    "URL_E_INVALID_SYNTAX",
    "URL_E_UNREGISTERED_PROTOCOL",
    "URL_FILE_USE_PATHURL",
    "URL_INTERNAL_PATH",
    "URL_NO_META",
    "URL_PART",
    "URL_PARTFLAG_KEEPSCHEME",
    "URL_PART_HOSTNAME",
    "URL_PART_NONE",
    "URL_PART_PASSWORD",
    "URL_PART_PORT",
    "URL_PART_QUERY",
    "URL_PART_SCHEME",
    "URL_PART_USERNAME",
    "URL_PLUGGABLE_PROTOCOL",
    "URL_SCHEME",
    "URL_SCHEME_ABOUT",
    "URL_SCHEME_FILE",
    "URL_SCHEME_FTP",
    "URL_SCHEME_GOPHER",
    "URL_SCHEME_HTTP",
    "URL_SCHEME_HTTPS",
    "URL_SCHEME_INVALID",
    "URL_SCHEME_JAVASCRIPT",
    "URL_SCHEME_KNOWNFOLDER",
    "URL_SCHEME_LOCAL",
    "URL_SCHEME_MAILTO",
    "URL_SCHEME_MAXVALUE",
    "URL_SCHEME_MK",
    "URL_SCHEME_MSHELP",
    "URL_SCHEME_MSSHELLDEVICE",
    "URL_SCHEME_MSSHELLIDLIST",
    "URL_SCHEME_MSSHELLROOTED",
    "URL_SCHEME_NEWS",
    "URL_SCHEME_NNTP",
    "URL_SCHEME_RES",
    "URL_SCHEME_SEARCH",
    "URL_SCHEME_SEARCH_MS",
    "URL_SCHEME_SHELL",
    "URL_SCHEME_SNEWS",
    "URL_SCHEME_TELNET",
    "URL_SCHEME_UNKNOWN",
    "URL_SCHEME_VBSCRIPT",
    "URL_SCHEME_WAIS",
    "URL_SCHEME_WILDCARD",
    "URL_UNESCAPE",
    "URL_UNESCAPE_AS_UTF8",
    "URL_UNESCAPE_HIGH_ANSI_ONLY",
    "URL_UNESCAPE_INPLACE",
    "URL_UNESCAPE_URI_COMPONENT",
    "URL_WININET_COMPATIBILITY",
    "UR_MONITOR_DISCONNECT",
    "UR_RESOLUTION_CHANGE",
    "UnloadUserProfile",
    "UnregisterAppConstrainedChangeNotification",
    "UnregisterAppStateChangeNotification",
    "UnregisterScaleChangeEvent",
    "UrlApplySchemeA",
    "UrlApplySchemeW",
    "UrlCanonicalizeA",
    "UrlCanonicalizeW",
    "UrlCombineA",
    "UrlCombineW",
    "UrlCompareA",
    "UrlCompareW",
    "UrlCreateFromPathA",
    "UrlCreateFromPathW",
    "UrlEscapeA",
    "UrlEscapeW",
    "UrlFixupW",
    "UrlGetLocationA",
    "UrlGetLocationW",
    "UrlGetPartA",
    "UrlGetPartW",
    "UrlHashA",
    "UrlHashW",
    "UrlIsA",
    "UrlIsNoHistoryA",
    "UrlIsNoHistoryW",
    "UrlIsOpaqueA",
    "UrlIsOpaqueW",
    "UrlIsW",
    "UrlUnescapeA",
    "UrlUnescapeW",
    "UserNotification",
    "V1PasswordCredentialProvider",
    "V1SmartcardCredentialProvider",
    "V1WinBioCredentialProvider",
    "VALIDATEUNC_CONNECT",
    "VALIDATEUNC_NOUI",
    "VALIDATEUNC_OPTION",
    "VALIDATEUNC_PERSIST",
    "VALIDATEUNC_PRINT",
    "VALIDATEUNC_VALID",
    "VID_Content",
    "VID_Details",
    "VID_LargeIcons",
    "VID_List",
    "VID_SmallIcons",
    "VID_ThumbStrip",
    "VID_Thumbnails",
    "VID_Tile",
    "VIEW_PRIORITY_CACHEHIT",
    "VIEW_PRIORITY_CACHEMISS",
    "VIEW_PRIORITY_DESPERATE",
    "VIEW_PRIORITY_INHERIT",
    "VIEW_PRIORITY_NONE",
    "VIEW_PRIORITY_RESTRICTED",
    "VIEW_PRIORITY_SHELLEXT",
    "VIEW_PRIORITY_SHELLEXT_ASBACKUP",
    "VIEW_PRIORITY_STALECACHEHIT",
    "VIEW_PRIORITY_USEASDEFAULT",
    "VOLUME_PREFIX",
    "VPCF_BACKGROUND",
    "VPCF_SORTCOLUMN",
    "VPCF_SUBTEXT",
    "VPCF_TEXT",
    "VPCF_TEXTBACKGROUND",
    "VPCOLORFLAGS",
    "VPWATERMARKFLAGS",
    "VPWF_ALPHABLEND",
    "VPWF_DEFAULT",
    "VaultProvider",
    "VirtualDesktopManager",
    "WC_NETADDRESS",
    "WINDOWDATA",
    "WM_CPL_LAUNCH",
    "WM_CPL_LAUNCHED",
    "WPSTYLE_CENTER",
    "WPSTYLE_CROPTOFIT",
    "WPSTYLE_KEEPASPECT",
    "WPSTYLE_MAX",
    "WPSTYLE_SPAN",
    "WPSTYLE_STRETCH",
    "WPSTYLE_TILE",
    "WTSAT_ARGB",
    "WTSAT_RGB",
    "WTSAT_UNKNOWN",
    "WTSCF_APPSTYLE",
    "WTSCF_DEFAULT",
    "WTSCF_FAST",
    "WTSCF_SQUARE",
    "WTSCF_WIDE",
    "WTS_ALPHATYPE",
    "WTS_APPSTYLE",
    "WTS_CACHED",
    "WTS_CACHEFLAGS",
    "WTS_CONTEXTFLAGS",
    "WTS_CROPTOSQUARE",
    "WTS_DEFAULT",
    "WTS_EXTRACT",
    "WTS_EXTRACTDONOTCACHE",
    "WTS_EXTRACTINPROC",
    "WTS_E_DATAFILEUNAVAILABLE",
    "WTS_E_EXTRACTIONBLOCKED",
    "WTS_E_EXTRACTIONPENDING",
    "WTS_E_EXTRACTIONTIMEDOUT",
    "WTS_E_FAILEDEXTRACTION",
    "WTS_E_FASTEXTRACTIONNOTSUPPORTED",
    "WTS_E_NOSTORAGEPROVIDERTHUMBNAILHANDLER",
    "WTS_E_SURROGATEUNAVAILABLE",
    "WTS_FASTEXTRACT",
    "WTS_FLAGS",
    "WTS_FORCEEXTRACTION",
    "WTS_IDEALCACHESIZEONLY",
    "WTS_INCACHEONLY",
    "WTS_INSTANCESURROGATE",
    "WTS_LOWQUALITY",
    "WTS_NONE",
    "WTS_REQUIRESURROGATE",
    "WTS_SCALETOREQUESTEDSIZE",
    "WTS_SCALEUP",
    "WTS_SKIPFASTEXTRACT",
    "WTS_SLOWRECLAIM",
    "WTS_THUMBNAILID",
    "WTS_WIDETHUMBNAILS",
    "WebBrowser",
    "WebBrowser_V1",
    "WebWizardHost",
    "WhichPlatform",
    "Win32DeleteFile",
    "WinBioCredentialProvider",
    "WinHelpA",
    "WinHelpW",
    "WriteCabinetState",
    "_APPCONSTRAIN_REGISTRATION",
    "_APPSTATE_REGISTRATION",
    "_BROWSERFRAMEOPTIONS",
    "_CDBE_ACTIONS",
    "_EXPCMDFLAGS",
    "_EXPCMDSTATE",
    "_EXPLORERPANESTATE",
    "_EXPPS",
    "_KF_DEFINITION_FLAGS",
    "_KF_REDIRECTION_CAPABILITIES",
    "_KF_REDIRECT_FLAGS",
    "_NMCII_FLAGS",
    "_NMCSAEI_FLAGS",
    "_NSTCECLICKTYPE",
    "_NSTCEHITTEST",
    "_NSTCITEMSTATE",
    "_NSTCROOTSTYLE",
    "_NSTCSTYLE",
    "_OPPROGDLGF",
    "_PDMODE",
    "_SHCONTF",
    "_SICHINTF",
    "_SPBEGINF",
    "_SPINITF",
    "_SV3CVW3_FLAGS",
    "_SVGIO",
    "_SVSIF",
    "_TRANSFER_ADVISE_STATE",
    "_TRANSFER_SOURCE_FLAGS",
    "__UNUSED_RECYCLE_WAS_GLOBALCOUNTER_CSCSYNCINPROGRESS",
    "__UNUSED_RECYCLE_WAS_GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SERVERDRIVE",
    "__UNUSED_RECYCLE_WAS_GLOBALCOUNTER_RECYCLEGLOBALDIRTYCOUNT",
    "idsAppName",
    "idsBadOldPW",
    "idsChangePW",
    "idsDefKeyword",
    "idsDifferentPW",
    "idsHelpFile",
    "idsIniFile",
    "idsIsPassword",
    "idsNoHelpMemory",
    "idsPassword",
    "idsScreenSaver",
    "wnsprintfA",
    "wnsprintfW",
    "wvnsprintfA",
    "wvnsprintfW",
]
_arch_optional = [
]