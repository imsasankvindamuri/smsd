from ..utils import ExtractorError as ExtractorError, format_field as format_field, traverse_obj as traverse_obj, try_get as try_get, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class RadLiveIE(InfoExtractor):
    IE_NAME: str

class RadLiveSeasonIE(RadLiveIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class RadLiveChannelIE(RadLiveIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
