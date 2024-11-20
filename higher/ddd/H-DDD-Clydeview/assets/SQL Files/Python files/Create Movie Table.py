# Title: Movie Table
# Author: Mr Friend
# Date: 19 Nov 2024

# Create table

fileIn = open("../CSV Files/Movie.csv", "r")
fileOut = open("../Movie.sql", "w")

table = """CREATE TABLE Movie (
    movieID INT NOT NULL,
    title VARCHAR(30) NOT NULL,
    director VARCHAR(30),
    yearReleased INT NOT NULL
        CHECK(yearReleased >= 1900
          AND yearReleased <= 2030),
    durationsMins INT NOT NULL
        CHECK(durationsMins >= 0),
    PRIMARY KEY (movieID)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Movie VALUES ")
    
    fileOut.write("(" +  data[0].strip() + ",")  # movieID
    fileOut.write("\"" + data[1].strip() + "\",")  # title
    fileOut.write("\"" + data[2].strip() + "\",")  # director
    fileOut.write(       data[3].strip() + ",")  # yearReleased
    fileOut.write(       data[4].strip() + ");\n")  # durationsMins

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
