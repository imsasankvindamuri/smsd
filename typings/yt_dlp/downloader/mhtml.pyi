from ..compat import imghdr as imghdr
from ..utils import escapeHTML as escapeHTML, formatSeconds as formatSeconds, srt_subtitles_timecode as srt_subtitles_timecode, urljoin as urljoin
from .fragment import FragmentFD as FragmentFD

class MhtmlFD(FragmentFD):
    def real_download(self, filename, info_dict): ...
