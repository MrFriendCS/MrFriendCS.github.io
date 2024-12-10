# Title: Create Subject Table
# Author: Mr Friend
# Date: 10 Dec 2024

# Files
fileIn = open("../CSV files/Subject/Subject.csv", "r")
fileOut = open("../Subject.sql", "w")


# Create Table

table = """CREATE TABLE Subject (
    subjectID INT NOT NULL,
    subject VARCHAR(30) NOT NULL,
    PRIMARY KEY (subjectID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Subject VALUES ")
    
    fileOut.write(       data[0].strip() + ",")  # subjectID
    fileOut.write("\"" + data[1].strip() + "\")")  # subject
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
