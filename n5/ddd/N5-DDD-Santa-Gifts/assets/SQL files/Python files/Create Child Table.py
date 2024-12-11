# Title: Create Child Table
# Author: Mr Friend
# Date: 11 Dec 2024

# Files
fileIn = open("../CSV files/Child.csv", "r")
fileOut = open("../Child1.sql", "w")


# Create Table

table = """CREATE TABLE Child (
    childID INT NOT NULL,
    firstName VARCHAR(20),
    lastName VARCHAR(30),
    nice BOOLEAN,
    PRIMARY KEY (childID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Child VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # childID
    fileOut.write("\"" + data[1].strip() + "\",")  # firstName
    fileOut.write("\"" + data[2].strip() + "\",")  # lastName
    fileOut.write(       data[3].strip() + ")")  # nice
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
