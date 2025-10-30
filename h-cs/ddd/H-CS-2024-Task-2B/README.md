# H CS 2024 - Task 2 Part B


[Swimming Association database](assets/SwimmingAssociation.db)


___2d___

``` sql
SELECT forename, surname, (quantity*unitPrice*1.2) AS [Total to Pay £]
FROM Customer, Gnome, GnomePurchase, CustOrder
WHERE CustOrder.orderID = "ord0024" 
AND Customer.customerID = CustOrder.customerID 
AND CustOrder.orderID = GnomePurchase.orderID 
AND Gnome.gnomeID = GnomePurchase.gnomeID; 
```