# Title: Patient Table
# Author: Mr Friend
# Date: 18 Nov 2026

# Initialise variable
tableName: str = "Patient"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    patientID INT NOT NULL
        CHECK (patientID >= 1),
    forename VARCHAR(15) NOT NULL,
    surname VARCHAR(15) NOT NULL,
    dateOfBirth DATE NOT NULL,
    address VARCHAR(30) NOT NULL,
    contactNo VARCHAR(12) NOT NULL,
    PRIMARY KEY (patientID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write(f"INSERT INTO {tableName} VALUES ")
    
    fileOut.write("(" + data[0].strip() + ",")      # patientID
    fileOut.write("'" + data[1].strip() + "',")     # forename
    fileOut.write("'" + data[2].strip() + "',")     # surname
    fileOut.write("'" + data[3].strip() + "',")     # dateOfBirth
    fileOut.write("'" + data[4].strip() + "',")     # address
    fileOut.write("'" + data[5].strip() + "');\n")  # contactNo

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
