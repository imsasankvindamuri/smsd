from ..networking import HEADRequest as HEADRequest
from ..utils import ExtractorError as ExtractorError, UserNotLive as UserNotLive, determine_ext as determine_ext, float_or_none as float_or_none, format_field as format_field, int_or_none as int_or_none, make_archive_id as make_archive_id, mimetype2ext as mimetype2ext, parse_duration as parse_duration, smuggle_url as smuggle_url, traverse_obj as traverse_obj, url_or_none as url_or_none
from .anvato import AnvatoIE as AnvatoIE
from .common import InfoExtractor as InfoExtractor
from .paramountplus import ParamountPlusIE as ParamountPlusIE

class CBSNewsBaseIE(InfoExtractor): ...

class CBSNewsEmbedIE(CBSNewsBaseIE):
    IE_NAME: str

class CBSNewsIE(CBSNewsBaseIE):
    IE_NAME: str
    IE_DESC: str

class CBSLocalBaseIE(CBSNewsBaseIE): ...
class CBSLocalIE(CBSLocalBaseIE): ...
class CBSLocalArticleIE(CBSLocalBaseIE): ...
class CBSNewsLiveBaseIE(CBSNewsBaseIE): ...
class CBSLocalLiveIE(CBSNewsLiveBaseIE): ...

class CBSNewsLiveIE(CBSNewsLiveBaseIE):
    IE_NAME: str
    IE_DESC: str

class CBSNewsLiveVideoIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
