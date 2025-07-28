from ..utils import clean_html as clean_html, format_field as format_field, int_or_none as int_or_none, str_or_none as str_or_none, strip_or_none as strip_or_none
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class MindsBaseIE(InfoExtractor): ...

class MindsIE(MindsBaseIE):
    IE_NAME: str

class MindsFeedBaseIE(MindsBaseIE): ...

class MindsChannelIE(MindsFeedBaseIE):
    IE_NAME: Incomplete

class MindsGroupIE(MindsFeedBaseIE):
    IE_NAME: Incomplete
