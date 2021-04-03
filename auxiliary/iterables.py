from collections.abc import Collection, Hashable, Iterable, Iterator, Sequence
from functools import reduce
from itertools import chain
from operator import add, mul
from typing import Any, Optional, cast

from auxiliary.typing import SupportsLessThan, _SA, _SM, _T


def windowed(it: Iterable[_T], width: int, step: int = 1, partial: bool = False) -> Iterator[Iterator[_T]]:
    """Returns the sliding window views of the supplied iterable.

    :param it: The values to generate the window views on.
    :param width: The sliding window width.
    :param step: The step of the window views.
    :param partial: Allow partial view.
    :return: The window views.
    """
    if not isinstance(it, Sequence):
        it = tuple(it)

    for i in range(0, len(it) if partial else len(it) - width + 1, step):
        yield iter(it[i:i + width])


def chunked(it: Iterable[_T], width: int) -> Iterator[Iterator[_T]]:
    """Chunks the iterable by the given width.

    :param it: The iterable to chunk.
    :param width: The width of the chunks.
    :return: The chunks.
    """
    return windowed(it, width, width, True)


def flattened(it: Iterable[Iterable[_T]]) -> Iterator[_T]:
    """Flattens the iterable.

    :param it: The iterable to flatten.
    :return: The flattened iterable.
    """
    return chain(*it)


def trimmed(it: Iterable[_T], percentage: float) -> Iterator[_T]:
    """Trims the iterable by the percentage.

    :param it: The values to trim.
    :param percentage: The trimmed percentage.
    :return: The trimmed sequence.
    """
    if not isinstance(it, Sequence):
        it = tuple(it)

    n = int(len(it) * percentage)

    return iter(it[n:len(it) - n])


def rotated(it: Iterable[_T], index: int) -> Iterator[_T]:
    """Rotates the iterable by the given index.

    :param it: The values to rotate.
    :param index: The index of rotation.
    :return: The rotated iterator.
    """
    return chain(it[index:], it[:index]) if isinstance(it, Sequence) else rotated(tuple(it), index)


def after(it: Iterable[_T], v: _T, loop: bool = False) -> _T:
    """Gets the next the value inside the iterable.

    :param it: The iterator to get from.
    :param v: The previous value.
    :param loop: True to allow loop-around, else False.
    :raises ValueError: If the value is the last element in the iterable and the looping is disabled.
    :return: The next value.
    """
    if not isinstance(it, Sequence):
        it = tuple(it)

    try:
        i = (it.index(v) + 1)

        if loop:
            i %= len(it)

        return cast(_T, it[i])
    except IndexError:
        raise ValueError('The value is the last element in the iterable.')


def iter_equal(it1: Iterable[Any], it2: Iterable[Any]) -> bool:
    """Checks if all elements in both iterables are equal to the elements in the other iterable at the same position.

    :param it1: The first iterable.
    :param it2: The second iterable.
    :return: True if the equality check passes, else False.
    """
    if not isinstance(it1, Collection):
        it1 = tuple(it1)

    if not isinstance(it2, Collection):
        it2 = tuple(it2)

    return len(it1) == len(it2) and all(x == y for x, y in zip(it1, it2))


def const(it: Iterable[Any]) -> bool:
    """Checks if all elements inside the iterable are equal to each other.

       If the iterable is empty, True is returned.

    :param it: The iterable.
    :return: True if all elements are equal, else False.
    """
    it = iter(it)

    try:
        x = next(it)
    except StopIteration:
        return True
    else:
        return all(x == y for y in it)


def unique(it: Iterable[Any]) -> bool:
    """Checks if all elements inside the iterable are unique to each other.

       If the iterable is empty, True is returned.

    :param it: The iterable.
    :return: True if all elements are unique, else False.
    """
    if not isinstance(it, Sequence):
        it = tuple(it)

    if not it:
        return True
    elif all(isinstance(x, Hashable) for x in it):
        return len(it) == len(set(it))
    elif all(isinstance(x, SupportsLessThan) for x in it):
        return all(x != y for x, y in windowed(sorted(it), 2))
    else:
        return all(all(it[i] != it[j] for j in range(len(it)) if i != j) for i in range(len(it)))


def sum_(values: Iterable[_SA], start: Optional[_SA] = None) -> _SA:
    """Calculates the sum of the elements in the iterable.

    :param values: The values to be summed.
    :param start: The optional start value.
    :raises ValueError: If the iterable is empty and the start value is not supplied.
    :return: The sum of the values.
    """
    try:
        return reduce(add, values if start is None else chain((start,), values))
    except TypeError:
        raise ValueError('The iterable is empty and the start value is not supplied')


def product(values: Iterable[_SM], start: Optional[_SM] = None) -> _SM:
    """Calculates the product of the elements in the iterable.

    :param values: The values to be multiplied.
    :param start: The optional start value.
    :raises ValueError: If the iterable is empty and the start value is not supplied.
    :return: The product of the values.
    """
    try:
        return reduce(mul, values if start is None else chain((start,), values))
    except TypeError:
        raise ValueError('The iterable is empty and the start value is not supplied')
