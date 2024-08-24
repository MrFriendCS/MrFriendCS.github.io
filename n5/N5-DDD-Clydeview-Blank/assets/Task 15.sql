-- Don't touch lines 1 to 6
.open ClydeviewBlank.db
.headers ON
.mode column
PRAGMA foreign_keys = on;
-- Don't touch lines 1 to 6

DROP TABLE Owner;
DROP TABLE Pet;


.print
.print Create Owner table

CREATE TABLE Owner (
    owner_id INT NOT NULL,
    first_name VARCHAR(20),
    surname VARCHAR(30),
    address VARCHAR(50),
    town VARCHAR(30),
    contact_phone VARCHAR(13) NOT NULL
        CHECK (LENGTH(contact_phone) >= 11),
    PRIMARY KEY (owner_id)
);

.print
.print Create Owner table

CREATE TABLE Pet (
    pet_code VARCHAR(4) NOT NULL
        CHECK (LENGTH(pet_code) = 5),
    pet_name VARCHAR(20),
    pet_type VARCHAR(10) NOT NULL
        CHECK (pet_type IN ("Cat", "Dog", "Budgie",
                            "Gerbil", "Tortoise")),
    dob DATE,
    vaccine BOOL NOT NULL,
    owner_id INT NOT NULL,
    FOREIGN KEY (owner_id)
        REFERENCES Owner (owner_id),
    PRIMARY KEY (pet_code)
);

.print
.print Display table definitions

SELECT sql
    FROM sqlite_schema
    WHERE tbl_name = "Owner"
        OR tbl_name = "Pet";
