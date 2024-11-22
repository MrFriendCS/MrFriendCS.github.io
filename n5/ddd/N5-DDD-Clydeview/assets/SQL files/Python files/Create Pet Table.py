# Title: Pet Table
# Author: Mr Friend
# Date: 22 Nov 2024

# Files
fileIn = open("../CSV files/Owner-Pet/Pet.csv", "r")
fileOut = open("../Pet.sql", "w")


# Create table

table = """CREATE TABLE Pet (
    petCode VARCHAR(5) NOT NULL 
        CHECK(LENGTH(petCode) = 5),
    petName VARCHAR(20),
    petType VARCHAR(8),
    dateOfBirth DATE,
    vaccination BOOL,
    ownerID INT NOT NULL,
    FOREIGN KEY (ownerID)
        REFERENCES Owner (ownerID),
    PRIMARY KEY (petCode)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Pet VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # petCode
    fileOut.write( "\"" + data[1].strip() + "\",")  # petName
    fileOut.write( "\"" + data[2].strip() + "\",")  # petType
    fileOut.write( "\"" + data[3].strip() + "\",")  # dateOfBirth
    if bool(int(data[4].strip())):  # vaccination
        fileOut.write( "TRUE,")
    else:
        fileOut.write( "FALSE,")
    fileOut.write(        data[5].strip() + ");\n")  # ownerID

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
