# Title: Product Table
# Author: Mr Friend
# Date: 22 Nov 2024

# Files
fileIn = open("../CSV Files/Manufacturer-Product/Product.csv", "r")
fileOut = open("../Product.sql", "w")


# Create table

table = """CREATE TABLE Product (
    name VARCHAR(30) NOT NULL,
    code VARCHAR(4) NOT NULL,
    stock INT NOT NULL
        CHECK (stock >= 0 AND stock <= 50),
    onOrder BOOL,
    price REAL,
    manufacturerID INT NOT NULL,
    FOREIGN KEY (manufacturerID) 
        REFERENCES Manufacturer (manufacturerID),
    PRIMARY KEY (code)
);"""
              
fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Product VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # name
    fileOut.write( "\"" + data[1].strip() + "\",")  # code
    fileOut.write(        data[2].strip() + ",")  # stock
    if bool(int(data[3].strip())):  # onOrder
        fileOut.write("TRUE,")
    else:
        fileOut.write("FALSE,")
    fileOut.write(        data[4].strip() + ",")  # price
    fileOut.write(        data[5].strip() + ");\n")  # manufacturerID

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
