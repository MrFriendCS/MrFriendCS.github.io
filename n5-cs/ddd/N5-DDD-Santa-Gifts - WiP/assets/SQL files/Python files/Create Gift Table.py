# Title: Create Gift Table
# Author: Mr Friend
# Date: 15 Dec 2025

# Files
fileIn = open("../CSV files/Gift.csv", "r")
fileOut = open("../Gift.sql", "w")


# Create Table

table = """CREATE TABLE Gift (
    giftID INT NOT NULL,
    childID INT NOT NULL,
    toyID INT NOT NULL,
    PRIMARY KEY (giftID),
    FOREIGN KEY (childID)
        REFERENCES Child(childID),
    FOREIGN KEY (toyID)
        REFERENCES Toy(toyID)
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
    fileOut.write(       data[2].strip() + ")")  # toyID
    fileOut.write(";\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
