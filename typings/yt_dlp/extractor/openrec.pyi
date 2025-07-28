from ..utils import ExtractorError as ExtractorError, get_first as get_first, int_or_none as int_or_none, traverse_obj as traverse_obj, try_get as try_get, unified_strdate as unified_strdate, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class OpenRecBaseIE(InfoExtractor): ...

class OpenRecIE(OpenRecBaseIE):
    IE_NAME: str

class OpenRecCaptureIE(OpenRecBaseIE):
    IE_NAME: str

class OpenRecMovieIE(OpenRecBaseIE):
    IE_NAME: str
