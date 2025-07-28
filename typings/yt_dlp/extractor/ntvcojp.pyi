from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601, str_or_none as str_or_none, url_or_none as url_or_none
from ..utils.traversal import require as require, traverse_obj as traverse_obj
from .streaks import StreaksBaseIE as StreaksBaseIE

class NTVCoJpCUIE(StreaksBaseIE):
    IE_NAME: str
    IE_DESC: str
