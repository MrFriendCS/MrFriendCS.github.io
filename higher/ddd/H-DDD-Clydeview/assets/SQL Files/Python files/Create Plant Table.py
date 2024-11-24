# Title: Plant Table
# Author: Mr Friend
# Date: 21 Nov 2024

# Files
fileIn = open("../CSV Files/Plant.csv", "r")
fileOut = open("../Plant.sql", "w")


# Create table

table = """CREATE TABLE Plant (
    category VARCHAR(10) NOT NULL,
    name VARCHAR(20) NOT NULL,
    variety VARCHAR(20) NOT NULL,
    code VARCHAR(3) NOT NULL,
    referenceID VARCHAR(3) NOT NULL,
    unit INT NOT NULL 
        CHECK(unit >= 0),
    price FLOAT NOT NULL
        CHECK(price >= 0),
    height VARCHAR(1) NOT NULL 
        CHECK(height IN("S","M","T")),
    PRIMARY KEY (referenceID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Plant VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # category
    fileOut.write( "\"" + data[1].strip() + "\",")  # plantName
    fileOut.write( "\"" + data[2].strip() + "\",")  # variety
    fileOut.write( "\"" + data[3].strip() + "\",")  # code
    fileOut.write( "\"" + data[4].strip() + "\",")  # referenceID
    fileOut.write(        data[5].strip() + ",")  # unit
    fileOut.write(        data[6].strip() + ",")  # price
    fileOut.write( "\"" + data[7].strip() + "\");\n")  # height

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
