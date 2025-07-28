from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, parse_resolution as parse_resolution, str_or_none as str_or_none, url_or_none as url_or_none
from ..utils.traversal import require as require, traverse_obj as traverse_obj, value as value
from .brightcove import BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor

class NineNowIE(InfoExtractor):
    IE_NAME: str
    BRIGHTCOVE_URL_TEMPLATE: str
