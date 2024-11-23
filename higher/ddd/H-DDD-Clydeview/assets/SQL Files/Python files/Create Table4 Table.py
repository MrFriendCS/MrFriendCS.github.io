# Title: Table4 Table
# Author: Mr Friend
# Date: 14 Nov 2024

# Files
fileIn = open("../CSV Files/Table4.csv", "r")
fileOut = open("../Table4.sql", "w")


# Create table

table = """CREATE TABLE Table4 (
    productID INT NOT NULL,
    productName VARCHAR(12) NOT NULL,
    buyingPrice INT NOT NULL
        CHECK(buyingPrice >= 0),
    sellingPrice INT NOT NULL
        CHECK(sellingPrice >= 0),
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
    fileOut.write(        data[2].strip() + ",")  # buyingPrice
    fileOut.write(        data[3].strip() + ");\n")  # sellingPrice

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
