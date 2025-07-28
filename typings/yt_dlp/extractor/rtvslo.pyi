from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_duration as parse_duration, traverse_obj as traverse_obj, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class RTVSLOIE(InfoExtractor):
    IE_NAME: str
    SUB_LANGS_MAP: Incomplete

class RTVSLOShowIE(InfoExtractor):
    IE_NAME: str
