# Title: H-SDD-Summer Part 1
# Author: Mr Friend
# Date: 23 Jun 2025

#
# Sub-programs
#


def circumference(size, rd="d"):
    """Calculate the circumference of a circle using the radius or diameter.  Returns the circumference to 4 dp."""
    
    # Local variables
    PI = 3.1415
    c = 0.0
    
    # Check if values are valid
    if size >= 0 and (rd == "r" or rd == "d"):
        
        # Check if radius being used
        if rd == "r":
            
            # Convert radius to diameter
            size = size * 2
        
        # Calculate circumference and round to 4 dp
        c = round(PI * size, 4)
        
    #
    else:
        
        # Set c to error values
        c = -1.0
    
    # Return circumference
    return c


def radius(size, dc="d"):
    """Calculate the radius of a circle using the diameter or circumference.  Returns the radius to 4 dp."""
    
    # Local variables
    PI = 3.1415
    r = 0.0
    
    # Check if values are valid
    if size >= 0 and (dc == "d" or dc == "c"):
        
        # Check if circumference being used
        if dc == "c":
            
            # Convert circumference to diameter
            size = size / PI
        
        # Calculate radius and round to 4 dp
        r = round(size / 2, 4)
        
    #
    else:
        
        # Set r to error values
        r = -1.0
        
    # Return radius
    return r


def diameter(size, rc="r"):
    """Calculate the diameter of a circle using the radius or circumference.  Returns the diameter to 4 dp."""
    
    # Local variables
    PI = 3.1415
    d = 0.0
    
    # Check if values are valid
    if size >= 0 and (rc == "r" or rc == "c"):
        
        # Check if circumference being used
        if rc == "c":
            
            # Convert circumference to diameter
            d = round(size / PI, 4)
        
        else:
            # Convert radius to diameter
            d = size * 2.0

        # Round to 4 dp
        d = round(d, 4)
        
    #
    else:
        
        # Set d to error values
        d = -1.0
        
    # Return diameter
    return d


def area(size, rdc="r"):
    """Calculate the area of a circle using the radius, diameter, or circumference.  Returns the area to 4 dp."""
    
    # Local variables
    PI = 3.1415
    a = 0.0
    
    # Check if values are valid
    if size >= 0 and (rdc == "r" or rdc == "d" or rdc == "c"):
        
        # Check if diameter being used
        if rdc == "d":
            
            # Convert diameter to radius
            size = size / 2
        
        # Check if curcumference being used
        elif rdc == "c":
            
            # Convert diameter to radius
            size = size / (2 * PI)
            
        # Calculate area and round to 4 dp
        a = round(PI * size**2, 4)
        
    #
    else:
        
        # Set a to error values
        a = -1.0
        
    # Return area
    return a

