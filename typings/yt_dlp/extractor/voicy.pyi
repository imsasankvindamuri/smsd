from ..utils import ExtractorError as ExtractorError, smuggle_url as smuggle_url, str_or_none as str_or_none, traverse_obj as traverse_obj, unified_strdate as unified_strdate, unsmuggle_url as unsmuggle_url
from .common import InfoExtractor as InfoExtractor

class VoicyBaseIE(InfoExtractor): ...

class VoicyIE(VoicyBaseIE):
    IE_NAME: str
    ARTICLE_LIST_API_URL: str

class VoicyChannelIE(VoicyBaseIE):
    IE_NAME: str
    PROGRAM_LIST_API_URL: str
    @classmethod
    def suitable(cls, url): ...
