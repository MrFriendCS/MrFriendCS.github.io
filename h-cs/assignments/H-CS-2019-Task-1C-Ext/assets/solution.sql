-- Don't change lines 1 to 5
.open FlightBooking.db
.headers on
.mode column
-- Don't change lines 1 to 5


.print H CS 2019 Task 1 Part C - Extension

.print
.print Q1d(i)
SELECT SUM(adultTicket) AS [EH adult tickets]
    FROM Customer, Booking
    WHERE postcode LIKE "EH%"
        AND Customer.customerID  = Booking.customerID;


.print
.print Q1d(ii)
SELECT SUM(adultTicket) + SUM(childTicket) 
    + SUM(concessionTicket) AS [Total Number of Passengers]
    FROM Booking, Flight
    WHERE departureDate LIKE "%04/2018%" 
        AND Booking.flightID = Flight.flightID;


.print
.print Q1d(iii)
SELECT AVG(capacity) AS [Average Capacity on Glasgow Flights]
    FROM Flight, Route
    WHERE Flight.routeID = Route.routeID
        AND departFrom LIKE "%N";


.print
.print Q1d(iv)
SELECT town, COUNT(*) AS [Total Boookings]
    FROM Customer, Booking, Flight, Route
    WHERE Customer.customerID  = Booking.customerID
        AND Booking.flightID=Flight.flightID
        AND Flight.routeID = Route.routeID
        AND arriveAT = "LHR"
        AND arrivalDate LIKE "%2018"
    GROUP BY town;


.print
.print Q1d(v)
SELECT SUM(adultTicket * 15 + childTicket * 15) AS [Total Case Cost]
    FROM Customer, Booking
    WHERE Customer.customerID  = Booking.customerID
        AND forename = "Grant"
        AND surname = "Reid";


.print
.print Q1d(vi)
SELECT forename, surname, 
    SUM(adultTicket * 55 
        + childTicket * 4 
        + concessionTicket * 30) AS [Total Fares]
    FROM Customer, Booking, Flight
    WHERE Customer.customerID = Booking.customerID
        AND Booking.flightID = Flight.flightID
        AND Flight.flightID = "A131T531Y47"
    GROUP BY forename, surname;


.print
.print Q1d(vii)
SELECT forename, surname, 
    Sum(adultTicket*7.5) - SUM(childTicket*5) AS [Tax Difference]
    FROM Customer, Booking, Flight, Route
    WHERE Customer.customerID  = Booking.customerID
        AND Booking.flightID=Flight.flightID
        AND Flight.routeID = Route.routeID
        AND midStopOne = "AMS"
    GROUP BY forename, surname;


.print