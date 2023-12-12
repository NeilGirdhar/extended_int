from __future__ import annotations

from math import inf
from numbers import Integral, Real
from typing import Any, NoReturn

from typing_extensions import override

from .extended_integral import ExtendedIntegral

__all__ = ['IntegerInfinity', 'int_inf']


class IntegerInfinity(ExtendedIntegral):  # noqa: PLR0904
    def __init__(self, *, negative: bool = False):
        super().__init__()
        self.negative = negative

    @staticmethod
    def _from_float(x: float) -> IntegerInfinity:
        if x == inf:
            return IntegerInfinity()
        if x == -inf:
            return IntegerInfinity(negative=True)
        raise UndefinedIntegerInfinityError

    # Display operators.
    @override
    def __repr__(self) -> str:
        return repr(float(self))

    @override
    def __str__(self) -> str:
        return str(float(self))

    @override
    def __format__(self, format_spec: str) -> str:
        return float(self).__format__(format_spec)

    # Comparison operators.
    @override
    def __lt__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            return self.negative and not other.negative
        if isinstance(other, Real):
            return self.negative and other != -inf
        return NotImplemented

    @override
    def __le__(self, other: Any) -> Any:
        return self < other or self == other

    @override
    def __eq__(self, other: object) -> Any:
        if isinstance(other, IntegerInfinity):
            return self.negative == other.negative
        if isinstance(other, Real):
            return other == (-inf if self.negative else inf)
        return NotImplemented

    @override
    def __ne__(self, other: object) -> Any:
        return not self == other

    def __gt__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            return not self.negative and other.negative
        if isinstance(other, Real):
            return not self.negative and other != inf
        return NotImplemented

    def __ge__(self, other: Any) -> Any:
        return self > other or self == other

    # Conversion operators.
    @override
    def __hash__(self) -> int:
        return hash(float(self))

    @override
    def __bool__(self) -> bool:
        return True

    @override
    def __complex__(self) -> float:
        return float(self)

    @override
    def __float__(self) -> float:
        return -inf if self.negative else inf

    def __index__(self) -> NoReturn:
        raise UndefinedIntegerInfinityError

    # Binary operators.
    @override
    def __add__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            if self.negative == other.negative:
                return self
            raise UndefinedIntegerInfinityError
        if isinstance(other, Integral):
            return self
        if isinstance(other, Real):
            return float(self) + other
        return NotImplemented

    @override
    def __sub__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            if self.negative != other.negative:
                return self
            raise UndefinedIntegerInfinityError
        if isinstance(other, Integral):
            return self
        if isinstance(other, Real):
            return float(self) + other
        return NotImplemented

    @override
    def __mul__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            if self.negative == other.negative:
                return IntegerInfinity()
            return IntegerInfinity(negative=True)
        if isinstance(other, Integral):
            return self
        if isinstance(other, Real):
            return float(self) * other
        return NotImplemented

    def __matmul__(self, other: Any) -> Any:
        return NotImplemented

    @override
    def __truediv__(self, other: Any) -> NoReturn:
        raise UndefinedIntegerInfinityError

    @override
    def __floordiv__(self, other: Any) -> NoReturn:
        raise UndefinedIntegerInfinityError

    @override
    def __mod__(self, other: Any) -> NoReturn:
        raise UndefinedIntegerInfinityError

    @override
    def __divmod__(self, other: Any) -> NoReturn:
        raise UndefinedIntegerInfinityError

    @override
    def __pow__(self, other: Any, modulo: None | int = None) -> ExtendedIntegral:
        if modulo is not None:
            raise UndefinedIntegerInfinityError
        if other < 0:
            return 0  # type: ignore # pyright: ignore
        return self

    def __and__(self, other: Any) -> Any:
        return NotImplemented

    def __xor__(self, other: Any) -> Any:
        return NotImplemented

    def __or__(self, other: Any) -> Any:
        return NotImplemented

    @override
    def __radd__(self, other: Any) -> Any:
        return self + other

    @override
    def __rsub__(self, other: Any) -> Any:
        return -self + other

    @override
    def __rmul__(self, other: Any) -> Any:
        return self * other

    def __rmatmul__(self, other: Any) -> Any:
        return NotImplemented

    @override
    def __rtruediv__(self, other: Any) -> Any:
        raise UndefinedIntegerInfinityError

    @override
    def __rfloordiv__(self, other: Any) -> Any:
        raise UndefinedIntegerInfinityError

    @override
    def __rmod__(self, other: Any) -> Any:
        raise UndefinedIntegerInfinityError

    @override
    def __rdivmod__(self, other: Any) -> Any:
        raise UndefinedIntegerInfinityError

    @override
    def __rpow__(self, other: Any) -> Any:
        if isinstance(other, Integral | IntegerInfinity):
            if self.negative:
                if other == 0:
                    raise UndefinedIntegerInfinityError
                return 0
            if other < 0:
                return IntegerInfinity(negative=True)
            if other > 0:  # type: ignore # pyright: ignore
                return IntegerInfinity()
            return 0
        if isinstance(other, Real):
            return other ** float(self)
        return NotImplemented

    # Unary operators.
    @override
    def __neg__(self) -> IntegerInfinity:
        return IntegerInfinity(negative=not self.negative)

    @override
    def __pos__(self) -> IntegerInfinity:
        return self

    @override
    def __abs__(self) -> IntegerInfinity:
        return IntegerInfinity()

    def __invert__(self) -> IntegerInfinity:
        return -self

    # Rounding.
    @override
    def __round__(self, ndigits: None | int = None) -> NoReturn:
        raise UndefinedIntegerInfinityError

    @override
    def __trunc__(self) -> NoReturn:
        raise UndefinedIntegerInfinityError

    @override
    def __floor__(self) -> NoReturn:
        raise UndefinedIntegerInfinityError

    @override
    def __ceil__(self) -> NoReturn:
        raise UndefinedIntegerInfinityError

    def __int__(self) -> NoReturn:
        raise OverflowError

    def __lshift__(self, other: Any) -> Any:
        return NotImplemented

    def __rshift__(self, other: Any) -> Any:
        return NotImplemented

    def __rlshift__(self, other: Any) -> Any:
        return NotImplemented

    def __rrshift__(self, other: Any) -> Any:
        return NotImplemented

    def __rand__(self, other: Any) -> Any:
        return NotImplemented

    def __rxor__(self, other: Any) -> Any:
        return NotImplemented

    def __ror__(self, other: Any) -> Any:
        return NotImplemented


int_inf = IntegerInfinity()


class UndefinedIntegerInfinityError(Exception):
    pass
