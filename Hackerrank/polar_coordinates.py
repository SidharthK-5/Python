"""
A complex number z is a number is given in the form x + yj.
x is the real part and y is the imaginary part of the complex number.
Find it's polar coordinates.
"""

import cmath


complex_number = complex(input())
print(abs(complex_number))
print(cmath.phase(complex_number))
