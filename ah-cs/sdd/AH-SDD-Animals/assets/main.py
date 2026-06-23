# Title: AH SDD Barra Zoo
# Author: Mr Friend
# Date: 22 Jun 2026

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
    """Read the animals into an array of objects."""
    
    # Variables
    animals = Animals()
    name: str = ''
    age: int = 0
    weight: float = 0.0
    alive: bool = True
    global database
    
    # Create a connection to the database
    # Create a new database file, if it doesn't exist
    connection = sqlite3.connect(database)

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
        
        if row[4] == 0:
            alive = False
        else:
            alive = True

        # Add animal to the collection
        animals.add_animal(Animal(name, age, weight, alive))

    # Close the connection to the database
    connection.close()
    
    return animals


def add_record(name: str='', age: int=0, weight: float=0.0) -> None:
    """Change the record of a dead animal."""
    
    # Variables
    query: str = ''
    global database
    
    # Create a connection to the database
    # Create a new database file, if it doesn't exist
    connection = sqlite3.connect(database)

    # Create a database cursor
    cursor = connection.cursor()

    # Create query - Table  
    query = f"""INSERT INTO Animal (name, age, weight, alive)
    VALUES ('{name}', {age}, {weight}, True);
    """
    
    try:
    
        # Insert new data
        cursor.execute(query)

        # Commit the new data
        connection.commit()
        
        print('Record added to Animal table.')
    
    except:
        
        print('Record not added to Animal table.')
        
    # Close the connection to the database
    connection.close()
    

def update_record(name: str='', die: bool=True) -> None:
    """Update a record in the Animal table.
       Either increase the age, or change the alive status.
       """
    
    # Variables
    query: str = ''
    global database


    if die:
        
        # Create query - Table  
        query = f"""UPDATE Animal
        SET age = age + 1
        WHERE name = '{name}';
        """
    
    else:
        
        # Create query - Table  
        query = f"""UPDATE Animal
        SET alive = False
        WHERE name = '{name}';
        """
    
    # Create a connection to the database
    connection = sqlite3.connect(database)

    # Create a database cursor
    cursor = connection.cursor()
    
    try:
    
        # Insert new data
        cursor.execute(query)

        # Commit the new data
        connection.commit()
        
        print('Record modified in Animal table.')
    
    except:
        
        print('Record not modified in Animal table.')
        
    # Close the connection to the database
    connection.close()


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
    
    # Options
    print('\n\te Add three example animals')
    print('\tx Exit\n')


def display_all_animals(animals) -> None:
    """Display the details of all the animals."""
    
    # Local variables
    name: str = ''
    age: int = 0
    weight: float = 0.0
    alive: bool = True
    array_of_animals: list = []
    
    # Get animal data
    array_of_animals = animals.get_animals()
        
    # Display Header
    print('\nAll Animals')
    print('------------')
    
    # Loop for each animal
    for index in range(len(array_of_animals)):
        
        # Get details
        name = array_of_animals[index].get_name()
        age = array_of_animals[index].get_age()
        weight = array_of_animals[index].get_weight()
        alive = array_of_animals[index].get_alive()
        
        # Display details        
        print(f'\nAnimal No {index+1}')
        
        print(f'\tName: {name}')
        print(f'\tAge: {age}')
        print(f'\tWeight {weight} kg')
        print(f'\tAlive: {alive}')


def add_new_animal(animals) -> None:
    """Add a new animal to the database and collection.
       Only animals that are alive can be added.
       """
    
    # Local variables
    name: str = ''
    age: int = 0
    weight: float = 0.0
        
    # Display Header
    print('\nAdd a New Animal')
    print('----------------\n')
    
    # Get animal name
    name = input('Name? ')
    
    # Get animal weight
    age = int(input('Age? '))
    
    # Get animal name
    weight = float(input('Weight? '))
    
    # Add animal to collection
    animals.add_animal(Animal(name, age, weight))
    
    # Add animal to database
    add_record(name, age, weight)


def celebrate_a_birthday(animals) -> None:
    """Celbrate the birthday of an animal."""
    
    # Local variables
    name: str = ''
    array_of_animals: list = []
    index: int = 0
    found = False
        
    # Display Header
    print('\nCelebrate a Birthday')
    print('--------------------\n')
    
    # Get name of animal that died
    name = input('Which animal has a birthday? ')
    
    # Get animal data
    array_of_animals = animals.get_animals()
    
    # Loop for each animal
    while not found and index < len(array_of_animals):
        
        # Check name
        if array_of_animals[index].get_name() == name:
            
            # Update details
            array_of_animals[index].birthday()
            found = True
            
            # Update database
            update_record(name, True)
            
        else:
            
            index += 1
           
    # Result
    if found:
        
        print(f'Happy birthday {name}!')
        
    else:
        
        print(f'No animal called {name} was found.')
    
    # Footer
    print('----------------\n')


def register_a_death(animals) -> None:
    """Register the death of an animal."""
    
    # Local variables
    name: str = ''
    array_of_animals: list = []
    index: int = 0
    found = False
        
    # Display Header
    print('\nRegister a Death')
    print('----------------\n')
    
    # Get name of animal that died
    name = input('Which animal died? ')
    
    # Get animal data
    array_of_animals = animals.get_animals()
    
    # Loop for each animal
    while not found and index < len(array_of_animals):
        
        # Check name
        if array_of_animals[index].get_name() == name:
            
            # Update details
            array_of_animals[index].die()
            found = True
            
            # Update database
            update_record(name, False)
            
        else:
            
            index += 1
           
    # Result
    if found:
        
        print(f'{name}\'s death has been registered.')
        
    else:
        
        print(f'No animal called {name} was found.')
    
    # Footer
    print('----------------\n')


def display_oldest(animals: Animals) -> None:
    """Display details of oldest animal."""
    
    # Local variables
    name: str = ''
    age: int = 0
    
    # Get data
    age, name = animals.find_oldest()
    
    print('\nOldest Animal')
    print('--------------')
    
    print(f'Name: {name}')
    print(f'Age: {age}')
    
    print('--------------\n')


def display_10_oldest(animals) -> None:
    """Display the details of the 10 oldest animals."""
    
    # Local variables
    name: str = ''
    age: int = 0
    array_of_animals: list = []
    index: int = 0
    count: int = 1
    
    # Order animals, oldest to youngest
    animals.order_by_age()
    
    # Get animal data
    array_of_animals = animals.get_animals()
        
    # Display Header
    print('\nTen Oldest Animals')
    print('-------------------')
    
    # Loop for each animal
    while index < 10 and index != len(array_of_animals):
        
        # Only display animals that are alive
        if array_of_animals[index].get_alive():
        
            # Get details
            name = array_of_animals[index].get_name()
            age = array_of_animals[index].get_age()
            
            # Display details        
            print(f'\nAnimal No {count}')
            
            print(f'\tName: {name}')
            print(f'\tAge: {age}')
            
            # Increment number of animals displayed
            count += 1
        
        # Increment index
        index += 1


def add_example_data() -> None:
    """Add example data to the Animal table."""
    
    # Variables
    query: str = ''
    global database
    
    # Create a connection to the database
    connection = sqlite3.connect(database)

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
            
        elif option == 'e':
            
            # Add example animals
            add_example_data()
            
        elif option == 'x':
        
            # Stop running code
            run = False

# Global variable
database = 'barra_zoo.db'


# Only run code if run directly
if __name__ == '__main__': main()
