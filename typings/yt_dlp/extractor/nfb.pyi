from ..utils import int_or_none as int_or_none, join_nonempty as join_nonempty, merge_dicts as merge_dicts, parse_count as parse_count, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class NFBBaseIE(InfoExtractor): ...

class NFBIE(NFBBaseIE):
    IE_NAME: str
    IE_DESC: str

class NFBSeriesIE(NFBBaseIE):
    IE_NAME: str
    IE_DESC: str
