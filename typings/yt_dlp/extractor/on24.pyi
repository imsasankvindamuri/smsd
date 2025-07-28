from ..utils import int_or_none as int_or_none, strip_or_none as strip_or_none, try_get as try_get, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class On24IE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
