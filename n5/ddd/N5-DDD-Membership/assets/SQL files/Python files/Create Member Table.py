# Title: Create Member Table
# Author: Mr Friend
# Date: 4 Dec 2024


# Files
fileIn = open("../CSV files/Member.csv", "r")
fileOut = open("../Member.sql", "w")


# Create Table

table = """CREATE TABLE Member ( 
    memberNo VARCHAR(8) NOT NULL UNIQUE,
    clubID VARCHAR(6) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    address VARCHAR(30),
    town VARCHAR(20),
    postcode VARCHAR(8),
    dob DATE NOT NULL 
        CHECK(dob >= \"1925-01-01\"),
    renew INT NOT NULL 
        CHECK(renew >=1 AND renew <= 12),
    gender VARCHAR(15) 
        CHECK(gender IN (\"F\", \"M\", \"ND\")),
    type VARCHAR(15) NOT NULL 
        CHECK(type IN (\"Adult\", \"Child\", \"Guest\",
                       \"Senior\", \"Student\")),
    FOREIGN KEY (clubID) 
        REFERENCES club(clubID),
    PRIMARY KEY (memberNo)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Member VALUES ")

    fileOut.write("(\"" + data[0].strip() + "\",")  # memberNo
    fileOut.write("\""  + data[1].strip() + "\",")  # clubID
    fileOut.write("\""  + data[2].strip() + "\",")  # firstName
    fileOut.write("\""  + data[3].strip() + "\",")  # lastName
    fileOut.write("\""  + data[4].strip() + "\",")  # address
    fileOut.write("\""  + data[5].strip() + "\",")  # town
    fileOut.write("\""  + data[6].strip() + "\",")  # postcode
    fileOut.write("\""  + data[7].strip() + "\",")  # dob
    fileOut.write(        data[8].strip() + ",")  # renew
    fileOut.write("\""  + data[9].strip() + "\",")  # gender
    fileOut.write("\""  + data[10].strip() + "\");\n")  # type    
    
    line = fileIn.readline()


fileIn.close()
fileOut.close()
