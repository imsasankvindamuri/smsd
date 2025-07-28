from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601, str_or_none as str_or_none, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from .youtube import YoutubeIE as YoutubeIE

class EggsBaseIE(InfoExtractor): ...

class EggsIE(EggsBaseIE):
    IE_NAME: str

class EggsArtistIE(EggsBaseIE):
    IE_NAME: str
