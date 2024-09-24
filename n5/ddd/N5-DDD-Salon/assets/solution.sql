SELECT Hairdresser.firstname, Hairdresser.lastname, Hairdresser.contactnumber, Client.firstname, Client.lastname, Client.contactnumber
    FROM Hairdresser, Client
    WHERE Hairdresser.hairdresserid = Client.hairdresserid;