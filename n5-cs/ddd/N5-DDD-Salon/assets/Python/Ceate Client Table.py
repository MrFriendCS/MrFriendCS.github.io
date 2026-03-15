# Title: Create Client Table
# Author: Mr Friend
# Date: 2 Mar 2026


"""Create Client table, with definition and data."""

fileIn = open("../CSV/client.csv", "r")
fileOut = open("../SQL/Client.sql", "w")

#line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()


tableProduct = """CREATE TABLE Client (
    clientid INT NOT NULL,
    hairdresserID INT NOT NULL,
    firstname VARCHAR(20),
    lastname VARCHAR(30),
    contactnumber VARCHAR(13) NOT NULL
        CHECK(LENGTH(contactnumber >= 11)),
    FOREIGN KEY (hairdresserID)
        REFERENCES Hairdresser (hairdresserID),
    PRIMARY KEY (clientID)
);"""
              
fileOut.write(tableProduct + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Client VALUES ")
    
    fileOut.write("("   + data[1].strip() + ",")  # clientID
    fileOut.write(        data[0].strip() + ",")  # hairdresserID
    fileOut.write( "\"" + data[2].strip() + "\",")  # firstname
    fileOut.write( "\"" + data[3].strip() + "\",")  # lastname
    fileOut.write( "\"" + data[4].strip() + "\");\n")  # contactnumber
 
    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
