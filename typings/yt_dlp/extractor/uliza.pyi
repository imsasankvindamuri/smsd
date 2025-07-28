from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, make_archive_id as make_archive_id, parse_qs as parse_qs, time_seconds as time_seconds
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class UlizaPlayerIE(InfoExtractor): ...

class UlizaPortalIE(InfoExtractor):
    IE_DESC: str
