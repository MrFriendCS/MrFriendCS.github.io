# Title: Table4 Table
# Author: Mr Friend
# Date: 17 Nov 2025

# Files
fileIn = open("../CSV/Table4.csv", "r")
fileOut = open("../SQL/Table4.sql", "w")


# Create table

table = """CREATE TABLE Table4 (
    productID INT NOT NULL,
    productName VARCHAR(12) NOT NULL,
    buyPricePence INT NOT NULL
        CHECK(buyPricePence >= 0),
    sellPricePence INT NOT NULL
        CHECK(sellPricePence >= 0),
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
    fileOut.write(        data[2].strip() + ",")  # buyPricePence
    fileOut.write(        data[3].strip() + ");\n")  # sellPricePence

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
