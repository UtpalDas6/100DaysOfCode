import unittest
from detect_prime import prime_func
from find_binary import binary
from sum_squares import sum_even


class TestScripts(unittest.TestCase):
    def test_prime_func_basic(self):
        self.assertEqual(prime_func([1, 2, 3, 4, 5, 6]), [2, 3, 5])
        self.assertEqual(prime_func([]), [])
        self.assertEqual(prime_func([8, 9, 10]), [])

    def test_binary_basic(self):
        self.assertEqual(binary(5), "101")
        self.assertEqual(binary(0), "0")
        self.assertEqual(binary(1), "1")

    def test_sum_even_basic(self):
        self.assertEqual(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
        self.assertEqual(sum_even([1]), 0)


if __name__ == "__main__":
    unittest.main()
