from ..utils import determine_ext as determine_ext, dict_get as dict_get, int_or_none as int_or_none, try_get as try_get, unified_timestamp as unified_timestamp
from ..utils.traversal import require as require, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class SVTBaseIE(InfoExtractor): ...

class SVTPlayIE(SVTBaseIE):
    IE_NAME: str
    IE_DESC: str

class SVTSeriesIE(SVTBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class SVTPageIE(SVTBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...
