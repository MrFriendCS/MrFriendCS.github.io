# Title: AH SDD Barra Zoo
# Author: Mr Friend
# Date: 19 Jun 2026


# Import classes
from animal import Animal
from animals import Animals

# Get extra code
import sqlite3


def create_database() -> None:
    """Create the zoo database if it doesn't exist,
       and populate with some test data.
       """
    
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
    
    
def add_example_data() -> None:
    """Adds example data to the Animal table."""
    
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

    # Insert data
    cursor.execute(query)

    # Commit the data
    connection.commit()

    # Close the connection to the database
    connection.close()


def display_menu() -> None:
    """Display the Barra Zoo menu."""
    
    # Header
    print('Barra Zoo')
    print('---------')
    
    
    
    
def main() -> None:
    """Main Barra Zoo code."""
    
    # Create database - if needed
    create_database()
    
    # Display menu
    display_menu()
    
    
    

# Only run code if run directly
if __name__ == "__main__": main()
