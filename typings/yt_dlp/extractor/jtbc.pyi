from ..utils import int_or_none as int_or_none, parse_duration as parse_duration, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class JTBCIE(InfoExtractor):
    IE_DESC: str

class JTBCProgramIE(InfoExtractor):
    IE_NAME: str
