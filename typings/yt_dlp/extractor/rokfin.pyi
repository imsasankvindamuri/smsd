from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, float_or_none as float_or_none, format_field as format_field, int_or_none as int_or_none, str_or_none as str_or_none, traverse_obj as traverse_obj, try_get as try_get, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor, SearchInfoExtractor as SearchInfoExtractor

class RokfinIE(InfoExtractor): ...
class RokfinPlaylistBaseIE(InfoExtractor): ...

class RokfinStackIE(RokfinPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RokfinChannelIE(RokfinPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RokfinSearchIE(SearchInfoExtractor):
    IE_NAME: str
    IE_DESC: str
