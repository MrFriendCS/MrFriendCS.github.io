# Title: AH-SDD-Shape Tests
# Author: 
# Date: 5 Jun 2026


# Get Dog class
from shape import Shape


def test_get_vertices() -> None:
    """Test the get_vertices() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global vertices_triangle
    
    try:
        # Test: get the vertices
        assert test_triangle.get_vertices() == vertices_triangle
        
        print('Pass: get_vertices()')
        
        test_passed += 1

    except:
        
        print('Fail: get_vertices()')
        
        test_failed += 1

def test_calc_perimeter() -> None:
    """Test the calc_perimeter() method."""
    
    # Use global variables
    global test_passed
    global test_failed
    global perimeter_triangle
    global perimeter_square
    
    try:
        # Test: calculate the perimeter of a triangle
        assert test_triangle.calc_perimeter() == perimeter_triangle
        
        print('Pass: calc_perimeter() - triangle')
        
        test_passed += 1

    except:
        
        print('Fail: calc_perimeter() - triangle')
        
        test_failed += 1
    
    try:
        # Test: calculate the perimeter of a square
        assert test_square.calc_perimeter() == perimeter_square
        
        print('Pass: calc_perimeter() - square')
        
        test_passed += 1

    except:
        
        print('Fail: calc_perimeter() - square')
        
        test_failed += 1


#
# Main program
#

# Global variables
test_passed = 0
test_failed = 0

vertices_triangle = [[7, 2], [11, 2], [7, 5]]
perimeter_triangle = 12  # 3 + 4 + 5

vertices_square = [[17.6, 13.7], [20.1, 13.7],
                   [20.1, 11.2], [17.6, 11.2]]
perimeter_square = 10  # 2.5 * 4


# Create test shapes
test_triangle = Shape(vertices_triangle)
test_square = Shape(vertices_square)

# Display header
print('Shape Class Tests')
print('-----------------\n')

# Run tests
test_get_vertices()
test_calc_perimeter()

# Display results
print('\nResults')
print('-------')

print(f'Passed: {test_passed}')
print(f'Failed: {test_failed}')
