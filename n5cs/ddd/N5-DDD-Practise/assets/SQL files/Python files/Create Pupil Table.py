# Title: Create Pupil Table
# Author: Mr Friend
# Date: 5 Dec 2024

# Files
fileIn = open("../CSV files/Pupil/Pupil.csv", "r")
fileOut = open("../Pupil.sql", "w")


# Create Table

table = """CREATE TABLE Pupil (
    pupilID INT NOT NULL,
    addressID INT,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    dob DATE NOT NULL,
    age INT NOT NULL
        CHECK ("age" >= 0),
    enrolled BOOL NOT NULL,
    PRIMARY KEY("pupilID")
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Pupil VALUES ")
    
    fileOut.write(       data[0].strip() + ",")  # pupilID
    fileOut.write(       data[1].strip() + ",")  # addressID
    fileOut.write("\"" + data[2].strip() + "\",")  # firstName
    fileOut.write("\"" + data[3].strip() + "\",")  # lastName
    fileOut.write("\"" + data[4].strip() + "\",")  # dob
    fileOut.write(       data[5].strip() + ",")  # age
    fileOut.write(       data[6].strip() + ")")  # enrolled
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
