# Title: Drug Table
# Author: Mr Friend
# Date: 18 Nov 2026

# Initialise variable
tableName: str = "Drug"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    drugID VARCHAR(12) NOT NULL,
    drugName VARCHAR(30) NOT NULL,
    manufacturer VARCHAR(30) NOT NULL,
    dosage INT NOT NULL
        CHECK (dosage >= 0),
    cost REAL NOT NULL
        CHECK (cost >= 0.0),
    PRIMARY KEY (drugID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write(f"INSERT INTO {tableName} VALUES ")
    
    fileOut.write("('" + data[0].strip() + "',")    # drugID
    fileOut.write("'"  + data[1].strip() + "',")    # drugName
    fileOut.write("'"  + data[2].strip() + "',")    # manufacturer
    fileOut.write(       data[3].strip() + ",")     # dosage
    fileOut.write(       data[4].strip() + ");\n")  # cost

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
