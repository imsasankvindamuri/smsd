from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, bug_reports_message as bug_reports_message, decode_base_n as decode_base_n, encode_base_n as encode_base_n, filter_dict as filter_dict, float_or_none as float_or_none, format_field as format_field, get_element_by_attribute as get_element_by_attribute, int_or_none as int_or_none, join_nonempty as join_nonempty, lowercase_escape as lowercase_escape, str_or_none as str_or_none, str_to_int as str_to_int, traverse_obj as traverse_obj, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class InstagramBaseIE(InfoExtractor): ...

class InstagramIOSIE(InfoExtractor):
    IE_DESC: str

class InstagramIE(InstagramBaseIE): ...
class InstagramPlaylistBaseIE(InstagramBaseIE): ...

class InstagramUserIE(InstagramPlaylistBaseIE):
    IE_DESC: str
    IE_NAME: str

class InstagramTagIE(InstagramPlaylistBaseIE):
    IE_DESC: str
    IE_NAME: str

class InstagramStoryIE(InstagramBaseIE):
    IE_NAME: str
