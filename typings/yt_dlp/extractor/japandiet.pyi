from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, join_nonempty as join_nonempty, parse_qs as parse_qs, smuggle_url as smuggle_url, traverse_obj as traverse_obj, try_call as try_call, unsmuggle_url as unsmuggle_url
from .common import InfoExtractor as InfoExtractor

class ShugiinItvBaseIE(InfoExtractor): ...

class ShugiinItvLiveIE(ShugiinItvBaseIE):
    IE_DESC: str
    @classmethod
    def suitable(cls, url): ...

class ShugiinItvLiveRoomIE(ShugiinItvBaseIE):
    IE_DESC: str

class ShugiinItvVodIE(ShugiinItvBaseIE):
    IE_DESC: str

class SangiinInstructionIE(InfoExtractor):
    IE_DESC: bool

class SangiinIE(InfoExtractor):
    IE_DESC: str
