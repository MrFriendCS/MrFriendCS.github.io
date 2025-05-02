# Title: BoxOffice Table
# Author: Mr Friend
# Date: 19 Nov 2024

# Files
fileIn = open("../CSV files/Movie-BoxOffice/BoxOffice.csv", "r")
fileOut = open("../BoxOffice.sql", "w")


# Table
table = """CREATE TABLE BoxOffice (
    movieID INT NOT NULL,
    rating FLOAT NOT NULL
        CHECK(rating >=0 AND
              rating <= 10),
    movieBudget INT NOT NULL
        CHECK(movieBudget >= 0),
    salesUS INT NOT NULL
        CHECK(salesUS >= 0),
    salesInternational INT NOT NULL
        CHECK(salesInternational >= 0),
    FOREIGN KEY (movieID)
        REFERENCES Movie(movieID),
    PRIMARY KEY (movieID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO BoxOffice VALUES ")
    
    fileOut.write("(" + data[0].strip() + ",")  # movieID
    fileOut.write(      data[1].strip() + ",")  # rating
    fileOut.write(      data[2].strip() + ",")  # moviebudget
    fileOut.write(      data[3].strip() + ",")  # USsales
    fileOut.write(      data[4].strip() + ");\n")  # internationalSales

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
