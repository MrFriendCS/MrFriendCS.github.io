# H CS 2023 - Task 2 Part B


[Gnome sales database](assets/GnomeSales.db)





___2d___

```
SELECT forename, surname, (quantity*unitPrice*1.2) AS [Total to Pay £]
FROM Customer, Gnome, GnomePurchase, CustOrder
WHERE CustOrder.orderID = "ord0024" 
AND Customer.customerID = CustOrder.customerID 
AND CustOrder.orderID = GnomePurchase.orderID 
AND Gnome.gnomeID = GnomePurchase.gnomeID; 
```