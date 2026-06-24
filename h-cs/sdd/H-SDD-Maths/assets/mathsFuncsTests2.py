# Title: Testing Functions in mathsFuncs.py
# Author: Mr Friend
# Date: 22 Jun 2026

# Get pupil functions to be tested
from mathsFuncs import *

#
# Sub-programs
#


def testR2D() -> None:
    """Test the functionality of the r2d() function."""
    
    # Initialise variables
    failCount = 0
    inputs = [20, 10, 5, 2.5, 1.2]
    outputs = [40.0, 20.0, 10.0, 5.0, 2.4]
    
    # Display function being tested
    print("\nTesting: r2d() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert r2d(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": r2d("
                  + str(inputs[index]) + ") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testD2R() -> None:
    """Test the functionality of the d2r() function."""
    
    # Initialise variables
    failCount = 0
    inputs = [20, 10, 5, 2.4, 1.2]
    outputs = [10.0, 5.0, 2.5, 1.2, 0.6]
    
    # Display function being tested
    print("\nTesting: d2r() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert d2r(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": d2r("
                  + str(inputs[index]) + ") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testCircumference() -> None:
    """Test the functionality of the circumference() function."""
    
    # Initialise variables
    failCount = 0
    inputs = [1, 10, 100]
    outputs = [3.14, 31.42, 314.15]
    
    # Display function being tested
    print("\nTesting: circumference() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert round(circumference(inputs[index]), 2) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": circumference("
                  + str(inputs[index]) + ") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testAreaOfCircle() -> None:
    """Test the functionality of the areaOfCircle() function."""
    
    # Initialise variables
    failCount = 0
    inputs =  [ 0, 0.01, 0.5,  1,    5,     10]
    outputs = [0, 0,    0.79, 3.14, 78.54, 314.15]
    
    # Display function being tested
    print("\nTesting: areaOfCircle() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert round(areaOfCircle(inputs[index]), 2) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": areaOfCircle("
                  + str(inputs[index]) + ") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")
        

def testAreaOfTriangle() -> None:
    """Test the functionality of the areaOfTriangle() function."""
    
    # Initialise variables
    failCount = 0
    inputs1 = [0,  1,  0.01, 1,    3, 4, 0.1,  0.25]
    inputs2 = [1,  0,  1,    0.01, 4, 3, 0.2,  0.3]
    outputs = [0, 0, 0.01, 0.01, 6, 6, 0.01, 0.04]
    
    # Display function being tested
    print("\nTesting: areaOfTriangle() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert round(areaOfTriangle(inputs1[index], inputs2[index]), 2) \
                   == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": areaOfTriangle(" +
                  str(inputs1[index]) + ", "
                  + str(inputs2[index]) + ") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def testVolOfSphere() -> None:
    """Test the functionality of the volOfSphere() function."""
    
    # Initialise variables
    failCount = 0
    inputs =  [0.01, 1,    5,      10]
    outputs = [0,   4.19, 523.58, 4188.67]
    
    # Display function being tested
    print("\nTesting: volOfSphere() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert round(volOfSphere(inputs[index]), 2) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": volOfSphere("
                  + str(inputs[index]) + ") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testGradient() -> None:
    """Test the functionality of the gradient() function."""
    
    # Initialise variables
    failCount = 0
    inputs1 = [[0, 0], [0, 5],]
    inputs2 = [[5, 5], [5, 0],]
    outputs = [1, -1]
    
    # Display function being tested
    print("\nTesting: gradient() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert gradient(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": gradient(" +
                  str(inputs1[index]) + ", "
                  + str(inputs2[index]) + ") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


#
# Main program
#
def main() -> None:
    
    # Tests
    testR2D()
    testD2R()
    testCircumference()
    testAreaOfCircle()
    testAreaOfTriangle()
    testVolOfSphere()
    testGradient()


main()