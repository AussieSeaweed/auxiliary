from collections import Sequence
from functools import reduce
from itertools import chain
from numbers import Real
from operator import add, gt, lt, mul
from typing import Iterable, TypeVar

T = TypeVar('T')


def trim(seq: Sequence[T], percentage: Real) -> Sequence[T]:
    """Trims the sequence by the percentage.

    :param seq: the sequence to be trimmed
    :param percentage: the percentage to trim
    :return: the trimmed sequence
    """
    n = int(len(seq) * percentage)

    return seq[n:len(seq) - n]


def window(seq: Sequence[T], n: int) -> Sequence[Sequence[T]]:
    """Returns the sliding window views of the supplied sequence

    :param seq: the sequence to be operated on
    :param n: the width of the sliding window
    :return: the window views
    """
    return tuple(seq[i:i + n] for i in range(len(seq) - n + 1))


def rotate(seq: Sequence[T], i: int) -> Sequence[T]:
    """Rotates the sequence by the given index.

    :param seq: the sequence to rotate
    :param i: the index of rotation
    :return: the rotated sequence
    """
    return tuple(chain(seq[i:], seq[:i]))


def sum(it: Iterable[T]) -> T:
    """Calculates the sum of the elements in the iterable.

    :param it: the iterable
    :return: the sum of the elements
    """
    return reduce(add, it)


def product(it: Iterable[T]) -> T:
    """Calculates the product of the elements in the iterable.

    :param it: the iterable
    :return: the product of the elements
    """
    return reduce(mul, it)


def limit(v: T, lower: T, upper: T) -> T:
    """Binds the value by the given interval.

    :param v: the value to bind
    :param lower: the lower limit
    :param upper: the upper limit
    :return: the bound value
    """
    if gt(lower, upper):
        raise ValueError('Lower bound is greater than the upper bound')

    if lt(v, lower):
        return lower
    elif lt(upper, v):
        return upper
    else:
        return v
