# Title: Order Class Tests
# Author: Mr Friend
# Date: 29 May 2026


# Import Menu Item and Order classes
from menu_item import Menu_Item
from order import Order


def test_add_item() -> None:
    """Test the get_add_item() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global item1_name
    global item1_price
    global item2_name
    global item2_price
    
    try:
        # Add first item to order
        test_order.add_item(test_menu_item1)
        
        # Test: One item added
        assert len(test_order.get_items()) == 1
        
        print('Pass: add_item() - first item')
        
        test_passed += 1

    except:
        
        print('Fail: add_item() - first item')
        
        test_failed += 1
    
    try:
        
        # Add second item to order
        test_order.add_item(test_menu_item2)
        
        # Test: Two items added
        assert len(test_order.get_items()) == 2
        
        print('Pass: add_item() - second item')
        
        test_passed += 1

    except:
        
        print('Fail: add_item() - second item')
        
        test_failed += 1


def test_get_items() -> None:
    """Test the get_items() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    # Local variable
    array_of_objects = []
    
    try:
        
        # Get items
        array_of_objects = test_order.get_items()
        
        # Loop for each item
        for item in array_of_objects:
            
            # Test: check object type
            assert isinstance(item, Menu_Item) == True
        
        print(f'Pass: get_items() - {len(array_of_objects)} items in order')
        
        test_passed += 1

    except:
        
        print('Fail: get_items()')
        
        test_failed += 1


def test_get_status() -> None:
    """Test the get_status() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    try:
        
        # Test: check status
        assert test_order.get_status() == 'In progress'
        
        print('Pass: get_status()')
        
        test_passed += 1

    except:
        
        print('Fail: get_status()')
        
        test_failed += 1
        

def test_calculate_cost() -> None:
    """Test the calculate_cost() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global item1_price
    global item2_price
        
    try:
        
        # Test: check status
        assert test_order.calculate_cost() == item1_price + item2_price
        
        print('Pass: calculate_cost()')
        
        test_passed += 1

    except:
        
        print('Fail: calculate_cost()')
        
        test_failed += 1
        

def test_complete_order() -> None:
    """Test the complete_order() method."""
    
    # Use global variables
    global test_passed
    global test_failed
        
    try:
        
        # Update status
        test_order.complete_order()
        
        # Test: check status
        assert test_order.get_status() == 'Completed'
        
        print('Pass: complete_order()')
        
        test_passed += 1

    except:
        
        print('Fail: complete_order()')
        
        test_failed += 1
        

def test_display_order() -> None:
    """Test the display_order() method."""
    
    # Use global variables
    global test_failed
    
    print('\nCheck output below:\n')
        
    try:
        
        # Update status
        test_order.display_order()

    except:
        
        print('Fail: display_order()')
        
        test_failed += 1



#
# Main program
#

# Global variables
test_passed = 0
test_failed = 0
item1_name = 'Hot Dog'
item1_price = 1.75
item2_name = 'Hamburger'
item2_price = 2.15

# Create menu items
test_menu_item1 = Menu_Item(item1_name, item1_price)
test_menu_item2 = Menu_Item(item2_name, item2_price)

# Create an order
test_order = Order()

# Display header
print('Order Tests')
print('-----------\n')

# Run tests
test_add_item()
test_get_items()
test_get_status()
test_calculate_cost()
test_complete_order()
test_display_order()

# Display results
print('\nResults')
print('-------')

print(f'Passed: {test_passed}')
print(f'Failed: {test_failed}')
