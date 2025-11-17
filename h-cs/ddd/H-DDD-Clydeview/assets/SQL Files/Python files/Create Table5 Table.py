# Title: Table5 Table
# Author: Mr Friend
# Date: 17 Nov 2025

# Files
fileIn = open("../CSV Files/Table5.csv", "r")
fileOut = open("../Table5.sql", "w")


# Create table

table = """CREATE TABLE Table5 (
    productName VARCHAR(20) NOT NULL,
    productID VARCHAR(50) NOT NULL,
    pricePounds FLOAT NOT NULL
        CHECK(pricePounds >= 0.00),
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
    fileOut.write(        data[2].strip() + ");\n")  # pricePounds

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
