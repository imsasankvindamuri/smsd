from ..utils import ExtractorError as ExtractorError, bug_reports_message as bug_reports_message, determine_ext as determine_ext, extract_attributes as extract_attributes, get_element_by_class as get_element_by_class, get_element_html_by_id as get_element_html_by_id, int_or_none as int_or_none, lowercase_escape as lowercase_escape, try_get as try_get, update_url_query as update_url_query
from .common import InfoExtractor as InfoExtractor
from .youtube import YoutubeIE as YoutubeIE

class GoogleDriveIE(InfoExtractor): ...

class GoogleDriveFolderIE(InfoExtractor):
    IE_NAME: str
