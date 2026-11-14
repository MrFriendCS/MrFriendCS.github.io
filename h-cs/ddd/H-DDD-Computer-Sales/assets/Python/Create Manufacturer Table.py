# Title: Manufacturer Table
# Author: Mr Friend
# Date: 14 Nov 2026

# Initialise variable
tableName: str = "Manufacturer"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    manufacturerID INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    website VARCHAR(50),
    yearFounded INT
        CHECK (yearFounded >= 1900),
    trading BOOL NOT NULL,
    PRIMARY KEY (manufacturerID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write(f"INSERT INTO {tableName} VALUES ")
    
    fileOut.write("('" + data[0].strip() + "',")  # manufacturerID
    fileOut.write("'" +  data[1].strip() + "',")  # name
    fileOut.write("'" +  data[2].strip() + "',")  # website
    fileOut.write(       data[3].strip() + ",")  # yearFounded
    fileOut.write(       data[4].strip() + ");\n")  # trading

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
