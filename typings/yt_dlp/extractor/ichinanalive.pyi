from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, str_or_none as str_or_none, traverse_obj as traverse_obj, unified_strdate as unified_strdate, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class IchinanaLiveIE(InfoExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class IchinanaLiveClipIE(InfoExtractor):
    IE_NAME: str

class IchinanaLiveVODIE(InfoExtractor):
    IE_NAME: str
