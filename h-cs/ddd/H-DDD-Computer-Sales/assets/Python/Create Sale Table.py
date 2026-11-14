# Title: Sale Table
# Author: Mr Friend
# Date: 14 Nov 2026

# Initialise variable
tableName: str = "Sale"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    saleID INT NOT NULL
        CHECK (saleID > 0),
    modelID INT NOT NULL,
    saleDate DATE,
    employeeID VARCHAR(10) NOT NULL,
    price FLOAT
        CHECK (price >= 0.0),
    PRIMARY KEY (saleID),
    FOREIGN KEY (modelID)
        REFERENCES Model (modelID),
    FOREIGN KEY (employeeID)
        REFERENCES Employee (employeeID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write(f"INSERT INTO {tableName} VALUES ")
    
    fileOut.write("(" + data[0].strip() + ",")  # saleID
    fileOut.write(      data[1].strip() + ",")  # modelID
    fileOut.write("'" + data[2].strip() + "',") # saleDate
    fileOut.write("'" + data[3].strip() + "',")  # employeeID
    fileOut.write(      data[4].strip() + ");\n")  # price

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
