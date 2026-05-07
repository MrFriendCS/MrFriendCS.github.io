# Title: N5 DDD Create Garage DB
# Author: Mr Friend
# Date: 23 Apr 2026

# Get extra code
import sqlite3


def dropVehicleTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Vehicle;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createVehicleTable():
    
    # SQL query
    createTable = '''CREATE TABLE Vehicle (
    vehReg VARCHAR(8),
    make VARCHAR(20),
    model VARCHAR(20),
    colour VARCHAR(20),
    PRIMARY KEY (vehReg)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertVehicleData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Vehicle.csv', 'r', encoding='utf-8')
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        vehReg = data[0].strip()
        make = data[1].strip()
        model = data[2].strip()
        colour = data[3].strip()
        
        # Create data
        values = '("' + vehReg + '","' + make + '","' + model + '","' + colour + '")'
        
        # SQL to insert data
        newData = 'INSERT INTO Vehicle VALUES' + values + ';'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropMoTtable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS MoT;
    '''

    # Drop the table
    cursor.execute(dropTable)

def createMoTtable():
    
    # SQL query
    createTable = '''CREATE TABLE MoT (
    motNo INT NOT NULL,
    vehReg VARCHAR(8),
    date DATE,
    pass BOOL,
    cost REAL,
    FOREIGN KEY (vehReg)  
        REFERENCES Vehicle(vehReg),
    PRIMARY KEY (motNo)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertMoTData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/MoT.csv', 'r', encoding='utf-8')
     
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        motNo = data[0].strip()
        vehReg = data[1].strip()
        date = data[2].strip()
        motPass = data[3].strip()
        cost = data[4].strip()
        
        # Create data
        values = '(' + motNo + ',"' + vehReg + '","' + date + '",' + \
                 motPass + ',' + cost + ')'
        
        # SQL to insert data
        newData = 'INSERT INTO MoT VALUES' + values + ';'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropRepairTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Repair;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createRepairTable():
    
    # SQL query
    createTable = '''CREATE TABLE Repair (
    repairID INT NOT NULL,
    vehReg VARCHAR(8) NOT NULL,
    date DATE,
    cost REAL,
    FOREIGN KEY (vehReg)
        REFERENCES vehicle (vehReg),
    PRIMARY KEY (repairID)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertRepairData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Repair.csv', 'r', encoding='utf-8')
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        repairID = data[0].strip()
        vehReg = data[1].strip()
        date = data[2].strip()
        cost = data[3].strip()
        
        # Create data
        values = '(' + repairID + ',"' + vehReg + '","' + date + '",' + cost +')'
        
        # SQL to insert data
        newData = 'INSERT INTO Repair VALUES' + values + ';'
        
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
conn = sqlite3.connect('../Garage.db')

# Create a database cursor
cursor = conn.cursor()


# Vehicle table
print("1. Vehicle table")
dropVehicleTable()
createVehicleTable()
insertVehicleData()


# MoT table
print("2. MoT table")
dropMoTtable()
createMoTtable()
insertMoTData()


# Repair table
print("3. Repair table")
dropRepairTable()
createRepairTable()
insertRepairData()


# Close the connection to the database
conn.close()
