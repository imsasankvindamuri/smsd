from ..networking.exceptions import HTTPError as HTTPError
from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, extract_attributes as extract_attributes, filter_dict as filter_dict, float_or_none as float_or_none, get_element_by_class as get_element_by_class, get_element_html_by_class as get_element_html_by_class, int_or_none as int_or_none, jwt_decode_hs256 as jwt_decode_hs256, jwt_encode_hs256 as jwt_encode_hs256, make_archive_id as make_archive_id, merge_dicts as merge_dicts, parse_age_limit as parse_age_limit, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, str_or_none as str_or_none, strip_or_none as strip_or_none, traverse_obj as traverse_obj, try_call as try_call, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class VRTBaseIE(InfoExtractor): ...

class VRTIE(VRTBaseIE):
    IE_DESC: str

class VrtNUIE(VRTBaseIE):
    IE_NAME: str
    IE_DESC: str

class DagelijkseKostIE(VRTBaseIE):
    IE_DESC: str

class Radio1BeIE(VRTBaseIE): ...
