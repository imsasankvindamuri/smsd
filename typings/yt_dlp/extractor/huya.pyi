from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, parse_duration as parse_duration, str_or_none as str_or_none, try_get as try_get, unescapeHTML as unescapeHTML, update_url as update_url, update_url_query as update_url_query, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class HuyaLiveIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    def encrypt(self, params, stream_info, stream_name): ...

class HuyaVideoIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
