# Title: N5-DDD-Membership
# Author: Mr Friend
# Date: 28 Sep 2024

def createClubTable():
    """Create sql file for club table."""

    # Initialise variables
    rows = 8
    ids = [""] * rows
    names = [""] * rows
    locations = [""] * rows
    types = [""] * rows
    opened = [""] * rows
    trainers = [False] * rows
    rooms = [0] * rows

    # Open file
    file = open("Club.csv", "r")
        
    # Ignore first row - Headers
    line = file.readline()

    # Loop for each company
    for index in range(rows):
        
        line = file.readline()
        
        temp = line.split(",")
        
        ids[index] = temp[0].strip()
        names[index] = temp[1].strip()
        locations[index] = temp[2].strip()
        types[index] = temp[3].strip()
        opened[index] = temp[4].strip()
        trainer = temp[5].strip()
        if trainer[0] == "T":
            trainers[index] = 1
        else:
            trainers[index] = 0
        rooms[index] = int(temp[6].strip())
        
    file.close()

    # Create file
    file = open("club.sql", "w")
     
    # SQL - Create table
    file.write("CREATE TABLE club (\n")
    file.write("    id VARCHAR(6) NOT NULL UNIQUE,\n")
    file.write("    name VARCHAR(30) NOT NULL,\n")
    file.write("    location VARCHAR(30) NOT NULL,\n")
    file.write("    type VARCHAR(20) NOT NULL,\n")
    file.write("    opened DATE,\n")
    file.write("    trainer BOOLEAN,\n")
    file.write("    rooms INT CHECK(rooms >= 0),\n")
    file.write("    PRIMARY KEY (id)\n")
    file.write(");\n\n")

    # SQL - Create values
    for index in range(rows):
        file.write("INSERT INTO club VALUES (")
        file.write("\"" + ids[index] + "\",")
        file.write("\"" + names[index] + "\",")
        file.write("\"" + locations[index] + "\",")
        file.write("\"" + types[index] + "\",")
        file.write("\"" + opened[index] + "\",")
        file.write(str(trainers[index]) + ",")
        file.write(str(rooms[index]) + ")")
        file.write(";\n")
        
    file.close()
    
    
def createMemberTable():
    """Create sql file for member table."""

    # Initialise variables
    rows = 200
    ids = [""] * rows
    clubs = [""] * rows
    firsts = [""] * rows
    lasts = [""] * rows
    addresses = [""] * rows
    towns = [""] * rows
    postcodes = [""] * rows
    dobs = [""] * rows
    months = [0] * rows
    genders = [""] * rows
    types = [""] * rows

    # Open file
    file = open("Member.csv", "r")
        
    # Ignore first row - Headers
    line = file.readline()

    # Loop for each row
    for index in range(rows):
        
        line = file.readline()
        
        temp = line.split(",")
        
        ids[index] = temp[0].strip()
        clubs[index] = temp[1].strip()
        firsts[index] = temp[2].strip()
        lasts[index] = temp[3].strip()
        addresses[index] = temp[4].strip()
        towns[index] = temp[5].strip()
        postcodes[index] = temp[6].strip()
        dobs[index] = temp[7].strip()
        months[index] = int(temp[8].strip())
        genders[index] = temp[9].strip()
        types[index] = temp[10].strip()
        
    file.close()

    # Create file
    file = open("member.sql", "w")
     
    # SQL - Create table
    file.write("CREATE TABLE member (\n")
    file.write("    member_no VARCHAR(8) NOT NULL UNIQUE,\n")
    file.write("    club_id VARCHAR(6) NOT NULL,\n")
    file.write("    first_name VARCHAR(20) NOT NULL,\n")
    file.write("    last_name VARCHAR(30) NOT NULL,\n")
    file.write("    address VARCHAR(30),\n")
    file.write("    town VARCHAR(20),\n")
    file.write("    postcode VARCHAR(8),\n")
    file.write("    dob DATE NOT NULL\n")
    file.write("        CHECK(dob >= \"1925-01-01\"),\n")
    file.write("    renew INT NOT NULL\n")
    file.write("        CHECK(renew >=1 AND renew <= 12),\n")
    file.write("    gender VARCHAR(15)\n")
    file.write("        CHECK(gender IN (\"F\", \"M\", \"ND\")),\n")
    file.write("    type VARCHAR(15) NOT NULL\n")
    file.write("        CHECK(type IN (\"Adult\", \"Child\", \"Guest\",\n")
    file.write("                       \"Senior\", \"Student\")),\n")
    file.write("    PRIMARY KEY (member_no)\n")
    file.write("    FOREIGN KEY (club_id)\n")
    file.write("        REFERENCES club(id)\n")
    file.write(");\n\n")

    # SQL - Create values
    for index in range(rows):
        file.write("INSERT INTO member VALUES (")
        file.write("\"" + ids[index] + "\",")
        file.write("\"" + clubs[index] + "\",")
        file.write("\"" + firsts[index] + "\",")
        file.write("\"" + lasts[index] + "\",")
        file.write("\"" + addresses[index] + "\",")
        file.write("\"" + towns[index] + "\",")
        file.write("\"" + postcodes[index] + "\",")
        file.write("\"" + dobs[index] + "\",")
        file.write(str(months[index]) + ",")
        file.write("\"" + genders[index] + "\",")
        file.write("\"" + types[index] + "\"")
        file.write(");\n")
        
    file.close()


def main():
    
    createClubTable()
    createMemberTable()
    

# Call main()
main()