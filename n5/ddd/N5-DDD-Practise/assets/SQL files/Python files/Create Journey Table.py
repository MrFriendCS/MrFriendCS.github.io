# Title: Create Journey Table
# Author: Mr Friend
# Date: 30 Nov 2024


def adjustTime(time):
    """Ensure 24-hour format is used"""
    
    if len(time) == 7:
        time = "0" + time
        
    return time


# Files
fileIn = open("../CSV files/Journey.csv", "r")
fileOut = open("../Journey.sql", "w")


# Create Table

table = """CREATE TABLE journey (
    journeyID INT NOT NULL,
    taxiID INT NOT NULL,
    pickUpDate DATE,
    pickUpTime TIME,
    pax INT
        CHECK (pax >= 1),
    pickUpLoc VARCHAR(30),
    dropOffLoc VARCHAR(30),
    FOREIGN KEY("taxiID") REFERENCES "taxi"("taxiID")
    PRIMARY KEY("journeyID")
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    data[3] = adjustTime(data[3])
    
    fileOut.write("INSERT INTO Journey VALUES ")
    
    fileOut.write("(" + str(data[0].strip()) + ",")  # journeyID
    fileOut.write(      str(data[1].strip()) + ",")  # taxiID
    fileOut.write(   "\"" + data[2].strip() + "\",")  # pickUpDate
    fileOut.write(   "\"" + data[3].strip() + "\",")  # pickUpTime
    fileOut.write(      str(data[4].strip()) + ",")  # pax
    fileOut.write(   "\"" + data[5].strip() + "\",")  # pickUpLoc
    fileOut.write(   "\"" + data[6].strip() + "\");\n")  # dropOffLoc

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
