# Title: Create Result Table
# Author: Mr Friend
# Date: 22 Dec 2024

"""
Produce SQL to create Result table.
"""

# Create Class Table

# Files
fileIn = open("../CSV files/Result.csv", "r")
fileOut = open("../Result.sql", "w")

# Create table
table = """CREATE TABLE Result (
    pupilID INT NOT NULL,
    subjectID VARCHAR(5) NOT NULL,
    grade VARCHAR(10),
    PRIMARY KEY (pupilID, subjectID),
    FOREIGN KEY (pupilID)
        REFERENCES Pupil (id),
    FOREIGN KEY (subjectID)
        REFERENCES Subject (id)
);"""
              
fileOut.write(table + "\n\n")


# Write data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Result VALUES (")
    
    fileOut.write(   str(data[0].strip()) + ",")  # pupilID
    fileOut.write("\"" + data[1].strip() + "\",")  # subjectID
    fileOut.write("\"" + data[2].strip() + "\"")  # grade
    fileOut.write(");\n")
 
    line = fileIn.readline()


fileIn.close()
fileOut.close()
