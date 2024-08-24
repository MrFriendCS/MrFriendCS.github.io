-- Don't change lines 1 to 5
.open FlightBooking.db
.headers on
.mode column
-- Don't change lines 1 to 5

.print H CS 2019 Task 1 Part B

.print
.print Q1b(i)
SELECT forename, surname, adultTicket * 5.5 
    + childTicket * 2 
    + concessionTicket * 1.5 AS [Tax (£)]
    FROM booking, customer
    WHERE booking.customerID = "GR01932"
        AND flightID = "QH182"
        AND booking.customerID = customer.customerID;


.print
.print Q1b(ii)
CREATE TEMP VIEW maxKids (maxNumber) AS
    SELECT MAX(childTicket)
        FROM booking;

SELECT forename, surname
    FROM customer, booking, maxKids
    WHERE customer.customerID = booking.customerID
        AND childTicket = maxNumber;

.print
