from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, remove_end as remove_end, smuggle_url as smuggle_url, strip_or_none as strip_or_none, traverse_obj as traverse_obj, try_get as try_get, unified_timestamp as unified_timestamp, unsmuggle_url as unsmuggle_url, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class ViuBaseIE(InfoExtractor): ...
class ViuIE(ViuBaseIE): ...

class ViuPlaylistIE(ViuBaseIE):
    IE_NAME: str

class ViuOTTIE(InfoExtractor):
    IE_NAME: str

class ViuOTTIndonesiaBaseIE(InfoExtractor): ...
class ViuOTTIndonesiaIE(ViuOTTIndonesiaBaseIE): ...
