# Title: Locker Class Tests
# Author: Mr Friend
# Date: 29 May 2026


# Import Locker class
from Locker import Locker


def test_lock_unlock() -> None:
    """Test the lock() and unlock() methods."""
    
    # Use global variables
    global test_passed
    global test_failed
    
    try:
        # Test: lock a locked locker
        assert test_locker.lock() == False
        
        print('Pass: lock() - locked locker')
        
        test_passed += 1

    except:
        
        print('Fail: lock() - locked locker')
        
        test_failed += 1


    try:
        # Test: unlock a locked locker
        assert test_locker.unlock() == True
        
        print('Pass: unlock() - locked locker')
        
        test_passed += 1

    except:
        
        print('Fail: unlock() - locked locker')
        
        test_failed += 1


    try:
        # Test: unlock an unlocked locker
        assert test_locker.unlock() == False
        
        print('Pass: unlock() - unlocked locker')
        
        test_passed += 1

    except:
        
        print('Fail: unlock() - unlocked locker')
        
        test_failed += 1


    try:
        # Test: lock an unlocked locker
        assert test_locker.lock() == True
        
        print('Pass: lock() - unlocked locker')
        
        test_passed += 1

    except:
        
        print('Fail: lock() - locked locker')
        
        test_failed += 1


def test_details() -> None:
    """Test the details() method."""
    
    # Use global variables for assignment
    global test_passed
    global test_failed
    
    # Get locker details
    details = test_locker.details()
    
    try:
        
        # Test: locker number
        assert details[0] == locker_no
        
        print('Pass: details() - locker name')
        
        test_passed += 1

    except:
        
        print('Fail: details() - locker name')
        
        test_failed += 1
    
    
    try:
        
        # Test: pupil name
        assert details[1] == pupil_name
        
        print('Pass: details() - pupil name')
        
        test_passed += 1

    except:
        
        print('Fail: details() - pupil name')
        
        test_failed += 1
    
    
    try:
        
        # Test: locked status
        assert details[2] == True
        
        print('Pass: details() - locked status')
        
        test_passed += 1

    except:
        
        print('Fail: details() - locked status')
        
        test_failed += 1


def test_assign() -> None:
    """Test the assign() method."""
    
    # Use global variables for assignment
    global test_passed
    global test_failed
    
    # Local variable
    new_pupil = 'A Pupil'
        
    #Assign locker
    test_locker.assign(new_pupil)
    
    try:
              
        # Test: pupil name
        assert test_locker.details()[1] == new_pupil
        
        print('Pass: details() - pupil name')
        
        test_passed += 1

    except:
        
        print('Fail: details() - pupil name')
        
        test_failed += 1
    
#
# Main program
#

# Global variables
test_passed = 0
test_failed = 0
locker_no = 12
pupil_name = 'Test'

# Create a locker
test_locker = Locker(locker_no, pupil_name)

# Display header
print('Locker Class Tests')
print('------------------\n')

# Run tests
test_lock_unlock()
test_details()
test_assign()

# Display results
print('\nResults')
print('-------')

print(f'Passed: {test_passed}')
print(f'Failed: {test_failed}')
