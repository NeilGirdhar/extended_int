from numbers import Integral, Real

__all__ = ['ExtendedIntegral']


class ExtendedIntegral(Real):
    pass


ExtendedIntegral.register(Integral)  # type: ignore
