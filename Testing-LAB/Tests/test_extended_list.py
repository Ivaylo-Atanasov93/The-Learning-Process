import unittest

from Code_for_Testing.Extended_List import IntegerList

class TestExtendedList(unittest.TestCase):
    def test_ListAddOperation_whenAddMethodCalled_shouldAddElement(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        array.add(5)
        self.assertEqual([2, 4, 6, 7, 2, 5, 6, 5, 5], array.get_data())

    def test_ListAddOperation_whenAddMethodCalled_shouldRaiseException(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        with self.assertRaises(Exception) as context:
            array.add("asd")
        self.assertIsInstance(context.exception, ValueError)

    def test_ListRemoveIndexOperation_whenRemoveIndexMethodIsCalled_shouldReturnTheValueOfTheGivenIndex(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        returned = array.remove_index(5)
        self.assertEqual([2, 4, 6, 7, 2, 6, 5], array.get_data())
        self.assertEqual(5, returned)

    def test_ListRemoveIndexOperation_whenRemoveIndexMethodIsCalled_shouldRaiseException(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        with self.assertRaises(Exception) as context:
            array.remove_index(10)
        self.assertIsInstance(context.exception, IndexError)

    def test_ListInit_whenInitializeCorrect_shouldReceiveAndKeepOnlyIntegers(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        self.assertEqual([2, 4, 6, 7, 2, 5, 6, 5], array.get_data())

    # def test_ListInitOperation_whenAddMethodCalled_shouldRaiseException(self):
    #     with self.assertRaises(Exception) as context:
    #         array = IntegerList(2, 4, 6, 7, 'Woof', 5, 6, 5)
    #     self.assertIsNotNone(context.exception)

    def test_ListInit_whenInitializeWithString_shouldRecieveAndKeepOnlyIntegers(self):
        array = IntegerList(2, 4, 6, 7, 2, "ASD", 6, 5)
        self.assertEqual([2, 4, 6, 7, 2, 6, 5], array.get_data())

    def test_ListGetOperation_whenGetMethodIsCalled_shouldReturnTheValueOfTheGivenIndex(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        self.assertEqual(5, array.get(5))

    def test_ListGetOperation_whenGetMethodIsCalledWithInvalidIndex_shouldRaiseException(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        with self.assertRaises(Exception) as context:
            array.get(10)
        self.assertIsInstance(context.exception, IndexError)

    def test_ListInsertOperation_whenInsertMethodIsCalledWithValidIndex_shouldReturnUpdatedList(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        array.insert(2, 10)
        self.assertEqual([2, 4, 10, 6, 7, 2, 5, 6, 5], array.get_data())

    def test_ListInsertOperation_whenInsertMethodIsCalledWithInvalidIndex_shouldReturnException(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        with self.assertRaises(Exception) as context:
            array.insert(10, 8)
        self.assertIsInstance(context.exception, IndexError)

    def test_ListInsertOperation_whenInsertMethodIsCalledWithString_shouldReturnException(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        with self.assertRaises(Exception) as context:
            array.insert(3, "ASD")
        self.assertIsInstance(context.exception, ValueError)

    def test_ListGetBiggestOperation_shouldReturnTheBiggestNumberInTheList(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        self.assertEqual(7, array.get_biggest())

    def test_ListGetIndexOperation_shouldReturnTheIndexOfTheGivenNumber(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        self.assertEqual(1, array.get_index(4))

    def test_ListGetDataOperation_whenGetDataMethodIsCalled_shouldReturnTheList(self):
        array = IntegerList(2, 4, 6, 7, 2, 5, 6, 5)
        self.assertEqual([2, 4, 6, 7, 2, 5, 6, 5], array.get_data())

if __name__ == "__main__":
    unittest.main()