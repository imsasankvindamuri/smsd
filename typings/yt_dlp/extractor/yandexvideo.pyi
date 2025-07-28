from ..utils import bug_reports_message as bug_reports_message, determine_ext as determine_ext, int_or_none as int_or_none, lowercase_escape as lowercase_escape, parse_qs as parse_qs, qualities as qualities, try_get as try_get, update_url_query as update_url_query, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class YandexVideoIE(InfoExtractor): ...
class YandexVideoPreviewIE(InfoExtractor): ...
class ZenYandexBaseIE(InfoExtractor): ...

class ZenYandexIE(ZenYandexBaseIE):
    IE_NAME: str
    IE_DESC: str

class ZenYandexChannelIE(ZenYandexBaseIE):
    IE_NAME: str
