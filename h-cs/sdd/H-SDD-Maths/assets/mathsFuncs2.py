# Title: H SDD Math Functions
# Author: Mr Friend
# Date: 18 Jun 2026


def r2d(r: float) -> float:
    """Calculates the diameter from a radius."""
    
    # Local variable
    d: float = 0.0
    
    # Calculate diameter
    d = r * 2
    
    return d


def d2r(d: float) -> float:
    """Calculates the radius from a diameter."""
    
    # Local variable
    r: float = 0.0
    
    # Calculate diameter
    r = d / 2
    
    return r


def circumference(d: float) -> float:
    """Calculates the circumference from a diameter."""
    
    # Local variables
    pi: float = 3.1415
    c: float = 0.0
    
    # Calculate diameter
    c = pi * d
    
    return c


def areaOfCircle(r: float) -> float:
    """Calculates the area of a circle from a radius."""
    
    # Local variables
    pi: float = 3.1415
    area: float = 0.0
    
    # Calculate area
    area = pi * r**2
    
    return area


def areaOfTriangle(base: float, height: float) -> float:
    """Calculates the area of a triangle from the base and height."""
    
    # Local variables
    area: float = 0.0
    
    # Calculate area
    area = 0.5 * base * height
    
    return area


def volOfSphere(r: float) -> float:
    """Calculates the volume of a sphere from a radius."""
    
    # Local variables
    pi: float = 3.1415
    vol: float = 0.0
    
    # Calculate volume
    vol = (4/3) * pi * r**3
    
    return vol


def gradient(coord1: list[float], coord2: list[float]) -> float:
    """Calculates the gradient of a straight line
       from two coordinates.
       """
    
    # Local variables
    dy: float = 0.0
    dx: float = 0.0
    m: float = 0.0
    
    # Calculate dy
    dy = coord2[1] - coord1[1]
    
    # Calculate dx
    dx = coord2[0] - coord1[0]
    
    # Calculate gradient
    m = dy / dx
    
    return m
