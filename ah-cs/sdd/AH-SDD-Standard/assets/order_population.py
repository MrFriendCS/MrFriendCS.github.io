# Title: AH SDD Order by Population
# author: Mr Friend
# Date: 23 Sep 2026


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
        
    # Close connection to file
    file.close()
        
    # Return parallel arrays
    return countries, capitals, areas, populations


def order_population(countries: list[str], capitals: list[str],
                     areas: list[float], populations: list[int]) \
                     -> tuple[list[str], list[str], \
                              list[float], list[int]]:
    """Bubble sort to order aparllel arrays, descending population."""
    """Returns parallel arrays."""
    
    # Initialise local variables
    tempCountry: str = ""
    tempCapital: str = ""
    tempArea: float = 0.0
    tempPopulation: int = 0
    n: int = 0
    sort: bool = True
    
    # Get number of elements
    n = len(countries)
    
    # Sort if needed
    while sort == True:
    
        # Turn sort off
        sort = False
    
        # Loop from start of array
        for index in range(n - 1):
    
            # Compare current element with next element
            if populations[index] < populations[index + 1]:
    
                # Swap countries
                tempCountry = countries[index]
                countries[index]  = countries[index + 1]
                countries[index + 1] = tempCountry
    
                # Swap capitals
                tempCapital = capitals[index]
                capitals[index]  = capitals[index + 1]
                capitals[index + 1] = tempCapital
    
                # Swap areas
                tempArea = areas[index]
                areas[index]  = areas[index + 1]
                areas[index + 1] = tempArea
    
                # Swap populations
                tempPopulation = populations[index]
                populations[index]  = populations[index + 1]
                populations[index + 1] = tempPopulation
    
                # Sorting still needed
                sort = True
    
        # Reduce the number elements to be checked
        n = n - 1
    
    # Return sorted parallel arrays
    return countries, capitals, areas, populations
    


def display_top_5(countries: list[str], populations: list[int]) -> None:
    """Display the information about the country on the screen."""
    
    # Display header
    print('\nTop 5 by Population')
    print('-------------------\n')
    
    for index in range(5):
        
        # Display count
        print(f'{index + 1}.')
        
        # Display information
        print(f'  Country: {countries[index]}')
        print(f'  Population: {populations[index]}\n')
            
    # Display footer
    print('=======')
    

def write_top_10(countries: list[str], capitals: list[str],
                areas: list[float], populations: list[int]) -> None:
    """Write the information about the country to a text file."""
    
    # Connect to file
    file = open('top_populations.csv', 'w', encoding='utf-8')
    
    # Write column headers
    file.write('country,capital,area,population\n')
    
    for index in range(10):
        
        # Write information
        file.write(f'{countries[index]},')
        file.write(f'{capitals[index]},')
        file.write(f'{areas[index]:},')
        file.write(f'{populations[index]}\n')


def main() -> None:
    
    # Initialise variables
    countries: list[str] = ["" for _ in range(47)]
    capitals: list[str] = ["" for _ in range(47)]
    areas: list[float] = [0.0 for _ in range(47)]
    populations: list[int] = [0 for _ in range(47)]
    
    # Read data from csv file
    countries, capitals, areas, populations = read_data()
     
    # Order by population, descending
    countries, capitals, areas, populations \
        = order_population(countries, capitals, areas, populations)
    
    # Display information about top 5 populous countries
    display_top_5(countries, populations)
    
    # Write data of top 10 populous countries to csv file
    write_top_10(countries, capitals, areas, populations)


# Run program
if __name__ == "__main__":

    main()