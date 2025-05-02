# Title: Book Table
# Author: Mr Friend
# Date: 22 Nov 2024

# Files
fileIn = open("../CSV files/Author-Book/Book.csv", "r")
fileOut = open("../Book.sql", "w")


# Create table

table = """CREATE TABLE Book (
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
    published DATE NOT NULL,
    pages INT NOT NULL 
        CHECK(pages >=26 
          AND pages <= 950),
    PRIMARY KEY (title),
    FOREIGN KEY (authorRef) 
        REFERENCES Author (authorRef)
);"""

fileOut.write(table + "\n\n")


# Insert data

line = fileIn.readline()  # Ignore heading row
line = fileIn.readline()

while line != "":
    
    data = line.split(",")
    
    fileOut.write("INSERT INTO Book VALUES (")
    
    fileOut.write("\"" + data[0].strip() + "\",")  # category
    fileOut.write("\"" + data[1].strip() + "\",")  # genre
    fileOut.write("\"" + data[2].strip() + "\",")  # title
    fileOut.write("\"" + data[3].strip() + "\",")  # authorRef
    fileOut.write("\"" + data[4].strip() + "\",")  # publisher
    fileOut.write("\"" + data[5].strip() + "\",")  # ISBN
    fileOut.write("\"" + data[6].strip() + "\",")  # published
    fileOut.write(       data[7].strip() + ");")  # pages
    fileOut.write("\n")

    line = fileIn.readline()


fileIn.close()
fileOut.close()
