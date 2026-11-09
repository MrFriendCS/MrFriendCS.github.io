# Title: Table5 Table
# Author: Mr Friend
# Date: 17 Nov 2025

# Files
fileIn = open("../CSV/Table5.csv", "r", encoding="utf-8")
fileOut = open("../SQL/Table5.sql", "w", encoding="utf-8")


# Create table

table = """CREATE TABLE Table5 (
    productName VARCHAR(20) NOT NULL,
    productID VARCHAR(50) NOT NULL,
    priceUK FLOAT NOT NULL
        CHECK(priceUK >= 0.00),
    PRIMARY KEY (productID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Table5 VALUES ")
    
    fileOut.write("(\""   + data[0].strip() + "\",")  # productName
    fileOut.write( "\"" + data[1].strip() + "\",")  # productID
    fileOut.write(        data[2].strip() + ");\n")  # priceUK

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
