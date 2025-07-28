from ..utils import clean_html as clean_html, extract_attributes as extract_attributes, get_element_html_by_id as get_element_html_by_id, int_or_none as int_or_none, parse_duration as parse_duration, str_or_none as str_or_none, unified_strdate as unified_strdate, url_or_none as url_or_none, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from .vimeo import VimeoIE as VimeoIE

class LaracastsBaseIE(InfoExtractor): ...

class LaracastsIE(LaracastsBaseIE):
    IE_NAME: str

class LaracastsPlaylistIE(LaracastsBaseIE):
    IE_NAME: str
