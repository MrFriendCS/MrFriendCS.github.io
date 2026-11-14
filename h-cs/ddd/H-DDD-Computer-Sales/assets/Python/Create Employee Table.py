# Title: Employee Table
# Author: Mr Friend
# Date: 14 Nov 2026

# Initialise variable
tableName: str = "Employee"

# Files
fileIn = open(f"../CSV/{tableName}.csv", "r", encoding="UTF-8")
fileOut = open(f"../SQL/{tableName}.sql", "w", encoding="UTF-8")


# Table
table = f"""CREATE TABLE {tableName} (
    employeeID VARCHAR(10) NOT NULL,
    firstName VARCHAR(15) NOT NULL
        CHECK (LENGTH(firstName) >= 3),
    lastName VARCHAR(20) NOT NULL
        CHECK (LENGTH(lastName) >= 3),
    houseNo INT
        CHECK (houseNo > 0),
    street VARCHAR(20),
    town VARCHAR(20),
    county VARCHAR(20),
    postcode VARCHAR(8),
    phone VARCHAR(20)
        CHECK (LENGTH(phone) = 11),
    daysPerWeek REAL
        CHECK (daysPerWeek >= 0.0 AND daysPerWeek <= 7.0),
    PRIMARY KEY (employeeID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write(f"INSERT INTO {tableName} VALUES ")
    
    fileOut.write("('" + data[0].strip() + "',")  # employeeID
    fileOut.write("'" +  data[1].strip() + "',")  # firstName
    fileOut.write("'" +  data[2].strip() + "',")  # lastName
    fileOut.write("'" +  data[3].strip() + "',")  # houseNo
    fileOut.write("'" +  data[4].strip() + "',")  # street
    fileOut.write("'" +  data[5].strip() + "',")  # town
    fileOut.write("'" +  data[6].strip() + "',")  # county
    fileOut.write("'" +  data[7].strip() + "',")  # postcode
    fileOut.write("'" +  data[8].strip() + "',")  # phone
    fileOut.write(       data[9].strip() + ");\n")  # daysPerWeek

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
