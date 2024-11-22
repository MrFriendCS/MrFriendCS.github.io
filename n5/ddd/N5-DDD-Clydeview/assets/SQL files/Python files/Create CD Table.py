# Title: CD Table
# Author: Mr Friend
# Date: 22 Nov 2024

# Files
fileIn = open("../CSV Files/Label-CD/CD.csv", "r")
fileOut = open("../CD.sql", "w")


# Create table

table = """CREATE TABLE CD (
    code VARCHAR(4) NOT NULL 
        CHECK(LENGTH(code) = 4),
    title VARCHAR(40) NOT NULL,
    artist VARCHAR(40) NOT NULL,
    label VARCHAR(20) NOT NULL,
    tracks INT 
        CHECK (tracks >= 10 
           AND tracks <= 60),
    cost REAL NOT NULL 
        CHECK(cost >= 6.99 
          AND cost <= 15.00),
    genre VARCHAR(20) NOT NULL
        CHECK (genre IN ("Choral", "Country", "Garage", "Indie", 
                         "Opera", "Pop", "R&B", "R&R", "Soul")),
    FOREIGN KEY (label)
        REFERENCES Label(label),
    PRIMARY KEY (code)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()


while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO CD VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # code
    fileOut.write( "\"" + data[1].strip() + "\",")  # title
    fileOut.write( "\"" + data[2].strip() + "\",")  # artist
    fileOut.write( "\"" + data[3].strip() + "\",")  # label
    fileOut.write(        data[4].strip() + ",")  # tracks
    fileOut.write(        data[5].strip() + ",")  # cost
    fileOut.write( "\"" + data[6].strip() + "\");\n")  # genre

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
