from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, parse_resolution as parse_resolution, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class PlVideoIE(InfoExtractor):
    IE_DESC: str
