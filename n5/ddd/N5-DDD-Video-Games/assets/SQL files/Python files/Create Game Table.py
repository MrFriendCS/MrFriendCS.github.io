# Title: Game Table
# Author: Mr Friend
# Date: 9 Dec 2024

# Files
fileIn = open("../CSV files/Game.csv", "r")
fileOut = open("../Game.sql", "w")


# Create table

table = """CREATE TABLE Game ( 
    title VARCHAR(30) NOT NULL,
    company VARCHAR(20) NOT NULL,
    genre VARCHAR(15) NOT NULL,
    age INT NOT NULL 
        CHECK (age IN (3, 7, 12, 16, 18)),
    price FLOAT NOT NULL 
        CHECK (price >= 0 AND price <= 100),
    released DATE NOT NULL 
        CHECK (released >= \"1970-01-01\"),
    copiesSold INT NOT NULL 
        CHECK (copiesSold >= 0),
    PRIMARY KEY (title),
    FOREIGN KEY (company)
        REFERENCES company(name)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Game VALUES (")
    
    fileOut.write("\"" + data[0].strip() + "\",")  # title
    fileOut.write("\"" + data[1].strip() + "\",")  # company
    fileOut.write("\"" + data[2].strip() + "\",")  # genre
    fileOut.write(   str(data[3].strip()) + ",")  # age
    fileOut.write(   str(data[4].strip()) + ",")  # price
    fileOut.write("\"" + data[5].strip() + "\",")  # released
    fileOut.write(   str(data[6].strip()) + ");")  # copiesSold
    fileOut.write("\n")
    
    line = fileIn.readline()


fileIn.close()
fileOut.close()
