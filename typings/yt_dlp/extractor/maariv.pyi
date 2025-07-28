from ..utils import int_or_none as int_or_none, parse_resolution as parse_resolution, unified_timestamp as unified_timestamp, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class MaarivIE(InfoExtractor):
    IE_NAME: str
