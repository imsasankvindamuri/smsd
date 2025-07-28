import functools
from ...networking.exceptions import HTTPError as HTTPError, network_exceptions as network_exceptions
from ...utils import ExtractorError as ExtractorError, NO_DEFAULT as NO_DEFAULT, UserNotLive as UserNotLive, bug_reports_message as bug_reports_message, format_field as format_field, get_first as get_first, int_or_none as int_or_none, parse_count as parse_count, parse_duration as parse_duration, parse_qs as parse_qs, smuggle_url as smuggle_url, str_to_int as str_to_int, strftime_or_none as strftime_or_none, traverse_obj as traverse_obj, try_get as try_get, unsmuggle_url as unsmuggle_url, update_url_query as update_url_query, url_or_none as url_or_none, urljoin as urljoin, variadic as variadic
from ._base import BadgeType as BadgeType, YoutubeBaseInfoExtractor as YoutubeBaseInfoExtractor
from ._video import YoutubeIE as YoutubeIE

class YoutubeTabBaseInfoExtractor(YoutubeBaseInfoExtractor):
    @staticmethod
    def passthrough_smuggled_data(func): ...
    @functools.cached_property
    def skip_webpage(self): ...

class YoutubeTabIE(YoutubeTabBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class YoutubePlaylistIE(YoutubeBaseInfoExtractor):
    IE_DESC: str
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
