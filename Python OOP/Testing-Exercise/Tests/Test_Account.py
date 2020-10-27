import unittest
from Code_For_Testing.Account import Account

class TestAccount(unittest.TestCase):
    def test_whenInitAccount_shouldInitializeNewAccount(self):
        name = 'John'
        amount = 100
        acc = Account(name, amount)
        self.assertEqual(name, acc.owner)
        self.assertEqual(amount, acc.balance)

    def test_whenAddTransactionWithInt_shouldAddTransaction(self):
        name = 'John'
        amount = 100
        transaction_amount = 20
        acc = Account(name, amount)
        acc.add_transaction(transaction_amount)
        self.assertEqual(amount + transaction_amount, acc.balance)


    def test_whenAddTransactionWithFloat_shouldRaiseException(self):
        name = 'John'
        amount = 100
        transaction_amount = 20.80
        acc = Account(name, amount)
        with self.assertRaises(Exception) as context:
            acc.add_transaction(transaction_amount)
        self.assertIsNotNone(context.exception)

    def test_whenBalanceMethodIsCalled_shouldReturnTheBalance(self):
        name = 'John'
        amount = 100
        amount_for_adding = 50
        amount_for_spending = -20
        acc = Account(name, amount)
        acc.add_transaction(amount_for_adding)
        acc.add_transaction(amount_for_spending)
        self.assertEqual(amount + amount_for_adding + amount_for_spending, acc.balance)

    def test_whenValidateTransactionMethodIsCalled_shouldIncreaseTheBalance(self):
        name = 'John'
        amount = 100
        amount_for_adding = 50
        acc = Account(name, amount)
        expected = f"New balance: {amount + amount_for_adding}"
        result = acc.validate_transaction(acc, amount_for_adding)
        self.assertEqual(expected, result)

    def test_whenValidateTransactionMethodIsCalledWithNegativeAmount_shouldRaiseValueError(self):
        name = 'John'
        amount = 100
        amount_for_validating = -500
        acc = Account(name, amount)
        with self.assertRaises(Exception) as context:
            acc.validate_transaction(amount_for_validating)
        self.assertIsNotNone(context.exception)

    def test_whenLenMethodIsCalled_shouldReturnTheAmountOfTheTransactions(self):
        acc = Account('bob', 10)
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)
        expected = 3
        result = len(acc)
        self.assertEqual(expected, result)

    def test_whenStrMethodIsCalled_shouldReturnStringRepresentationOfTheAccount(self):
        name = 'John'
        amount = 100
        acc = Account(name, amount)
        expected = f'Account of {name} with starting amount: {amount}'
        result = str(acc)
        self.assertEqual(expected, result)

    def test_whenReprMethodIsCalled_shouldReturnRepresentationOfTheAccount(self):
        name = 'John'
        amount = 100
        acc = Account(name, amount)
        expected = f'Account({name}, {amount})'
        result = repr(acc)
        self.assertEqual(expected, result)

    def test_whenGetItemMethodIsCalled_shouldReturnTheTransactionOnTheGivenIndex(self):
        acc = Account('George', 1000)
        acc.add_transaction(200)
        acc.add_transaction(-20)
        acc.add_transaction(-180)
        expected = -180
        result = acc[-1]
        self.assertEqual(expected, result)

    def test_whenReversedMethodIsCalled_shouldReturnReversedTransactionsList(self):
        acc = Account('George', 1000)
        transactions = [200, -20, -180]
        acc.add_transaction(transactions[0])
        acc.add_transaction(transactions[1])
        acc.add_transaction(transactions[2])
        expected = list(reversed(transactions))
        result = list(reversed(acc))
        self.assertEqual(expected, result)

    def test_whenGreaterThanMethodIsCalled_shouldReturnTrueOrFalseDependingOnWichOfTheGivenAccountIsBigger(self):
        acc = Account('bob', 10)
        acc2 = Account('john')
        expected = True
        result = acc > acc2
        self.assertEqual(expected, result)

    def test_whenGreaterOrEqualMethodIsCalled_shouldReturnTrueOrFalseDependingOnWichOfTheGivenAccountIsBigger(self):
        acc = Account('bob', 10)
        acc2 = Account('john', 10)
        expected = True
        result = acc >= acc2
        self.assertEqual(expected, result)

    def test_whenLessThanMethodIsCalled_shouldReturnTrueOrFalseDependingOnWichOfTheGivenAccountIsBigger(self):
        acc = Account('bob', 10)
        acc2 = Account('john')
        expected = False
        result = acc < acc2
        self.assertEqual(expected, result)

    def test_whenLessOrEqualMethodIsCalled_shouldReturnTrueOrFalseDependingOnWichOfTheGivenAccountIsBigger(self):
        acc = Account('bob', 10)
        acc2 = Account('john', 200)
        expected = True
        result = acc <= acc2
        self.assertEqual(expected, result)

    def test_whenEqualMethodIsCalled_shouldReturnTrueOrFalseDependingOnAreTheAccountsEqualOrNot(self):
        acc = Account('bob', 10)
        acc2 = Account('john', 10)
        expected = True
        result = acc == acc2
        self.assertEqual(expected, result)

    def test_whenNonEqualMethodIsCalled_shouldReturnTrueOrFalseDependingOnAreTheAccountsNonEqualOrEqual(self):
        acc = Account('bob', 10)
        acc2 = Account('john', 10)
        expected = False
        result = acc != acc2
        self.assertEqual(expected, result)

    def test_whenAddMethodIsCalled_shouldReturnAddedNamesOfTheGivenOwnersAndSumTheBalanceOfBoth(self):
        acc = Account('Bobby', 10)
        acc2 = Account('Johny')
        acc.add_transaction(20)
        acc.add_transaction(-20)
        acc.add_transaction(30)
        acc2.add_transaction(10)
        acc2.add_transaction(60)
        acc3 = acc + acc2
        expected_name = "Bobby&Johny"
        expected_balance = 110
        expected_transactions = [20, -20, 30, 10, 60]
        returned_name = acc3.owner
        returned_balance = acc3.balance
        returned_transactions = acc3._transactions
        self.assertEqual(expected_name, returned_name)
        self.assertEqual(expected_balance, returned_balance)
        self.assertEqual(expected_transactions, returned_transactions)

if __name__ == "__main__":
    unittest.main()