from ..utils import InAdvancePagedList as InAdvancePagedList, int_or_none as int_or_none, str_or_none as str_or_none, traverse_obj as traverse_obj, try_call as try_call, update_url_query as update_url_query
from .common import InfoExtractor as InfoExtractor
from .videa import VideaIE as VideaIE

class XimalayaBaseIE(InfoExtractor): ...

class XimalayaIE(XimalayaBaseIE):
    IE_NAME: str
    IE_DESC: str

class XimalayaAlbumIE(XimalayaBaseIE):
    IE_NAME: str
    IE_DESC: str
