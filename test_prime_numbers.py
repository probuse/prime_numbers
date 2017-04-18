import unittest
from prime_numbers_ import prime_numbers

class PrimeNumberTestCases(unittest.TestCase):
    def setup(self):
        self.result1 = prime_numbers(-3)
        self.result2 = prime_numbers(kkk)
        self.result3 = prime_numbers('kkk')
        self.result4 = prime_numbers(3.5)
        self.result5 = prime_numbers(5)
        self.result6 = prime_numbers(0)
        self.result7 = prime_numbers(1)
        self.result8 = prime_numbers(27)
        self.result9 = prime_numbers(2)
    
    def test_number_is_prime(self):
        self.assertEquals(prime_numbers(6), [2, 3, 5])
'''           
    def test_negative_integer(self):
        self.assertEquals(prime_numbers(-3), TypeError)
        self.assertFalse(prime_numbers(-100))

        
    def test_only_integers(self):
        self.assertIsInstance(prime_numbers(3.4), int)
        self.assertFalse(prime_numbers('kkk'))
        
    def test_one_and_zero(self):
        self.assertEquals(prime_numbers(0), ValueError)
        self.assertFalse(prime_numbers(1))
        
    def test_number_is_prime(self):
        self.assertEquals(prime_numbers(6), [2, 3, 5])
'''        
if __name__ == '__main__':
    unittest.main()
