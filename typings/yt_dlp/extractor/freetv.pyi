from ..utils import int_or_none as int_or_none, traverse_obj as traverse_obj, urlencode_postdata as urlencode_postdata
from .common import InfoExtractor as InfoExtractor

class FreeTvBaseIE(InfoExtractor): ...
class FreeTvMoviesIE(FreeTvBaseIE): ...

class FreeTvIE(FreeTvBaseIE):
    IE_NAME: str
