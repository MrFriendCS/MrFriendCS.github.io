# Title: H SDD Tuck Shop
# Author: Mr Friend
# Date 23 Aug 2024

# Declare global variables and arrays
names = [""] * 11
weights = [0] * 11
prices = [0.0] * 11
newPrices = [0.0] * 11
line = ""
temp = [""] * 3
firstLetter = ""
ascii = 0

# Open connection to file
file = open("tuckshop.txt", "r")

# Loop for each line of data
for index in range(len(names)):
    # Read line of data
    line = file.readline()

    # Split line - array
    temp = line.split(",")

    # Assign values to arrays
    names[index] = temp[0].strip()
    weights[index] = int(temp[1].strip())
    prices[index] = float(temp[2].strip())
    
# close connection to file
file.close()


# Loop for each value
for index in range(len(prices)):

    # Increase by 10%
    prices[index] = round(prices[index] * 1.10, 2)

# Loop for each name
for index in range(len(names)):

    # Get first letter
    firstLetter = names[index][0]
    
    # ASCII value
    ascii = ord(firstLetter)
    
    if ascii >= 97 and ascii <= 122:
        firstLetter = chr(ascii-32)
        names[index] = firstLetter + names[index][1: ]


# Open connection to file
file = open("pricelist.txt", "w")

file.write("Tuck Shop Price List\n")
file.write("--------------------\n\n")

# Loop for each line of data
for index in range(len(names)):
    
    file.write(names[index] + " (")
    file.write(str(weights[index]) + "g) - ")
    
    if prices[index] >= 1:
        file.write("£" + str(prices[index]) + "\n")
    else:
        file.write(str(prices[index]) + "p" + "\n")

file.write("\nEnd of price list!")

# close connection to file
file.close()
