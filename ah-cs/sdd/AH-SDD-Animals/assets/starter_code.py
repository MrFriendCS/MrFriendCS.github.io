# Title: AH SDD Barra Zoo - Starter Code
# Author: 
# Date: 

# Get extra code
import sqlite3

# Import classes
from animal import Animal
from animals import Animals


def create_database() -> None:
    """Create the zoo database, if it doesn't exist."""
    
    # Variables
    query: str = ''
    global database
    
    # Create a connection to the database
    # Create a new database file, if it doesn't exist
    connection = sqlite3.connect(database)

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
    """Read the animals data into Animal objects
       in an Animals object.
       """


def add_record(name: str='', age: int=0, weight: float=0.0) -> None:
    """Change the record of a dead animal."""
    

def update_record(name: str='', die: bool=True) -> None:
    """Update a record in the Animal table.
       Either increase the age, or change the alive status.
       """


def display_menu() -> None:
    """Display the Barra Zoo menu."""
    
    # Header
    print('\nBarra Zoo')
    print('---------')
    print('\nMenu:\n')
    
    # Options
    print('\t1 Display all animals')
    print('\t2 Add a new animal')
    print('\t3 Celebrate a birthday')
    print('\t4 Report a death')
    print('\t5 Display oldest animal')
    print('\t6 Display 10 oldest animals')
    
    # Option
    print('\tx Exit\n')


def display_all_animals(animals) -> None:
    """Display the details of all the animals."""


def add_new_animal(animals) -> None:
    """Add a new animal to the database and collection.
       Only animals that are alive can be added.
       """


def celebrate_a_birthday(animals) -> None:
    """Celbrate the birthday of an animal."""


def register_a_death(animals) -> None:
    """Register the death of an animal."""


def display_oldest(animals: Animals) -> None:
    '''Display details of oldest animal.'''


def display_10_oldest(animals) -> None:
    """Display the details of the 10 oldest animals."""


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
        if option == '1':
            
            # Display all animals
            display_all_animals(animals)
        
        # Select option
        elif option == '2':
            
            # Add a new animal
            add_new_animal(animals)
        
        # Select option
        elif option == '3':
            
            # Celebrate a birthday
            celebrate_a_birthday(animals)
        
        # Select option
        elif option == '4':
            
            # Register a death
            register_a_death(animals)
        
        # Select option
        elif option == '5':
            
            # Display oldest animal
            display_oldest(animals)
        
        # Select option
        elif option == '6':
            
            # Display 10 oldest animals
            display_10_oldest(animals)
            
        elif option == 'x':
        
            # Stop running code
            run = False


# Global variable
database = 'barra_zoo.db'


# Only run code if run directly
if __name__ == '__main__': main()
