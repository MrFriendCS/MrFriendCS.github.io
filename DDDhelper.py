# Title: DDD Helper
# Author: Mr Friend
# Date: 18 Dec 2025

"""Functions to help create data for N5 and Higher DDD tasks.""" 

"""
getForename()
getSurname()
getPhone(percentMobile=50)
getDate(min=2024, max=2024)
getEmail(forename="", surname="", percentNull=0)
getNights(min=1, max=10)
getPrice(min=1, max=10, pence=True)
getTrue(percentTrue=50)
getNumber(min=0, max=100)
getVRN()
getMake()
getModel(make="")
getColour()
getGift()
getHair()
getEye()
getSchoolYear(primary=False)
getGrade()
"""

# Get extra code
import random


def getForename() -> str:
    """Pick a random forename."""
    
    forenames = ["Adam", "Aiden", "Aimee", "Alan", "Alanna", "Alexander",
                 "Alison", "Alistair", "Amy", "Andrew", "Angela", "Angus",
                 "Anne", "Anthony", "Aonghas", "Ava", "Barbara", "Brian",
                 "Caitlin", "Callum", "Calum", "Caralisa", "Carol", "Catherine",
                 "Charles", "Charlie", "Charlotte", "Christ", "Christine", "Ciara",
                 "Claire", "Colin", "Copper", "Craig", "Danieal", "Daniel",
                 "Danielle", "Darren", "David", "Derek", "Domhnall", "Dominic",
                 "Donald", "Douglas", "Ealasaid", "Eilidh", "Elaine", "Elizabeth",
                 "Ella", "Emily", "Emma", "Erin", "Ethan", "Fay", "Finlay",
                 "Fiona", "Gary", "George", "Gillian", "Gordon", "Graham",
                 "Hannah", "Heather", "Helen", "Holly", "Hudson", "Hugh", "Iain",
                 "Iain Ruairidh", "Ian", "India", "Innes", "Isabella", "James",
                 "Jamie", "Jane", "Janet", "Jason", "Jean", "Jennifer", "Joan",
                 "John", "JosephJulia", "Julie", "Karen", "Katie", "Keith", "Kevin",
                 "Kieran", "Lacey", "Laura", "Lewis", "Liam", "Lily", "Lincoln",
                 "Linda", "Lisa", "Lorna", "Louise", "Lynn", "Maddison", "Mairead",
                 "Mairi", "Margaret", "Maria", "Mark", "Martin", "Mary", "Mason",
                 "Matthew", "Maureen", "Michael", "Micheal", "Michelle", "Mirren",
                 "Miyah", "Neil", "Niamh", "Nicola", "Oliver", "Olivia", "Owen",
                 "Pamela", "Patricia", "Patrick", "Paul", "Peter", "Philip",
                 "Rachel", "Richard", "Robbie", "Robert", "Roderick", "Ross",
                 "Rowan", "Ruairidh", "Ryan", "Sam", "Sandra", "Sarah", "Scott",
                 "Seonaidh", "Seumas", "Sharon", "Shelly", "Simon", "Sophia",
                 "Sophie", "Stephen", "Steven", "Stewart", "Stuart", "Summer",
                 "Susan", "Thomas", "Vincent", "Wendy", "William", "Zoey"]
    
    forename = random.choice(forenames)
    
    return forename


