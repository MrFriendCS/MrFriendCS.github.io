# Title: PrescribedDrug Table
# Author: Mr Friend
# Date: 18 Nov 2026

# Initialise variable
tableName: str = "PrescribedDrug"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    drugID TEXT NOT NULL,
    patientID INT NOT NULL
        CHECK (patientID >= 1),
    datePrescribed DATE,
    PRIMARY KEY (drugID, patientID, datePrescribed),
    FOREIGN KEY (drugID)
        REFERENCES Drug (drugID),
    FOREIGN KEY (patientID)
        REFERENCES Patient (patientID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write(f"INSERT INTO {tableName} VALUES ")
    
    fileOut.write("('" + data[0].strip() + "',")     # drugID
    fileOut.write(       data[1].strip() + ",")      # patientID
    fileOut.write("'"  + data[2].strip() + "');\n")  # datePrescribed

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
