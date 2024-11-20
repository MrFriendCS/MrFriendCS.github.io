# Create Label Table

fileIn = open("Label.csv", "r")
fileOut = open("Label.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

tableLabel = """CREATE TABLE Label (
    label VARCHAR(20) NOT NULL,
    founded INT NOT NULL,
    parentCompany VARCHAR(30),
    countryOfOrigin VARCHAR(7) NOT NULL 
        CHECK (countryOfOrigin IN ("Germany", "Japan", "UK", "USA")),
    website VARCHAR(50),
    PRIMARY KEY (label)
);"""

fileOut.write(tableLabel + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Label VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # label
    fileOut.write( "\"" + data[1].strip() + "\",")  # founded
    fileOut.write( "\"" + data[2].strip() + "\",")  # parentCompany
    fileOut.write( "\"" + data[3].strip() + "\",")  # countryOfOrigin
    fileOut.write( "\"" + data[4].strip() + "\");\n")  # website

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
