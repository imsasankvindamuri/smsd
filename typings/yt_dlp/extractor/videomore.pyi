from ..utils import int_or_none as int_or_none, parse_qs as parse_qs
from .common import InfoExtractor as InfoExtractor

class VideomoreBaseIE(InfoExtractor): ...

class VideomoreIE(InfoExtractor):
    IE_NAME: str

class VideomoreVideoIE(VideomoreBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class VideomoreSeasonIE(VideomoreBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
