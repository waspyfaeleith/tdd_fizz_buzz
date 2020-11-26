import unittest

from src.fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz__3_returns_fizz(self):
       self.assertEqual("fizz", fizz_buzz(3)) 

    def test_fizz_buzz__5_returns_buzz(self):
        self.assertEqual("buzz", fizz_buzz(5))
    
    def test_fizz_buzz__15_returns_fizzbuzz(self):
        self.assertEqual("fizzbuzz", fizz_buzz(15))