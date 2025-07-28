from ..utils import ExtractorError as ExtractorError, encode_data_uri as encode_data_uri, float_or_none as float_or_none, int_or_none as int_or_none, join_nonempty as join_nonempty, mimetype2ext as mimetype2ext, str_or_none as str_or_none
from .common import InfoExtractor as InfoExtractor

class UstreamIE(InfoExtractor):
    IE_NAME: str

class UstreamChannelIE(InfoExtractor):
    IE_NAME: str
