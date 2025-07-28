from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, url_or_none as url_or_none
from ..utils.traversal import subs_list_to_dict as subs_list_to_dict, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class MonsterSirenHypergryphMusicIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
