# Title: Menu Item Class
# Author: Mr Friend
# Date: 29 May 2026


class MenuItem:
    """A class to define a menu item. """    
    
    def __init__(self, name: str='', price: float=0.0):
        """Create a menu item.
           
           name  -- what it is, i.e. 'Cheese toastie' (default '')
           price -- how much it costs (default 0.0)
           """
    
        # Instance variables - Private
        self.__name = name
        self.__price = price
    
    def get_name(self) -> str:
        """A method to access the name of a menu item."""
        
        return self.__name
    
    def set_name(self, new_name: str='') -> None:
        """A method to update the name of a menu item."""
        
        self.__name = new_name
    
    def get_price(self) -> float:
        """A method to access the price of a menu item."""
        
        return self.__price
    
    def set_price(self, new_price: float=0.0) -> bool:
        """A method to update the price of a menu item."""
        
        # Local variable
        success = False
        
        # Chack validity of price:
        if new_price >= 0.0:
            
            # Update price
            self.__price = new_price
            
            success = True
        
        return success
