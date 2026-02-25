# Title: Create Subject Table
# Author: Mr Friend
# Date: 22 Dec 2024

"""
Produce SQL to create Subject table.
"""

# Create Class Table

# Files
fileIn = open("../CSV files/Subject.csv", "r")
fileOut = open("../Subject.sql", "w")

# Create table
table = """CREATE TABLE Subject (
    id VARCHAR(5) NOT NULL,
    name VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);"""
              
fileOut.write(table + "\n\n")


# Write data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Subject VALUES (")
    
    fileOut.write("\"" + data[0].strip() + "\",")  # id
    fileOut.write("\"" + data[1].strip() + "\"")  # class
    fileOut.write(");\n")
 
    line = fileIn.readline()


fileIn.close()
fileOut.close()
