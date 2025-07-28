from ..networking import HEADRequest as HEADRequest
from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, traverse_obj as traverse_obj, update_url_query as update_url_query, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class SBSIE(InfoExtractor):
    IE_DESC: str
