import unittest
from project.Custom_List_Project import CustomList

class TestCustomList(unittest.TestCase):
    def test_InitCustomList_shouldInitializeNewInstanceOfCustomList(self):
        result = CustomList(5, 6, 7, 8)
        expected = [5, 6, 7, 8]
        self.assertEqual(expected, result)