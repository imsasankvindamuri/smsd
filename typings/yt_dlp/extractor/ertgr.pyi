from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, dict_get as dict_get, int_or_none as int_or_none, merge_dicts as merge_dicts, parse_age_limit as parse_age_limit, parse_iso8601 as parse_iso8601, parse_qs as parse_qs, str_or_none as str_or_none, try_get as try_get, url_or_none as url_or_none, variadic as variadic
from ..utils.traversal import traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class ERTFlixBaseIE(InfoExtractor): ...

class ERTFlixCodenameIE(ERTFlixBaseIE):
    IE_NAME: str
    IE_DESC: str

class ERTFlixIE(ERTFlixBaseIE):
    IE_NAME: str
    IE_DESC: str

class ERTWebtvEmbedIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
