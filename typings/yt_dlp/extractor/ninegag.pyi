from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, traverse_obj as traverse_obj, unescapeHTML as unescapeHTML, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class NineGagIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
