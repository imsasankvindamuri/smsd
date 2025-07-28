from ..networking import HEADRequest as HEADRequest
from ..utils import int_or_none as int_or_none, traverse_obj as traverse_obj, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class TenPlayIE(InfoExtractor):
    IE_NAME: str

class TenPlaySeasonIE(InfoExtractor):
    IE_NAME: str
