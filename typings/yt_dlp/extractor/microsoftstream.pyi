from ..utils import merge_dicts as merge_dicts, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, parse_resolution as parse_resolution, try_get as try_get, url_basename as url_basename
from .common import InfoExtractor as InfoExtractor

class MicrosoftStreamIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    def extract_all_subtitles(self, *args, **kwargs): ...
