import enum
from _typeshed import Incomplete
from yt_dlp.extractor.youtube.pot.provider import PoTokenRequest

__all__ = ['WEBPO_CLIENTS', 'ContentBindingType', 'get_webpo_content_binding']

WEBPO_CLIENTS: Incomplete

class ContentBindingType(enum.Enum):
    VISITOR_DATA = 'visitor_data'
    DATASYNC_ID = 'datasync_id'
    VIDEO_ID = 'video_id'
    VISITOR_ID = 'visitor_id'

def get_webpo_content_binding(request: PoTokenRequest, webpo_clients=..., bind_to_visitor_id: bool = False) -> tuple[str | None, ContentBindingType | None]: ...
