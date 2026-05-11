# Title: H DDD Clydeview Create DB
# Author: Mr Friend
# Date: 11 May 2026

# Get extra code
import sqlite3


def dropTable(tableName=""):
        
    if tableName != "":
        
        # SQL query
        query = f'DROP TABLE IF EXISTS {tableName};'

        # Drop the table
        cursor.execute(query)


def table1Table():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Table1 (
        pupilID INT NOT NULL,
        forename VARCHAR(12) NOT NULL,
        surname VARCHAR(12) NOT NULL,
        test1 INT NOT NULL
            CHECK (test1 >= 0 AND test1 <= 10),
        test2 INT NOT NULL
            CHECK (test2 >= 0 AND test2 <= 10),
        test3 INT NOT NULL
            CHECK (test3 >= 0 AND test3 <= 10),
        test4 INT NOT NULL
            CHECK(test4 >= 0 AND test4 <= 10),
        PRIMARY KEY (pupilID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Table1.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            pupilID = data[0].strip()
            first = data[1].strip()
            last = data[2].strip()
            test1 = data[3].strip()
            test2 = data[4].strip()
            test3 = data[5].strip()
            test4 = data[6].strip()
            
            # Create data            
            values = f'({pupilID},"{first}","{last}",{test1},{test2},' \
                     + f'{test3},{test1})'
            
            # SQL to insert data
            newData = f'INSERT INTO Table1 VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Table1")
    createTable()
    insertData()


def table2Table():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Table2 (
        staffID INT NOT NULL,
        forename VARCHAR(12) NOT NULL,
        surname VARCHAR(12) NOT NULL,
        hourlyRate FLOAT NOT NULL
            CHECK (hourlyRate >= 0),
        hoursWorked INT NOT NULL
            CHECK (hoursWorked >= 0),
        PRIMARY KEY (staffID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Table2.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            staffID = data[0].strip()
            first = data[1].strip()
            last = data[2].strip()
            rate = data[3].strip()
            hours = data[4].strip()
            
            # Create data            
            values = f'({staffID},"{first}","{last}",{rate},{hours})'
                        
            # SQL to insert data
            newData = f'INSERT INTO Table2 VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Table2")
    createTable()
    insertData()


def table3Table():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Table3 (
        studentID INT NOT NULL,
        forename VARCHAR(50) NOT NULL,
        surname VARCHAR(50) NOT NULL,
        test1 INT NOT NULL
            CHECK (test1 >= 0 AND test1 <= 20),
        test2 INT NOT NULL
            CHECK (test2 >= 0 AND test2 <= 20),
        test3 INT NOT NULL
            CHECK (test3 >= 0 AND test3 <= 20),
        test4 INT NOT NULL
            CHECK(test4 >= 0 AND test4 <= 20),
        test5 INT NOT NULL
            CHECK (test5 >= 0 AND test5 <= 20),
        PRIMARY KEY (studentID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Table3.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            studentID = data[0].strip()
            first = data[1].strip()
            last = data[2].strip()
            test1 = data[3].strip()
            test2 = data[4].strip()
            test3 = data[5].strip()
            test4 = data[6].strip()
            test5 = data[7].strip()
            
            # Create data            
            values = f'({studentID},"{first}","{last}",{test1},{test2},' \
                     + f'{test3}, {test4}, {test5})'
                        
            # SQL to insert data
            newData = f'INSERT INTO Table3 VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Table3")
    createTable()
    insertData()


def table4Table():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Table4 (
        productID INT NOT NULL,
        productName VARCHAR(12) NOT NULL,
        buyingPence INT NOT NULL
            CHECK (buyingPence >= 0),
        sellingPence INT NOT NULL
            CHECK (sellingPence >= 0),
        PRIMARY KEY (productID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Table4.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            productID = data[0].strip()
            name = data[1].strip()
            buy = data[2].strip()
            sell = data[3].strip()
            
            # Create data            
            values = f'({productID},"{name}",{buy},{sell})'
                        
            # SQL to insert data
            newData = f'INSERT INTO Table4 VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Table4")
    createTable()
    insertData()


def table5Table():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Table5 (
        productName VARCHAR(20) NOT NULL,
        productID VARCHAR(50) NOT NULL,
        pricePounds FLOAT NOT NULL
            CHECK (pricePounds >= 0.00),
        PRIMARY KEY (productID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Table5.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            name = data[0].strip()
            productID = data[1].strip()
            price = data[2].strip()
            
            # Create data            
            values = f'("{name}","{productID}",{price})'
                        
            # SQL to insert data
            newData = f'INSERT INTO Table5 VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Table5")
    createTable()
    insertData()


def table6Table():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Table6 (
        fishType VARCHAR(12) NOT NULL,
        pricePerKilo FLOAT NOT NULL
            CHECK (pricePerKilo >= 0.00),
        numberOfKilos FLOAT NOT NULL
            CHECK (numberOfKilos >= 0.0),
        PRIMARY KEY (fishType)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Table6.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            fishType = data[0].strip()
            price = data[1].strip()
            number = data[2].strip()
            
            # Create data            
            values = f'("{fishType}",{price},{number})'
                        
            # SQL to insert data
            newData = f'INSERT INTO Table6 VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Table6")
    createTable()
    insertData()


def employeeTable():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Employee (
        employeeID INT NOT NULL,
        jobTitle VARCHAR(8) NOT NULL,
        name VARCHAR(20) NOT NULL,
        building VARCHAR(2),
        yearsEmployed INT NOT NULL
            CHECK (yearsEmployed >= 0),
        PRIMARY KEY (employeeID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Employee.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            employeeID = data[0].strip()
            job = data[1].strip()
            name = data[2].strip()
            building = data[3].strip()
            years = data[4].strip()
            
            # Check for NULL values
            if building == '':
                building = 'NULL'
            else:
                building = f'"{building}"'
            
            # Create data            
            values = f'({employeeID},"{job}","{name}",{building},{years})'
            
            # SQL to insert data
            newData = f'INSERT INTO Employee VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Employee")
    createTable()
    insertData()


def memberTable():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Member (
        membershipNumber VARCHAR(6) NOT NULL,
        forename VARCHAR(20) NOT NULL,
        surname VARCHAR(20) NOT NULL,
        address VARCHAR(30),
        town VARCHAR(40),
        postcode VARCHAR(8),
        dateOfBirth DATE NOT NULL,
        monthOfRenewal VARCHAR(9) NOT NULL,
        typeOfMembership VARCHAR(7) NOT NULL
            CHECK (typeOfMembership IN ("Adult","Child","Senior","Student")),
        PRIMARY KEY (membershipNumber)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Member.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            memNo = data[0].strip()
            first = data[1].strip()
            last = data[2].strip()
            address = data[3].strip()
            town = data[4].strip()
            postcode = data[5].strip()
            dob = data[6].strip()
            renew = data[7].strip()
            memType = data[8].strip()
            
            # Check for NULL values
            if address == '':
                address = 'NULL'
            else:
                address = f'"{address}"'
            
            if town == '':
                town = 'NULL'
            else:
                town = f'"{town}"'
            
            if postcode == '':
                postcode = 'NULL'
            else:
                postcode = f'"{postcode}"'
            
            # Create data            
            values = f'("{memNo}","{first}","{last}",{address},{town},' \
                     + f'{postcode},"{dob}","{renew}","{memType}")'
            
            # SQL to insert data
            newData = f'INSERT INTO Member VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Member")
    createTable()
    insertData()


def plantTable():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Plant (
        category VARCHAR(10) NOT NULL,
        name VARCHAR(20) NOT NULL,
        variety VARCHAR(20) NOT NULL,
        code VARCHAR(3) NOT NULL,
        referenceID VARCHAR(3) NOT NULL,
        quantity INT NOT NULL
            CHECK (quantity >= 0),
        price FLOAT NOT NULL
            CHECK (price >= 0),
        height VARCHAR(1) NOT NULL
            CHECK (height IN("S","M","T")),
        PRIMARY KEY (referenceID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Plant.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            category = data[0].strip()
            name = data[1].strip()
            variety = data[2].strip()
            code = data[3].strip()
            refID = data[4].strip()
            quantity = data[5].strip()
            price = data[6].strip()
            height = data[7].strip()
            
            # Create data            
            values = f'("{category}","{name}","{variety}","{code}",' \
                     + f'"{refID}",{quantity},{price},"{height}")'
            
            # SQL to insert data
            newData = f'INSERT INTO Plant VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Plant")
    createTable()
    insertData()


def hotelTable():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Hotel (
        hotelRef VARCHAR(4) NOT NULL,
        name VARCHAR(30) NOT NULL,
        city VARCHAR(20),
        starRating INT NOT NULL
            CHECK (starRating >= 0 AND starRating <= 5),
        pricePerNight REAL,
        kmFromAirport REAL,
        PRIMARY KEY (hotelRef)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Hotel-Holiday/Hotel.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            hotelRef = data[0].strip()
            name = data[1].strip()
            city = data[2].strip()
            rating = data[3].strip()
            price = data[4].strip()
            distance = data[5].strip()
            
            # Create data            
            values = f'("{hotelRef}","{name}","{city}",{rating},{price},' \
                     + f'{distance})'
            
            # SQL to insert data
            newData = f'INSERT INTO Hotel VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Hotel")
    createTable()
    insertData()


def holidayTable():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Holiday (
        title VARCHAR(30) NOT NULL,
        destination VARCHAR(30) NOT NULL,
        country VARCHAR(20),
        dateOfDeparture DATE NOT NULL,
        nights INT NOT NULL,
        hotelRef VARCHAR(4) NOT NULL,
        FOREIGN KEY (hotelRef)
            REFERENCES Hotel (hotelRef),
        PRIMARY KEY (title)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Hotel-Holiday/Holiday.csv', 'r', encoding='latin-1')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            name = data[0].strip()
            dest = data[1].strip()
            country = data[2].strip()
            date = data[3].strip()
            nights = data[4].strip()
            hotelRef = data[5].strip()
            
            # Create data            
            values = f'("{name}","{dest}","{country}","{date}",{nights},' \
                     + f'"{hotelRef}")'
            
            # SQL to insert data
            newData = f'INSERT INTO Holiday VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Holiday")
    createTable()
    insertData()


def countryTable():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Country (
        name VARCHAR(35) NOT NULL,
        code VARCHAR(4) NOT NULL,
        capital VARCHAR(20) NOT NULL,
        area INT NOT NULL
            CHECK(area >= 0),
        population INT NOT NULL
            CHECK(population >= 0),
        PRIMARY KEY (code)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Country-City/Country.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            name = data[0].strip()
            code = data[1].strip()
            capital = data[2].strip()
            area = data[3].strip()
            pop = data[4].strip()
            
            # Create data            
            values = f'("{name}","{code}","{capital}",{area},{pop})'
            
            # SQL to insert data
            newData = f'INSERT INTO Country VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Country")
    createTable()
    insertData()


def cityTable():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE City (
        cityID INT NOT NULL,
        name VARCHAR(20) NOT NULL,
        countryCode VARCHAR(4) NOT NULL,
        population INT
            CHECK (population >= 0),
        longitude REAL,
        latitude REAL,
        FOREIGN KEY (countryCode)
            REFERENCES Country (code),
        PRIMARY KEY (cityID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Country-City/City.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            cityID = data[0].strip()
            name = data[1].strip()
            code = data[2].strip()
            pop = data[3].strip()
            long = data[4].strip()
            lat = data[5].strip()
            
            # Check for NULL values
            if pop == '':
                pop = 'NULL'
                
            if long == '':
                long = 'NULL'
                
            if lat == '':
                lat = 'NULL'
            
            # Create data            
            values = f'("{cityID}","{name}","{code}",{pop},{long},{lat})'
            
            # SQL to insert data
            newData = f'INSERT INTO City VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("City")
    createTable()
    insertData()


def movieTable():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Movie (
        movieID INT NOT NULL,
        title VARCHAR(30) NOT NULL,
        director VARCHAR(30),
        yearReleased INT NOT NULL
            CHECK (yearReleased >= 1900 AND yearReleased <= 2030),
        durationsMins INT NOT NULL
            CHECK(durationsMins >= 0),
        PRIMARY KEY (movieID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Movie-BoxOffice/Movie.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            movieID = data[0].strip()
            title = data[1].strip()
            director = data[2].strip()
            year = data[3].strip()
            mins = data[4].strip()
            
            # Check for NULL values
            if director == '':
                director = 'NULL'
            else:
                director = f'"{director}"'
            
            # Create data            
            values = f'({movieID},"{title}",{director},{year},{mins})'
            
            # SQL to insert data
            newData = f'INSERT INTO Movie VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("Movie")
    createTable()
    insertData()


def boxOfficeTable():

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE BoxOffice (
        movieID INT NOT NULL,
        rating REAL NOT NULL
            CHECK (rating >=0 AND rating <= 10),
        movieBudget INT NOT NULL
            CHECK (movieBudget >= 0),
        salesUS INT NOT NULL
            CHECK (salesUS >= 0),
        salesInternational INT NOT NULL
            CHECK (salesInternational >= 0),
        FOREIGN KEY (movieID)
            REFERENCES Movie (movieID),
        PRIMARY KEY (movieID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Movie-BoxOffice/BoxOffice.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            movieID = data[0].strip()
            rating = data[1].strip()
            budget = data[2].strip()
            salesUS = data[3].strip()
            salesInt = data[4].strip()
            
            # Create data            
            values = f'({movieID},{rating},{budget},{salesUS},{salesInt})'
            
            # SQL to insert data
            newData = f'INSERT INTO BoxOffice VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable("BoxOffice")
    createTable()
    insertData()

'''           
# Check for boolean values
directDebit = f'{"FALSE" if directDebit=="0" else "TRUE"}'
'''           

#
# Main program
#

# Create a connection to a database
# Creates a new database file, if it doesn’t exist
conn = sqlite3.connect('../Clydeview.db')

# Create a database cursor
cursor = conn.cursor()

'''
print(" 1. Table1 table")
table1Table()

print(" 2. Table2 table")
table2Table()

print(" 3. Table3 table")
table3Table()

print(" 4. Table4 table")
table4Table()

print(" 5. Table5 table")
table5Table()

print(" 6. Table6 table")
table6Table()

print(" 7. Employee table")
employeeTable()

print(" 8. Member table")
memberTable()

print(" 9. Plant table")
plantTable()

print("10. Hotel table")
hotelTable()

print("11. Holiday table")
holidayTable()

print("12. Country table")
countryTable()

print("13. City table")
cityTable()
'''
print("14. Movie table")
movieTable()

print("15. BoxOffice table")
boxOfficeTable()


# Close the connection to the database
conn.close()

