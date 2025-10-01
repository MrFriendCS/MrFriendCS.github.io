# Title: H SDD - Functions
# Author: Mr Friend
# Date: 1 Oct 2025


def gradient(dy, dx):
    """Calculates dy/dx, to 2 dp.  Returns the result.""" 
    
    # Initialise local variable
    gradient = 0.0
    
    # Check for invalid dx
    if dx == 0:
        
        # Set gradient to -1.0
        gradient = -1.0
        
    # If dx is valid
    else:
        
        # Calculate gradient
        gradient = dy / dx
        
        # Round gradient
        gradient = round(gradient, 2)
    
    # Return result
    return gradient


def hypotenuse(a, b):
    """Calculates the long side of a right angled triangle, to 2 dp.  Returns the result."""
    
    # Initialise local variable
    c = 0.0
    
    # Check for invalid a or b
    if a <= 0 or b <= 0:
        
        # Set c to -1.0
        c = -1.0
        
    # If a and b are valid
    else:
        
        # Calculate hypotenuse
        c = (a**2 + b**2)**0.5
        
        # Round hypotenuse
        c = round(c, 2)
    
    # Return result
    return c


def areaCircle(radius):
    """Calculates the area of a circle, to 2 dp.  Returns the result."""
    
    # Initialise local variables
    pi = 3.1415
    area = 0.0
    
    # Check for invalid radius
    if radius <= 0:
        
        # Set area to -1.0
        area = -1.0
        
    # If radius is valid
    else:
        
        # Calculate area
        area = pi * radius**2
        
        # Round area
        area = round(area, 2)
    
    # Return result
    return area


def areaTriangle(base, height):
    """Calculates the area of a triangle, to 2 dp.  Returns the result."""
    
    # Initialise local variable
    area = 0.0
    
    # Check for invalid base or height
    if base <= 0 or height <= 0:
        
        # Set area to -1.0
        area = -1.0
        
    # If base and height are valid
    else:
        
        # Calculate area
        area = 0.5 * base * height
        
        # Round area
        area = round(area, 2)
    
    # Return result
    return area


def areaSquare(side):
    """Calculates the area of a square, to 2 dp.  Returns the result."""
    
    # Initialise local variable
    area = 0.0
    
    # Check for invalid radius
    if side <= 0:
        
        # Set area to -1.0
        area = -1.0
        
    # If side is valid
    else:
        
        # Calculate area
        area = side**2
        
        # Round area
        area = round(area, 2)
    
    # Return result
    return area


def areaRectangle(width, height):
    """Calculates the area of a rectangle, to 2 dp.  Returns the result."""
    
    # Initialise local variable
    area = 0.0
    
    # Check for invalid width or height
    if width <= 0 or height <= 0:
        
        # Set area to -1.0
        area = -1.0
        
    # If base and height are valid
    else:
        
        # Calculate area
        area = width * height
        
        # Round area
        area = round(area, 2)
    
    # Return result
    return area


def volPrism(csa, height):
    """Calculates the volume of a prism, to 2 dp.  Returns the result."""
    
    # Initialise local variable
    volume = 0.0
    
    # Check for invalid csa or height
    if csa <= 0 or height <= 0:
        
        # Set volume to -1.0
        volume = -1.0
        
    # If csa and height are valid
    else:
        
        # Calculate volume
        volume = csa * height
        
        # Round volume
        volume = round(volume, 2)
    
    # Return result
    return volume


def volCylinder(radius, height):
    """Calculates the volume of a cylinder, to 2 dp.  Returns the result."""
        
    # Initialise local variable
    pi = 3.1415
    volume = 0.0
    
    # Check for invalid csa or height
    if radius <= 0 or height <= 0:
        
        # Set volume to -1.0
        volume = -1.0
        
    # If radius and height are valid
    else:
        
        # Calculate volume
        volume = pi * radius**2 * height
        
        # Round volume
        volume = round(volume, 2)
    
    # Return result
    return volume


def volCone(radius, height):
    """Calculates the volume of a cone, to 2 dp.  Returns the result."""

        
    # Initialise local variable
    pi = 3.1415
    volume = 0.0
    
    # Check for invalid radius or height
    if radius <= 0 or height <= 0:
        
        # Set volume to -1.0
        volume = -1.0
        
    # If radius and height are valid
    else:
        
        # Calculate volume
        volume = (1/3) * pi * radius**2 * height
        
        # Round volume
        volume = round(volume, 2)
    
    # Return result
    return volume


def volSphere(radius):
    """Calculates the volume of a sphere, to 2 dp.  Returns the result."""

    # Initialise local variable
    pi = 3.1415
    volume = 0.0
    
    # Check for invalid radius
    if radius <= 0:
        
        # Set volume to -1.0
        volume = -1.0
        
    # If radius and height are valid
    else:
        
        # Calculate volume
        volume = (4/3) * pi * radius**3
        
        # Round volume
        volume = round(volume, 2)
    
    # Return result
    return volume


def compoundInt(initial, rate, periods):
    """Calculates the compound interest, to 2 dp.  Returns the result."""
    
    # Initialise local variable
    final = 0.0
    interest = 0.0
    multiplier = 0.0
    
    # Check for invalid values
    if initial <= 0 or periods <= 0:
        
        # Set compound interest to -1.0
        interest = -1.0
    
    else:
        
        # Calculate multiplier
        multiplier = 1 + (rate / 100)
        
        # Calculate final amount
        final = initial * multiplier ** periods
        
        # Calculate compund interest
        interest = final - initial
        
        # Round compund interest to 2 dp
        interest = round(compoundInterest, 2)
    
    # Return result
    return interest
