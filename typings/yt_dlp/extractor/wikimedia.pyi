from ..utils import clean_html as clean_html, get_element_by_class as get_element_by_class, parse_qs as parse_qs, remove_start as remove_start, unescapeHTML as unescapeHTML, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class WikimediaIE(InfoExtractor):
    IE_NAME: str
