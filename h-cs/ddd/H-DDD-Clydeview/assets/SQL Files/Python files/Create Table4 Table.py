# Title: Table4 Table
# Author: Mr Friend
# Date: 17 Nov 2025

# Files
fileIn = open("../CSV Files/Table4.csv", "r")
fileOut = open("../Table4.sql", "w")


# Create table

table = """CREATE TABLE Table4 (
    productID INT NOT NULL,
    productName VARCHAR(12) NOT NULL,
    buyPence INT NOT NULL
        CHECK(buyPence >= 0),
    sellPence INT NOT NULL
        CHECK(sellPence >= 0),
    PRIMARY KEY (productID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Table4 VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # productID
    fileOut.write( "\"" + data[1].strip() + "\",")  # productName
    fileOut.write(        data[2].strip() + ",")  # buyPence
    fileOut.write(        data[3].strip() + ");\n")  # sellPence

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
