from ..utils import int_or_none as int_or_none, js_to_json as js_to_json, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class NTVDeIE(InfoExtractor):
    IE_NAME: str
