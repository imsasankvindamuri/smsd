import abc
import enum
from _typeshed import Incomplete
from yt_dlp.extractor.common import InfoExtractor as InfoExtractor
from yt_dlp.utils import NO_DEFAULT as NO_DEFAULT, bug_reports_message as bug_reports_message, classproperty as classproperty, traverse_obj as traverse_obj
from yt_dlp.version import __version__ as __version__

class IEContentProviderLogger(abc.ABC, metaclass=abc.ABCMeta):
    class LogLevel(enum.IntEnum):
        TRACE = 0
        DEBUG = 10
        INFO = 20
        WARNING = 30
        ERROR = 40
    log_level: Incomplete
    @abc.abstractmethod
    def trace(self, message: str): ...
    @abc.abstractmethod
    def debug(self, message: str): ...
    @abc.abstractmethod
    def info(self, message: str): ...
    @abc.abstractmethod
    def warning(self, message: str, *, once: bool = False): ...
    @abc.abstractmethod
    def error(self, message: str): ...

class IEContentProviderError(Exception):
    expected: Incomplete
    def __init__(self, msg=None, expected: bool = False) -> None: ...

class IEContentProvider(abc.ABC, metaclass=abc.ABCMeta):
    PROVIDER_VERSION: str
    BUG_REPORT_LOCATION: str
    ie: Incomplete
    settings: Incomplete
    logger: Incomplete
    def __init__(self, ie: InfoExtractor, logger: IEContentProviderLogger, settings: dict[str, list[str]], *_, **__) -> None: ...
    @classmethod
    def __init_subclass__(cls, *, suffix=None, **kwargs): ...
    @classproperty
    def PROVIDER_NAME(cls) -> str: ...
    @classproperty
    def BUG_REPORT_MESSAGE(cls): ...
    @classproperty
    def PROVIDER_KEY(cls) -> str: ...
    @abc.abstractmethod
    def is_available(self) -> bool: ...
    def close(self) -> None: ...

class BuiltinIEContentProvider(IEContentProvider, abc.ABC, metaclass=abc.ABCMeta):
    PROVIDER_VERSION = __version__
    BUG_REPORT_MESSAGE: Incomplete

def register_provider_generic(provider, base_class, registry): ...
def register_preference_generic(base_class, registry, *providers): ...
