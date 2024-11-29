# Title: Create Hotel
# Author: Mr Friend
# Date: 22 Nov 2024

# Files
fileIn = open("../CSV files/Hotel-Holiday/Hotel.csv", "r")
fileOut = open("../Hotel.sql", "w")


# Create Table

table = """CREATE TABLE Hotel (
    hotelRef VARCHAR(4) NOT NULL,
    name VARCHAR(30) NOT NULL,
    city VARCHAR(20),
    starRating INT NOT NULL
        CHECK (starRating >= 0 AND starRating <= 5),
    pricePerNight REAL,
    kmFromAirport REAL,
    PRIMARY KEY (hotelRef)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Hotel VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # hotelRef
    fileOut.write( "\"" + data[1].strip() + "\",")  # name
    fileOut.write( "\"" + data[2].strip() + "\",")  # city
    fileOut.write(        data[3].strip() + ",")  # starRating
    fileOut.write(        data[4].strip() + ",")  # pricePerNight
    fileOut.write(        data[5].strip() + ");\n")  # kmFromAirport

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
