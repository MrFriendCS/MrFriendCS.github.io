# Title: Create Employee & Laptop Tables
# Author: Mr Friend
# Date: 14 Jan 2024

# Create Employee table

employeeTable = """CREATE TABLE Employee (
    id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    role VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (id)
);"""

fileIn = open("employee.csv", "r")
fileOut = open("employee.sql", "w")

fileOut.write(employeeTable + "\n\n")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO employee VALUES ")
    
    fileOut.write("(" +   data[0].strip() + ",")  # id
    fileOut.write( "\"" + data[1].strip() + "\",")  # name
    fileOut.write( "\"" + data[2].strip() + "\",")  # developer
    fileOut.write(        data[3].strip() + ");\n")  # age

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create Borrow table

borrowTable = """CREATE TABLE Borrow (
    id INT NOT NULL,
    laptop INT NOT NULL,
    borrowed DATE NOT NULL,
    returned BOOL NOT NULL,
    FOREIGN KEY (id)
        REFERENCES employee (id),
    PRIMARY KEY (id, laptop)
);"""

fileIn = open("borrow.csv", "r")
fileOut = open("borrow.sql", "w")

fileOut.write(borrowTable + "\n\n")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Borrow VALUES ")
    
    fileOut.write("(" +   data[0].strip() + ",")  # id
    fileOut.write(        data[1].strip() + ",")  # laptop
    fileOut.write( "\"" + data[2].strip() + "\",")  # borrowed
    fileOut.write(        data[3].strip() + ");\n")  # returned

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create Laptop table

borrowTable = """CREATE TABLE Laptop (
    laptop INT NOT NULL,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20) NOT NULL,
    value REAL NOT NULL,
    working BOOL NOT NULL,
    PRIMARY KEY (laptop)
);"""

fileIn = open("laptop.csv", "r")
fileOut = open("laptop.sql", "w")

fileOut.write(laptopTable + "\n\n")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Laptop VALUES ")
    
    fileOut.write("(" +   data[0].strip() + ",")  # laptop
    fileOut.write( "\"" + data[1].strip() + "\",")  # make
    fileOut.write( "\"" + data[2].strip() + "\",")  # model
    fileOut.write(        data[3].strip() + ",")  # value
    fileOut.write(        data[4].strip() + ");\n")  # working

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()