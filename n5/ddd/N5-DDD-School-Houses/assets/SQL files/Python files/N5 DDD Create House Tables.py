# Title: SSchool Houses Database
# Author: Mr Friend
# Date: 17 Jan 2024

"""
Produce SQL to create two tables and populate with data.
"""

# Create House Table

fileIn = open("house.csv", "r")
fileOut = open("house.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()


houseTable = """CREATE TABLE House (
    house VARCHAR(15) NOT NULL,
    guidance_teacher VARCHAR(30),
    colour VARCHAR(15) NOT NULL,
    PRIMARY KEY (house)
);"""
              
fileOut.write(houseTable + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO House VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # hairdresserid
    fileOut.write( "\"" + data[1].strip() + "\",")  # guidance_teacher
    fileOut.write( "\"" + data[2].strip() + "\");\n")  # colour
 
    line = fileIn.readline()
    
fileIn.close()
fileOut.close()

# Create Pupil Table

fileIn = open("pupil.csv", "r")
fileOut = open("pupil.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()


pupilTable = """CREATE TABLE Pupil (
    id VARCHAR(10) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    gender VARCHAR(10),
    house VARCHAR(15) NOT NULL,
    year VARCHAR(5) NOT NULL,
    age INT NOT NULL,
    FOREIGN KEY (house)
        REFERENCES House (house),
    PRIMARY KEY (id)
);"""
              
fileOut.write(pupilTable + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Pupil VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # id
    fileOut.write( "\"" + data[1].strip() + "\",")  # last_name
    fileOut.write( "\"" + data[2].strip() + "\",")  # first_name
    fileOut.write( "\"" + data[3].strip() + "\",")  # gender
    fileOut.write( "\"" + data[4].strip() + "\",")  # house
    fileOut.write( "\"" + data[5].strip() + "\",")  # year
    fileOut.write(        data[6].strip() + ");\n")  # age
 
    line = fileIn.readline()
    
fileIn.close()
fileOut.close()