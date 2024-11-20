# Title: SuperHero Table
# Author: Mr Friend
# Date: 20 Nov 2024

# Files
fileIn = open("../CSV files/Product.csv", "r")
fileOut = open("../Product.sql", "w")


# Table
tableProduct = """CREATE TABLE Product (
    productName VARCHAR(40) NOT NULL,
    productCode VARCHAR(40),
    numberInStock INT,
    onOrder BOOL,
    costPrice REAL,
    manufacturerID INT NOT NULL,
    FOREIGN KEY (manufacturerID) 
        REFERENCES Manufacturer (manufacturerID),
    PRIMARY KEY (productCode)
);"""
              
fileOut.write(tableProduct + "\n\n")

# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Product VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # productName
    fileOut.write( "\"" + data[1].strip() + "\",")  # productCode
    fileOut.write(        data[2].strip() + ",")  # numberInStock
    if bool(int(data[3].strip())):  # onOrder
        fileOut.write("TRUE,")
    else:
        fileOut.write("FALSE,")
    fileOut.write(        data[4].strip() + ",")  # costPrice
    fileOut.write(        data[5].strip() + ");\n")  # manufacturerID

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
