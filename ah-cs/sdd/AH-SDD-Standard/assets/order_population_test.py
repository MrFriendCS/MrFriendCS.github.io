# Title: AH SDD - Order by Population - Tests
# Author: Mr Friend
# Date: 23 Sep 2026

'''Tests the functions in order_population.py'''

import order_population


def test_read_data() -> int:
    """Tests the read_data() function"""
    
    # Local variable
    test: int = 1
    
    print('\nread_data() Tests')
    print('-----------------\n')
    
    try:
        
        # Parallel arrays
        
        print('Test ' + str(test) +
              ': Read data --> ', end='')
        assert len(order_population.read_data()) == 4
        print('Passed')
        
        print('Test ' + str(test) +
              ': Read data - Array of countries --> ', end='')
        assert len(order_population.read_data()[0]) == 47
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': First value --> ', end='')
        assert order_population.read_data()[0][0] == 'Albania'
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': Last value --> ', end='')
        assert order_population.read_data()[0][-1] == 'Vatican City'
        print('Passed')
        
        print('Test ' + str(test) +
              ': Read data - Array of capitals --> ', end='')
        assert len(order_population.read_data()[1]) == 47
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': First value --> ', end='')
        assert order_population.read_data()[1][0] == 'Tirana'
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': Last value --> ', end='')
        assert order_population.read_data()[1][-1] == 'Vatican City'
        print('Passed')
        
        print('Test ' + str(test) +
              ': Read data - Array of areas --> ', end='')
        assert len(order_population.read_data()[2]) == 47
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': First value --> ', end='')
        assert order_population.read_data()[2][0] == 28748
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': Last value --> ', end='')
        assert order_population.read_data()[2][-1] == 0.49
        print('Passed')
        
        print('Test ' + str(test) +
              ': Read data - Array of populations --> ', end='')
        assert len(order_population.read_data()[3]) == 47
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': First value --> ', end='')
        assert order_population.read_data()[3][0] == 2886026
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': Last value --> ', end='')
        assert order_population.read_data()[3][-1] == 825
        print('Passed')
        
        print('\nPASSED: read_data()')
        print('===================\n')
        
        return 1
        
    except:
        
        print('Failed')
        print('\nFAILED: read_data()')
        print('===================\n')
        
        return 0
    

def test_order_population() -> int:
    """Tests the order_population() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[list[str]]
    inputs2: list[list[str]]
    inputs3: list[list[float]]
    inputs4: list[list[int]]
    
    output1: list[str]
    output2: list[str]
    output3: list[float]
    output4: list[int]
    
    # Values
    inputs1 = [['a', 'b', 'c'], ['c', 'b', 'a'],
               ['b', 'a', 'c'], ['a', 'c', 'b']]
    inputs2 = [['a', 'b', 'c'], ['c', 'b', 'a'],
               ['b', 'a', 'c'], ['a', 'c', 'b']]
    inputs3 = [[1.1, 2.2, 3.3], [3.3, 2.2, 1.1],
               [2.2, 1.1, 3.3], [1.1, 3.3, 2.2]]
    inputs4 = [[1, 2, 3], [3, 2, 1],
               [2, 1, 3], [1, 3, 2]]
    
    outputs1 = ['c', 'b', 'a']
    outputs2 = ['c', 'b', 'a']
    outputs3 = [3.3, 2.2, 1.1]
    outputs4 = [3, 2, 1]
    
    print("\norder_population() Tests")
    print("------------------------\n")
    
    try:
        
        for index in range(len(inputs1)):
            
            print(f'Test {test}: order_population({inputs1[index]}, {inputs2[index]}, {inputs3[index]}, {inputs4[index]}) --> ', end="")
            
            assert order_population.order_population(inputs1[index], inputs2[index], inputs3[index], inputs4[index]) == (outputs1, outputs2, outputs3, outputs4)
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: order_population()")
        print("==========================\n")
        
        return 1
        
    except:
        
        print("Failed")
        print("\nFAILED: order_population()")
        print("==========================\n")
        
        return 0


def test_display_top_5() -> int:
    """Tests the display_top_5() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[str]
    inputs2: list[int]
    
    # Values
    inputs1 = ['a', 'b', 'c', 'd', 'e', 'f']
    inputs2 = [1, 2, 3, 4, 5, 6]
    
    print('\ndisplay_top_5() Tests')
    print('---------------------\n')
    
    try:
        
            
        print(f'Test {test}: display_top_5({inputs1}, {inputs2}) --> ')
        
        order_population.display_top_5(inputs1, inputs2)
               
        print("\nCOMPLETED: display_top_5()")
        print("==========================\n")
        
        return 1
        
    except:
        
        print('Failed')
        print('\nFAILED: display_top_5()')
        print('=======================\n')
        
        return 0



def test_write_top_10() -> int:
    """Tests the write_top_10() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[str]
    inputs2: list[str]
    inputs3: list[float]
    inputs4: list[int]
    
    # Values
    inputs1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    inputs2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    inputs3 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.8, 11.7]
    inputs4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    print('\nwrite_top_10() Tests')
    print('--------------------\n')
    
    try:
            
        print(f'Test {test}: write_top_10({inputs1}, {inputs2}, {inputs3}, {inputs4}) --> ')
        
        order_population.write_top_10(inputs1, inputs2, inputs3, inputs4)
        
        test += 1
               
        print("\nCOMPLETED: write_top_10()")
        print("=========================\n")
        
        return 1
        
    except:
        
        print('Failed')
        print('\nFAILED: write_top_10()')
        print('=======================\n')
        
        return 0


def test_all() -> None:
    '''Tests all functions'''
    
    # Local variable
    passed: int = 0
    
    print('\nRun All Tests')
    print('-------------\n')
    
    try:
        
        passed += test_read_data()
        passed += test_order_population()
        passed += test_display_top_5()
        passed += test_write_top_10()
        
        if passed == 4:
            print('\nTesting of all functions: COMPLETED!')
            print('====================================\n')
        else:
            1/0  # Throws an exception
        
    except:
        
        print('\nTesting of all functions: FAILED!')
        print('=================================\n')
        

#
# Main program
#

# Initialise global variables
test: str = ''
run: bool = True

while run:
    print('\norder_population Tests')
    print('------------------\n')

    print('1. read_data()')
    print('2. order_population()')
    print('3. display_top_5()')
    print('4. write_top_10()')
    
    print('\na. All tests')
    print('x. Exit')

    # Get text value from user
    test = input('\nTest: ')

    if test == '1':
        test_read_data()
        
    elif test == '2':
        test_order_population()
        
    elif test == '3':
        test_display_top_5()
        
    elif test == '4':
        test_write_top_10()
             
    elif test == 'a':
        # Run all tests
        test_all()
        
    elif test == 'x':
        # Exit tests
        run = False
