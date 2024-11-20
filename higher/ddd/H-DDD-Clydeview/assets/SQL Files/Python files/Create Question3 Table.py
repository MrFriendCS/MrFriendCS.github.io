# Title: Question3 Table
# Author: Mr Friend
# Date: 14 Nov 2024

# Create table

fileIn = open("../CSV Files/Question3.csv", "r")
fileOut = open("../Question3.sql", "w")

table = """CREATE TABLE Question3 (
    StudentID INT NOT NULL,
    Forename VARCHAR(50) NOT NULL,
    Surname VARCHAR(50) NOT NULL,
    test1 INT NOT NULL
        CHECK(test1 >= 0 AND test1 <= 20),
    test2 INT NOT NULL
        CHECK(test2 >= 0 AND test2 <= 20),
    test3 INT NOT NULL
        CHECK(test3 >= 0 AND test3 <= 20),
    test4 INT NOT NULL
        CHECK(test4 >= 0 AND test4 <= 20),
    test5 INT NOT NULL
        CHECK(test5 >= 0 AND test5 <= 20),
    PRIMARY KEY (StudentID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Question3 VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # StudentID
    fileOut.write( "\"" + data[1].strip() + "\",")  # Forename
    fileOut.write( "\"" + data[2].strip() + "\",")  # Surname
    fileOut.write(        data[3].strip() + ",")  # test1
    fileOut.write(        data[4].strip() + ",")  # test2
    fileOut.write(        data[5].strip() + ",")  # test3
    fileOut.write(        data[6].strip() + ",")  # test4
    fileOut.write(        data[7].strip() + ");\n")  # test5

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
