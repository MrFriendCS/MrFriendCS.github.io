# Title: Testing Functions in functions.py
# Author: Mr Friend
# Date: 27 Sep 2025

# Get pupil functions to be tested
from functions import *

#
# Sub-programs
#


def testGradient():
    """Test the functionality of the gradient() function."""
    
    # Initialise variables
    failCount = 0
    inputs1 = [1, 10,   1,   54.3, 54.3]
    inputs2 = [0, 1,   -10,  10,   100]
    outputs = [-1, 10, -0.1, 5.43, 0.54]
    
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
                  str(inputs1[index]) + ", " +
                  str(inputs2[index]) + ") = " +
                  str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def testHypotenuse():
    """Test the functionality of the hypotenuse() function."""
    
    # Initialise variables
    failCount = 0
    inputs1 = [ 0,  1, 0.01, 1, 3, 4, 1,       0.2]
    inputs2 = [ 1,  0, 1,    0.01, 4, 3, 1,    0.2]
    outputs = [-1, -1, 1,    1,    5, 5, 1.41, 0.28]
    
    # Display function being tested
    print("\nTesting: hypotenuse() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert hypotenuse(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": hypotenuse(" +
                  str(inputs1[index]) + ", " +
                  str(inputs2[index]) + ") = " +
                  str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def testAreaCircle():
    """Test the stretch functionality of the areaCircle() function."""
    
    # Initialise variables
    failCount = 0
    inputs =  [ 0, 0.01, 0.5,  1,    5,     10]
    outputs = [-1, 0,    0.79, 3.14, 78.54, 314.15]
    
    # Display function being tested
    print("\nStretch tests: areaCircle() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert areaCircle(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": areaCircle(" +
                  str(inputs[index]) + ") = " +
                  str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")
        

def testAreaTriangle():
    """Test the functionality of the areaTriangle() function."""
    
    # Initialise variables
    failCount = 0
    inputs1 = [0,  1,  0.01, 1,    3, 4, 0.1,  0.25]
    inputs2 = [1,  0,  1,    0.01, 4, 3, 0.2,  0.3]
    outputs = [-1, -1, 0.01, 0.01, 6, 6, 0.01, 0.04]
    
    # Display function being tested
    print("\nTesting: areaTriangle() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert areaTriangle(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": areaTriangle(" +
                  str(inputs1[index]) + ", " +
                  str(inputs2[index]) + ") = " +
                  str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def testAreaSquare():
    """Test the stretch functionality of the areaSquare() function."""
    
    # Initialise variables
    failCount = 0
    inputs =  [ 0, 0.01, 1, 10,  0.5,  0.25]
    outputs = [-1, 0,    1, 100, 0.25, 0.06]
    
    # Display function being tested
    print("\nStretch tests: areaSquare() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert areaSquare(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": areaSquare(" +
                  str(inputs[index]) + ") = " +
                  str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testAreaRectangle():
    """Test the functionality of the areaRectangle() function."""
    
    # Initialise variables
    failCount = 0
    inputs1 = [ 0,  1, 0.01, 1,    3,  4,  0.1,  0.25]
    inputs2 = [ 1,  0, 1,    0.01, 4,  3,  0.2,  0.3]
    outputs = [-1, -1, 0.01, 0.01, 12, 12, 0.02, 0.07]
    
    # Display function being tested
    print("\nTesting: areaRectangle() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert areaRectangle(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": areaRectangle(" +
                  str(inputs1[index]) + ", " +
                  str(inputs2[index]) + ") = " +
                  str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def testVolPrism():
    """Test the functionality of the volPrism() function."""
    
    # Initialise variables
    failCount = 0
    inputs1 = [ 0,  1, 0.01, 1,    3,  4,  0.1,  0.25]
    inputs2 = [ 1,  0, 1,    0.01, 4,  3,  0.2,  0.3]
    outputs = [-1, -1, 0.01, 0.01, 12, 12, 0.02, 0.07]
    
    # Display function being tested
    print("\nTesting: volPrism() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert volPrism(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": volPrism(" +
                  str(inputs1[index]) + ", " +
                  str(inputs2[index]) + ") = " +
                  str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def testVolCone():
    """Test the functionality of the volCone() function."""
    
    # Initialise variables
    failCount = 0
    inputs1 = [ 0,  1, 0.01, 1,    1,    10,     1]
    inputs2 = [ 1,  0, 1,    0.01, 3,    30,     1]
    outputs = [-1, -1, 0,    0.01, 3.14, 3141.5, 1.05]
    
    # Display function being tested
    print("\nTesting: volCone() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert volCone(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": volCone(" +
                  str(inputs1[index]) + ", " +
                  str(inputs2[index]) + ") = " +
                  str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def testSphere():
    """Test the stretch functionality of the volSphere() function."""
    
    # Initialise variables
    failCount = 0
    inputs =  [ 0, 0.01, 1,    1,    5,      10]
    outputs = [-1, 0,    4.19, 4.19, 523.58, 4188.67]
    
    # Display function being tested
    print("\nStretch tests: volSphere() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert volSphere(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " +
                  str(index+1) + ": volSphere(" +
                  str(inputs[index]) + ") = " +
                  str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


#
# Main program
#

# Tests

testGradient()
testHypotenuse()

testAreaCircle()
testAreaTriangle()
testAreaSquare()
testAreaRectangle()

testVolPrism()
testVolCone()
testSphere()