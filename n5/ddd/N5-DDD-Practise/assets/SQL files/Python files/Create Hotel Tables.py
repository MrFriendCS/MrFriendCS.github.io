# Title: Create Hotel Tables
# Author: Mr Friend
# Date: 6 Oct 2024

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


@dataclass
class customer:
    """A record to represent a hotel customer."""
    
    custNo: int = 0
    first_name: str = ""
    last_name: str = ""
    phone: str = ""
    email: str = ""


@dataclass
class booking:
    """A record to represent a hotel booking."""
    
    reservation: int = 0
    arrive: str = ""
    nights: int = 0
    ppn: float = 0.0
    prepaid: bool = False
    custNo: int = 0


#
# Main program
#

customers = [customer()] * 100
bookings = [booking()] * 400

# Create customer data

customerTable = """CREATE TABLE Customer (
    custNo INT NOT NULL,
    first_name VARCHAR(20),
    last_name VARCHAR(30),
    phone VARCHAR(11) NOT NULL
        CHECK(LENGTH(phone) = 11),
    email VARCHAR(30),
    PRIMARY KEY (custNo)
);"""

for index in range(len(customers)):

    custNo = index + 1
    first_name = DDDhelper.getForename()
    last_name = DDDhelper.getSurname()
    phone = DDDhelper.getPhone()
    email = DDDhelper.getEmail(first_name, last_name)

    # Add record to array
    customers[index] = customer(custNo, first_name, last_name, phone, email)

# Create booking data

bookingTable = """CREATE TABLE Booking (
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
    
    reservation = 750 + index
    arrive = DDDhelper.getDate(2024, 2025)
    nights = DDDhelper.getNights()
    ppn = DDDhelper.getPrice(50, 100)
    custNo = DDDhelper.getNumber(len(customers))
    prepaid = DDDhelper.getTrue(20)

    # Add record to array
    bookings[index] = booking(reservation, arrive, nights, ppn, prepaid, custNo)

# Write customer data to file

file = open("Customer.sql", "w")

file.write(customerTable + "\n\n")

for index in range(len(customers)):
    
    file.write("INSERT INTO Customer VALUES ")
    file.write("("   + str(customers[index].custNo) + ",")
    file.write( "\"" + customers[index].first_name + "\",")
    file.write( "\"" + customers[index].last_name + "\",")
    file.write( "\"" + customers[index].phone + "\",")
    
    if customers[index].email != "":
        file.write( "\"" + customers[index].email + "\");\n")
    else:
        file.write("NULL);\n")

file.close()


# Write booking data to file

file = open("Booking.sql", "w")

file.write(bookingTable + "\n\n")

for index in range(len(bookings)):

    file.write("INSERT INTO Booking VALUES ")
    file.write("("   + str(bookings[index].reservation) + ",")
    file.write( "\"" + bookings[index].arrive + "\",")
    file.write(        str(bookings[index].nights) + ",")
    file.write(        str(bookings[index].ppn) + ",")
    file.write(        str(bookings[index].prepaid) + ",")
    file.write(        str(bookings[index].custNo) + ");\n")

file.close()
