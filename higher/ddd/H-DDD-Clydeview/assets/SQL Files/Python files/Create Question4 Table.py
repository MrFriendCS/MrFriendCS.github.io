# Title: Question4 Table
# Author: Mr Friend
# Date: 14 Nov 2024

# Create table

fileIn = open("../CSV Files/Question4.csv", "r")
fileOut = open("../Question4.sql", "w")

table = """CREATE TABLE Question4 (
    ProductID INT NOT NULL,
    productName VARCHAR(12) NOT NULL,
    buyingPrice INT NOT NULL
        CHECK(buyingPrice >= 0),
    sellingPrice INT NOT NULL
        CHECK(sellingPrice >= 0),
    PRIMARY KEY (ProductID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Question4 VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # ProductID
    fileOut.write( "\"" + data[1].strip() + "\",")  # productName
    fileOut.write(        data[2].strip() + ",")  # buyingPrice
    fileOut.write(        data[3].strip() + ");\n")  # sellingPrice

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
