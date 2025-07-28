from ..aes import aes_cbc_encrypt_bytes as aes_cbc_encrypt_bytes
from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, float_or_none as float_or_none, int_or_none as int_or_none, js_to_json as js_to_json, traverse_obj as traverse_obj, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class TencentBaseIE(InfoExtractor): ...
class VQQBaseIE(TencentBaseIE): ...

class VQQVideoIE(VQQBaseIE):
    IE_NAME: str

class VQQSeriesIE(VQQBaseIE):
    IE_NAME: str

class WeTvBaseIE(TencentBaseIE): ...

class WeTvEpisodeIE(WeTvBaseIE):
    IE_NAME: str

class WeTvSeriesIE(WeTvBaseIE): ...
class IflixBaseIE(WeTvBaseIE): ...

class IflixEpisodeIE(IflixBaseIE):
    IE_NAME: str

class IflixSeriesIE(IflixBaseIE): ...
