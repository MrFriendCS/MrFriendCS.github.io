# Title: Plant Table
# Author: Mr Friend
# Date: 13 Nov 2024

# Create table

table = """CREATE TABLE Plant (
    category VARCHAR(10),
    plantName VARCHAR(20) NOT NULL,
    variety VARCHAR(20) NOT NULL,
    code VARCHAR(3) NOT NULL,
    referenceID VARCHAR(3) NOT NULL,
    unit INT 
        CHECK(unit >= 0),
    price FLOAT 
        CHECK(price >= 0),
    height VARCHAR(1) 
        CHECK(height IN("S","M","T")),
    PRIMARY KEY (referenceID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Plant VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # Category
    fileOut.write( "\"" + data[1].strip() + "\",")  # plantName
    fileOut.write( "\"" + data[2].strip() + "\",")  # Variety
    fileOut.write( "\"" + data[3].strip() + "\",")  # code
    fileOut.write( "\"" + data[4].strip() + "\",")  # referenceID
    fileOut.write(        data[5].strip() + ",")  # Unit
    fileOut.write(        data[6].strip() + ",")  # Price
    fileOut.write( "\"" + data[7].strip() + "\");\n")  # Height

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
