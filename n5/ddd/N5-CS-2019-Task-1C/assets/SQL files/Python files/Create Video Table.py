# Title: Video Table
# Author: Mr Friend
# Date: 19 Jan 2025

# Files
fileIn = open("../CSV files/Video.csv", "r")
fileOut = open("../Video.sql", "w")


# Create table

table = """CREATE TABLE Video (
    videoID INT NOT NULL,
    vloggerID INT NOT NULL,
    videoName VARCHAR(30) NOT NULL,
    duration INT NOT NULL,
    dateCreated DATE NOT NULL,
    content VARCHAR(40) NOT NULL,
    rating INT NOT NULL
        CHECK (rating >= 1
          AND  rating <= 5),
    PRIMARY KEY (videoID),
    FOREIGN KEY (vloggerID)
        REFERENCES Vlogger (vloggerID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Video VALUES (")
    
    fileOut.write(       data[0].strip() + ",")  # videoID
    fileOut.write(       data[1].strip() + ",")  # vloggerID
    fileOut.write("\"" + data[2].strip() + "\",")  # videoName
    fileOut.write(       data[3].strip() + ",")  # duration
    fileOut.write("\"" + data[4].strip() + "\",")  # dateCreated
    fileOut.write("\"" + data[5].strip() + "\",")  # content
    fileOut.write(       data[6].strip() + ");")  # rating
    fileOut.write("\n")

    line = fileIn.readline()


fileIn.close()
fileOut.close()
