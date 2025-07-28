from ..utils import OnDemandPagedList as OnDemandPagedList, clean_podcast_url as clean_podcast_url, float_or_none as float_or_none, int_or_none as int_or_none, strip_or_none as strip_or_none, traverse_obj as traverse_obj, try_get as try_get, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class SpotifyBaseIE(InfoExtractor): ...

class SpotifyIE(SpotifyBaseIE):
    IE_NAME: str
    IE_DESC: str

class SpotifyShowIE(SpotifyBaseIE):
    IE_NAME: str
    IE_DESC: str
