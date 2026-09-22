# Title: AH SDD Find a Country
# author: Mr Friend
# Date: 22 Sep 2026

def read_data() -> tuple[list[str], list[str], list[float], list[int]]:
    """Read data from csv file and return parallel arrays."""
    
    # Initialise local variables
    countries: list[str] = ["" for _ in range(47)]
    capitals: list[str] = ["" for _ in range(47)]
    areas: list[float] = [0.0 for _ in range(47)]
    populations: list[int] = [0 for _ in range(47)]
    data: list[str] = ["" for _ in range(4)]
    line: str = ""
    
    # Connect to file
    file = open('countries.csv', 'r', encoding='utf-8')
    
    # Read first line and discard headers
    file.readline()
    
    # Loop for each record
    for index in range(len(countries)):
        
        # Read line
        line = file.readline()
        
        # Seperate values
        data = line.split(',')
        
        # Assign values to parallel arrays
        countries[index] = data[0].strip()
        capitals[index] = data[1].strip()
        areas[index] = float(data[2].strip())
        populations[index] = int(data[3].strip())
        
    # Return parallel arrays
    return countries, capitals, areas, populations


def find_country(countries: list[str], country: str) -> int:
    pass


def display_country() -> None:
    pass


def write_summary() -> None:
    pass


def main() -> None:
    read_data()


# Run program
if __name__ == "__main__":

    main()