# Title: Animala Class Tests
# Author: Mr Friend
# Date: 10 Jun 2026


# Import classes
from animal import Animal
from animals import Animals


def test_get_number_of_animals() -> None:
    """Test the get_number_of_animals() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    try:
        # Test: get the number of animals in the collection
        assert test_object.get_number_of_animals() == 0
        
        print('Pass: get_number_of_animals()')
        
        test_passed += 1

    except:
        
        print('Fail: get_number_of_animals()')
        
        test_failed += 1


def test_add_animal() -> None:
    """Test the add_animal() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    # Add first animal to collection
    test_object.add_animal(animal1)
    
    try:
        # Test: get the number of animals in the collection
        assert test_object.get_number_of_animals() == 1
        
        print('Pass: add_animal() - first animal')
        
        test_passed += 1

    except:
        
        print('Fail: add_animal() - first animal')
        
        test_failed += 1
    
    # Add animals to collection
    test_object.add_animal(animal2)
    test_object.add_animal(animal3)
    
    try:
        # Test: get the number of animals in the collection
        assert test_object.get_number_of_animals() == 3
        
        print('Pass: add_animal() - extra animals')
        
        test_passed += 1

    except:
        
        print('Fail: add_animal() - extra animals')
        
        test_failed += 1


def test_find_oldest() -> None:
    """Test the find_oldest() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    try:
        # Test: get the oldest animal in collection
        assert test_object.find_oldest() == (17, 'Bonzo')
        
        print('Pass: find_oldest() - test 1')
        
        test_passed += 1

    except:
        
        print('Fail: find_oldest() - test 1')
        
        test_failed += 1
    
    # Bonzo died :-(
    animal3.die()
    
    try:
        # Test: get the oldest animal in collection
        assert test_object.find_oldest() == (3, 'Kitty')
        
        print('Pass: find_oldest() - test 2')
        
        test_passed += 1

    except:
        
        print('Fail: find_oldest() - test 2')
        
        test_failed += 1
    
    
def display_animals() -> None:
    """Display the details of all the animals."""
    
    # Variables
    animals = test_object.get_animals()
    
    # Header
    print('\nAnimals')
    print('-------')
    
    for index in range(len(animals)):
        
        # Animal's details
        print(f'\nAnimal {index+1}')
        print(f'Name: {animals[index].get_name()}')
        print(f'Age: {animals[index].get_age()}')
        print(f'Weight: {animals[index].get_weight()}')
        print(f'Alive: {animals[index].get_alive()}')
        
    # Footer
    print('=======\n')
    
    


#
# Main program
#

# Global variables
test_passed = 0
test_failed = 0

# Create an animals object
test_object = Animals()

# Create animal objects
animal1 = Animal('Goldie', 2, 0.1, True)
animal2 = Animal('Kitty', 3, 2.7, True)
animal3 = Animal('Bonzo', 17, 15.4, True)

# Display header
print('Animal Class Tests')
print('------------------')

# Run tests
test_get_number_of_animals()
test_add_animal()
test_find_oldest()
display_animals()
test_object.order_by_age()
display_animals()
test_object.order_by_weight()
display_animals()

# Display results
print('\nResults')
print('-------')

print(f'Passed: {test_passed}')
print(f'Failed: {test_failed}')
