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
    name VARCHAR(15) NOT NULL,
    guidanceTeacher VARCHAR(30),
    colour VARCHAR(15) NOT NULL,
    PRIMARY KEY (name)
);"""
              
fileOut.write(table + "\n\n")


# Write data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO House VALUES (")
    
    fileOut.write("\"" + data[0].strip() + "\",")  # hairdresserid
    fileOut.write("\"" + data[1].strip() + "\",")  # guidance_teacher
    fileOut.write("\"" + data[2].strip() + "\"")  # colour
    fileOut.write(");\n")
 
    line = fileIn.readline()


fileIn.close()
fileOut.close()
