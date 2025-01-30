-- Title: N5 CS 2021S Task 1 Part B
-- Author: Mr Friend
-- Date: 30 Jan 2025

-- Q1d
INSERT INTO Employee
VALUES (1599, "Jeremy", "May", "67 Red Lane", "07923782534", "TRUE");

-- Evidence
SELECT *
FROM Employee
WHERE employeeNumber = 1599;


-- Remove employee
DELETE FROM Employee
WHERE employeeNumber = 1599;
