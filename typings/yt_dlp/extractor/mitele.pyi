from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601
from .telecinco import TelecincoBaseIE as TelecincoBaseIE

class MiTeleIE(TelecincoBaseIE):
    IE_DESC: str
