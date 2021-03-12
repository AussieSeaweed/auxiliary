from collections.abc import Iterable, Iterator, Sequence, Sized
from functools import reduce
from itertools import chain, islice as _islice
from operator import mul
from typing import Any, Optional, cast

from auxiliary.typing import _F, _SLT, _T


def const_len(func: _F) -> _F:
    """Decorates a function to make sure all sized arguments are of the same length.

    :param func: The function to decorate.
    :return: The decorated function.
    """

    def checked_func(*args: Any, **kwargs: Any) -> Any:
        if const(len(arg) for arg in chain(args, kwargs.values()) if isinstance(arg, Sized)):
            return func(*args, **kwargs)
        else:
            raise ValueError('Sized arguments are not of constant length')

    return cast(_F, checked_func)


def retain_iter(func: _F) -> _F:
    """Decorates a function to make sure all iterators are converted to sequences to persist after iterations.

    :param func: The function to decorate.
    :return: The decorated function.
    """

    def retained_func(*args: Any, **kwargs: Any) -> Any:
        return func(*(
            tuple(arg) if isinstance(arg, Iterator) else arg for arg in args
        ), **{
            key: tuple(value) if isinstance(value, Iterator) else value for key, value in kwargs.items()
        })

    return cast(_F, retained_func)


def ilen(it: Iterable[Any]) -> int:
    """Sizes the given iterator.

    :param it: The iterator to size.
    :return: The length of the iterator.
    """
    return len(it) if isinstance(it, Sized) else len(tuple(it))


def islice(it: Iterable[_T], *args: Optional[int]) -> Iterator[_T]:
    """Slices the given iterator.

    :param it: The iterable to slice.
    :param args: Stop or start, stop[, step].
    :return: The sliced iterator.
    """
    return iter(it[slice(*args)]) if isinstance(it, Sequence) else _islice(it, *args)


def iindex(it: Iterable[_T], index: int) -> _T:
    """Indexes the given iterator.

    :param it: The iterator to index.
    :param index: The index.
    :return: The element at the given index.
    """
    try:
        return cast(_T, it[index]) if isinstance(it, Sequence) else next(x for i, x in enumerate(it) if i == index)
    except StopIteration:
        raise IndexError('Index out of bound')


@retain_iter
def chunked(it: Iterable[_T], width: int) -> Iterator[Iterator[_T]]:
    """Chunks the iterable by the given width.

    :param it: The iterable to chunk.
    :param width: The width of the chunks.
    :return: The chunks.
    """
    return (islice(it, i, i + width) for i in range(0, ilen(it), width))


@retain_iter
def windowed(it: Iterable[_T], width: int) -> Iterator[Iterator[_T]]:
    """Returns the sliding window views of the supplied iterable.

    :param it: The values to generate the window views on.
    :param width: The sliding window width.
    :return: The window views.
    """
    return (islice(it, i, i + width) for i in range(ilen(it) - width + 1))


@retain_iter
def trimmed(it: Iterable[_T], percentage: float) -> Iterator[_T]:
    """Trims the iterable by the percentage.

    :param it: The values to trim.
    :param percentage: The trimmed percentage.
    :return: The trimmed sequence.
    """
    n = int(ilen(it) * percentage)

    return islice(it, n, ilen(it) - n)


@retain_iter
def rotated(it: Iterable[_T], index: int) -> Iterator[_T]:
    """Rotates the iterable by the given index.

    :param it: The values to rotate.
    :param index: The index of rotation.
    :return: The rotated iterator.
    """
    return chain(islice(it, index % ilen(it), None), islice(it, index % ilen(it)))


@retain_iter
def after(it: Iterable[_T], v: _T, loop: bool = False) -> _T:
    """Gets the next the value inside the iterable.

    :param it: The iterator to get from.
    :param v: The previous value.
    :param loop: True to loop around, else False. Defaults to False.
    :return: The next value.
    """
    try:
        return iindex(it, tuple(it).index(v) + 1)
    except IndexError:
        if loop:
            return iindex(it, 0)
        else:
            raise ValueError('The value is the last element')


@retain_iter
def iter_equal(it1: Iterable[_T], it2: Iterable[_T]) -> bool:
    """Checks if all elements in both iterables are equal to the elements in the other iterable at the same position.

    :param it1: The first iterable.
    :param it2: The second iterable.
    :return: True if the equality check passes, else False.
    """
    return ilen(it1) == ilen(it2) and all(x == y for x, y in zip(it1, it2))


@retain_iter
def const(it: Iterable[_T]) -> bool:
    """Checks if all elements inside the iterable are equal to each other.

       If the iterable is empty, True is returned.

    :param it: The iterable.
    :return: True if all elements are equal, else False.
    """
    return all(x == iindex(it, 0) for x in it)


def unique(it: Iterable[_T]) -> bool:
    """Checks if all elements inside the iterable are unique to each other.

       If the iterable is empty, True is returned.

    :param it: The iterable.
    :return: True if all elements are unique, else False.
    """
    it = tuple(it)

    return all(all(it[i] != it[j] for j in range(len(it)) if i != j) for i in range(len(it)))


def product(values: Iterable[_T], start: Optional[_T] = None) -> _T:
    """Calculates the product of the elements in the iterable.

    :param values: The values to be multiplied.
    :param start: The optional start value.
    :return: The product of the values.
    """
    try:
        return reduce(mul, values if start is None else chain((start,), values))
    except TypeError:
        raise ValueError('Invalid iterable')


def bind(value: _SLT, lower: _SLT, upper: _SLT) -> _SLT:
    """Binds the value by the given interval.

    :param value: The value to be bound.
    :param lower: The lower limit.
    :param upper: The upper limit.
    :return: The bound value.
    """
    if upper < lower:
        raise ValueError('Lower bound is greater than the upper bound')
    elif value < lower:
        return lower
    elif upper < value:
        return upper
    else:
        return value


def next_or_none(it: Iterator[_T]) -> Optional[_T]:
    """Tries to get the next element of the iterator.

    :param it: The iterator to consume.
    :return: None if there is no next element, else the next element.
    """
    try:
        return next(it)
    except StopIteration:
        return None


def default(optional: Optional[_T], default_: _T) -> _T:
    """Checks if the value is not None and returns it or the default value.

    :param optional: The optional value.
    :param default_: The default value.
    :return: The default value if the value to check is None, else the checked value.
    """
    return default_ if optional is None else optional


def get(optional: Optional[_T]) -> _T:
    """Checks if the optional value is not none and returns it.

    :param optional: The optional value.
    :return: The checked value.
    """
    if optional is None:
        raise ValueError('The checked value is None')
    else:
        return optional
