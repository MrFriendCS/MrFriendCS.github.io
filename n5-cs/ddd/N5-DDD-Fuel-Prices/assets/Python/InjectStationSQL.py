# Title: Inject Station SQL
# Author: Mr Friend
# Date: 14 Mar 2026


# Get extra code
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('../FuelPrices.db')

# Create a database cursor
cursor = conn.cursor()

# Drop the existing table
cursor.execute("DROP TABLE Station;")


# Get Station SQL
file = open("../SQL/Station.sql", "r")
stationSQL = file.read()
file.close()

# Create the new table
cursor.execute(stationSQL)


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


# Close the connection to the database
conn.close()