def getSurname() -> str:
    """Pick a random surname."""
    
    surnames = ["Allan", "Anderson", "Austin", "Baker", "Barton", "Beaton",
                 "Bell", "Berry", "Black", "Blackie", "Blake", "Boyd", "Brown",
                 "Burgess", "Cameron", "Campbell", "Clark", "Coleman", "Cooper",
                 "Daly", "Davidson", "Davies", "Docherty", "Duncan", "Edwards",
                 "Evans", "Ferguson", "Fraser", "Friend", "Frost", "Galbraith",
                 "Gibson", "Gillies", "Goodwin", "Graham", "Grant", "Gray",
                 "Green", "Griffin", "Hamilton", "Hardy", "Hawkings", "Henderson",
                 "Hewitt", "Higgins", "Hill", "Howart", "Hughes", "Hunter",
                 "Irving", "Jackson", "Johnston", "Jones", "Kearney", "Kelly",
                 "Kennedy", "Kerr", "Lambert", "MacArthur", "MacDonald",
                 "MacDougall", "MacIain", "MacIsaac", "MacKechnie", "MacKenzie",
                 "MacKinnon", "MacLean", "MacLeod", "MacNeil", "Mackay",
                 "Macpherson", "Manford", "Marshall", "Martin", "McGuire",
                 "McIntyre", "Miller", "Mitchell", "Monk", "Moore", "Morrison",
                 "Murray", "Newton", "Nicholson", "O'Brien", "O'Carroll",
                 "Osborne", "Paterson", "Peters", "Porter", "Reid", "Roberts",
                 "Robertson", "Robinson", "Ross", "Russell", "Scott", "Sharp",
                 "Shepherd", "Simpson", "Small", "Smiley", "Smith", "Smyth",
                 "Stewart", "Stokes", "Stone", "Swinney", "Taylor", "Thomas",
                 "Thompson", "Thomson", "Turner", "Walker", "Wallace", "Ward",
                 "Warren", "Watson", "Wilson", "Wood", "Wright", "Yates", "Young"]
    
    surname = random.choice(surnames)
    
    return surname


def getPhone(percentMobile=50) -> str:
    """Pick a random phone number - landline and mobile."""
    
    phoneNo = ""
    
    for counter in range(9):
        
        phoneNo = phoneNo + str(random.randint(0, 9))
        
    if random.randint(1, 100) < percentMobile:
        phoneNo = "07" + phoneNo
    else:
        phoneNo = "01" + phoneNo
    
    return phoneNo


def getEmail(forename="", surname="", percentNull=0) -> str:
    """Create a random email address."""
    
    if forename == "":
        forename = getForename()
        
    if surname == "":
        surname = getSurname()
    
    if random.randint(1, 100) > percentNull:
    
        domains = ["aol.com", "bt.com", "gmail.com", "gmx.com", "hotmail.com",
                   "icloud.com", "mailchimp.com", "outlook.com",
                   "protonmail.com", "yahoomail.com"]
        
        if random.randint(1, 100) > 80:  # 20% chance
            number = ""
            
        else:  # 80% chance
            number = str(random.randint(1, 2000))
            
        if random.randint(1, 100) > 50:  # 50% chance
            name = forename
            
        else:  # 50% chance
            name = forename[0] + "." + surname
        
        domain = domains[random.randint(0, len(domains)-1)]
        
        email  = name.lower() + number + "@" + domain
        
    else:
        
        email = ""
    
    return email


def getDate(min=2024, max=2024) -> str:
    """Create a random date (yyyy-mm-dd)."""
    
    day = random.randint(1, 30)
    month = random.randint(1, 12)
    year = random.randint(min, max)
    
    if month == 2 and day > 28:
        day = random.randint(1, 28)
    
    if day < 10:
        dayStr = "0" + str(day)
    else:
        dayStr = str(day)
        
    if month < 10:
        monthStr = "0" + str(month)
    else:
        monthStr = str(month)
        
    yearStr = str(year)
    
    date = yearStr + "-" + monthStr + "-" + dayStr
    
    return date


def getNights(min=1, max=14) -> int:
    """Pick random number of nights."""
    
    nights = random.randint(min, max)
    
    return nights


def getPrice(min=1, max=10, pence=True) -> float:
    """Pick a random price, with pence"""
    
    price = random.randint(int(min * 100), int(max * 100))
    
    price = price / 100
    
    if not pence:
        
        price = int(price)
    
    return price


def getTrue(percentTrue=50) -> bool:
    """Pick a random Boolean value."""
    
    chance = random.randint(1, 100)
    
    if chance <= percentTrue:
        result = True
    else:
        result = False
    
    return result


