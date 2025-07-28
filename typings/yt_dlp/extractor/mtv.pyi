from ..networking import HEADRequest as HEADRequest, Request as Request
from ..utils import ExtractorError as ExtractorError, RegexNotFoundError as RegexNotFoundError, find_xpath_attr as find_xpath_attr, fix_xml_ampersands as fix_xml_ampersands, float_or_none as float_or_none, int_or_none as int_or_none, join_nonempty as join_nonempty, strip_or_none as strip_or_none, timeconvert as timeconvert, try_get as try_get, unescapeHTML as unescapeHTML, update_url_query as update_url_query, url_basename as url_basename, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class MTVServicesInfoExtractor(InfoExtractor): ...

class MTVServicesEmbeddedIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVJapanIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVVideoIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVDEIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVItaliaIE(MTVServicesInfoExtractor):
    IE_NAME: str

class MTVItaliaProgrammaIE(MTVItaliaIE):
    IE_NAME: str
