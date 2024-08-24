-- Don't change lines 1 to 6
.open Flights.db
.headers on
.mode column
PRAGMA foreign_keys = on;
-- Don't change lines 1 to 6

.print
.print Q1
SELECT *
    FROM Airport
    WHERE code = "GLA";

.print
.print Q2
SELECT *
    FROM Route
    WHERE depCode = "GLA";

.print
.print Q3
SELECT *
    FROM Airport
    WHERE code = "IBZ"
        OR code = "BRU";

.print
.print Q4 - Insert
INSERT INTO Airport
    VALUES ("Barra", "United Kingdom", "BRR", "Europe");

.print
.print Q5
SELECT *
    FROM Airport
    WHERE code = "BRR";

.print
.print Q6 - Insert
INSERT INTO Route
    VALUES (8000, "BRR", "GLA", NULL, NULL);

.print
.print Q6 - Insert
INSERT INTO Route
    VALUES (8001, "GLA", "BRR", NULL, NULL);

.print
.print Q8
SELECT *
    FROM Route
    WHERE routeID = 8000
        OR routeID = 8001;

.print
.print Q9 - Get codes
SELECT *
    FROM Airport
    WHERE name = "Bristol"
        OR name = "Birmingham";

.print
.print Q9 - Insert
INSERT INTO Route
    VALUES (8002, "BRR", "BRS", "GLA", "BHX");

.print
.print Q10 - Insert
INSERT INTO Route
    VALUES (8003, "BRS", "BRR", "BHX", "GLA");

.print
.print Q11
SELECT *
    FROM Route
    WHERE routeID = 8002
        OR routeID = 8003;

.print
.print Q12
SELECT name, code
    FROM Airport
    WHERE country = "Denmark";

.print
.print Q13 - Insert
INSERT INTO Route
    VALUES (8004, "BRR", "BLL", "GLA", NULL);

.print
.print Q14 - Insert
INSERT INTO Route
    VALUES (8005, "BLL", "BRR", "GLA", NULL);

.print
.print Q15
SELECT *
    FROM Route
    WHERE routeID = 8004
        OR routeID = 8005;

.print
.print Q16 - Insert
INSERT INTO Flight
    VALUES ("LM0456", "2024-02-02", "14:55:00", 
        "2024-02-02", "16:05:00", 18, 8000);

.print
.print Q17 - Insert
INSERT INTO Flight
    VALUES ("LM0451", "2024-02-04", "10:15:00", 
        "2024-02-04", "11:30:00", 18, 8001);

.print
.print Q18
SELECT *
    FROM Flight
    WHERE flightID = "LM0456"
        OR flightID = "LM0451"
    ORDER BY depDate ASC;

.print
.print Q19
SELECT flightID, depCode, arrCode, depDate, depTime, arrTime
    FROM Route, Flight
    WHERE Route.routeID = Flight.routeID
        AND (flightID = "LM0451"
        OR flightID = "LM0456")
    ORDER BY depDate ASC;



.print
.print Q24 - Insert
INSERT INTO booking
    VALUES(109423, 2, 3, 0,"GR01976", "LM0456");

.print
.print Q25 - Insert
INSERT INTO booking
    VALUES(109424, 2, 3, 0,"GR01976", "LM0451");

.print
.print Q26
SELECT *
    FROM Booking
    WHERE customerID = "GR01976";

.print
.print Q27
SELECT bookingNo, Flight.flightID, depDate, depTime
    FROM Flight, Booking
    WHERE Flight.flightID = Booking.flightID
        AND customerID = "GR01976";

.print
.print Q28
SELECT bookingNo, Flight.flightID, depCode, depDate, depTime
    FROM Route, Flight, Booking
    WHERE Route.routeID = Flight.routeID
        AND Flight.flightID = Booking.flightID
        AND customerID = "GR01976";

.print
.print Q29
SELECT bookingNo, Flight.flightID, name, depDate, depTime
    FROM Airport, Route, Flight, Booking
    WHERE Airport.code = Route.depCode
        AND Route.routeID = Flight.routeID
        AND Flight.flightID = Booking.flightID
        AND customerID = "GR01976";