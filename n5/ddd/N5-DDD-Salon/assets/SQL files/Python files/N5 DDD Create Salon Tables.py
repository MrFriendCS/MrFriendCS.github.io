# Title: Salon System Database
# Author: Mr Friend
# Date: 6 Oct 2024

"""
Produce SQL to create two tables and populate with data.
"""


def hairdresser():
    """Create Hairdresser table, with definition and data."""

    fileIn = open("hairdresser.csv", "r")
    fileOut = open("hairdresser.sql", "w")

    #line = fileIn.readline()  # Ignore heading row
    line = fileIn.readline()


    tableProduct = """CREATE TABLE Hairdresser (
    hairdresserid INT NOT NULL,
    firstname VARCHAR(20),
    lastname VARCHAR(30),
    contactnumber VARCHAR(13) NOT NULL
        CHECK(LENGTH(contactnumber >= 11)),
    salon VARCHAR(30),
    PRIMARY KEY (hairdresserid)
);"""
                  
    fileOut.write(tableProduct + "\n\n")

    while line != "":
        
        data = line.split(",")
        
        fileOut.write("INSERT INTO Hairdresser VALUES ")
        
        fileOut.write("("   + data[0].strip() + ",")  # hairdresserid
        fileOut.write( "\"" + data[1].strip() + "\",")  # firstname
        fileOut.write( "\"" + data[2].strip() + "\",")  # lastname
        fileOut.write( "\"" + data[3].strip() + "\",")  # contactnumber
        fileOut.write( "\"" + data[4].strip() + "\");\n")  # salon
     
        line = fileIn.readline()
        
    fileIn.close()
    fileOut.close()


def client():
    """Create Client table, with definition and data."""

    fileIn = open("client.csv", "r")
    fileOut = open("client.sql", "w")

    #line = fileIn.readline()  # Ignore heading row
    line = fileIn.readline()


    tableProduct = """CREATE TABLE Client (
    clientid INT NOT NULL,
    hairdresserid INT NOT NULL,
    firstname VARCHAR(20),
    lastname VARCHAR(30),
    contactnumber VARCHAR(13) NOT NULL
        CHECK(LENGTH(contactnumber >= 11)),
    FOREIGN KEY (hairdresserid)
        REFERENCES Hairdresser (hairdresserid),
    PRIMARY KEY (clientid)
);"""
                  
    fileOut.write(tableProduct + "\n\n")

    while line != "":
        
        data = line.split(",")
        
        fileOut.write("INSERT INTO Client VALUES ")
        
        fileOut.write("("   + data[1].strip() + ",")  # clientid
        fileOut.write(        data[0].strip() + ",")  # hairdresserid
        fileOut.write( "\"" + data[2].strip() + "\",")  # firstname
        fileOut.write( "\"" + data[3].strip() + "\",")  # lastname
        fileOut.write( "\"" + data[4].strip() + "\");\n")  # contactnumber
     
        line = fileIn.readline()
        
    fileIn.close()
    fileOut.close()
    

def main():
    """Main program."""
    hairdresser()
    client()


# Call main()
main()
