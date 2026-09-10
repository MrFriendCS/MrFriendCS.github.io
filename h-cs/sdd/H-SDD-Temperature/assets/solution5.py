# Title: H SDD - Temperature Dates
# Author: Mr Friend
# Date: 10 Sep 2026

# Get extra code
from dataclasses import dataclass


@dataclass
class HourlyValue:
    """A record to hold temperature data."""
    
    # Fields
    date: str = ""
    time: str = ""
    temp: float = 0.0


def f2c(tempF: float) -> float:
    """Converts fahrenheit value to celsius.  Rounds to 1 dp."""

    # Declare local variable
    tempC: float = 0.0

    # Convert
    tempC = (tempF - 32) * 5 / 9

    # Round
    tempC = round(tempC, 1)

    # Return celsius value
    return tempC


def us2iso(dateUS: str) -> str:
    """Converts US date (mm-dd-yyyy) to ISO date (yyyy-mm-dd)."""

    # Declare local variables
    dateISO: str = ""
    dd: str = ""
    mm: str = ""
    yyyy: str = ""

    # Extract values
    dd = dateUS[3:5]
    mm = dateUS[0:2]
    yyyy = dateUS[-4: ]

    # Combine values
    dateISO = yyyy + "-" + mm + "-" + dd

    # Return ISO format date
    return dateISO


def readData() -> list[HourlyValue]:
    """Read data from file and assign to parallel arrays."""

    # Declare local variables
    line: str = ""
    data: list[str] = ["" for _ in range(3)]
    values: list[HourlyValue] = [HourlyValue() for _ in range(8759)]

    # Open connection to the file
    file = open("dataUS.csv", "r", encoding="UTF-8")

    # Read each row of data
    for index in range(len(values)):

        # Read line of data
        line = file.readline()

        # Split line at commas
        data = line.split(",")

        # Assign data to parallel arrays
        values[index].date = data[0].strip()
        values[index].time = data[1].strip()
        values[index].temp = float(data[2].strip())

    # Close connection to the file
    file.close()

    # Return array of records
    return values


def convertData(values: list[HourlyValue]) -> list[HourlyValue]:
    """Convert data in array of records:
           fahrenheit temperatures to celsius
           US dates to ISO dates"""

    # Loop for each value
    for index in range(len(values)):
        
        # 2.1 Convert date
        values[index].date = us2iso(values[index].date)
        
        # 2.2 Convert temperature
        values[index].temp = f2c(values[index].temp)

    # Return array of records
    return values


def writeData(values: list[HourlyValue]) -> None:
    """Write data to file from arrays of records."""

    # Create file
    file = open("dataISO.csv", "w", encoding="UTF-8")
    
    # Loop for each value
    for index in range(len(values)):

        # Write a line of data
        file.write(values[index].date + ",")
        file.write(values[index].time + ",")
        file.write(str(values[index].temp) + "\n")

    # Close connection to the file
    file.close()

    
def main():
    """Main program."""
    
    # Declare global variable
    data: list[HourlyValue] = [HourlyValue() for _ in range(8759)]

    # 1. Read the data from a csv file
    data = readData()

    # 2. Convert the dates and temperatures
    data = convertData(data)

    # 3. Write the data to a csv file
    writeData(data)


# Call main()
main()
