from ...utils import ExtractorError as ExtractorError, traverse_obj as traverse_obj
from ._tab import YoutubeTabBaseInfoExtractor as YoutubeTabBaseInfoExtractor
from ._video import YoutubeIE as YoutubeIE

class YoutubeClipIE(YoutubeTabBaseInfoExtractor):
    IE_NAME: str
