# Title: AH-SDD-Dog Tests
# Author: 
# Date: 3 Jun 2026


# Get Dog class
from dog import Dog


def test_get_name() -> None:
    """Test the get_name() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global name
    
    try:
        # Test: get the name
        assert test_dog.get_name() == name
        
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
        # Test: get the age
        assert test_dog.get_age() == age
        
        print('Pass: get_age()')
        
        test_passed += 1

    except:
        
        print('Fail: get_age()')
        
        test_failed += 1


def test_birthday() -> None:
    """Test the birthday() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global age
    
    try:
        # Increase age by 1
        test_dog.birthday()
        
        # Test: get the age
        assert test_dog.get_age() == age + 1
        
        print('Pass: birthday()')
        
        test_passed += 1

    except:
        
        print('Fail: birthday()')
        
        test_failed += 1


def test_eat() -> None:
    """Test the eat() method."""
    
    # Use global variables
    global test_failed
    
    print('\nCheck output below:\n')
        
    try:
        
        # Test: Lower case food
        test_dog.eat('pizza (lower)')

    except:
        
        print('Fail: eat(\'pizza (lower)\')')
        
        test_failed += 1
        
    try:
        
        # Test: Upper case food
        test_dog.eat('PIZZA (upper)')

    except:
        
        print('Fail: eat(\'PIZZA (upper)\')')
        
        test_failed += 1


#
# Main program
#

# Global variables
test_passed = 0
test_failed = 0
name = 'Fido'
age = 9

# Create a dog
test_dog = Dog(name, age)

# Display header
print('Dog Class Tests')
print('---------------\n')

# Run tests
test_get_name()
test_get_age()
test_birthday()
test_eat()

# Display results
print('\nResults')
print('-------')

print(f'Passed: {test_passed}')
print(f'Failed: {test_failed}')
