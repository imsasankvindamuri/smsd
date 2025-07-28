from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, dict_get as dict_get, int_or_none as int_or_none, js_to_json as js_to_json, str_or_none as str_or_none, strip_or_none as strip_or_none, traverse_obj as traverse_obj, try_get as try_get, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class TVPIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class TVPStreamIE(InfoExtractor):
    IE_NAME: str

class TVPEmbedIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class TVPVODBaseIE(InfoExtractor): ...

class TVPVODVideoIE(TVPVODBaseIE):
    IE_NAME: str

class TVPVODSeriesIE(TVPVODBaseIE):
    IE_NAME: str
