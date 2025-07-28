from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, format_field as format_field, parse_iso8601 as parse_iso8601, traverse_obj as traverse_obj, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class WykopBaseIE(InfoExtractor): ...

class WykopDigIE(WykopBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class WykopDigCommentIE(WykopBaseIE):
    IE_NAME: str

class WykopPostIE(WykopBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class WykopPostCommentIE(WykopBaseIE):
    IE_NAME: str
