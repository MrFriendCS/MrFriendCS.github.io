# Title: N5 DDD Fuel Prices Create DB
# Author: Mr Friend
# Date: 12 May 2026


# Get extra code
import sqlite3


def dropTable():
        
    # SQL query
    query = f'DROP TABLE IF EXISTS Station;'

    # Drop the table
    cursor.execute(query)


def createTable():
    
    # SQL query
    createTable = '''CREATE TABLE Station (
    id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    postcode VARCHAR(8) NOT NULL
        CHECK (LENGTH(postcode) >= 5), 
    motorway BOOL
        CHECK (motorway IN (0,1)),
    supermarket BOOL
        CHECK (supermarket IN (0,1)),
    latitude REAL,
    longitude REAL,
    e5 REAL
        CHECK (e5 >= 0.0),
    e10 REAL
        CHECK (e10 >= 0.0),
    b7s REAL
        CHECK (b7s >= 0.0),
    b7p REAL
        CHECK (b7p >= 0.0),
    open TIME
        CHECK (open LIKE "__:__:__"),
    close TIME
        CHECK (close LIKE "__:__:__"),
    openSun TIME
        CHECK (openSun LIKE "__:__:__"),
    closeSun TIME
        CHECK (closeSun LIKE "__:__:__"),
    carWash BOOL
        CHECK (carWash IN (0,1)),
    toilets BOOL
        CHECK (toilets IN (0,1)),
    PRIMARY KEY (id)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertData():
    
    # Get Station Data
    file = open("../SQL/StationData.sql", "r")

    # Read first record
    record = file.readline()

    while record != "":
        
        # Insert record
        cursor.execute(record)

        # Commit the new data
        conn.commit()
        
        # Read next record
        record = file.readline()

    file.close()


# Create a connection to the database
conn = sqlite3.connect('../FuelPrices.db')

# Create a database cursor
cursor = conn.cursor()

print("1. Drop table")
dropTable()

print("2. Create table")
createTable()

print("3.Insert data")
insertData()


# Close the connection to the database
conn.close()
