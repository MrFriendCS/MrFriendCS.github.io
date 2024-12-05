# Title: Create Taxi Table
# Author: Mr Friend
# Date: 30 Nov 2024

# Files
fileIn = open("../CSV files/Taxi.csv", "r")
fileOut = open("../Taxi.sql", "w")


# Create Table

table = """CREATE TABLE Taxi (
    taxiID INT NOT NULL,
    taxiReg VARCHAR(8) NOT NULL,
    make VARCHAR(20),
    model VARCHAR(20),
    colour VARCHAR(15),
    PRIMARY KEY (taxiID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Taxi VALUES ")
    
    fileOut.write("(" + str(data[0].strip()) + ",")  # taxiID
    fileOut.write(   "\"" + data[1].strip() + "\",")  # taxiReg
    fileOut.write(   "\"" + data[2].strip() + "\",")  # make
    fileOut.write(   "\"" + data[3].strip() + "\",")  # model
    fileOut.write(   "\"" + data[4].strip() + "\");\n")  # colour

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
