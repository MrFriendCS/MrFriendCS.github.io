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
    print('----------------\n')
    
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
        print('==================\n')
        
        return 1
        
    except:
        print('Failed')
        print('\nFAILED: read_data()')
        print('==================\n')
        
        return 0
    

def test_find_country() -> int:
    """Tests the find_country() function"""
    
    # Local variables
    test: int = 1
    inputs: list[list[str]]
    outputs: list[int]
    
    # Values
    inputs = [['HS1 1AB', 'HS2 2CD', 'HS3 3EF'],
              ['HS0 1AB', 'HS2 2CD', 'HS3 3EF'],
              ['HS0 1AB', 'HS2 2CD', 'HS0 3EF'],
              ['HS0 1AB', 'HS0 2CD', 'HS0 3EF']]
    outputs = [0, 1, 2, 3]
    
    print("\nfind_country() Tests")
    print("------------===-\n")
    
    try:
        
        for index in range(len(inputs)):
            
            print(f'Test {str(test)}: find_country({inputs[index]}) --> ', end="")
            
            assert find_country.find_country(inputs[index]) == outputs[index]
            
            print("Passed")
            
            test += 1
               
        print("\nPASSED: display_information()")
        print("==================\n")
        
        return 1
        
    except:
        
        print("Failed")
        print("\nFAILED: display_information()")
        print("==================\n")
        
        return 0


def test_write_summary() -> int:
    """Tests the writeSummary() function"""
    
    print('\nwriteSummary() Tests')
    print('--------------------\n')
    
    try:
        
        print('Test: writeSummary(' +
              '0, 1, 2, 1, 2, ["HS1 2AB", "HS7 5LQ", "HS9 5XD"], [1, 2, 2]' +
              ') --> ', end='')
        housePrices.writeSummary(0, 1, 2, 1, 2, ['HS1 2AB', 'HS7 5LQ', 'HS9 5XD'], [1, 2, 2])
        print('Written')
                     
        print('\nCompleted: writeSummary()')
        print('=========================\n')
        
        return 1
        
    except:
        print('Failed')
        print('\nFAILED: writeSummary()')
        print('===================\n')
        
        return 0



def testAll() -> None:
    '''Tests all functions'''
    
    # Local variable
    passed: int = 0
    
    print('\nRun All Tests')
    print('-------------\n')
    
    try:
        
        passed += test_read_data()
        passed += test_write_summary()
        
        if passed == 9:
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
    print('\nhousePrices Tests')
    print('--------------\n')

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
