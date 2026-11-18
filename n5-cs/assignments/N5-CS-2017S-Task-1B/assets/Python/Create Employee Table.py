# Title: Sale Table
# Author: Mr Friend
# Date: 14 Nov 2026

# Initialise variable
tableName: str = "Employee"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    employeeNumber INT NOT NULL
        CHECK (employeeNumber >= 1000
           AND employeeNumber <= 9999),
    firstName VARCHAR(15) NOT NULL,
    surname VARCHAR(15) NOT NULL,
    address VARCHAR(50) NOT NULL,
    contactNumber VARCHAR(11) NOT NULL
        CHECK (LENGTH(contactNumber) = 11),
    drivingLicence BOOL NOT NULL,
    PRIMARY KEY (employeeNumber)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write(f"INSERT INTO {tableName} VALUES ")
    
    fileOut.write("(" + data[0].strip() + ",")    # employeeNumber
    fileOut.write("'" + data[1].strip() + "',")   # firstName
    fileOut.write("'" + data[2].strip() + "',")   # surname
    fileOut.write("'" + data[3].strip() + "',")   # address
    fileOut.write("'" + data[4].strip() + "',")   # contactNumber
    fileOut.write(      data[5].strip() + ");\n") # drivingLicence

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
