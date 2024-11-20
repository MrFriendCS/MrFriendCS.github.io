# Create CD Table

fileIn = open("CD.csv", "r")
fileOut = open("CD.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

tableCD = """CREATE TABLE CD (
    CDCode VARCHAR(4) NOT NULL 
        CHECK(LENGTH(CDCode) = 4),
    title VARCHAR(40) NOT NULL,
    artist VARCHAR(40) NOT NULL,
    label VARCHAR(20) NOT NULL,
    numberOfTracks INT 
        CHECK (numberOfTracks >= 10 
           AND numberOfTracks <= 60),
    cost REAL NOT NULL 
        CHECK(cost >= 6.99 
          AND cost <= 15.00),
    genre VARCHAR(20) NOT NULL
        CHECK (genre IN ("Choral", "Country", "Garage", "Indie", 
                         "Opera", "Pop", "R&B", "R&R", "Soul")),
    FOREIGN KEY (label)
        REFERENCES Label (label),
    PRIMARY KEY (CDCode)
);"""

fileOut.write(tableCD + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO CD VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # CDCode
    fileOut.write( "\"" + data[1].strip() + "\",")  # title
    fileOut.write( "\"" + data[2].strip() + "\",")  # artist
    fileOut.write( "\"" + data[3].strip() + "\",")  # label
    fileOut.write(        data[4].strip() + ",")  # numberOfTracks
    fileOut.write(        data[5].strip() + ",")  # cost
    fileOut.write( "\"" + data[6].strip() + "\");\n")  # genre

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
