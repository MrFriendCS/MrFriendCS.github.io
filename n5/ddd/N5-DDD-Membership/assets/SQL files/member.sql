CREATE TABLE Member ( 
    memberNo VARCHAR(8) NOT NULL UNIQUE,
    clubID VARCHAR(6) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    address VARCHAR(30),
    town VARCHAR(20),
    postcode VARCHAR(8),
    dob DATE NOT NULL 
        CHECK(dob >= "1925-01-01"),
    renew INT NOT NULL 
        CHECK(renew >=1 AND renew <= 12),
    gender VARCHAR(15) 
        CHECK(gender IN ("F", "M", "ND")),
    type VARCHAR(15) NOT NULL 
        CHECK(type IN ("Adult", "Child", "Guest",
                       "Senior", "Student")),
    FOREIGN KEY (clubID) 
        REFERENCES club(clubID),
    PRIMARY KEY (memberNo)
);

INSERT INTO Member VALUES ("AAJ118","SP433","Josephine","Bauer","60 Ligula Street","Brockton","WQ03 7XN","1971-10-14",9,"F","Adult");
INSERT INTO Member VALUES ("AHI288","SP345","Charles","Pollard","50 Vitae Street","Lowhall","DP2H 3IW","1979-09-14",7,"M","Adult");
INSERT INTO Member VALUES ("AIE225","SP197","Chiquita","Stone","73 Nunc Road","Watertown","K1Y 2IY","1969-08-29",8,"F","Adult");
INSERT INTO Member VALUES ("AVC243","SP128","Demetria","Hanson","31 Porttitor Road","Parkers","Q8 2OI","1959-03-17",2,"F","Adult");
INSERT INTO Member VALUES ("AVJ194","SP487","Wallace","Blevins","13 Euismod Avenue","Lowhall","C76 6FO","1955-12-02",8,"M","Adult");
INSERT INTO Member VALUES ("AWP182","SP487","Whoopi","Holcomb","61 Lacus Road","Baldwin","YH3F 5QM","1972-07-25",5,"F","Adult");
INSERT INTO Member VALUES ("AXE117","SP365","Faith","Hooper","73 Ipsum Street","Lebaness","HD8Z 5SB","1956-05-21",5,"F","Adult");
INSERT INTO Member VALUES ("BBP129","SP324","Venus","Stafford","4 Lobortis Avenue","Lowhall","PK6 4MY","1947-05-30",11,"F","Adult");
INSERT INTO Member VALUES ("BBZ172","SP345","Sopoline","Dominguez","81 Ipsum Street","Lebaness","P0R 8UL","1986-06-24",11,"F","Student");
INSERT INTO Member VALUES ("BDA285","SP433","Judah","Rowland","8 Com Road","Brockton","GJ86 0QG","1971-10-08",4,"M","Adult");
INSERT INTO Member VALUES ("BFS219","SP433","Dacey","Conrad","8 Diam Street","Lowhall","QI8 4BD","1994-08-23",5,"M","Senior");
INSERT INTO Member VALUES ("BFU236","SP433","Amity","Booker","15 Feugiat Street","Port Worland","Y9 5JM","1969-07-16",12,"F","Adult");
INSERT INTO Member VALUES ("BLR256","SP197","Shaine","Moses","4 Nec Street","Baldwin","HA5Z 4RL","1985-08-21",4,"M","Senior");
INSERT INTO Member VALUES ("BLY235","SP324","Fritz","Massey","24 Malesuada Avenue","Benton","NB1D 8CG","1970-03-05",3,"M","Adult");
INSERT INTO Member VALUES ("BMG254","SP433","Claudia","Porter","4 Tincidunt Road","Brockton","Y35 3HT","1996-01-18",7,"F","Adult");
INSERT INTO Member VALUES ("BNJ273","SP487","Susan","Leblanc","15 Vel Avenue","Allentown","DV1F 3XW","1999-09-16",3,"F","Student");
INSERT INTO Member VALUES ("BTA297","SP487","Hector","Flynn","32 Neque Road","Deedon","O91 9JU","1953-05-01",3,"M","Adult");
INSERT INTO Member VALUES ("BVH111","SP128","Brennan","Carrillo","45 Nec Street","Baldwin","C10 8XH","1951-12-19",8,"M","Student");
INSERT INTO Member VALUES ("BWA234","SP128","Guy","Marsh","53 Sit Road","Brockton","GJ6W 6EL","1973-07-21",5,"M","Student");
INSERT INTO Member VALUES ("BWE112","SP128","Brent","Brooks","76 Odio Road","Muncie","E58 8HC","1977-03-22",10,"M","Adult");
INSERT INTO Member VALUES ("CBK142","SP365","Madeson","Munoz","14 Mi Street","Deedon","RB7 1WQ","2000-04-27",1,"F","Student");
INSERT INTO Member VALUES ("CDG191","SP487","Samantha","Barnes","91 Parturient Street","Baldwin","AI26 2YL","1989-03-04",5,"F","Adult");
INSERT INTO Member VALUES ("CDZ218","SP324","Dai","Whitney","81 Magna Road","Lowhall","X8 8XG","1956-02-23",9,"M","Adult");
INSERT INTO Member VALUES ("CMB202","SP197","Forrest","Cervantes","99 Phasellus Road","Baldwin","W03 8HQ","1993-09-08",12,"M","Child");
INSERT INTO Member VALUES ("CMP246","SP197","Charlotte","Hinton","65 Tempus Avenue","Baldwin","UZ9V 9AL","1973-12-17",10,"F","Child");
INSERT INTO Member VALUES ("CMZ176","SP345","Griffith","Simmons","30 Enim Road","Lowhall","O4 7CT","1974-09-20",10,"M","Child");
INSERT INTO Member VALUES ("CQM262","SP197","Roberta","Mccall","55 Vestibulum Avenue","Baldwin","R4 7CE","1949-07-25",5,"F","Child");
INSERT INTO Member VALUES ("CTV244","SP197","Thomas","Albert","21 Dapibus Road","Deedon","D50 3ST","1998-10-23",8,"M","Child");
INSERT INTO Member VALUES ("CWH123","SP128","Nathan","Acosta","58 Nisl Street","Deedon","ST9 4TW","1973-05-09",8,"M","Student");
INSERT INTO Member VALUES ("DGU106","SP433","Scarlet","Greene","44 Dui Street","Baldwin","HL8S 5SB","1962-01-26",2,"F","Adult");
INSERT INTO Member VALUES ("DMW185","SP345","Debra","Perkins","26 Bibendum Road","Lowhall","RF4 5XG","1968-10-27",7,"F","Adult");
INSERT INTO Member VALUES ("DNT257","SP487","Mechelle","Wooten","5 Est Road","Lebaness","C99 5GT","1956-03-31",3,"F","Senior");
INSERT INTO Member VALUES ("DPR140","SP345","Hayes","Hill","63 Crase Road","Worland","GB64 8BP","1972-03-27",8,"M","Adult");
INSERT INTO Member VALUES ("DUF292","SP345","Emily","Barnes","16 Facilisi Avenue","Faverdeen","JR7H 7PU","1983-02-05",7,"F","Adult");
INSERT INTO Member VALUES ("EBR220","SP487","Aileen","Lester","93 Phasellus Street","Baldwin","XK9 5NA","1965-10-04",7,"F","Adult");
INSERT INTO Member VALUES ("EGZ210","SP365","Moana","Glover","42 Malesuada Road","Benton","G3 4SV","1979-10-22",3,"F","Adult");
INSERT INTO Member VALUES ("EIS108","SP487","Martena","Taylor","16 Aliquam Avenue","Worland","P24 6MH","1949-11-17",3,"F","Adult");
INSERT INTO Member VALUES ("EJK122","SP487","TaShya","Kelly","88 Lorem Avenue","Brockton","H9 5AK","1986-11-14",12,"F","Adult");
INSERT INTO Member VALUES ("EKW264","SP365","Jolie","Mcneil","94 Non Avenue","Lowhall","K1E 9VM","1973-02-05",3,"F","Adult");
INSERT INTO Member VALUES ("EOH226","SP107","Kiona","Fowler","54 Velit Road","Baldwin","O12 7LX","1961-01-26",10,"F","Adult");
INSERT INTO Member VALUES ("EON223","SP487","Wynne","Bridges","3 Ace Street","Lowhall","TU8C 4CY","1995-12-14",4,"M","Adult");
INSERT INTO Member VALUES ("EOS119","SP197","Kiona","Blake","66 Interdum Road","Lebaness","B58 4QW","1965-11-17",9,"F","Adult");
INSERT INTO Member VALUES ("EPH215","SP345","Basil","Hendrix","25 Magna Road","Lowhall","S7C 1KK","1945-12-17",7,"M","Adult");
INSERT INTO Member VALUES ("ESK183","SP433","Gillian","Wood","19 Pellentesque Road","Lowhall","C43 1ML","1992-04-15",9,"F","Adult");
INSERT INTO Member VALUES ("FCE107","SP345","Nita","Fisher","80 Crase Street","Worland","VL65 9QH","1955-08-07",1,"F","Student");
INSERT INTO Member VALUES ("FMH120","SP365","Maggie","Bradley","30 Crase Road","Worland","AY24 2KU","1959-07-18",7,"F","Student");
INSERT INTO Member VALUES ("FNK165","SP345","Dawn","Coffey","96 Ipsum Road","Lebaness","AZ96 8YB","1954-09-17",10,"F","Senior");
INSERT INTO Member VALUES ("FVA113","SP433","Winifred","Anderson","69 Pellentesque Street","Lowhall","AG11 9RN","1974-09-08",12,"F","Student");
INSERT INTO Member VALUES ("FVM221","SP345","Sigourney","Carey","63 Vulputate Street","Baldwin","B2 3HT","1971-05-01",5,"F","Adult");
INSERT INTO Member VALUES ("FXN209","SP487","Daria","Yang","87 Ut Street","Baldwin","B5 8KP","1996-11-19",10,"F","Student");
INSERT INTO Member VALUES ("GCJ249","SP345","Raya","Oliver","72 Primis Street","Brockton","JJ48 4UM","1995-11-22",8,"F","Adult");
INSERT INTO Member VALUES ("GDA149","SP324","Jessica","Olson","82 Vel Street","Allentown","J0 5QW","1962-11-16",10,"F","Adult");
INSERT INTO Member VALUES ("GJG237","SP345","Darius","Yates","30 Quis Street","Brockton","RY8K 2XH","1976-06-24",7,"M","Senior");
INSERT INTO Member VALUES ("GLL179","SP487","Hermione","Kidd","51 Donec Road","Lowhall","J0Y 0HG","1971-02-20",3,"F","Adult");
INSERT INTO Member VALUES ("GNJ170","SP197","Keefe","Carpenter","92 Nibh Avenue","Muncie","HN66 2JM","1987-07-02",1,"M","Child");
INSERT INTO Member VALUES ("GNT232","SP345","Catherine","Roberts","75 Elit Avenue","Berkeley","HU7N 3VB","1985-10-01",6,"F","Adult");
INSERT INTO Member VALUES ("GRX229","SP128","Xyla","Barker","71 Semper Avenue","Brockton","L3S 0QP","1978-09-23",2,"F","Adult");
INSERT INTO Member VALUES ("GXT253","SP345","Erich","Britt","58 Ornare Street","Muncie","NO33 3FI","1946-12-21",5,"M","Adult");
INSERT INTO Member VALUES ("GYT278","SP487","Mallory","Gentry","7 Natoque Street","Deedon","LA86 4NJ","1950-09-13",10,"M","Adult");
INSERT INTO Member VALUES ("HBJ167","SP345","Lorna","Hayes","15 At Street","Lowhall","HF4U 8RA","1992-12-03",5,"F","Adult");
INSERT INTO Member VALUES ("HBU196","SP487","Isabelle","James","21 Lectus Avenue","Lebaness","YW23 0XN","1990-04-27",11,"F","Student");
INSERT INTO Member VALUES ("HCH136","SP345","Riley","Newton","86 Libero Road","Charleston","P9 4HW","1970-02-05",7,"M","Adult");
INSERT INTO Member VALUES ("HGD189","SP197","Omar","Harding","24 Aliquam Street","Worland","SP8 1SZ","1946-04-26",8,"M","Child");
INSERT INTO Member VALUES ("HLC205","SP107","Barbara","Morales","90 Acer Road","Baldwin","K7J 7GJ","1994-04-06",11,"F","Adult");
INSERT INTO Member VALUES ("HNH155","SP107","Dominique","Russell","35 Aliquam Avenue","Worland","C64 6YJ","1956-06-10",7,"F","Child");
INSERT INTO Member VALUES ("HTV195","SP487","Marvin","Jarvis","25 Vel Avenue","Allentown","E29 0KT","1973-07-28",11,"M","Adult");
INSERT INTO Member VALUES ("HYS181","SP324","Steven","Hogan","6 In Street","Charleston","F07 5KK","1999-10-24",11,"M","Adult");
INSERT INTO Member VALUES ("HZU240","SP345","Bevis","Sampson","88 Egestas Avenue","Baldwin","V6 4CJ","1949-11-20",12,"M","Adult");
INSERT INTO Member VALUES ("IAL211","SP433","Erich","Logan","17 Consectetuer Avenue","Brockton","LX6I 3RF","1956-01-07",7,"M","Adult");
INSERT INTO Member VALUES ("IFG212","SP345","Janna","Carpenter","13 Tellus Road","Allentown","A7 4IU","1985-01-22",3,"F","Senior");
INSERT INTO Member VALUES ("IKH124","SP345","Ruth","Santos","44 Vestibulum Street","Baldwin","X7 0KS","2000-08-09",11,"F","Adult");
INSERT INTO Member VALUES ("IOI116","SP128","James","Frank","65 Massa Street","Lowhall","NE1Y 5WP","1966-11-19",10,"M","Adult");
INSERT INTO Member VALUES ("IPU145","SP433","Jena","Macdonald","23 Sit Road","Brockton","IL1 2NX","1971-02-17",8,"F","Student");
INSERT INTO Member VALUES ("IPU222","SP128","Davis","Herman","45 Nascetur Avenue","Charleston","MO4R 3RS","1968-06-20",9,"M","Student");
INSERT INTO Member VALUES ("IQO168","SP197","Ruth","Sparks","49 Nonummy Road","Newton","H4N 5JJ","1999-12-27",4,"F","Student");
INSERT INTO Member VALUES ("ITU178","SP324","Russell","Phillips","69 Nec Avenue","Baldwin","F79 4DQ","1948-10-31",12,"M","Student");
INSERT INTO Member VALUES ("IZQ242","SP197","Yolanda","Mcgowan","77 Aliquam Road","Worland","Y09 0QC","1997-03-14",3,"F","Senior");
INSERT INTO Member VALUES ("JAO169","SP433","Jack","Humphrey","54 Suspendisse Road","Faverdeen","BD85 9KG","1987-07-14",3,"M","Student");
INSERT INTO Member VALUES ("JEQ268","SP107","Danielle","Graves","69 Proin Street","Brockton","W17 7ZI","1972-08-13",3,"F","Adult");
INSERT INTO Member VALUES ("JFY146","SP433","Inga","Davenport","14 Aliquam Avenue","Worland","YL4Z 7JQ","1952-08-06",8,"F","Adult");
INSERT INTO Member VALUES ("JQN148","SP345","Nelly","Pitts","89 Ridiculus Street","Port Worland","A1 0IM","1992-09-02",1,"F","Adult");
INSERT INTO Member VALUES ("JST207","SP365","Lee","George","81 Enim Avenue","Lowhall","J90 5FB","1992-03-08",11,"M","Student");
INSERT INTO Member VALUES ("JUH204","SP345","Lev","Dillon","63 Adipiscing Street","Lowhall","TU7 7GD","1951-10-09",8,"M","Adult");
INSERT INTO Member VALUES ("JVL130","SP128","Ariana","Herring","30 Semper Road","Brockton","X02 0HH","1954-03-12",9,"F","Student");
INSERT INTO Member VALUES ("KBF252","SP107","Cathleen","Cote","46 At Road","Lowhall","YR3B 3ZT","1972-05-25",10,"F","Adult");
INSERT INTO Member VALUES ("KCD188","SP487","Alice","Gates","50 Eget Road","Baldwin","IU6 4UQ","1953-07-16",3,"F","Adult");
INSERT INTO Member VALUES ("KGD230","SP128","Nissim","Rodgers","27 Nunc Street","Watertown","H2 2WU","1974-09-15",5,"M","Child");
INSERT INTO Member VALUES ("KOC174","SP107","Holly","Singleton","86 Litora Avenue","Baldwin","TK3X 7CG","1992-09-14",7,"F","Adult");
INSERT INTO Member VALUES ("KPC201","SP487","Genevieve","Heath","1 Dignissim Street","Lebaness","K44 2QH","1956-03-08",3,"F","Adult");
INSERT INTO Member VALUES ("KPM163","SP107","Leilani","Allen","92 Fermentum Road","Baldwin","M4U 8HM","1997-03-14",7,"F","Adult");
INSERT INTO Member VALUES ("KTU197","SP345","Bradley","Clarke","19 Adipiscing Road","Lowhall","X7I 6PV","1959-01-21",10,"M","Child");
INSERT INTO Member VALUES ("KWP213","SP487","Sophia","Mccarty","25 Et Road","Riverton","R7M 1LL","1974-06-01",4,"F","Adult");
INSERT INTO Member VALUES ("KZR289","SP487","Mary","Carter","28 Crase Road","Worland","MV4S 2KM","1990-03-15",7,"F","Student");
INSERT INTO Member VALUES ("LDB151","SP433","Victor","Tran","5 Rutrum Road","Worland","KN9N 6CD","1984-07-06",8,"M","Child");
INSERT INTO Member VALUES ("LEC245","SP345","Leroy","Barry","62 Vel Avenue","Allentown","MD8 2YY","1960-03-09",6,"M","Senior");
INSERT INTO Member VALUES ("LFD227","SP345","Julie","Logan","41 Euismod Road","Lowhall","D3 3ZN","1975-08-29",7,"F","Child");
INSERT INTO Member VALUES ("LGI127","SP487","Octavius","Schroeder","18 Nibh Road","Muncie","AE4 0YZ","1977-10-11",5,"M","Adult");
INSERT INTO Member VALUES ("LGP171","SP487","Jennifer","Reilly","41 Iaculis Avenue","Lebaness","N65 7OH","1952-11-08",6,"F","Adult");
INSERT INTO Member VALUES ("LHJ260","SP197","Georgia","Barrera","77 Massa Road","Lowhall","XG9 5QE","1980-02-12",5,"F","Adult");
INSERT INTO Member VALUES ("LQF214","SP345","Tara","Harper","39 Pede Street","Charleston","V04 0PN","1946-06-11",10,"F","Child");
INSERT INTO Member VALUES ("MAW282","SP345","Karina","Hudson","25 Fringilla Road","Torrington","D3 1OV","1964-10-05",7,"F","Senior");
INSERT INTO Member VALUES ("MFT147","SP365","Hayley","Conway","86 Quisque Street","Evansville","V1 5UV","1990-10-29",5,"F","Adult");
INSERT INTO Member VALUES ("MGL208","SP487","Christen","Murray","67 Netus Road","Parkers","ET8 1WC","1955-09-16",11,"M","Adult");
INSERT INTO Member VALUES ("MMC175","SP433","Bell","Conley","19 Integer Road","Lowhall","S1V 6TS","1987-07-09",9,"M","Senior");
INSERT INTO Member VALUES ("MSZ173","SP365","Louis","Pope","82 Per Avenue","Lowhall","VK5 1QJ","1995-05-26",2,"M","Adult");
INSERT INTO Member VALUES ("MVB206","SP128","Clarke","Stephenson","30 Facilisis Street","Faverdeen","RT48 9KI","1993-01-24",9,"M","Adult");
INSERT INTO Member VALUES ("MYB160","SP487","Randall","Chase","46 Porttitor Street","Parkers","D2T 8IO","1956-06-14",8,"M","Student");
INSERT INTO Member VALUES ("MZR138","SP324","Rajah","Terry","47 Nunc Street","Watertown","D6 6PZ","1963-09-01",7,"M","Senior");
INSERT INTO Member VALUES ("NKN126","SP345","Sage","Lang","10 Vivamus Street","Clifton","J5Z 0CB","1987-09-27",5,"F","Adult");
INSERT INTO Member VALUES ("NLL144","SP128","Preston","Reynolds","40 At Road","Lowhall","CW38 4IG","1980-07-08",5,"M","Adult");
INSERT INTO Member VALUES ("NOJ283","SP197","Ishmael","Butler","72 Donec Street","Lowhall","EJ6B 5YG","1976-06-01",2,"M","Adult");
INSERT INTO Member VALUES ("NRI190","SP487","Ali","Rutledge","39 Lorem Avenue","Brockton","UF80 9YS","1959-09-03",6,"M","Adult");
INSERT INTO Member VALUES ("NTM250","SP197","Sage","Church","4 Rutrum Road","Worland","I7H 6KD","1953-10-28",8,"F","Senior");
INSERT INTO Member VALUES ("NTS153","SP487","Jacqueline","Skinner","27 At Street","Lowhall","K4 8HS","1953-12-06",6,"F","Adult");
INSERT INTO Member VALUES ("NUL128","SP197","Dahlia","Greene","13 Dictum Street","Lowhall","GA8 2HN","1976-11-21",3,"F","Adult");
INSERT INTO Member VALUES ("NXP157","SP345","Sydney","York","58 Non Street","Lowhall","J8 8TL","1954-11-08",7,"M","Child");
INSERT INTO Member VALUES ("NYS266","SP487","Stephanie","Lindsay","78 Venenatis Road","Faverdeen","M3A 1UT","1967-06-23",10,"F","Adult");
INSERT INTO Member VALUES ("OBX110","SP128","Kelly","Nieves","72 Cursus Avenue","Lebaness","A82 8BN","1990-03-28",3,"F","Adult");
INSERT INTO Member VALUES ("ONW276","SP487","Xerxes","Roberts","34 Id Avenue","Muncie","XK8U 8YC","1959-04-15",4,"M","Adult");
INSERT INTO Member VALUES ("OXX216","SP487","Martina","Raymond","34 Mollis Street","Lebaness","S86 1GE","1948-01-14",3,"F","Adult");
INSERT INTO Member VALUES ("PBF184","SP345","Althea","Mcmahon","46 Arcu Avenue","Lebaness","PP34 8ZT","1978-09-11",4,"F","Adult");
INSERT INTO Member VALUES ("PDB133","SP487","Colin","Chan","21 Quis Avenue","Brockton","N86 5UL","1953-03-30",2,"M","Adult");
INSERT INTO Member VALUES ("PHP137","SP345","Daniel","Stuart","34 Nonummy Street","Newton","RT19 4GZ","1953-01-31",9,"M","Student");
INSERT INTO Member VALUES ("PMJ156","SP128","Camden","Trevino","63 Egestas Street","Baldwin","G96 3CG","1978-01-27",10,"M","Adult");
INSERT INTO Member VALUES ("PRI186","SP487","Yetta","Pickett","67 Sed Avenue","Torrington","P05 0WR","1999-05-08",12,"F","Student");
INSERT INTO Member VALUES ("PWD105","SP107","Ciaran","Shaffer","14 Ligula Street","Brockton","N7D 4MR","2000-02-17",9,"M","Adult");
INSERT INTO Member VALUES ("QBN299","SP345","Debra","Morgan","59 Non Road","Lowhall","VV01 5TW","1946-08-13",5,"F","Adult");
INSERT INTO Member VALUES ("QFI203","SP345","Sylvia","Duffy","75 Vitae Street","Lowhall","EB3 3ZM","1966-06-28",5,"F","Senior");
INSERT INTO Member VALUES ("QGF248","SP345","Josephine","Evans","96 Vivamus Road","Clifton","IW7 7VO","1962-02-28",5,"F","Senior");
INSERT INTO Member VALUES ("QLM270","SP433","Hannah","Estrada","4 Elit Avenue","Berkeley","T19 6IS","1970-12-03",5,"F","Adult");
INSERT INTO Member VALUES ("QMP166","SP487","Taylor","Owen","21 Sollicitudin Avenue","Faverdeen","J38 7MQ","1997-07-13",3,"M","Student");
INSERT INTO Member VALUES ("QNH247","SP107","Olivia","Lopez","75 Cursus Street","Lebaness","QF5M 8NJ","1998-11-16",11,"F","Adult");
INSERT INTO Member VALUES ("QPW150","SP345","Cecilia","Burt","72 Amet Road","Brockton","I4 4PW","1980-03-21",3,"F","Adult");
INSERT INTO Member VALUES ("QVK132","SP345","Cadman","Donovan","47 Tincidunt Road","Brockton","IP7A 4UF","1956-12-20",4,"M","Student");
INSERT INTO Member VALUES ("QYG131","SP433","Daryl","Cantrell","39 Quis Avenue","Brockton","A22 3TI","1976-08-19",1,"M","Child");
INSERT INTO Member VALUES ("RCV238","SP487","Sylvester","Mcguire","89 Quis Avenue","Brockton","F2 0CI","1973-03-20",4,"M","Adult");
INSERT INTO Member VALUES ("RNH279","SP487","Grady","Mcdonald","43 Iaculis Avenue","Lebaness","CA4 5BG","1959-06-13",10,"M","Senior");
INSERT INTO Member VALUES ("ROP295","SP345","Lael","Simpson","73 Rhoncus Street","Charleston","O7D 3WF","1957-10-28",6,"M","Senior");
INSERT INTO Member VALUES ("RST139","SP345","Bruce","Mercer","63 Auctor Road","Lowhall","C98 3PG","1989-04-30",2,"M","Child");
INSERT INTO Member VALUES ("RTN159","SP197","Rogan","Hancock","86 Aliquam Street","Worland","PM04 4HI","1966-10-25",3,"M","Adult");
INSERT INTO Member VALUES ("RUD180","SP128","Hashim","Underwood","48 Aliquet Street","Baldwin","HW07 6LB","1975-01-27",7,"M","Adult");
INSERT INTO Member VALUES ("RXJ267","SP487","Donna","Burks","97 Donec Road","Lowhall","HV4 3KO","1956-05-24",8,"F","Student");
INSERT INTO Member VALUES ("RZM187","SP365","Brooke","Tran","56 Orci Road","Muncie","MW6G 5JL","1984-11-29",6,"F","Adult");
INSERT INTO Member VALUES ("SJN154","SP107","Willina","Key","84 Elit Street","Berkeley","OY8Q 6OC","1956-01-17",4,"F","Adult");
INSERT INTO Member VALUES ("SML100","SP128","Brady","Schmidt","58 Ace Road","Lowhall","ED88 4WD","1953-03-04",1,"M","Student");
INSERT INTO Member VALUES ("SQH269","SP345","Madaline","Barrera","86 Donec Street","Lowhall","CT89 0UD","1953-03-22",12,"F","Adult");
INSERT INTO Member VALUES ("SWT286","SP128","Vernon","Leon","68 Purus Avenue","Lowhall","ID60 4MY","1982-11-26",12,"M","Adult");
INSERT INTO Member VALUES ("SZA135","SP487","Rafael","Hatfield","9 Quisque Road","Evansville","D5W 8QA","1947-02-02",8,"M","Student");
INSERT INTO Member VALUES ("TBF293","SP487","Tarik","Perry","34 Integer Road","Lowhall","SE45 3KL","1961-07-29",7,"M","Adult");
INSERT INTO Member VALUES ("TCQ177","SP345","Murphy","Robbins","58 Sed Road","Faverdeen","QD66 7NB","1968-08-15",7,"M","Adult");
INSERT INTO Member VALUES ("TQT280","SP197","Burke","Preston","41 Et Road","Riverton","R51 1DR","1988-03-04",2,"M","Adult");
INSERT INTO Member VALUES ("TTJ277","SP487","Athena","Tillman","71 Lorem Avenue","Brockton","LJ44 8IO","1962-07-31",6,"F","Adult");
INSERT INTO Member VALUES ("TWT284","SP487","Noelani","Vaughn","16 Cubilia Street","Weirton","NU5 8MO","1999-03-12",11,"F","Adult");
INSERT INTO Member VALUES ("TXJ199","SP324","Daryl","Morin","86 Ace Road","Lowhall","F8T 2KQ","1993-10-29",3,"M","Student");
INSERT INTO Member VALUES ("TZX115","SP487","Leilani","Alford","11 Dictum Street","Lowhall","TS70 7CM","1971-05-30",2,"F","Adult");
INSERT INTO Member VALUES ("UAS239","SP487","Alana","Patterson","53 Faucibus Street","Lebaness","UR9H 6LN","1978-04-08",6,"F","Student");
INSERT INTO Member VALUES ("UJX251","SP365","Latifah","Vincent","19 Euismod Road","Lowhall","L4 2XM","1981-10-26",8,"F","Adult");
INSERT INTO Member VALUES ("UKB114","SP487","Maxine","Garcia","17 Vitae Avenue","Lowhall","W4B 4KU","1997-10-01",1,"F","Senior");
INSERT INTO Member VALUES ("UMF152","SP324","MacKenzie","Jordan","49 Eleifend Road","Deedon","L1U 4CS","1964-06-01",12,"M","Adult");
INSERT INTO Member VALUES ("UPB198","SP107","Zeph","Bond","57 Natoque Avenue","Deedon","NS9X 0SH","1992-01-08",6,"M","Student");
INSERT INTO Member VALUES ("UPV217","SP365","Zachary","Bates","49 Velit Road","Baldwin","T12 4BC","1959-04-29",12,"M","Senior");
INSERT INTO Member VALUES ("URP265","SP487","Hakeem","Sweet","80 Lobortis Avenue","Lowhall","Y5I 4GF","1980-02-11",4,"M","Adult");
INSERT INTO Member VALUES ("UVR228","SP433","Hammett","Hill","56 Nullam Avenue","Newton","T0 8IP","1983-12-28",8,"M","Adult");
INSERT INTO Member VALUES ("UWA261","SP128","Neil","Dillard","10 Iaculis Road","Lebaness","IQ1 2RD","1965-04-01",3,"M","Student");
INSERT INTO Member VALUES ("UXM231","SP345","Kirestin","Snyder","18 Gravida Street","Lowhall","RS8 1VX","1994-10-30",8,"F","Adult");
INSERT INTO Member VALUES ("UYT125","SP128","Bo","Barr","37 Parturient Road","Baldwin","M6I 2IS","1958-11-11",10,"M","Adult");
INSERT INTO Member VALUES ("VCV274","SP433","Ina","Wells","54 Tellus Road","Allentown","G41 0YZ","1966-06-22",10,"F","Adult");
INSERT INTO Member VALUES ("VDT141","SP487","Jade","Barry","71 Aliquet Avenue","Baldwin","I28 8WR","1984-09-12",1,"F","Adult");
INSERT INTO Member VALUES ("VHZ296","SP345","Angela","Dickerson","30 Dolor Street","Brockton","W6Y 3QL","1958-02-28",10,"F","Senior");
INSERT INTO Member VALUES ("VMD193","SP107","Mary","Franco","66 Acer Street","Baldwin","PV0V 0WI","1978-06-07",7,"F","Adult");
INSERT INTO Member VALUES ("VVP259","SP433","Velma","Castro","18 Enim Street","Lowhall","FF4W 4VN","1970-10-21",5,"F","Senior");
INSERT INTO Member VALUES ("VVS275","SP107","Flavia","Carver","33 Luctus Street","Parkers","O76 5AL","1984-05-08",1,"F","Adult");
INSERT INTO Member VALUES ("VZX263","SP487","Derek","Mcdonald","17 Dignissim Avenue","Lebaness","J19 0VO","1953-06-30",4,"M","Adult");
INSERT INTO Member VALUES ("WBA109","SP197","Sally","Moran","48 Sit Street","Brockton","KO02 6AK","1980-02-20",4,"F","Adult");
INSERT INTO Member VALUES ("WBM294","SP487","Rafael","Santiago","32 Ut Avenue","Baldwin","J7N 6IH","1953-10-09",9,"M","Adult");
INSERT INTO Member VALUES ("WHG104","SP433","MacKenzie","Peters","30 Ace Road","Lowhall","N9G 5LA","1959-02-09",11,"M","Adult");
INSERT INTO Member VALUES ("WXU134","SP345","Briony","Lane","33 Fringilla Street","Torrington","V6 2OH","1992-12-24",1,"F","Child");
INSERT INTO Member VALUES ("WYM290","SP345","Garrett","Baldwin","4 Eu Road","Baldwin","X8Q 3LQ","1979-02-05",8,"M","Student");
INSERT INTO Member VALUES ("WYN158","SP107","Scarlet","Duffy","26 Sed Avenue","Torrington","E90 6UL","1994-06-12",9,"F","Senior");
INSERT INTO Member VALUES ("XID241","SP107","Madeson","Parker","73 Vel Street","Allentown","A2T 1EQ","1969-04-26",8,"F","Adult");
INSERT INTO Member VALUES ("XQQ291","SP487","Maryam","Rivera","68 Vestibulum Street","Baldwin","L2D 5NS","1958-12-15",10,"F","Student");
INSERT INTO Member VALUES ("XSU224","SP197","Cynthia","Schmidt","39 Malestie Avenue","Brockton","ZF9G 1YY","1990-11-01",12,"F","Adult");
INSERT INTO Member VALUES ("XUV271","SP197","Hilda","Klein","32 Inceptos Road","Lebaness","A0 6NR","1968-09-26",1,"F","Adult");
INSERT INTO Member VALUES ("XWF233","SP324","Michelle","Mccarty","10 Aliquam Road","Worland","P5M 5PK","1984-03-09",1,"F","Senior");
INSERT INTO Member VALUES ("XYG258","SP324","Kathleen","Dominguez","33 Porttitor Avenue","Parkers","R5 4QG","1999-01-22",5,"F","Student");
INSERT INTO Member VALUES ("XZA192","SP487","Angela","Compton","9 Nunc Road","Watertown","SP89 4YS","1972-04-25",5,"F","Adult");
INSERT INTO Member VALUES ("XZI281","SP128","Amal","Farley","75 Metus Street","Brockton","I4H 0TD","1969-06-24",2,"M","Student");
INSERT INTO Member VALUES ("YBA200","SP128","Rylee","Goodman","27 Aliquet Street","Baldwin","YU5T 0VE","1992-06-04",9,"M","Student");
INSERT INTO Member VALUES ("YGM298","SP345","Helen","West","94 Arcu Street","Lebaness","R1 4CD","1995-11-09",3,"F","Child");
INSERT INTO Member VALUES ("YMD255","SP197","Seth","Morin","6 Nec Street","Baldwin","U2W 2IG","1966-08-14",10,"M","Adult");
INSERT INTO Member VALUES ("YZO162","SP487","Donna","Ashley","56 Malesuada Avenue","Benton","IZ36 4NF","1959-10-20",5,"F","Adult");
INSERT INTO Member VALUES ("ZDA101","SP324","Noelani","Vasquez","73 Tellus Avenue","Allentown","AI2A 7ZF","1976-01-20",7,"F","Student");
INSERT INTO Member VALUES ("ZDG287","SP128","Whilem","Hall","66 Eu Street","Baldwin","YM3 3VD","1988-09-24",11,"M","Child");
INSERT INTO Member VALUES ("ZFZ272","SP487","Thomas","Riggs","37 Sociis Street","Worland","SQ44 9PZ","1978-08-02",9,"M","Student");
INSERT INTO Member VALUES ("ZKD102","SP365","Maggy","Stevenson","31 Tortor Road","Baldwin","E5W 6JV","1964-12-29",11,"F","Senior");
INSERT INTO Member VALUES ("ZKF121","SP345","Tamara","Wade","95 Ace Road","Lowhall","F3P 3JH","1969-07-23",6,"F","Senior");
INSERT INTO Member VALUES ("ZNE161","SP197","Irene","Landry","46 Eu Avenue","Baldwin","MI7 5MA","1953-10-31",11,"F","Child");
INSERT INTO Member VALUES ("ZSA143","SP128","Donovan","Flynn","82 Vel Street","Allentown","D2F 0CT","1998-02-23",11,"M","Guest");
INSERT INTO Member VALUES ("ZTB103","SP487","Hollee","Ward","39 Orci Road","Muncie","VF88 5CX","1966-02-25",12,"F","Guest");
INSERT INTO Member VALUES ("ZTK164","SP107","Dexter","Ward","64 Diam Road","Lowhall","O3E 3HO","1979-07-25",2,"M","Student");
