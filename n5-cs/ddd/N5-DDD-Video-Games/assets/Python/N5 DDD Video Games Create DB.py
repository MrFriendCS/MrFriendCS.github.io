# Title: N5 DDD Create Video Games DB
# Author: Mr Friend
# Date: 7 May 2026

# Get extra code
import sqlite3


def companyTable():

    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Company;
        '''

        # Drop the table
        cursor.execute(dropTable)


    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Company (
        name VARCHAR(20) NOT NULL,
        country VARCHAR(20) NOT NULL,
        founded DATE NOT NULL 
            CHECK (founded >= "1970-01-01"),
        website VARCHAR(30),
        profit INT NOT NULL,
        PRIMARY KEY (name)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Company.csv', 'r', encoding='utf-8')
        
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
            country = data[1].strip()
            founded = data[2].strip()
            website = data[3].strip()
            profit = data[4].strip()
            
            # Check for NULL values
            if website == '':
                website = 'NULL'
            else:
                website = f'"{website}"'

            # Create data
            values = f'("{name}","{country}","{founded}",{website},{profit})'
            
            # SQL to insert data
            newData = f'INSERT INTO Company VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


def gameTable():
    
    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Game;
        '''

        # Drop the table
        cursor.execute(dropTable)


    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Game (
        title VARCHAR(30) NOT NULL,
        company VARCHAR(20) NOT NULL,
        genre VARCHAR(15) NOT NULL,
        age INT NOT NULL 
            CHECK (age IN (3, 7, 12, 16, 18)),
        price FLOAT NOT NULL 
            CHECK (price >= 0 AND price <= 100),
        released DATE NOT NULL 
            CHECK (released >= "1970-01-01"),
        copiesSold INT NOT NULL 
            CHECK (copiesSold >= 0),
        PRIMARY KEY (title),
        FOREIGN KEY (company)
            REFERENCES Company(name)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Game.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            title = data[0].strip()
            company = data[1].strip()
            genre = data[2].strip()
            age = data[3].strip()
            price = data[4].strip()
            released = data[5].strip()
            copiesSold = data[6].strip()
                     
            # Create data
            values = f'("{title}","{company}","{genre}",{age},{price},"{released}",{copiesSold})'
            
            # SQL to insert data
            newData = f'INSERT INTO Game VALUES {values};'
            
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
conn = sqlite3.connect('../VideoGames.db')

# Create a database cursor
cursor = conn.cursor()


# Company table
print("1. Company table")
companyTable()


# Game table
print("2. Game table")
gameTable()


# Close the connection to the database
conn.close()
