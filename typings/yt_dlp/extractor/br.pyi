from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_duration as parse_duration, xpath_element as xpath_element, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class BRIE(InfoExtractor):
    IE_DESC: str
