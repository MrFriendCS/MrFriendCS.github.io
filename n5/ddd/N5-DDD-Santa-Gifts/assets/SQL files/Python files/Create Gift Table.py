# Title: Create Gift Table
# Author: Mr Friend
# Date: 11 Dec 2024

# Files
fileIn = open("../CSV files/Gift.csv", "r")
fileOut = open("../Gift.sql", "w")


# Create Table

table = """CREATE TABLE Gift (
    giftID INT NOT NULL,
    childID INT,
    item VARCHAR(50),
    PRIMARY KEY (giftID),
    FOREIGN KEY (childID)
        REFERENCES child(childID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Gift VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # giftID
    fileOut.write(       data[1].strip() + ",")  # childID
    fileOut.write("\"" + data[2].strip() + "\")")  # item
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()

