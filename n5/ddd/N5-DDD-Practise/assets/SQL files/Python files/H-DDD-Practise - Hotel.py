# Title: Create Hotel Tables
# Author: Mr Friend
# Date: 3 Oct 2024

import sys

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


import DDDhelper

from dataclasses import dataclass


def createCustomers(count):
    """Create customer data and table."""
    
    
    @dataclass
    class Customer:
        """A record to represent a hotel customer."""
    
        custNo: int = 0
        first_name: str = ""
        last_name: str = ""
        phone: str = ""
        email: str = ""
    
    
    customers = [Customer() for i in range(count)]

    # Create customer data

    customerTable = """CREATE TABLE customer (
        custNo INT NOT NULL,
        first_name VARCHAR(20),
        last_name VARCHAR(30),
        phone VARCHAR(11) NOT NULL
            CHECK(LENGTH(phone) = 11),
        email VARCHAR(30),
        PRIMARY KEY (custNo)
    );"""

    for index in range(len(customers)):

        customers[index].custNo = index + 1
        first_name = DDDhelper.getForename()
        customers[index].first_name = first_name
        last_name = DDDhelper.getSurname()
        customers[index].last_name = last_name
        customers[index].phone = DDDhelper.getPhone()
        customers[index].email = DDDhelper.getEmail(first_name, last_name)
    
    # Write customer data to file

    file = open("customer.sql", "w")

    file.write(customerTable + "\n\n")

    for index in range(len(customers)):
        
        file.write("INSERT INTO customer VALUES ")
        file.write("(")
        file.write(    str(customers[index].custNo) + ",")
        file.write( "\"" + customers[index].first_name + "\",")
        file.write( "\"" + customers[index].last_name + "\",")
        file.write( "\"" + customers[index].phone + "\",")
        
        if customers[index].email != "":
            file.write( "\"" + customers[index].email + "\");\n")
        else:
            file.write("NULL);\n")

    file.close()


def createBookings(count):
    """Create booking data and table."""
    
    
    @dataclass
    class Booking:
        """A record to represent a hotel booking."""
        
        reservation: int = 0
        arrive: str = ""
        nights: int = 0
        ppn: float = 0.0
        prepaid: bool = False
        custNo: int = 0
    
    
    bookings = [Booking() for i in range(count)]
    
    # Create booking data

    bookingTable = """CREATE TABLE booking (
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

    for index in range(len(bookings)):
        
        bookings[index].reservation = 750 + index
        bookings[index].arrive = DDDhelper.getDate(2024, 2025)
        bookings[index].nights = DDDhelper.getNights()
        bookings[index].ppn = DDDhelper.getPrice(50, 100)
        bookings[index].custNo = DDDhelper.getNumber(int(count/4))
        bookings[index].prepaid = DDDhelper.getTrue(20)

    # Write booking data to file

    file = open("booking.sql", "w")

    file.write(bookingTable + "\n\n")

    for index in range(len(bookings)):

        file.write("INSERT INTO booking VALUES ")
        file.write("(")
        file.write(    str(bookings[index].reservation) + ",")
        file.write( "\"" + bookings[index].arrive + "\",")
        file.write(    str(bookings[index].nights) + ",")
        file.write(    str(bookings[index].ppn) + ",")
        file.write(    str(bookings[index].prepaid) + ",")
        file.write(    str(bookings[index].custNo))
        file.write(");\n")

    file.close()


def main():
    """Main program."""    
    createCustomers(100)
    createBookings(400)


# Call main()
main()
