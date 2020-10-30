import unittest
from project.Custom_List_Project import CustomList
from project.Errors import CustomListIndexException, CustomListTypeException


class CustomListTestsBase(unittest.TestCase):
    def setup_list(self, *args):
        cl = CustomList()
        [cl.append(el) for el in args]
        return cl

class TestCustomList(CustomListTestsBase):

#Testing the List Append Functionality_______________________________________________________________

    def test_customListAppend_whenEmptyList_shouldReturnListWithTheElement(self):
        cl = self.setup_list()
        value = 5
        result = cl.append(value)
        self.assertEqual([value], result)

    def test_CustomListAppend_whenListHasTwoElements_shouldReturnListWithTheNewElementAtTheEnd(self):
        cl = self.setup_list(1, 2)
        value = 5
        result = cl.append(value)
        self.assertEqual([1, 2, 5], result)

#Testing the List Remove Functionality_______________________________________________________________

    def test_customListRemove_whenIndexInTheMiddle_shouldRemoveElement(self):
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.remove(2)
        expected = 3
        self.assertEqual(expected, result)
        self.assertListEqual([4, 2, 1], cl.reverse())

    def test_customListRemove_whenIndexIsZero_shouldRemoveElement(self):
        value_to_remove = 3
        cl = self.setup_list(value_to_remove, 1, 2, 4)
        result = cl.remove(0)
        expected = value_to_remove
        self.assertEqual(expected, result)
        self.assertListEqual([4, 2, 1], cl.reverse())

    def test_customListRemove_whenIndexIsLenMinus1_shouldRemoveElement(self):
        value_to_remove = 3
        cl = self.setup_list(1, 2, 4, value_to_remove)
        result = cl.remove(3)
        expected = value_to_remove
        self.assertEqual(expected, result)
        self.assertListEqual([4, 2, 1], cl.reverse())

    def test_customListRemove_whenListHasSingleElement_shouldRemoveElement(self):
        value_to_remove = 3
        cl = self.setup_list(value_to_remove)
        result = cl.remove(0)
        expected = value_to_remove
        self.assertEqual(expected, result)
        self.assertListEqual([], cl.reverse())

    def test_customListRemove_whenIndexIsEqualToLen_shouldRaiseException(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.remove(list_len)
        self.assertIsNotNone(context.exception)

    def test_customListRemove_whenIndexIsLessThanLen_shouldRaiseException(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.remove(-list_len - 1)
        self.assertIsNotNone(context.exception)

    def test_customListRemove_whenIndexIsNotInteger_shouldRaiseException(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListTypeException) as context:
            cl.remove('index')
        self.assertIsNotNone(context.exception)

    def test_customListRemove_whenListIsEmpty_shouldRaiseException(self):
        cl = self.setup_list()
        with self.assertRaises(CustomListIndexException) as context:
            cl.remove(0)
        self.assertIsNotNone(context.exception)

#Testing the List Get Functionality_______________________________________________________________

    def test_customListGet_whenIndexInTheMiddle_shouldReturnElement(self):
        value_to_get = 3
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.get(2)
        self.assertEqual(value_to_get, result)

    def test_customListGet_whenIndexIsZero_shouldReturnElement(self):
        value_to_get = 3
        cl = self.setup_list(1, 2, value_to_get, 4,)
        result = cl.get(2)
        expected = value_to_get
        self.assertEqual(expected, result)

    def test_customListGet_whenIndexIsLenMinus1_shouldReturnElement(self):
        value_to_get = 3
        cl = self.setup_list(1, 2, 4, value_to_get)
        result = cl.get(3)
        expected = value_to_get
        self.assertEqual(expected, result)

    def test_customListGet_whenListHasSingleElement_shouldReturnElement(self):
        value_to_get = 3
        cl = self.setup_list(value_to_get)
        result = cl.get(0)
        expected = value_to_get
        self.assertEqual(expected, result)

    def test_customListGet_whenIndexIsEqualToLen_shouldRaiseException(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.get(list_len)
        self.assertIsNotNone(context.exception)

    def test_customListGet_whenIndexIsLessThanLen_shouldRaiseException(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.get(-list_len - 1)
        self.assertIsNotNone(context.exception)

    def test_customListGet_whenIndexIsNotInteger_shouldRaiseException(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListTypeException) as context:
            cl.get('index')
        self.assertIsNotNone(context.exception)

    def test_customListGet_whenListIsEmpty_shouldRaiseException(self):
        cl = self.setup_list()
        with self.assertRaises(CustomListIndexException) as context:
            cl.get(0)
        self.assertIsNotNone(context.exception)

#Testing the List Extend Functionality_______________________________________________________________

    def test_customListExtend_whenEmptyAndExtendWithNotEmpty_shouldExtendIt(self):
        cl = self.setup_list()
        iterable = [1, 2, 3, 4, 5]
        result = cl.extend(iterable)
        self.assertEqual(iterable, result)
        self.assertEqual(iterable[::-1], cl.reverse())

    def test_CustomListExtend_whenNonEmptyAndExtendWithEmpty_shouldExtendIt(self):
        cl = self.setup_list(1, 2, 3, 4, 5)
        iterable = []
        result = cl.extend(iterable)
        self.assertEqual([1, 2, 3, 4, 5], result)
        self.assertEqual([5, 4, 3, 2, 1], cl.reverse())

    def test_customListExtend_whenNotEmptyAndExtendWithNotEmpty_shouldExtendIt(self):
        initial_values = list(range(4))
        cl = self.setup_list(*initial_values)
        other_list = [1]

        result = cl.extend(other_list)
        self.assertEqual(initial_values + [1], result)
        self.assertEqual((initial_values + [1])[::-1], cl.reverse())

    def test_customListExtend_whenNotEmptyAndExtendWithCustomIterable_shouldExtendIt(self):
        class CustomIterable:
            def __init__(self):
                self.is_done = False

            def __iter__(self):
                return self

            def __next__(self):
                if self.is_done:
                    raise StopIteration
                self.is_done = True
                return 1

        initial_values = list(range(4))
        cl = self.setup_list(*initial_values)
        other_list = CustomIterable()

        result = cl.extend(other_list)
        self.assertEqual(initial_values + [1], result)
        self.assertEqual((initial_values + [1])[::-1], cl.reverse())

    def test_customListExtend_whenNonIterable_shouldRaiseException(self):
        cl = self.setup_list()
        with self.assertRaises(CustomListTypeException) as context:
            cl.extend(5)
        self.assertIsNotNone(context.exception)

# Testing the List Extend Functionality_______________________________________________________________

    def test_customListInsert_whenIndexInTheMiddle_shouldInsertItAndReturnTheList(self):
        index_to_insert = 2
        value_to_insert = -3
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.insert(index_to_insert, value_to_insert)

        self.assertEqual([1, 2, value_to_insert, 3, 4], result)
        self.assertEqual([4, 3, value_to_insert, 2, 1], cl.reverse())

    def test_customListInsert_whenIndexIsZero_shouldInsertItAndReturnTheList(self):
        index_to_insert = 0
        value_to_insert = -3
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.insert(index_to_insert, value_to_insert)

        self.assertEqual([value_to_insert, 1, 2, 3, 4], result)
        self.assertEqual([4, 3, 2, 1, value_to_insert,], cl.reverse())

    def test_customListInsert_whenIndexIsEqualToLen_shouldInsertItAndReturnTheList(self):
        index_to_insert = 4
        value_to_insert = -3
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.insert(index_to_insert, value_to_insert)
        self.assertEqual([1, 2, 3, 4, value_to_insert], result)
        self.assertEqual([value_to_insert, 4, 3, 2, 1], cl.reverse())

    def test_customListInsert_whenIndexIsLenMinus1_shouldInsertItAndReturnTheList(self):
        index_to_insert = -5
        value_to_insert = -3
        cl = self.setup_list(1, 2, 3, 4)
        with self.assertRaises(CustomListIndexException) as context:
            cl.insert(index_to_insert, value_to_insert)
        self.assertIsNotNone(context.exception)

    def test_customListInsert_whenListIsEmptyAndInsertAtIndex0_shouldInsertAndReturnTheList(self):
        index_to_insert = 0
        value_to_insert = -3
        cl = self.setup_list()
        result = cl.insert(index_to_insert, value_to_insert)

        self.assertEqual([value_to_insert], result)
        self.assertEqual([value_to_insert], cl.reverse())

    def test_customListInsert_whenListIsEmptyAndInsertAtIndex3_shouldRaiseException(self):
        index_to_insert = 3
        value_to_insert = -3
        cl = self.setup_list()
        result = cl.insert(index_to_insert, value_to_insert)
        self.assertEqual([value_to_insert], result)
        self.assertEqual([value_to_insert], cl.reverse())

    def test_customListInsert_whenIndexIsLessThanNegativeLen_shouldRaiseException(self):
        list_len = 4
        cl = self.setup_list(*range(list_len))
        with self.assertRaises(CustomListIndexException) as context:
            cl.insert(-list_len - 1, 4)
        self.assertIsNotNone(context.exception)

    def test_customListInsert_whenIndexIsNotInt_shouldRaiseException(self):
        list_len = 4
        cl = self.setup_list(range(list_len))
        with self.assertRaises(CustomListTypeException) as context:
            cl.insert('index', 4)
        self.assertIsNotNone(context.exception)