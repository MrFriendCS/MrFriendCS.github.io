# Title: Create Toy Table
# Author: Mr Friend
# Date: 15 Dec 2025

# Files
fileIn = open("../CSV files/ToyList.csv", "r")
fileOut = open("../Toy.sql", "w")


# Create Table

table = """CREATE TABLE Toy (
    toyID INT NOT NULL,
    item VARCHAR(50) NOT NULL,
    cost FLOAT NOT NULL,
    PRIMARY KEY (toyID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

toyID = 0

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Toy VALUES (")
    
    fileOut.write(       str(toyID)      + ",")  # toyID
    fileOut.write("\"" + data[0].strip() + "\",")  # item
    fileOut.write(       data[1].strip() + ")")  # cost
    fileOut.write(";\n")

    line = fileIn.readline()
    toyID = toyID + 1
    
fileIn.close()
fileOut.close()
