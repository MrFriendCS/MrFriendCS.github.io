# Title: Create Teacher Table
# Author: Mr Friend
# Date: 10 Dec 2024

# Files
fileIn = open("../CSV files/Subject/Teacher.csv", "r")
fileOut = open("../Teacher.sql", "w")


# Create Table

table = """CREATE TABLE Teacher (
    staffID INT NOT NULL,
    subjectID INT NOT NULL,
    PRIMARY KEY (staffID, subjectID),
    FOREIGN KEY (staffID)
        REFERENCES Staff (staffID),
    FOREIGN KEY (subjectID)
        REFERENCES Subject (subjectID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Teacher VALUES ")
    
    fileOut.write(data[0].strip() + ",")  # staffID
    fileOut.write(data[1].strip() + ")")  # subjectID
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
