from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, join_nonempty as join_nonempty, str_or_none as str_or_none, traverse_obj as traverse_obj, update_url as update_url, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class TelecincoBaseIE(InfoExtractor): ...

class TelecincoIE(TelecincoBaseIE):
    IE_DESC: str
