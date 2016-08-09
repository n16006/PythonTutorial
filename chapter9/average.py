def average(values):
    """calculate average from numric list"""


    >>> print(average([20, 30, 70]))


    return sum(values) / len(values)

import doctest
doctest.testmod()