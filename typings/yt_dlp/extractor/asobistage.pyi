from ..utils import str_or_none as str_or_none, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class AsobiStageIE(InfoExtractor):
    IE_DESC: str
