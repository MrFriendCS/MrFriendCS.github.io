CREATE TABLE Prisoner (
    prisonID INT NOT NULL,
    surname VARCHAR(30) NOT NULL
        CHECK (LENGTH(surname) >= 3),
    forename VARCHAR(20) NOT NULL
        CHECK (LENGTH(forename) >= 3),
    hair VARCHAR(6)
        CHECK(hair IN ("Black", "Blond", "Brown", "Grey", "None", "Red", "White")),
    eyes VARCHAR(5)
        CHECK (eyes IN ("Amber", "Black", "Blue", "Brown", "Green", "Hazel", "Grey")),
    height FLOAT NOT NULL
        CHECK (height >= 1.3 AND height <= 2.5),
    conviction VARCHAR(20) NOT NULL,
    open BOOLEAN NOT NULL,
    dob DATE NOT NULL,
    PRIMARY KEY (prisonID)
);

INSERT INTO Prisoner VALUES (1958831,"Irving","Lewis","White","Black",2.39,"Vandalism",True,"1998-11-22");
INSERT INTO Prisoner VALUES (4855253,"MacLean","Ciara","Blond","Amber",1.97,"Extortion",True,"1965-02-01");
INSERT INTO Prisoner VALUES (4168687,"Millar","Shelly","None","Brown",1.83,"Burglary",True,"1993-01-23");
INSERT INTO Prisoner VALUES (3716964,"Clark","Shelly","Grey","Hazel",1.82,"Extortion",False,"2004-10-17");
INSERT INTO Prisoner VALUES (2338713,"Docherty","Shelly","Red","Brown",2.07,"Robbery",True,"1967-04-07");
INSERT INTO Prisoner VALUES (3819083,"Wilson","Angus","White","Green",2.4,"Shoplifting",False,"1962-11-28");
INSERT INTO Prisoner VALUES (3914130,"Davidson","Ruairidh","Red","Amber",1.66,"Cyberbullying",False,"1996-02-21");
INSERT INTO Prisoner VALUES (3596960,"Campbell","Erin","Grey","Hazel",1.64,"Theft",False,"1962-04-12");
INSERT INTO Prisoner VALUES (2869675,"Grant","Stewart","Red","Grey",1.77,"Fraud",False,"1989-10-26");
INSERT INTO Prisoner VALUES (2214496,"Brown","Findlay","White","Green",2.3,"Vandalism",True,"1990-08-01");
INSERT INTO Prisoner VALUES (3904861,"walker","Lewis","Black","Brown",1.71,"Theft",True,"1971-02-14");
INSERT INTO Prisoner VALUES (2539273,"Paterson","Liam","Red","Brown",1.97,"Hacking",True,"1998-07-03");
INSERT INTO Prisoner VALUES (2073258,"Grant","Angus","Black","Hazel",2.14,"Shoplifting",True,"1975-07-10");
INSERT INTO Prisoner VALUES (2520012,"MacLeod","Dominic","Grey","Amber",2.01,"Fraud",False,"1965-10-12");
INSERT INTO Prisoner VALUES (3159109,"Monk","Shelly","Blond","Black",2.1,"Burglary",True,"1966-09-05");
INSERT INTO Prisoner VALUES (2740565,"MacDougall","Ryan","None","Green",2.01,"Theft",True,"1974-10-11");
INSERT INTO Prisoner VALUES (1256309,"MacNeil","Donald","White","Grey",1.53,"Arson",True,"1979-08-16");
INSERT INTO Prisoner VALUES (2159513,"Paterson","Erin","Red","Black",2.32,"Kidnapping",True,"1993-06-18");
INSERT INTO Prisoner VALUES (3001238,"Wilson","Alanna","None","Grey",1.71,"Theft",True,"1983-02-22");
INSERT INTO Prisoner VALUES (3607156,"Millar","Darren","Red","Grey",2.04,"Cyberbullying",False,"1996-06-20");
INSERT INTO Prisoner VALUES (4967731,"Brown","Kieran","Blond","Blue",1.48,"Bribery",False,"1992-04-04");
INSERT INTO Prisoner VALUES (3276029,"Brown","Dominic","Brown","Blue",1.33,"Fraud",True,"1984-11-05");
INSERT INTO Prisoner VALUES (1401125,"Walker","Anthony","Black","Black",2.09,"Extortion",True,"1963-06-07");
INSERT INTO Prisoner VALUES (3824690,"Simpson","Ryan","Brown","Grey",2.47,"Extortion",True,"1978-05-25");
INSERT INTO Prisoner VALUES (4662416,"MacNeil","Domhnall","Red","Amber",1.39,"Drugs",True,"1985-09-30");
INSERT INTO Prisoner VALUES (1913947,"Monk","Vincent","Blond","Hazel",2.0,"Arson",True,"1986-10-03");
INSERT INTO Prisoner VALUES (1117839,"Henderson","James","None","Grey",1.76,"Shoplifting",True,"1975-01-25");
INSERT INTO Prisoner VALUES (4591874,"MacIain","Darren","White","Grey",1.64,"Burglary",True,"1987-09-16");
INSERT INTO Prisoner VALUES (1915684,"MacKinnon","Shelly","Red","Grey",2.36,"Extortion",False,"1967-02-22");
INSERT INTO Prisoner VALUES (1799913,"Robertson","Vincent","White","Green",1.62,"Cyberbullying",False,"1971-11-07");
INSERT INTO Prisoner VALUES (2567504,"Millar","John","Brown","Amber",1.36,"Theft",True,"1969-06-08");
INSERT INTO Prisoner VALUES (4773605,"Small","Simon","Black","Brown",2.08,"Arson",True,"1995-10-08");
INSERT INTO Prisoner VALUES (1382683,"Henderson","Ruairidh","White","Brown",1.31,"Fraud",True,"1979-12-16");
INSERT INTO Prisoner VALUES (1587973,"Henderson","Domhnall","Red","Green",2.05,"Kidnapping",True,"2001-11-04");
INSERT INTO Prisoner VALUES (3192265,"Millar","Miyah","Blond","Amber",2.11,"Kidnapping",True,"1962-05-23");
INSERT INTO Prisoner VALUES (2390756,"Galbraith","Julia","Grey","Green",2.22,"Bribery",True,"1999-05-06");
INSERT INTO Prisoner VALUES (1182841,"Monk","Calum","Grey","Hazel",1.74,"Shoplifting",True,"1971-12-11");
INSERT INTO Prisoner VALUES (1624453,"MacLean","Patrick","Black","Hazel",1.56,"Arson",False,"2003-11-28");
INSERT INTO Prisoner VALUES (3366755,"MacDougall","Kieran","None","Brown",2.29,"Assault",False,"1985-02-16");
INSERT INTO Prisoner VALUES (3169018,"MacLeod","Callum","Red","Black",2.04,"Forgery",True,"1963-02-22");
INSERT INTO Prisoner VALUES (3574571,"Young","Alan","White","Brown",2.18,"Theft",False,"2001-12-16");
INSERT INTO Prisoner VALUES (3898324,"MacArthur","Miyah","White","Grey",1.62,"Vandalism",False,"1985-08-11");
INSERT INTO Prisoner VALUES (4316578,"Campbell","Scott","Grey","Amber",1.59,"Kidnapping",True,"1992-06-09");
INSERT INTO Prisoner VALUES (3027459,"Millar","Ryan","None","Black",1.56,"Bribery",True,"2003-05-12");
INSERT INTO Prisoner VALUES (3094428,"McGuire","Seumas","Blond","Green",1.97,"Burglary",True,"1977-03-05");
INSERT INTO Prisoner VALUES (1339093,"Clark","Wendy","Blond","Black",2.03,"Arson",True,"1974-01-08");
INSERT INTO Prisoner VALUES (1050361,"MacIain","Shelly","None","Blue",1.52,"Vandalism",True,"1965-01-09");
INSERT INTO Prisoner VALUES (3365772,"Henderson","Ruairidh","White","Blue",2.13,"Bribery",False,"1964-03-22");
INSERT INTO Prisoner VALUES (4917580,"Monk","Seumas","Red","Brown",2.39,"Assault",False,"1986-04-25");
INSERT INTO Prisoner VALUES (2180943,"Mitchell","Calum","None","Brown",2.49,"Extortion",True,"2001-09-27");
INSERT INTO Prisoner VALUES (4466569,"Robertson","Julia","Blond","Blue",1.36,"Forgery",False,"1996-10-20");
INSERT INTO Prisoner VALUES (3949995,"Blackie","Domhnall","Red","Black",2.07,"Kidnapping",True,"1974-08-03");
INSERT INTO Prisoner VALUES (3416639,"MacNeil","Ryan","Grey","Black",1.36,"Burglary",False,"1988-09-16");
INSERT INTO Prisoner VALUES (4533736,"Simpson","Erin","Red","Black",1.66,"Theft",False,"1963-02-26");
INSERT INTO Prisoner VALUES (1456418,"Mitchell","Darren","Red","Brown",2.17,"Arson",False,"1989-12-20");
INSERT INTO Prisoner VALUES (1173515,"Blake","Wendy","Blond","Grey",1.3,"Kidnapping",True,"1970-06-13");
INSERT INTO Prisoner VALUES (3826934,"Docherty","John","White","Black",1.38,"Burglary",False,"1963-02-02");
INSERT INTO Prisoner VALUES (2435374,"Small","James","Grey","Brown",2.35,"Burglary",False,"1992-01-12");
INSERT INTO Prisoner VALUES (2545845,"Blackie","Domhnall","White","Grey",2.05,"Robbery",True,"1994-08-04");
INSERT INTO Prisoner VALUES (4949292,"Mitchell","Anthony","Brown","Green",2.24,"Kidnapping",True,"1984-10-19");
INSERT INTO Prisoner VALUES (3445718,"Campbell","Donald","Grey","Brown",2.18,"Theft",True,"1986-02-19");
INSERT INTO Prisoner VALUES (1203821,"Robertson","Ciara","Red","Black",2.09,"Assault",True,"1992-09-25");
INSERT INTO Prisoner VALUES (4220251,"Blackie","Findlay","Grey","Blue",1.61,"Hacking",True,"1974-02-16");
INSERT INTO Prisoner VALUES (1129090,"MacIain","Simon","Blond","Black",1.61,"Drugs",True,"1975-05-09");
INSERT INTO Prisoner VALUES (1434989,"MacIain","Donald","Brown","Black",1.97,"Hacking",True,"1984-09-08");
INSERT INTO Prisoner VALUES (4131743,"Paterson","Callum","Black","Grey",1.76,"Robbery",True,"1990-07-05");
INSERT INTO Prisoner VALUES (4476235,"Brown","Donald","Brown","Grey",2.24,"Shoplifting",True,"1960-08-08");
INSERT INTO Prisoner VALUES (3887321,"Blackie","Shelly","Grey","Grey",1.33,"Extortion",True,"1988-11-30");
INSERT INTO Prisoner VALUES (1077631,"Henderson","Julia","Blond","Brown",2.48,"Forgery",True,"1976-05-14");
INSERT INTO Prisoner VALUES (3705666,"Blackie","Seumas","None","Blue",2.18,"Vandalism",False,"1974-12-03");
INSERT INTO Prisoner VALUES (2162280,"MacArthur","Anthony","Grey","Black",1.56,"Burglary",True,"2000-01-24");
INSERT INTO Prisoner VALUES (3683084,"Small","Ryan","Blond","Hazel",1.89,"Arson",False,"1969-11-24");
INSERT INTO Prisoner VALUES (2316935,"Mitchell","Shelly","Grey","Amber",1.93,"Kidnapping",True,"1969-09-27");
INSERT INTO Prisoner VALUES (2680347,"McGuire","Erin","Brown","Hazel",1.38,"Assault",True,"1964-12-08");
INSERT INTO Prisoner VALUES (4672612,"Wilson","Anthony","Blond","Black",2.05,"Shoplifting",True,"1983-08-06");
INSERT INTO Prisoner VALUES (4123379,"Mitchell","Micheal","None","Hazel",2.35,"Hacking",False,"1967-01-08");
INSERT INTO Prisoner VALUES (2065983,"MacDougall","Stewart","White","Grey",2.27,"Bribery",True,"1970-06-16");
INSERT INTO Prisoner VALUES (3150082,"Stewart","Erin","Red","Blue",1.33,"Bribery",True,"1967-12-15");
INSERT INTO Prisoner VALUES (4925415,"Grant","Ruairidh","White","Amber",1.84,"Forgery",True,"1964-07-22");
INSERT INTO Prisoner VALUES (2108986,"Campbell","Andrew","White","Brown",2.16,"Vandalism",True,"1974-11-18");
INSERT INTO Prisoner VALUES (1695758,"Stewart","Alanna","White","Blue",1.6,"Bribery",False,"1987-10-03");
INSERT INTO Prisoner VALUES (1350209,"Smith","Angus","White","Grey",1.51,"Extortion",False,"1997-02-03");
INSERT INTO Prisoner VALUES (2368418,"Mitchell","Ryan","White","Grey",1.32,"Shoplifting",True,"1986-08-19");
INSERT INTO Prisoner VALUES (4658838,"Small","James","Black","Hazel",2.21,"Shoplifting",False,"1963-12-14");
INSERT INTO Prisoner VALUES (2890975,"Stewart","John","Grey","Blue",1.57,"Robbery",True,"2000-07-27");
INSERT INTO Prisoner VALUES (3621408,"Mitchell","Callum","Brown","Black",2.48,"Burglary",False,"1980-01-28");
INSERT INTO Prisoner VALUES (3108389,"Wilson","Anthony","Grey","Blue",1.94,"Hacking",True,"1962-05-30");
INSERT INTO Prisoner VALUES (1771850,"Monk","Angus","White","Amber",2.5,"Kidnapping",True,"1985-11-30");
INSERT INTO Prisoner VALUES (4915651,"Henderson","Roderick","Blond","Blue",1.5,"Theft",False,"1986-01-06");
INSERT INTO Prisoner VALUES (1792138,"Docherty","Callum","Brown","Black",2.49,"Fraud",True,"1963-11-02");
INSERT INTO Prisoner VALUES (1491844,"Ferguson","Robbie","Blond","Green",2.29,"Cyberbullying",True,"2003-08-28");
INSERT INTO Prisoner VALUES (4237989,"Docherty","Julia","Brown","Amber",1.61,"Robbery",True,"1964-07-24");
INSERT INTO Prisoner VALUES (1885102,"Mitchell","Findlay","None","Black",2.1,"Shoplifting",True,"1960-10-19");
INSERT INTO Prisoner VALUES (1010311,"MacLean","Vincent","White","Amber",2.33,"Robbery",False,"1977-03-13");
INSERT INTO Prisoner VALUES (2822638,"Friend","Callum","Grey","Amber",2.01,"Forgery",True,"1973-02-25");
INSERT INTO Prisoner VALUES (2500482,"Grant","John","Grey","Amber",1.75,"Burglary",False,"1966-08-19");
INSERT INTO Prisoner VALUES (3381257,"Simpson","Shelly","Black","Black",2.41,"Arson",True,"1974-11-27");
INSERT INTO Prisoner VALUES (3936624,"Friend","Vincent","Grey","Blue",2.28,"Kidnapping",True,"1984-07-06");
INSERT INTO Prisoner VALUES (3579257,"MacLean","Alexander","Red","Blue",2.41,"Shoplifting",True,"2003-12-20");
INSERT INTO Prisoner VALUES (2020908,"Henderson","Ruairidh","Blond","Green",2.36,"Drugs",True,"1986-03-30");
INSERT INTO Prisoner VALUES (1011494,"Robertson","Alanna","None","Grey",1.47,"Drugs",True,"1978-10-08");
INSERT INTO Prisoner VALUES (3040976,"MacIain","Callum","Red","Black",2.03,"Arson",True,"1980-04-16");
INSERT INTO Prisoner VALUES (2859814,"Ferguson","Alan","Brown","Brown",1.62,"Arson",True,"1983-04-13");
INSERT INTO Prisoner VALUES (4694286,"Thomson","Ruairidh","White","Hazel",1.92,"Cyberbullying",True,"1999-07-23");
INSERT INTO Prisoner VALUES (2923912,"MacArthur","Alan","Grey","Black",1.9,"Theft",True,"1967-11-18");
INSERT INTO Prisoner VALUES (2972223,"Ferguson","Roderick","Black","Blue",2.34,"Hacking",True,"1981-05-21");
INSERT INTO Prisoner VALUES (4537485,"Monk","Samuel","Brown","Brown",2.0,"Kidnapping",False,"1982-08-25");
INSERT INTO Prisoner VALUES (4628199,"Brown","Julia","Grey","Green",1.35,"Extortion",True,"1976-01-19");
INSERT INTO Prisoner VALUES (1615499,"MacDougall","Simon","Blond","Hazel",2.36,"Burglary",True,"1977-05-28");
INSERT INTO Prisoner VALUES (1053386,"MacKinnon","Roderick","None","Green",2.18,"Arson",False,"1975-05-16");
INSERT INTO Prisoner VALUES (1656890,"Smyth","Calum","White","Grey",1.68,"Burglary",True,"1961-07-05");
INSERT INTO Prisoner VALUES (2476579,"MacArthur","Stewart","None","Black",1.96,"Hacking",True,"1996-04-09");
INSERT INTO Prisoner VALUES (3738566,"MacNeil","Ruairidh","Brown","Brown",2.42,"Shoplifting",False,"1960-04-16");
INSERT INTO Prisoner VALUES (4608294,"Wilson","Stewart","Brown","Brown",2.34,"Fraud",False,"1962-12-25");
INSERT INTO Prisoner VALUES (1395446,"MacLean","Donald","White","Brown",2.09,"Cyberbullying",True,"1962-04-01");
INSERT INTO Prisoner VALUES (1908783,"Smiley","Liam","Red","Black",2.1,"Shoplifting",True,"1985-01-13");
INSERT INTO Prisoner VALUES (1999665,"MacArthur","Micheal","Black","Green",2.13,"Cyberbullying",True,"1995-07-11");
INSERT INTO Prisoner VALUES (4376497,"Small","Vincent","Brown","Blue",1.59,"Bribery",True,"1974-07-17");
INSERT INTO Prisoner VALUES (1679818,"Smith","Wendy","Black","Green",1.87,"Extortion",True,"1977-03-30");
INSERT INTO Prisoner VALUES (3429430,"Galbraith","Seumas","Red","Grey",2.06,"Burglary",True,"1985-09-27");
INSERT INTO Prisoner VALUES (4832628,"Brown","Domhnall","Grey","Black",1.71,"Cyberbullying",True,"1987-04-21");
INSERT INTO Prisoner VALUES (2102132,"Walker","Julia","Brown","Hazel",2.0,"Kidnapping",True,"2000-08-05");
INSERT INTO Prisoner VALUES (4735292,"Monk","John","White","Brown",1.36,"Shoplifting",True,"1984-06-06");
INSERT INTO Prisoner VALUES (1846996,"Millar","Wendy","Blond","Grey",1.55,"Drugs",True,"1993-03-02");
INSERT INTO Prisoner VALUES (1452861,"MacNeil","Craig","Red","Blue",1.43,"Shoplifting",True,"1960-12-15");
INSERT INTO Prisoner VALUES (1067323,"Campbell","Seumas","Grey","Green",1.87,"Assault",True,"1982-11-26");
INSERT INTO Prisoner VALUES (1665766,"Henderson","Shelly","White","Green",2.47,"Fraud",True,"1991-04-30");
INSERT INTO Prisoner VALUES (4320574,"Blackie","John","Blond","Grey",1.4,"Hacking",True,"1984-07-14");
INSERT INTO Prisoner VALUES (3932461,"Smith","Alan","Grey","Grey",2.0,"Kidnapping",False,"1969-11-28");
INSERT INTO Prisoner VALUES (1334908,"MacLean","Julia","Red","Blue",2.17,"Robbery",True,"1986-06-14");
INSERT INTO Prisoner VALUES (1349413,"Smiley","John","Brown","Hazel",1.65,"Fraud",True,"1971-10-05");
INSERT INTO Prisoner VALUES (4315139,"Friend","James","Red","Amber",2.02,"Arson",True,"1976-09-28");
INSERT INTO Prisoner VALUES (2016179,"Docherty","James","Black","Amber",1.34,"Burglary",False,"1991-09-17");
INSERT INTO Prisoner VALUES (1156177,"Smyth","Callum","Blond","Green",1.78,"Fraud",True,"1978-05-23");
INSERT INTO Prisoner VALUES (4313064,"Friend","Ian","Black","Brown",1.61,"Assault",True,"1965-03-26");
INSERT INTO Prisoner VALUES (2620404,"Stewart","Findlay","Grey","Hazel",2.35,"Assault",True,"1994-04-03");
INSERT INTO Prisoner VALUES (1874534,"Clark","Robbie","None","Blue",2.19,"Forgery",True,"1969-10-30");
INSERT INTO Prisoner VALUES (1357739,"Stewart","Miyah","Blond","Black",1.82,"Extortion",True,"1962-10-25");
INSERT INTO Prisoner VALUES (4830358,"Grant","Andrew","Brown","Hazel",1.48,"Drugs",True,"1966-01-29");
INSERT INTO Prisoner VALUES (1648377,"Young","Ciara","Grey","Hazel",1.34,"Forgery",False,"1989-12-21");
INSERT INTO Prisoner VALUES (2771051,"MacNeil","Calum","None","Blue",1.41,"Fraud",False,"1978-05-22");
INSERT INTO Prisoner VALUES (2990919,"Campbell","Dominic","Black","Brown",2.11,"Assault",False,"1978-02-27");
INSERT INTO Prisoner VALUES (2368976,"Millar","Seumas","Red","Hazel",1.85,"Drugs",True,"1984-10-20");
INSERT INTO Prisoner VALUES (4543608,"Friend","John","Blond","Amber",2.25,"Robbery",True,"2004-03-28");
INSERT INTO Prisoner VALUES (4032030,"Young","Calum","Brown","Grey",2.43,"Assault",False,"1979-02-07");
INSERT INTO Prisoner VALUES (1284654,"Irving","Donald","Grey","Amber",1.9,"Burglary",True,"1992-04-20");
INSERT INTO Prisoner VALUES (3403242,"Campbell","Robbie","Red","Amber",2.0,"Hacking",False,"2002-12-19");
INSERT INTO Prisoner VALUES (3390626,"MacDonald","Findlay","Brown","Green",2.06,"Theft",True,"1990-01-15");
INSERT INTO Prisoner VALUES (1979804,"Monk","Calum","Brown","Green",2.4,"Robbery",True,"1981-05-08");
INSERT INTO Prisoner VALUES (1920461,"Stewart","Erin","Black","Hazel",1.95,"Extortion",True,"1964-08-06");
INSERT INTO Prisoner VALUES (4964787,"MacKinnon","Ciara","Red","Amber",2.5,"Extortion",True,"1970-10-23");
INSERT INTO Prisoner VALUES (1133421,"Ferguson","Seumas","Brown","Grey",1.86,"Extortion",False,"1964-12-17");
INSERT INTO Prisoner VALUES (4871288,"Small","Seumas","Grey","Black",1.84,"Theft",False,"1983-09-22");
INSERT INTO Prisoner VALUES (2914626,"Grant","Andrew","Grey","Brown",2.01,"Extortion",False,"1969-05-14");
INSERT INTO Prisoner VALUES (4008151,"Smiley","Angus","None","Black",1.8,"Theft",True,"1965-12-17");
INSERT INTO Prisoner VALUES (2250853,"McGuire","Vincent","Black","Black",2.19,"Kidnapping",True,"1994-04-14");
INSERT INTO Prisoner VALUES (4506983,"Monk","Stewart","Red","Amber",2.07,"Extortion",True,"1971-09-18");
INSERT INTO Prisoner VALUES (4559931,"Smith","Ciara","Red","Amber",2.05,"Bribery",True,"1989-01-13");
INSERT INTO Prisoner VALUES (2577358,"Clark","Findlay","Black","Green",2.27,"Burglary",False,"1991-12-12");
INSERT INTO Prisoner VALUES (2038119,"Friend","Dominic","Grey","Hazel",2.18,"Arson",True,"1991-04-10");
INSERT INTO Prisoner VALUES (4326444,"Galbraith","Darren","Red","Brown",1.69,"Vandalism",True,"1994-01-09");
INSERT INTO Prisoner VALUES (2868958,"MacLean","Ruairidh","Black","Hazel",2.07,"Shoplifting",True,"1990-11-17");
INSERT INTO Prisoner VALUES (3260997,"Galbraith","Erin","Brown","Blue",2.37,"Drugs",False,"1973-05-25");
INSERT INTO Prisoner VALUES (1277908,"Henderson","Ryan","Black","Grey",1.74,"Hacking",False,"1978-03-22");
INSERT INTO Prisoner VALUES (2935440,"Davidson","Stewart","None","Blue",1.91,"Cyberbullying",False,"1989-03-10");
INSERT INTO Prisoner VALUES (1851730,"Stewart","Andrew","Grey","Green",2.36,"Hacking",True,"1990-08-18");
INSERT INTO Prisoner VALUES (2727380,"Blackie","Ruairidh","Blond","Black",2.35,"Hacking",True,"1976-05-16");
INSERT INTO Prisoner VALUES (3777721,"Robertson","John","Red","Brown",1.52,"Theft",False,"2001-11-05");
INSERT INTO Prisoner VALUES (2711838,"Brown","Erin","White","Amber",2.35,"Vandalism",False,"1969-12-10");
INSERT INTO Prisoner VALUES (3624561,"MacDonald","James","Brown","Hazel",2.1,"Assault",False,"1972-05-07");
INSERT INTO Prisoner VALUES (3863568,"Thomson","Stewart","Red","Green",2.0,"Arson",False,"1991-05-30");
INSERT INTO Prisoner VALUES (1845062,"Blake","Ciara","None","Black",1.71,"Fraud",False,"1966-11-15");
INSERT INTO Prisoner VALUES (3540739,"MacDonald","Dominic","Grey","Amber",1.7,"Extortion",False,"1973-04-05");
INSERT INTO Prisoner VALUES (2677974,"Blackie","Lincoln","None","Grey",2.31,"Bribery",False,"1987-11-08");
INSERT INTO Prisoner VALUES (4311353,"Irving","Ciara","Grey","Hazel",1.53,"Drugs",False,"2002-08-05");
INSERT INTO Prisoner VALUES (1862501,"MacKinnon","James","White","Blue",1.52,"Fraud",True,"1973-07-24");
INSERT INTO Prisoner VALUES (4863907,"Grant","Vincent","Blond","Blue",1.88,"Robbery",False,"1962-02-25");
INSERT INTO Prisoner VALUES (3032273,"McGuire","Ryan","Blond","Blue",1.47,"Arson",False,"1961-12-14");
INSERT INTO Prisoner VALUES (2805618,"MacDougall","Anthony","Black","Blue",2.38,"Drugs",False,"1997-09-06");
INSERT INTO Prisoner VALUES (3536446,"Friend","Miyah","White","Blue",1.32,"Shoplifting",True,"1980-06-20");
INSERT INTO Prisoner VALUES (4815925,"Smith","Darren","Brown","Black",1.42,"Arson",False,"1974-11-17");
INSERT INTO Prisoner VALUES (2710551,"Stewart","Darren","Red","Grey",1.65,"Fraud",True,"1988-01-17");
INSERT INTO Prisoner VALUES (1645907,"Smith","Domhnall","Brown","Blue",1.97,"Fraud",True,"1963-04-07");
INSERT INTO Prisoner VALUES (4388330,"Smyth","Erin","Black","Hazel",2.09,"Assault",True,"2002-10-18");
INSERT INTO Prisoner VALUES (2940252,"Smith","Erin","Blond","Amber",1.87,"Shoplifting",True,"1994-02-06");
INSERT INTO Prisoner VALUES (3949146,"Mitchell","Findlay","Brown","Green",2.13,"Assault",True,"1983-05-16");
INSERT INTO Prisoner VALUES (2758947,"Young","Ruairidh","Red","Black",1.36,"Burglary",False,"1976-12-24");
INSERT INTO Prisoner VALUES (1875228,"Campbell","Calum","Red","Hazel",1.42,"Forgery",True,"1969-10-25");
INSERT INTO Prisoner VALUES (4530451,"Small","Liam","Grey","Amber",2.41,"Forgery",False,"1984-07-25");
INSERT INTO Prisoner VALUES (3931059,"MacLeod","Domhnall","Black","Green",1.68,"Assault",False,"1996-05-22");
INSERT INTO Prisoner VALUES (2034750,"McGuire","Julia","Brown","Brown",1.73,"Drugs",False,"1977-01-23");
INSERT INTO Prisoner VALUES (4047944,"Robertson","Angus","Blond","Black",2.47,"Extortion",True,"1998-05-29");
INSERT INTO Prisoner VALUES (4021269,"MacDonald","Dominic","Black","Amber",1.47,"Robbery",True,"1998-06-11");
INSERT INTO Prisoner VALUES (2652954,"Wilson","Miyah","Grey","Grey",2.31,"Assault",True,"2002-05-09");
INSERT INTO Prisoner VALUES (4207671,"Smiley","Alanna","White","Grey",1.37,"Drugs",True,"1987-07-14");
INSERT INTO Prisoner VALUES (1689080,"Paterson","Ciara","Red","Blue",2.49,"Forgery",True,"2002-02-02");
INSERT INTO Prisoner VALUES (1708400,"MacArthur","Michael","Brown","Grey",1.5,"Assault",True,"1996-09-27");
INSERT INTO Prisoner VALUES (3515238,"Brown","Miyah","Red","Green",1.41,"Hacking",True,"1977-09-27");
INSERT INTO Prisoner VALUES (1518463,"Millar","Dominic","Brown","Brown",1.76,"Kidnapping",True,"1973-01-11");
INSERT INTO Prisoner VALUES (1553774,"McGuire","Ryan","Brown","Blue",1.43,"Shoplifting",False,"1966-11-17");
