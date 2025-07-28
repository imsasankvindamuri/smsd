from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, join_nonempty as join_nonempty, parse_age_limit as parse_age_limit, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class ViewLiftBaseIE(InfoExtractor): ...

class ViewLiftEmbedIE(ViewLiftBaseIE):
    IE_NAME: str

class ViewLiftIE(ViewLiftBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
