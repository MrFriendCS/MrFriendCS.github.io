# Title: AH-SDD-Shape
# Author: 
# Date: 5 Jun 2026


class Shape:
    """A class to represent a shape."""
    
    def __init__(self, vertices:list):
        """Create a new shape."""
        
        self.__vertices = vertices
    
    def get_vertices(self) -> list[list[int]]:
        """Returns the vertices of the shape."""
        
        return self.__vertices
    
    def calc_perimeter(self) -> float:
        """Returns the perimeter of the shape."""
        
        # Local variables
        dy = 0.0
        dx = 0.0
        length = 0.0
        perimeter = 0.0
        
        # Loop for each vertice, except the last
        for index in range(len(self.__vertices)-1):
            
            # Get values
            dx = self.__vertices[index+1][0] \
                 - self.__vertices[index][0]
            dy = self.__vertices[index+1][1] \
                 - self.__vertices[index][1]
            
            # Calculate length
            length =(dx**2 + dy**2)**0.5
            
            # Update perimeter
            perimeter += length
        
        # Calculate length of last side# Get values
        dx = self.__vertices[len(self.__vertices)-1][0] \
             - self.__vertices[0][0]
        dy = self.__vertices[len(self.__vertices)-1][1] \
             - self.__vertices[0][1]
        
        # Calculate length
        length = (dx**2 + dy**2)**0.5
        
        # Update perimeter
        perimeter += length
        
        return perimeter
