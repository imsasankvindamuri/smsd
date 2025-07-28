from ..utils.traversal import require as require, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from .kaltura import KalturaIE as KalturaIE

class AZMedienIE(InfoExtractor):
    IE_DESC: str
