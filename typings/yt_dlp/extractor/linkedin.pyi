from ..utils import ExtractorError as ExtractorError, extract_attributes as extract_attributes, float_or_none as float_or_none, int_or_none as int_or_none, mimetype2ext as mimetype2ext, srt_subtitles_timecode as srt_subtitles_timecode, try_get as try_get, url_or_none as url_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from ..utils.traversal import find_elements as find_elements, require as require, traverse_obj as traverse_obj
from .common import InfoExtractor as InfoExtractor

class LinkedInBaseIE(InfoExtractor): ...
class LinkedInLearningBaseIE(LinkedInBaseIE): ...
class LinkedInIE(LinkedInBaseIE): ...

class LinkedInLearningIE(LinkedInLearningBaseIE):
    IE_NAME: str
    def json2srt(self, transcript_lines, duration=None): ...

class LinkedInLearningCourseIE(LinkedInLearningBaseIE):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class LinkedInEventsIE(LinkedInBaseIE):
    IE_NAME: str
