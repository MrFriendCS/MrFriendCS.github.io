# Title: Testing Functions in standard.py
# Author: Mr Friend
# Date: 24 Jun 2025

# Get functions to be tested
from standard import *

#
# Sub-programs
#

def testSearch():
    """Test the functionality of the search() function."""
    
    # Initialise local variables
    failCount = 0
    
    values1 = [66.8, 67.4, 83.2, 5.4, 46.8, 60.5]
    values2 = ["A", "S", "A", "J", "K", "C", "D"]
    values3 = ["Campbell", "Ford", "MacDonald", "Smyth", "Young", "Robertson"]
    values4 = [17, 14, 16, 17, 13, 14, 12]
    
    inputs1 = [values1, values2, values3, values4]
    inputs2 = [66.8, "J", "Robertson", 11]
    outputs = [True, True, True, False]
    
    # Display function being tested
    print("\nTesting: search() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert search(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": search("
                  + str(inputs1[index]) + ", \"" + str(inputs2[index]) + "\") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def testFindMin():
    """Test the functionality of the findMin() function."""
    
    # Initialise local variables
    failCount = 0
    
    values1 = [66.8, 67.4, 83.2, 5.4, 46.8, 60.5]
    values2 = ["A", "S", "A", "J", "K", "C", "D"]
    values3 = ["Ford", "MacDonald", "Smyth", "Young", "Robertson", "Campbell"]
    values4 = [17, 14, 16, 17, 13, 14, 12]
    
    inputs = [values1, values2, values3, values4]
    outputs = [5.4, "A", "Campbell", 12]
    
    # Display function being tested
    print("\nTesting: findMin() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert findMin(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": findMin("
                  + str(inputs[index])  + ") = " + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testFindMax():
    """Test the functionality of the findMax() function."""
    
    # Initialise local variables
    failCount = 0
    
    values1 = [83.2, 67.4, 66.8, 5.4, 46.8, 60.5]
    values2 = ["A", "D", "A", "J", "K", "C", "S"]
    values3 = ["Ford", "MacDonald", "Smyth", "Young", "Robertson", "Campbell"]
    values4 = [17, 14, 16, 17, 13, 14, 12]
    
    inputs = [values1, values2, values3, values4]
    outputs = [83.2, "S", "Young", 17]
    
    # Display function being tested
    print("\nTesting: findMax() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert findMax(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": findMax("
                  + str(inputs[index])  + ") = " + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testCount():
    """Test the functionality of the count() function."""
    
    # Initialise local variables
    failCount = 0
    
    values1 = [66.8, 67.4, 83.2, 5.4, 46.8, 60.5]
    values2 = ["J", "S", "A", "J", "K", "C", "J"]
    values3 = ["Campbell", "Ford", "MacDonald", "Smyth", "Young", "Robertson"]
    values4 = [17, 14, 16, 17, 13, 14, 12]
    
    inputs1 = [values1, values2, values3, values4]
    inputs2 = [66.8, "J", "Robertson", 11]
    outputs = [1, 3, 1, 0]
    
    # Display function being tested
    print("\nTesting: count() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert count(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": count("
                  + str(inputs1[index]) + ", \"" + str(inputs2[index]) + "\") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


#
# Main program
#

# Tests
testSearch()
testFindMin()
testFindMax()
testCount()
