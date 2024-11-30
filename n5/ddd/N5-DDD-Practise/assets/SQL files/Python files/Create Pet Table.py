# Title: Create Pet Table
# Author: Mr Friend
# Date: 15 Jan 2024

# Create Pet table

petTable = """CREATE TABLE Pet (
    name VARCHAR(20) NOT NULL,
    type VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    insured BOOL NOT NULL,
    lastVisit DATE NOT NULL,
    PRIMARY KEY (name)
);"""

fileIn = open("pet.csv", "r")
fileOut = open("pet.sql", "w")

fileOut.write(petTable + "\n\n")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Pet VALUES ")
    
    fileOut.write( "(\"" + data[0].strip() + "\",")  # name
    fileOut.write( "\"" +  data[1].strip() + "\",")  # type
    fileOut.write(         data[2].strip() + ",")  # age
    fileOut.write( "\"" +  data[3].strip() + "\",")  # insured
    fileOut.write( "\"" +  data[4].strip() + "\");\n")  # lastVisit

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
