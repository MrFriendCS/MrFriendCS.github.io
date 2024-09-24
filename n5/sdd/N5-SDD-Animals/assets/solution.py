# Title: N5 SDD Animals
# Author: Mr Friend
# Date: 12 Oct 2023

# Declare variables
name = ""
age = 0
catAnswer = ""
dogAnswer = ""
type = ""

# Get name
while name == "":
    name = input("Hi!  What is your name? ")
    # Error message if left balnk
    if name == "":
        print("\nAre you shy?")

# Get age
while age < 11 or age > 18:
    # Get answer
    age = int(input("\nHi " + name + " how old are you? "))

    # Error message if too young or too old
    if age < 11 or age > 18:
        print(name + "! You must be aged 11 to 18.")

# Like cats?
while catAnswer != "yes" and catAnswer != "no":
    # Get answer: 'yes' or 'no'
    catAnswer = input("\n" + name + ", do you like cats? ")

    # Error message if not 'yes' or 'no'
    if catAnswer != "yes" and catAnswer != "no":
        print(name + "! It's a yes or no question.")

# Like dogs?
while dogAnswer != "yes" and dogAnswer != "no":
    # Get answer: 'yes' or 'no'
    dogAnswer = input("\n" + name + ", do you like dogs? ")

    # Error message if not 'yes' or 'no'
    if dogAnswer != "yes" and dogAnswer != "no":
        print(name + "! It's a yes or no question.")

# Display data summary
print("\nData Summary")
print("------------")
print("Name: " + name)
print("Age: " + str(age))
print("Like cats: " + catAnswer)
print("Like dogs: " + dogAnswer)

# Decide type of person
if catAnswer == "yes" and dogAnswer == "yes":
    type = "a good"
elif catAnswer == "no" and dogAnswer == "no":
    type = "an evil"
else:
    # Everyone else
    type = "an ok"

# Display results
print("\nFrom your answers about animals")
print("I think you're " + type + " person!")
