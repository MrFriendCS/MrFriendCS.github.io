# Title: Order Class
# Author: Mr Friend
# Date: 29 May 2026


class Order:
    """A class for a canteen order."""  
    
    def __init__(self):
        """Create a new canteen order
           
           items  -- menu_items that have been added to the order (default [])
           status -- the status of the order (default 'In progress')
           """
    
        # Instance variables - Private
        self.__items = []
        self.__status = 'In progress'
    
    def add_item(self, item: MenuItem) -> None:
        """Method to add an item to the order."""
        
        self.__items += [item]
    
    def get_items(self) -> list[MenuItem]:
        """Method to access the menu items."""
        
        return self.__items
    
    def get_status(self) -> str:
        """Method to access the status of the order."""
        
        return self.__status
    
    def display_order(self) -> None:
        """Method to display the order."""
               
        # Loop for each item
        for item in self.__items:
            
            print(f'{item.get_name()} - £{item.get_price():.2f}')
    
    def calculate_cost(self) -> float:
        """Method to calculate the cost of the order."""
        
        # Local variable
        cost = 0.0
        
        # Loop for each item
        for item in self.__items:
            
            # Update cost
            cost = cost + item.get_price()
        
        return cost
    
    def complete_order(self) -> None:
        """Method to update the status of the order."""
            
        # Update status
        self.__status = 'Completed'
