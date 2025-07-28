from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, extract_attributes as extract_attributes, get_element_by_class as get_element_by_class, get_element_by_id as get_element_by_id, get_elements_html_by_class as get_elements_html_by_class, int_or_none as int_or_none, merge_dicts as merge_dicts, parse_count as parse_count, parse_qs as parse_qs, traverse_obj as traverse_obj, unified_strdate as unified_strdate, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class YouPornIE(InfoExtractor): ...
class YouPornListBaseIE(InfoExtractor): ...

class YouPornCategoryIE(YouPornListBaseIE):
    IE_DESC: str

class YouPornChannelIE(YouPornListBaseIE):
    IE_DESC: str

class YouPornCollectionIE(YouPornListBaseIE):
    IE_DESC: str

class YouPornTagIE(YouPornListBaseIE):
    IE_DESC: str

class YouPornStarIE(YouPornListBaseIE):
    IE_DESC: str

class YouPornVideosIE(YouPornListBaseIE):
    IE_DESC: str
