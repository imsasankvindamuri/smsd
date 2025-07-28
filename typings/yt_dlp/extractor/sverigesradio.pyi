from ..utils import determine_ext as determine_ext, extract_attributes as extract_attributes, get_element_by_id as get_element_by_id, get_element_html_by_class as get_element_html_by_class, int_or_none as int_or_none, str_or_none as str_or_none, traverse_obj as traverse_obj, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class SverigesRadioBaseIE(InfoExtractor): ...

class SverigesRadioPublicationIE(SverigesRadioBaseIE):
    IE_NAME: str

class SverigesRadioEpisodeIE(SverigesRadioBaseIE):
    IE_NAME: str
