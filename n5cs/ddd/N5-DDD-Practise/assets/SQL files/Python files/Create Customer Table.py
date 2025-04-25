# Title: Create Customer Table
# Author: Mr Friend
# Date: 2 Dec 2024

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

fileOut = open("..\\Customer.sql", "w")
count = 100


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


for index in range(count):
    
    # Create data
    firstName = DDDhelper.getForename()
    lastName = DDDhelper.getSurname()
    custNo = index + 1
    phone = DDDhelper.getPhone()
    email = DDDhelper.getEmail(firstName, lastName)

    # Insert data
    fileOut.write("INSERT INTO Customer VALUES ")
    fileOut.write("(")
    fileOut.write(    str(custNo) + ",")
    fileOut.write( "\"" + firstName + "\",")
    fileOut.write( "\"" + lastName + "\",")
    fileOut.write( "\"" + phone + "\",")
    
    if email != "":
        fileOut.write( "\"" + email + "\");\n")
    else:
        fileOut.write("NULL);\n")

fileOut.close()
