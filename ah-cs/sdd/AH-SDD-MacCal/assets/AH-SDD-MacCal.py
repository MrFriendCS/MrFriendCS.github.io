# Title: AH SDD MacCal
# Author: Mr Friend
# Date: 17 May 2026


class Sailing:
    '''Declare a class to define a sailing.'''
    
    def __init__(self, id=0, date='', time='', depart='', arrive='', \
                 duration=0, passengers=0, cars=0):
        '''Constructor method. ''' \
        '''Automatically called when an object is created.'''
    
        # Class properties - Private
        self.__id = id
        self.__date = date
        self.__time = time
        self.__pod = depart
        self.__poa = arrive
        self.__duration = duration
        self.__pax = passengers
        self.__cars = cars
    
    def status(self):
        '''Method to display the status of a sailing.'''
            
        # Display status message
        print(f'Sailing: {self.__id}')
        print(f'Date: {self.__date}')
        print(f'Time: {self.__time}')
        print(f'From: {self.__pod}')
        print(f'To: {self.__poa}')
        print(f'Duration: {self.__duration}')
        print(f'Passengers: {self.__passengers}')
        print(f'Cars: {self.__cars}')
        
"""  
    def arrival(self):
        '''Method to calculate the arrival time.'''
        
        # Update locked status
        self.__isLocked = False
            
        # Display message
        print(f'Locker {self.__id} has been unlocked.\n')
"""           
    def passengerTicket(self, noOfPax=1):
        '''Method to update passenger numbers.'''
        
        # Local variable
        success = False
        
        # Can tickets be sold
        if self.__pax - noOfPax <= 50:
            
            # Update number of passengers
            self.__pax = self.__pax - noOfPax
            
            # Update success
            success = True
        
        return success
    
    def carTicket(self, noOfCars=1):
        '''Method to update car numbers.'''
        
        # Local variable
        success = False
        
        # Can tickets be sold
        if self.__cars - noOfPax <= 10:
            
            # Update number of passengers
            self.__cars = self.__cars - noOfCars
            
            # Update success
            success = True
        
        return success
