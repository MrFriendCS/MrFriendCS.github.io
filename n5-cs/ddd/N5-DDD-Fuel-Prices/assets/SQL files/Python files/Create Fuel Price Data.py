# Title: N5-DDD-Fueld-Prices
# Author: Mr Friend
# Date: 15 Jan 2026

"""
Data source: https://www.developer.fuel-finder.service.gov.uk/access-latest-fuelprices

Read and clean the data, and then export as CSV file.
"""

def readData():
    """Read data from file."""
    
    # Initialise local variables
    line = ""
    temp = []
    
    # Connect to the raw data
    file = open("../CSV files/UpdatedFuelPrice.csv", "r")
    
    # Read first line of data
    line = file.readline()
    
    # Split the data
    temp = line.split(",")
    
    print(temp)
    
    file.close()
    
    


def writeCSV(a, b, c, d, e, f, g, h, i):
    """Create prisoner CSV file."""
    
    file = open("../FuelPrice.csv", "w")
    
    
    # Loop for each prisoner
    for index in range(len(a)):
        file.write(str(a[index]) + ",")
        file.write(    b[index] + ",")
        file.write(    c[index] + ",")
        file.write(    d[index] + ",")
        file.write(    e[index] + ",")
        file.write(str(f[index]) + ",")
        file.write(    g[index] + ",")
        file.write(str(h[index]) + ",")
        file.write(    i[index] + "\n")
        
    file.close()


def main():
    """Main program."""

    # Initialise variables
    noOfPrisoners = 200 

    # 1 - Get IDs
    ids = getIDs(noOfPrisoners)

    # 2 - Get surnames
    surnames = getSurnames(noOfPrisoners)

    # 3 - Get forename
    forenames = getForenames(noOfPrisoners)
    
    # 4 - Get hair colours
    hairs = getHairColours(noOfPrisoners)
    
    # 5 - Get eye colurs
    eyes = getEyeColours(noOfPrisoners)
    
    # 6 - Get eye colurs
    heights = getHeights(noOfPrisoners)
    
    # 7 - Get convictions
    convictions = getConvictions(noOfPrisoners)
    
    # 8 - Get open prisons
    opens = getOpens(noOfPrisoners)
    
    # 9 - Get DOBs
    dobs = getDOBs(noOfPrisoners)

    # 10 - Get pupil names
    pupilFirsts, pupilLasts = getPupils()
    
    # 11 = Update names
    forenames, surnames = updateNames(forenames, surnames, pupilFirsts, pupilLasts)

    # 12 - Write prisoner table
    writeCSV(ids, surnames, forenames, hairs, eyes,
                       heights, convictions, opens, dobs)


# Call main()
# main()
