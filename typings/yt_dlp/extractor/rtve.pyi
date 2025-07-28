from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, determine_ext as determine_ext, float_or_none as float_or_none, make_archive_id as make_archive_id, parse_iso8601 as parse_iso8601, qualities as qualities, url_or_none as url_or_none
from ..utils.traversal import subs_list_to_dict as subs_list_to_dict, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class RTVEBaseIE(InfoExtractor): ...

class RTVEALaCartaIE(RTVEBaseIE):
    IE_NAME: str
    IE_DESC: str

class RTVEAudioIE(RTVEBaseIE):
    IE_NAME: str
    IE_DESC: str

class RTVELiveIE(RTVEBaseIE):
    IE_NAME: str
    IE_DESC: str

class RTVETelevisionIE(InfoExtractor):
    IE_NAME: str
