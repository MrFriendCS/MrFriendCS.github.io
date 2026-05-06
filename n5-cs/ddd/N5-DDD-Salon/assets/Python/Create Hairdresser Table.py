# Title: Create Hairdresser Table
# Author: Mr Friend
# Date: 6 Oct 2024


"""Create Hairdresser table, with definition and data."""

fileIn = open("../CSV/hairdresser.csv", "r")
fileOut = open("../SQL/Hairdresser.sql", "w")

#line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()


tableProduct = """CREATE TABLE Hairdresser (
    hairdresserID INT NOT NULL,
    firstName VARCHAR(20),
    lastName VARCHAR(30),
    phone VARCHAR(13) NOT NULL
        CHECK(LENGTH(phone >= 11)),
    salon VARCHAR(30),
    PRIMARY KEY (hairdresserID)
);"""
              
fileOut.write(tableProduct + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Hairdresser VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # hairdresserID
    fileOut.write( "\"" + data[1].strip() + "\",")  # firstName
    fileOut.write( "\"" + data[2].strip() + "\",")  # lastName
    fileOut.write( "\"" + data[3].strip() + "\",")  # phone
    fileOut.write( "\"" + data[4].strip() + "\");\n")  # salon
 
    line = fileIn.readline()
    
fileIn.close()
fileOut.close()

