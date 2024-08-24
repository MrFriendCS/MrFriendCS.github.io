# Title: 2020 H CS Task 2 Part B
# Author: Mr Friend
# Date: 21 Jan 2020

#
# Subprograms
#

# 1 - Procedure to get a new member
def newMember():

    """
    Get new member first name, surname, category and password.
    OUT: first name, surname, category, password
    """
    
    # Declare local variables
    newFirstName = ""
    newSurname = ""
    newCategory = ""
    newPassword = ""
    
    # 1.1 Get first name
    newFirstName = input("Enter the new member's first name: ")
    
    # 1.2 Get surname
    newSurname = input("Enter the new member's surname: ")
    
    # 1.3 Get category
    newCategory = input("Enter the new member's category: ")

    # 1.4 Call function to get a valid password
    newPassword = getPassword()
    
    return newFirstName, newSurname, newCategory, newPassword


# 1.4 - Function to get a valid password
def getPassword():

    """
    Get a valid password.  Starts with a Capital letter, finishes with #, $, or %.
    OUT: password
    """

    # Declare local variables
    password = ""
    firstLetter = False
    lastLetter = False
    
    # 1.4.1 Loop until password is valid
    while (not firstLetter) or (not lastLetter):
        
        # 1.4.2 Ask the user to enter a password
        password = input("Enter a password: ")
        
        # 1.4.3 - Check that the first character is a capital letter
        if  ord(password[0]) >= 65 and ord(password[0]) <= 90:
            firstLetter = True
        else:
            print("Password must start with a capital letter.")
        
        # 1.4.4 - Check that the last character is #, $ or %
        if ord(password[-1]) >= 35 and ord(password[-1]) <= 37:
            lastLetter = True
        else:
            print("Password must finish with #, $, or %.")
        
    # 1.4.5 Return a valid password
    return password


def getCategory(newFirstName, newSurname, newCategory, newPassword):

    """
    Read existing member data from file to parallel arrays. Add new member data to parallel arrays. Display first name, surname and category of all members.
    """

    # Declare local variables
    file = ""
    line = ""
    counter = 0
    firstNames = [""] * 50
    surnames = [""] * 50
    categories = [""] * 50
    passwords = [""] * 50
    data = [""] * 4

    # 2.1 Read existing member data from file into four parallel arrays: firstName(), surname(), category(), password()

    # Connect to the file
    file = open("members.txt", "r")

    # Read a line from the file
    line = file.readline()

    # Loop if a line has been read from file
    while line != "":

        # Split the line
        data = line.split(",")

        # Store values in parallel arrays
        firstNames[counter] = data[0].strip()
        surnames[counter] = data[1].strip()
        categories[counter] = data[2].strip()
        passwords[counter] = data[3].strip()

        # Increment counter
        counter = counter + 1

        # Read next line of file
        line = file.readline()

    # Close connection to file
    file.close()

    # 2.2 Add the new member data to the existing member data in the parallel arrays

    firstNames[counter] = newFirstName
    surnames[counter] = newSurname
    categories[counter] = newCategory
    passwords[counter] = newPassword

    # Increment counter
    counter = counter + 1
    
    # 2.3 Display the first name, surname and category of all members
    print("Ours members are: ")
    for index in range(counter):
        print(firstNames[index] + " " + surnames[index] + " " + categories[index])

    return categories


def displayInfo(categories):

    """
    Find and display the number of members in each category and the total number of members.
    """

    # Declare local variables
    category = ""
    adult = 0
    junior = 0
    senior = 0
    total = 0

    # Loop for length of array
    for index in range(len(categories)):
        # Get current category
        category = categories[index]

        # Increment appropriate category total
        if category == "Adult":
            adult = adult + 1
        elif category == "Junior":
            junior = junior + 1
        elif category == "Senior":
            senior = senior + 1
    
    # Calculate total membership
    total = adult + junior + senior

    print("There are currently " + str(adult) + " Adult members")
    print("There are currently " + str(junior) + " Junior members")
    print("There are currently " + str(senior) + " Senior members")
    print("Total current membership is " + str(total))


##
## Main program
##

# Declare global variables
firstName = ""
surname = ""
category = ""
password = ""
categories = [""] * 50

# 1. Get new member first name, surname, category and password
firstName, surname, category, password = newMember()

# 2. Read existing member data from file to parallel arrays.
# IN: first name, surname, category, password
categories = getCategory(firstName, surname, category, password)

# 3. Find and display the number of members in each category
# IN: category()
displayInfo(categories)
