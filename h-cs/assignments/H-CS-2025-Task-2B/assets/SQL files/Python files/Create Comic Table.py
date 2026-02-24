# Title: Create Comic Table
# Author: Mr Friend
# Date: 30 Oct 2025

# Files
fileIn = open("../CSV files/Comic.csv", "r")
fileOut = open("../Comic.sql", "w")


# Create Table

table = """CREATE TABLE Comic (
    comicID INT NOT NULL,
    comicTitle VARCHAR(40) NOT NULL,
    issue INT NOT NULL,
    seriesID INT NOT NULL,
    publisherID INT NOT NULL,
    publicationDate DATE NOT NULL,
    genre VARCHAR(30) NOT NULL,
    valuation INT NOT NULL,
    PRIMARY KEY (comicID),
    FOREIGN KEY (publisherID)
        REFERENCES child(Publisher),
    FOREIGN KEY (seriesID)
        REFERENCES child(Series)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Comic VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # comicID
    fileOut.write("\"" + data[1].strip() + "\",")  # comicTitle
    fileOut.write(       data[2].strip() + ",")  # issue
    fileOut.write(       data[3].strip() + ",")  # seriesID
    fileOut.write(       data[4].strip() + ",")  # publisherID
    fileOut.write("\"" + data[5].strip() + "\",")  # publicationDate
    fileOut.write("\"" + data[6].strip() + "\",")  # genre
    fileOut.write(       data[7].strip() + ")")  # valuation
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
