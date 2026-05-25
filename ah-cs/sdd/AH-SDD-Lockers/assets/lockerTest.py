# Title: Locker Class Tests
# Author: Mr Friend
# Date: 25 May 2026


# Import Locker class
from Locker import Locker

# Global variables
testPassed = 0
testFailed = 0

# Create a locker
testLocker = Locker()

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
    assert testLocker.lock() == False
    
    print('Pass: lock() - unlocked locker')
    
    testPassed += 1

except:
    
    print('Fail: lock() - locked locker')
    
    testFailed += 1


# Display results
print('\nResults')
print('-------')

print(f'Passed: {testPassed}')
print(f'Failed: {testFailed}')