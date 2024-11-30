CREATE TABLE Game (
    title VARCHAR(30) NOT NULL UNIQUE,
    company VARCHAR(20) NOT NULL,
    genre VARCHAR(15) NOT NULL,
    age INT NOT NULL
        CHECK(age IN (3, 7, 12, 16, 18)),
    price FLOAT NOT NULL
        CHECK(price >= 0 AND price <= 100),
    released DATE NOT NULL
        CHECK(released >= "1970-01-01"),
    copies_sold INT NOT NULL
        CHECK(copies_sold >= 0),
    PRIMARY KEY (title)
    FOREIGN KEY (company)
        REFERENCES company(name)
);

INSERT INTO Game VALUES ("007 - Dr. No","Station Games","Action",7,29.99,"2009-04-24",17792);
INSERT INTO Game VALUES ("6502 Simulator","TB Games","Simulation",16,19.99,"1996-09-04",18000);
INSERT INTO Game VALUES ("Action Biker","StudioArts","Action",7,5.99,"1996-07-28",18390);
INSERT INTO Game VALUES ("Adventure Island","TB Games","Adventure",18,19.99,"2009-08-23",14842);
INSERT INTO Game VALUES ("Aerobic Dance","Victory","Dance",3,14.99,"2012-11-27",15010);
INSERT INTO Game VALUES ("Alchemy","Elite","Action",7,19.99,"2009-03-24",3494);
INSERT INTO Game VALUES ("Alien Attack","Elite","Action",7,14.99,"2008-04-11",7236);
INSERT INTO Game VALUES ("Amusement Park","TB Games","Simulation",12,14.99,"2005-02-03",6477);
INSERT INTO Game VALUES ("Amusement Park - Add on pack","TB Games","Simulation",3,29.99,"2016-02-06",17199);
INSERT INTO Game VALUES ("Armageddon","Station Games","Action",7,7.99,"2008-11-30",14378);
INSERT INTO Game VALUES ("Backgammon","StudioArts","Strategy",18,5.99,"2008-01-27",8364);
INSERT INTO Game VALUES ("BattleChess","TB Games","Strategy",12,14.99,"2016-08-28",6840);
INSERT INTO Game VALUES ("Boxing Fever","Eaglehead Software","Fighting",12,29.99,"2008-07-11",5892);
INSERT INTO Game VALUES ("Breath of Life","Eaglehead Software","Simulation",7,19.99,"1995-10-01",2282);
INSERT INTO Game VALUES ("Cave","Elite","Adventure",18,9.99,"2005-11-13",12243);
INSERT INTO Game VALUES ("Celebrity Come Dancing","StudioArts","Dance",12,19.99,"2004-03-13",9682);
INSERT INTO Game VALUES ("Championship Wrestling","StudioArts","Fighting",16,9.99,"2010-04-13",11464);
INSERT INTO Game VALUES ("Chess 2000","Station Games","Strategy",16,5.99,"2004-02-06",8481);
INSERT INTO Game VALUES ("ChessWorlds","Station Games","Strategy",18,9.99,"2009-08-03",13078);
INSERT INTO Game VALUES ("Dance Revolution","TB Games","Dance",18,29.99,"2014-10-12",12251);
INSERT INTO Game VALUES ("Dancing Queen","Elite","Dance",16,5.99,"2014-08-07",3490);
INSERT INTO Game VALUES ("Dark Star","Victory","Action",7,14.99,"2000-06-07",1158);
INSERT INTO Game VALUES ("Deep Strike","Eaglehead Software","Action",16,29.99,"2010-10-22",15978);
INSERT INTO Game VALUES ("Devil's Revenge","Eaglehead Software","Action",12,34.99,"2017-01-02",3004);
INSERT INTO Game VALUES ("Disco Diva","Eaglehead Software","Dance",18,14.99,"2002-07-20",6126);
INSERT INTO Game VALUES ("Draughts","Elite","Strategy",18,14.99,"2003-01-15",3782);
INSERT INTO Game VALUES ("DynaWarrior","Elite","Fighting",16,9.99,"2010-12-27",11498);
INSERT INTO Game VALUES ("Elite III","TB Games","Adventure",7,14.99,"2009-12-11",15978);
INSERT INTO Game VALUES ("Escape from Alcatraz","Eaglehead Software","Strategy",16,5.99,"2006-11-12",4309);
INSERT INTO Game VALUES ("Fantastic Voyage","Eaglehead Software","Action",7,5.99,"2006-11-01",15076);
INSERT INTO Game VALUES ("Fantastic Voyage - The return","TB Games","Action",12,14.99,"2004-03-16",13842);
INSERT INTO Game VALUES ("Fighter King","TB Games","Fighting",18,14.99,"2016-05-01",5652);
INSERT INTO Game VALUES ("Firefox Down","Elite","Action",18,34.99,"2004-10-11",12432);
INSERT INTO Game VALUES ("Flight Sim - Airbus","Station Games","Simulation",18,5.99,"2015-01-06",7568);
INSERT INTO Game VALUES ("Flight Sim - Combat Mission","Station Games","Simulation",18,19.99,"1999-06-29",10486);
INSERT INTO Game VALUES ("Flight Sim - Mission Iraq","Station Games","Simulation",12,19.99,"2010-04-18",3822);
INSERT INTO Game VALUES ("Flight Sim 2000","Station Games","Simulation",16,19.99,"2008-07-10",9732);
INSERT INTO Game VALUES ("Freestyle Snowboarding","TB Games","Action",12,9.99,"1996-04-24",16068);
INSERT INTO Game VALUES ("Fugitive","Elite","Action",16,29.99,"2016-03-29",7450);
INSERT INTO Game VALUES ("Gedi Wars - Chronicles","StudioArts","Action",7,29.99,"2010-12-28",13792);
INSERT INTO Game VALUES ("Gedi Wars - Galactic Battle","StudioArts","Action",12,9.99,"2012-05-13",7434);
INSERT INTO Game VALUES ("Gedi Wars - I","Eaglehead Software","Action",7,5.99,"2009-06-04",9191);
INSERT INTO Game VALUES ("Gedi Wars - II","Eaglehead Software","Action",18,34.99,"1996-05-10",10914);
INSERT INTO Game VALUES ("Gedi Wars - III","Eaglehead Software","Action",12,5.99,"2005-10-29",6965);
INSERT INTO Game VALUES ("Gedi Wars - IV","Eaglehead Software","Action",18,5.99,"1998-09-01",5156);
INSERT INTO Game VALUES ("Gedi Wars - IX","Eaglehead Software","Action",18,9.99,"2009-12-07",8308);
INSERT INTO Game VALUES ("Gedi Wars - Legend","StudioArts","Action",18,9.99,"2008-11-11",13542);
INSERT INTO Game VALUES ("Gedi Wars - Origins","StudioArts","Action",18,29.99,"2008-09-22",15978);
INSERT INTO Game VALUES ("Gedi Wars - Tactical Supremo","StudioArts","Action",7,14.99,"2011-04-01",17414);
INSERT INTO Game VALUES ("Gedi Wars - The Battle for Alpha Prime","StudioArts","Action",16,19.99,"2005-05-05",11145);
INSERT INTO Game VALUES ("Gedi Wars - V","Eaglehead Software","Action",12,9.99,"1999-03-29",3054);
INSERT INTO Game VALUES ("Gedi Wars - VI","Eaglehead Software","Action",12,19.99,"2015-08-29",9428);
INSERT INTO Game VALUES ("Gedi Wars - VII","Eaglehead Software","Action",12,29.99,"1996-04-24",7008);
INSERT INTO Game VALUES ("Gedi Wars - VIII","Eaglehead Software","Action",16,29.99,"2002-06-11",7941);
INSERT INTO Game VALUES ("Gedi Wars - X","Eaglehead Software","Action",18,9.99,"2003-02-13",15010);
INSERT INTO Game VALUES ("Geoforce Skateboarder","Victory","Simulation",18,9.99,"2001-07-29",15010);
INSERT INTO Game VALUES ("Gettysburg","TB Games","Strategy",18,34.99,"2012-12-29",5834);
INSERT INTO Game VALUES ("Golf - St. Andrews","TB Games","Simulation",18,34.99,"2007-12-31",13285);
INSERT INTO Game VALUES ("Golf - The Masters","TB Games","Simulation",12,9.99,"1995-12-30",18390);
INSERT INTO Game VALUES ("Grand Prix 2000","Victory","Simulation",12,5.99,"1999-11-08",18390);
INSERT INTO Game VALUES ("Grand Prix 2004","StudioArts","Simulation",18,19.99,"2007-11-03",9478);
INSERT INTO Game VALUES ("Incredible Journey","Station Games","Action",16,14.99,"2001-10-30",11618);
INSERT INTO Game VALUES ("International Conspiracy","Eaglehead Software","Action",18,34.99,"2010-07-21",10460);
INSERT INTO Game VALUES ("Invasion Force","StudioArts","Action",7,14.99,"2000-01-10",3454);
INSERT INTO Game VALUES ("Jacko's Party","Victory","Dance",12,29.99,"2006-02-14",6033);
INSERT INTO Game VALUES ("Jujitsu Warriors","StudioArts","Fighting",12,14.99,"2004-05-13",10266);
INSERT INTO Game VALUES ("Kung-Fu","Station Games","Fighting",12,5.99,"2003-09-30",7554);
INSERT INTO Game VALUES ("Kung-Fu Revenge","Eaglehead Software","Fighting",18,9.99,"2003-02-22",5308);
INSERT INTO Game VALUES ("Legend of Karos","Victory","Adventure",7,5.99,"2003-04-23",9205);
INSERT INTO Game VALUES ("LunarBase","Elite","Action",7,5.99,"2007-05-25",15010);
INSERT INTO Game VALUES ("ManicDancer","Victory","Dance",18,5.99,"1995-11-19",15410);
INSERT INTO Game VALUES ("Mat Dance","TB Games","Dance",18,29.99,"1997-02-13",16910);
INSERT INTO Game VALUES ("Mat Dance -","TB Games","Dance",3,9.99,"2011-06-10",7808);
INSERT INTO Game VALUES ("Mat Dance - Competition","TB Games","Dance",18,34.99,"2009-02-18",3975);
INSERT INTO Game VALUES ("Mat Dance Professional","TB Games","Dance",12,19.99,"2004-04-02",10162);
INSERT INTO Game VALUES ("Middle Earth - Conquest","Eaglehead Software","Strategy",7,5.99,"2009-02-06",16144);
INSERT INTO Game VALUES ("Middle Earth - Final Conquest","Eaglehead Software","Strategy",7,34.99,"2014-05-29",8646);
INSERT INTO Game VALUES ("Middle Earth - Magiq","Eaglehead Software","Strategy",12,5.99,"2015-02-21",6202);
INSERT INTO Game VALUES ("Monopoly","Station Games","Strategy",12,29.99,"2014-01-10",3828);
INSERT INTO Game VALUES ("Motor Cycle Sim","Station Games","Simulation",16,34.99,"2005-07-01",12458);
INSERT INTO Game VALUES ("Motorway Tycoon","StudioArts","Simulation",16,19.99,"1999-11-16",10760);
INSERT INTO Game VALUES ("Ocean Race","StudioArts","Action",16,14.99,"2000-04-06",3621);
INSERT INTO Game VALUES ("Omar Sharif's Bridge Tutor","Elite","Strategy",3,34.99,"2004-05-15",3614);
INSERT INTO Game VALUES ("Operation - Nighthawk","TB Games","Action",12,9.99,"2002-05-08",15752);
INSERT INTO Game VALUES ("Operation Genesis","TB Games","Action",12,34.99,"2010-01-26",10988);
INSERT INTO Game VALUES ("Pharoh's Gold","Elite","Adventure",7,34.99,"2013-05-15",15010);
INSERT INTO Game VALUES ("Premiere Football 2000","Victory","Simulation",18,14.99,"1996-05-19",10466);
INSERT INTO Game VALUES ("Premiere Football 2001","Victory","Simulation",18,9.99,"2010-10-16",8479);
INSERT INTO Game VALUES ("Premiere Football 2002","Victory","Simulation",3,5.99,"2017-02-05",12837);
INSERT INTO Game VALUES ("Premiere Football 2003","Victory","Simulation",12,34.99,"2011-11-17",5388);
INSERT INTO Game VALUES ("Premiere Football 2004","Victory","Simulation",3,5.99,"1999-12-04",8788);
INSERT INTO Game VALUES ("Race Track","Elite","Simulation",12,9.99,"2007-12-04",12567);
INSERT INTO Game VALUES ("Reversi","Victory","Strategy",18,29.99,"2015-07-05",18390);
INSERT INTO Game VALUES ("RoboWars","Station Games","Fighting",18,29.99,"2003-01-25",10692);
INSERT INTO Game VALUES ("Run Silent Run Deep","TB Games","Simulation",12,14.99,"1997-07-21",18390);
INSERT INTO Game VALUES ("Scrabble","Eaglehead Software","Strategy",12,5.99,"2011-01-26",16954);
INSERT INTO Game VALUES ("Sentinel","Victory","Action",7,19.99,"2015-09-09",19226);
INSERT INTO Game VALUES ("Sentipede","Station Games","Action",16,29.99,"2002-09-01",14542);
INSERT INTO Game VALUES ("Snowboard Extreme","StudioArts","Simulation",16,29.99,"1999-03-13",16140);
INSERT INTO Game VALUES ("Soft & Cuddly","StudioArts","Action",16,19.99,"2006-01-06",15978);
INSERT INTO Game VALUES ("Space Adventure","Victory","Adventure",7,29.99,"2002-05-04",15010);
INSERT INTO Game VALUES ("Splinter Cell","Station Games","Action",16,34.99,"1999-06-29",2746);
INSERT INTO Game VALUES ("Star Attack","Station Games","Action",12,5.99,"2003-01-09",3225);
INSERT INTO Game VALUES ("Stratagem","TB Games","Strategy",12,19.99,"2014-11-03",17102);
INSERT INTO Game VALUES ("Strategic Conquest","TB Games","Strategy",16,5.99,"2008-12-22",12516);
INSERT INTO Game VALUES ("Strike Fleet","Victory","Adventure",7,19.99,"1998-05-14",15978);
INSERT INTO Game VALUES ("The Eden Project","Station Games","Strategy",16,5.99,"2000-12-19",22852);
INSERT INTO Game VALUES ("The Great Escape","Victory","Adventure",7,19.99,"2014-08-09",14193);
INSERT INTO Game VALUES ("Till the death","TB Games","Fighting",18,5.99,"1997-08-24",13992);
INSERT INTO Game VALUES ("WarGames","Station Games","Fighting",12,5.99,"2006-08-27",4366);
INSERT INTO Game VALUES ("Winter Games","Elite","Sports",16,9.99,"2006-01-10",18502);
INSERT INTO Game VALUES ("World Baseball","Victory","Sports",12,14.99,"1997-10-16",14606);
INSERT INTO Game VALUES ("World Basketball","Victory","Sports",3,9.99,"2001-02-24",13893);
INSERT INTO Game VALUES ("World Cricket","Station Games","Sports",3,14.99,"2015-05-24",1176);
INSERT INTO Game VALUES ("World Football","Eaglehead Software","Sports",3,34.99,"1999-11-22",14529);
INSERT INTO Game VALUES ("World Hockey","StudioArts","Sports",16,19.99,"2009-01-18",8922);
INSERT INTO Game VALUES ("World Tennis","TB Games","Sports",12,19.99,"2010-05-11",18196);
INSERT INTO Game VALUES ("World War II - Tank Battle","StudioArts","Fighting",7,14.99,"2002-07-05",12792);
INSERT INTO Game VALUES ("Wrestlemania","Victory","Fighting",12,5.99,"2005-08-04",2324);
INSERT INTO Game VALUES ("Xenon Prime","StudioArts","Adventure",18,9.99,"1996-05-16",3406);
INSERT INTO Game VALUES ("Zoo","Eaglehead Software","Simulation",16,9.99,"1996-08-15",21198);
