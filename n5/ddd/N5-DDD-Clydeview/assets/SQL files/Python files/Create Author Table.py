# Create Author Table

fileIn = open("Author.csv", "r")
fileOut = open("Author.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

tableAuthor = """CREATE TABLE Author (
    authorRef INT NOT NULL,
    firstName VARCHAR(20),
    surname VARCHAR(20),
    nationality VARCHAR(20),
    dob DATE,
    website VARCHAR(80),
    PRIMARY KEY (authorRef)
);"""

fileOut.write(tableAuthor + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Author VALUES ")
    
    fileOut.write("("   + data[0].strip() + ",")  # authorRef
    fileOut.write( "\"" + data[1].strip() + "\",")  # firstName
    fileOut.write( "\"" + data[2].strip() + "\",")  # surname
    fileOut.write( "\"" + data[3].strip() + "\",")  # nationality
    if data[4].strip() == "":  # dob
        fileOut.write( "NULL,")
    else:
        fileOut.write( "\"" + data[4].strip() + "\",")
    if data[5].strip() == "":  # website
        fileOut.write( "NULL);\n")
    else:
        fileOut.write( "\"" + data[5].strip() + "\");\n")

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()
