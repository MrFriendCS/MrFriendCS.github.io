# Title: H SDD Walking
# Author: 
# Date: 


def getData() -> list[float]:
    """Get the walking distances of four weeks."""
    
    # Local variables
    distance: float = 0.0
    distances: list[float] = [0.0] * 4
    
    
    
    # End function
    return distances


def calcTotal(distances: list[float]) -> float:
    """Calculate the total distance walked."""
    
    # Local variable
    total: float = 0.0
    
    
    
    # End function
    return total


def calcAverage(total: float) -> float:
    """Calculate the average distance walked."""
    
    # Local variable
    average: float = 0.0
    
    
    
    # End function
    return average


def writeData(distances: list[float], total: float,
              average: float) -> None:
    """Write the results to a file."""
    
    

#
# Main Program
#


# Global variables
distances: list = [0.0] * 4
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
