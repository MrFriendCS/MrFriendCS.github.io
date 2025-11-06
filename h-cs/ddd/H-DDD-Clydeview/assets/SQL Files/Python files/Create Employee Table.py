# Title: Employee Table
# Author: Mr Friend
# Date: 22 Nov 2024

# Files
fileIn = open("../CSV files/Employee.csv", "r")
fileOut = open("../Employee.sql", "w")


# Create table

table = """CREATE TABLE Employee (
    employeeID INT NOT NULL,
    jobTitle VARCHAR(8) NOT NULL,
    name VARCHAR(20),
    building VARCHAR(2),
    yearsEmployed INT NOT NULL
        CHECK(yearsEmployed >= 0),
    PRIMARY KEY (employeeID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Employee VALUES ")
    
    fileOut.write("(" +  data[0].strip() + ",")  # employeeID
    fileOut.write("\"" + data[1].strip() + "\",")  # jobTitle
    fileOut.write("\"" + data[2].strip() + "\",")  # name
    fileOut.write("\"" + data[3].strip() + "\",")  # building
    fileOut.write(       data[4].strip() + ");\n")  # yearsEmployeed

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
