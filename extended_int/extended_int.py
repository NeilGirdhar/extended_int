from numbers import Real, Integral
from math import inf, isnan
from .extended_integral import Infinite

__all__ = ['IntegerInfinity']


class IntegerInfinity(Infinite):

    def __init__(self, negative=False):
        self.negative = negative

    @staticmethod
    def _from_float(x):
        if x == inf:
            return IntegerInfinity()
        if x == -inf:
            return IntegerInfinity(True)
        raise UndefinedIntegerInfinityError()

    # Display operators.
    def __repr__(self):
        return repr(float(self))

    def __str__(self):
        return str(float(self))

    def __format__(self, format_spec):
        return float(self).__format(format_spec)

    # Comparison operators.
    def __lt__(self, other):
        if isinstance(other, IntegerInfinity):
            return self.negative and not other.negative
        if isinstance(other, Real):
            if self.negative:
                return other != -inf
            return False
        return NotImplemented

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        if isinstance(other, IntegerInfinity):
            return self.negative == other.negative
        if isinstance(other, Real):
            if self.negative:
                return other == -inf
            return other == inf
        return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        if isinstance(other, IntegerInfinity):
            return not self.negative and other.negative
        if isinstance(other, Real):
            if self.negative:
                return False
            return other != inf
        return NotImplemented

    def __ge__(self, other):
        return self > other or self == other

    # Conversion operators.
    def __hash__(self):
        return hash(float(self))

    def __bool__(self):
        return True

    def __complex__(self):
        return float(self)

    def __int__(self):
        raise UndefinedIntegerInfinityError()

    def __float__(self):
        if self.negative:
            return -inf
        return inf

    def __index__(self):
        raise UndefinedIntegerInfinityError()

    # Binary operators.
    def __add__(self, other):
        if isinstance(other, IntegerInfinity):
            if self.negative == other.negative:
                return self
            raise UndefinedIntegerInfinityError()
        if isinstance(other, Integral):
            return self
        if isinstance(other, Real):
            return float(self) + other
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, IntegerInfinity):
            if self.negative == -other.negative:
                return self
            raise UndefinedIntegerInfinityError()
        if isinstance(other, Integral):
            return self
        if isinstance(other, Real):
            return float(self) + other
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, IntegerInfinity):
            if self.negative == other.negative:
                return IntegerInfinity()
            return IntegerInfinity(True)
        if isinstance(other, Integral):
            return self
        if isinstance(other, Real):
            return float(self) * other
        return NotImplemented

    def __matmul__(self, other):
        return NotImplemented

    def __truediv__(self, other):
        raise UndefinedIntegerInfinityError()

    def __floordiv__(self, other):
        raise UndefinedIntegerInfinityError()

    def __mod__(self, other):
        raise UndefinedIntegerInfinityError()

    def __divmod__(self, other):
        raise UndefinedIntegerInfinityError()

    def __pow__(self, other, modulo=None):
        if modulo is not None:
            raise UndefinedIntegerInfinityError()
        if other < 0:
            return 0
        return self

    def __lshift__(self, other):
        return NotImplemented

    def __rshift__(self, other):
        return NotImplemented

    def __and__(self, other):
        return NotImplemented

    def __xor__(self, other):
        return NotImplemented

    def __or__(self, other):
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return -self + other

    def __rmul__(self, other):
        return self * other

    def __rmatmul__(self, other):
        return NotImplemented

    def __rtruediv__(self, other):
        raise UndefinedIntegerInfinityError()

    def __rfloordiv__(self, other):
        raise UndefinedIntegerInfinityError()

    def __rmod__(self, other):
        raise UndefinedIntegerInfinityError()

    def __rdivmod__(self, other):
        raise UndefinedIntegerInfinityError()

    def __rpow__(self, other):
        if isinstance(other, (Integral, IntegerInfinity)):
            if self.negative:
                if other == 0:
                    raise UndefinedIntegerInfinityError()
                return 0
            if other < 0:
                return IntegerInfinity(True)
            if other > 0:
                return IntegerInfinity()
            return 0
        if isinstance(other, Real):
            return other ** float(self)
        return NotImplemented

    def __rlshift__(self, other):
        return NotImplemented

    def __rrshift__(self, other):
        return NotImplemented

    def __rand__(self, other):
        return NotImplemented

    def __rxor__(self, other):
        return NotImplemented

    def __ror__(self, other):
        return NotImplemented

    # Unary operators.
    def __neg__(self):
        return IntegerInfinity(not self.negative)

    def __pos__(self):
        return self

    def __abs__(self):
        return IntegerInfinity()

    def __invert__(self):
        return -self

    # Rounding.
    def __round__(self):
        raise UndefinedIntegerInfinityError()

    def __trunc__(self):
        raise UndefinedIntegerInfinityError()

    def __floor__(self):
        raise UndefinedIntegerInfinityError()

    def __ceil__(self):
        raise UndefinedIntegerInfinityError()


class UndefinedIntegerInfinityError(Exception):
    pass
