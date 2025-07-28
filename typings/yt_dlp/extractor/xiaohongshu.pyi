from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, js_to_json as js_to_json, url_or_none as url_or_none, urlhandle_detect_ext as urlhandle_detect_ext
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class XiaoHongShuIE(InfoExtractor):
    IE_DESC: str
