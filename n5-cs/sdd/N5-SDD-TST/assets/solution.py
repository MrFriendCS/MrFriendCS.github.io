# Title: N5 SDD TST
# Author: Mr Friend
# Date: 3 Sep 2024

# Initalise variables
noOfTours = 0
noOfPassengers = 0
passengerType = ""
tourCost = 0
tourCosts = [0] * 4
totalCost = 0
averageCost = 0.0


# Display header
print("\n TST")
print("-----\n")

# Get valid number of tours
while noOfTours < 1 or noOfTours > 4:
    
    # Get number of tours
    noOfTours = int(input("Number of tours: "))
    
    # Check if valid
    if noOfTours < 1 or noOfTours > 4:
        
        # Error message
        print("\nInvalid:  Enter a value of 1 to 4")


#Loop for each tour
for index in range(noOfTours):

    # Get number of passengers
    while noOfPassengers < 1 or noOfPassengers > 5:
        
        # Get valid number of passengers
        noOfPassengers = int(input("\nNumber passengers on tour " +str(index+1) + ": "))
        
        # Check if valid
        if noOfPassengers < 1 or noOfPassengers > 5:
            
            # Error message
            print("\nInvalid:  Enter a value of 1 to 5")

    # Loop for each passenger
    for count in range(noOfPassengers):
    
        # Get valid passengers type
        while passengerType != "a" and  passengerType != "c":
            
            # Get passengers type
            passengerType = input("Tour " + str(index+1)
                                  + " passenger " + str(count+1) + " type: ")
            
            # Check if valid
            if passengerType != "a" and  passengerType != "c":
                
                # Error message
                print("\nInvalid: Enter a value of 'a' for addult or 'c' for child")

        # Is passenger an adult?
        if passengerType == "a":
            
            # Increase tour cost by £25
            tourCost = tourCost + 25
            
        else:
            
            # Increase tour cost by £15
            tourCost = tourCost + 15
            
        # Reset passengerType
        passengerType = ""
            
    # Store tour cost
    tourCosts[index] = tourCost
    
    # Reset tour cost
    tourCost = 0
    
    # Reset noOfPassangers
    noOfPassengers = 0


# Calculate total cost of tours
for index in range(noOfTours):
    
    # Update total cost
    totalCost = totalCost + tourCosts[index]

# Calculate average cost of tours
average = totalCost / noOfTours

# Round average to 2 dp
average = round(average, 2)

# Display header
print("\nTours")
print("-----\n")


# Display cost of tours
for index in range(noOfTours):
    
    print(str(index+1) + ": £" + str(tourCosts[index]))

# Display average cost of tours
print("\nAvg: £" + str(average))

# Display total cost of tours
print("Total: £" + str(totalCost))

# Display footer
print("===========\n")
