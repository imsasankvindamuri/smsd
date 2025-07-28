from ..utils import int_or_none as int_or_none, unified_strdate as unified_strdate, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class MBNIE(InfoExtractor):
    IE_DESC: str
