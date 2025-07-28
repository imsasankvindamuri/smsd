from ...utils import traverse_obj as traverse_obj
from ._tab import YoutubeTabBaseInfoExtractor as YoutubeTabBaseInfoExtractor, YoutubeTabIE as YoutubeTabIE
from ._video import YoutubeIE as YoutubeIE

class YoutubeNotificationsIE(YoutubeTabBaseInfoExtractor):
    IE_NAME: str
    IE_DESC: str
