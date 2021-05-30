from collections.abc import Iterator
from typing import Optional

from auxiliary.typing import _SLT, _T


def next_or_none(it: Iterator[_T]) -> Optional[_T]:
    """Tries to get the next element of the iterator.

    :param it: The iterator to consume.
    :return: None if there is no next element, else the next element.
    """
    try:
        return next(it)
    except StopIteration:
        return None


def skipped(it: Iterator[_T]) -> Iterator[_T]:
    """Skips the next element of the iterator.

    :param it: The iterator to consume.
    :return: The skipped iterator.
    """
    next(it)

    return it


def bind(value: _SLT, lower: _SLT, upper: _SLT) -> _SLT:
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


def default(optional: Optional[_T], default_value: _T) -> _T:
    """Checks if the value is not None and returns it or the default value.

    :param optional: The optional value.
    :param default_value: The default value.
    :return: The default value if the value to check is None, else the checked value.
    """
    return default_value if optional is None else optional


def get(optional: Optional[_T]) -> _T:
    """Checks if the optional value is not none and returns it.

    :param optional: The optional value.
    :return: The checked value.
    :raises TypeError: If the checked value is None.
    """
    if optional is None:
        raise TypeError('The checked value is None')
    else:
        return optional
