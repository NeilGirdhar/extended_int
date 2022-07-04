from __future__ import annotations

from math import inf
from numbers import Integral, Real
from typing import Any, NoReturn

from .extended_integral import ExtendedIntegral

__all__ = ['IntegerInfinity', 'int_inf']


class IntegerInfinity(ExtendedIntegral):
    def __init__(self, negative: bool = False):
        self.negative = negative

    @staticmethod
    def _from_float(x: float) -> IntegerInfinity:
        if x == inf:
            return IntegerInfinity()
        if x == -inf:
            return IntegerInfinity(True)
        raise UndefinedIntegerInfinityError()

    # Display operators.
    def __repr__(self) -> str:
        return repr(float(self))

    def __str__(self) -> str:
        return str(float(self))

    def __format__(self, format_spec: str) -> str:
        return float(self).__format__(format_spec)

    # Comparison operators.
    def __lt__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            return self.negative and not other.negative
        if isinstance(other, Real):
            if self.negative:
                return other != -inf
            return False
        return NotImplemented

    def __le__(self, other: Any) -> Any:
        return self < other or self == other

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            return self.negative == other.negative
        if isinstance(other, Real):
            if self.negative:
                return other == -inf
            return other == inf
        return NotImplemented

    def __ne__(self, other: Any) -> Any:
        return not self == other

    def __gt__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            return not self.negative and other.negative
        if isinstance(other, Real):
            if self.negative:
                return False
            return other != inf
        return NotImplemented

    def __ge__(self, other: Any) -> Any:
        return self > other or self == other

    # Conversion operators.
    def __hash__(self) -> int:
        return hash(float(self))

    def __bool__(self) -> bool:
        return True

    def __complex__(self) -> float:
        return float(self)

    def __int__(self) -> NoReturn:
        raise OverflowError()

    def __float__(self) -> float:
        if self.negative:
            return -inf
        return inf

    def __index__(self) -> NoReturn:
        raise UndefinedIntegerInfinityError()

    # Binary operators.
    def __add__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            if self.negative == other.negative:
                return self
            raise UndefinedIntegerInfinityError()
        if isinstance(other, Integral):
            return self
        if isinstance(other, Real):
            return float(self) + other
        return NotImplemented

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            if self.negative != other.negative:
                return self
            raise UndefinedIntegerInfinityError()
        if isinstance(other, Integral):
            return self
        if isinstance(other, Real):
            return float(self) + other
        return NotImplemented

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, IntegerInfinity):
            if self.negative == other.negative:
                return IntegerInfinity()
            return IntegerInfinity(True)
        if isinstance(other, Integral):
            return self
        if isinstance(other, Real):
            return float(self) * other
        return NotImplemented

    def __matmul__(self, other: Any) -> Any:
        return NotImplemented

    def __truediv__(self, other: Any) -> NoReturn:
        raise UndefinedIntegerInfinityError()

    def __floordiv__(self, other: Any) -> NoReturn:
        raise UndefinedIntegerInfinityError()

    def __mod__(self, other: Any) -> NoReturn:
        raise UndefinedIntegerInfinityError()

    def __divmod__(self, other: Any) -> NoReturn:
        raise UndefinedIntegerInfinityError()

    def __pow__(self, other: Any, modulo: None | int = None) -> ExtendedIntegral:
        if modulo is not None:
            raise UndefinedIntegerInfinityError()
        if other < 0:
            return 0  # type: ignore
        return self

    def __lshift__(self, other: Any) -> Any:
        return NotImplemented

    def __rshift__(self, other: Any) -> Any:
        return NotImplemented

    def __and__(self, other: Any) -> Any:
        return NotImplemented

    def __xor__(self, other: Any) -> Any:
        return NotImplemented

    def __or__(self, other: Any) -> Any:
        return NotImplemented

    def __radd__(self, other: Any) -> Any:
        return self + other

    def __rsub__(self, other: Any) -> Any:
        return -self + other

    def __rmul__(self, other: Any) -> Any:
        return self * other

    def __rmatmul__(self, other: Any) -> Any:
        return NotImplemented

    def __rtruediv__(self, other: Any) -> Any:
        raise UndefinedIntegerInfinityError()

    def __rfloordiv__(self, other: Any) -> Any:
        raise UndefinedIntegerInfinityError()

    def __rmod__(self, other: Any) -> Any:
        raise UndefinedIntegerInfinityError()

    def __rdivmod__(self, other: Any) -> Any:
        raise UndefinedIntegerInfinityError()

    def __rpow__(self, other: Any) -> Any:
        if isinstance(other, (Integral, IntegerInfinity)):
            if self.negative:
                if other == 0:
                    raise UndefinedIntegerInfinityError()
                return 0
            if other < 0:
                return IntegerInfinity(True)
            if other > 0:  # type: ignore
                return IntegerInfinity()
            return 0
        if isinstance(other, Real):
            return other ** float(self)
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

    # Unary operators.
    def __neg__(self) -> IntegerInfinity:
        return IntegerInfinity(not self.negative)

    def __pos__(self) -> IntegerInfinity:
        return self

    def __abs__(self) -> IntegerInfinity:
        return IntegerInfinity()

    def __invert__(self) -> IntegerInfinity:
        return -self

    # Rounding.
    def __round__(self, ndigits: None | int = None) -> NoReturn:
        raise UndefinedIntegerInfinityError()

    def __trunc__(self) -> NoReturn:
        raise UndefinedIntegerInfinityError()

    def __floor__(self) -> NoReturn:
        raise UndefinedIntegerInfinityError()

    def __ceil__(self) -> NoReturn:
        raise UndefinedIntegerInfinityError()


int_inf = IntegerInfinity()


class UndefinedIntegerInfinityError(Exception):
    pass
