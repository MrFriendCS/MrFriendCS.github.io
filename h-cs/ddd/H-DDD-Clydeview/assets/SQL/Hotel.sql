CREATE TABLE Hotel (
    hotelRef VARCHAR(4) NOT NULL,
    name VARCHAR(30) NOT NULL,
    city VARCHAR(20),
    starRating INT NOT NULL
        CHECK (starRating >= 0 AND starRating <= 5),
    pricePerNight REAL,
    kmFromAirport REAL,
    PRIMARY KEY (hotelRef)
);

INSERT INTO Hotel VALUES ("H101","Catalonia Inn","Barcelona",2,40.00,11.1);
INSERT INTO Hotel VALUES ("H102","Barce Bunkhouse","Barcelona",1,25.00,15.3);
INSERT INTO Hotel VALUES ("H103","Casa Luxor","Barcelona",5,100.00,13.4);
INSERT INTO Hotel VALUES ("H104","Villa Grande","Barcelona",5,95.00,12.7);
INSERT INTO Hotel VALUES ("H105","Catalonia Lux","Barcelona",5,75.00,12.3);
INSERT INTO Hotel VALUES ("H106","Die Wand Hotel","Berlin",4,70.00,14.0);
INSERT INTO Hotel VALUES ("H107","Den Baumkronen","Berlin",1,30.00,15.6);
INSERT INTO Hotel VALUES ("H108","Der Wald","Berlin",3,60.00,16.3);
INSERT INTO Hotel VALUES ("H109","Hotel Tranquilo","Madrid",5,95.00,15.6);
INSERT INTO Hotel VALUES ("H110","Empera","Madrid",3,62.00,14.1);
INSERT INTO Hotel VALUES ("H111","Napolean Ville","Paris",2,48.00,18.3);
INSERT INTO Hotel VALUES ("H112","Maison De Jean","Paris",1,35.00,17.7);
INSERT INTO Hotel VALUES ("H113","Hotel Saint-Jean","Paris",3,59.00,18.0);
INSERT INTO Hotel VALUES ("H114","Champs-Elysees Star Residence","Paris",5,120.00,19.0);
INSERT INTO Hotel VALUES ("H115","Sleepy Inn","London",1,39.00,14.8);
INSERT INTO Hotel VALUES ("H116","Eastern Hotel","London",2,47.00,6.5);
INSERT INTO Hotel VALUES ("H117","The Westroy","London",3,55.00,22.5);
INSERT INTO Hotel VALUES ("H118","Number 9","London",3,58.00,18.5);
INSERT INTO Hotel VALUES ("H119","Tower Turrets","London",5,135.00,17.0);
INSERT INTO Hotel VALUES ("H120","St James House","London",5,120.00,16.0);
INSERT INTO Hotel VALUES ("H121","Hotel Vicori","Rome",4,85.00,34.5);
INSERT INTO Hotel VALUES ("H122","Hotel Fario","Rome",4,80.00,18.6);
INSERT INTO Hotel VALUES ("H123","Hotel Geno","Rome",4,78.00,22.9);
INSERT INTO Hotel VALUES ("H124","Darios","Rome",3,65.00,23.0);
INSERT INTO Hotel VALUES ("H125","Avanti","Rome",2,45.00,26.8);
INSERT INTO Hotel VALUES ("H126","Hotel Evoli","Rome",3,64.00,28.3);
INSERT INTO Hotel VALUES ("H127","Hotel Sereno","Rome",4,82.00,25.4);
INSERT INTO Hotel VALUES ("H128","Paz","Lisbon",3,67.00,10.0);
INSERT INTO Hotel VALUES ("H129","Feriado","Lisbon",3,68.00,12.3);
INSERT INTO Hotel VALUES ("H130","Lisboa Bay","Lisbon",3,62.00,16.0);
INSERT INTO Hotel VALUES ("H131","Lado Colina","Lisbon",2,55.00,25.0);
INSERT INTO Hotel VALUES ("H132","Hotel Caledonia","Edinburgh",3,57.00,14.5);
INSERT INTO Hotel VALUES ("H133","Castle View","Edinburgh",4,65.00,9.8);
INSERT INTO Hotel VALUES ("H134","Princes Hotel","Edinburgh",5,89.00,13.5);
INSERT INTO Hotel VALUES ("H135","The Holyrood","Edinburgh",3,59.00,10.7);
INSERT INTO Hotel VALUES ("H136","Classic Hotel","Edinburgh",4,72.00,12.0);
INSERT INTO Hotel VALUES ("H137","Liffey House","Dublin",3,55.00,13.0);
INSERT INTO Hotel VALUES ("H138","Dublin Apartments","Dublin",1,29.00,14.5);
INSERT INTO Hotel VALUES ("H139","Central Road Hotel","Dublin",3,65.00,10.1);
INSERT INTO Hotel VALUES ("H140","Trinty Towers","Dublin",4,76.00,12.6);
