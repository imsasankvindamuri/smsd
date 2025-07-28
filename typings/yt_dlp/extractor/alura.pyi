from ..utils import ExtractorError as ExtractorError, clean_html as clean_html, int_or_none as int_or_none, urlencode_postdata as urlencode_postdata, urljoin as urljoin
from .common import InfoExtractor as InfoExtractor

class AluraIE(InfoExtractor): ...

class AluraCourseIE(AluraIE):
    @classmethod
    def suitable(cls, url): ...
