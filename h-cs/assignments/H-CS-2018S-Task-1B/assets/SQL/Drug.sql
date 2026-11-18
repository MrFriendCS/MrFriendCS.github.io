CREATE TABLE Drug (
    drugID VARCHAR(12) NOT NULL,
    drugName VARCHAR(30) NOT NULL,
    manufacturer VARCHAR(30) NOT NULL,
    dosage INT NOT NULL
        CHECK (dosage >= 0),
    cost REAL NOT NULL
        CHECK (cost >= 0.0),
    PRIMARY KEY (drugID)
);

INSERT INTO Drug VALUES ('103BSJGS836S','Enalapril','Alkonovo',250,120);
INSERT INTO Drug VALUES ('104BSHGS350R','Enalapril','Alkonovo',400,140);
INSERT INTO Drug VALUES ('16343SHSAR3D','Ibuprophen','Pharmascotia',600,3.400000095);
INSERT INTO Drug VALUES ('19BHDS239475','Amolodipine','Medione',2000,45);
INSERT INTO Drug VALUES ('20BHDS235723','Amolodipine','Medione',800,30);
INSERT INTO Drug VALUES ('72BSJCJAK468','Aspirin','ASCIICare',350,2.5);
INSERT INTO Drug VALUES ('93763SHSAG3D','Ibuprophen','Pharmascotia',1000,4);
INSERT INTO Drug VALUES ('94HSJ378BSDJS','Ventolin','Javacare',100,12);
INSERT INTO Drug VALUES ('95LSJCVAH864','Aspirin','ASCIICare',500,3.25);
INSERT INTO Drug VALUES ('ADSIJD8244244','Spiriva Handihaler','RPD Biotech',50,78);
INSERT INTO Drug VALUES ('CPSVS700347A','Lantus Solostar','CSS Ceuticals',700,29);
INSERT INTO Drug VALUES ('DSJKDSIOEISBG','Sitaglipton','BioReid',750,800);
INSERT INTO Drug VALUES ('HG2383474SKD','Atorvastatin','Boolean Laboratories',300,40);
INSERT INTO Drug VALUES ('KASJBCBEUIHE2','Metaformin','PseudoPharm',650,32);
INSERT INTO Drug VALUES ('MASJBCBEUI900','Metaformin','PseudoPharm',900,36);
INSERT INTO Drug VALUES ('PAK946120BSV','Budesonaide','CScience Logistics',150,14);
INSERT INTO Drug VALUES ('PHASHVEHSB2','Crestor','SQL Medicare',1500,199);
INSERT INTO Drug VALUES ('PNXVS895347W','Lantus Solostar','CSS Ceuticals',1250,35);
INSERT INTO Drug VALUES ('SAJGSKD048SS','Gliclazide','productPharm',850,67);
INSERT INTO Drug VALUES ('SDAIJD9364534','Spiriva Handihaler','RPD Biotech',1750,158);
