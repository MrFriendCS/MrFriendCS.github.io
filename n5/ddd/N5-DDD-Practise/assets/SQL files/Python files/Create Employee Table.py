# Title: Create Employee Table
# Author: Mr Friend
# Date: 2 Dec 2024

# Files
fileIn = open("../CSV files/Employee/Employee.csv", "r")
fileOut = open("../Employee.sql", "w")


# Create Table

table = """CREATE TABLE Employee (
    id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    role VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (id)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Employee VALUES ")
    
    fileOut.write("(" +   data[0].strip() + ",")  # id
    fileOut.write( "\"" + data[1].strip() + "\",")  # name
    fileOut.write( "\"" + data[2].strip() + "\",")  # developer
    fileOut.write(        data[3].strip() + ");\n")  # age

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
