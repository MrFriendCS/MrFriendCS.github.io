

SELECT postcode, name
    FROM Station
    WHERE carWash = TRUE
    ORDER BY postcode ASC,
             name ASC;
