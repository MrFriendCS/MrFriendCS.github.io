# Title: Hotels and Holidays
# Author: Mr Friend
# Date: 18 Jan 2024

# Create Hotels Table

fileIn = open("Hotel.csv", "r")
fileOut = open("Hotel.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

table = """CREATE TABLE Hotel (
    hotelRef VARCHAR(4) NOT NULL,
    hotelName VARCHAR(30) NOT NULL,
    city VARCHAR(20),
    starRating INT NOT NULL
        CHECK (starRating >= 0 AND starRating <= 5),
    pricePerNight REAL,
    kmFromAirport REAL,
    PRIMARY KEY (hotelRef)
);"""

fileOut.write(table + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Hotel VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # hotelRef
    fileOut.write( "\"" + data[1].strip() + "\",")  # hotelName
    fileOut.write( "\"" + data[2].strip() + "\",")  # city
    fileOut.write(        data[3].strip() + ",")  # starRating
    fileOut.write(        data[4].strip() + ",")  # pricePerNight
    fileOut.write(        data[5].strip() + ");\n")  # kmFromAirport

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()


# Create Holiday Table

fileIn = open("Holiday.csv", "r")
fileOut = open("Holiday.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

table = """CREATE TABLE Holiday (
    title VARCHAR(30) NOT NULL,
    destination VARCHAR(30) NOT NULL,
    country VARCHAR(20),
    dateOfDeparture DATE NOT NULL,
    nights INT,
    hotelRef VARCHAR(4),
    PRIMARY KEY (title)
);"""

fileOut.write(table + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Holiday VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # title
    fileOut.write( "\"" + data[1].strip() + "\",")  # destination
    fileOut.write( "\"" + data[2].strip() + "\",")  # country
    fileOut.write( "\"" + data[3].strip() + "\",")  # dateOfDeparture
    fileOut.write( "\"" + data[4].strip() + "\",")  # nights
    fileOut.write( "\"" + data[5].strip() + "\");\n")  # hotelRef

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
