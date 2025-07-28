from ..utils import clean_html as clean_html, parse_iso8601 as parse_iso8601, update_url as update_url, url_or_none as url_or_none
from ..utils.traversal import subs_list_to_dict as subs_list_to_dict, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor
from .youtube import YoutubeIE as YoutubeIE

class StarTrekIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
