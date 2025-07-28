from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, extract_attributes as extract_attributes, get_element_by_id as get_element_by_id, int_or_none as int_or_none, parse_count as parse_count, parse_duration as parse_duration, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class NewgroundsIE(InfoExtractor): ...

class NewgroundsPlaylistIE(InfoExtractor):
    IE_NAME: str

class NewgroundsUserIE(InfoExtractor):
    IE_NAME: str
