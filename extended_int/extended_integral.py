from numbers import Real, Integral

__all__ = ['ExtendedIntegral']


class ExtendedIntegral(Real):
    pass


ExtendedIntegral.register(Integral)
