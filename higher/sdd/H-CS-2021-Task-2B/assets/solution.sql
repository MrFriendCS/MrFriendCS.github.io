-- Don't change lines 1 to 5
.open MyTreat.db
.headers on
.mode column
-- Don't change lines 1 to 5

.print H CS 2021 Task 2 Part B

.print
.print Q2c
SELECT firstName, surname, Voucher.voucherID, price£ * quantityPurchased AS [Amount of Money Spent on Voucher]
    FROM Customer, CustomerOrder, Voucher
    WHERE Customer.custID = CustomerOrder.custID
        AND Voucher.voucherID = CustomerOrder.voucherID
        AND category = "Adventure"
        AND voucherName LIKE "%escape room%"
    ORDER BY Voucher.voucherID ASC;


.print
.print Q2d
SELECT Voucher.voucherID, supplierName, voucherName, quantityAvailable - SUM(quantityPurchased) AS [Still Available]
    FROM Voucher, Supplier, CustomerOrder
    WHERE Supplier.supplierCode = Voucher.supplierCode
        AND Voucher.voucherID = CustomerOrder.voucherID
        AND Voucher.voucherID = "V543"
    GROUP BY Voucher.voucherID, supplierName, voucherName;


.print
.print Q2e
SELECT Supplier.supplierName, Voucher.voucherName, Voucher.price£,
        COUNT(*) AS [Number of Customers]
    FROM CustomerOrder, Supplier, Voucher
    WHERE CustomerOrder.voucherID = Voucher.voucherID
        AND Supplier.supplierCode = Voucher.supplierCode
        AND Voucher.price£ < 15
        AND Voucher.category = "Family"
    GROUP BY Supplier.supplierName, Voucher.voucherName, Voucher.price£
    ORDER BY [Number of Customers] DESC;
    

.print
