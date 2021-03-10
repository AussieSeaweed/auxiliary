from collections.abc import Callable
from enum import Enum
from functools import cached_property, total_ordering
from typing import Any, Protocol, TypeVar, runtime_checkable

_T = TypeVar('_T')
_F = TypeVar('_F', bound=Callable[..., Any])


@runtime_checkable
class SupportsLessThan(Protocol):
    """SupportsLessThan is the protocol for types that support less than comparison operators."""

    def __lt__(self, other: Any) -> bool:
        pass


@total_ordering
class OrderedEnum(Enum, SupportsLessThan):
    """OrderedEnum is the enum class for all ordered enums."""

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.index < other.index
        else:
            return NotImplemented

    @cached_property
    def index(self) -> int:
        """
        :return: The index of the enum element.
        """
        values: tuple[OrderedEnum, ...] = tuple(type(self))

        return values.index(self)