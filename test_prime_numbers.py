import unittest
from prime_numbers_ import prime_numbers, is_prime

class PrimeNumberTestCases(unittest.TestCase):
    
    def test_prime_numbers_output(self):
        self.assertEquals(prime_numbers(6), [2, 3, 5])
        self.assertEquals(prime_numbers(2), [2])
           
    def test_input_is_positive_and_greater_than_zero(self):
        with self.assertRaises(TypeError) : prime_numbers(-3)
        with self.assertRaises(TypeError) : prime_numbers(0)
        
    def test_input_is_integer(self):
        with self.assertRaises(TypeError) : prime_numbers('Hello Friend')
        with self.assertRaises(TypeError) : prime_numbers(3.45)
        
    def test_1_not_prime(self):
        self.assertEquals(prime_numbers(1), False)
        
    
if __name__ == '__main__':
    unittest.main()
