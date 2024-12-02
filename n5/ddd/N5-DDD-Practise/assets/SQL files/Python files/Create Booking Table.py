# Title: Create Booking Table
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
    # Personal laptop
    sys.path.append(start2 + end)


# Get extra code
import DDDhelper


fileOut = open("../Booking.sql", "w")

count = 400

# Create table

table = """CREATE TABLE booking (
    reservation INT NOT NULL,
    arrive DATE NOT NULL,
    nights INT NOT NULL 
        CHECK(nights >= 1),
    ppn REAL NOT NULL
        CHECK (ppn >= 50),
    prepaid BOOL,
    custNo INT NOT NULL,
    FOREIGN KEY (custNo)
        REFERENCES Customer (custNo),
    PRIMARY KEY (reservation)
);"""

fileOut.write(table + "\n\n")


for index in range(count):
    
    # Create data
    reservation = 750 + index
    arrive = DDDhelper.getDate(2024, 2025)
    nights = DDDhelper.getNights()
    ppn = DDDhelper.getPrice(50, 100)
    custNo = DDDhelper.getNumber(int(count/4))
    prepaid = DDDhelper.getTrue(20)

    # Insert data
    fileOut.write("INSERT INTO Booking VALUES ")
    fileOut.write("(")
    fileOut.write(    str(reservation) + ",")
    fileOut.write( "\"" + arrive + "\",")
    fileOut.write(    str(nights) + ",")
    fileOut.write(    str(ppn) + ",")
    fileOut.write(    str(prepaid) + ",")
    fileOut.write(    str(custNo))
    fileOut.write(");\n")


fileOut.close()
