from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, parse_qs as parse_qs, qualities as qualities, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class SixPlayIE(InfoExtractor):
    IE_NAME: str
