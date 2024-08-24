-- Don't change lines 1 to 5
.open Surgery.db
.headers on
.mode column
-- Don't change lines 1 to 5


.print H CS Specimen Task 1 Part B


.print Q1c (i)
SELECT drugID, COUNT(drugID)
    FROM PrescribedDrug
    GROUP BY drugID
    ORDER BY COUNT(drugID) DESC;


.print
.print Q1c (ii) - implemented as a single query
SELECT patientID, datePrescribed
    FROM PrescribedDrug, Drug
    WHERE PrescribedDrug.DrugID = drug.drugID 
        AND dosage = (SELECT MAX(dosage)
    FROM Drug);


.print
.print Q1c (ii) - implemented using a VIEW
CREATE TEMP VIEW HighestDosage (maxDosage) AS
    SELECT max(dosage)
    FROM Drug;


SELECT patientID, datePrescribed
    FROM PrescribedDrug, Drug, HighestDosage
    WHERE PrescribedDrug.drugID = Drug.drugID
        AND Drug.dosage = HighestDosage.maxDosage;


.print
.print Q1d
SELECT forename, surname, patientID
    FROM Patient
    WHERE address LIKE '%EH12%';


.print