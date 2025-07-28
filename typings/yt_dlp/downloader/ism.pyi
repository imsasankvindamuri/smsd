from ..networking.exceptions import HTTPError as HTTPError
from ..utils import RetryManager as RetryManager
from .fragment import FragmentFD as FragmentFD
from _typeshed import Incomplete

u8: Incomplete
u88: Incomplete
u16: Incomplete
u1616: Incomplete
u32: Incomplete
u64: Incomplete
s88: Incomplete
s16: Incomplete
s1616: Incomplete
s32: Incomplete
unity_matrix: Incomplete
TRACK_ENABLED: int
TRACK_IN_MOVIE: int
TRACK_IN_PREVIEW: int
SELF_CONTAINED: int

def box(box_type, payload): ...
def full_box(box_type, version, flags, payload): ...
def write_piff_header(stream, params) -> None: ...
def extract_box_data(data, box_sequence): ...

class IsmFD(FragmentFD):
    def real_download(self, filename, info_dict): ...
