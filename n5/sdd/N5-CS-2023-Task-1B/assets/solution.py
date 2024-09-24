# Title: N5 CS 2023 Task 1B
# Author: 
# Date: 5 Feb 2023

# Declare variable and arrays
startMiles = 0
stations = 0
currentMiles = 0
kwRating = 0
milesTravelled = 0
pricePerMile = 0.0
totalJourneyCost = 0.0
totalMiles = 0
journeyStage = [0.0] * 10
journeyMiles = [0] * 10  # Not shown in design

#
# Get journey details
#

# Get mileage at start of journey
startMiles = int(input("Enter the start mileage: "))

# Get number of charging stations
stations = int(input("Enter the number of charging stations: "))


#
# Calculate and store the cost of
#   each stage of the journey
#

# Loop for each charging station
for index in range(stations):

    # Get mileage at current charging station
    currentMiles = int(input("Enter the current mileage: "))

    # Get valid kW rating for current charging station
    kwRating = int(input("Enter the kW rating: "))
    
    while not (kwRating == 7 or kwRating ==22 or kwRating == 50):
        print("Enter a valid kW rating: 7, 22, or 50.")
        kwRating = int(input("Enter the kW rating: "))

    # Is kW rating = 7?
    if kwRating == 7:
        # Yes
        pricePerMile = 0
    # No - Is kW rating = 22?
    elif kwRating == 22:
        # Yes
        pricePerMile = 0.005
    else:
        # No
        pricePerMile = 0.01
        
    # Calculate and store milesTravelled
    milesTravelled = currentMiles - startMiles

    # Store new startMiles
    startMiles = currentMiles
    
    # Calculate and store cost of journeyStage
    journeyStage[index] = pricePerMile * milesTravelled

    # Store miles travelled - not in design
    journeyMiles[index] = milesTravelled


#
# Display total miles, journey stage costs and total cost
#

# Loop for each charging station
for index in range(stations):
    
    # Display next journeyStage
    print("Journey stage " + str(index + 1) + " cost = " + str(journeyStage[index]))

    # Calculate totalJourneyCost
    totalJourneyCost = totalJourneyCost + journeyStage[index]

    # Calculate totalMiles
    totalMiles = totalMiles + journeyMiles[index]

# Display totalJourneyCost rounded to 2 decimal places
print("Total cost = " + str(round(totalJourneyCost, 2)))

# Display totalMiles with message
print("Total miles = " + str(totalMiles))
