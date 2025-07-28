from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, extract_attributes as extract_attributes, parse_duration as parse_duration, parse_qs as parse_qs, unified_strdate as unified_strdate
from ..utils.traversal import find_element as find_element, require as require, traverse_obj as traverse_obj
from .ard import ARDMediathekBaseIE as ARDMediathekBaseIE

class SRMediathekIE(ARDMediathekBaseIE):
    IE_NAME: str
    IE_DESC: str
