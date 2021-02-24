from collections import Sequence
from functools import reduce
from itertools import chain
from operator import add, gt, lt, mul
from typing import Iterable, TypeVar

T = TypeVar('T')


def trim(seq: Sequence[T], percentage: float) -> Sequence[T]:
    """Trims the sequence by the percentage.

    :param seq: the sequence to be trimmed
    :param percentage: the percentage to trim
    :return: the trimmed sequence
    """
    n = int(len(seq) * percentage)

    return seq[n:len(seq) - n]


def window(seq: Sequence[T], n: int) -> Iterable[Sequence[T]]:
    """Returns the sliding window views of the supplied sequence

    :param seq: the sequence to be operated on
    :param n: the width of the sliding window
    :return: the window views
    """
    return (seq[i:i + n] for i in range(len(seq) - n + 1))


def rotate(seq: Sequence[T], i: int) -> Iterable[T]:
    """Rotates the sequence by the given index.

    :param seq: the sequence to rotate
    :param i: the index of rotation
    :return: the rotated iterable
    """
    return chain(seq[i:], seq[:i])


def seq_equal(seq1: Sequence[T], seq2: Sequence[T]) -> bool:
    """Checks if all elements in both sequences are equal to the elements in the other sequence at the same position.

    :param seq1: the first sequence
    :param seq2: the second sequence
    :return: True if the equality check passes, else False
    """
    return len(seq1) == len(seq2) and all(x == y for x, y in zip(seq1, seq2))


def sum_(it: Iterable[T]) -> T:
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


def constant(it: Iterable[T]) -> bool:
    """Checks if all elements inside the iterable are equal to each other.

    If the iterable is empty, True is returned.

    :param it: the iterable
    :return: True if all elements are equal, else False
    """
    return len(set(it)) <= 1
