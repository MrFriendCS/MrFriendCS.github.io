# Title: Question6 Table
# Author: Mr Friend
# Date: 14 Nov 2024

# Files
fileIn = open("../CSV Files/Question6.csv", "r")
fileOut = open("../Question6.sql", "w")


# Create table

table = """CREATE TABLE Question6 (
    fishType VARCHAR(12) NOT NULL,
    pricePerKilo FLOAT NOT NULL
        CHECK(pricePerKilo >= 0.00),
    numberOfKilos FLOAT NOT NULL
        CHECK(numberOfKilos >= 0.0),
    PRIMARY KEY (fishType)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Question6 VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # fishType
    fileOut.write(        data[1].strip() + ",")  # pricePerKilo
    fileOut.write(        data[2].strip() + ");\n")  # numberOfKilos

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
