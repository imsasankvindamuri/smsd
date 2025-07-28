from ..utils import clean_html as clean_html, int_or_none as int_or_none, mimetype2ext as mimetype2ext, str_or_none as str_or_none, traverse_obj as traverse_obj, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor, SearchInfoExtractor as SearchInfoExtractor

class PRXBaseIE(InfoExtractor):
    PRX_BASE_URL_RE: str

class PRXStoryIE(PRXBaseIE): ...
class PRXSeriesIE(PRXBaseIE): ...
class PRXAccountIE(PRXBaseIE): ...

class PRXStoriesSearchIE(PRXBaseIE, SearchInfoExtractor):
    IE_DESC: str
    IE_NAME: str

class PRXSeriesSearchIE(PRXBaseIE, SearchInfoExtractor):
    IE_DESC: str
    IE_NAME: str
