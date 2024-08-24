.print
.print Task 17

.print
.print Q1
SELECT title, hotelName, kmFromAirport, 
        kmFromAirport - 2.8 [New km]
    FROM Hotel, Holiday
    WHERE hotel.hotelRef = Holiday.hotelRef
        AND city = "Madrid";


.print
.print Q2
SELECT hotelName, 
       pricePerNight + 7.25 [ppn+Tax],     
       ROUND((pricePerNight + 7.25) * 1.13, 2) AS [Euros]
    FROM Hotel
    WHERE city = "Rome"
    ORDER BY Euros DESC;


.print
.print Q3
