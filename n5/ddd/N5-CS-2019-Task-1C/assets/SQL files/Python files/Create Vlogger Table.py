# Title: Vlogger Table
# Author: Mr Friend
# Date: 19 Jan 2025

# Files
fileIn = open("../CSV files/Vlogger.csv", "r")
fileOut = open("../Vlogger.sql", "w")


# Create table

table = """CREATE TABLE Vlogger (
    vloggerID INT NOT NULL,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    username VARCHAR(6) NOT NULL,
    expertise VARCHAR(15) NOT NULL,
    PRIMARY KEY (vloggerID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Vlogger VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # vloggerID
    fileOut.write("\"" + data[1].strip() + "\",")  # forename
    fileOut.write("\"" + data[2].strip() + "\",")  # surname
    fileOut.write("\"" + data[3].strip() + "\",")  # username
    fileOut.write("\"" + data[4].strip() + "\");")  # expertise
    fileOut.write("\n")

    line = fileIn.readline()


fileIn.close()
fileOut.close()
