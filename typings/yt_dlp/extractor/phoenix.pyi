from ..utils import int_or_none as int_or_none, merge_dicts as merge_dicts, try_get as try_get, unified_timestamp as unified_timestamp
from .youtube import YoutubeIE as YoutubeIE
from .zdf import ZDFBaseIE as ZDFBaseIE

class PhoenixIE(ZDFBaseIE):
    IE_NAME: str
