"""
Given two complex numbers 'C' and 'D'. Perform the following operations with C and D
C+D
C-D
C*D
C/D
mod(C)
mod(D)

Input will be real and imaginary parts of the complex numbers
Display the output in separate lines
"""

import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # __ before and after a builtin function does overwriting.
    # In the case of following functions, argument 'self' denoted 1st complex num and argument 'no' denotes 2nd complex num
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        # Multiplication = (a*c - b*d) + (a*d + b*c)i
        return Complex(
            self.real * no.real - self.imaginary * no.imaginary,
            self.real * no.imaginary + self.imaginary * no.real,
        )

    def __truediv__(self, no):
        # Division = (a*c + b*d)/(c**2 + d**2) + [(c*b - a*d)/(c**2 + d**2)]i
        return Complex(
            (self.real * no.real + self.imaginary * no.imaginary)
            / (no.real**2 + no.imaginary**2),
            (no.real * self.imaginary - self.real * no.imaginary)
            / (no.real**2 + no.imaginary**2),
        )

    def mod(self):
        return Complex((math.sqrt(self.real**2 + self.imaginary**2)), 0)

    # str() is the convert_to_string function
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (
                self.real
            )  # rounds self.real to 2 decimal places and puts it in the place of %f (formatting)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == "__main__":
    C = map(float, input().split())
    D = map(float, input().split())
    X = Complex(
        *C
    )  # c is a list. Instead of passing the whole list, the address of 0th element is passed as pointer
    Y = Complex(*D)
    print(
        *map(str, [X + Y, X - Y, X * Y, X / Y, X.mod(), Y.mod()]), sep="\n"
    )  # *map denotes that it is used as pointer
