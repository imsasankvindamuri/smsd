from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, qualities as qualities
from .common import InfoExtractor as InfoExtractor

class PlaytvakIE(InfoExtractor):
    IE_DESC: str
