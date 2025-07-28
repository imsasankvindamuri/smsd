from ..networking import HEADRequest as HEADRequest
from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, join_nonempty as join_nonempty, parse_qs as parse_qs, update_url_query as update_url_query
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class RedCDNLivxIE(InfoExtractor):
    IE_NAME: str
