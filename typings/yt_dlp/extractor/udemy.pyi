from ..networking import Request as Request
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, extract_attributes as extract_attributes, float_or_none as float_or_none, int_or_none as int_or_none, js_to_json as js_to_json, smuggle_url as smuggle_url, try_get as try_get, unescapeHTML as unescapeHTML, unsmuggle_url as unsmuggle_url, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class UdemyIE(InfoExtractor):
    IE_NAME: str

class UdemyCourseIE(UdemyIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
