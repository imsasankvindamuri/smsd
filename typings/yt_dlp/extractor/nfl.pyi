from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, get_element_by_class as get_element_by_class, int_or_none as int_or_none, make_archive_id as make_archive_id, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata
from ..utils.traversal import traverse_obj as traverse_obj
from .anvato import AnvatoIE as AnvatoIE
from .common import InfoExtractor as InfoExtractor

class NFLBaseIE(InfoExtractor): ...

class NFLIE(NFLBaseIE):
    IE_NAME: str

class NFLArticleIE(NFLBaseIE):
    IE_NAME: str

class NFLPlusReplayIE(NFLBaseIE):
    IE_NAME: str

class NFLPlusEpisodeIE(NFLBaseIE):
    IE_NAME: str
