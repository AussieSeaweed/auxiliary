from __future__ import annotations

from typing import Protocol, TypeVar, runtime_checkable


@runtime_checkable
class SupportsLessThan(Protocol):
    """SupportsLessThan is the protocol for types that support the less than comparison operator."""

    def __lt__(self: _SLT, other: _SLT) -> bool: ...


@runtime_checkable
class SupportsAdd(Protocol):
    """SupportsAdd is the protocol for types that support the __add__ operator."""

    def __add__(self: _SA, other: _SA) -> _SA: ...


@runtime_checkable
class SupportsMul(Protocol):
    """SupportsMul is the protocol for types that support the __mul__ operator."""

    def __mul__(self: _SM, other: _SM) -> _SM: ...


_T = TypeVar('_T')
_SLT = TypeVar('_SLT', bound=SupportsLessThan)
_SA = TypeVar('_SA', bound=SupportsAdd)
_SM = TypeVar('_SM', bound=SupportsMul)
