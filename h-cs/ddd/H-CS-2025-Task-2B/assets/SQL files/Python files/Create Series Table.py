# Title: Create Series Table
# Author: Mr Friend
# Date: 30 Oct 2025

# Files
fileIn = open("../CSV files/Series.csv", "r")
fileOut = open("../Series.sql", "w")


# Create Table

table = """CREATE TABLE Series (
    seriesID INT NOT NULL,
    seriesName VARCHAR(30) NOT NULL,
    startYear INT NOT NULL,
    endYear INT NOT NULL,
    PRIMARY KEY (seriesID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Series VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # seriesID
    fileOut.write("\"" + data[1].strip() + "\",")  # seriesName
    fileOut.write(       data[2].strip() + ",")  # startYear
    fileOut.write(       data[3].strip() + ")")  # endYear
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
