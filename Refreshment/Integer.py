from math import floor

class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return Integer(floor(value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(value):
            if (i + 1) == len(value) or roman_numerals[c] >= roman_numerals[value[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return Integer(result)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:
                return Integer(int(value))
            except Exception:
                return "wrong type"
        return "wrong type"

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        return self.value + integer.value

