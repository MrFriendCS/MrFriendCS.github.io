# N5 CS 2022 Task 2 Part C

ScotAuction sells property in Aberdeen, Dundee, Edinburgh, Glasgow, Inverness, Perth and Stirling.

To register a property for sale, ScotAuction requests the following details from sellers: name, email address, telephone number and home address. ScotAuction gives each seller a unique ID and will contact the seller if an offer is made.

Every property registered for sale must have the following information recorded: house number, street, city, postcode, asking price and estimated property value. ScotAuction generates a unique reference code for all properties. Sellers should also state the number of bedrooms in the property.

A seller can have multiple properties for sale.

A property cannot be listed for sale without the seller’s details being recorded first.

___2c(i)___ The asking price for propertyRef DUN-101 has not been recorded correctly. This should be changed from £105500 to £112000.

Implement an SQL statement that will make the required change to the asking price.

(__2 marks__)

Print evidence of the SQL statement and the Property table, clearly showing that the change has been implemented.


___2c(ii)___ Implement an SQL statement that will add the following details of a new seller to the database. 

<table>
    <tr>
        <td>sellerID:</td>
        <td>1502</td>
    </tr>
    <tr>
        <td>sellerName:</td>
        <td>Eve Grace</td>
    </tr>
    <tr>
        <td>sellerAddress:</td>
        <td>128 Cameron Drive Edinburgh EH4 5DS</td>
    </tr>
    <tr>
        <td>email:</td>
        <td>EveGrace@yehoo.net</td>
    </tr>
    <tr>
        <td>telephoneNumber:</td>
        <td>0131 279100</td>
    </tr>
</table>

(__2 marks__)

_Print evidence of the SQL statement and the Seller table, clearly showing that the change has been implemented._

___(iii)___ ScotAuction is running a workshop to give sellers advice on how to achieve a higher sale price. Due to the limited spaces available, ScotAuction is only inviting selected sellers to attend. 

Implement an SQL statement that will display the seller’s email address and telephone number along with the property’s postcode for properties that have three bedrooms and an asking price of less than £150000.

(__4 marks__)

_Print evidence of the SQL statement and the output._

___2d___ ScotAuction would like a list of seller IDs and asking prices for properties in Glasgow. The list should be sorted showing the lowest price first.

The following incorrect SQL statement is written:

``` sql
SELECT Seller.sellerID, price
FROM Seller, Property
WHERE town = "Glasgow" AND Seller.sellerID = Property.sellerID
ORDER BY askingPrice ASC;
```

Test this SQL statement. 

State two reasons why this SQL statement will not run when implemented.

(__2 marks__)

___2e___ The initial analysis identified the following functional requirements for the database. It should:

* allow ScotAuction to store a seller’s email address and telephone number
* allow sellers to state an estimated value of their property
* record key details about each property, including the address and the number of bedrooms
* limit the value and location of the properties that can be entered

Use the above analysis to evaluate the database in terms of fitness for purpose.

(__1 mark__)