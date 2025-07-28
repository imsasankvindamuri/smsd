from ..utils import bool_or_none as bool_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, traverse_obj as traverse_obj, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class TV4IE(InfoExtractor):
    IE_DESC: str
