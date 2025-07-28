from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class KikaIE(InfoExtractor):
    IE_DESC: str

class KikaPlaylistIE(InfoExtractor): ...
