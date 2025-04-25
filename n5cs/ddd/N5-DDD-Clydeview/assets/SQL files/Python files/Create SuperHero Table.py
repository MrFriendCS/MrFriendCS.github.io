# Title: SuperHero Table
# Author: Mr Friend
# Date: 20 Nov 2024

# Files
fileIn = open("../CSV files/SuperHero.csv", "r")
fileOut = open("../SuperHero.sql", "w")

# Table
table = """CREATE TABLE SuperHero (
    characterID INT NOT NULL,
    name VARCHAR(40),
    role VARCHAR(30),
    mainAbility VARCHAR(30),
    ability2 VARCHAR(30),
    ability3 VARCHAR(30),
    originOfPower VARCHAR(30),
    alterEgo VARCHAR(40),
    PRIMARY KEY (characterID)
);"""

fileOut.write(table + "\n\n")


# Data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO SuperHero VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # characterID
    fileOut.write( "\"" + data[1].strip() + "\",")  # name
    fileOut.write( "\"" + data[2].strip() + "\",")  # role
    fileOut.write( "\"" + data[3].strip() + "\",")  # mainAbility
    
    if data[4].strip() != "":  # ability2
        fileOut.write( "\"" + data[4].strip() + "\",")
    else:
        fileOut.write("NULL,")
        
    if data[5].strip() != "":  # ability3
        fileOut.write( "\"" + data[5].strip() + "\",")
    else:
        fileOut.write("NULL,")
    fileOut.write( "\"" + data[6].strip() + "\",")  # originOfPower
    
    if data[7].strip() != "":  # alterEgo
        fileOut.write( "\"" + data[7].strip() + "\");\n") 
    else:
        fileOut.write("NULL);\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
