# Title: H-SDD-Countries
# Author: Mr Friend
# Date: 20 Aug 2025

# Initialise variables
countries = ["UK", "France", "Berlin", "Norway", "Spain", "Italy"]
capitals = ["London", "Paris", "Berlin", "Oslo", "Madrid", "Rome"]
populations = [66.8, 67.4, 83.2, 5.4, 46.8, 60.5]

# Make connection to file
file = open("countries.csv", "w")

# Loop for each record
for index in range(len(countries)):
    
    # Write country to file
    file.write(countries[index] + ",")
    
    # Write capital to file
    file.write(capitals[index] + ",")
    
    # Write populations to file
    file.write(str(populations[index]) + "\n")

# Close connection to file
file.close()