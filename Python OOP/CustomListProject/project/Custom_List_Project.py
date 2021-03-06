from project.Errors import CustomListIndexException, CustomListTypeException, CustomListSumException
from collections.abc import Iterable
import sys


class CustomList:
    def __init__(self, *args):
        self.elements = list(args)

    def __verify_index(self, index, shouldIncludePlusOne=False):
        try:
            if shouldIncludePlusOne:
                if not self.elements:
                    return
                elif index > 0:
                    self.elements[index - 1]
                else:
                    self.elements[index]
            else:
                self.elements[index]
        except IndexError as ex:
            raise CustomListIndexException(
                f'MyCustomList does not found element on this index - {index}\nThe original exception was - {ex}')
        except TypeError as ex:
            raise CustomListTypeException(
                f'Index argument does not match the supported type. Should be integer, got {type(index)} instead.')

    def append(self, element):
        self.elements = self.elements + [element]
        return self.elements

    def remove(self, index):
        self.__verify_index(index)
        value = self.elements[index]
        del self.elements[index]
        return value

    def get(self, index):
        self.__verify_index(index)
        value = self.elements[index]
        return value

    def extend(self, iterable):
        if not isinstance(iterable, Iterable):
            raise CustomListTypeException(f'The argument should be iterable. Got {type(iterable)} instead')
        self.elements = self.elements + list(iterable)
        return self.elements

    def insert(self, index, element):
        self.__verify_index(index, shouldIncludePlusOne=True)
        self.elements = self.elements[0:index] + [element] + self.elements[index:]
        return self.elements

    def pop(self):
        try:
            value = self.elements[-1]
            del self.elements[-1]
            return value
        except IndexError as ex:
            raise CustomListIndexException(
                f'MyCustomList does not found elements in the list\nThe original exception was - {ex}')

    def clear(self):
        self.elements = []

    def index(self, value):
        for index in range(len(self.elements)):
            if self.elements[index] == value:
                return index
        return -1

    def count(self, value):
        counter = 0
        for element in self.elements:
            if element == value:
                counter += 1
        return counter

    def reverse(self):
        return self.elements[::-1]

    def copy(self):
        copy = [el for el in self.elements]
        return CustomList(*copy)

    def size(self):
        return len(self.elements)

    def add_first(self, element):
        self.elements = [element] + self.elements

    def dictionize(self):
        custom_dict = {}
        for index in range(0, len(self.elements), 2):
            try:
                custom_dict[self.elements[index]] = self.elements[index + 1]
            except IndexError:
                custom_dict[self.elements[index]] = ' '
        return custom_dict

    def move(self, amount):
        if len(self.elements) == 0:
            return self.elements
        self.elements = self.elements[amount:] + self.elements[:amount]
        return self.elements

    def sum(self):
        result = 0
        for element in self.elements:
            if isinstance(element, int) or isinstance(element, float):
                result += element
            elif hasattr(element, '__len__'):
                result += len(element)
            else:
                raise CustomListSumException(
                    f'Please provide a len method to custom objects if you want to sum the elements.')
        return result

    def overbound(self):
        max_num = -sys.maxsize
        element = None
        for el in self.elements:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el

            if max_num < num:
                max_num = num
                element = el
        return self.elements.index(element)

    def underbound(self):
        min_num = sys.maxsize
        element = None
        for el in self.elements:
            if not isinstance(el, int) and not isinstance(el, float):
                num = len(el)
            else:
                num = el

            if min_num > num:
                min_num = num
                element = el
        return self.elements.index(element)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{';'.join([repr(el) for el in self.elements])}"
