# Create Book Table

fileIn = open("Book.csv", "r")
fileOut = open("Book.sql", "w")

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

tableBook = """CREATE TABLE Book (
    category VARCHAR(5) NOT NULL 
        CHECK (category IN ("Adult", "Child")),
    genre VARCHAR(13) NOT NULL 
        CHECK (genre IN ("Joke\", "Sport", "Fiction", "Fantasy",
                         "Thriller", "Autobiography", "Mystery")),
    title VARCHAR(100) NOT NULL,
    authorRef INT NOT NULL,
    publisher VARCHAR(30) NOT NULL,
    ISBN VARCHAR(10) NOT NULL 
        CHECK (LENGTH(ISBN) = 10),
    dateOfPublication DATE,
    numberOfPages INT NOT NULL 
        CHECK(numberOfPages >=26 
          AND numberOfPages <= 950),
    FOREIGN KEY (authorRef) 
        REFERENCES Author (authorRef),
    PRIMARY KEY (title)
);"""

fileOut.write(tableBook + "\n\n")

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Book VALUES ")
    
    fileOut.write("(\"" + data[0].strip() + "\",")  # category
    fileOut.write( "\"" + data[1].strip() + "\",")  # genre
    fileOut.write( "\"" + data[2].strip() + "\",")  # title
    fileOut.write( "\"" + data[3].strip() + "\",")  # authorRef
    fileOut.write( "\"" + data[4].strip() + "\",")  # publisher
    fileOut.write( "\"" + data[5].strip() + "\",")  # ISBN
    fileOut.write( "\"" + data[6].strip() + "\",")  # dateOfPublication
    fileOut.write(        data[7].strip() + ");\n")  # numberOfPages

    line = fileIn.readline()
    
fileIn.close()
fileOut.close()