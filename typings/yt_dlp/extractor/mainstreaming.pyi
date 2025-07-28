from ..utils import int_or_none as int_or_none, js_to_json as js_to_json, parse_duration as parse_duration, traverse_obj as traverse_obj, try_get as try_get, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class MainStreamingIE(InfoExtractor):
    IE_DESC: str
