# Title: Create Marathon Table
# Author: Mr Friend
# Date: 10 Dec 2024

# Files
fileIn = open("../CSV files/Marathon.csv", "r")
fileOut = open("../Marathon.sql", "w")


# Create Table

table = """CREATE TABLE Marathon (
    surname VARCHAR(30),
    forename VARCHAR(20),
    country VARCHAR(3)
        CHECK (LENGTH("country") = 3),
    number INT
        CHECK ("number" > 0),
    category VARCHAR(10),
    gender VARCHAR(1),
    half TIME,
    finish TIME
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Marathon VALUES ")
    
    fileOut.write(       data[0].strip() + ",")  # surname
    fileOut.write("\"" + data[1].strip() + "\",")  # forename
    fileOut.write("\"" + data[2].strip() + "\",")  # country
    fileOut.write("\"" + data[3].strip() + "\",")  # number
    fileOut.write("\"" + data[4].strip() + "\",")  # category
    fileOut.write("\"" + data[5].strip() + "\",")  # gender
    fileOut.write("\"" + data[6].strip() + "\",")  # half
    fileOut.write("\"" + data[7].strip() + "\")")  # finish
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
