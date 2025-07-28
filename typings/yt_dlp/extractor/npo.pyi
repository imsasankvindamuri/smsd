from ..utils import determine_ext as determine_ext, int_or_none as int_or_none, merge_dicts as merge_dicts, orderedSet as orderedSet, str_or_none as str_or_none, try_call as try_call, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class NPOIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class NPOLiveIE(InfoExtractor):
    IE_NAME: str

class NPORadioIE(InfoExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class NPORadioFragmentIE(InfoExtractor):
    IE_NAME: str

class NPODataMidEmbedIE(InfoExtractor): ...

class SchoolTVIE(NPODataMidEmbedIE):
    IE_NAME: str

class HetKlokhuisIE(NPODataMidEmbedIE):
    IE_NAME: str

class NPOPlaylistBaseIE(NPOIE): ...

class VPROIE(NPOPlaylistBaseIE):
    IE_NAME: str

class WNLIE(NPOPlaylistBaseIE):
    IE_NAME: str

class AndereTijdenIE(NPOPlaylistBaseIE):
    IE_NAME: str
