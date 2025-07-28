from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, js_to_json as js_to_json, parse_filesize as parse_filesize, parse_resolution as parse_resolution, str_or_none as str_or_none, traverse_obj as traverse_obj, url_basename as url_basename, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class ZoomIE(InfoExtractor):
    IE_NAME: str
