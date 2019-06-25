##########################################
extended_int: Extended Integers for Python
##########################################

.. image:: https://badge.fury.io/py/extended_int.svg
    :target: https://badge.fury.io/py/extended_int

Example
=======

.. code-block:: python

    In [0]: from numbers import *

    In [0]: from extended_int import *

    In [0]: i = IntegerInfinity()

    In [4]: float(i)
    Out[4]: inf

    In [5]: print(i)
    inf

    In [6]: i ** i

    Out[6]: inf

    In [7]: i
    Out[7]: inf

    In [9]: isinstance(i, Real)

    Out[9]: True

    In [10]: isinstance(i, Integral)

    Out[10]: False

    In [11]: isinstance(i, Infinite)

    Out[11]: True

    In [12]: isinstance(i, ExtendedIntegral)

    Out[12]: True

    In [13]: isinstance(2, ExtendedIntegral)

    Out[13]: True

    In [14]: isinstance(2, Infinite)

    Out[14]: False
