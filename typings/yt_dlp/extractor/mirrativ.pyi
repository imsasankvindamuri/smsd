from ..utils import ExtractorError as ExtractorError, dict_get as dict_get, traverse_obj as traverse_obj, try_get as try_get
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class MirrativBaseIE(InfoExtractor):
    def assert_error(self, response) -> None: ...

class MirrativIE(MirrativBaseIE):
    IE_NAME: str
    TESTS: Incomplete

class MirrativUserIE(MirrativBaseIE):
    IE_NAME: str
