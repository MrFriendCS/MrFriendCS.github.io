# Title: Create Pupil Table
# Author: Mr Friend
# Date: 19 Dec 2024

"""
Produce SQL for Pupil table.
"""

# Create Pupil Table

# Files
fileIn = open("../CSV files/Pupil.csv", "r")
fileOut = open("../Pupil.sql", "w")

# Create table

table = """CREATE TABLE Pupil (
    id INT NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    house INT NOT NULL,
    year VARCHAR(2) NOT NULL
        CHECK (year IN ("S1", "S2", "S3", "S4", "S5", "S6")),
    age INT NOT NULL
        CHECK (age >= 11 AND age <= 18),
    PRIMARY KEY (id),
    FOREIGN KEY (house)
        REFERENCES House (id)
);"""
              
fileOut.write(table + "\n\n")


# Write data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Pupil VALUES (")
    
    fileOut.write("\"" + data[0].strip() + "\",")  # id
    fileOut.write("\"" + data[1].strip() + "\",")  # lastName
    fileOut.write("\"" + data[2].strip() + "\",")  # firstName
    fileOut.write("\"" + data[3].strip() + "\",")  # house
    fileOut.write("\"" + data[4].strip() + "\",")  # year
    fileOut.write(       data[5].strip()        )  # age
    fileOut.write(");\n")
 
    line = fileIn.readline()


fileIn.close()
fileOut.close()