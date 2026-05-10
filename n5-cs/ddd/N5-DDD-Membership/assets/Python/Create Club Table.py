# Title: Create Club Table
# Author: Mr Friend
# Date: 9 May 2026


# Files
fileIn = open("../CSV/Club.csv", "r")
fileOut = open("../SQL/Club.sql", "w")


# Create Table

table = """CREATE TABLE Club (
    clubID VARCHAR(6) NOT NULL,
    name VARCHAR(30) NOT NULL,
    location VARCHAR(30) NOT NULL,
    type VARCHAR(20) NOT NULL,
    opened DATE
        CHECK (opened LIKE '____-__-__'),
    trainer BOOLEAN NOT NULL
        CHECK (trainer IN (0, 1)),
    rooms INT
        CHECK (rooms >= 0),
    PRIMARY KEY (clubID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Club VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # clubID
    fileOut.write("\""  + data[1].strip() + "\",")  # name
    fileOut.write("\""  + data[2].strip() + "\",")  # location
    fileOut.write("\""  + data[3].strip() + "\",")  # type
    fileOut.write("\""  + data[4].strip() + "\",")  # opened
    
    trainer = data[5].strip()
    
    if trainer == "FALSE":
        fileOut.write("FALSE,")  # trainer
    else:
        fileOut.write("TRUE,")  # trainer
    
    fileOut.write(         data[6].strip() + ");\n")  # rooms


    line = fileIn.readline()


fileIn.close()
fileOut.close()
