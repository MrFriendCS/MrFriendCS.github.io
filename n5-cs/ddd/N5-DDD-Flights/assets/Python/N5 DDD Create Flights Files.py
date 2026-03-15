# Title: N5 DDD Create Flights Files
# Author: Mr Friend
# Date: 27 Jan 2023

# Create Route.sql

fileIn = open("../CSV/Route.csv", "r")
fileOut = open("../SQL/Route.sql", "w")

table = """CREATE TABLE Route (
    routeID INT NOT NULL,
    depCode VARCHAR(3) NOT NULL,
    arrCode VARCHAR(3) NOT NULL,
    stop1code VARCHAR(3),
    stop2code VARCHAR(3),
    FOREIGN KEY (depCode)
        REFERENCES Airport (code),
    FOREIGN KEY (arrCode)
        REFERENCES Airport (code),
    FOREIGN KEY (stop1code)
        REFERENCES Airport (code),
    FOREIGN KEY (stop2code)
        REFERENCES Airport (code),
    PRIMARY KEY (routeID)
);"""
            
fileOut.write(table + "\n\n")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Route VALUES ")
    
    fileOut.write( "(" + data[0].strip() + ",")
    fileOut.write("\"" + data[1].strip() + "\",")
    fileOut.write("\"" + data[2].strip() + "\",")
    
    if len(data[3].strip()) == 3:
        fileOut.write("\"" + data[3].strip() + "\",")
    else:
        fileOut.write("NULL,")
        
    if len(data[4].strip()) == 3:
        fileOut.write("\"" + data[4].strip() + "\");\n")
    else:
        fileOut.write("NULL);\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create Flight.sql

fileIn = open("../CSV/Flight.csv", "r")
fileOut = open("../SQL/Flight.sql", "w")

table = """CREATE TABLE Flight (
    flightID VARCHAR(5) NOT NULL,
    depDate DATE NOT NULL,
    depTime TIME NOT NULL,
    arrDate DATE NOT NULL,
    arrTime TIME NOT NULL,
    capacity INT NOT NULL,
    routeID INT NOT NULL,
    FOREIGN KEY (routeID)
        REFERENCES Route (routeID),
    PRIMARY KEY (flightID)
);"""

fileOut.write(table + "\n\n")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Flight VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")
    fileOut.write( "\"" + data[1].strip() + "\",")
    fileOut.write( "\"" + data[2].strip() + "\",")
    fileOut.write( "\"" + data[3].strip() + "\",")
    fileOut.write( "\"" + data[4].strip() + "\",")
    fileOut.write(        data[5].strip() + ",")
    fileOut.write(        data[6].strip() + ");\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create Garage.sql

fileIn = open("../CSV/Customer.csv", "r")
fileOut = open("../SQL/Customer.sql", "w")

table = """CREATE TABLE Customer (
    customerID VARCHAR(7) NOT NULL,
    forename VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    street VARCHAR(30) NOT NULL,
    town VARCHAR(20) NOT NULL,
    postcode VARCHAR(8) NOT NULL,
    PRIMARY KEY (customerID)
);"""

fileOut.write(table + "\n\n")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Customer VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")
    fileOut.write( "\"" + data[1].strip() + "\",")
    fileOut.write( "\"" + data[2].strip() + "\",")
    fileOut.write( "\"" + data[3].strip() + "\",")
    fileOut.write( "\"" + data[4].strip() + "\",")
    fileOut.write( "\"" + data[5].strip() + "\");\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create Booking.sql

fileIn = open("../CSV/Booking.csv", "r")
fileOut = open("../SQL/Booking.sql", "w")

table = """CREATE TABLE Booking (
    bookingNo INT NOT NULL,
    adultTicket INT NOT NULL,
    childTicket INT NOT NULL,
    concessionTicket INT NOT NULL,
    customerID VARCHAR(7) NOT NULL,
    flightID VARCHAR(5) NOT NULL,
    FOREIGN KEY (customerID)
        REFERENCES Customer (customerID),
    FOREIGN KEY (flightID)
        REFERENCES Flight (flightID),
    PRIMARY KEY (bookingNo)
);"""

fileOut.write(table + "\n\n")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Booking VALUES ")
    
    fileOut.write("(" +   data[0].strip() + ",")
    fileOut.write(        data[1].strip() + ",")
    fileOut.write(        data[2].strip() + ",")
    fileOut.write(        data[3].strip() + ",")
    fileOut.write( "\"" + data[4].strip() + "\",")
    fileOut.write( "\"" + data[5].strip() + "\");\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()

# Create Airport Table

fileIn = open("../CSV/Airport.csv", "r")
fileOut = open("../SQL/Airport.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()


table = """CREATE TABLE Airport (
    name VARCHAR(50) NOT NULL,
    country VARCHAR(20) NOT NULL,
    code VARCHAR(3) NOT NULL
        CHECK (LENGTH(code) = 3),
    continent VARCHAR(15) NOT NULL,
    PRIMARY KEY (code)
);"""
              
fileOut.write(table + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Airport VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # airport
    fileOut.write( "\"" + data[1].strip() + "\",")  # country
    fileOut.write( "\"" + data[2].strip() + "\",")  # code
    fileOut.write( "\"" + data[3].strip() + "\");\n")  # continent
 
    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
