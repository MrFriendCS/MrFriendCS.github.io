# Title: Create Hotel Tables
# Author: Mr Friend
# Date: 3 Oct 2024

# Import extra code
import sys

# Determine where the DDDhelper file is
shool = "C:\\Users\\afriend1r\\AppData\\Local\\Programs\\Thonny"

start1 = "C:\\Users\\afriend1r"
start2 = "D:"

end = "\\OneDrive - Glow Scotland\\GitHub\\MrFriendCS.github.io"

# Check if directory exists
if shool in sys.path:
    # School laptop
    sys.path.append(start1 + end)
    
else:
    # Personel laptop
    sys.path.append(start2 + end)


# Get extra code
import DDDhelper
from dataclasses import dataclass


@dataclass
class Customer:
    """A record to represent a hotel customer."""
    custNo: int = 0
    firstName: str = ""
    lastName: str = ""
    phone: str = ""
    email: str = ""
    

@dataclass
class Booking:
    """A record to represent a hotel booking."""
    reservation: int = 0
    arrive: str = ""
    nights: int = 0
    ppn: float = 0.0
    prepaid: bool = False
    custNo: int = 0


def createCustomers(count):
    """Create customer data and table."""
    
    customers = [Customer() for i in range(count)]

    fileOut = open("..\\Customer.sql", "w")

    # Create table

    table = """CREATE TABLE Customer (
        custNo INT NOT NULL,
        firstName VARCHAR(20),
        lastName VARCHAR(30),
        phone VARCHAR(11) NOT NULL
            CHECK(LENGTH(phone) = 11),
        email VARCHAR(30),
        PRIMARY KEY (custNo)
    );"""
    
    fileOut.write(table + "\n\n")
    
    
    # Create data

    for index in range(len(customers)):
        
        firstName = DDDhelper.getForename()
        lastName = DDDhelper.getSurname()
        
        customers[index].custNo = index + 1
        customers[index].firstName = firstName
        customers[index].lastName = lastName
        customers[index].phone = DDDhelper.getPhone()
        customers[index].email = DDDhelper.getEmail(firstName, lastName)
    
    
    # Insert data
    
    for index in range(len(customers)):
        
        fileOut.write("INSERT INTO Customer VALUES ")
        fileOut.write("(")
        fileOut.write(    str(customers[index].custNo) + ",")
        fileOut.write( "\"" + customers[index].firstName + "\",")
        fileOut.write( "\"" + customers[index].lastName + "\",")
        fileOut.write( "\"" + customers[index].phone + "\",")
        
        if customers[index].email != "":
            fileOut.write( "\"" + customers[index].email + "\");\n")
        else:
            fileOut.write("NULL);\n")

    fileOut.close()


def createBookings(count):
    """Create booking data and table."""  
    
    bookings = [Booking() for i in range(count)]
    
    fileOut = open("../Booking.sql", "w")
    
    # Create table

    table = """CREATE TABLE booking (
        reservation INT NOT NULL,
        arrive DATE NOT NULL,
        nights INT NOT NULL CHECK(nights >= 1),
        ppn REAL NOT NULL CHECK (ppn >= 50),
        prepaid BOOL,
        custNo INT NOT NULL,
        FOREIGN KEY (custNo)
            REFERENCES Customer (custNo),
        PRIMARY KEY (reservation)
    );"""

    fileOut.write(table + "\n\n")
    
    
    # Create data

    for index in range(len(bookings)):
        
        bookings[index].reservation = 750 + index
        bookings[index].arrive = DDDhelper.getDate(2024, 2025)
        bookings[index].nights = DDDhelper.getNights()
        bookings[index].ppn = DDDhelper.getPrice(50, 100)
        bookings[index].custNo = DDDhelper.getNumber(int(count/4))
        bookings[index].prepaid = DDDhelper.getTrue(20)


    ## Insert data

    for index in range(len(bookings)):

        fileOut.write("INSERT INTO Booking VALUES ")
        fileOut.write("(")
        fileOut.write(    str(bookings[index].reservation) + ",")
        fileOut.write( "\"" + bookings[index].arrive + "\",")
        fileOut.write(    str(bookings[index].nights) + ",")
        fileOut.write(    str(bookings[index].ppn) + ",")
        fileOut.write(    str(bookings[index].prepaid) + ",")
        fileOut.write(    str(bookings[index].custNo))
        fileOut.write(");\n")

    fileOut.close()


def main():
    """Main program."""    
    createCustomers(100)
    createBookings(400)


# Call main()
main()
