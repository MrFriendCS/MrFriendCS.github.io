# Title: N5 DDD Membership Create DB
# Author: Mr Friend
# Date: 9 May 2026

# Get extra code
import sqlite3


def clubTable():

    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Club;
        '''

        # Drop the table
        cursor.execute(dropTable)


    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Club (
        clubID VARCHAR(6) NOT NULL,
        name VARCHAR(30) NOT NULL,
        location VARCHAR(30) NOT NULL,
        type VARCHAR(20) NOT NULL,
        opened DATE
            CHECK (opened LIKE "____-__-__"),
        trainer BOOLEAN NOT NULL
            CHECK (trainer IN (0, 1)),
        rooms INT
            CHECK (rooms >= 0),
        PRIMARY KEY (clubID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Club.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            clubID = data[0].strip()
            name = data[1].strip()
            location = data[2].strip()
            clubType = data[3].strip()
            opened = data[4].strip()
            trainer = data[5].strip()
            rooms = data[6].strip()
            
            # Check for NULL values
            if opened == '':
                opened = 'NULL'
            else:
                opened = f'"{opened}"'
            
            if rooms == '':
                rooms = 'NULL'
            
            # Create data
            values = f'("{clubID}","{name}","{location}","{clubType}",' \
                     + f'{opened},{trainer},{rooms})'
            
            # SQL to insert data
            newData = f'INSERT INTO Club VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


def memberTable():

    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Member;
        '''

        # Drop the table
        cursor.execute(dropTable)

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Member (
        memberNo VARCHAR(8) NOT NULL,
        clubID VARCHAR(6) NOT NULL,
        firstName VARCHAR(20) NOT NULL,
        lastName VARCHAR(30) NOT NULL,
        address VARCHAR(30),
        town VARCHAR(20),
        postcode VARCHAR(8),
        dob DATE NOT NULL 
            CHECK (dob >= "1925-01-01" AND dob LIKE "____-__-__"),
        renew INT NOT NULL 
            CHECK (renew >=1 AND renew <= 12),
        gender VARCHAR(2) NOT NULL
            CHECK (gender IN ("F", "M", "ND")),
        type VARCHAR(15) NOT NULL 
            CHECK (type IN ("Adult", "Child", "Guest", "Senior", "Student")),
        FOREIGN KEY (clubID) 
            REFERENCES Club (clubID),
        PRIMARY KEY (memberNo)
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
            memberNo = data[0].strip()
            clubID = data[1].strip()
            first = data[2].strip()
            last = data[3].strip()
            address = data[4].strip()
            town = data[5].strip()
            postcode = data[6].strip()
            dob = data[7].strip()
            renew = data[8].strip()
            gender = data[9].strip()
            memberType = data[10].strip()
            
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
            values = f'("{memberNo}","{clubID}","{first}","{last}",' \
                     + f'{address},{town},{postcode},"{dob}",{renew},' \
                     + f'"{gender}","{memberType}")'
            
            # SQL to insert data
            newData = f'INSERT INTO Member VALUES {values};'
            
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
conn = sqlite3.connect('../Membership.db')

# Create a database cursor
cursor = conn.cursor()


# Club table
print("1. Club table")
clubTable()


# Member table
print("2. Member table")
memberTable()


# Close the connection to the database
conn.close()
