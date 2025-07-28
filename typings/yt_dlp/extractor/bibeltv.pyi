from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, format_field as format_field, int_or_none as int_or_none, js_to_json as js_to_json, orderedSet as orderedSet, parse_iso8601 as parse_iso8601, traverse_obj as traverse_obj, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class BibelTVBaseIE(InfoExtractor):
    API_URL: str
    AUTH_TOKEN: str

class BibelTVVideoIE(BibelTVBaseIE):
    IE_DESC: str
    IE_NAME: str

class BibelTVSeriesIE(BibelTVBaseIE):
    IE_DESC: str
    IE_NAME: str

class BibelTVLiveIE(BibelTVBaseIE):
    IE_DESC: str
    IE_NAME: str
