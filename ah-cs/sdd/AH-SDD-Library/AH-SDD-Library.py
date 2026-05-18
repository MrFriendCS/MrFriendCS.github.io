# Title: AH SDD Library
# Author: Mr Friend
# Date: 17 May 2026


class Book:
    '''Declare a class to define a library book.'''
    
    def __init__(self, id=0, title='', author='', isBorrowed=False, date='', fine=0.5):
        '''Object constructor method. ''' \
        '''Automatically called when an object is created.'''
    
        # Class properties - Private
        self.__id = id
        self.__title = title
        self.__author = author
        self.__isBorrowed = isBorrowed
        self.__dateBorrowed = date
        self._finePerDay = fine
    
    def bookDetails(self):
        '''Method to display information about a book.'''
        
        # Local variables
        inLibrary = "No"
        date = self.__dateBorrowed
        
        print(f'ID: {self.__id}')
        print(f'Title: {self.__title}')
        print(f'Author: {self.__author}')
                
    def availability(self):
        '''Method to display the availability of a book.'''
        
        # Local variables
        inLibrary = "Yes"
        date = self.__dateBorrowed
        
        if self.__isBorrowed == True:
            inLibrary = "No"
        
        print(f'In library: {inLibrary}')
        
        if self.__isBorrowed == True:
            print(f'Date borrowed: {date}\n')
        
        
        
    def borrowBook(self):
        '''Method to borrow a book.'''
        
        # Get extra code
        from datetime import datetime
        
        # Local variables
        date = ''
        success = False
        
        # Get current date - Convert from date object to str
        date = datetime.now().strftime("%Y-%m-%d")
                
        # Check if book has already been borrowed
        if self.__isBorrowed == False:
            
            # Borrow the book
            self.__isBorrowed = True
            self.__dateBorrowed = date
            
            # Update success
            success = True
        
        return success
    
    def returnBook(self):
        '''Method to return a book.'''
            
        # Return the book
        self.__isBorrowed = False
        
    def calculateFine(self):
        '''Method to calculate the fine of a late book.'''
        
        # Local variable
        daysLate = 0
        
        # Get extra code
        from datetime import date, datetime
        
        # Get current date
        now = datetime.now().date()
        
        # Borrowed date - convert from str to date object
        dateBorrowed = date(int(self.__dateBorrowed[ :4]),
                            int(self.__dateBorrowed[5:7]),
                            int(self.__dateBorrowed[-2: ]))
        
        # Calculate days late
        daysLate = (now - dateBorrowed).days
        
        print(daysLate)
        
            
        
newBook = Book(1, 'Beowulf', 'Seumas Heaney')

newBook.bookDetails()

newBook.availability()

newBook.borrowBook()

newBook.availability()

newBook.calculateFine()
