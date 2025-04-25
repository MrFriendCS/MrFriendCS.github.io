# Title: Create Insurer Table
# Author: Mr Friend
# Date: 5 Dec 2024

# Files
fileIn = open("../CSV files/Insurer/Insurer.csv", "r")
fileOut = open("../Insurer.sql", "w")


# Create Table

table = """CREATE TABLE Insurer (
    id INT NOT NULL,
    company VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Insurer VALUES ")
    
    fileOut.write( "("  + data[0].strip() + ",")  # id
    fileOut.write( "\"" + data[1].strip() + "\");\n")  # company


    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
