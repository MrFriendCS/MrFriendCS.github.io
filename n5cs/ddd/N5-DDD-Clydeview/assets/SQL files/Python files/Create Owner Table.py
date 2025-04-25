# Title: Owner Table
# Author: Mr Friend
# Date: 22 Nov 2024

# Files
fileIn = open("../CSV files/Owner-Pet/Owner.csv", "r")
fileOut = open("../Owner.sql", "w")


# Create table

table = """CREATE TABLE Owner (
    ownerID INTEGER NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    address VARCHAR(40) NOT NULL,
    town VARCHAR(20) NOT NULL,
    contactTele VARCHAR(11) NOT NULL 
        CHECK (LENGTH(contactTele) = 11),
    PRIMARY KEY (ownerID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Owner VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # ownerID
    fileOut.write( "\"" + data[1].strip() + "\",")  # firstName
    fileOut.write( "\"" + data[2].strip() + "\",")  # surname
    fileOut.write( "\"" + data[3].strip() + "\",")  # address
    fileOut.write( "\"" + data[4].strip() + "\",")  # town
    fileOut.write( "\"" + data[5].strip() + "\");\n")  # contactTele

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