def getNumber(min=0, max=100) -> int:
    """Pick a random number."""
    
    number = random.randint(min, max)
    
    return number


def getVRN() -> str:
    """Pick a random vehicle registration number."""
   
    # Declare local variables
    notUsed = ["I", "J", "Q", "T", "U", "X", "Z"]
    regLetter = ""
    regYear = 0
    
    vehReg = ""
        
    # Create registration number
    # P(reg) = P(letter)^5 x P(number)
    # p(reg) = (1/19)^5 x (1/38) = 1/94,091,762
    
    # Add DVLA memory tag
    for counter in range(2):
        regLetter = "I"  # Reset
        while regLetter in notUsed:
            regLetter = chr(random.randint(65, 89))
        
        vehReg = vehReg + regLetter
    
    # Add age identifier
    regYear = random.randint(2, 20)
    
    if bool(random.randint(0, 1)):
        regYear = regYear + 50
        
    if regYear < 10:
        vehReg = vehReg + "0" + str(regYear) + " "
    else:            
        vehReg = vehReg + str(regYear) + " "
    
    # Add 3 random letters
    for counter in range(3):
        regLetter = "I"  # Reset
        while regLetter in notUsed:
            regLetter = chr(random.randint(65, 89))
        
        vehReg = vehReg + regLetter
                      
    return vehReg


def getMake() -> str:
    """Pick a random vehicle make."""
    
    # Initialise local variables
    make = ""
    makes = ["Ford", "Honda", "Hyundai", "Kia", "Nissan",
             "Renualt", "Skoda", "Toyota", "Vauxhall", "Volkwagen"]
    
    # Pick make
    make = random.choice(makes)
    
    return make


