from math import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        self.numerator = numerator
        self.denominator = denominator
        self._normalize()

    def _normalize(self):
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def __le__(self, other):
        return not self.__gt__(other)

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return (self.numerator * other.denominator) > (other.numerator * self.denominator)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
