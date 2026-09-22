# Title: Unit Test - Test 'add' Function
# Author: Mr Friend
# Date: 18 Apr 2026

# Get extra code
import unittest

# Get code to test
from main import add


class TestAddFunction(unittest.TestCase):
    """Define tests."""
    
    def testAddPos(self):
        self.assertEqual(add(1, 2), 3)

    def testAddNeg(self):
        self.assertEqual(add(-1, -2), -3)

    def testAddMixed(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)


# Run tests
if __name__ == '__main__':
    unittest.main()
