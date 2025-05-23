CREATE TABLE Loan (
    id INT NOT NULL,
    laptop INT NOT NULL,
    borrowed DATE NOT NULL,
    returned BOOL NOT NULL,
    FOREIGN KEY (id)
        REFERENCES employee (id),
    PRIMARY KEY (id, laptop)
);

INSERT INTO Loan VALUES (3,1,"2023-10-01",TRUE);
INSERT INTO Loan VALUES (4,1,"2023-11-30",FALSE);
INSERT INTO Loan VALUES (3,3,"2023-12-21",FALSE);
