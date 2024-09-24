-- Don't touch lines 1 to 6
.open ClydeviewBlank.db
.headers ON
.mode column
PRAGMA foreign_keys = on;
-- Don't touch lines 1 to 6

DROP TABLE Manufacturer;
DROP TABLE Product;


.print
.print Create Manufacturer table

CREATE TABLE Manufacturer (
    manufacturer_id INT NOT NULL,
    name VARCHAR(30),
    address VARCHAR(50),
    phone VARCHAR(13) NOT NULL
        CHECK (LENGTH(phone) >= 11),
    PRIMARY KEY (manufacturer_id)
);

.print
.print Create Product table

CREATE TABLE Product (
    name VARCHAR(30),
    code VARCHAR(4) NOT NULL,
    no_in_stock INT NOT NULL
        CHECK (no_in_stock >= 0 AND no_in_stock <= 50),
    on_order BOOL NOT NULL,
    price REAL NOT NULL
        CHECK (price > 1.00),
    manufacturer_id INT NOT NULL,
    FOREIGN KEY (manufacturer_id)
        REFERENCES Manufacturer (manufacturer_id),
    PRIMARY KEY (code)
);

.print
.print Display table definitions

SELECT sql
    FROM sqlite_schema
    WHERE tbl_name = "Product"
        OR tbl_name = "Manufacturer";
