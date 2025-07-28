from ..utils import ExtractorError as ExtractorError, UserNotLive as UserNotLive, determine_ext as determine_ext, int_or_none as int_or_none, js_to_json as js_to_json, parse_resolution as parse_resolution, str_or_none as str_or_none, traverse_obj as traverse_obj, unescapeHTML as unescapeHTML, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from .openload import PhantomJSwrapper as PhantomJSwrapper

class DouyuBaseIE(InfoExtractor): ...

class DouyuTVIE(DouyuBaseIE):
    IE_DESC: str

class DouyuShowIE(DouyuBaseIE): ...
