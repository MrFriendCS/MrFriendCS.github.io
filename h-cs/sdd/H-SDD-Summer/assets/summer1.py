# Title: H-SDD-Summer Part 1
# Author: Mr Friend
# Date: 24 Jun 2026

#
# Sub-programs
#


def getRadius() -> float:
    """Get a valid radius."""
    
    # Local variable
    r: float = 0.0
    
    # Header
    print("Radius Fun")
    print("----------")
    
    # Get valid radius from user
    while r <= 0.0:
        
        # Get radius
        r = float(input("\nEnter the radius: "))
        
        # Check rdius
        if r <= 0.0:
            
            # Display error message
            print("The rdius must be more than zero.")
    
    # End function
    return r


def calcDiameter(r: float) -> float:
    """Calculate the diameter of a circle to
       2 dp using the radius.
       """
    
    # Local variable
    d: float = 0.0
    
    # Calculate the diameter
    d = r * 2
    
    # Round to 2 dp
    d = round(d, 2)
        
    # End function
    return d


def calcCircumference(r: float) -> float:
    """Calculate the circumference of a circle to
       2 dp using the radius.
       """
    
    # Local variables
    PI: float = 3.1415
    c: float = 0.0
    
    # Calculate the circumference
    c = 2 * PI * r
    
    # Round to 2 dp
    c = round(c, 2)
            
    # End function
    return c


def calcArea(r: float) -> float:
    """Calculate the area of a circle to
       2 dp using the radius.
       """
    
    # Local variables
    PI: float = 3.1415
    area: float = 0.0
    
    # Calculate the area
    area = PI * r**2
    
    # Round to 2 dp
    area = round(area, 2)
            
    # End function
    return area


def calcVolume(r: float) -> float:
    """Calculate the volume of a sphere to
       2 dp using the radius.
       """
    
    # Local variables
    PI: float = 3.1415
    vol: float = 0.0
    
    # Calculate the volume
    vol = (4/3) * PI * r**3
    
    # Round to 2 dp
    vol = round(vol, 2)
            
    # End function
    return vol


def writeResults(r: float, d: float, c: float,
                 area: float, vol: float) -> None:
    """Write the results to a file."""
    
    # Connect to the file
    file = open("radiusFun.txt", "w", encoding="utf-8")
    
    # Write header
    file.write("Radius Fun Results\n")
    file.write("------------------\n\n")
    
    # Write radius
    file.write("Radius: " + str(r) + "\n")
    
    # Write diameter
    file.write("Diameter: " + str(d) + "\n")
    
    # Write circumference
    file.write("Circumference: " + str(c) + "\n")
    
    # Write area
    file.write("Area of circle: " + str(area) + "\n")
    
    # Write volume
    file.write("Volume of sphere: " + str(vol) + "\n")
    
    # Footer
    file.write("\n==================\n")
    
    # Close connection to file
    file.close()


#
# Main Program
#

# Global variables
r: float = 0.0
d: float = 0.0
c: float = 0.0
area: float = 0.0
vol: float = 0.0

# Get valid radius
r = getRadius()

# Calculate diameter
d = calcDiameter(r)

# Calculate circumference
c = calcCircumference(r)

# Calculate area of circle
area = calcArea(r)

# Calculate volume of sphere
vol = calcVolume(r)

# Write results to file
writeResults(r, d, c, area, vol)

