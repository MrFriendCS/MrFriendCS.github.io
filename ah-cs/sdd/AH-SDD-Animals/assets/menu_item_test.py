# Title: Menu Item Class Tests
# Author: Mr Friend
# Date: 29 May 2026


# Import Menu Item class
from menu_item import Menu_Item


def test_get_name() -> None:
    """Test the get_name() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global name
    
    try:
        # Test: get the name of a menu item
        assert test_menu_item.get_name() == name
        
        print('Pass: get_name()')
        
        test_passed += 1

    except:
        
        print('Fail: get_name()')
        
        test_failed += 1


def test_set_name() -> None:
    """Test the set_name() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    # Local vairable
    new_name = 'Hamburger'
    
    try:
    
        # Set the name of a menu item
        test_menu_item.set_name(new_name)
    
        # Test: get the name of a menu item
        assert test_menu_item.get_name() == new_name
        
        print('Pass: set_name()')
        
        test_passed += 1

    except:
        
        print('Fail: set_name()')
        
        test_failed += 1


def test_get_price() -> None:
    """Test the get_price() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global price
    
    try:
        # Test: get the price of a menu item
        assert test_menu_item.get_price() == price
        
        print('Pass: get_price()')
        
        test_passed += 1

    except:
        
        print('Fail: get_price()')
        
        test_failed += 1


def test_set_price() -> None:
    """Test the set_price() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    # Local vairable
    new_price = 2.15
    
    try:
    
        # Set the price of a menu item
        test_menu_item.set_price(new_price)
    
        # Test: get the price of a menu item
        assert test_menu_item.get_price() == new_price
        
        print('Pass: set_price()')
        
        test_passed += 1

    except:
        
        print('Fail: set_price()')
        
        test_failed += 1


#
# Main program
#

# Global variables
test_passed = 0
test_failed = 0
name = 'Hot Dog'
price = 1.75

# Create a menu item
test_menu_item = Menu_Item(name, price)

# Display header
print('Menu Item Class Tests')
print('---------------------')

# Run tests
test_get_name()
test_set_name()
test_get_price()
test_set_price()

# Display results
print('\nResults')
print('-------')

print(f'Passed: {test_passed}')
print(f'Failed: {test_failed}')
