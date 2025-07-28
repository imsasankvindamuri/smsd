from ..utils import ExtractorError as ExtractorError, classproperty as classproperty, remove_start as remove_start
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class UnsupportedInfoExtractor(InfoExtractor):
    IE_DESC: bool
    URLS: Incomplete
    @classproperty
    def IE_NAME(cls): ...

LF: str

class KnownDRMIE(UnsupportedInfoExtractor):
    URLS: Incomplete

class KnownPiracyIE(UnsupportedInfoExtractor):
    URLS: Incomplete
