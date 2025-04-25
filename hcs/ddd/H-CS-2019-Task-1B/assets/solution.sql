-- Title: H CS 2019 Task 1 Part B
-- Author: Mr Friend
-- Date: 30 Jan 2025


-- Q1b(i)
SELECT forename, surname, (adultTicket * 5.5) 
    + (childTicket * 2) 
    + (concessionTicket * 1.5) AS [Tax (£)]
    FROM Customer, Booking
    WHERE Customer.customerID = Booking.customerID
      AND booking.customerID = "GR01932"
      AND flightID = "QH182";


-- Q1b(ii)

-- Find most children
CREATE TEMP VIEW MaxKids (maxNumber) AS
    SELECT MAX(childTicket)
    FROM Booking;

-- Use most children
SELECT forename, surname
    FROM Customer, Booking, MaxKids
    WHERE Customer.customerID = Booking.customerID
      AND childTicket = maxNumber;