def getModel(make="") -> str:
    """Pick a random vehicle model."""
    
    # Initialise local variables
    model = ""
    makeNo = 0
    makes = ["Ford", "Honda", "Hyundai", "Kia", "Nissan",
             "Renualt", "Skoda", "Toyota", "Vauxhall", "Volkwagen"]
    
    # Get make number
    if make == "":
        make = getMake()
    elif make not in makes:
        make = getMake()
        
    # Loop for each make
    for index in range(len(makes)):
        if makes[index] == make:
            makeNo == index
    
    # Models - 1D arrays
    fords = ["B-MAX", "Capri", "C-MAX", "Cougar", "EcoSport", "Edge", "Escort",
             "Explorer", "Fiesta", "Focus", "Focus C-MAX", "Fusion", "Galaxy",
             "Granada", "Grand C-MAX", "Grand Tourneo Connect", "Ka", "Kuga",
             "Maverick", "Mondeo", "Mustang", "Mustang Mach-E", "Orion",
             "Probe", "Puma", "Scorpio", "Sierra", "Sierra Sapphire", "S-MAX",
             "StreetKa", "Tourneo Connect", "Tourneo Courier",
             "Transit Courier Kombi", "Transit Custom"]
    
    hondas = ["Accord", "Ballade", "Civic", "Concerto", "CR-V", "CRX", "CR-Z",
              "e", "FR-V", "HR-V", "Insight", "Integra", "Integra Type-R",
              "Jazz", "Legend", "Logo", "NSX", "Prelude", "S2000", "Shuttle",
              "Stream"]
    
    hyundais = ["Accent", "Amica", "Atoz", "Bayon", "Coupe", "Elantra",
                "Genesis", "Getz", "Grandeur", "i10", "i20", "i30", "i40",
                "i800", "Ioniq", "Ioniq 5", "Ioniq 6", "Ioniq Electric",
                "ix20", "ix35", "Kona", "Kona Electric", "Lantra", "Matrix",
                "Pony", "Pony X2", "Santa Fe", "S-Coupe", "Sonata", "Stellar",
                "Terracan", "Trajet", "Tucson", "Veloster", "XG30"]
    
    kias = ["Carens", "Ceed", "Cerato", "Clarus", "e-Niro", "EV6", "Magentis",
            "Mentor", "Niro", "Niro EV", "Optima", "Picanto", "Pride",
            "ProCeed", "Rio", "Sedona", "Shuma", "Shuma II", "Sorento",
            "Soul", "Soul EV", "Sportage", "Stinger", "Stonic", "Venga",
            "Xceed"]
    
    nissans = ["100 NX", "200 SX", "280C", "300C", "300 ZX", "350Z", "370Z",
               "Almera", "Almera Tino", "Ariya", "Bluebird", "Cherry", "Cube",
               "GT-R", "Juke", "Laurel", "Leaf", "Maxima", "Maxima QX",
               "Micra", "Murano", "Note", "NV200 Combi", "Pathfinder",
               "Patrol", "Pixo", "Prairie", "Primera", "Pulsar", "Qashqai",
               "Qashqai+2", "QX", "Serena", "Silvia", "Skyline R33",
               "Skyline R34", "Stanza", "Sunny", "Terrano", "X-Trail"]
    
    renaults = ["4", "5", "9", "11", "18", "19", "21", "25", "Arkana",
                "Avantime", "Captur", "Clio", "Espace", "Fluence",
                "Grand Espace", "Grand Modus", "Grand Scenic", "GTA", "A610",
                "Kadjar", "Kangoo", "Koleos", "Laguna", "Megane",
                "Megane E-Tech", "Megane Scenic", "Modus", "Safrane",
                "Scenic", "Sport Spider", "Twingo", "Twizy", "Vel Satis",
                "Wind", "Zoe"]
    
    skodas = ["Citigo", "Citigo-e", "Enyaq", "Estelle", "Fabia", "Favorit",
              "Felicia", "Kamiq", "Karoq", "Kodiaq", "Octavia", "Rapid",
              "Roomster", "Scala", "Superb", "Yeti"]
    
    toyotas = ["4-Runner", "Auris", "Avensis", "Avensis Verso", "Aygo", "bZ4X",
               "Camry", "Carina", "Carina E", "Celica", "C-HR", "Corolla",
               "GR Supra", "GR86", "GT86", "Highlander", "IQ", "Land Cruiser",
               "Land Cruiser Amazon", "Land Cruiser Colorado",
               "Land Cruiser V8", "MR2", "Paseo", "Picnic", "Previa", "Prius",
               "Proace City Verso", "RAV4", "Space Cruiser", "Starlet",
               "Supra", "Tercel", "Urban Cruiser", "Verso", "Yaris",
               "Yaris Cross"]
    
    vauxhalls = ["Adam", "Agila", "Ampera", "Antara", "Astra", "Astra Belmont",
                 "Calibra", "Carlton", "Cascada", "Cavalier", "Combo",
                 "Combo Tour", "Combo-e Life", "Corsa", "Corsa-e", "Crossland",
                 "Crossland X", "Frontera", "Grandland", "Grandland X",
                 "Insignia", "Meriva", "Mokka", "Mokka-e", "Monaro",
                 "Monterey", "Nova", "Omega", "Senator", "Signum", "Sintra",
                 "Tigra", "Vectra", "Viva", "Vivaro", "Vivaro Life",
                 "Vivaro Tourer", "Vivaro-e Life", "VX220", "VXR8", "Zafira"]
    
    volkswagens = ["Arteon", "Beetle", "Beetle Dune", "Bora", "Caddy",
                   "Caddy Life", "Caddy Maxi", "Caddy Maxi Camper",
                   "Caddy Maxi Life", "California", "Caravelle", "CC",
                   "Corrado", "e-Golf", "Eos", "e-Up", "Fox", "Golf",
                   "Grand California", "ID. Buzz", "ID.3", "ID.4", "ID.5",
                   "Jetta", "Lupo", "Multivan", "Passat", "Phaeton", "Polo",
                   "Scirocco", "Sharan", "Taigo", "T-Cross", "Tiguan",
                   "Touareg", "Touran", "T-Roc", "Up", "Vento"]
    
    # Models - 2D array
    models = [fords, hondas, hyundais, kias, nissans,
              renaults, skodas, toyotas, vauxhalls, volkswagens]
    
    # Pick model
    model = random.choice(models[makeNo])
    
    return model


