# Title: Create Pet Table
# Author: Mr Friend
# Date: 5 Dec 2024

# Files
fileIn = open("../CSV files/Insurer/Pet.csv", "r")
fileOut = open("../Pet.sql", "w")


# Create Table

table = """CREATE TABLE Pet (
    name VARCHAR(20) NOT NULL,
    type VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    insurer INT NOT NULL,
    PRIMARY KEY (name),
    FOREIGN KEY (insurer)
        REFERENCES Insurer (id)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Pet VALUES ")
    
    fileOut.write( "(\"" + data[0].strip() + "\",")  # name
    fileOut.write( "\"" +  data[1].strip() + "\",")  # type
    fileOut.write(         data[2].strip() + ",")  # age
    fileOut.write(         data[3].strip() + ");\n")  # insurer

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
