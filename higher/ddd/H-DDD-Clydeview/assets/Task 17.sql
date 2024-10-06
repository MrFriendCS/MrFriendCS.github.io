-- Task 17

-- Q1
SELECT title, hotelName, kmFromAirport, 
        kmFromAirport - 2.8 [New km]
    FROM Hotel, Holiday
    WHERE hotel.hotelRef = Holiday.hotelRef
        AND city = "Madrid";


-- Q2
SELECT hotelName, 
       pricePerNight + 7.25 [ppn+Tax],     
       ROUND((pricePerNight + 7.25) * 1.13, 2) AS [Euros]
    FROM Hotel
    WHERE city = "Rome"
    ORDER BY Euros DESC;


-- Q3
