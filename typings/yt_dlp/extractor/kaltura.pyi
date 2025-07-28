from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, format_field as format_field, int_or_none as int_or_none, remove_start as remove_start, smuggle_url as smuggle_url, traverse_obj as traverse_obj, unsmuggle_url as unsmuggle_url
from .common import InfoExtractor as InfoExtractor

class KalturaIE(InfoExtractor):
    IFRAME_PACKAGE_DATA_REGEX: str