def getColour() -> str:
    """Pick a random colour."""
    
    # Initialise local variable
    colours = ["Blue", "Silver", "Red", "Green", "Yellow", "Black", "White"]

    # Pick colour
    colour = random.choice(colours)
  
    return colour


def getGift() -> str:
    """Pick a random gift."""
    
    # Initialise local variable
    gifts = ["Beast Lab Core Line Shark Playset", "Furby Purple Interactive Toy Plush", "Barbie Estate Dolls House and 3 Dolls",
             "Bitzee Interactive Digital Pet", "DesignaFriend Connie Fashion Designer Doll", "LEGO Star WarsAhsoka Clone Trooper",
             "Nerf Elite 2.0 Double Punch Blaster", "Gabby's Dollhouse Cat Friendship Cruise Ship Playset",
             "MGA's Miniverse – Make it Mini Food: Dine", "Teenage Mutant Ninja Turtles Pizza Delivery Van",
             "Chad Valley Wooden 2 in 1 Café", "Chad Valley Trevor Talk Back Dino", "Little Live Pets – My Puppy’s Home Dalmatian Edition",
             "Squishmallows Drew the Mint Dragon", "LEGO Technic Lamborghini", "LEGO Harry Potter Dobby the House-Elf Figure",
             "Chad Valley Wooden Pizza", "Fingerlings Monkey Pink - Harmony", "Hot Wheels Monster Trucks Ultimate Crush Yard Playset"]
    
    # Pick gift
    gift = random.choice(gifts)
    
    return gift


def getHair() -> str:
    """Pick a random hair colour."""
    
    # Initialise local variable
    colours = ["Black", "Blond", "Brown", "Grey", "None", "Red", "White"]

    # Pick colour
    colour = random.choice(colours)
  
    return colour


def getEye() -> str:
    """Pick a random eye colour."""
    
    # Initialise local variable
    colours = ["Amber", "Black", "Blue", "Brown", "Green", "Hazel", "Grey"]

    # Pick colour
    colour = random.choice(colours)
  
    return colour


def getConviction() -> str:
    """Pick a random eye colour."""
    
    # Initialise local variable
    convictions = ["Arson", "Assault", "Bribery", "Burglary", "Cyberbullying",
                   "Drugs", "Extortion", "Forgery", "Fraud", "Hacking",
                   "Kidnapping", "Robbery", "Shoplifting", "Theft", "Vandalism"]

    # Pick colour
    conviction = random.choice(convictions)
  
    return conviction


def getSchoolYear(primary=False) -> str:
    """Pick a school year model."""
    
    # Initialise list
    if primary:
        years = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]
    else:
        years = ["S1", "S2", "S3", "S4", "S5", "S6"]
        
    # Pick year
    year = random.choice(years)
  
    return year


def getGrade() -> str:
    """Pick a SQA grade."""
    
    # Local variable
    grade = ""
        
    # Pick score
    score = random.normalvariate(100, 15)
    
    # Determine grade
    if score >= 125:
        grade = "A"
    elif score >= 110:
        grade = "B"
    elif score >= 85:
        grade = "C"
    elif score >= 75:
        grade = "D"
    else:
        grade = "No Award"
  
    return grade


def getBand() -> int:
    """Pick a SQA band."""
    
    # Local variable
    band = 0
        
    # Pick score
    score = random.normalvariate(100, 15)
    
    # Determine grade
    if score >= 130:
        band = 1
    if score >= 125:
        band = 2
    elif score >= 117:
        band = 3
    elif score >= 110:
        band = 4
    elif score >= 97:
        band = 5
    elif score >= 85:
        band = 6
    elif score >= 80:
        band = 7
    elif score >= 75:
        band = 8
    else:
        band = 9
  
    return band
