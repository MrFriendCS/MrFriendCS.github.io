CREATE TABLE Borrow (
    id INT NOT NULL,
    laptop INT NOT NULL,
    borrowed DATE NOT NULL,
    returned BOOL NOT NULL,
    FOREIGN KEY (id)
        REFERENCES employee (id),
    PRIMARY KEY (id, laptop)
);

INSERT INTO Borrow VALUES (3,1,"2023-10-01",TRUE);
INSERT INTO Borrow VALUES (4,1,"2023-11-30",FALSE);
INSERT INTO Borrow VALUES (3,3,"2023-12-21",FALSE);
