from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, join_nonempty as join_nonempty, mimetype2ext as mimetype2ext, parse_qs as parse_qs, unified_strdate as unified_strdate, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class FirstTVIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
