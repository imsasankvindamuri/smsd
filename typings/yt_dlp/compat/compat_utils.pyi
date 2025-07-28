import types
from _typeshed import Incomplete
from typing import NamedTuple

class _Package(NamedTuple):
    name: Incomplete
    version: Incomplete

def get_package_info(module): ...

class EnhancedModule(types.ModuleType):
    def __bool__(self) -> bool: ...
    def __getattribute__(self, attr): ...

def passthrough_module(parent, child, allowed_attributes=..., *, callback=...): ...
