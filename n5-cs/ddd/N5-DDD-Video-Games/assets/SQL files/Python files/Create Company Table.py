# Title: Company Table
# Author: Mr Friend
# Date: 9 Dec 2024

# Files
fileIn = open("../CSV files/Company.csv", "r")
fileOut = open("../Company.sql", "w")


# Create table

table = """CREATE TABLE Company ( 
    name VARCHAR(20) NOT NULL,
    country VARCHAR(20) NOT NULL,
    founded DATE NOT NULL 
        CHECK (founded >= \"1970-01-01\"),
    website VARCHAR(30),
    profit INT NOT NULL,
    PRIMARY KEY (name)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")

    fileOut.write("INSERT INTO Company VALUES (")
    
    fileOut.write("\"" + data[0].strip() + "\",")  # name
    fileOut.write("\"" + data[1].strip() + "\",")  # country
    fileOut.write("\"" + data[2].strip() + "\",")  # founded
    fileOut.write("\"" + data[3].strip() + "\",")  # website
    fileOut.write(   str(data[4].strip()) + ");")  # profit
    fileOut.write("\n")
    
    line = fileIn.readline()


fileIn.close()
fileOut.close()
