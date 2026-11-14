# Title: Model Table
# Author: Mr Friend
# Date: 14 Nov 2026

# Initialise variable
tableName: str = "Model"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    modelID INT NOT NULL
        CHECK (modelID > 0),
    manufacturerID INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    cpuSpeed REAL
        CHECK (cpuSpeed > 0.0),
    ram REAL
        CHECK (ram > 0.0),
    cores INT
        CHECK (cores >= 1),
    wifi BOOLEAN,
    releaseDate DATE,
    PRIMARY KEY (modelID),
    FOREIGN KEY (manufacturerID)
        REFERENCES Manufacturer (manufacturerID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write(f"INSERT INTO {tableName} VALUES ")
    
    fileOut.write("(" + data[0].strip() + ",")  # modelID
    fileOut.write(      data[1].strip() + ",")  # manufacturerID
    fileOut.write("'" + data[2].strip() + "',") # name
    fileOut.write(      data[3].strip() + ",")  # cpuSpeed
    fileOut.write(      data[4].strip() + ",")  # ram
    fileOut.write(      data[5].strip() + ",")  # cores
    fileOut.write(      data[6].strip() + ",")  # wifi
    fileOut.write("'" + data[7].strip() + "');\n")  # releaseDate

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
