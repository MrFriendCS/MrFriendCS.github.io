# Title: N5 SDD SnapTok
# Author: Mr Friend
# Date: 24 Sep 2023

# Declare variables
eligible = False
age = 0
location = ""
username = ""
password = ""
uCheck = ""
pCheck = ""

# Get age and location
age = int(input("Enter your age: "))
location = input("Enter your location: ")

# Is age at least 13 and location UK?
if age >= 13 and location == "uk":
    # Yes

    # Display message
    print("\nYou are eligible for a SnapTok account")

    # Set eligible to True
    eligible = True

else:
    # No

    # Display message
    print("\nYou are not eligible for a SnapTok account")
    print("You must be at least 13 years old and in the UK")
    print("\nGoodbye!")

# Is user eligible for an account?
if eligible == True:
    # Yes

    # Enter username and password
    username = input("\nChoose a username: ")
    password = input("Choose a password: ")

    # Re-enter username and password
    uCheck = input("\nRe-enter username: ")
    pCheck = input("Re-enter password: ")

    # Do uesernames and passwords match?
    if uCheck == username and pCheck == password:
        # Yes

        # Display message
        print("\nWelcome to SnapTok!")

    else:
        # No

        # Display message
        print("\nInvalid details - Goodbye!")
