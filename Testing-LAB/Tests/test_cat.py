import unittest

from Code_for_Testing.Cat import Cat


class CatTester(unittest.TestCase):
    def test_CatEat_whenCatEatMethodIsCalled_shouldIncreaseCatSize(self):
        #•	Cat's size is increased after eating
        cat = Cat('Rocky')
        cat_size = cat.size
        cat.eat()
        self.assertEqual(cat_size + 1, cat.size)

    def test_CatEat_whenCatEatMethodIsCalled_shouldBeFed(self):
    #•	Cat is fed after eating
        cat = Cat('Rocky')
        cat.eat()
        self.assertEqual(True, cat.fed)

    def test_CatEat_whenCatAlreadyFed_shouldRaiseExeption(self):
    #•	Cat cannot eat if already fed, raises an error
        cat = Cat('Rocky')
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()
        self.assertIsNotNone(context.exception)

    def test_CatSleep_whenCatSleepMethodIsCalled_shouldRaiseExeption(self):
    #•	Cat cannot fall asleep if not fed, raises an error
        cat = Cat('Rocky')
        with self.assertRaises(Exception) as context:
            cat.sleep()
        self.assertIsNotNone(context.exception)

    def test_CatSleepy_shouldNotBeSleepy(self):
    #•	Cat is not sleepy after sleeping
        cat = Cat('Rocky')
        cat.eat()
        cat.sleep()
        self.assertEqual(False, cat.sleepy)

if __name__ == "__main__":
    unittest.main()