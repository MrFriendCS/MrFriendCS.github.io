# Title: Testing Functions in summmer1.py
# Author: Mr Friend
# Date: 23 Jun 2025

# Get functions to be tested
from summer1 import *

#
# Sub-programs
#

def testCircumference():
    """Test the functionality of the circumference() function."""
    
    # Initialise variable
    failCount = 0
    inputs1 = [0.5, 1, 10, 100,
               1, 10, 100, 0.5,
               0, -0.1, 1, 1]
    inputs2 = ["r", "r", "r", "r",
               "d", "d", "d", "d",
               "r", "r", "a", ""]
    outputs = [3.1415, 6.283, 62.83, 628.3,
               3.1415, 31.415, 314.15, 1.5708,
               0, -1.0, -1.0, -1.0]
    
    # Display function being tested
    print("\nTesting: circumference() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert circumference(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": circumference("
                  + str(inputs1[index]) + ", \"" + inputs2[index] + "\") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def stretchCircumference():
    """Test the stretch functionality of the circumference() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [1, 2, 20, 200, -0.1]
    outputs = [3.1415, 6.283, 62.83, 628.3, -1.0]
    
    # Display function being tested
    print("\nStretch tests: circumference() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert circumference(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": circumference("
                  + str(inputs[index]) + ") = " + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testRadius():
    """Test the functionality of the radius() function."""
    
    # Initialise variable
    failCount = 0
    inputs1 = [1, 2, 20, 100,
               3.1415, 25.132, 1, 2,
               0, -0.1, 1, 1]
    inputs2 = ["d", "d", "d", "d",
               "c", "c", "c", "c",
               "d", "d", "a", ""]
    outputs = [0.5, 1.0, 10.0, 50,
               0.5, 4, 0.1592, 0.3183,
               0.0, -1.0, -1.0, -1.0]
    
    # Display function being tested
    print("\nTesting: radius() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert radius(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": radius("
                  + str(inputs1[index]) + ", \"" + inputs2[index] + "\") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def stretchRadius():
    """Test the stretch functionality of the radius() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [1, 2, 0.001, 0.0001, -0.1]
    outputs = [0.5, 1.0, 0.0005, 0.0001, -1.0]
    
    # Display function being tested
    print("\nStretch tests: radius() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert radius(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": radius("
                  + str(inputs[index]) + ") = " + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testDiameter():
    """Test the functionality of the diameter() function."""
    
    # Initialise variable
    failCount = 0
    inputs1 = [1, 2, 20, 100,
               3.1415, 6.283, 1, 0.5,
               0, -0.1, 1, 1]
    inputs2 = ["r", "r", "r", "r",
               "c", "c", "c", "c",
               "r", "d", "a", ""]
    outputs = [2.0, 4.0, 40.0, 200.0,
               1.0, 2.0, 0.3183, 0.1592,
               0.0, -1.0, -1.0, -1.0]
    
    # Display function being tested
    print("\nTesting: diameter() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert diameter(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": diameter("
                  + str(inputs1[index]) + ", \"" + inputs2[index] + "\") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def stretchDiameter():
    """Test the stretch functionality of the diameter() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [1, 2, 0.0001, 0.000025, -0.1]
    outputs = [2.0, 4.0, 0.0002, 0.0001, -1.0]
    
    # Display function being tested
    print("\nStretch tests: diameter() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert diameter(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": diameter("
                  + str(inputs[index]) + ") = " + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


def testArea():
    """Test the functionality of the area() function."""
    
    # Initialise variable
    failCount = 0
    inputs1 = [1, 2, 40, 0.5,
               1, 2, 40, 0.5,
               3.1415, 6.283, 31.415, 1.5708,
               0, -0.1, 1, 1]
    inputs2 = ["r", "r", "r", "r",
               "d", "d", "d", "d",
               "c", "c", "c", "c",
               "d", "d", "a", ""]
    outputs = [3.1415, 12.566, 5026.4, 0.7854,
               0.7854, 3.1415, 1256.6, 0.1963,
               0.7854, 3.1415, 78.5375, 0.1964,
               0.0, -1.0, -1.0, -1.0]
    
    # Display function being tested
    print("\nTesting: area() function")

    # Loop through tests
    for index in range(len(inputs1)):
        
        try:
            
            assert area(inputs1[index], inputs2[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": area("
                  + str(inputs1[index]) + ", \"" + inputs2[index] + "\") = "
                  + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs1)) + " tests passed.")


def stretchArea():
    """Test the stretch functionality of the area() function."""
    
    # Initialise variable
    failCount = 0
    inputs = [1, 2, 40, 0.5, -0.1]
    outputs = [3.1415, 12.566, 5026.4, 0.7854, -1.0]
    
    # Display function being tested
    print("\nStretch tests: area() function")

    # Loop through tests
    for index in range(len(inputs)):
        
        try:
            
            assert area(inputs[index]) == outputs[index]
            
        except:
            
            # Increment failure count
            failCount = failCount + 1
            
            # Display failure message
            print("\tFailed Test " + str(index+1) + ": area("
                  + str(inputs[index]) + ") = " + str(outputs[index]))
    
    # Display success message
    if failCount == 0:
        
        print("\tAll " + str(len(inputs)) + " tests passed.")


#
# Main program
#

# Circumference tests
testCircumference()
stretchCircumference()

# Radius tests
testRadius()
stretchRadius()

# Diameter tests
testDiameter()
stretchDiameter()

# Area tests
testArea()
stretchArea()
