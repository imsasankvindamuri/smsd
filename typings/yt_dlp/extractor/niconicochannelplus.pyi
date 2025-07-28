from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, filter_dict as filter_dict, int_or_none as int_or_none, parse_qs as parse_qs, str_or_none as str_or_none, traverse_obj as traverse_obj, unified_timestamp as unified_timestamp, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class NiconicoChannelPlusBaseIE(InfoExtractor): ...

class NiconicoChannelPlusIE(NiconicoChannelPlusBaseIE):
    IE_NAME: str
    IE_DESC: str

class NiconicoChannelPlusChannelBaseIE(NiconicoChannelPlusBaseIE): ...

class NiconicoChannelPlusChannelVideosIE(NiconicoChannelPlusChannelBaseIE):
    IE_NAME: str
    IE_DESC: str

class NiconicoChannelPlusChannelLivesIE(NiconicoChannelPlusChannelBaseIE):
    IE_NAME: str
    IE_DESC: str
