from ..utils import clean_html as clean_html, determine_ext as determine_ext, int_or_none as int_or_none, parse_duration as parse_duration, parse_resolution as parse_resolution, try_get as try_get, unified_timestamp as unified_timestamp, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class CCMAIE(InfoExtractor):
    IE_DESC: str
