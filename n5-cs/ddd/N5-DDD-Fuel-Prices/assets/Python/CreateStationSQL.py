# Title: Create Station Table
# Author: Mr Friend
# Date: 17 Mar 2026

"""
Produce SQL for Station table and data.
"""

# Create Station Table

# Connect to file
fileSQL = open("../SQL/Station.sql", "w")

# Create table

table = """CREATE TABLE Station (
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
);"""

# Write to file
fileSQL.write(table + "\n")

# Close connection to file
fileSQL.close()


# Write data

# Connect to file
fileIn = open("../CSV/FuelPrice.csv", "r")
fileOut = open("../SQL/StationData.sql", "w")

# Ignore headers
line = fileIn.readline()

# Read first line of data
line = fileIn.readline()

id = 1

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Station VALUES (")
    
    fileOut.write(       str(id)         +   ",")  # id
    fileOut.write("\"" + data[0].strip() + "\",")  # name
    fileOut.write("\"" + data[1].strip() + "\",")  # postcode
    fileOut.write(       data[2].strip() +   ",")  # motorway
    fileOut.write(       data[3].strip() +   ",")  # supermarket
    fileOut.write(       data[4].strip() +   ",")  # latitude
    fileOut.write(       data[5].strip() +   ",")  # longitude
    fileOut.write(       data[6].strip() +   ",")  # e5
    fileOut.write(       data[7].strip() +   ",")  # e10
    fileOut.write(       data[8].strip() +   ",")  # b7s
    fileOut.write(       data[9].strip() +   ",")  # b7p
    fileOut.write("\"" + data[10].strip() + "\",") # open
    fileOut.write("\"" + data[11].strip() + "\",") # close
    fileOut.write("\"" + data[12].strip() + "\",") # openSun
    fileOut.write("\"" + data[13].strip() + "\",") # closeSun
    fileOut.write(       data[14].strip() +   ",") # carWash
    fileOut.write(       data[15].strip()        ) # toilets
    fileOut.write(");\n")
 
     # Read next line
    line = fileIn.readline()
    
    # Increment id
    id = id + 1


fileIn.close()
fileOut.close()