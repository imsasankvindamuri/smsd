from ..utils import ExtractorError as ExtractorError, InAdvancePagedList as InAdvancePagedList, determine_ext as determine_ext, extract_attributes as extract_attributes, int_or_none as int_or_none, js_to_json as js_to_json, parse_iso8601 as parse_iso8601, strip_or_none as strip_or_none, traverse_obj as traverse_obj, unescapeHTML as unescapeHTML, unified_timestamp as unified_timestamp, url_or_none as url_or_none, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class PolskieRadioBaseIE(InfoExtractor): ...

class PolskieRadioLegacyIE(PolskieRadioBaseIE):
    IE_NAME: str

class PolskieRadioIE(PolskieRadioBaseIE): ...

class PolskieRadioAuditionIE(InfoExtractor):
    IE_NAME: str

class PolskieRadioCategoryIE(InfoExtractor):
    IE_NAME: str
    @classmethod
    def suitable(cls, url): ...

class PolskieRadioPlayerIE(InfoExtractor):
    IE_NAME: str

class PolskieRadioPodcastBaseIE(InfoExtractor): ...

class PolskieRadioPodcastListIE(PolskieRadioPodcastBaseIE):
    IE_NAME: str

class PolskieRadioPodcastIE(PolskieRadioPodcastBaseIE):
    IE_NAME: str
