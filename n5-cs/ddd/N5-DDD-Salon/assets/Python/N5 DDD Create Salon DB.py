# Title: N5 DDD Create Salon DB
# Author: Mr Friend
# Date: 6 May 2026

# Get extra code
import sqlite3


def hairdresserTable():

    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Hairdresser;
        '''

        # Drop the table
        cursor.execute(dropTable)


    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Hairdresser (
        hairdresserID INT NOT NULL,
        firstName VARCHAR(20),
        lastName VARCHAR(30),
        phone VARCHAR(13) NOT NULL
            CHECK (LENGTH(phone >= 11)),
        salon VARCHAR(30),
        PRIMARY KEY (hairdresserID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Hairdresser.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            hairID = data[0].strip()
            first = data[1].strip()
            last = data[2].strip()
            phone = data[3].strip()
            salon = data[4].strip()
            
            # Check for NULL values
            if first == '':
                first = 'NULL'
            else:
                first = f'"{first}"'
                
            if last == '':
                last = 'NULL'
            else:
                last = f'"{last}"'
                
            if salon == '':
                salon = 'NULL'
            else:
                salon = f'"{salon}"'
            
            # Create data
            values = f'({hairID},{first},{last},"{phone}",{salon})'
            
            # SQL to insert data
            newData = f'INSERT INTO Hairdresser VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


def clientTable():
    
    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Client;
        '''

        # Drop the table
        cursor.execute(dropTable)


    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Client (
        clientid INT NOT NULL,
        hairdresserID INT NOT NULL,
        firstName VARCHAR(20),
        lastName VARCHAR(30),
        phone VARCHAR(13) NOT NULL
            CHECK (LENGTH(phone >= 11)),
        FOREIGN KEY (hairdresserID)
            REFERENCES Hairdresser (hairdresserID),
        PRIMARY KEY (clientID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Client.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            clientID = data[0].strip()
            hairID = data[1].strip()
            first = data[2].strip()
            last = data[3].strip()
            phone = data[4].strip()
            
            # Check for NULL values
            if first == '':
                first = 'NULL'
            else:
                first = f'"{first}"'
            
            if last == '':
                last = 'NULL'
            else:
                last = f'"{last}"'
            
            # Create data
            values = f'({clientID},{hairID},{first},{last},"{phone}")'
            
            # SQL to insert data
            newData = f'INSERT INTO Client VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


#
# Main program
#

# Create a connection to a database
# Creates a new database file, if it doesn’t exist
conn = sqlite3.connect('../Salon.db')

# Create a database cursor
cursor = conn.cursor()


# Hairdresser table
print("1. Hairdresser table")
hairdresserTable()


# Client table
print("2. Client table")
clientTable()


# Close the connection to the database
conn.close()
