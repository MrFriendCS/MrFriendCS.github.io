# Title: Create Publisher Table
# Author: Mr Friend
# Date: 30 Oct 2025

# Files
fileIn = open("../CSV files/Publisher.csv", "r")
fileOut = open("../Publisher.sql", "w")


# Create Table

table = """CREATE TABLE Publisher (
    publisherID INT NOT NULL,
    publisherName VARCHAR(30) NOT NULL,
    foundedYear INT NOT NULL,
    headquarters VARCHAR(10) NOT NULL,
    PRIMARY KEY (publisherID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Publisher VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # publisherID
    fileOut.write("\"" + data[1].strip() + "\",")  # publisherName
    fileOut.write(       data[2].strip() + ",")  # foundedYear
    fileOut.write("\"" + data[3].strip() + "\")")  # headquarters
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
