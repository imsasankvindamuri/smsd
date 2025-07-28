from ..networking import HEADRequest as HEADRequest
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, determine_ext as determine_ext, format_field as format_field, get_element_by_class as get_element_by_class, get_elements_html_by_class as get_elements_html_by_class, int_or_none as int_or_none, orderedSet as orderedSet, parse_count as parse_count, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class BitChuteIE(InfoExtractor): ...

class BitChuteChannelIE(InfoExtractor):
    PAGE_SIZE: int
    HTML_CLASS_NAMES: Incomplete
