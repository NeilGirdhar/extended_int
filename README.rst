##########################################
extended_int: Extended Integers for Python
##########################################

.. image:: https://badge.fury.io/py/extended_int.svg
    :target: https://badge.fury.io/py/extended_int

Example
=======

.. code-block:: python

    In [1]: from numbers import Real, Integral

    In [2]: from extended_int import ExtendedIntegral, int_inf

    In [3]: float(int_inf)
    Out[3]: inf

    In [4]: print(int_inf)
    inf

    In [5]: int(int_inf)
    ---------------------------------------------------------------------------
    OverflowError                             Traceback (most recent call last)

    In [6]: isinstance(int_inf, Real)
    Out[6]: True

    In [7]: isinstance(int_inf, Integral)
    Out[7]: False


    In [8]: isinstance(2.5, ExtendedIntegral)

    Out[8]: False

    In [9]: isinstance(int_inf, ExtendedIntegral)

    Out[9]: True

    In [10]: isinstance(2, ExtendedIntegral)

    Out[10]: True
