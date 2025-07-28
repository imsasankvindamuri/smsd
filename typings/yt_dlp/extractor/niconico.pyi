from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, determine_ext as determine_ext, extract_attributes as extract_attributes, float_or_none as float_or_none, int_or_none as int_or_none, parse_bitrate as parse_bitrate, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, parse_resolution as parse_resolution, qualities as qualities, str_or_none as str_or_none, truncate_string as truncate_string, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_basename as url_basename, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from ..utils.traversal import find_element as find_element, require as require, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor, SearchInfoExtractor as SearchInfoExtractor
from _typeshed import Incomplete

class NiconicoBaseIE(InfoExtractor):
    @property
    def is_logged_in(self): ...

class NiconicoIE(NiconicoBaseIE):
    IE_NAME: str
    IE_DESC: str

class NiconicoPlaylistBaseIE(InfoExtractor): ...

class NiconicoPlaylistIE(NiconicoPlaylistBaseIE):
    IE_NAME: str

class NiconicoSeriesIE(NiconicoPlaylistBaseIE):
    IE_NAME: str

class NiconicoHistoryIE(NiconicoPlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class NicovideoSearchBaseIE(InfoExtractor): ...

class NicovideoSearchIE(NicovideoSearchBaseIE, SearchInfoExtractor):
    IE_DESC: str
    IE_NAME: str

class NicovideoSearchURLIE(NicovideoSearchBaseIE):
    IE_NAME: Incomplete
    IE_DESC: str

class NicovideoSearchDateIE(NicovideoSearchBaseIE, SearchInfoExtractor):
    IE_DESC: str
    IE_NAME: Incomplete

class NicovideoTagURLIE(NicovideoSearchBaseIE):
    IE_NAME: str
    IE_DESC: str

class NiconicoUserIE(InfoExtractor): ...

class NiconicoLiveIE(NiconicoBaseIE):
    IE_NAME: str
    IE_DESC: str
