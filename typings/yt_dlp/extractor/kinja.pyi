from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class KinjaEmbedIE(InfoExtractor):
    IE_NAME: str
