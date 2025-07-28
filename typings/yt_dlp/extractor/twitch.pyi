from ..utils import ExtractorError as ExtractorError, UserNotLive as UserNotLive, base_url as base_url, clean_html as clean_html, dict_get as dict_get, float_or_none as float_or_none, int_or_none as int_or_none, join_nonempty as join_nonempty, make_archive_id as make_archive_id, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, qualities as qualities, str_or_none as str_or_none, try_get as try_get, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, urljoin as urljoin
from ..utils.traversal import traverse_obj as traverse_obj, value as value
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete
from typing import NamedTuple

class TwitchBaseIE(InfoExtractor): ...

class TwitchVodIE(TwitchBaseIE):
    IE_NAME: str

class TwitchCollectionIE(TwitchBaseIE): ...
class TwitchPlaylistBaseIE(TwitchBaseIE): ...
class TwitchVideosBaseIE(TwitchPlaylistBaseIE): ...

class TwitchVideosIE(TwitchVideosBaseIE):

    class Broadcast(NamedTuple):
        type: Incomplete
        label: Incomplete
    @classmethod
    def suitable(cls, url): ...

class TwitchVideosClipsIE(TwitchPlaylistBaseIE):

    class Clip(NamedTuple):
        filter: Incomplete
        label: Incomplete

class TwitchVideosCollectionsIE(TwitchPlaylistBaseIE): ...

class TwitchStreamIE(TwitchVideosBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class TwitchClipsIE(TwitchBaseIE):
    IE_NAME: str
