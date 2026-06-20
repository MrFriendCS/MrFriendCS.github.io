# Title: AH SDD Barra Zoo
# Author: Mr Friend
# Date: 19 Jun 2026


# Import classes
from animal import Animal
from animals import Animals

# Get extra code
import sqlite3


def create_database() -> None:
    """Create the zoo database if it doesn't exist."""
    
    # Local variables
    query: str = ''
    
    # Create a connection to the database
    # Create a new database file, if it doesn't exist
    connection = sqlite3.connect('barra_zoo.db')

    # Create a database cursor
    cursor = connection.cursor()

    # Create query - Table  
    query = """CREATE TABLE IF NOT EXISTS Animal (
    animal_id INTEGER NOT NULL,
    name VARCHAR(30) UNIQUE NOT NULL,
    age INTEGER NOT NULL CHECK (age >= 0),
    weight REAL NOT NULL CHECK (weight >= 0.0),
    alive BOOLEAN NOT NULL,
    PRIMARY KEY (animal_id AUTOINCREMENT)
    );"""
    
    # Create the table
    cursor.execute(query)

    # Close the connection to the database
    connection.close()


def read_data() -> Animals:
    """Read the animals into an array of objects."""
    
    # Local variables
    animals = Animals()
    name: str = ''
    age: int = 0
    weight: float = 0.0
    alive: bool = True
    
    # Create a connection to the database
    # Create a new database file, if it doesn't exist
    connection = sqlite3.connect('barra_zoo.db')

    # Create a database cursor
    cursor = connection.cursor()

    # Create query - Table  
    query = """SELECT *
    FROM Animal;
    """
    
    # Run query and store result
    result = cursor.execute(query)

    # Loop for each animal
    for row in result:
        
        # Get data
        name = row[1]
        age = row[2]
        weight = row[3]
        alive = row[4]

        # Add animal to the collection
        animals.add_animal(Animal(name, age, weight, alive))

    # Close the connection to the database
    connection.close()
    
    return animals
    
    
def add_example_data() -> None:
    """Add example data to the Animal table."""
    
    # Local variables
    query: str = ''
    
    # Create a connection to the database
    connection = sqlite3.connect('barra_zoo.db')

    # Create a database cursor
    cursor = connection.cursor()
  
    # Create query - Insert
    query = '''
    INSERT INTO Animal (name, age, weight, alive)
        VALUES
            ("Bonzo", 17, 15.4,TRUE),
            ("Goldie", 2, 0.1, TRUE),
            ("Kitty", 3, 2.7, TRUE);
    '''

    try:
        # Insert data
        cursor.execute(query)
        
        # Commit the data
        connection.commit()
    
        # Success message
        print('\nThree animals added to database.')
        
    except:
    
        # Failure message
        print('\nNo animals were added to database.')

    # Close the connection to the database
    connection.close()


def display_oldest(animals: Animals) -> None:
    '''Display details of oldest animal.'''
    
    # Local variables
    name: str = ''
    age: int = ''
    
    # Get data
    age, name = animals.find_oldest()
    
    print('\nOldest Animal')
    print('--------------')
    
    print(f'Name: {name}')
    print(f'Age: {age}')
    
    print('--------------\n')


def display_menu() -> None:
    """Display the Barra Zoo menu."""
    
    # Header
    print('\nBarra Zoo')
    print('---------')
    print('\nMenu:\n')
    
    # Options
    print('\t1 Display all animals')
    print('\t2 Add a new animal')
    print('\t3 Report a death')
    print('\t4 Display oldest animal')
    print('\t5 Display 10 oldest animals')
    
    # Options
    print('\n\te Add three example animals')
    print('\tx Exit\n')


def main() -> None:
    """Main Barra Zoo code."""
    
    # Local variables
    option: str = ''
    run: bool = True
    
    # Create database - if needed
    create_database()
    
    # Read animal data
    animals = read_data()
    
    # Loop
    while run:
    
        # Display menu
        display_menu()
        
        # Get option
        option = input('Enter choice: ')
        
        # Select option
        if option == 'e':
            
            # Add example animals
            add_example_data()
        
        elif option == '4':
            
            # Display oldest animal
            display_oldest(animals)
            
        elif option == 'x':
        
            # Stop running code
            run = False


# Only run code if run directly
if __name__ == '__main__': main()
