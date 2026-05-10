# Title: N5 DDD Santa Gifts Create DB
# Author: Mr Friend
# Date: 10 May 2026

# Get extra code
import sqlite3


def childTable():

    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Child;
        '''

        # Drop the table
        cursor.execute(dropTable)


    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Child (
        childID INT NOT NULL,
        firstName VARCHAR(20),
        lastName VARCHAR(30),
        nice BOOLEAN,
        PRIMARY KEY (childID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Child.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            childID = data[0].strip()
            first = data[1].strip()
            last = data[2].strip()
            nice = data[3].strip()
            
            # Check for Boolean values
            nice = f'{"TRUE" if nice.lower()=="true" else "FALSE"}'
            
            # Create data
            values = f'("{childID}","{first}","{last}",{nice})'
            
            # SQL to insert data
            newData = f'INSERT INTO Child VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


def toyTable():

    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Toy;
        '''

        # Drop the table
        cursor.execute(dropTable)

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Toy (
        toyID INT NOT NULL,
        name VARCHAR(50) NOT NULL,
        cost FLOAT NOT NULL,
        PRIMARY KEY (toyID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Toy.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
        
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            toyID = data[0].strip()
            name = data[1].strip()
            cost = data[2].strip()
            
            # Create data
            values = f'({toyID},"{name}",{cost})'
            
            # SQL to insert data
            newData = f'INSERT INTO Toy VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


def giftTable():

    def dropTable():
        
        # SQL query
        dropTable = '''
        DROP TABLE IF EXISTS Gift;
        '''

        # Drop the table
        cursor.execute(dropTable)

    def createTable():
        
        # SQL query
        createTable = '''CREATE TABLE Gift (
        giftID INT NOT NULL,
        childID INT NOT NULL,
        toyID INT NOT NULL,
        PRIMARY KEY (giftID),
        FOREIGN KEY (childID)
            REFERENCES Child(childID),
        FOREIGN KEY (toyID)
            REFERENCES Toy(toyID)
        );'''

        # Create the new table
        cursor.execute(createTable)


    def insertData():
        
        line = ''
        data = []
        values = ''
        
        file = open('../CSV/Gift.csv', 'r', encoding='utf-8')
        
        # Read header
        line = file.readline()
         
        # Read first line
        line = file.readline()
        
        # Loop for each record
        while line != '':
            
            # Split data
            data = line.split(',')
            
            # Extract values
            giftID = data[0].strip()
            childID = data[1].strip()
            toyID = data[2].strip()
            
            # Create data
            values = f'({giftID},{childID},{toyID})'
            
            # SQL to insert data
            newData = f'INSERT INTO Gift VALUES {values};'
            
            # Insert new data
            cursor.execute(newData)

            # Commit the new data
            conn.commit()
            
            # Read next line
            line = file.readline()
    
    
    dropTable()
    createTable()
    insertData()


def errorCheck():
    """Check that only one of each 'naughty' pupil exists."""
           
    selectNames = '''SELECT firstName, lastName, COUNT(*) AS Pupils
    FROM Child
    WHERE nice = FALSE
    GROUP BY firstName, lastName
    HAVING Pupils > 1;'''
    
    # Run query and store result
    result = cursor.execute(selectNames)
    
    rows = 0
    
    # Dislay all rows
    for row in result:

        # Display row
        print("\t", row)
        
        # Increment number of 
        rows += 1
    
    if rows == 0:
        print("\tNo duplicate names found.")



#
# Main program
#

# Create a connection to a database
# Creates a new database file, if it doesn’t exist
conn = sqlite3.connect('../Santa.db')

# Create a database cursor
cursor = conn.cursor()


# Child table
print("1. Child table")
childTable()


# Toy table
print("2. Toy table")
toyTable()


# Gift table
print("3. Gift table")
giftTable()


# Check for errors
print("4. Check for errors")
errorCheck()


# Close the connection to the database
conn.close()
