from ..utils import ExtractorError as ExtractorError, format_field as format_field, int_or_none as int_or_none, str_or_none as str_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

CDN_API_BASE: str
MOMENT_URL_FORMAT: Incomplete

class YouNowLiveIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...

class YouNowChannelIE(InfoExtractor): ...

class YouNowMomentIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
