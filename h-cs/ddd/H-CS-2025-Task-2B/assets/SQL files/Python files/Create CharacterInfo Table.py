# Title: Create CharacterInfo Table
# Author: Mr Friend
# Date: 30 Oct 2025

# Files
fileIn = open("../CSV files/CharacterInfo.csv", "r")
fileOut = open("../CharacterInfo.sql", "w")


# Create Table

table = """CREATE TABLE CharacterInfo (
    characterID INT NOT NULL,
    characterName VARCHAR(30) NOT NULL,
    alias VARCHAR(30) NOT NULL,
    creator VARCHAR(30) NOT NULL,
    PRIMARY KEY (characterID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO CharacterInfo VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # characterID
    fileOut.write("\"" + data[1].strip() + "\",")  # characterName
    fileOut.write("\"" + data[2].strip() + "\",")  # alias
    fileOut.write("\"" + data[3].strip() + "\")")  # creator
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
