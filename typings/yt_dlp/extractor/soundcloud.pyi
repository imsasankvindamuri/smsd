from ..networking import HEADRequest as HEADRequest
from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, float_or_none as float_or_none, int_or_none as int_or_none, join_nonempty as join_nonempty, mimetype2ext as mimetype2ext, parse_qs as parse_qs, str_or_none as str_or_none, try_call as try_call, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_or_none as url_or_none, urlhandle_detect_ext as urlhandle_detect_ext
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor, SearchInfoExtractor as SearchInfoExtractor

class SoundcloudEmbedIE(InfoExtractor): ...

class SoundcloudBaseIE(InfoExtractor):
    def sign(self, user, pw, clid): ...

class SoundcloudIE(SoundcloudBaseIE):
    IE_NAME: str

class SoundcloudPlaylistBaseIE(SoundcloudBaseIE): ...

class SoundcloudSetIE(SoundcloudPlaylistBaseIE):
    IE_NAME: str

class SoundcloudPagedPlaylistBaseIE(SoundcloudBaseIE): ...

class SoundcloudUserIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundcloudUserPermalinkIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundcloudTrackStationIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundcloudRelatedIE(SoundcloudPagedPlaylistBaseIE):
    IE_NAME: str

class SoundcloudPlaylistIE(SoundcloudPlaylistBaseIE):
    IE_NAME: str

class SoundcloudSearchIE(SoundcloudBaseIE, SearchInfoExtractor):
    IE_NAME: str
    IE_DESC: str
