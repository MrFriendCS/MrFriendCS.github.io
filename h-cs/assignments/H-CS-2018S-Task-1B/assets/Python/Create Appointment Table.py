# Title: Appointment Table
# Author: Mr Friend
# Date: 18 Nov 2026

# Initialise variable
tableName: str = "Appointment"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    appDate DATE NOT NULL,
    appTime TIME NOT NULL,
    doctorID INT NOT NULL,
    patientID INT NOT NULL,
    PRIMARY KEY (appDate, appTime, doctorID)
    FOREIGN KEY (doctorID)
        REFERENCES Doctor (doctorID),
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
    
    fileOut.write("('" + data[0].strip() + "',")    # appDate
    fileOut.write("'"  + data[1].strip() + "',")    # appTime
    fileOut.write(       data[2].strip() + ",")     # doctorID
    fileOut.write(       data[3].strip() + ");\n")  # patientID

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
