# Title: Create House Table
# Author: Mr Friend
# Date: 19 Dec 2024

"""
Produce SQL to create House table.
"""

# Create House Table

# Files
fileIn = open("../CSV files/House.csv", "r")
fileOut = open("../House.sql", "w")

# Create table
table = """CREATE TABLE House (
    id INT NOT NULL,
    name VARCHAR(20) NOT NULL,
    guidanceTeacher VARCHAR(30),
    emblem VARCHAR(10) NOT NULL,
    colour VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);"""
              
fileOut.write(table + "\n\n")


# Write data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO House VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # id
    fileOut.write("\"" + data[1].strip() + "\",")  # name
    fileOut.write("\"" + data[2].strip() + "\",")  # guidanceTeacher
    fileOut.write("\"" + data[3].strip() + "\",")  # emblem
    fileOut.write("\"" + data[4].strip() + "\"")  # colour
    fileOut.write(");\n")
 
    line = fileIn.readline()


fileIn.close()
fileOut.close()
