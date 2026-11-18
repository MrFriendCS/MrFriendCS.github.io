-- H CS 2019 Task 1 Part C - Extension


-- Q1d(i)
SELECT SUM(adultTicket) AS [EH adult tickets]
    FROM Customer,
         Booking
    WHERE postcode LIKE "EH%"
      AND Customer.customerID  = Booking.customerID;


-- Q1d(ii)
SELECT SUM(adultTicket)
     + SUM(childTicket) 
     + SUM(concessionTicket) AS [Total Number of Passengers]
    FROM Booking,
         Flight
    WHERE departureDate LIKE "%04/2018%" 
      AND Booking.flightID = Flight.flightID;


-- Q1d(iii)
SELECT AVG(capacity) AS [Average Capacity on Some Flights]
    FROM Flight,
         Route
    WHERE Flight.routeID = Route.routeID
      AND departFrom LIKE "%N";


-- Q1d(iv)
SELECT town,
       COUNT(*) AS [Total Bookings]
    FROM Customer,
         Booking,
         Flight,
         Route
    WHERE Customer.customerID  = Booking.customerID
      AND Booking.flightID=Flight.flightID
      AND Flight.routeID = Route.routeID
      AND arriveAT = "LHR"
      AND arrivalDate LIKE "%2018"
    GROUP BY town;


-- Q1d(v)
SELECT SUM(adultTicket * 15 + childTicket * 15) AS [Total Case Cost]
    FROM Customer,
         Booking
    WHERE Customer.customerID  = Booking.customerID
      AND forename = "Grant"
      AND surname = "Reid";


-- Q1d(vi)
SELECT forename, surname, 
    SUM(adultTicket * 55 
      + childTicket * 40
      + concessionTicket * 30) AS [Total Fares]
    FROM Customer,
         Booking,
         Flight
    WHERE Customer.customerID = Booking.customerID
      AND Booking.flightID = Flight.flightID
      AND Flight.flightID = "A131T531Y47"
    GROUP BY forename, surname;


-- Q1d(vii)
SELECT forename, surname, 
    Sum(adultTicket*7.5) - SUM(childTicket*5) AS [Tax Difference]
    FROM Customer,
         Booking,
         Flight,
         Route
    WHERE Customer.customerID  = Booking.customerID
      AND Booking.flightID=Flight.flightID
      AND Flight.routeID = Route.routeID
      AND midStopOne = "AMS"
    GROUP BY forename, surname;
