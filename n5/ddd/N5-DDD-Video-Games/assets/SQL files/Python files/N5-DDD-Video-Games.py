# Title: N5-DDD-Video-Games
# Author: Mr Friend
# Date: 6 Oct 2024

def createCompanyTable():
    """Create sql file for company table."""

    # Initialise variables
    rows = 6
    names = [""] * rows
    foundeds = [""] * rows
    countries = [""] * rows
    websites = [""] * rows
    profits = [0] * rows

    # Open file
    file = open("Company.csv", "r")
        
    # Ignore first row - Headers
    line = file.readline()

    # Loop for each company
    for index in range(rows):
        
        line = file.readline()
        
        temp = line.split(",")
        
        names[index] = temp[0].strip()
        countries[index] = temp[1].strip()
        foundeds[index] = temp[2].strip()
        websites[index] = temp[3].strip()
        profits[index] = int(temp[4].strip())
        
    file.close()


    # Create file
    file = open("Company.sql", "w")
     
    # SQL - Create table

    table = """CREATE TABLE Company (
    name VARCHAR(20) NOT NULL UNIQUE,
    country VARCHAR(20) NOT NULL,
    founded DATE NOT NULL
        CHECK(founded >= \"1970-01-01\"),
    website VARCHAR(30),
    profit INT NOT NULL,
    PRIMARY KEY (name)
);"""

    file.write(table + "\n\n")

    # SQL - Create values

    # Loop for each row
    for index in range(rows):
        file.write("INSERT INTO Company VALUES (")
        file.write("\"" + names[index] + "\",")
        file.write("\"" + countries[index] + "\",")
        file.write("\"" + foundeds[index] + "\",")
        file.write("\"" + websites[index] + "\",")
        file.write(str(profits[index]) + ");\n")
        
    file.close()
    
    
def createGameTable():
    """Create sql file for Game table."""

    # Initialise variables
    rows = 121
    titles = [""] * rows
    companies = [""] * rows
    genres = [""] * rows
    ages = [0] * rows
    prices = [0.0] * rows
    releases = [""] * rows
    countries = [""] * rows
    sales = [0] * rows

    # Open file
    file = open("Game.csv", "r")
        
    # Ignore first row - Headers
    line = file.readline()

    # Loop for each row
    for index in range(rows):
        
        line = file.readline()
        
        temp = line.split(",")
        
        titles[index] = temp[0].strip()
        companies[index] = temp[1].strip()
        genres[index] = temp[2].strip()
        ages[index] = int(temp[3].strip())
        prices[index] = float(temp[4].strip())
        releases[index] = temp[5].strip()
        sales[index] = int(temp[6].strip())
        
    file.close()


    # Create file
    file = open("Game.sql", "w")
     
    # SQL - Create table

    table = """CREATE TABLE Game (
    title VARCHAR(30) NOT NULL UNIQUE,
    company VARCHAR(20) NOT NULL,
    genre VARCHAR(15) NOT NULL,
    age INT NOT NULL
        CHECK(age IN (3, 7, 12, 16, 18)),
    price FLOAT NOT NULL
        CHECK(price >= 0 AND price <= 100),
    released DATE NOT NULL
        CHECK(released >= \"1970-01-01\"),
    copies_sold INT NOT NULL
        CHECK(copies_sold >= 0),
    FOREIGN KEY (company)
        REFERENCES company(name),
    PRIMARY KEY (title)
);"""

    # SQL - Create values

    # Loop for each row
    for index in range(rows):
        file.write("INSERT INTO Game VALUES (")
        file.write("\"" + titles[index] + "\",")
        file.write("\"" + companies[index] + "\",")
        file.write("\"" + genres[index] + "\",")
        file.write(str(ages[index]) + ",")
        file.write(str(prices[index]) + ",")
        file.write("\"" + releases[index] + "\",")
        file.write(str(sales[index]) + ");\n")
        
    file.close()


def main():
    
    createCompanyTable()
    createGameTable()
    

# Call main()
main()