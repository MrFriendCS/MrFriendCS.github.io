CREATE TABLE SuperHero (
    characterID INT NOT NULL,
    name VARCHAR(40),
    role VARCHAR(30),
    mainAbility VARCHAR(30),
    ability2 VARCHAR(30),
    ability3 VARCHAR(30),
    originOfPower VARCHAR(30),
    alterEgo VARCHAR(40),
    PRIMARY KEY (characterID)
);

INSERT INTO SuperHero VALUES (1,"Batman","Super Hero","Martial arts","Gadgets","Acrobatics","Training","Bruce Wayne");
INSERT INTO SuperHero VALUES (2,"Superman","Super Hero","Flight","Super-strength","Super-speed","Alien","Clark Kent");
INSERT INTO SuperHero VALUES (3,"The Hulk","Super Hero","Strength","Regeneration",NULL,"Radiation","Bruce Banner");
INSERT INTO SuperHero VALUES (4,"Wonder Woman","Super Hero","Flight","Super-strength","Super-speed","Magic","Princess Diana of Themyscira");
INSERT INTO SuperHero VALUES (5,"Green Lantern","Super Hero","Flight","Super-strength","Super-speed","Technology","Hal Jordan");
INSERT INTO SuperHero VALUES (6,"Spider-Man","Super Hero","Acrobatics","Martial arts","Super-strength","Radiation","Peter Parker");
INSERT INTO SuperHero VALUES (7,"Captain America","Super Hero","Martial arts","Super-strength",NULL,"Chemicals","Steve Rogers");
INSERT INTO SuperHero VALUES (8,"Iron Man","Super Hero","Flight","Armour","Super-strength","Technology","Tony Stark");
INSERT INTO SuperHero VALUES (9,"Daredevil","Super Hero","Martial arts","Acrobatics",NULL,"Chemicals","Matt Murdock");
INSERT INTO SuperHero VALUES (10,"Judge Dredd","Super Hero","Marksman","Martial arts",NULL,"Training","Joe Dredd");
INSERT INTO SuperHero VALUES (11,"Captain Marvel","Super Hero","Flight","Super-strength","Super-speed","Magic","Billy Batson");
INSERT INTO SuperHero VALUES (12,"Doctor Who","Super Hero","Time travel","Gadgets",NULL,"Alien",NULL);
INSERT INTO SuperHero VALUES (13,"Asterix","Super Hero","Strength","Super-speed",NULL,"Chemicals",NULL);
INSERT INTO SuperHero VALUES (14,"Harry Potter","Super Hero","Magic",NULL,NULL,"Training",NULL);
INSERT INTO SuperHero VALUES (15,"Thor","Super Hero","Strength","Weather control","Flight","Magic","Thor Odinson");
INSERT INTO SuperHero VALUES (16,"Buffy the Vampire Slayer","Super Hero","Strength","Martial arts","Acrobatics","Magic","Buffy Summers");
INSERT INTO SuperHero VALUES (17,"The Joker","Super Villain","Intelligence",NULL,NULL,"Chemicals",NULL);
INSERT INTO SuperHero VALUES (18,"Doctor Doom","Super Villain","Intelligence","Gadgets","Armour","Technology","Victor von Doom");
INSERT INTO SuperHero VALUES (19,"Green Goblin","Super Villain","Strength","Gadgets","Regeneration","Chemicals","Norman Osborn");
INSERT INTO SuperHero VALUES (20,"The Kingpin","Super Villain","Intelligence","Martial arts",NULL,"Training","Wilson Fisk");
INSERT INTO SuperHero VALUES (21,"Magneto","Super Villain","Flight","Telekinesis",NULL,"Mutant powers","Erik Magnus");
INSERT INTO SuperHero VALUES (22,"Lex Luthor","Super Villain","Intelligence","Gadgets",NULL,"Training",NULL);
INSERT INTO SuperHero VALUES (23,"The Penguin","Super Villain","Intelligence","Gadgets",NULL,"Inheritance","Oswald Copperpot");
INSERT INTO SuperHero VALUES (24,"The Riddler","Super Villain","Intelligence",NULL,NULL,"Training","Edward Nigma");
INSERT INTO SuperHero VALUES (25,"Lord Voldemort","Super Villain","Magic",NULL,NULL,"Training","Tom Marvelo Riddle");
INSERT INTO SuperHero VALUES (26,"Loki","Super Villain","Strength","Magic",NULL,"Magic","Loki Laufeyson");
INSERT INTO SuperHero VALUES (27,"Angelis","Super Villain","Strength","Martial arts","Acrobatics","Magic","Angel");
INSERT INTO SuperHero VALUES (28,"Sauron","Super Villain","Mind control","Magic","Intelligence","Magic",NULL);
INSERT INTO SuperHero VALUES (29,"Mastermancer","Team member","Magic","Intelligence",NULL,"Magic",NULL);
INSERT INTO SuperHero VALUES (30,"The Bombadier","Team member","Gadgets","Flight",NULL,"Inheritance",NULL);
INSERT INTO SuperHero VALUES (31,"Minda","Team member","Intelligence","Magic",NULL,"Training",NULL);
INSERT INTO SuperHero VALUES (32,"Fission Woman","Team member","Strength","Electrical Control",NULL,"Radiation",NULL);
INSERT INTO SuperHero VALUES (33,"Turbogal","Team member","Speed","Flight",NULL,"Mutant powers",NULL);
INSERT INTO SuperHero VALUES (34,"Organogirl","Team member","Regeneration","Water breathing",NULL,"Technology",NULL);
INSERT INTO SuperHero VALUES (35,"Snapshot","Team member","Marksman","Strength",NULL,"Chemicals",NULL);
INSERT INTO SuperHero VALUES (36,"Trapezoid","Team member","Acrobatics","Magic",NULL,"Alien",NULL);
INSERT INTO SuperHero VALUES (37,"Knife Edge","Team member","Martial arts","Time travel",NULL,"Training",NULL);
INSERT INTO SuperHero VALUES (38,"The Doorman","Team member","Teleportation","Strength",NULL,"Chemicals",NULL);
INSERT INTO SuperHero VALUES (39,"Psychoman","Team member","Telepathy","Invisibility",NULL,"Alien",NULL);
INSERT INTO SuperHero VALUES (40,"Psipriest","Team member","Telekinesis","Marksman",NULL,"Radiation",NULL);
INSERT INTO SuperHero VALUES (41,"Ember","Team member","Fire control","Magic",NULL,"Magic",NULL);
INSERT INTO SuperHero VALUES (42,"Winterfall","Team member","Ice control","Strength",NULL,"Mutant powers",NULL);
INSERT INTO SuperHero VALUES (43,"Blizzard","Team member","Weather control","Plasticity",NULL,"Technology",NULL);
INSERT INTO SuperHero VALUES (44,"Whale Woman","Team member","Water breathing","Fire control",NULL,"Mutant powers",NULL);
INSERT INTO SuperHero VALUES (45,"Dark Shadow","Team member","Invisibility","Teleportation",NULL,"Chemicals",NULL);
INSERT INTO SuperHero VALUES (46,"Idea","Team member","Mind control","Flight",NULL,"Alien",NULL);
INSERT INTO SuperHero VALUES (47,"Stretcho","Team member","Plasticity","Magic",NULL,"Magic",NULL);
INSERT INTO SuperHero VALUES (48,"Master Wing","Team member","Flight","Gadgets",NULL,"Radiation",NULL);
INSERT INTO SuperHero VALUES (49,"Mistress Falcon","Team member","Animal control","Strength",NULL,"Training",NULL);
INSERT INTO SuperHero VALUES (50,"Tankman","Team member","Armour","Telekinesis",NULL,"Mutant powers",NULL);
INSERT INTO SuperHero VALUES (51,"Oracle","Team member","Precognition","Invisibility",NULL,"Chemicals",NULL);
INSERT INTO SuperHero VALUES (52,"Chronos","Team member","Time travel","Water breathing",NULL,"Technology",NULL);
INSERT INTO SuperHero VALUES (53,"Xenoa","Henchman","Magic","Weather control",NULL,"Training",NULL);
INSERT INTO SuperHero VALUES (54,"Computrace","Henchman","Gadgets","Strength",NULL,"Training",NULL);
INSERT INTO SuperHero VALUES (55,"Black Ice","Henchman","Intelligence","Invisibility",NULL,"Radiation",NULL);
INSERT INTO SuperHero VALUES (56,"The Iron Avenger","Henchman","Strength","Flight",NULL,"Alien",NULL);
INSERT INTO SuperHero VALUES (57,"The Dart","Henchman","Speed","Strength",NULL,"Mutant powers",NULL);
INSERT INTO SuperHero VALUES (58,"Broodborn","Henchman","Regeneration","Teleportation",NULL,"Alien",NULL);
INSERT INTO SuperHero VALUES (59,"Cobalt Assassin","Henchman","Marksman","Ice control",NULL,"Training",NULL);
INSERT INTO SuperHero VALUES (60,"Morax","Henchman","Acrobatics","Gadgets",NULL,"Training",NULL);
INSERT INTO SuperHero VALUES (61,"Agares","Henchman","Martial arts","Strength",NULL,"Mutant powers",NULL);
INSERT INTO SuperHero VALUES (62,"Hellgate","Henchman","Teleportation","Flight",NULL,"Radiation",NULL);
INSERT INTO SuperHero VALUES (63,"Ziminiar","Henchman","Telepathy","Animal control",NULL,"Magic",NULL);
INSERT INTO SuperHero VALUES (64,"Doctor Pseudonym","Henchman","Telekinesis","Strength",NULL,"Mutant powers",NULL);
INSERT INTO SuperHero VALUES (65,"Nucleocinder","Henchman","Fire control","Magic",NULL,"Alien",NULL);
INSERT INTO SuperHero VALUES (66,"Coldsnap","Henchman","Ice control","Flight",NULL,"Chemicals",NULL);
INSERT INTO SuperHero VALUES (67,"The Tempest","Henchman","Weather control","Speed",NULL,"Magic",NULL);
INSERT INTO SuperHero VALUES (68,"Dark Wave","Henchman","Water breathing","Telekinesis",NULL,"Technology",NULL);
INSERT INTO SuperHero VALUES (69,"Knightmare","Henchman","Invisibility","Speed",NULL,"Radiation",NULL);
INSERT INTO SuperHero VALUES (70,"The Minean","Henchman","Mind control","Gadgets",NULL,"Mutant powers",NULL);
INSERT INTO SuperHero VALUES (71,"Wara","Henchman","Plasticity","Strength",NULL,"Magic",NULL);
INSERT INTO SuperHero VALUES (72,"Droidraven","Henchman","Flight","Martial arts",NULL,"Chemicals",NULL);
INSERT INTO SuperHero VALUES (73,"Fang","Henchman","Animal control","Water breathing",NULL,"Technology",NULL);
INSERT INTO SuperHero VALUES (74,"Carapace","Henchman","See Invisibility","Armour",NULL,"Inheritance",NULL);
INSERT INTO SuperHero VALUES (75,"Bloodseer","Henchman","Precognition","Strength",NULL,"Technology",NULL);
INSERT INTO SuperHero VALUES (76,"Titor","Henchman","Time travel","Magic",NULL,"Chemicals",NULL);
