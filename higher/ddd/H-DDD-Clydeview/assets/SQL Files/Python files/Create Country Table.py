# Title: Country Table
# Author: Mr Friend
# Date: 20 Nov 2024

# Files
fileIn = open("../CSV files/Country-City/Country.csv", "r")
fileOut = open("../Country.sql", "w")


# Table
table = """CREATE TABLE Country (
    name VARCHAR(35) NOT NULL,
    code VARCHAR(4) NOT NULL,
    capital VARCHAR(20) NOT NULL,
    area INT 
        CHECK(area >= 0),
    population INT
        CHECK(population >= 0),
    PRIMARY KEY (code)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Country VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # name
    fileOut.write("\"" +  data[1].strip() + "\",")  # code
    fileOut.write("\"" +  data[2].strip() + "\",")  # capital
    fileOut.write(        data[3].strip() + ",")  # area
    fileOut.write(        data[4].strip() + ");\n")  # population

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
