from ..utils import UnsupportedError as UnsupportedError, bool_or_none as bool_or_none, determine_ext as determine_ext, int_or_none as int_or_none, js_to_json as js_to_json, parse_qs as parse_qs, str_or_none as str_or_none, try_get as try_get, unified_timestamp as unified_timestamp, url_or_none as url_or_none
from ..utils.traversal import subs_list_to_dict as subs_list_to_dict, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class RutubeBaseIE(InfoExtractor): ...

class RutubeIE(RutubeBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubeEmbedIE(RutubeBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubePlaylistBaseIE(RutubeBaseIE): ...

class RutubeTagsIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubeMovieIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubePersonIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubePlaylistIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str

class RutubeChannelIE(RutubePlaylistBaseIE):
    IE_NAME: str
    IE_DESC: str
