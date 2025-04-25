# Title: Create Staff Table
# Author: Mr Friend
# Date: 10 Dec 2024

# Files
fileIn = open("../CSV files/Subject/Staff.csv", "r")
fileOut = open("../Staff.sql", "w")


# Create Table

table = """CREATE TABLE Staff (
    staffID INT NOT NULL,
    title VARCHAR(6) NOT NULL,
    lastName VARCHAR(30),
    role VARCHAR(15) NOT NULL,
    PRIMARY KEY (staffID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Staff VALUES ")
    
    fileOut.write(       data[0].strip() + ",")  # staffID
    fileOut.write("\"" + data[1].strip() + "\",")  # title
    fileOut.write("\"" + data[2].strip() + "\",")  # surname
    fileOut.write("\"" + data[3].strip() + "\")")  # role
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
