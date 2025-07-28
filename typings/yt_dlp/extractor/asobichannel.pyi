from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, merge_dicts as merge_dicts, parse_iso8601 as parse_iso8601, url_or_none as url_or_none
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class AsobiChannelBaseIE(InfoExtractor): ...

class AsobiChannelIE(AsobiChannelBaseIE):
    IE_NAME: str
    IE_DESC: str

class AsobiChannelTagURLIE(AsobiChannelBaseIE):
    IE_NAME: str
    IE_DESC: str
