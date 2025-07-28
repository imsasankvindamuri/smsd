from ..utils import OnDemandPagedList as OnDemandPagedList, format_field as format_field, int_or_none as int_or_none, parse_resolution as parse_resolution, str_or_none as str_or_none, try_get as try_get, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete
from collections.abc import Generator

class PeerTubeIE(InfoExtractor): ...

class PeerTubePlaylistIE(InfoExtractor):
    IE_NAME: str
    def call_api(self, host, name, path, base, **kwargs): ...
    def fetch_page(self, host, playlist_id, playlist_type, page) -> Generator[Incomplete, None, Incomplete]: ...
