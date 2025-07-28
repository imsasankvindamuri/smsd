from ..utils import int_or_none as int_or_none, merge_dicts as merge_dicts, parse_iso8601 as parse_iso8601
from ..utils.traversal import require as require, traverse_obj as traverse_obj
from .zdf import ZDFBaseIE as ZDFBaseIE

class DreiSatIE(ZDFBaseIE):
    IE_NAME: str
