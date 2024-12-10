# Title: Create Address Table
# Author: Mr Friend
# Date: 10 Dec 2024

# Files
fileIn = open("../CSV files/Pupil/Address.csv", "r")
fileOut = open("../Address.sql", "w")


# Create Table

table = """CREATE TABLE Address (
    addressID INT NOT NULL,
    firstLine VARCHAR(30) NOT NULL,
    town VARCHAR(30) NOT NULL,
    postcode VARCHAR(8) NOT NULL,
    phone VARCHAR(12),
    PRIMARY KEY(addressID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Address VALUES ")
    
    fileOut.write(       data[0].strip() + ",")  # addressID
    fileOut.write("\"" + data[1].strip() + "\",")  # firstLine
    fileOut.write("\"" + data[2].strip() + "\",")  # town
    fileOut.write("\"" + data[3].strip() + "\",")  # postcode
    fileOut.write("\"" + data[4].strip() + "\")")  # phone
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
