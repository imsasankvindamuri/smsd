from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, clean_html as clean_html, extract_attributes as extract_attributes, get_element_by_class as get_element_by_class, get_element_html_by_id as get_element_html_by_id, parse_count as parse_count, remove_end as remove_end, update_url as update_url, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class MurrtubeIE(InfoExtractor): ...

class MurrtubeUserIE(InfoExtractor):
    IE_DESC: str
