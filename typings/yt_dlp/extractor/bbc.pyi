from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, dict_get as dict_get, float_or_none as float_or_none, get_element_by_class as get_element_by_class, int_or_none as int_or_none, join_nonempty as join_nonempty, js_to_json as js_to_json, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, strip_or_none as strip_or_none, traverse_obj as traverse_obj, try_get as try_get, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class BBCCoUkIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    class MediaSelectionError(Exception):
        id: Incomplete
        def __init__(self, error_id) -> None: ...

class BBCIE(BBCCoUkIE):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class BBCCoUkArticleIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class BBCCoUkPlaylistBaseIE(InfoExtractor): ...
class BBCCoUkIPlayerPlaylistBaseIE(InfoExtractor): ...

class BBCCoUkIPlayerEpisodesIE(BBCCoUkIPlayerPlaylistBaseIE):
    IE_NAME: str

class BBCCoUkIPlayerGroupIE(BBCCoUkIPlayerPlaylistBaseIE):
    IE_NAME: str

class BBCCoUkPlaylistIE(BBCCoUkPlaylistBaseIE):
    IE_NAME: str
