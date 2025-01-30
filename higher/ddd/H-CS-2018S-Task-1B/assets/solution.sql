-- Title: H CS 2018S Task 1 Part B
-- Author: Mr Friend
-- Date: 29 Jan 2025


-- Q1c (i)
SELECT drugID, COUNT(drugID)
    FROM PrescribedDrug
    GROUP BY drugID
    ORDER BY COUNT(drugID) DESC;


-- Q1c (ii)

-- Find highest dosage
CREATE TEMP VIEW HighestDosage (maxDosage) AS
    SELECT MAX(dosage)
    FROM Drug;

-- use highest dosage
SELECT patientID, datePrescribed
    FROM PrescribedDrug, Drug, HighestDosage
    WHERE PrescribedDrug.drugID = Drug.drugID
        AND Drug.dosage = HighestDosage.maxDosage;


-- Q1d
SELECT forename, surname, patientID
    FROM Patient
    WHERE address LIKE '%EH12%';



-- Infor only

-- Q1c (ii) - implemented as a single query
SELECT patientID, datePrescribed
    FROM PrescribedDrug, Drug
    WHERE PrescribedDrug.DrugID = drug.drugID 
        AND dosage = (SELECT MAX(dosage)
    FROM Drug);
