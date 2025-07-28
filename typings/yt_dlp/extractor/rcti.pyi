from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, dict_get as dict_get, strip_or_none as strip_or_none, traverse_obj as traverse_obj, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class RCTIPlusBaseIE(InfoExtractor): ...
class RCTIPlusIE(RCTIPlusBaseIE): ...

class RCTIPlusSeriesIE(RCTIPlusBaseIE):
    @classmethod
    def suitable(cls, url): ...

class RCTIPlusTVIE(RCTIPlusBaseIE):
    @classmethod
    def suitable(cls, url): ...
