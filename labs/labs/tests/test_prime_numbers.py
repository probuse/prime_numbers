from nose.tools import *
from lab1 import prime_numbers

def test_positive_integer():
    assertEqual(prime_numbers(-3), ValueError)
    assertEqual(prime_numbers(kkk), ValueError)
    assertEqual(prime_numbers('kkk'), ValueError)
    assertEqual(prime_numbers(3.5), ValueError)

def test_is_prime():
    assertEqual(is_prime(0), False)
    assertEqual(is_prime(1), False)
    assertEqual(is_prime(2), True)
    assertEqual(is_prime(27), False)
