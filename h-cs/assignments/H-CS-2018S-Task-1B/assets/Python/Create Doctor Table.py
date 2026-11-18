# Title: Doctor Table
# Author: Mr Friend
# Date: 18 Nov 2026

# Initialise variable
tableName: str = "Doctor"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    doctorID INT NOT NULL
        CHECK (doctorID >= 1),
    forename VARCHAR(15) NOT NULL,
    surname VARCHAR(15) NOT NULL,
    address VARCHAR(30) NOT NULL,
    postcode VARCHAR(8) NOT NULL,
    telNo VARCHAR(12) NOT NULL,
    dateQualified DATE NOT NULL,
    PRIMARY KEY (doctorID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write(f"INSERT INTO {tableName} VALUES ")
    
    fileOut.write("(" + data[0].strip() + ",")  # doctorID
    fileOut.write("'" + data[1].strip() + "',")  # forename
    fileOut.write("'" + data[2].strip() + "',")  # surname
    fileOut.write("'" + data[3].strip() + "',")  # address
    fileOut.write("'" + data[4].strip() + "',")  # postcode
    fileOut.write("'" + data[5].strip() + "',")  # telNo
    fileOut.write("'" + data[6].strip() + "');\n")  # dateQualified

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
