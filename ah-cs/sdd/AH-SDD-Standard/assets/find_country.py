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
        
    # Close connection to file
    file.close()
        
    # Return parallel arrays
    return countries, capitals, areas, populations


def find_country(countries: list[str], country: str) -> int:
    """Binary search to find a country in an array."""
    """Returns the index position."""
    
    # Initialise local variables
    start: int = 0
    end: int = len(countries) - 1
    middle: int = 0
    found: bool = False
    
    # Loop until found, or all elements checked
    while not found and (start <= end):

        # Calculate mid point of array to be searched
        middle = int((start + end) / 2)

        # Check if found
        if countries[middle] == country:

            # Update result
            found = True

        # Check if target value is greater than current value
        elif countries[middle] > country:

            # Update end of array to be searched
            end = middle - 1

        else:

            # Update start of array to be searched
            start = middle + 1
    
    # Return index position
    if found:
        
        return middle
    
    else:
        
        return -1


def display_country(capitals: list[str], areas: list[float],
                    populations: list[int], index: int) -> None:
    """Display the information about the country on the screen."""
    
    # Display header
    print('\nResult')
    print('------\n')
    
    # Display information
    print(f'Capital: {capitals[index]}')
    print(f'Area: {areas[index]:} km^2')
    print(f'Population: {populations[index]}')
    
    # Display footer
    print('\n=======')
    

def write_summary(countries: list[str], capitals: list[str],
                  areas: list[float], populations: list[int],
                  index: int) -> None:
    """Write the information about the country to a text file."""
    
    # Connect to file
    file = open('country.txt', 'w', encoding='utf-8')
    
    # Write header
    file.write('Country Details\n')
    file.write('---------------\n\n')
    
    # Write information
    file.write(f'Country: {countries[index]}\n')
    file.write(f'Capital: {capitals[index]}\n')
    file.write(f'Area: {areas[index]:} km^2\n')
    file.write(f'Population: {populations[index]}\n')
    
    # Write footer
    file.write('\n===============')


def main() -> None:
    
    # Initialise variables
    countries: list[str] = ["" for _ in range(47)]
    capitals: list[str] = ["" for _ in range(47)]
    areas: list[float] = [0.0 for _ in range(47)]
    populations: list[int] = [0 for _ in range(47)]
    country: str = ""
    index: int = 0
    
    # Read data from csv file
    countries, capitals, areas, populations = read_data()
    
    # Display header
    print('Find a Country')
    print('--------------\n')
    
    # Get country from user
    country = input('Which country? ')
    
    # Get index position of country
    index = find_country(countries, country)
    
    # Display country information
    display_country(capitals, areas, populations, index)
    
    # Write country information to text file.
    write_summary(countries, capitals, areas, populations, index)
                  
# Run program
if __name__ == "__main__":

    main()