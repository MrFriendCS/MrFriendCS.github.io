# Title: Business Tables: Supplier to Customer
# Author: Mr Friend
# Date: 23 Jan 2024

# Create Customer Table

fileIn = open("Customer.csv", "r")
fileOut = open("Customer.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

table = """CREATE TABLE Customer (
    customerID INT NOT NULL,
    shopName VARCHAR(30) NOT NULL,
    address VARCHAR(30) NOT NULL,
    city VARCHAR(20) NOT NULL,
    postcode VARCHAR(8) NOT NULL,
    contactName VARCHAR(40) NOT NULL,
    email VARCHAR(50),
    PRIMARY KEY (customerID)
);"""

fileOut.write(table + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Customer VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # customerID
    fileOut.write( "\"" + data[1].strip() + "\",")  # shopName
    fileOut.write( "\"" + data[2].strip() + "\",")  # address
    fileOut.write( "\"" + data[3].strip() + "\",")  # city
    fileOut.write( "\"" + data[4].strip() + "\",")  # postcode
    fileOut.write( "\"" + data[5].strip() + "\",")  # contactName
    if data[6].strip() != "":  # email
        fileOut.write( "\"" + data[6].strip() + "\");\n")
    else:
        fileOut.write("NULL);\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create CustomerOrder Table

fileIn = open("CustomerOrder.csv", "r")
fileOut = open("CustomerOrder.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

table = """CREATE TABLE CustomerOrder (
    orderNumber INT NOT NULL,
    orderDate DATE NOT NULL,
    customerID INT NOT NULL,
    FOREIGN KEY (customerID)
        REFERENCES Customer (customerID),
    PRIMARY KEY (orderNumber)
);"""

fileOut.write(table + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO CustomerOrder VALUES ")
    
    fileOut.write("("  + data[0].strip() + ",")  # orderNumber
    fileOut.write("\"" + data[1].strip() + "\",")  # orderDate
    fileOut.write(       data[2].strip() + ");\n")  # customerID

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create Supplier Table

fileIn = open("Supplier.csv", "r")
fileOut = open("Supplier.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

table = """CREATE TABLE Supplier (
    supplierID VARCHAR(5) NOT NULL,
    name VARCHAR(30) NOT NULL,
    address VARCHAR(30) NOT NULL,
    city VARCHAR(20) NOT NULL,
    postcode VARCHAR(8) NOT NULL,
    PRIMARY KEY (supplierID)
);"""

fileOut.write(table + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Supplier VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # supplierID
    fileOut.write( "\"" + data[1].strip() + "\",")  # name
    fileOut.write( "\"" + data[2].strip() + "\",")  # address
    fileOut.write( "\"" + data[3].strip() + "\",")  # city
    fileOut.write( "\"" + data[4].strip() + "\");\n")  # postcode

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create Product Table

fileIn = open("Product.csv", "r")
fileOut = open("Product.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

table = """CREATE TABLE Product (
    productID VARCHAR(10) NOT NULL,
    supplierID VARCHAR(5) NOT NULL,
    name VARCHAR(30) NOT NULL,
    price REAL NOT NULL,
    description VARCHAR(100) NOT NULL,
    FOREIGN KEY (supplierID)
        REFERENCES Supplier (supplierID),
    PRIMARY KEY (productID)
);"""

fileOut.write(table + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Product VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # productID
    fileOut.write( "\"" + data[1].strip() + "\",")  # supplierID
    fileOut.write( "\"" + data[2].strip() + "\",")  # name
    fileOut.write(        data[3].strip() + ",")  # price
    fileOut.write( "\"" + data[4].strip() + "\");\n")  # description

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create OrderProduct Table

fileIn = open("OrderProduct.csv", "r")
fileOut = open("OrderProduct.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

table = """CREATE TABLE OrderProduct (
    orderNumber INT NOT NULL,
    productID VARCHAR(10) NOT NULL,
    quantity INT NOT NULL
        CHECK(quantity > 0),
    FOREIGN KEY (orderNumber)
        REFERENCES CustomerOrder (orderNumber),
    FOREIGN KEY (productID)
        REFERENCES Product (productID),
    PRIMARY KEY (orderNumber, productID)
);"""

fileOut.write(table + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO OrderProduct VALUES ")
    
    fileOut.write("("  + data[0].strip() + ",")  # orderNumber
    fileOut.write("\"" + data[1].strip() + "\",")  # productID
    fileOut.write(       data[2].strip() + ");\n")  # quantity

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()