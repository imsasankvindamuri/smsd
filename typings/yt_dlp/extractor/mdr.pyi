from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, join_nonempty as join_nonempty, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, url_or_none as url_or_none, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class MDRIE(InfoExtractor):
    IE_DESC: str
