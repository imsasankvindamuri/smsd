from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, extract_attributes as extract_attributes, parse_duration as parse_duration, parse_qs as parse_qs
from ..utils.traversal import find_element as find_element, find_elements as find_elements, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class VrSquareIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class VrSquarePlaylistBaseIE(InfoExtractor): ...

class VrSquareChannelIE(VrSquarePlaylistBaseIE):
    IE_NAME: str

class VrSquareSearchIE(VrSquarePlaylistBaseIE):
    IE_NAME: str

class VrSquareSectionIE(VrSquarePlaylistBaseIE):
    IE_NAME: str
