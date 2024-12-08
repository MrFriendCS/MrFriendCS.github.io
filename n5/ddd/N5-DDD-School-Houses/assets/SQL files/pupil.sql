CREATE TABLE Pupil (
    id VARCHAR(10) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    gender VARCHAR(10),
    house VARCHAR(15) NOT NULL,
    year VARCHAR(5) NOT NULL,
    age INT NOT NULL,
    FOREIGN KEY (house)
        REFERENCES House (house),
    PRIMARY KEY (id)
);

INSERT INTO Pupil VALUES ("00-4313836","Chiplen","Manolo","male","Kelvin","S5",17);
INSERT INTO Pupil VALUES ("00-6090755","Coppeard","Christoph","male","Forth","S4",15);
INSERT INTO Pupil VALUES ("00-9337697","Dallewater","Wolfy","male","Clyde","S5",16);
INSERT INTO Pupil VALUES ("01-2484018","Figure","Clevie","male","Clyde","S1",11);
INSERT INTO Pupil VALUES ("01-7816352","McSperrin","Waldemar","male","Kelvin","S2",13);
INSERT INTO Pupil VALUES ("02-0084992","Chaston","Hernando","male","Clyde","S4",15);
INSERT INTO Pupil VALUES ("02-8115904","Landers","Adelaide","female","Forth","S3",14);
INSERT INTO Pupil VALUES ("04-0255383","Braden","Alberto","male","Kelvin","S6",18);
INSERT INTO Pupil VALUES ("05-4846616","Clacey","Martina","female","Clyde","S1",11);
INSERT INTO Pupil VALUES ("05-9935098","Hessenthaler","Mick","male","Clyde","S5",16);
INSERT INTO Pupil VALUES ("06-2733279","Yeliashev","Huey","male","Forth","S5",16);
INSERT INTO Pupil VALUES ("06-3246418","Benard","Konstantine","male","Clyde","S4",16);
INSERT INTO Pupil VALUES ("07-0954678","Kyrkeman","Shell","female","Forth","S5",17);
INSERT INTO Pupil VALUES ("07-2753771","MacGow","Garrard","male","Kelvin","S3",13);
INSERT INTO Pupil VALUES ("07-3324812","Gain","Tedd","male","Forth","S4",16);
INSERT INTO Pupil VALUES ("07-7633787","Ruddlesden","Codie","male","Kelvin","S5",16);
INSERT INTO Pupil VALUES ("08-0150469","Wrigley","Suellen","female","Clyde","S5",17);
INSERT INTO Pupil VALUES ("08-2030480","Cancellieri","Michaela","female","Clyde","S5",16);
INSERT INTO Pupil VALUES ("08-5656627","Rawcliffe","Renaud","male","Clyde","S3",13);
INSERT INTO Pupil VALUES ("08-6263878","Maurice","Juditha","female","Clyde","S5",17);
INSERT INTO Pupil VALUES ("08-8388612","Beaney","Laurella","female","Kelvin","S2",13);
INSERT INTO Pupil VALUES ("10-2909098","Behling","Farlay","male","Forth","S5",17);
INSERT INTO Pupil VALUES ("10-5930088","Bottom","Zacharie","male","Clyde","S6",18);
INSERT INTO Pupil VALUES ("11-0974531","Keough","Shellysheldon","male","Clyde","S5",16);
INSERT INTO Pupil VALUES ("11-3921761","Wray","Johnny","female","Kelvin","S1",12);
INSERT INTO Pupil VALUES ("11-7422016","Beadle","Cris","female","Clyde","S4",16);
INSERT INTO Pupil VALUES ("12-0020068","Gow","Olenolin","male","Kelvin","S2",13);
INSERT INTO Pupil VALUES ("12-8600180","Tireman","Joe","male","Kelvin","S4",15);
INSERT INTO Pupil VALUES ("13-5075359","Hollow","Maribel","female","Forth","S6",17);
INSERT INTO Pupil VALUES ("13-5265635","Wilshin","Haslett","male","Clyde","S5",17);
INSERT INTO Pupil VALUES ("13-7163879","Wells","Mark","male","Forth","S3",14);
INSERT INTO Pupil VALUES ("14-6332302","Domonkos","Stacie","female","Forth","S4",15);
INSERT INTO Pupil VALUES ("15-8308073","Longbottom","Micheal","male","Forth","S4",15);
INSERT INTO Pupil VALUES ("15-9240011","Tumpane","Rickert","male","Forth","S1",11);
INSERT INTO Pupil VALUES ("16-0791956","Maffin","Rolf","male","Forth","S6",17);
INSERT INTO Pupil VALUES ("16-6735362","Haddleston","Cynde","female","Forth","S2",13);
INSERT INTO Pupil VALUES ("17-0944498","Jeenes","Dedra","female","Clyde","S6",17);
INSERT INTO Pupil VALUES ("17-3643364","Gebb","Sherm","male","Forth","S6",17);
INSERT INTO Pupil VALUES ("17-7403628","Domke","Guillermo","male","Forth","S1",12);
INSERT INTO Pupil VALUES ("17-9337331","Langmuir","Ruthann","female","Clyde","S1",12);
INSERT INTO Pupil VALUES ("18-1982835","Dootson","Alanson","male","Clyde","S5",17);
INSERT INTO Pupil VALUES ("18-2454163","Sandes","Mildred","female","Forth","S2",12);
INSERT INTO Pupil VALUES ("19-9185112","Merryweather","Otes","male","Forth","S4",15);
INSERT INTO Pupil VALUES ("20-0912612","Daton","Pooh","male","Kelvin","S5",17);
INSERT INTO Pupil VALUES ("20-6738928","Reith","Geri","female","Clyde","S1",11);
INSERT INTO Pupil VALUES ("20-9951859","McPhee","Alfi","female","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("22-1261316","Jones","Tommy","male","Clyde","S2",12);
INSERT INTO Pupil VALUES ("23-1134759","Beamiss","Stanfield","male","Clyde","S3",14);
INSERT INTO Pupil VALUES ("23-1187973","Lain","Magda","female","Forth","S6",17);
INSERT INTO Pupil VALUES ("24-1459740","Asgodby","Gris","male","Clyde","S1",11);
INSERT INTO Pupil VALUES ("24-9579383","Belvard","Mina","female","Forth","S3",13);
INSERT INTO Pupil VALUES ("26-9342030","Wales","Barry","male","Kelvin","S2",12);
INSERT INTO Pupil VALUES ("27-8163687","Tonsley","Erv","male","Kelvin","S2",12);
INSERT INTO Pupil VALUES ("28-1316730","Skingley","Joe","male","Forth","S6",17);
INSERT INTO Pupil VALUES ("28-1924141","Shipley","Susanetta","female","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("28-3299803","O'Day","Nikolaos","male","Clyde","S2",12);
INSERT INTO Pupil VALUES ("28-7733750","Gainsborough","Vivia","female","Clyde","S5",17);
INSERT INTO Pupil VALUES ("30-2614746","Slowgrave","Nester","male","Kelvin","S6",18);
INSERT INTO Pupil VALUES ("30-7110343","Estevez","Almire","female","Kelvin","S6",17);
INSERT INTO Pupil VALUES ("32-5676941","Andrivot","Dario","male","Clyde","S4",15);
INSERT INTO Pupil VALUES ("33-6201412","Saban","Maris","female","Forth","S1",12);
INSERT INTO Pupil VALUES ("34-3745788","Yonnie","Carmelita","female","Kelvin","S1",12);
INSERT INTO Pupil VALUES ("34-7210692","Nelson","Alexander","male","Clyde","S6",17);
INSERT INTO Pupil VALUES ("34-7649672","Lambrick","Earl","male","Kelvin","S1",12);
INSERT INTO Pupil VALUES ("35-6010805","Austen","Cristionna","female","Clyde","S3",14);
INSERT INTO Pupil VALUES ("35-7218278","Schole","Tiff","female","Forth","S6",17);
INSERT INTO Pupil VALUES ("36-3183071","Gewer","Roselia","female","Clyde","S6",17);
INSERT INTO Pupil VALUES ("36-5086565","Nelson","Ricki","male","Clyde","S2",12);
INSERT INTO Pupil VALUES ("37-7091289","Mival","Deeyn","female","Clyde","S5",16);
INSERT INTO Pupil VALUES ("37-8571578","Bassett","Rinaldo","male","Forth","S6",18);
INSERT INTO Pupil VALUES ("38-0429566","Antonchik","Tanhya","female","Kelvin","S3",13);
INSERT INTO Pupil VALUES ("38-3046886","Jenton","Tab","male","Forth","S1",12);
INSERT INTO Pupil VALUES ("38-3054554","Barry","Ben","male","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("38-5465467","Benda","Alli","female","Forth","S6",17);
INSERT INTO Pupil VALUES ("38-6520204","Shyre","Adriana","female","Clyde","S6",17);
INSERT INTO Pupil VALUES ("39-0200374","Piggrem","Esdras","male","Clyde","S1",12);
INSERT INTO Pupil VALUES ("39-4019866","Tickner","Ulric","male","Forth","S2",12);
INSERT INTO Pupil VALUES ("39-4559182","Tybalt","Timoteo","male","Forth","S5",17);
INSERT INTO Pupil VALUES ("40-1240620","Niece","Georg","male","Kelvin","S2",13);
INSERT INTO Pupil VALUES ("40-9405607","Shipston","Jillane","female","Kelvin","S1",12);
INSERT INTO Pupil VALUES ("41-1773594","Gian","Jackson","male","Kelvin","S6",18);
INSERT INTO Pupil VALUES ("41-6812000","D'Alwis","Linell","female","Forth","S2",12);
INSERT INTO Pupil VALUES ("43-2606558","Rubury","Leticia","female","Kelvin","S5",16);
INSERT INTO Pupil VALUES ("44-4959990","Darrach","Lezley","male","Clyde","S5",16);
INSERT INTO Pupil VALUES ("44-6251776","Perez","Erhart","male","Forth","S6",17);
INSERT INTO Pupil VALUES ("44-8248620","Hurlin","Gary","male","Forth","S3",14);
INSERT INTO Pupil VALUES ("45-9819580","MacAlinden","Ynez","female","Kelvin","S4",16);
INSERT INTO Pupil VALUES ("46-0051994","Mallord","Merilee","female","Kelvin","S2",12);
INSERT INTO Pupil VALUES ("46-0589408","Linkie","Albina","female","Clyde","S6",18);
INSERT INTO Pupil VALUES ("46-9603829","Desbrow","Ave","male","Forth","S6",18);
INSERT INTO Pupil VALUES ("46-9802074","Dubarry","Berty","female","Forth","S2",13);
INSERT INTO Pupil VALUES ("47-0331832","McGurgan","Lind","male","Clyde","S1",12);
INSERT INTO Pupil VALUES ("47-6465315","Arnson","Kendell","male","Clyde","S2",12);
INSERT INTO Pupil VALUES ("48-1005056","Cadamy","Tedra","female","Kelvin","S6",18);
INSERT INTO Pupil VALUES ("48-7922618","Anderson","Dolf","male","Clyde","S5",16);
INSERT INTO Pupil VALUES ("49-1727455","Cullon","Henrieta","female","Clyde","S6",17);
INSERT INTO Pupil VALUES ("49-3603710","Learmount","Jeremy","male","Clyde","S4",15);
INSERT INTO Pupil VALUES ("49-4077709","Blythin","Sascha","male","Kelvin","S5",16);
INSERT INTO Pupil VALUES ("49-4340220","Dufaire","Kathryne","female","Clyde","S3",14);
INSERT INTO Pupil VALUES ("50-7660366","Smith","Corbin","male","Clyde","S6",18);
INSERT INTO Pupil VALUES ("50-9407444","Ovendale","Karlene","female","Clyde","S4",15);
INSERT INTO Pupil VALUES ("51-0281452","Rowsel","Lou","male","Kelvin","S1",12);
INSERT INTO Pupil VALUES ("51-1862459","Skeats","Antonella","female","Forth","S4",16);
INSERT INTO Pupil VALUES ("51-7620480","Sarchwell","Lynnelle","female","Clyde","S2",12);
INSERT INTO Pupil VALUES ("52-8960575","Pearl","Chandler","male","Kelvin","S6",18);
INSERT INTO Pupil VALUES ("53-8183469","O'Noulane","Lira","female","Kelvin","S2",12);
INSERT INTO Pupil VALUES ("55-1197365","Phinnessy","Erda","female","Forth","S1",12);
INSERT INTO Pupil VALUES ("56-5849904","Wilkins","Elene","female","Kelvin","S1",12);
INSERT INTO Pupil VALUES ("57-2010140","Wells","Karen","female","Forth","S3",13);
INSERT INTO Pupil VALUES ("57-9745592","Baume","Monika","female","Kelvin","S4",15);
INSERT INTO Pupil VALUES ("58-0602465","Kennermann","Kingston","male","Kelvin","S4",15);
INSERT INTO Pupil VALUES ("59-4261085","Zahor","Layla","female","Forth","S5",17);
INSERT INTO Pupil VALUES ("60-0571996","Kennington","Tatum","female","Kelvin","S6",18);
INSERT INTO Pupil VALUES ("62-0366584","Currall","Merilyn","female","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("63-0169072","Kesten","Christophorus","male","Kelvin","S1",11);
INSERT INTO Pupil VALUES ("63-6276567","Ricciardelli","Jorie","female","Kelvin","S4",15);
INSERT INTO Pupil VALUES ("63-6348491","Slaymaker","Ewen","male","Clyde","S5",17);
INSERT INTO Pupil VALUES ("63-6887316","Etherington","Ynez","female","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("63-8936584","Whaplington","Alleen","female","Forth","S5",17);
INSERT INTO Pupil VALUES ("66-1476466","Bloxsom","Urban","male","Clyde","S6",17);
INSERT INTO Pupil VALUES ("66-3578748","Petroselli","Pall","male","Kelvin","S6",17);
INSERT INTO Pupil VALUES ("67-3339423","Jones","Edgard","male","Clyde","S6",17);
INSERT INTO Pupil VALUES ("67-4685052","Guerola","Tailor","male","Clyde","S5",16);
INSERT INTO Pupil VALUES ("68-0447666","Alenichev","Sarine","female","Kelvin","S5",17);
INSERT INTO Pupil VALUES ("68-9806462","Beardsley","Jordan","female","Forth","S6",18);
INSERT INTO Pupil VALUES ("69-3638412","Livingston","Baillie","male","Forth","S5",17);
INSERT INTO Pupil VALUES ("70-1997783","Basnett","Ernaline","female","Forth","S4",15);
INSERT INTO Pupil VALUES ("71-5117345","Blare","Jackie","male","Kelvin","S5",17);
INSERT INTO Pupil VALUES ("71-6907647","Jollands","Drucie","female","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("71-7131473","Rolston","Leon","male","Clyde","S3",13);
INSERT INTO Pupil VALUES ("71-9728884","Vales","Gordy","male","Clyde","S5",16);
INSERT INTO Pupil VALUES ("72-7328929","Whiting","Laurel","female","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("73-1311854","Brugsma","Rollin","male","Kelvin","S5",17);
INSERT INTO Pupil VALUES ("73-1497595","Truluck","Mimi","female","Forth","S1",11);
INSERT INTO Pupil VALUES ("73-6025719","Ellicott","Rodina","female","Clyde","S3",13);
INSERT INTO Pupil VALUES ("74-0625258","Smith","Deeanne","female","Forth","S1",12);
INSERT INTO Pupil VALUES ("74-1101464","Smith","Richardo","male","Clyde","S5",16);
INSERT INTO Pupil VALUES ("74-3345043","Elsby","Catharina","female","Forth","S4",15);
INSERT INTO Pupil VALUES ("74-5043777","Pantling","Cele","female","Clyde","S1",11);
INSERT INTO Pupil VALUES ("75-4485382","Swinfon","Haley","female","Clyde","S6",18);
INSERT INTO Pupil VALUES ("76-3208997","Battyll","Alla","female","Clyde","S1",12);
INSERT INTO Pupil VALUES ("76-6499876","Puckrin","Tobi","female","Kelvin","S3",13);
INSERT INTO Pupil VALUES ("76-8442115","Furnell","Mar","male","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("77-0834408","Spaight","Esme","female","Kelvin","S4",15);
INSERT INTO Pupil VALUES ("77-3111088","Grosvenor","Nelia","female","Forth","S6",17);
INSERT INTO Pupil VALUES ("78-8746322","Whoston","Corney","male","Clyde","S3",13);
INSERT INTO Pupil VALUES ("78-9247555","Charte","William","male","Forth","S3",14);
INSERT INTO Pupil VALUES ("79-0457541","Sawfoot","Kacy","female","Forth","S1",12);
INSERT INTO Pupil VALUES ("79-3172798","Brumhead","Anna-diana","female","Forth","S6",17);
INSERT INTO Pupil VALUES ("79-5343198","O'Donoghue","Conrade","male","Forth","S2",12);
INSERT INTO Pupil VALUES ("81-2873562","Savine","Winna","female","Kelvin","S5",17);
INSERT INTO Pupil VALUES ("82-0715390","Mizzi","Hedy","female","Forth","S4",15);
INSERT INTO Pupil VALUES ("82-4017167","Blague","Gallagher","male","Kelvin","S5",16);
INSERT INTO Pupil VALUES ("82-9795460","Hattersley","Mackenzie","male","Clyde","S2",12);
INSERT INTO Pupil VALUES ("84-1722727","Penvarne","Kaylyn","female","Forth","S5",16);
INSERT INTO Pupil VALUES ("84-3695927","Sandes","Farr","male","Forth","S1",11);
INSERT INTO Pupil VALUES ("84-5201964","Dowtry","Ebba","female","Clyde","S2",12);
INSERT INTO Pupil VALUES ("84-5308048","Pracy","Ibrahim","male","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("84-7202192","Durtnel","Martyn","male","Kelvin","S4",15);
INSERT INTO Pupil VALUES ("85-0325355","McCallion","Shawn","male","Kelvin","S4",16);
INSERT INTO Pupil VALUES ("85-9113762","Ranklin","Tracey","male","Clyde","S1",12);
INSERT INTO Pupil VALUES ("86-0126558","Sleath","Laurie","female","Clyde","S2",12);
INSERT INTO Pupil VALUES ("86-9706742","Yushankin","Sophronia","female","Kelvin","S5",17);
INSERT INTO Pupil VALUES ("88-7603718","Jennery","Orella","female","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("89-9295145","Goadbie","Jameson","male","Kelvin","S3",13);
INSERT INTO Pupil VALUES ("90-0378854","Billam","Deva","female","Kelvin","S1",11);
INSERT INTO Pupil VALUES ("90-0425090","Coil","Nora","female","Forth","S4",15);
INSERT INTO Pupil VALUES ("90-5443973","Trobe","Matty","male","Kelvin","S1",12);
INSERT INTO Pupil VALUES ("91-0402846","Demonge","Everett","male","Clyde","S3",13);
INSERT INTO Pupil VALUES ("91-5302871","Grimditch","Moselle","female","Clyde","S5",17);
INSERT INTO Pupil VALUES ("91-7998640","Truelove","Lynnett","female","Forth","S1",11);
INSERT INTO Pupil VALUES ("92-1460753","Full","Fabiano","male","Forth","S4",15);
INSERT INTO Pupil VALUES ("92-3050778","Swan","Adina","female","Clyde","S6",17);
INSERT INTO Pupil VALUES ("93-0089107","Waite","Basia","female","Clyde","S5",16);
INSERT INTO Pupil VALUES ("93-1277430","Surtees","Papagena","female","Clyde","S5",17);
INSERT INTO Pupil VALUES ("93-3021890","Mc Giffin","Felice","female","Kelvin","S3",13);
INSERT INTO Pupil VALUES ("93-5622190","Devlin","Cordy","male","Kelvin","S5",16);
INSERT INTO Pupil VALUES ("93-5901132","Cawdron","Mary","female","Forth","S4",16);
INSERT INTO Pupil VALUES ("93-7279621","Zorer","Peg","female","Kelvin","S4",15);
INSERT INTO Pupil VALUES ("94-5423074","Noell","Othelia","female","Clyde","S5",17);
INSERT INTO Pupil VALUES ("94-5493708","Landsman","Hayley","female","Kelvin","S6",17);
INSERT INTO Pupil VALUES ("94-9789697","Tennison","James","male","Forth","S6",18);
INSERT INTO Pupil VALUES ("95-1547502","Preskett","Godfree","male","Clyde","S5",16);
INSERT INTO Pupil VALUES ("95-6099701","Klamman","Rosette","female","Kelvin","S3",13);
INSERT INTO Pupil VALUES ("95-7218544","Gillan","Caprice","female","Forth","S5",16);
INSERT INTO Pupil VALUES ("96-0212986","McCullouch","Harper","male","Kelvin","S5",16);
INSERT INTO Pupil VALUES ("96-5430621","Sheddan","Pepillo","male","Clyde","S6",17);
INSERT INTO Pupil VALUES ("96-5691536","Blanpein","Suzette","female","Kelvin","S3",14);
INSERT INTO Pupil VALUES ("96-7378194","Dawson","Ernie","male","Forth","S4",16);
INSERT INTO Pupil VALUES ("96-8626181","Laxon","Joyan","female","Kelvin","S1",12);
INSERT INTO Pupil VALUES ("97-7829323","Waistell","Kelly","female","Clyde","S4",16);
INSERT INTO Pupil VALUES ("98-4468812","Durkin","Kendricks","male","Kelvin","S4",16);
INSERT INTO Pupil VALUES ("98-4490975","Brugemann","Stoddard","female","Forth","S1",11);
INSERT INTO Pupil VALUES ("98-6223445","Domino","Elston","male","Clyde","S6",17);
INSERT INTO Pupil VALUES ("98-8883306","Grabert","Robert","female","Forth","S3",14);
INSERT INTO Pupil VALUES ("99-8627839","Ulrik","Corina","female","Kelvin","S6",18);
INSERT INTO Pupil VALUES ("99-9077962","Beeke","Tallia","female","Kelvin","S2",12);
INSERT INTO Pupil VALUES ("99-9288234","Hachard","Augy","male","Forth","S4",16);
