from abc import ABC, abstractmethod
from collections.abc import Hashable, Sequence
from enum import Enum
from functools import reduce, total_ordering
from itertools import chain
from operator import mul


@total_ordering
class IndexedEnum(Enum):
    """IndexedEnum is the enum class for all ordered enums.

    They can be compared with others compared by their indices.
    """

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.index < other.index
        else:
            return NotImplemented

    @property
    def index(self):
        """Returns the index of this indexed enum element.

        :return: The index of this indexed enum element.
        """
        return list(type(self)).index(self)


class SupportsLessThan(ABC):
    """SupportsLessThan is the protocol for types that support the less than comparison operator."""

    @abstractmethod
    def __lt__(self, other): ...


def window(iterable, width, step=1, partial=False):
    """Yields the sliding window views of the supplied iterable.

    :param iterable: The values to generate the window views on.
    :param width: The sliding window width.
    :param step: The step of the window views, defaults to 1.
    :param partial: Allow partial view, defaults to False.
    :return: The window views.
    """
    if not isinstance(iterable, Sequence):
        iterable = tuple(iterable)

    for i in range(0, len(iterable) if partial else len(iterable) - width + 1, step):
        yield iterable[i:i + width]


def chunk(iterable, width):
    """Chunks the iterable by the given width.

    :param iterable: The iterable to chunk.
    :param width: The width of the chunks.
    :return: The chunks.
    """
    return window(iterable, width, width, True)


def flatten(iterable):
    """Flattens the iterable.

    :param iterable: The iterable to flatten.
    :return: The flattened iterable.
    """
    return chain(*iterable)


def rotate(iterable, index):
    """Rotates the iterable by the index.

    :param iterable: The iterable to rotate.
    :param index: The index of rotation.
    :return: The rotated sequence.
    """
    iterable = tuple(iterable)

    return iterable[index:] + iterable[:index]


def distinct(iterable):
    """Checks if all elements inside the iterable are unique to each other.

    If the iterable is empty, True is returned.

    :param iterable: The iterable.
    :return: True if all elements are unique, else False.
    """
    if not isinstance(iterable, Sequence):
        iterable = tuple(iterable)

    if not iterable:
        return True
    elif all(isinstance(x, Hashable) for x in iterable):
        return len(iterable) == len(set(iterable))
    elif all(isinstance(x, SupportsLessThan) for x in iterable):
        return all(x != y for x, y in window(sorted(iterable), 2))
    else:
        return all(
            all(iterable[i] != iterable[j] for j in range(len(iterable)) if i != j) for i in range(len(iterable))
        )


def const(iterable):
    """Checks if all elements inside the iterable are equal to each other.

    If the iterable is empty, True is returned.

    :param iterable: The iterable to check.
    :return: True if all elements are equal, else False.
    """
    iterable = iter(iterable)

    try:
        x = next(iterable)
    except StopIteration:
        return True
    else:
        return all(x == y for y in iterable)


def prod(values):
    """Multiplies the supplied values together and returns the product.

    :param values: The values to multiply.
    :return: The product of the supplied values.
    """
    return reduce(mul, values, 1)


def bind(value, lower, upper):
    """Binds the value by the given interval.

    :param value: The value to be bound.
    :param lower: The lower limit.
    :param upper: The upper limit.
    :return: The bound value.
    :raises ValueError: If the lower bound is greater than the upper bound.
    """
    if upper < lower:
        raise ValueError('Lower bound is greater than the upper bound')
    elif value < lower:
        return lower
    elif upper < value:
        return upper
    else:
        return value


def next_or_none(iterator):
    """Consumes the iterator and returns the yielded value, or None, if the all elements in the iterator is consumed.

    :param iterator: The iterator to optionally consume.
    :return: The consumed value if possible, else None.
    """
    try:
        return next(iterator)
    except StopIteration:
        return None
