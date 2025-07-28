import optparse
from .compat import compat_expanduser as compat_expanduser
from .cookies import SUPPORTED_BROWSERS as SUPPORTED_BROWSERS, SUPPORTED_KEYRINGS as SUPPORTED_KEYRINGS
from .downloader.external import list_external_downloaders as list_external_downloaders
from .postprocessor import FFmpegExtractAudioPP as FFmpegExtractAudioPP, FFmpegMergerPP as FFmpegMergerPP, FFmpegSubtitlesConvertorPP as FFmpegSubtitlesConvertorPP, FFmpegThumbnailsConvertorPP as FFmpegThumbnailsConvertorPP, FFmpegVideoRemuxerPP as FFmpegVideoRemuxerPP, SponsorBlockPP as SponsorBlockPP
from .postprocessor.modify_chapters import DEFAULT_SPONSORBLOCK_CHAPTER_TITLE as DEFAULT_SPONSORBLOCK_CHAPTER_TITLE
from .update import UPDATE_SOURCES as UPDATE_SOURCES, detect_variant as detect_variant, is_non_updateable as is_non_updateable
from .utils import Config as Config, OUTTMPL_TYPES as OUTTMPL_TYPES, POSTPROCESS_WHEN as POSTPROCESS_WHEN, deprecation_warning as deprecation_warning, expand_path as expand_path, format_field as format_field, get_executable_path as get_executable_path, get_system_config_dirs as get_system_config_dirs, get_user_config_dirs as get_user_config_dirs, join_nonempty as join_nonempty, orderedSet_from_options as orderedSet_from_options, remove_end as remove_end, variadic as variadic, write_string as write_string
from .version import CHANNEL as CHANNEL, __version__ as __version__
from _typeshed import Incomplete

def parseOpts(overrideArguments=None, ignore_config_files: str = 'if_override'): ...

class _YoutubeDLHelpFormatter(optparse.IndentedHelpFormatter):
    def __init__(self) -> None: ...
    @staticmethod
    def format_option_strings(option): ...

class _YoutubeDLOptionParser(optparse.OptionParser):
    ALIAS_DEST: str
    ALIAS_TRIGGER_LIMIT: int
    def __init__(self) -> None: ...
    values: Incomplete
    def parse_known_args(self, args=None, values=None, strict: bool = True): ...
    def error(self, msg) -> None: ...
    def format_option_help(self, formatter=None): ...

def create_parser(): ...
