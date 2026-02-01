from math import gcd
from functools import total_ordering

@total_ordering
class Fraction:
    def __init__(self, a, b):
        self._validate(b)
        self.a = a
        self.b = b

    def _validate(self, b):
        if b == 0:
            raise ValueError("The denominator cannot be equal to 0")

    def simplify(self):
        return self.a // gcd(self.a, self.b), self.b // gcd(self.a, self.b)

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

    def __sub__(self, other):
        return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)

    def __eq__(self, other):
        return self.simplify() == other.simplify()

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


if __name__ == '__main__':
    f_a = Fraction(2, 3)
    f_b = Fraction(3, 6)

    f_c = f_b + f_a
    print(f_c)

    f_d = f_b * f_a
    print(f_d)

    f_e = f_a - f_b
    print(f_e)

    print(f_d > f_c)
    print(f_d >= f_e)
    print(f_a != f_b)
    f_1 = Fraction(2, 4)
    f_2 = Fraction(3, 6)
    print(f_1 == f_2)
