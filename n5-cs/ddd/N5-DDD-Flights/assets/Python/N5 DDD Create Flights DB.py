# Title: N5 DDD Create Flights DB
# Author: Mr Friend
# Date: 22 Apr 2026

# Get extra code
import sqlite3


def dropCustomerTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Customer;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createCustomerTable():
    
    # SQL query
    createTable = '''CREATE TABLE Customer (
    customerID VARCHAR(7) NOT NULL,
    forename VARCHAR(30) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    street VARCHAR(30) NOT NULL,
    town VARCHAR(20) NOT NULL,
    postcode VARCHAR(8) NOT NULL,
    PRIMARY KEY (customerID)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertCustomerData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Customer.csv', 'r')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        custID = data[0].strip()
        forename = data[1].strip()
        surname = data[2].strip()
        street = data[3].strip()
        town = data[4].strip()
        postcode = data[5].strip()
        
        # Create data
        values = '("' + custID + '","' + forename + '","' + surname + '","' + \
            street + '","' + town + '","' + postcode + '")'
        
        # SQL to insert data
        newData = 'INSERT INTO Customer VALUES' + values + ';'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropAirportTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Airport;
    '''

    # Drop the table
    cursor.execute(dropTable)

def createAirportTable():
    
    # SQL query
    createTable = '''CREATE TABLE Airport (
    name VARCHAR(50) NOT NULL,
    country VARCHAR(20) NOT NULL,
    code VARCHAR(3) NOT NULL
        CHECK (LENGTH(code) = 3),
    continent VARCHAR(15) NOT NULL,
    PRIMARY KEY (code)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertAirportData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Airport.csv', 'r')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        name = data[0].strip()
        country = data[1].strip()
        code = data[2].strip()
        continent = data[3].strip()
        
        # Create data
        values = '("' + name + '","' + country + '","' + code + '","' + continent + '")'
        
        # SQL to insert data
        newData = 'INSERT INTO Airport VALUES' + values + ';'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropRouteTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Route;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createRouteTable():
    
    # SQL query
    createTable = '''CREATE TABLE Route (
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
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertRouteData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Route.csv', 'r')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        routeID = data[0].strip()
        depCode = data[1].strip()
        arrCode = data[2].strip()
        stop1Code = data[3].strip()
        stop2Code = data[4].strip()
        
        # Create data
        values = '(' + routeID + ',"' + depCode + '","' + arrCode + '"'
        
        if stop1Code == '':
            values = values + ',NULL'
        else:
            values = values + ',"' + stop1Code + '"'
            
        if stop2Code == '':
            values = values + ',NULL)'
        else:
            values = values + ',"' + stop2Code + '")'
        
        # SQL to insert data
        newData = 'INSERT INTO Route VALUES' + values + ';'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropFlightTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Flight;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createFlightTable():
    
    # SQL query
    createTable = '''CREATE TABLE Flight (
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
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertFlightData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Flight.csv', 'r')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        flightID = data[0].strip()
        depDate = data[1].strip()
        depTime = data[2].strip()
        arrDate = data[3].strip()
        arrTime = data[4].strip()
        capacity = data[5].strip()
        routeID = data[6].strip()
        
        # Create data
        values = '("' + flightID + '","' + depDate + '","' + depTime + '","' + \
               arrDate + '","' + arrTime + '",' + capacity + ',' + \
               routeID + ')'
        
        # SQL to insert data
        newData = 'INSERT INTO Flight VALUES' + values + ';'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropBookingTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Booking;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createBookingTable():
    
    # SQL query
    createTable = '''CREATE TABLE Booking (
    bookingNo INT NOT NULL,
    adultTicket INT NOT NULL,
    childTicket INT NOT NULL,
    concessionTicket INT NOT NULL,
    customerID VARCHAR(7) NOT NULL,
    flightID VARCHAR(5) NOT NULL,
    PRIMARY KEY (bookingNo),
    FOREIGN KEY (customerID)
        REFERENCES Customer (customerID),
    FOREIGN KEY (flightID)
        REFERENCES Flight (flightID)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertBookingData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Booking.csv', 'r')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        bookingNo = data[0].strip()
        adult = data[1].strip()
        child = data[2].strip()
        consession = data[3].strip()
        custID = data[4].strip()
        flightID = data[5].strip()
        
        # Create data
        values = '(' + bookingNo + ',' + adult + ',' + child + ',' + \
               consession + ',"' + custID + '","' + flightID + '")'
        
        # SQL to insert data
        newData = 'INSERT INTO Booking VALUES' + values + ';'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


#
# Main program
#

# Create a connection to a database
# Creates a new database file, if it doesn’t exist
conn = sqlite3.connect('../Flights.db')

# Create a database cursor
cursor = conn.cursor()


# Customer table
print("1. Customer table")
dropCustomerTable()
createCustomerTable()
insertCustomerData()


# Airport table
print("2. Airport table")
dropAirportTable()
createAirportTable()
insertAirportData()


# Route table
print("3. Route table")
dropRouteTable()
createRouteTable()
insertRouteData()


# Flight table
print("4. Flight table")
dropFlightTable()
createFlightTable()
insertFlightData()


# Booking table
print("5. Booking table")
dropBookingTable()
createBookingTable()
insertBookingData()


# Close the connection to the database
conn.close()
