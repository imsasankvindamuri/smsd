import enum
import functools
from ..networking import Request as Request
from ..postprocessor.ffmpeg import EXT_TO_OUT_FORMATS as EXT_TO_OUT_FORMATS, FFmpegPostProcessor as FFmpegPostProcessor
from ..utils import Popen as Popen, RetryManager as RetryManager, check_executable as check_executable, classproperty as classproperty, cli_bool_option as cli_bool_option, cli_option as cli_option, cli_valueless_option as cli_valueless_option, determine_ext as determine_ext, encodeArgument as encodeArgument, find_available_port as find_available_port, remove_end as remove_end, traverse_obj as traverse_obj
from .fragment import FragmentFD as FragmentFD
from _typeshed import Incomplete

class Features(enum.Enum):
    TO_STDOUT = ...
    MULTIPLE_FORMATS = ...

class ExternalFD(FragmentFD):
    SUPPORTED_PROTOCOLS: Incomplete
    SUPPORTED_FEATURES: Incomplete
    def real_download(self, filename, info_dict): ...
    @classmethod
    def get_basename(cls): ...
    @classproperty
    def EXE_NAME(cls): ...
    @functools.cached_property
    def exe(self): ...
    @classmethod
    def available(cls, path=None): ...
    @classmethod
    def supports(cls, info_dict): ...
    @classmethod
    def can_download(cls, info_dict, path=None): ...

class CurlFD(ExternalFD):
    AVAILABLE_OPT: str

class AxelFD(ExternalFD):
    AVAILABLE_OPT: str

class WgetFD(ExternalFD):
    AVAILABLE_OPT: str

class Aria2cFD(ExternalFD):
    AVAILABLE_OPT: str
    SUPPORTED_PROTOCOLS: Incomplete
    @staticmethod
    def supports_manifest(manifest): ...
    def aria2c_rpc(self, rpc_port, rpc_secret, method, params=()): ...

class HttpieFD(ExternalFD):
    AVAILABLE_OPT: str
    EXE_NAME: str

class FFmpegFD(ExternalFD):
    SUPPORTED_PROTOCOLS: Incomplete
    SUPPORTED_FEATURES: Incomplete
    @classmethod
    def available(cls, path=None): ...
    def on_process_started(self, proc, stdin) -> None: ...
    @classmethod
    def can_merge_formats(cls, info_dict, params): ...

class AVconvFD(FFmpegFD): ...

def list_external_downloaders(): ...
def get_external_downloader(external_downloader): ...
