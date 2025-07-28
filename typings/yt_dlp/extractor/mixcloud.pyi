from ..compat import compat_ord as compat_ord
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, try_get as try_get, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class MixcloudBaseIE(InfoExtractor): ...

class MixcloudIE(MixcloudBaseIE):
    IE_NAME: str

class MixcloudPlaylistBaseIE(MixcloudBaseIE): ...

class MixcloudUserIE(MixcloudPlaylistBaseIE):
    IE_NAME: str

class MixcloudPlaylistIE(MixcloudPlaylistBaseIE):
    IE_NAME: str
