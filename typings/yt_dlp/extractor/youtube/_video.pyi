from ...jsinterp import JSInterpreter as JSInterpreter
from ...networking.exceptions import HTTPError as HTTPError
from ...utils import ExtractorError as ExtractorError, LazyList as LazyList, NO_DEFAULT as NO_DEFAULT, bug_reports_message as bug_reports_message, clean_html as clean_html, datetime_from_str as datetime_from_str, filesize_from_tbr as filesize_from_tbr, filter_dict as filter_dict, float_or_none as float_or_none, format_field as format_field, get_first as get_first, int_or_none as int_or_none, join_nonempty as join_nonempty, js_to_json as js_to_json, mimetype2ext as mimetype2ext, orderedSet as orderedSet, parse_codecs as parse_codecs, parse_count as parse_count, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, qualities as qualities, remove_end as remove_end, remove_start as remove_start, smuggle_url as smuggle_url, str_or_none as str_or_none, str_to_int as str_to_int, strftime_or_none as strftime_or_none, traverse_obj as traverse_obj, try_call as try_call, try_get as try_get, unescapeHTML as unescapeHTML, unified_strdate as unified_strdate, unsmuggle_url as unsmuggle_url, update_url_query as update_url_query, url_or_none as url_or_none, urljoin as urljoin, variadic as variadic
from ...utils.networking import clean_headers as clean_headers, clean_proxies as clean_proxies, select_proxy as select_proxy
from ..openload import PhantomJSwrapper as PhantomJSwrapper
from ._base import BadgeType as BadgeType, INNERTUBE_CLIENTS as INNERTUBE_CLIENTS, YoutubeBaseInfoExtractor as YoutubeBaseInfoExtractor, short_client_name as short_client_name
from .pot._director import initialize_pot_director as initialize_pot_director
from .pot.provider import PoTokenContext as PoTokenContext, PoTokenRequest as PoTokenRequest

STREAMING_DATA_CLIENT_NAME: str
STREAMING_DATA_INITIAL_PO_TOKEN: str
STREAMING_DATA_FETCH_SUBS_PO_TOKEN: str
STREAMING_DATA_INNERTUBE_CONTEXT: str
PO_TOKEN_GUIDE_URL: str

class YoutubeIE(YoutubeBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def extract_id(cls, url): ...
    def fetch_po_token(self, client: str = 'web', context=..., ytcfg=None, visitor_data=None, data_sync_id=None, session_index=None, player_url=None, video_id=None, webpage=None, required: bool = False, **kwargs): ...
