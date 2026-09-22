# Title: AH SDD - Find a country - Tests
# Author: Mr Friend
# Date: 22 Sep 2026

'''Tests the functions in find_country.py'''

import find_country


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
        assert len(find_country.read_data()) == 4
        print('Passed')
        
        print('Test ' + str(test) +
              ': Read data - Array of countries --> ', end='')
        assert len(find_country.read_data()[0]) == 47
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': First value --> ', end='')
        assert find_country.read_data()[0][0] == 'Albania'
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': Last value --> ', end='')
        assert find_country.read_data()[0][-1] == 'Vatican City'
        print('Passed')
        
        print('Test ' + str(test) +
              ': Read data - Array of capitals --> ', end='')
        assert len(find_country.read_data()[1]) == 47
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': First value --> ', end='')
        assert find_country.read_data()[1][0] == 'Tirana'
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': Last value --> ', end='')
        assert find_country.read_data()[1][-1] == 'Vatican City'
        print('Passed')
        
        print('Test ' + str(test) +
              ': Read data - Array of areas --> ', end='')
        assert len(find_country.read_data()[2]) == 47
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': First value --> ', end='')
        assert find_country.read_data()[2][0] == 28748
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': Last value --> ', end='')
        assert find_country.read_data()[2][-1] == 0.49
        print('Passed')
        
        print('Test ' + str(test) +
              ': Read data - Array of populations --> ', end='')
        assert len(find_country.read_data()[3]) == 47
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': First value --> ', end='')
        assert find_country.read_data()[3][0] == 2886026
        print('Passed')
        
        test += 1
        print('Test ' + str(test) +
              ': Last value --> ', end='')
        assert find_country.read_data()[3][-1] == 825
        print('Passed')
        
        print('\nPASSED: read_data()')
        print('===================\n')
        
        return 1
        
    except:
        print('Failed')
        print('\nFAILED: read_data()')
        print('===================\n')
        
        return 0
    

def test_find_country() -> int:
    """Tests the find_country() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[list[str]]
    inputs2: list[str]
    outputs: list[int]
    
    # Values
    inputs1 = [['a', 'b', 'c'], ['a', 'b', 'c'],
               ['a', 'b', 'c'], ['a', 'b', 'c']]
    inputs2 = ['x', 'a', 'b', 'c']
    outputs = [-1, 0, 1, 2]
    
    print("\nfind_country() Tests")
    print("--------------------\n")
    
    try:
        
        for index in range(len(inputs1)):
            
            print(f'Test {test}: find_country({inputs1[index]}, {inputs2[index]}) --> ', end="")
            
            assert find_country.find_country(inputs1[index], inputs2[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: find_country()")
        print("======================\n")
        
        return 1
        
    except:
        
        print("Failed")
        print("\nFAILED: find_country()")
        print("======================\n")
        
        return 0


def test_display_country() -> int:
    """Tests the display_country() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[list[str]]
    inputs2: list[list[float]]
    inputs3: list[list[int]]
    inputs4: list[int]
    
    # Values
    inputs1 = [['a', 'b', 'c'], ['a', 'b', 'c']]
    inputs2 = [[1.1, 2.2, 3.3], [1.1, 2.2, 3.3]]
    inputs3 = [[1, 2, 3], [1, 2, 3]]
    inputs4 = [2, -1]
    
    print('\ndisplay_country() Tests')
    print('-----------------------\n')
    
    try:
        
        for index in range(len(inputs1)):
            
            print(f'Test {test}: display_country({inputs1[index]}, {inputs2[index]}, {inputs3[index]}, {inputs4[index]}) --> ')
            
            find_country.display_country(inputs1[index], inputs2[index],
                                         inputs3[index], inputs4[index])
            
            test += 1
        
        return 1
        
    except:
        
        print('Failed')
        print('\nFAILED: display_country()')
        print('=========================\n')
        
        return 0



def test_write_summary() -> int:
    """Tests the write_summary() function"""
    
    # Local variables
    test: int = 1
    inputs1: list[str]
    inputs2: list[str]
    inputs3: list[float]
    inputs4: list[int]
    inputs5: int
    
    # Values
    inputs1 = ['a', 'b', 'c']
    inputs2 = ['d', 'e', 'f']
    inputs3 = [1.1, 2.2, 3.3]
    inputs4 = [1, 2, 3]
    inputs5 = 2
    
    print('\nwrite_summary() Tests')
    print('---------------------\n')
    
    try:
            
        print(f'Test {test}: write_summary({inputs1}, {inputs2}, {inputs3}, {inputs4}, {inputs5}) --> ')
        
        find_country.write_summary(inputs1, inputs2, inputs3, inputs4, inputs5)
        
        test += 1
        
        return 1
        
    except:
        
        print('Failed')
        print('\nFAILED: write_summary()')
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
        passed += test_find_country()
        passed += test_display_country()
        passed += test_write_summary()
        
        if passed == 4:
            print('\nTesting of all functions: PASSED!')
            print('=================================\n')
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
    print('\nfind_country Tests')
    print('------------------\n')

    print('1. read_data()')
    print('2. find_country()')
    print('3. display_country()')
    print('4. write_summary()')
    
    print('\na. All tests')
    print('x. Exit')

    # Get text value from user
    test = input('\nTest: ')

    if test == '1':
        test_read_data()
        
    elif test == '2':
        test_find_country()
        
    elif test == '3':
        test_display_country()
        
    elif test == '4':
        test_write_summary()
             
    elif test == 'a':
        # Run all tests
        test_all()
        
    elif test == 'x':
        # Exit tests
        run = False
