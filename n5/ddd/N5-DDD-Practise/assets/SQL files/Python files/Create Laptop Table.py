# Title: Create Employee Table
# Author: Mr Friend
# Date: 2 Dec 2024

# Files
fileIn = open("../CSV files/Employee/Laptop.csv", "r")
fileOut = open("../Laptop.sql", "w")


# Create Table

table = """CREATE TABLE Laptop (
    laptop INT NOT NULL,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20) NOT NULL,
    value REAL NOT NULL,
    working BOOL NOT NULL,
    PRIMARY KEY (laptop)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Laptop VALUES ")
    
    fileOut.write("(" +   data[0].strip() + ",")  # laptop
    fileOut.write( "\"" + data[1].strip() + "\",")  # make
    fileOut.write( "\"" + data[2].strip() + "\",")  # model
    fileOut.write(        data[3].strip() + ",")  # value
    fileOut.write(        data[4].strip() + ");\n")  # working

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
