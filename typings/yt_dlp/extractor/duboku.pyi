from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, extract_attributes as extract_attributes, get_elements_by_class as get_elements_by_class, int_or_none as int_or_none, js_to_json as js_to_json, smuggle_url as smuggle_url, unescapeHTML as unescapeHTML
from .common import InfoExtractor as InfoExtractor

class DubokuIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class DubokuPlaylistIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
