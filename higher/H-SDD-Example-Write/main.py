# Title: H SDD Example Write
# Author: Mr Friend
# Date: 28 Sep 2023

"""
A program to demonstrate writing to csv and txt files.
"""

#
# Subprograms
#

def writeCSV(names, orders, spends, discounts):
    """
    Write data to a comma seprerated values file.
    """

    # Open (create) the file in write mode
    file = open("csvFile.csv", "w")

    # Loop for each element
    for index in range(len(names)):
        file.write(names[index] + ",")
        file.write(str(orders[index]) + ",")
        file.write(str(spends[index]) + ",")
        file.write(str(discounts[index]) + "\n")

    # Close the file
    file.close


def writeTXT(nicks, orders, spends, discounts):
    """
    Write data to a text file.
    """

    # Open (create) the file in write mode
    file = open("textFile.txt", "w")

    # Write opening text
    file.write("Big Spend Shop\n")
    file.write("--------------\n\n")
    file.write("Customer details:\n\n")

    # Loop for each element
    for index in range(len(names)):
        file.write(names[index] + " has ordered ")
        file.write(str(orders[index]) + " times and spent £")
        file.write(str(spends[index]) + ".\n")
        if discounts[index]:
            file.write("\t" + names[index])
            file.write(" is entitled to a discount.\n")

    # Write closing text
    file.write("\n--------------\n")

    # Close the file
    file.close


#
# Main program
#

# Declare global arrays
names = ["Abe", "Bob", "Cat", "Dee"]
orders = [5, 3, 9, 4]
spends = [34.56, 21.98, 85.21, 29.71]
discounts = [True, False, False, True]

# Write data to csv file
writeCSV(names, orders, spends, discounts)

# Write data to text file
writeTXT(names, orders, spends, discounts)
