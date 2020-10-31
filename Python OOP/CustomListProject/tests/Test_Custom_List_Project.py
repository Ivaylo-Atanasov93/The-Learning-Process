import unittest
from project.Custom_List_Project import CustomList
from project.Errors import CustomListIndexException, CustomListTypeException, CustomListSumException


class CustomListTestsBase(unittest.TestCase):
    def setup_list(self, *args):
        cl = CustomList()
        [cl.append(el) for el in args]
        return cl

    def assertCustomListStringEqual(self, ll, cl1):
        expected = f"{';'.join([repr(el) for el in ll])}"
        self.assertEqual(expected, str(cl1))


class TestCaseBase(unittest.TestCase):
    def assertEmpty(self, iterable):
        return self.assertListEqual([], list(iterable))


class TestCustomList(CustomListTestsBase):

    # Testing the List Append Functionality_____________________________________________________________________________

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

    # Testing the List Remove Functionality_____________________________________________________________________________

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

    # Testing the List Get Functionality________________________________________________________________________________

    def test_customListGet_whenIndexInTheMiddle_shouldReturnElement(self):
        value_to_get = 3
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.get(2)
        self.assertEqual(value_to_get, result)

    def test_customListGet_whenIndexIsZero_shouldReturnElement(self):
        value_to_get = 3
        cl = self.setup_list(1, 2, value_to_get, 4, )
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

    # Testing the List Extend Functionality_____________________________________________________________________________

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

    # Testing the List Insert Functionality_____________________________________________________________________________

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
        self.assertEqual([4, 3, 2, 1, value_to_insert, ], cl.reverse())

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

    # Testing the List Pop Functionality________________________________________________________________________________

    def test_customListPop_whenIsEmptyList_shouldRaiseException(self):
        cl = self.setup_list()
        with self.assertRaises(CustomListIndexException) as context:
            cl.pop()
        self.assertIsNotNone(context.exception)

    def test_CustomListAppend_whenNonEmpty_shouldReturnLastElement(self):
        cl = self.setup_list(1, 2, 3)
        result = cl.pop()
        self.assertEqual(3, result)
        self.assertEqual([2, 1], cl.reverse())

    # Testing the List Clear Functionality______________________________________________________________________________

    def test_customListClear_whenNonEmptyList_shouldClear(self):
        cl = self.setup_list(1, 2, 3)
        cl.clear()
        self.assertEqual([], cl.reverse())

    def test_customListClear_whenEmptyList_shouldClear(self):
        cl = self.setup_list()
        cl.clear()
        self.assertEqual([], cl.reverse())

    # Testing the List Index Functionality______________________________________________________________________________

    def test_customListIndex_whenListIsEmpty_shouldReturnMinusOne(self):
        cl = self.setup_list()
        index = cl.index(-5)
        self.assertEqual(-1, index)

    def test_customListIndex_whenValueNotInList_shouldReturnMinusOne(self):
        cl = self.setup_list(1, 2, 3, 4)
        index = cl.index(-5)
        self.assertEqual(-1, index)

    def test_customListIndex_whenValueIsInList_shouldReturnItsValue(self):
        cl = self.setup_list(1, 2, 3, 4)
        index = cl.index(2)
        self.assertEqual(1, index)

    def test_customListIndex_whenListContainsValueMultipleTimes_shouldReturnItsValue(self):
        cl = self.setup_list(1, 2, 3, 4, 1, 2, 4)
        index = cl.index(4)
        self.assertEqual(3, index)

    # Testing the List Count Functionality______________________________________________________________________________

    def test_customListCount_whenListIsEmpty_shouldReturn0(self):
        cl = self.setup_list()
        result = cl.count(2)
        self.assertEqual(0, result)

    def test_customListCount_whenValueNotInList_shouldReturnMinusOne(self):
        cl = self.setup_list(1, 3, 4, 5, 6)
        result = cl.count(2)
        self.assertEqual(0, result)

    def test_customListCount_whenValueIsInList_shouldReturnItsValue(self):
        cl = self.setup_list(1, 2, 3, 4)
        result = cl.count(2)
        self.assertEqual(1, result)

    def test_customListCount_whenListContainsValueMultipleTimes_shouldReturnItsValue(self):
        cl = self.setup_list(1, 2, 3, 4, 1, 2, 4)
        result = cl.count(4)
        self.assertEqual(2, result)

    # Testing the List Reverse Functionality____________________________________________________________________________

    def test_customListReverse_whenIsEmptyList_shouldReturnItReversed(self):
        cl = self.setup_list()
        self.assertEqual([], cl.reverse())

    def test_CustomListReverse_whenMultipleElements_shouldReturnReversedList(self):
        values = list(range(4))
        cl = self.setup_list(*values)

        result = cl.reverse()

        self.assertEqual(values[::-1], result)

    def test_customListReverse_whenIsListHasOnlyOneElement_shouldReturnItReversed(self):
        cl = self.setup_list(1)
        self.assertEqual([1], cl.reverse())

    # Testing the List Copy Functionality_______________________________________________________________________________

    def test_customListCopy_whenEmptyList_shouldReturnEmptyCustomList(self):
        cl = self.setup_list()

        result = cl.copy()

        self.assertNotEqual(cl, result)
        self.assertListEqual(cl.reverse(), result.reverse())

    def test_customListCopy_whenNonEmptyList_shouldReturnCopyOfTheCustomList(self):
        cl = self.setup_list(1, 2, 3, 4, 5)

        result = cl.copy()

        self.assertNotEqual(cl, result)
        self.assertListEqual(cl.reverse(), result.reverse())

    # Testing the List Size Functionality_______________________________________________________________________________

    def test_customListSize_whenEmptyList_shouldReturnZero(self):
        cl = self.setup_list()
        result = cl.size()
        self.assertEqual(0, result)

    def test_customListSize_whenNonEmptyList_shouldReturnCorrectLengthOfTheList(self):
        values = [1, 2, 3, 4, 5]
        cl = self.setup_list(*values)
        result = cl.size()
        self.assertEqual(len(values), result)

    # Testing the List Add First Functionality__________________________________________________________________________

    def test_customListAddFirst_whenIsEmptyList_shouldAddElement(self):
        cl = self.setup_list()
        cl.add_first(0)
        self.assertEqual([0], cl.reverse())

    def test_CustomListAddFirst_whenNonEmpty_shouldAddElementOnFirstIndex(self):
        cl = self.setup_list(1, 2, 3)
        cl.add_first(0)
        self.assertEqual([3, 2, 1, 0], cl.reverse())

    # Testing the List Dictionarize Functionality_______________________________________________________________________

    def test_customListDictionarize_whenIsEmptyList_shouldReturnEmptyDictionary(self):
        cl = self.setup_list()
        result = cl.dictionize()
        self.assertEqual({}, result)

    def test_CustomListDictionarize_whenNonEmpty_shouldReturnDictionary(self):
        cl = self.setup_list(1, 2, 3)
        expected = {1: 2, 3: ' '}
        result = cl.dictionize()
        self.assertEqual(expected, result)

    def test_customListDictionarize_whenIsListHasOnlyOneElement_shouldDictionaryWithOnePairWithValueEmptyString(self):
        cl = self.setup_list(1, 2, 3, 4, 5, 6)
        expected = {1: 2, 3: 4, 5: 6}
        result = cl.dictionize()
        self.assertEqual(expected, result)

    # Testing the List Move Functionality_______________________________________________________________________________

    def test_customListMove_whenListIsEmpty_should(self):
        cl = self.setup_list()
        result = cl.move(0)
        self.assertEqual([], result)

    def test_customListMove_whenSingleElement_shouldReturnIt(self):
        cl = self.setup_list(1)
        result = cl.move(3)
        self.assertEqual([1], result)
        self.assertEqual([1], cl.reverse())

    def test_customListMove_whenMultipleElements_shouldMoveThem(self):
        part_1 = [1, 2]
        part_2 = [3, 4, 5]
        cl = self.setup_list(*part_1, *part_2)

        result = cl.move(2)
        expected = part_2 + part_1

        self.assertEqual(expected, result)
        self.assertCustomListStringEqual(expected, cl)

    # Testing the List Sum Functionality________________________________________________________________________________

    def test_customListSum_whenIsEmptyList_shouldReturnSum(self):
        cl = self.setup_list()
        result = cl.sum()
        self.assertEqual(0, result)

    def test_CustomListSum_whenHasMultipleNumbers_shouldSumAllValues(self):
        cl = self.setup_list(1, 2, 3, 4, 5)
        result = cl.sum()
        self.assertEqual(15, result)

    def test_CustomListSum_whenHasMultipleElementsWithLenObjects_shouldSumAllValuesAndSumOfAllLenObjects(self):
        numbers = [1, 2, 3, 4, 5]
        len_objects = ['house', [1, 2], (3, 4), {1, 2, 3}, {1: 2, 3: 4}]
        cl = self.setup_list(*numbers, *len_objects)
        expected = sum(numbers) + sum(len(el) for el in len_objects)
        result = cl.sum()
        self.assertEqual(expected, result)

    def test_CustomListSum_whenHasInvalidObjects_shouldRaiseException(self):
        numbers = [1, 2, 3, 4, 5]
        len_objects = ['house', [1, 2], (3, 4), {1, 2, 3}, {1: 2, 3: 4}]
        invalid_objects = [object()]
        cl = self.setup_list(*numbers, *len_objects, *invalid_objects)
        with self.assertRaises(CustomListSumException) as context:
            cl.sum()
        self.assertIsNotNone(context.exception)

    # Testing the List Overbound Functionality__________________________________________________________________________

    def test_CustomListOverbound_whenHasSingleNumber_shouldReturnItsIndex(self):
        values = [1]
        cl = self.setup_list(*values)
        expected = values.index(max(values))
        result = cl.overbound()
        self.assertEqual(expected, result)

    def test_CustomListOverbound_whenHasMultipleNumbers_shouldReturnTheIndexOfTheBiggest(self):
        values = [1, 2, 3, 4, 5]
        cl = self.setup_list(*values)
        expected = values.index(max(values))
        result = cl.overbound()
        self.assertEqual(expected, result)

    def test_CustomListOverbound_whenHasMultipleElementsWithLenObjectsAndBiggestIsANumber_shouldReturnTheIndexOfTheBiggestNumber(
            self):
        numbers = [1, 2, 3, 4, 5]
        len_objects = ['house', [1, 2], (3, 4), {1, 2, 3}, {1: 2, 3: 4}]
        all = numbers + len_objects
        cl = self.setup_list(*all)
        expected = 4
        result = cl.overbound()
        self.assertEqual(expected, result)

    def test_CustomListOverbound_whenHasMultipleElementsWithLenObjectsAndBiggestIsALenObject_shouldReturnTheIndexOfTheBiggestNumber(
            self):
        numbers = [1, 2, 3]
        len_objects = ['house', [1, 2], (3, 4), {1, 2, 3, 9}, {1: 2, 3: 4}]
        cl = self.setup_list(*numbers, *len_objects)
        expected = 3
        result = cl.overbound()
        self.assertEqual(expected, result)

    # Testing the List Overbound Functionality__________________________________________________________________________

    def test_CustomListUnderbound_whenHasSingleNumber_shouldReturnItsIndex(self):
        values = [1]
        cl = self.setup_list(*values)
        expected = values.index(min(values))
        result = cl.underbound()
        self.assertEqual(expected, result)

    def test_CustomListUnderbound_whenHasMultipleNumbers_shouldReturnTheIndexOfTheSmallest(self):
        values = [1, 2, 3, 0, 4, 5]
        cl = self.setup_list(*values)
        expected = values.index(min(values))
        result = cl.underbound()
        self.assertEqual(expected, result)

    def test_CustomListUnderbound_whenHasMultipleElementsWithLenObjectsAndBiggestIsANumber_shouldReturnTheIndexOfTheSmallestNumber(
            self):
        numbers = [1, 2, 3, 4, 5, 0]
        len_objects = ['house', [1, 2], (3, 4), {1, 2, 3}, {1: 2, 3: 4}]
        all = numbers + len_objects
        cl = self.setup_list(*all)
        expected = 5
        result = cl.underbound()
        self.assertEqual(expected, result)

    def test_CustomListUnderbound_whenHasMultipleElementsWithLenObjectsAndBiggestIsALenObject_shouldReturnTheIndexOfTheSmallestNumber(
            self):
        numbers = [1, 2, 3]
        len_objects = ['house', [1, 2], (3, 4), '', {1, 2, 3, 9}, {1: 2, 3: 4}]
        cl = self.setup_list(*numbers, *len_objects)
        expected = 6
        result = cl.underbound()
        self.assertEqual(expected, result)
