from ..jsinterp import js_number_to_string as js_number_to_string
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, dict_get as dict_get, filter_dict as filter_dict, float_or_none as float_or_none, format_field as format_field, int_or_none as int_or_none, join_nonempty as join_nonempty, make_archive_id as make_archive_id, remove_end as remove_end, str_or_none as str_or_none, strip_or_none as strip_or_none, truncate_string as truncate_string, try_call as try_call, try_get as try_get, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, xpath_text as xpath_text
from ..utils.traversal import require as require, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from .periscope import PeriscopeBaseIE as PeriscopeBaseIE, PeriscopeIE as PeriscopeIE
from _typeshed import Incomplete

class TwitterBaseIE(InfoExtractor):
    @property
    def is_logged_in(self): ...

class TwitterCardIE(InfoExtractor):
    IE_NAME: str

class TwitterIE(TwitterBaseIE):
    IE_NAME: str

class TwitterAmplifyIE(TwitterBaseIE):
    IE_NAME: str

class TwitterBroadcastIE(TwitterBaseIE, PeriscopeBaseIE):
    IE_NAME: str

class TwitterSpacesIE(TwitterBaseIE):
    IE_NAME: str
    SPACE_STATUS: Incomplete

class TwitterShortenerIE(TwitterBaseIE):
    IE_NAME: str
