from ..utils import int_or_none as int_or_none, parse_duration as parse_duration
from .common import InfoExtractor as InfoExtractor

class RtlNlIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class RTLLuBaseIE(InfoExtractor):
    def get_media_url(self, webpage, video_id, media_type): ...
    def get_formats_and_subtitles(self, webpage, video_id): ...

class RTLLuTeleVODIE(RTLLuBaseIE):
    IE_NAME: str

class RTLLuArticleIE(RTLLuBaseIE):
    IE_NAME: str

class RTLLuLiveIE(RTLLuBaseIE): ...
class RTLLuRadioIE(RTLLuBaseIE): ...
