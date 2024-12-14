# Title: Holiday Table
# Author: Mr Friend
# Date: 13 Dec 2024

# Files
fileIn = open("../CSV files/Hotel-Holiday/Holiday.csv", "r")
fileOut = open("../Holiday.sql", "w")


# Create table

table = """CREATE TABLE Holiday (
    name VARCHAR(30) NOT NULL,
    destination VARCHAR(30) NOT NULL,
    country VARCHAR(20),
    dateOfDeparture DATE NOT NULL,
    nights INT,
    hotelRef VARCHAR(4),
    FOREIGN KEY (hotelRef)
        REFERENCES Hotel(hotelRef),
    PRIMARY KEY (title)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Holiday VALUES (")
    
    fileOut.write("\"" + data[0].strip() + "\",")  # title
    fileOut.write("\"" + data[1].strip() + "\",")  # destination
    fileOut.write("\"" + data[2].strip() + "\",")  # country
    fileOut.write("\"" + data[3].strip() + "\",")  # dateOfDeparture
    fileOut.write("\"" + data[4].strip() + "\",")  # nights
    fileOut.write("\"" + data[5].strip() + "\");")  # hotelRef
    fileOut.write("\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
