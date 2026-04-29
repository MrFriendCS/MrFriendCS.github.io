# Title: N5 DDD Create Clydeview DB
# Author: Mr Friend
# Date: 23 Apr 2026

# Get extra code
import sqlite3


def dropSuperHeroTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS SuperHero;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createSuperHeroTable():
    
    # SQL query
    createTable = '''CREATE TABLE SuperHero (
    characterID INT NOT NULL,
    name VARCHAR(40),
    role VARCHAR(30),
    mainAbility VARCHAR(30),
    ability2 VARCHAR(30),
    ability3 VARCHAR(30),
    originOfPower VARCHAR(30),
    alterEgo VARCHAR(40),
    PRIMARY KEY (characterID)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertSuperHeroData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/SuperHero.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        charID = data[0].strip()
        name = data[1].strip()
        role = data[2].strip()
        mainAbility = data[3].strip()
        ability2 = data[4].strip()
        ability3 = data[5].strip()
        originOfPower = data[6].strip()
        alterEgo = data[7].strip()
             
        values = f'({charID},"{name}","{role}","{mainAbility}",'

        if ability2 == '':
            ability2 = 'NULL'
        else:
            ability2 = f'"{ability2}"'
            
        if ability3 == '':
            ability3 = 'NULL'
        else:
            ability3 = f'"{ability3}"'
            
        if alterEgo == '':
            alterEgo = 'NULL'
        else:
            alterEgo = f'"{alterEgo}"'
        
        values = values + f'{ability2},{ability3},"{originOfPower}",{alterEgo})'
        
        # SQL to insert data
        newData = f'INSERT INTO SuperHero VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropCustomerTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Customer;
    '''

    # Drop the table
    cursor.execute(dropTable)

