from math import gcd

def reduction(function):
    """Creating a decorator to reduce the fraction"""
    def reduce(*args):
        numerator, denominator = function(*args)
        divider = gcd(numerator, denominator)
        return Rational(numerator // divider, denominator // divider)

    return reduce


class Rational:
    """class for performing mathematical operations with fractions, as well as their comparison"""

    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise TypeError("Incorrect input! Variable type must be int!")
        if not denominator:
            raise ZeroDivisionError("Denominator can't be zero!")
        self.__numerator = numerator
        self.__denominator = denominator


    @reduction
    def __add__(self, other):
        """overloading the add operator"""
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        return numerator, denominator

    @reduction
    def __sub__(self, other):
        """overloading the substraction operator"""
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        return numerator, denominator

    @reduction
    def __mul__(self, other):
        """overloading the mulitpy operator"""
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        numerator = self.__numerator * other.__numerator
        denominator = self.__denominator * other.__denominator
        return numerator, denominator

    @reduction
    def __truediv__(self, other):
        """overloading the division operator"""
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        if other.__numerator == 0:
            raise ZeroDivisionError("Division by zero!")
        numerator = self.__numerator * other.__denominator
        denominator = self.__denominator * other.__numerator
        return numerator, denominator

    def __eq__(self, other):
        """overloading comparison a = b"""
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        return self.__numerator * other.__denominator == other.__numerator * self.__denominator

    def __lt__(self, other):
        """overloading comparison a < b"""
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator

    def __le__(self, other):
        """overloading comparison a <= b"""
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        return self.__numerator * other.__denominator <= other.__numerator * self.__denominator

    def __gt__(self, other):
        """overloading comparison a > b"""
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __ge__(self, other):
        """overloading comparison a >= b"""
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        return self.__numerator * other.__denominator >= other.__numerator * self.__denominator

    def __str__(self):
        return f'{self.__numerator}/{self.__denominator} = {round(self.__numerator / self.__denominator, 2)}'


rational = Rational(3, 6)
print(rational)
b = Rational(1, 6)
c = Rational(2, 18)
d = Rational(3, 5)
z = Rational(0, 3)
e = rational + b
p = Rational(4, 6)
print(e)
f = e - c
print(f'{e} - {c} = {f}')
g = f * d
print(f'{f} * {d} = {g}')
h = g / b
print(f'{g} / {b} = {h}')
k = Rational(2, 3)
print(f"k=g? It's {k == g}")
print(f"k=p? It's {k == p}")
print(f"k>d? It's {k>d}")
print(f"k<d? It's {k<d}")
print(f"k<=d? It's {k<=d}")
print(f"k>=d? It's {k>=d}")
j = h / z
print(f'{h} /  {z} = {j}')

