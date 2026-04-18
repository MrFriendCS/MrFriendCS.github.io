# Title: Unit Test - Test 'Person' Class
# Author: Mr Friend
# Date: 18 Apr 2026

# Get extra code
import unittest

# Get code to test
from main import Person


class TestMultiplyFunction(unittest.TestCase):
    """Define tests."""
    
    def testPersonCreation(self):
        # Create a Person
        person = Person("Tom", 19)
        
        # Test name    
        self.assertEqual(person.getName(), "Tom")
        
        # Test age    
        self.assertEqual(person.getAge(), 19)

    def testPersonSeeAge(self):
        # Create a Person
        person = Person("Tom", 19)
        
        # Set age    
        person.setAge(25)
        
        # Test age    
        self.assertEqual(person.getAge(), 25)


# Run tests
if __name__ == '__main__':
    unittest.main()
