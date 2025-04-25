-- Title: H CS 2023 Task 2 Part B
-- Author: Mr Friend
-- Date: 26 Feb 2025


-- Q2(b)
SELECT gnomeName, SUM(Quantity) AS [Total gnomes sold]
    FROM Gnome, GnomePurchase
    WHERE Gnome.gnomeID = GnomePurchase.gnomeID
        AND description LIKE "%solar%"
    GROUP BY gnomeName
    ORDER BY [Total gnomes sold] DESC;


-- Q2(c)
-- Find most expensive
CREATE TEMP VIEW Expensive(maximum) AS
    SELECT MAX(unitPrice)
    FROM Gnome;

-- Use most expensive
SELECT emailAddress, CustOrder.orderID, Quantity
    FROM Customer, CustOrder, GnomePurchase, Gnome, Expensive
    WHERE Customer.customerID = CustOrder.customerID
        AND CustOrder.orderID = GnomePurchase. orderID
        AND GnomePurchase.gnomeID = Gnome.gnomeID
        AND unitPrice = maximum
        AND quantity >= 3;


-- Q2(d)
SELECT forename, surname, SUM(quantity * unitPrice * 1.2) AS [Total to Pay £]
    FROM Customer, Gnome, GnomePurchase, CustOrder
    WHERE CustOrder.orderID = "ord0024" 
        AND Customer.customerID = CustOrder.customerID 
        AND CustOrder.orderID = GnomePurchase.orderID 
        AND Gnome.gnomeID = GnomePurchase.gnomeID
    GROUP BY forename, surname;
