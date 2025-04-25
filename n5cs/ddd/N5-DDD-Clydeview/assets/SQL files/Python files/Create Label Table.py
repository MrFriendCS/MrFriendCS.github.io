# Title: CD Table
# Author: Mr Friend
# Date: 22 Nov 2024

# Files
fileIn = open("../CSV Files/Label-CD/Label.csv", "r")
fileOut = open("../Label.sql", "w")


# Create table

table = """CREATE TABLE Label (
    label VARCHAR(20) NOT NULL,
    founded INT NOT NULL,
    parentCompany VARCHAR(30),
    country VARCHAR(7) NOT NULL 
        CHECK (country IN ("Germany", "Japan", "UK", "USA")),
    website VARCHAR(50),
    PRIMARY KEY (label)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Label VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # label
    fileOut.write( "\"" + data[1].strip() + "\",")  # founded
    fileOut.write( "\"" + data[2].strip() + "\",")  # parentCompany
    fileOut.write( "\"" + data[3].strip() + "\",")  # country
    fileOut.write( "\"" + data[4].strip() + "\");\n")  # website

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
