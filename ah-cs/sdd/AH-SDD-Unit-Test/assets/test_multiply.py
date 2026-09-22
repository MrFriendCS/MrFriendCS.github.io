# Title: Unit Test - Test 'multiply' Function
# Author: Mr Friend
# Date: 18 Apr 2026

# Get extra code
import unittest

# Get code to test
from main import multiply


class TestMultiplyFunction(unittest.TestCase):
    """Define tests."""
    
    def testMultiplyPos(self):
        self.assertEqual(multiply(3, 2), 6)

    def testMultiplyNeg(self):
        self.assertEqual(multiply(-3, -2), 6)
        
    def testMultiplyMixed(self):
        self.assertEqual(multiply(3, -2), -6)
        self.assertEqual(multiply(-3, 2), -6)


# Run tests
if __name__ == '__main__':
    unittest.main()
