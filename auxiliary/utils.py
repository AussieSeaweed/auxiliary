from collections import Sequence
from functools import reduce
from itertools import chain
from operator import add, lt, mul
from typing import Iterable, TypeVar

T = TypeVar('T')


def trim(it: Iterable[T], percentage: float) -> Sequence[T]:
    """Trims the iterable by the percentage.

    :param it: the iterable to be trimmed
    :param percentage: the percentage to trim
    :return: the trimmed sequence
    """
    if isinstance(it, Sequence):
        n = int(len(it) * percentage)

        return it[n:len(it) - n]
    else:
        return trim(tuple(it), percentage)


def window(it: Iterable[T], n: int) -> Iterable[Sequence[T]]:
    """Returns the sliding window views of the supplied iterable

    :param it: the iterable to be operated on
    :param n: the width of the sliding window
    :return: the window views
    """
    if isinstance(it, Sequence):
        return (it[i:i + n] for i in range(len(it) - n + 1))
    else:
        return window(tuple(it), n)


def rotate(it: Iterable[T], i: int) -> Iterable[T]:
    """Rotates the iterable by the given index.

    :param it: the iterable to rotate
    :param i: the index of rotation
    :return: the rotated iterable
    """
    if isinstance(it, Sequence):
        return chain(it[i:], it[:i])
    else:
        return rotate(tuple(it), i)


def constant(it: Iterable[T]) -> bool:
    """Checks if all elements inside the iterable are equal to each other.

    If the iterable is empty, True is returned.

    :param it: the iterable
    :return: True if all elements are equal, else False
    """
    if isinstance(it, Sequence):
        return not it or all(x == it[0] for x in it)
    else:
        return constant(tuple(it))


def iter_equal(it1: Iterable[T], it2: Iterable[T]) -> bool:
    """Checks if all elements in both iterables are equal to the elements in the other iterable at the same position.

    :param it1: the first iterable
    :param it2: the second iterable
    :return: True if the equality check passes, else False
    """
    if isinstance(it1, Sequence) and isinstance(it2, Sequence):
        return len(it1) == len(it2) and all(x == y for x, y in zip(it1, it2))
    else:
        return iter_equal(tuple(it1), tuple(it2))


def sum_(it: Iterable[T]) -> T:
    """Calculates the sum of the elements in the iterable.

    :param it: the iterable
    :return: the sum of the elements
    """
    try:
        return reduce(add, it)
    except TypeError:
        raise ValueError('Invalid iterable')


def product(it: Iterable[T]) -> T:
    """Calculates the product of the elements in the iterable.

    :param it: the iterable
    :return: the product of the elements
    """
    try:
        return reduce(mul, it)
    except TypeError:
        raise ValueError('Invalid iterable')


def limit(v: T, lower: T, upper: T) -> T:
    """Binds the value by the given interval.

    :param v: the value to bind
    :param lower: the lower limit
    :param upper: the upper limit
    :return: the bound value
    """
    if not (lt(lower, upper) or lower == upper):
        raise ValueError('Lower bound is greater than the upper bound')

    if lt(v, lower):
        return lower
    elif lt(upper, v):
        return upper
    else:
        return v
