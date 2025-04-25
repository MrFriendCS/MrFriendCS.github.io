# Title: Table2 Table
# Author: Mr Friend
# Date: 14 Nov 2024

# Files
fileIn = open("../CSV Files/Table2.csv", "r")
fileOut = open("../Table2.sql", "w")


# Create table

table = """CREATE TABLE Table2 (
    staffID INT NOT NULL,
    forename VARCHAR(12) NOT NULL,
    surname VARCHAR(12) NOT NULL,
    hourlyRate FLOAT NOT NULL
        CHECK(hourlyRate >= 0),
    hoursWorked INT NOT NULL
        CHECK(hoursWorked >= 0),
    PRIMARY KEY (staffID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Table2 VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # PupilID
    fileOut.write( "\"" + data[1].strip() + "\",")  # Forename
    fileOut.write( "\"" + data[2].strip() + "\",")  # Surname
    fileOut.write(        data[3].strip() + ",")  # hourlyRate
    fileOut.write(        data[4].strip() + ");\n")  # hoursWorked

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
