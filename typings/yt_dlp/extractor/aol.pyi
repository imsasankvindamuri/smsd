from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_qs as parse_qs, url_or_none as url_or_none
from .yahoo import YahooIE as YahooIE

class AolIE(YahooIE):
    IE_NAME: str
