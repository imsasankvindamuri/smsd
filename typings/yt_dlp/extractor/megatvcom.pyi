from ..networking import HEADRequest as HEADRequest
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, extract_attributes as extract_attributes, get_element_by_class as get_element_by_class, get_element_html_by_id as get_element_html_by_id, parse_qs as parse_qs, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class MegaTVComBaseIE(InfoExtractor): ...

class MegaTVComIE(MegaTVComBaseIE):
    IE_NAME: str
    IE_DESC: str

class MegaTVComEmbedIE(MegaTVComBaseIE):
    IE_NAME: str
    IE_DESC: str
