# Title: Table1 Table
# Author: Mr Friend
# Date: 14 Nov 2024

# Files
fileIn = open("../CSV Files/Table1.csv", "r")
fileOut = open("../Table1.sql", "w")


# Create table

table = """CREATE TABLE Table1 (
    pupilID INT NOT NULL,
    forename VARCHAR(12) NOT NULL,
    surname VARCHAR(12) NOT NULL,
    test1 INT NOT NULL
        CHECK(test1 >= 0 AND test1 <= 10),
    test2 INT NOT NULL
        CHECK(test2 >= 0 AND test2 <= 10),
    test3 INT NOT NULL
        CHECK(test3 >= 0 AND test3 <= 10),
    test4 INT NOT NULL
        CHECK(test4 >= 0 AND test4 <= 10),
    PRIMARY KEY (pupilID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Table1 VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # pupilID
    fileOut.write( "\"" + data[1].strip() + "\",")  # forename
    fileOut.write( "\"" + data[2].strip() + "\",")  # surname
    fileOut.write(        data[3].strip() + ",")  # test1
    fileOut.write(        data[4].strip() + ",")  # test2
    fileOut.write(        data[5].strip() + ",")  # test3
    fileOut.write(        data[6].strip() + ");\n")  # test4

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
