# Title: Locker Class Tests
# Author: Mr Friend
# Date: 25 May 2026


# Import Locker class
from Locker import Locker


def testLockUnlock() -> None:
    '''Test the lock() and unlock() methods.'''
    
    # Use global variables
    global testPassed
    global testFailed
    
    try:
        # Test: lock a locked locker
        assert testLocker.lock() == False
        
        print('Pass: lock() - locked locker')
        
        testPassed += 1

    except:
        
        print('Fail: lock() - locked locker')
        
        testFailed += 1


    try:
        # Test: unlock a locked locker
        assert testLocker.unlock() == True
        
        print('Pass: unlock() - locked locker')
        
        testPassed += 1

    except:
        
        print('Fail: unlock() - locked locker')
        
        testFailed += 1


    try:
        # Test: unlock an unlocked locker
        assert testLocker.unlock() == False
        
        print('Pass: unlock() - unlocked locker')
        
        testPassed += 1

    except:
        
        print('Fail: unlock() - unlocked locker')
        
        testFailed += 1


    try:
        # Test: lock an unlocked locker
        assert testLocker.lock() == True
        
        print('Pass: lock() - unlocked locker')
        
        testPassed += 1

    except:
        
        print('Fail: lock() - locked locker')
        
        testFailed += 1


def testDetails() -> None:
    '''Test the details() method.'''
    
    # Use global variables for assignment
    global testPassed
    global testFailed
    
    # Get locker details
    details = testLocker.details()
    
    try:
        
        # Test: locker number
        assert details[0] == lockerNo
        
        print('Pass: details() - locker name')
        
        testPassed += 1

    except:
        
        print('Fail: details() - locker name')
        
        testFailed += 1
    
    
    try:
        
        # Test: pupil name
        assert details[1] == pupilName
        
        print('Pass: details() - pupil name')
        
        testPassed += 1

    except:
        
        print('Fail: details() - pupil name')
        
        testFailed += 1
    
    
    try:
        
        # Test: locked status
        assert details[2] == True
        
        print('Pass: details() - locked status')
        
        testPassed += 1

    except:
        
        print('Fail: details() - locked status')
        
        testFailed += 1


def testAssign() -> None:
    '''Test the assign() method.'''
    
    # Use global variables for assignment
    global testPassed
    global testFailed
    
    # Local variable
    newPupil = 'A Pupil'
        
    #Assign locker
    testLocker.assign(newPupil)
    
    try:
              
        # Test: pupil name
        assert testLocker.details()[1] == newPupil
        
        print('Pass: details() - pupil name')
        
        testPassed += 1

    except:
        
        print('Fail: details() - pupil name')
        
        testFailed += 1
    
#
# Main program
#

# Global variables
testPassed = 0
testFailed = 0
lockerNo = 12
pupilName = 'Test'

# Create a locker
testLocker = Locker(lockerNo, pupilName)

# Display header
print('Locker Class Tests')
print('------------------\n')

# Run tests
testLockUnlock()
testDetails()
testAssign()

# Display results
print('\nResults')
print('-------')

print(f'Passed: {testPassed}')
print(f'Failed: {testFailed}')
