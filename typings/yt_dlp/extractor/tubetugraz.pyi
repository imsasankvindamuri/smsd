from ..utils import float_or_none as float_or_none, parse_resolution as parse_resolution, traverse_obj as traverse_obj, urlencode_postdata as urlencode_postdata, variadic as variadic
from .common import InfoExtractor as InfoExtractor

class TubeTuGrazBaseIE(InfoExtractor): ...

class TubeTuGrazIE(TubeTuGrazBaseIE):
    IE_DESC: str

class TubeTuGrazSeriesIE(TubeTuGrazBaseIE): ...
