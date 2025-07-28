from ..utils import clean_html as clean_html, format_field as format_field, get_element_by_class as get_element_by_class, parse_duration as parse_duration, parse_qs as parse_qs, traverse_obj as traverse_obj, unified_timestamp as unified_timestamp, update_url_query as update_url_query, url_basename as url_basename
from .common import InfoExtractor as InfoExtractor

class TelegramEmbedIE(InfoExtractor):
    IE_NAME: str
