from ..utils import ExtractorError as ExtractorError, OnDemandPagedList as OnDemandPagedList, int_or_none as int_or_none, jwt_decode_hs256 as jwt_decode_hs256, mimetype2ext as mimetype2ext, qualities as qualities, traverse_obj as traverse_obj, try_call as try_call, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class IwaraBaseIE(InfoExtractor): ...

class IwaraIE(IwaraBaseIE):
    IE_NAME: str

class IwaraUserIE(IwaraBaseIE):
    IE_NAME: str

class IwaraPlaylistIE(IwaraBaseIE):
    IE_NAME: str
