# Title: Create Prisoner Table
# Author: Mr Friend
# Date: 5 Dec 2024

# Files
fileIn = open("../CSV files/Prisoner.csv", "r")
fileOut = open("../Prisoner.sql", "w")


# Create Table

table = """CREATE TABLE Prisoner (
    prisonID INT NOT NULL,
    surname VARCHAR(30) NOT NULL 
        CHECK (LENGTH(surname) >= 3),
    forename VARCHAR(20) NOT NULL 
        CHECK (LENGTH(forename) >= 3),
    hair VARCHAR(6) 
        CHECK (hair IN ("Black", "Blond", "Brown", "Grey",
                        "None", "Red", "White")),
    eyes VARCHAR(5) 
        CHECK (eyes IN ("Amber", "Black", "Blue", "Brown",
                        "Green", "Hazel", "Grey")),
    height FLOAT NOT NULL
        CHECK (height >= 1.3
           AND height <= 2.5),
    conviction VARCHAR(20) NOT NULL,
    open BOOLEAN NOT NULL,
    dob DATE NOT NULL,
    PRIMARY KEY (prisonID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Prisoner VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # prisonID
    fileOut.write("\"" + data[1].strip() + "\",")  # surname
    fileOut.write("\"" + data[2].strip() + "\",")  # forename
    fileOut.write("\"" + data[3].strip() + "\",")  # hair
    fileOut.write("\"" + data[4].strip() + "\",")  # eyes
    fileOut.write(       data[5].strip() + ",")  # height
    fileOut.write("\"" + data[6].strip() + "\",")  # conviction
    fileOut.write(       data[7].strip() + ",")  # open
    fileOut.write("\"" + data[8].strip() + "\")")  # dob
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
