CREATE TABLE Plant (
    category VARCHAR(10),
    plantName VARCHAR(20) NOT NULL,
    variety VARCHAR(20) NOT NULL,
    code VARCHAR(3) NOT NULL,
    referenceID VARCHAR(3) NOT NULL,
    unit INT 
        CHECK(unit >= 0),
    price FLOAT 
        CHECK(price >= 0),
    height VARCHAR(1) 
        CHECK(height IN("S","M","T")),
    PRIMARY KEY (referenceID)
);

INSERT INTO Plant VALUES ("Patio","Eunonymous","Mixed","VY","B07",12,12.50,"S");
INSERT INTO Plant VALUES ("Patio","Hebe","Varigatum","P","B11",1,12.00,"M");
INSERT INTO Plant VALUES ("Patio","Pieris","Carnival","B","B17",1,12.00,"M");
INSERT INTO Plant VALUES ("Patio","Begonia","Cocunut Ice","Y","B21",1,4.50,"S");
INSERT INTO Plant VALUES ("Patio","Begonia","Cocunut Ice","Y","B22",3,9.00,"S");
INSERT INTO Plant VALUES ("Patio","Begonia","Cocunut Ice","Y","B23",9,19.50,"S");
INSERT INTO Plant VALUES ("Patio","Dahlia","Moonfire","B","B24",1,5.50,"M");
INSERT INTO Plant VALUES ("Patio","Carnation","Trailing","RP","B35",5,8.25,"M");
INSERT INTO Plant VALUES ("Patio","Bamboo","Pleioblastus","N","B43",1,6.00,"M");
INSERT INTO Plant VALUES ("Climber","Clematis","Bouchard","P","C02",1,5.00,"T");
INSERT INTO Plant VALUES ("Climber","Rose","Compassion","Y","C11",1,8.00,"T");
INSERT INTO Plant VALUES ("Climber","Vine","Crimson Glory","P","C26",1,10.50,"T");
INSERT INTO Plant VALUES ("Climber","Honeysuckle","Belgica","YP","C51",1,8.25,"M");
INSERT INTO Plant VALUES ("Climber","Jasmin","Winter","YPB","C59",1,7.50,"T");
INSERT INTO Plant VALUES ("Climber","Wisteria","Wonder","B","C64",1,15.00,"T");
INSERT INTO Plant VALUES ("Fruit","Apple","Bramley","G","F17",1,16.50,"T");
INSERT INTO Plant VALUES ("Fruit","Apple","Cox","R","F19",1,16.30,"T");
INSERT INTO Plant VALUES ("Fruit","Apple","Discovery","G","F26",1,16.25,"T");
INSERT INTO Plant VALUES ("Fruit","Cherry","June","R","F31",1,16.00,"T");
INSERT INTO Plant VALUES ("Fruit","Pear","Conference","G","F32",1,16.00,"T");
INSERT INTO Plant VALUES ("Fruit","Plum","Victoria","P","F48",1,16.25,"T");
INSERT INTO Plant VALUES ("Fruit","Peach","Nancy","O","F72",1,16.00,"M");
INSERT INTO Plant VALUES ("Hedge","Berberis","Barberry","Y","H25",5,35.00,"M");
INSERT INTO Plant VALUES ("Hedge","Holly","Common","G","H29",1,50.00,"T");
INSERT INTO Plant VALUES ("Hedge","Bamboo","Blue Zion","B","H59",10,149.00,"T");
INSERT INTO Plant VALUES ("Hedge","Pyracantha","Orat","O","H60",5,30.00,"M");
INSERT INTO Plant VALUES ("Hedge","Dog Wood","Red Doa","R","H64",10,50.00,"T");
INSERT INTO Plant VALUES ("Perennial","Aconitem","Monkshood","B","P24",1,3.00,"M");
INSERT INTO Plant VALUES ("Perennial","Anemone","Pink Star","P","P29",3,8.50,"S");
INSERT INTO Plant VALUES ("Perennial","Astilbe","Regal","WP","P32",1,3.50,"M");
INSERT INTO Plant VALUES ("Perennial","Echinops","Blue Wing","B","P38",1,3.25,"M");
INSERT INTO Plant VALUES ("Perennial","Hosta","Albo","V","P41",1,3.50,"S");
INSERT INTO Plant VALUES ("Perennial","Iris","Sibirica","Y","P42",3,6.00,"M");
INSERT INTO Plant VALUES ("Perennial","Phlox","Edward","RW","P46",1,3.30,"S");
INSERT INTO Plant VALUES ("Shrub","Acer","Purple Mood","P","S08",1,18.00,"T");
INSERT INTO Plant VALUES ("Shrub","Buddleia","White Will","W","S14",1,7.50,"M");
INSERT INTO Plant VALUES ("Shrub","Hebe","Varigata","VR","S21",3,20.50,"S");
INSERT INTO Plant VALUES ("Shrub","Daphne","Purple Haze","P","S38",1,16.50,"S");
INSERT INTO Plant VALUES ("Shrub","Camellia","Sure Red","R","S60",1,13.00,"M");
INSERT INTO Plant VALUES ("Shrub","Hydrangea","Regal","P","S68",1,7.75,"T");
INSERT INTO Plant VALUES ("Shrub","Hydrangea","Elizabeth","B","S69",1,7.00,"T");
INSERT INTO Plant VALUES ("Shrub","Magnolia","Soulang","WP","S73",1,15.00,"M");
INSERT INTO Plant VALUES ("Shrub","Magnolia","Paul","W","S79",1,15.00,"M");
INSERT INTO Plant VALUES ("Shrub","Bay Tree","Standard","G","S81",1,70.00,"M");
INSERT INTO Plant VALUES ("Shrub","Bay Tree","Pyramid","G","S83",1,40.00,"S");
INSERT INTO Plant VALUES ("Fuchsia","Annabel","Erne","W","U17",6,6.95,"S");
INSERT INTO Plant VALUES ("Fuchsia","Darkeyes","Bann","RW","U21",6,6.50,"S");
INSERT INTO Plant VALUES ("Fuchsia","Dancing Flame","Lagan","R","U25",6,6.95,"M");
INSERT INTO Plant VALUES ("Fuchsia","Thalia","Strule","PR","U37",6,6.50,"S");
INSERT INTO Plant VALUES ("Fuchsia","Swingtime","Shimna","PW","U52",6,6.25,"M");
