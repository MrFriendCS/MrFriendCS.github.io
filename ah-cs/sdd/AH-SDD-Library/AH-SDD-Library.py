# Title: AH SDD Library
# Author: Mr Friend
# Date: 17 May 2026


class Book:
    '''Declare a class to define a library book.'''
    
    def __init__(self, id=0, title='', author='', borrowed=False, date=''):
        '''Object constructor method. ''' \
        '''Automatically called when an object is created.'''
    
        # Class properties - Private
        self.__id = id
        self.__title = title
        self.__author = author
        self.__loan = borrowed
        self.__dateBorrowed = date
    
    def bookDetails(self):
        '''Method to display information about a book.'''
        
        # Local variables
        inLibrary = "No"
        date = self.__dateBorrowed
        
        print(f'Book ID: {self.__id}')
        print(f'Title: {self.__title}')
        print(f'Author: {self.__author}\n')
                
    def available(self):
        '''Method to display the availability of a book.'''
        
        if self.__loan == True:
            
            print('The book has been borrowed.')
            print(f'Date borrowed: {self.__dateBorrowed}\n')
            
        else:
            
            print('The book is in the library\n')
            
    def borrowBook(self):
        '''Method to borrow a book.'''
        
        # Get extra code
        from datetime import datetime
        
        # Local variables
        date = ''
        success = False
        
        # Get current date - Convert from date object to str
        date = datetime.now().strftime('%Y-%m-%d')
                
        # Check if book has already been borrowed
        if self.__loan == False:
            
            # Borrow the book
            self.__loan = True
            self.__dateBorrowed = date
            
            # Update success
            success = True
        
        return success
    
    def returnBook(self):
        '''Method to return a book.'''
            
        # Return the book
        self.__loan = False
        
    def daysLeft(self):
        '''Method to check how late book a book is.'''
        
        # Check if book is on loan
        if self.__loan == True:
            
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
            daysLate = (now - dateBorrowed).days - 21
            
            if daysLate > 0:
                
                # Late
                print(f'Days late: {daysLate}\n')
                
            else:
                
                # Not late
                print(f'Days left: {abs(daysLate)}\n')
        
        else:
            
            # Not borrowed
            print('The book is in the library.\n')
    
    def setDateBorrowed(self, date=""):
        '''Method to calculate the modify the date ''' \
            + '''a book was borrowed.'''
        
        # Local variables
        success = False
        validDate = True
        
        if len(date) == 10:
        
            # Check date is valid
            for index in range(len(date)):
                
                ascii = ord(date[index])
                
                if index == 4 or index == 7:
                    
                    if ascii != 45:
                        
                        validDate = False
                
                elif ascii < 48 or ascii > 59:
                    
                    validDate = False
        
        else:
            
            validDate = False
        
        if validDate == True:
        
            # Update borrowed date
            self.__dateBorrowed = date
            
            # Update success
            success = True
        
        return success
        

        
newBook = Book(1, 'Beowulf', 'Seumas Heaney')

newBook.daysLeft()

newBook.bookDetails()

newBook.available()

newBook.borrowBook()

newBook.available()

newBook.daysLeft()

newBook.setDateBorrowed('2026-04-18')

newBook.daysLeft()
