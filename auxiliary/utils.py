from collections import Sequence
from itertools import chain
from numbers import Real
from typing import TypeVar

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
