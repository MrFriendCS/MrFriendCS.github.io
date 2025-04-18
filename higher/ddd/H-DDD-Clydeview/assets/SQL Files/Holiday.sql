CREATE TABLE Holiday (
    title VARCHAR(30) NOT NULL,
    destination VARCHAR(30) NOT NULL,
    country VARCHAR(20),
    dateOfDeparture DATE NOT NULL,
    nights INT,
    hotelRef VARCHAR(4),
    FOREIGN KEY (hotelRef)
        REFERENCES Hotel(hotelRef),
    PRIMARY KEY (title)
);

INSERT INTO Holiday VALUES ("Barcelona Pricebuster","Catalonia","Spain","2024-07-12","3","H102");
INSERT INTO Holiday VALUES ("Beautiful Berlin","Berlin","Germany","2024-07-29","4","H108");
INSERT INTO Holiday VALUES ("Budget Dublin","Dublin","Ireland","2024-08-07","2","H138");
INSERT INTO Holiday VALUES ("Capital Spain","Madrid","Spain","2024-07-11","3","H110");
INSERT INTO Holiday VALUES ("Catalonia Caper","Catalonia","Spain","2024-06-24","3","H101");
INSERT INTO Holiday VALUES ("Catalonia Crystal","Catalonia","Spain","2024-06-29","3","H101");
INSERT INTO Holiday VALUES ("Catalonia on a budget","Catalonia","Spain","2024-07-25","3","H102");
INSERT INTO Holiday VALUES ("Dublin Attractions","County Dublin","Ireland","2024-08-07","3","H140");
INSERT INTO Holiday VALUES ("Dublin City Break","Dublin","Ireland","2024-07-31","3","H139");
INSERT INTO Holiday VALUES ("Dublin Package","Dublin","Ireland","2024-08-15","3","H138");
INSERT INTO Holiday VALUES ("Edinburgh City Break","Edinburgh","Scotland","2024-07-12","2","H133");
INSERT INTO Holiday VALUES ("Eternal City","Trastevere-Rome","Italy","2024-07-04","5","H122");
INSERT INTO Holiday VALUES ("France Fantastic","Ile De France","France","2024-08-15","5","H113");
INSERT INTO Holiday VALUES ("French Attractions","Ile De France","France","2024-08-07","4","H112");
INSERT INTO Holiday VALUES ("French Experience","Ile De France","France","2024-07-13","6","H113");
INSERT INTO Holiday VALUES ("Geloland","Windsor","England","2024-07-22","4","H118");
INSERT INTO Holiday VALUES ("Germany Afresh","Brandenburg","Germany","2024-08-11","5","H108");
INSERT INTO Holiday VALUES ("Glorious Paris","Champs �lys�es","France","2024-07-14","4","H114");
INSERT INTO Holiday VALUES ("Glorious Spain","Madrid","Spain","2024-07-13","5","H109");
INSERT INTO Holiday VALUES ("Green Ireland","Dublin Bay","Ireland","2024-08-22","4","H137");
INSERT INTO Holiday VALUES ("Irish Glory","County Dublin","Ireland","2024-08-16","4","H139");
INSERT INTO Holiday VALUES ("Italy Glory","Trastevere-Rome","Italy","2024-07-02","2","H124");
INSERT INTO Holiday VALUES ("Italy Heaven","Lazio","Italy","2024-08-02","4","H121");
INSERT INTO Holiday VALUES ("Italy Luxury","Trastevere-Rome","Italy","2024-07-03","3","H123");
INSERT INTO Holiday VALUES ("Italy Package","Fiumicino","Italy","2024-06-04","5","H125");
INSERT INTO Holiday VALUES ("La vie fran�aise","Ile De France","France","2024-08-02","5","H113");
INSERT INTO Holiday VALUES ("Lisbon Package","Sintra","Portugal","2024-06-12","6","H130");
INSERT INTO Holiday VALUES ("London Attractions","Kensington","England","2024-08-03","2","H115");
INSERT INTO Holiday VALUES ("London Highlights","Kensington","England","2024-07-06","4","H119");
INSERT INTO Holiday VALUES ("London on a budget","Islington","England","2024-07-26","3","H115");
INSERT INTO Holiday VALUES ("London Package","Hammersmith","England","2024-06-30","3","H116");
INSERT INTO Holiday VALUES ("London Traveller","Greenwich","England","2024-08-14","4","H116");
INSERT INTO Holiday VALUES ("Lovely Lisbon","Lisbon","Portugal","2024-06-05","3","H130");
INSERT INTO Holiday VALUES ("Madrid Attractions","Arg�elles","Spain","2024-08-13","5","H109");
INSERT INTO Holiday VALUES ("Madrid City Break","Madrid","Spain","2024-07-02","2","H109");
INSERT INTO Holiday VALUES ("Madrid Summer Madness","Arg�elles","Spain","2024-08-14","7","H110");
INSERT INTO Holiday VALUES ("Old England","Canary Wharf","England","2024-07-19","4","H117");
INSERT INTO Holiday VALUES ("Paris and Surroundings","Ile De France","France","2024-06-30","3","H112");
INSERT INTO Holiday VALUES ("Paris Luxury","Champs �lys�es","France","2024-08-22","2","H114");
INSERT INTO Holiday VALUES ("Paris on a budget","Ile De France","France","2024-07-31","3","H111");
INSERT INTO Holiday VALUES ("Paris Package","Quartier Latin","France","2024-08-01","5","H113");
INSERT INTO Holiday VALUES ("Paris Paradise","Paris","France","2024-06-04","3","H114");
INSERT INTO Holiday VALUES ("Portugal on a budget","Lisbon","Portugal","2024-07-02","2","H131");
INSERT INTO Holiday VALUES ("Portugal Relax","Silver Coast","Portugal","2024-07-19","5","H128");
INSERT INTO Holiday VALUES ("Portugal Sun","Sintra","Portugal","2024-07-19","3","H129");
INSERT INTO Holiday VALUES ("Portugal Tour","Silver Coast","Portugal","2024-06-19","5","H129");
INSERT INTO Holiday VALUES ("Regal London","Canary Wharf","England","2024-07-06","5","H120");
INSERT INTO Holiday VALUES ("Religious Rome","Vatican City","Italy","2024-06-02","4","H127");
INSERT INTO Holiday VALUES ("Roman Route","Lazio","Italy","2024-06-03","4","H126");
INSERT INTO Holiday VALUES ("Romantic Rome","Rome","Italy","2024-07-09","4","H127");
INSERT INTO Holiday VALUES ("Scenic Scotland","East Coast","Scotland","2024-08-19","4","H135");
INSERT INTO Holiday VALUES ("Scotland Attractions","East Coast","Scotland","2024-07-05","5","H133");
INSERT INTO Holiday VALUES ("Scottish Glory","Lothian","Scotland","2024-06-22","4","H132");
INSERT INTO Holiday VALUES ("Scottish Luxury","Edinburgh","Scotland","2024-08-13","4","H134");
INSERT INTO Holiday VALUES ("Scottish Package","Lothian","Scotland","2024-06-29","3","H132");
INSERT INTO Holiday VALUES ("Seven Hills","Lisbon Area","Portugal","2024-07-12","5","H131");
INSERT INTO Holiday VALUES ("Sorbonne Special","Quartier Latin","France","2024-07-13","4","H111");
INSERT INTO Holiday VALUES ("Spanish Beach","Catalonia","Spain","2024-08-04","5","H104");
INSERT INTO Holiday VALUES ("Spanish Luxury","Catalonia","Spain","2024-08-03","3","H103");
INSERT INTO Holiday VALUES ("Spanish Siesta","Madrid","Spain","2024-06-16","5","H109");
INSERT INTO Holiday VALUES ("Spanish Sun","Catalonia","Spain","2024-08-11","5","H104");
INSERT INTO Holiday VALUES ("Tartan Experience","East Coast","Scotland","2024-07-19","4","H136");
INSERT INTO Holiday VALUES ("Theatre Break","London West End","England","2024-08-02","3","H117");
INSERT INTO Holiday VALUES ("Vibrant Paris","Quartier Latin","France","2024-07-29","5","H112");
INSERT INTO Holiday VALUES ("Wimbledon Winner","Wimbledon","England","2024-06-30","6","H120");
