-- Don't change lines 1 to 5
.open gnomeSales.db
.headers on
.mode column
-- Don't change lines 1 to 5

.print H CS 2023 Task 2B

.print
.print Q2b
SELECT gnomeName, SUM(Quantity) AS [Total gnomes sold]
    FROM Gnome, GnomePurchase
    WHERE Gnome.gnomeID = GnomePurchase.gnomeID
        AND description LIKE "%solar%"
    GROUP BY gnomeName
    ORDER BY [Total gnomes sold] DESC;


.print
.print Q2c
-- Find most expensive
CREATE TEMP VIEW expensive(maximum) AS
    SELECT MAX(unitPrice)
    FROM Gnome;

-- Use most expensive
SELECT emailAddress, CustOrder.orderID, Quantity
    FROM Customer, CustOrder, GnomePurchase, Gnome, expensive
    WHERE Customer.customerID = CustOrder.customerID
        AND CustOrder.orderID = GnomePurchase. orderID
        AND GnomePurchase.gnomeID = Gnome.gnomeID
        AND unitPrice = maximum
        AND quantity >= 3;


.print
.print Q2d
SELECT forename, surname, SUM(quantity*unitPrice*1.2) AS [Total to Pay £]
    FROM Customer, Gnome, GnomePurchase, CustOrder
    WHERE CustOrder.orderID = "ord0024" 
        AND Customer.customerID = CustOrder.customerID 
        AND CustOrder.orderID = GnomePurchase.orderID 
        AND Gnome.gnomeID = GnomePurchase.gnomeID
    GROUP BY forename, surname;


.print