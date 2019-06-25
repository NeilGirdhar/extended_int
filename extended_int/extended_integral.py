from numbers import Real, Integral

__all__ = ['ExtendedIntegral', 'Infinite']


class ExtendedIntegral(Real):
    pass


class Infinite(Real):
    pass


ExtendedIntegral.register(Integral)
ExtendedIntegral.register(Infinite)
