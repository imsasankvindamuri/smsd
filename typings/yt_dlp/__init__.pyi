from .YoutubeDL import YoutubeDL as YoutubeDL
from .extractor import gen_extractors as gen_extractors, list_extractors as list_extractors
from _typeshed import Incomplete
from typing import NamedTuple

__all__ = ['YoutubeDL', 'gen_extractors', 'list_extractors', 'main', 'parse_options']

class ParsedOptions(NamedTuple):
    parser: Incomplete
    options: Incomplete
    urls: Incomplete
    ydl_opts: Incomplete

def parse_options(argv=None): ...
def main(argv=None) -> None: ...
