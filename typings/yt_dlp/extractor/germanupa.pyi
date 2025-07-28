from ..utils import parse_qs as parse_qs, traverse_obj as traverse_obj, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor
from .vimeo import VimeoIE as VimeoIE

class GermanupaIE(InfoExtractor):
    IE_DESC: str
