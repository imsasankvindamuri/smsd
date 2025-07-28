from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, join_nonempty as join_nonempty, mimetype2ext as mimetype2ext, parse_iso8601 as parse_iso8601, traverse_obj as traverse_obj, try_get as try_get, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor, SearchInfoExtractor as SearchInfoExtractor
from .youtube import YoutubeIE as YoutubeIE

class YahooIE(InfoExtractor):
    IE_DESC: str

class YahooSearchIE(SearchInfoExtractor):
    IE_DESC: str
    IE_NAME: str

class YahooJapanNewsIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
