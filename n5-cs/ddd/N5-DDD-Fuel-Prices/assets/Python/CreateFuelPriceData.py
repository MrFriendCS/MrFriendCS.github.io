# Title: N5-DDD-Fuel-Prices
# Author: Mr Friend
# Date: 23 Mar 2026

"""
Data source: https://www.developer.fuel-finder.service.gov.uk/access-latest-fuelprices

Read and clean the data, and then export as CSV file.
"""


# Get extra code
from dataclasses import dataclass

@dataclass
class Station:
    """Defines a record for a service station."""
    name: str = ""
    postcode: str = ""
    motorway: int = 0
    supermarket: int = 0
    lat: float = 0.0
    long: float = 0.0
    e5: float = 0.0
    e10: float = 0.0
    b7s: float = 0.0
    b7p: float = 0.0
    open1: str = ""
    close1: str = ""
    open7: str = ""
    close7: str = ""
    carWash: int = 0
    toilets: int = 0
    
def getLatestFile():
    """Get the latest fuel price file."""
    
    # Get extra code
    import os
    
    # Local variables
    directory = "../CSV"
    latestFile = ""
    latestTime = 0
    
    # iterate over the files in the directory using os.scandir
    for entry in os.scandir(directory):
        
        # Check if item is a valid file
        if entry.is_file() and entry.name[0:16] == "UpdatedFuelPrice":
            
            # Get the name of the file
            filename = entry.name
            
            # Check if current file is newer
            if filename[17:30] > latestFile[17:30]:
                
                # Update the anme of latest file
                latestFile = filename
    
    return latestFile
    

def pence(price):
    """Checks price is in pounds, and convert if not."""
    
    # Local variable
    cost = 0.0

    # E5 fuel price
    if price != "":
        
        # convert to real value
        cost = float(price)
        
        # Cost recorded in pounds?
        if cost < 10:
            
            # Convert pounds to pence
            cost = cost * 100

        # Cost over £10
        if cost >= 500:
            
            # Ignore
            cost = 0.0
        
    return round(cost, 1)


def boolean(value):
    """Converts text to Boolean."""
    
    # Local variable
    result = 0
    
    if value.lower() == "true":
        
        result = 1
    
    return result

def getName(name):
    """Remove problem characters, such as \".  Capitalise all names."""
    
    # Local variables
    newName = ""
    ascii = 0
    
    # Loop for each character
    for index in range(len(name)):
        
        # Get ASCII value
        ascii = ord(name[index])
        
        # Check valid
        if (ascii == 32 or ascii == 38) or (ascii >= 48 and ascii <= 57) or (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
            
            # Lower case?
            if ascii >= 97:
                
                # Change to upper case
                ascii = ascii - 32
            
            # Create name
            newName = newName + chr(ascii)
    
    # Check if name is blank
    if newName == "":
        
        newName = "No name supplied"
            
    return newName


def readData():
    """Read data from file.  Many addresses entered incorrectly with commas, so negative indexing used after 11."""
    
    # Initialise local variables
    filename = ""
    line = ""
    temp = []
    
    motorway = 0  # 4
    supermarket = 0  # 5
    latitude = 0.0  # 16
    longitude = 0.0  # 17
    e5 = 0.0  # 18
    e10 = 0.0  # 21
    b7s = 0.0  # 24
    b7p = 0.0  # 27
    carWash = 0  # 63
    toilets = 0  # 67
    
    stations = []
    
    # Choose file to use
    filename = "..\csv\\" + getLatestFile()
    
    # Connect to the raw data
    file = open(filename, "r")
    
    # Read and discard headers
    line = file.readline()
    
    # Read first line of data
    line = file.readline()
    
    # Repeat until no further data is read
    while line != "":
                
        # Split the data
        temp = line.split(",")
        
        # Only process open stations
        if not(temp[7].lower() == "true" or temp[8].lower() == "true"): 
        
            # Create temp record
            tempStation = Station()

            # Get type
            motorway = boolean(temp[4])
            supermarket = boolean(temp[5])
            
            
            # Get location
            latitude = float(temp[-52])  # 16
            longitude = float(temp[-51])  # 17
            
            # Check Lat and Long correct way round
            if abs(latitude) < abs((longitude)):
                latitude = longitude
                longitude = float(temp[-52])  # 16
                
            # Check longitude not east of Ness Point
            if longitude > 1.7628:
                
                longitude = -longitude
            
            
            # Get fuel prices
            # E5 fuel price
            e5 = pence(temp[-50])  # 18
            
            # E10 fuel price
            e10 = pence(temp[-47])  # 21
            
            # B7S fuel price
            b7s = pence(temp[-44])  # 24
            
            # B7P fuel price
            b7p = pence(temp[-41])  # 27
            
            
            # Get amenities
            # Car wash
            carWash = boolean(temp[-5])  # 63
            
            # Customer toilets
            toilets = boolean(temp[-1].strip())  # 67
            
            
            # Update temp record
            tempStation.name = getName(temp[3])
            tempStation.postcode = temp[10]
                        
            tempStation.motorway = motorway
            tempStation.supermarket = supermarket
                                  
            tempStation.lat = abs(latitude)  # Ensure positive
            tempStation.long = longitude

            tempStation.e5 = e5
            tempStation.e10 = e10
            tempStation.b7s = b7s
            tempStation.b7p = b7p
            
            tempStation.open1 = temp[-32]  # 36
            tempStation.close1 = temp[-31]  # 37
            
            tempStation.open7 = temp[-14]  # 54
            tempStation.close7 = temp[-13]  # 55
            
            tempStation.carWash = carWash
            tempStation.toilets = toilets
            
            
            # Add current station to array of records
            stations = stations + [tempStation]
        
        # Read next line of data
        line = file.readline()
        
    # Close the connection to the file
    file.close()
        
    # Return array of records
    return stations


def writeCSV(stations):
    """Write fuel prices to CSV file."""
    
    # Create a connection to the file
    file = open("../CSV/FuelPrice.csv", "w")
    
    
    # Headers
    file.write("name,postcode,motorway,supermarket,latitude,longitude,e5,e10,b7s,b7p,open,close,openSun,closeSun,car wash, toilets\n")
    
    # Loop for each station
    for station in stations:
        
        file.write(station.name             + ",")
        file.write(station.postcode         + ",")
        file.write(str(station.motorway)    + ",")
        file.write(str(station.supermarket) + ",")
        file.write(str(station.lat)         + ",")
        file.write(str(station.long)        + ",")
        
        if station.e5 != 0:
            file.write(str(station.e5)      + ",")
        else:
            file.write("NULL"               + ",")
        
        if station.e10 != 0:
            file.write(str(station.e10)     + ",")
        else:
            file.write("NULL"               + ",")
            
        if station.b7s != 0:
            file.write(str(station.b7s)     + ",")
        else:
            file.write("NULL"               + ",")
            
        if station.b7p != 0:
            file.write(str(station.b7p)     + ",")
        else:
            file.write("NULL"               + ",")
        
        file.write(station.open1            + ",")
        file.write(station.close1           + ",")
        file.write(station.open7            + ",")
        file.write(station.close7           + ",")
        file.write(str(station.carWash)     + ",")
        file.write(str(station.toilets)     + "\n")
    
    # Close the connection to the file
    file.close()


def main():
    """Main program."""

    # Initialise variables
    stations = [] 

    # 1 - Get stations
    stations = readData()

    # 2 - Write stations data
    writeCSV(stations)


# Call main()
main()
