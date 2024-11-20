# Create Manufacturer Table

fileIn = open("Manufacturer.csv", "r")
fileOut = open("Manufacturer.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()


tableManufacturer = """CREATE TABLE Manufacturer (
    manufacturerID INT NOT NULL,
    name VARCHAR(40),
    address VARCHAR(40),
    telephoneNumber VARCHAR(11) 
        CHECK (LENGTH(telephoneNumber) = 11),
    PRIMARY KEY (manufacturerID)
);"""

fileOut.write(tableManufacturer + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Manufacturer VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # manufacturerID
    fileOut.write( "\"" + data[1].strip() + "\",")  # name
    fileOut.write( "\"" + data[2].strip() + "\",")  # address
    fileOut.write( "\"" + data[3].strip() + "\");\n")  # telephoneNumber

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
