from ..utils import determine_ext as determine_ext, parse_count as parse_count, remove_end as remove_end, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor
from _typeshed import Incomplete

class NitterIE(InfoExtractor):
    NON_HTTP_INSTANCES: Incomplete
    HTTP_INSTANCES: Incomplete
    DEAD_INSTANCES: Incomplete
    INSTANCES: Incomplete
    current_instance: Incomplete
