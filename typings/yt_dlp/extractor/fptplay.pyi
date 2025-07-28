from ..utils import clean_html as clean_html, join_nonempty as join_nonempty, strip_or_none as strip_or_none
from .common import InfoExtractor as InfoExtractor

class FptplayIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
    def get_api_with_st_token(self, video_id, episode): ...
