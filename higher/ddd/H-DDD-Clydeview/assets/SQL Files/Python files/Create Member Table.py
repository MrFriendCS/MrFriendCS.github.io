# Title: Member Table
# Author: Mr Friend
# Date: 20 Nov 2024

# Create table

fileIn = open("../CSV Files/Member.csv", "r")
fileOut = open("../Member.sql", "w")

table = """CREATE TABLE Member (
    membershipNumber VARCHAR(6) NOT NULL,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    address VARCHAR(30),
    town VARCHAR(40),
    postcode VARCHAR(8),
    dateOfBirth DATE NOT NULL,
    monthOfRenewal VARCHAR(9),
    typeOfMembership VARCHAR(7) NOT NULL
        CHECK(typeOfMembership IN("Adult","Child","Senior","Student")),
    PRIMARY KEY (membershipNumber)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Member VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # membershipNumber
    fileOut.write( "\"" + data[1].strip() + "\",")  # Firstname
    fileOut.write( "\"" + data[2].strip() + "\",")  # Surname
    fileOut.write( "\"" + data[3].strip() + "\",")  # Address
    fileOut.write( "\"" + data[4].strip() + "\",")  # Town
    fileOut.write( "\"" + data[5].strip() + "\",")  # Postcode
    fileOut.write( "\"" + data[6].strip() + "\",")  # dateOfBirth
    fileOut.write( "\"" + data[7].strip() + "\",")  # monthOfRenewal
    fileOut.write( "\"" + data[8].strip() + "\");\n")  # typeOfMembership

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
