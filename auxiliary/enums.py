from __future__ import annotations

from enum import Enum
from functools import cached_property, total_ordering
from typing import TypeVar


@total_ordering
class OrderedEnum(Enum):
    """OrderedEnum is the enum class for all ordered enums.

    They can be compared with others compared by their indices.
    """

    def __lt__(self: _OE_co, other: _OE_co) -> bool:
        if isinstance(other, type(self)):
            return self.index < other.index
        else:
            return NotImplemented

    @cached_property
    def index(self) -> int:
        """Returns the ordinal of this ordered enum element.

        :return: The index of this ordered enum element.
        """
        values = list[OrderedEnum](type(self))

        return values.index(self)


_OE_co = TypeVar('_OE_co', bound=OrderedEnum)
