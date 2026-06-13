# Title: H CS 2024S Task 1 Part B
# Author: Mr Friend
# Date: 20 Jan 2025


#
# Functions and Procedures
#

def getData() -> tuple[list[str], list[str], list[str], list[str], list[int]]:
    """1. Get qualifying athletes’ data."""
    
    # Declare local varaibles and arrays
    length = 30
    line = ""
    data = [""] * 5
    entryID = [""] * length
    location = [""] * length
    forename = [""] * length
    surname = [""] * length
    jumps = [0] * length

    # 1.1 Open athletes.csv file
    file = open("athletes.csv", "r", encoding="UTF-8")
    
    # 1.2 Loop for thirty athletes
    for index in range(30):

        # Read line from file
        line = file.readline()

        # Split line
        data = line.split(",")
    
        # 1.3 Store entryID, location, forename, surname, jumps
        #     for athlete in parallel arrays
        entryID[index] = data[0].strip()
        location[index] = data[1].strip()
        forename[index] = data[2].strip()
        surname[index] = data[3].strip()
        jumps[index] = int(data[4].strip())
    
    # 1.4 End loop
    
    # 1.5 Close athletes.csv file
    file.close()

    # Return values to main program
    return entryID, location, forename, surname, jumps


def createBibValues(entryID: list[str], location: list[str],
                    forename: list[str], surname: list[str]) -> None:
    """2. Generate bib values and write to new file with entry IDs."""

    # Declare local variable
    bibValue = ""
    
    # 2.1 Create bibValues.csv file
    file = open("bibValues.csv", "w", encoding="UTF-8")
    
    # 2.2 Loop for thirty athletes
    for index in range(30):
        
        # 2.3 Set bibValue to first letter of forename & full surname
        #     & ASCII value of first letter of location
        bibValue = forename[index][0] + surname[index]
        bibValue = bibValue + str(ord(location[index][0]))
        
        # 2.4 Write entryID and bibValue to file
        file.write(entryID[index] + "," + bibValue + "\n")
        
    # 2.5 End loop
    
    # 2.6 Close bibValues.csv file
    file.close()


def findMost(jumps: list[int]) -> int:

    """3. Find the highest number of jumping jacks completed."""

    # Declare local variable
    maxJumps = 0
    
    # 3.1 Set maximum jumps to the value stored in the first
    #     index of the jumps array
    maxJumps = jumps[0]

    # 3.2 Start loop from second index to end of array
    for index in range(1, 30):
            
        # 3.3 If the current number of jumps is more than
        #     maximum jumps then
        if jumps[index] > maxJumps:
    
            # 3.4 Set maximum jumps to current number of jumps
            maxJumps = jumps[index]

        # 3.5 End if
    
    # 3.6 End loop
    
    # 3.7 Return maximum jumps
    return maxJumps


def dislayBigJumpers(maxJumps: int, forenames: list[str],
                     surnames: list[str], jumps: list[int]):
    """4. Display the full name of the athlete(s) who completed
       the highest number of jumping jacks.
       """
    
    # 4.1 Loop for thirty athletes
    for index in range(30):
        
        # 4.2 If current number of jumps equals maximum jumps then
        if jumps[index] == maxJumps:
        
            # 4.3 Display forename and surname
            print(forenames[index] + " " + surnames[index])

        # 4.4 End if
        
    # 4.5 End loop


def countLocations(locations: list[str]) -> None:
    """5. Display the total number of athletes from each
       location in the final.
       """

    # Declare local variables
    coatbridge = 0
    inverness = 0     
    kirkcaldy = 0
    motherwell = 0
    other = 0

    # Loop for thirty athletes
    for index in range(30):

        if locations[index] == "Coatbridge":
            coatbridge = coatbridge + 1
        
        elif locations[index] == "Inverness":
            inverness = inverness + 1

        elif locations[index] == "Kirkcaldy":
            kirkcaldy = kirkcaldy + 1

        elif locations[index] == "Motherwell":
            motherwell = motherwell + 1

        else:
            other = other + 1

    # Display results
    print("\nCoatbridge has " + str(coatbridge) + " finalists")
    print("Inverness has " + str(inverness) + " finalists")
    print("Kirkcaldy has " + str(kirkcaldy) + " finalists")
    print("Motherwell has " + str(motherwell) + " finalists\n")

    # Not really needed
    if other != 0:
        print("There are " + str(other) + "other finalists")

        
#
# Main Program
#

# Declare global variables and arrays

length = 30
maxJumps = 0
entryID = [""] * length
location = [""] * length
forename = [""] * length
surname = [""] * length
jumps = [0] * length

# 1. Get qualifying athletes’ data
entryID, location, forename, surname, jumps =  getData()

# 2. Generate bib values and write to new file with entry IDs
createBibValues(entryID, location, forename, surname)

# 3. Find the highest number of jumping jacks completed
maxJumps = findMost(jumps)

# 4. Display the full name of the athlete(s) who completed
#    the highest number of jumping jacks
dislayBigJumpers(maxJumps, forename, surname, jumps)

# 5. Display the total number of athletes from each location
#    in the final
countLocations(location)
