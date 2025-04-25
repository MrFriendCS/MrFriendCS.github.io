/*
-- Don't touch lines 1 to 6
.open salonsystem.db
.headers ON
.mode column
PRAGMA foreign_keys = on;
-- Don't touch lines 1 to 6
*/



SELECT Hairdresser.firstname, Hairdresser.lastname, Hairdresser.contactnumber, Client.firstname, Client.lastname, Client.contactnumber
    FROM Hairdresser, Client
    WHERE Hairdresser.hairdresserid = Client.hairdresserid;