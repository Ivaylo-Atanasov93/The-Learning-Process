class Integer:

    def __init__(self, value:int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"
        return Integer(int(value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(value):
            if (i + 1) == len(value) or roman_numerals[c] >= roman_numerals[value[i + 1]]:
                result  += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return Integer(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        return Integer(int(value))

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        return self.value + integer.value

    def __str__(self):
        return f'{self.value}'

# first_num = Integer(10)
# second_num = Integer.from_roman("XVIII")
# print(second_num)
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
# print(first_num.add(second_num))

first_integer = Integer(10)
second_integer = Integer(12)
result = first_integer.add(second_integer)
print(result)

first_integer = Integer(10)
second_integer2 = 12
result2 = first_integer.add(second_integer2)
print(result)