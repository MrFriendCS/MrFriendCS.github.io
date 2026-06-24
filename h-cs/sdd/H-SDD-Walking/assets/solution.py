# Title: H SDD Walking
# Author: Mr Friend
# Date: 24 Jun 2026


def getData() -> list[float]:
    """Get the walking distances of four weeks."""
    
    # Local variables
    distance: float = 0.0
    distances: list[float] = [0.0] * 4

    # Message
    print("Enter the distance walked each week:\n")

    # Loop for each week
    for index in range(len(distances)):
        
        # Get distance walked
        distance = float(input("Week " + str(index+1) + ": "))
        
        # Re-enter if invalid
        while distance < 0:
            # Error message
            print("\nDistance must be 0 or more")
        
            # Get distance walked
            distance = float(input("Week " + str(index+1) + ": "))
            
        # Store distance
        distances[index] = distance
    
    # End function
    return distances


def calcTotal(distances: list[float]) -> float:
    """Calculate the total distance walked."""
    
    # Local variable
    total: float = 0.0

    # loop for each distance
    for distance in distances:
        
        # Increase total
        total = total + distance
    
    # End function
    return total


def calcAverage(total: float) -> float:
    """Calculate the average distance walked."""
    
    # Local variable
    average: float = 0.0
    
    # Calculate the average distance to 1 dp
    average = round(total / 4, 1)
    
    # End function
    return average


def writeData(distances: list[float], total: float,
              average: float) -> None:
    """Write the results to a file."""
    
    # Connect to the file
    file = open("walking.txt", "w", encoding="utf-8")
    
    # Write header
    file.write("Walking Results - 4 Weeks\n")
    file.write("-------------------------\n\n")
    
    # Write distances
    for index in range(len(distances)):
        
        file.write("Week " + str(index+1) + ": "
                   + str(distances[index]) + "\n")
    
    # Write total distance
    file.write("\nTotal: " + str(total) + " miles\n")
    
    # Write average distance
    file.write("\nAverage: " + str(average) + " miles (1 dp)\n")
    
    # Close connection to file
    file.close()
    

#
# Main Program
#


# Global variables
distances: list[float] = [0.0] * 4
total: float = 0.0
average: float = 0.0

# Get data
distances = getData()

# Calculate total distance walked
total = calcTotal(distances)

# Calculate average distance walked
average = calcAverage(total)

# Create results file
writeData(distances, total, average)
