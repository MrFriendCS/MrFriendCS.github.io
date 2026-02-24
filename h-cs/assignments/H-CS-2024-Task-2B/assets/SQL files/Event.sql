CREATE TABLE Event (
    eventID VARCHAR(255) NOT NULL,
    eventDate DATE NOT NULL,
    city VARCHAR(255) NOT NULL,
    venue VARCHAR(255) NOT NULL,
    PRIMARY KEY (eventID)
);


INSERT INTO Event VALUES("Event 1","2024-01-06","Glasgow","Tollcross International Swimming Centre");
INSERT INTO Event VALUES("Event 2","2024-01-13","Leeds","John Charles Centre for Sport");
INSERT INTO Event VALUES("Event 3","2024-01-20","Bangor","Bangor Aurora Aquatic and Leisure Complex");
INSERT INTO Event VALUES("Event 4","2024-01-27","Cardiff","Cardiff International Pool");
