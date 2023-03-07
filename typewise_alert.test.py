import unittest
from production_code import find_max

class TestFindMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_max([]))

    def test_single_item_list(self):
        self.assertEqual(find_max([1]), 1)

    def test_ordered_list(self):
        self.assertEqual(find_max([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(find_max([3, 1, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_max([-1, -2, -3]), -1)

if __name__ == '__main__':
    unittest.main()
