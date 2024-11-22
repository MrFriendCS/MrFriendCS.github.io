# Title: City Table
# Author: Mr Friend
# Date: 20 Nov 2024

# Files
fileIn = open("../CSV files/Country-City/City.csv", "r")
fileOut = open("../City.sql", "w")


# Table
table = """CREATE TABLE City (
    cityID INT NOT NULL,
    cityName VARCHAR(20) NOT NULL,
    countryCode VARCHAR(4) NOT NULL,
    population INT 
        CHECK(population >= 0),
    longitude FLOAT,
    latitude FLOAT,
    FOREIGN KEY (countryCode)
        REFERENCES Country(countryCode),
    PRIMARY KEY (cityID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO City VALUES ")
    
    fileOut.write("(" +  data[0].strip() + ",")  # cityID
    fileOut.write("\"" + data[1].strip() + "\",")  # cityName
    fileOut.write("\"" + data[2].strip() + "\",")  # countryCode
    
    if data[3].strip() == "":
        fileOut.write("NULL,")
    else:
        fileOut.write(   data[3].strip() + ",")  # population
        
    if data[4].strip() == "":
        fileOut.write("NULL,")
    else:
        fileOut.write(   data[4].strip() + ",")  # longitude
        
    if data[5].strip() == "":
        fileOut.write("NULL);\n")
    else:
        fileOut.write(   data[5].strip() + ");\n")  # latitude

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
