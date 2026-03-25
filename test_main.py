import unittest
from main import calculate_multi, calculate_sub, calculate_sum_and_average, get_numbers_from_user

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average([1, -2, 3])

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average(["a", "b", "c"])


    # Write unitest for calculate_sub function
    def test_calculate_sub_valid_numbers(self):
        self.assertEqual(calculate_sub([10, 2, 3]), 5)

    def test_calculate_sub_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sub([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_calculate_sub_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_sub([1, -2, 3])

    def test_calculate_sub_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_sub(["a", "b", "c"])

    # Write unit-test for calculate_multi function
    def test_calculate_multi_valid_numbers(self):
        self.assertEqual(calculate_multi([2, 3, 4]), 24)

    def test_calculate_multi_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_multi([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_calculate_multi_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_multi([1, -2, 3])

    def test_calculate_multi_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_multi(["a", "b", "c"])


if __name__ == '__main__':
    unittest.main()
