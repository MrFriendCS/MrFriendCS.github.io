# Title: Gary's Garage
# Author: Mr Friend
# Date: 6 Oct 2024

"""
Create the data and export as SQL statements to build tables.
"""

# Import Extra Code
import sys
import random
from dataclasses import dataclass


# Find DDDhelper file
shool = "C:\\Users\\afriend1r\\AppData\\Local\\Programs\\Thonny"

start1 = "C:\\Users\\afriend1r"
start2 = "D:"

end = "\\OneDrive - Glow Scotland\\GitHub\\MrFriendCS.github.io"

# Check if directory exists
if shool in sys.path:
    # School laptop
    sys.path.append(start1 + end)
    
else:
    # Personel laptop
    sys.path.append(start2 + end)

# Get extra code
import DDDhelper


def getVehicleData(count):
    """Create the data for the vehicle entity."""
    
    
    @dataclass
    class Vehicle:
        """A record to represent a vehicle."""
        
        vrn: str = ""  # PK
        make: str = ""
        model: str = ""
        colour: str = ""


    vehicles = [Vehicle() for index in range(count)]
    
    # Loop for each vehicle
    for index in range(count):
        
        # Pick VRN       
        vehicles[index].vrn = DDDhelper.getVRN()
                
        # Pick make and model
        vehicles[index].make = DDDhelper.getMake()
        
        # Pick model
        vehicles[index].model = DDDhelper.getModel(vehicles[index].make)
        
        # Pick colour
        vehicles[index].colour = DDDhelper.getColour()
        
    return vehicles


def getMOTdata(vehicles, count):
    """Create the data for the MOT entity."""
    
    
    @dataclass
    class MOT:
        """A record to represent a MOT."""
        
        no: int = 0    # PK
        vrn: str = ""  # FK
        date: str = ""
        result: bool = True
        cost: float = 0.0
    

    mots = [MOT() for index in range(count)]
    
    # Loop for each MOT
    for index in range(count):
        
        # MOT number
        mots[index].no = index + 1
        
        # MOT vehicle registration
        mots[index].vrn = random.choice(vehicles).vrn
        
        # MOT date        
        mots[index].date = DDDhelper.getDate(2000, 2020)
               
        # MOT pass / fail
        mots[index].result = DDDhelper.getTrue(72)
            
        # MOT costs        
        mots[index].cost = round(int(mots[index].date[:4]) - 2000 + 35.99, 2)
            
    return mots


def getFails(mots):
    """Count number of failures."""
    
    # Initialise local variable
    count = 0
    
    # Loop for each MOT
    for mot in mots:
        
        # Check if a failure
        if not mot.result:
            
            # Increment count
            count = count + 1
            
    return count


def getRepairData(mots, count):
    """Create the data for the repair entity."""
    
    
    @dataclass
    class Repair:
        """A record to represent a repair."""
        
        no: int = 0    # PK
        vrn: str = ""  # FK
        date: str = ""
        cost: float = 0.0


    # Initialise local variables
    repairs = [Repair() for index in range(count)]
    

    day = 0
    dayStr = ""
    
    counter = 0
    
    for index in range(len(mots)):
        
        if not mots[index].result:
            repairs[counter].no = counter + 1
            repairs[counter].vrn = mots[index].vrn
            
            day = int(mots[index].date[-2: ])
            
            if day < 10:
                dayStr = "0" + str(day)
            else:
                dayStr = str(day)
            
            repairs[counter].date = mots[index].date[0:-2] + dayStr
            repairs[counter].cost = random.randint(45, 525) + 0.99
            
            counter = counter + 1
            
    return repairs
    


def writeVehicleTable(vehicles):
    """Create vehicle.sql file with definition and data."""
    
    file = open("vehicle.sql", "w")
    
    # SQL - Create table
    
    table = """CREATE TABLE vehicle (
    veh_reg VARCHAR(8),
    make VARCHAR(20),
    model VARCHAR(20),
    colour VARCHAR(20),
    PRIMARY KEY (veh_reg)
);"""
    
    file.write(table + "\n\n")
    
    # SQL - Create values
    
    # Loop for each vehicle
    for vehicle in vehicles:
        file.write("INSERT INTO vehicle VALUES (")
        file.write("\"" + vehicle.vrn + "\",")
        file.write("\"" + vehicle.make + "\",")
        file.write("\"" + vehicle.model + "\",")
        file.write("\"" + vehicle.colour + "\");\n")
        
    file.close()
        

def writeMOTtable(mots):
    """Create mot.sql file with definition and data."""

    file = open("mot.sql", "w")
    
    # SQL - Create table
    
    table = """CREATE TABLE mot (
    mot_no INT NOT NULL,
    veh_reg VARCHAR(8),
    date DATE,
    pass BOOL,
    cost REAL,
    FOREIGN KEY (veh_reg)  
        REFERENCES vehicle(veh_reg),
    PRIMARY KEY (mot_no)
);"""
    
    file.write(table + "\n\n")
    
    # SQL - Create values
    
    # Loop for each mot test
    for mot in mots:
        file.write("INSERT INTO mot VALUES (")
        file.write(    str(mot.no) + ",")
        file.write( "\"" + mot.vrn + "\",")
        file.write( "\"" + mot.date + "\",")
        file.write(str(int(mot.result)) + ",")
        file.write(    str(mot.cost) + ");\n")
        
    file.close()


def writeRepairTable(repairs):
    """Create repair.sql file with definition and data."""
    
    file = open("repair.sql", "w")
    
    # SQL - Create table
    
    table = """CREATE TABLE repair (
    mot_no INT NOT NULL,
    veh_reg VARCHAR(8) NOT NULL,
    date DATE,
    cost REAL,
    FOREIGN KEY (veh_reg)
        REFERENCES vehicle(veh_reg),
    PRIMARY KEY (mot_no)
);"""
    
    file.write(table + "\n\n")
      
    
    # SQL - Create values
    
    # Loop for each mot test
    for repair in repairs:
        file.write("INSERT INTO repair VALUES (")
        file.write(   str(repair.no) + ",")
        file.write("\"" + repair.vrn + "\",")
        file.write("\"" + repair.date + "\",")
        file.write(   str(repair.cost) + ");\n")
        
    file.close()


def main():
    """Main program."""

    # Initialise variables
    noOfVehs = 200
    noOfMOTS = 1000
    fails = 0

    # 1 - Get vehicle entity data
    vehicles = getVehicleData(noOfVehs)

    # 2 - Get MOT entity data
    mots =  getMOTdata(vehicles, noOfMOTS)

    # 3 - Count failures
    fails = getFails(mots)

    # 4 - Get repair entity data
    repairs = getRepairData(mots, fails)

    # 5 - Write vehicle table
    writeVehicleTable(vehicles)

    # 6 - Write MOT table
    writeMOTtable(mots)

    # 7 - Write repair table
    writeRepairTable(repairs)


# Call main()
main()