def createCustomerTable():
    
    # SQL query
    createTable = '''CREATE TABLE Customer (
    customerNo INT NOT NULL,
    forename VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    street VARCHAR(50) NOT NULL,
    town VARCHAR(20) NOT NULL,
    package VARCHAR(10) NOT NULL CHECK (package IN 
        ("Standard", "Large", "Premier")),
    directDebit BOOL NOT NULL,
    paymentDue DATE,
    PRIMARY KEY (customerNo)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertCustomerData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Customer.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        custNo = data[0].strip()
        forename = data[1].strip()
        surname = data[2].strip()
        street = data[3].strip()
        town = data[4].strip()
        package = data[5].strip()
        directDebit = data[6].strip()
        paymentDue = data[7].strip()
        
        # Create data
        values = f'({custNo},"{forename}","{surname}","{street}",' \
                 + f'"{town}","{package}",'
        
        directDebit = f'{"FALSE" if directDebit=="0" else "TRUE"}'
               
        values = values + f'{directDebit},"{paymentDue}")'
        
        # SQL to insert data
        newData = f'INSERT INTO Customer VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropAuthorTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Author;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createAuthorTable():
    
    # SQL query
    createTable = '''CREATE TABLE Author (
    authorRef INT NOT NULL,
    forename VARCHAR(20),
    surname VARCHAR(20),
    nationality VARCHAR(20),
    dob DATE,
    website VARCHAR(80),
    PRIMARY KEY (authorRef)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertAuthorData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Author-Book/Author.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        authorRef = data[0].strip()
        forename = data[1].strip()
        surname = data[2].strip()
        nationality = data[3].strip()
        dob = data[4].strip()
        website = data[5].strip()
        
        # Create data
        values = f'({authorRef},"{forename}","{surname}","{nationality}",'
        
        if dob == '':
            dob = 'NULL'
        else:
            dob = f'"{dob}"'
        
        if website == '':
            website = 'NULL'
        else:
            website = f'"{website}"'
        
        values = values + f'{dob},{website})'
        
        # SQL to insert data
        newData = f'INSERT INTO Author VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropBookTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Book;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createBookTable():
    
    # SQL query
    createTable = '''CREATE TABLE Book (
    category VARCHAR(5) NOT NULL 
        CHECK (category IN ("Adult", "Child")),
    genre VARCHAR(13) NOT NULL 
        CHECK (genre IN ("Joke", "Sport", "Fiction", "Fantasy",
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
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertBookData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Author-Book/Book.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        category = data[0].strip()
        genre = data[1].strip()
        title = data[2].strip()
        authorRef = data[3].strip()
        publisher = data[4].strip()
        ISBN = data[5].strip()
        published= data[6].strip()
        pages = data[7].strip()
        
        # Create data
        values = f'("{category}","{genre}","{title}","{authorRef}","' \
                 + f'{publisher}","{ISBN}","{published}",{pages})'
        
        # SQL to insert data
        newData = f'INSERT INTO Book VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropLabelTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Label;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createLabelTable():
    
    # SQL query
    createTable = '''CREATE TABLE Label (
    label VARCHAR(20) NOT NULL,
    founded INT NOT NULL,
    parentCompany VARCHAR(30),
    country VARCHAR(7) NOT NULL 
        CHECK (country IN ("Germany", "Japan", "UK", "USA")),
    website VARCHAR(50),
    PRIMARY KEY (label)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertLabelData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Label-CD/Label.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        label = data[0].strip()
        founded = data[1].strip()
        parentCompany = data[2].strip()
        country = data[3].strip()
        website = data[4].strip()
        
        # Create data
        values = f'("{label}",{founded},"{parentCompany}","{country}",' \
                 + f'"{website}")'
        
        # SQL to insert data
        newData = f'INSERT INTO Label VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropCDtable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS CD;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createCDtable():
    
    # SQL query
    createTable = '''CREATE TABLE CD (
    code VARCHAR(4) NOT NULL 
        CHECK(LENGTH(code) = 4),
    title VARCHAR(40) NOT NULL,
    artist VARCHAR(40) NOT NULL,
    label VARCHAR(20) NOT NULL,
    tracks INT 
        CHECK (tracks >= 10 
           AND tracks <= 60),
    cost REAL NOT NULL 
        CHECK(cost >= 6.99 
          AND cost <= 15.00),
    genre VARCHAR(20) NOT NULL
        CHECK (genre IN ("Choral", "Country", "Garage", "Indie", 
                         "Opera", "Pop", "R&B", "R&R", "Soul")),
    FOREIGN KEY (label)
        REFERENCES Label(label),
    PRIMARY KEY (code)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertCDdata():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Label-CD/CD.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        code = data[0].strip()
        title = data[1].strip()
        artist = data[2].strip()
        label = data[3].strip()
        tracks = data[4].strip()
        cost = data[5].strip()
        genre = data[6].strip()
        
        # Create data
        values = f'("{code}","{title}","{artist}","{label}",{tracks},' \
                 + f'{cost},"{genre}")'
        
        # SQL to insert data
        newData = f'INSERT INTO CD VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropOwnerTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Owner;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createOwnerTable():
    
    # SQL query
    createTable = '''CREATE TABLE Owner (
    ownerID INTEGER NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    address VARCHAR(40) NOT NULL,
    town VARCHAR(20) NOT NULL,
    contactTele VARCHAR(11) NOT NULL 
        CHECK (LENGTH(contactTele) = 11),
    PRIMARY KEY (ownerID)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertOwnerData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Owner-Pet/Owner.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        ownerID = data[0].strip()
        first = data[1].strip()
        last = data[2].strip()
        address = data[3].strip()
        town = data[4].strip()
        contactTele = data[5].strip()
        
        # Create data
        values = f'({ownerID},"{first}","{last}","{address}","{town}",' \
                 + f'"{contactTele}")'
        
        # SQL to insert data
        newData = f'INSERT INTO Owner VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropPetTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Pet;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createPetTable():
    
    # SQL query
    createTable = '''CREATE TABLE Pet (
    code VARCHAR(5) NOT NULL 
        CHECK(LENGTH(code) = 5),
    name VARCHAR(20),
    type VARCHAR(8)
        CHECK (type IN("Budgie", "Cat", "Dog", "Gerbil", "Tortoise")),
    dateOfBirth DATE
        CHECK (dateOfBirth LIKE "____-__-__"),
    vaccination BOOL
        CHECK (vaccination IN (TRUE, FALSE)),
    ownerID INT NOT NULL,
    FOREIGN KEY (ownerID)
        REFERENCES Owner (ownerID),
    PRIMARY KEY (code)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertPetData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Owner-Pet/Pet.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        code = data[0].strip()
        name = data[1].strip()
        petType = data[2].strip()
        dob = data[3].strip()
        vax = data[4].strip()
        ownerID = data[5].strip()
        
        # Create data
        values = f'("{code}","{name}","{petType}","{dob}",'
        
        if vax == "0":
            vax = 'FALSE'
        else:
            vax = 'TRUE'
        
        values = values + f'{vax},{ownerID})'
        
        # SQL to insert data
        newData = f'INSERT INTO Pet VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropManufacturerTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Manufacturer;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createManufacturerTable():
    
    # SQL query
    createTable = '''CREATE TABLE Manufacturer (
    manufacturerID INT NOT NULL,
    name VARCHAR(20),
    address VARCHAR(40),
    telephone VARCHAR(11) 
        CHECK (LENGTH(telephone) = 11),
    PRIMARY KEY (manufacturerID)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertManufacturerData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Manufacturer-Product/Manufacturer.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        manID = data[0].strip()
        name = data[1].strip()
        address = data[2].strip()
        telephone = data[3].strip()
        
        # Create data
        values = f'({manID},"{name}","{address}","{telephone}")'
        
        # SQL to insert data
        newData = f'INSERT INTO Manufacturer VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


def dropProductTable():
    
    # SQL query
    dropTable = '''
    DROP TABLE IF EXISTS Product;
    '''

    # Drop the table
    cursor.execute(dropTable)


def createProductTable():
    
    # SQL query
    createTable = '''CREATE TABLE Product (
    name VARCHAR(30) NOT NULL,
    code VARCHAR(4) NOT NULL,
    stock INT NOT NULL
        CHECK (stock >= 0 AND stock <= 50),
    onOrder BOOL,
    price REAL,
    manufacturerID INT NOT NULL,
    FOREIGN KEY (manufacturerID) 
        REFERENCES Manufacturer (manufacturerID),
    PRIMARY KEY (code)
    );'''

    # Create the new table
    cursor.execute(createTable)


def insertProductData():
    
    line = ''
    data = []
    values = ''
    
    file = open('../CSV/Manufacturer-Product/Product.csv', 'r', encoding='utf-8')
    
    # Read header
    line = file.readline()
    
    # Read first line
    line = file.readline()
    
    # Loop for each record
    while line != '':
        
        # Split data
        data = line.split(',')
        
        name = data[0].strip()
        code = data[1].strip()
        stock = data[2].strip()
        onOrder = data[3].strip()
        price = data[4].strip()
        manID = data[5].strip()
        
        # Create data
        values = f'("{name} ","{code}",{stock},'
        
        onOrder = f'{"FALSE" if onOrder=="0" else "TRUE"}'

        values = values + f'{onOrder},{price},{manID})'
        
        # SQL to insert data
        newData = f'INSERT INTO Product VALUES {values};'
        
        # Insert new data
        cursor.execute(newData)

        # Commit the new data
        conn.commit()
        
        # Read next line
        line = file.readline()


#
# Main program
#

# Create a connection to a database
# Creates a new database file, if it doesn’t exist
conn = sqlite3.connect('../Clydeview.db')

# Create a database cursor
cursor = conn.cursor()


# SuperHero table
print("1. SuperHero table")
dropSuperHeroTable()
createSuperHeroTable()
insertSuperHeroData()


# Customer table
print("2. Customer table")
dropCustomerTable()
createCustomerTable()
insertCustomerData()


# Author table
print("3. Author table")
dropAuthorTable()
createAuthorTable()
insertAuthorData()


# Book table
print("4. Book table")
dropBookTable()
createBookTable()
insertBookData()


# Label table
print("5. Label table")
dropLabelTable()
createLabelTable()
insertLabelData()


# CD table
print("6. CD table")
dropCDtable()
createCDtable()
insertCDdata()


# Owner table
print("7. Owner table")
dropOwnerTable()
createOwnerTable()
insertOwnerData()


# Pet table
print("8. Pet table")
dropPetTable()
createPetTable()
insertPetData()


# Manufacturer table
print("9. Manufacturer table")
dropManufacturerTable()
createManufacturerTable()
insertManufacturerData()


# Product table
print("10. Product table")
dropProductTable()
createProductTable()
insertProductData()


# Close the connection to the database
conn.close()
