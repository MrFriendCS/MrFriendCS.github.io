# Title: Create ComicCharacter Table
# Author: Mr Friend
# Date: 30 Dec 2025

# Files
fileIn = open("../CSV files/ComicCharacter.csv", "r")
fileOut = open("../ComicCharacter.sql", "w")


# Create Table

table = """CREATE TABLE ComicCharacter (
    comicCharacterID INT NOT NULL,
    comicID INT NOT NULL,
    characterID INT NOT NULL,
    mainCharacter INT NOT NULL,
    PRIMARY KEY (comicCharacterID),
    FOREIGN KEY (comicID)
        REFERENCES child(Comic),
    FOREIGN KEY (characterID)
        REFERENCES child(CharacterInfo)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO ComicCharacter VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # comicCharacterID
    fileOut.write(       data[1].strip() + ",")  # comicID
    fileOut.write(       data[2].strip() + ",")  # characterID
    fileOut.write(       data[3].strip() + ")")  # mainCharacter
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
