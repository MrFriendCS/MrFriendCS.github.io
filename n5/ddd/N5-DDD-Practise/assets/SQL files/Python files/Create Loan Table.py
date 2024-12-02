# Title: Create Loan Table
# Author: Mr Friend
# Date: 2 Dec 2024

# Files
fileIn = open("../CSV files/Employee/Loan.csv", "r")
fileOut = open("../Loan.sql", "w")


# Create Table

table = """CREATE TABLE Loan (
    id INT NOT NULL,
    laptop INT NOT NULL,
    borrowed DATE NOT NULL,
    returned BOOL NOT NULL,
    FOREIGN KEY (id)
        REFERENCES employee (id),
    PRIMARY KEY (id, laptop)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Loan VALUES ")
    
    fileOut.write("(" +   data[0].strip() + ",")  # id
    fileOut.write(        data[1].strip() + ",")  # laptop
    fileOut.write( "\"" + data[2].strip() + "\",")  # borrowed
    fileOut.write(        data[3].strip() + ");\n")  # returned

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
