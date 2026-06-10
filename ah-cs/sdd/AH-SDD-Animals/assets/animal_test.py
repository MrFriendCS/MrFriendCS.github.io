# Title: Animal Class Tests
# Author: Mr Friend
# Date: 10 Jun 2026


# Import class
from animal import Animal


def test_get_name() -> None:
    """Test the get_name() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global name
    
    try:
        # Test: get the name of the animal
        assert test_object.get_name() == name
        
        print('Pass: get_name()')
        
        test_passed += 1

    except:
        
        print('Fail: get_name()')
        
        test_failed += 1


def test_get_age() -> None:
    """Test the get_age() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global age
    
    try:
        # Test: get the age of the animal
        assert test_object.get_age() == age
        
        print('Pass: get_price()')
        
        test_passed += 1

    except:
        
        print('Fail: get_price()')
        
        test_failed += 1


def test_birthday() -> None:
    """Test the birthday() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    # Local variable
    age = test_object.get_age()
    
    # Happy birthday!
    test_object.birthday()
    
    try:
        # Test: get the age of the animal
        assert test_object.get_age() == age + 1
        
        print('Pass: birthday()')
        
        test_passed += 1

    except:
        
        print('Fail: birthday()')
        
        test_failed += 1


def test_get_weight() -> None:
    """Test the get_weight() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global weight
    
    try:
        # Test: get the weight of the animal
        assert test_object.get_weight() == weight
        
        print('Pass: get_weight()')
        
        test_passed += 1

    except:
        
        print('Fail: get_weight()')
        
        test_failed += 1


def test_set_weight() -> None:
    """Test the set_weight() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global test_weight
    
    # Update the weight of the animal
    test_object.set_weight(test_weight)
    
    try:
        # Test: get the weight of the animal
        assert test_object.get_weight() == test_weight
        
        print('Pass: set_weight()')
        
        test_passed += 1

    except:
        
        print('Fail: set_weight()')
        
        test_failed += 1


def test_get_alive() -> None:
    """Test the get_alive() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global alive
    
    try:
        # Test: get the alive status of the animal
        assert test_object.get_alive() == alive
        
        print('Pass: get_alive()')
        
        test_passed += 1

    except:
        
        print('Fail: get_alive()')
        
        test_failed += 1


def test_die() -> None:
    """Test the die() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    # The animal has died :-(
    test_object.die()
    
    try:
        # Test: check the animal is dead
        assert test_object.get_alive() == False
        
        print('Pass: die()')
        
        test_passed += 1

    except:
        
        print('Fail: die()')
        
        test_failed += 1


#
# Main program
#

# Global variables
test_passed = 0
test_failed = 0

name = 'Bonzo'
age = 17
weight = 15.4
alive = True

test_weight = 14.5

# Create an animal object
test_object = Animal(name, age, weight, alive)

# Display header
print('Animal Class Tests')
print('------------------')

# Run tests
test_get_name()
test_get_age()
test_birthday()
test_get_weight()
test_set_weight()
test_get_alive()
test_die()

# Display results
print('\nResults')
print('-------')

print(f'Passed: {test_passed}')
print(f'Failed: {test_failed}')
