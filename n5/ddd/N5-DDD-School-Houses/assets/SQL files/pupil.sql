CREATE TABLE Pupil (
    id INT NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    houseID INT NOT NULL,
    year VARCHAR(2) NOT NULL
        CHECK (year IN ("S1", "S2", "S3", "S4", "S5", "S6")),
    age INT NOT NULL
        CHECK (age >= 11 AND age <= 18),
    PRIMARY KEY (id),
    FOREIGN KEY (houseID)
        REFERENCES House (id)
);

INSERT INTO Pupil VALUES ("1","MacNeil","Craig","4","S4",13);
INSERT INTO Pupil VALUES ("2","MacLeod","Julia","3","S1",12);
INSERT INTO Pupil VALUES ("3","Friend","Calum","1","S4",15);
INSERT INTO Pupil VALUES ("4","Paterson","Roderick","4","S5",16);
INSERT INTO Pupil VALUES ("5","Docherty","Alexander","4","S6",17);
INSERT INTO Pupil VALUES ("6","Smiley","Patrick","2","S6",17);
INSERT INTO Pupil VALUES ("7","Campbell","Aimee","4","S6",17);
INSERT INTO Pupil VALUES ("8","Ferguson","Aonghas","2","S6",17);
INSERT INTO Pupil VALUES ("9","Irving","Stewart","1","S3",14);
INSERT INTO Pupil VALUES ("10","MacDonald","Aonghas","4","S5",16);
INSERT INTO Pupil VALUES ("11","Smyth","Lewis","2","S6",17);
INSERT INTO Pupil VALUES ("12","Young","Kieran","3","S2",13);
INSERT INTO Pupil VALUES ("13","Robertson","Callum","2","S3",14);
INSERT INTO Pupil VALUES ("14","Walker","Darren","2","S1",12);
INSERT INTO Pupil VALUES ("15","MacLean","Alexander","4","S4",12);
INSERT INTO Pupil VALUES ("16","Walker","India","2","S5",16);
INSERT INTO Pupil VALUES ("17","Davidson","India","3","S5",16);
INSERT INTO Pupil VALUES ("18","Small","Domhnall","1","S2",13);
INSERT INTO Pupil VALUES ("19","Small","Jamie","4","S1",12);
INSERT INTO Pupil VALUES ("20","Clark","Stewart","3","S3",14);
INSERT INTO Pupil VALUES ("21","MacLean","Patrick","4","S5",15);
INSERT INTO Pupil VALUES ("22","Galbraith","Seonaidh","1","S4",15);
INSERT INTO Pupil VALUES ("23","MacNeil","Aonghas","2","S5",16);
INSERT INTO Pupil VALUES ("24","Millar","Maddison","3","S6",17);
INSERT INTO Pupil VALUES ("25","Wilson","Simon","2","S4",15);
INSERT INTO Pupil VALUES ("26","Nicholson","Patrick","2","S5",16);
INSERT INTO Pupil VALUES ("27","Davidson","Anthony","3","S2",13);
INSERT INTO Pupil VALUES ("28","Ferguson","Robbie","4","S6",17);
INSERT INTO Pupil VALUES ("29","Smith","Rowan","3","S4",15);
INSERT INTO Pupil VALUES ("30","MacIain","Mason","3","S2",13);
INSERT INTO Pupil VALUES ("31","McIntyre","Maddison","2","S3",14);
INSERT INTO Pupil VALUES ("32","Kearney","Miyah","1","S2",13);
INSERT INTO Pupil VALUES ("33","Irving","Ryan","1","S2",13);
INSERT INTO Pupil VALUES ("34","MacDonald","Caitlin","3","S5",16);
INSERT INTO Pupil VALUES ("35","Monk","Samuel","4","S4",12);
INSERT INTO Pupil VALUES ("36","Thomson","Ethan","2","S5",16);
INSERT INTO Pupil VALUES ("37","Galbraith","Ian","2","S2",13);
INSERT INTO Pupil VALUES ("38","Simpson","Innes","1","S3",14);
INSERT INTO Pupil VALUES ("39","Brown","Rowan","3","S5",16);
INSERT INTO Pupil VALUES ("40","Daly","Mairi","3","S4",15);
INSERT INTO Pupil VALUES ("41","Smiley","Caitlin","3","S2",13);
INSERT INTO Pupil VALUES ("42","MacIain","Callum","4","S4",15);
INSERT INTO Pupil VALUES ("43","Friend","Robbie","3","S1",12);
INSERT INTO Pupil VALUES ("44","Henderson","Andrew","4","S5",16);
INSERT INTO Pupil VALUES ("45","MacKinnon","Roderick","3","S5",16);
INSERT INTO Pupil VALUES ("46","Blake","Oliver","1","S1",12);
INSERT INTO Pupil VALUES ("47","Johnson","James","4","S4",15);
INSERT INTO Pupil VALUES ("48","Grant","Thomas","3","S5",16);
INSERT INTO Pupil VALUES ("49","Mitchell","India","4","S4",15);
INSERT INTO Pupil VALUES ("50","Docherty","Ethan","2","S4",15);
INSERT INTO Pupil VALUES ("51","Kearney","Shelly","1","S2",13);
INSERT INTO Pupil VALUES ("52","MacKinnon","Ruairidh","4","S1",12);
INSERT INTO Pupil VALUES ("53","Mitchell","Ava","2","S5",16);
INSERT INTO Pupil VALUES ("54","Daly","Calum","1","S2",13);
INSERT INTO Pupil VALUES ("55","Galbraith","Mairi","2","S5",16);
INSERT INTO Pupil VALUES ("56","Brown","Andrew","3","S3",14);
INSERT INTO Pupil VALUES ("57","McGuire","India","1","S4",15);
INSERT INTO Pupil VALUES ("58","MacIain","Shelly","3","S1",12);
INSERT INTO Pupil VALUES ("59","Campbell","Micheal","3","S3",14);
INSERT INTO Pupil VALUES ("60","Johnson","Ross","2","S6",17);
INSERT INTO Pupil VALUES ("61","Irving","Lewis","4","S4",15);
INSERT INTO Pupil VALUES ("62","Simpson","Oliver","4","S4",15);
INSERT INTO Pupil VALUES ("63","MacArthur","Michael","4","S4",14);
INSERT INTO Pupil VALUES ("64","Ferguson","Callum","4","S4",15);
INSERT INTO Pupil VALUES ("65","Docherty","Alan","4","S3",14);
INSERT INTO Pupil VALUES ("66","Henderson","Calum","4","S5",16);
INSERT INTO Pupil VALUES ("67","MacNeil","Miyah","2","S6",17);
INSERT INTO Pupil VALUES ("68","Irving","Craig","2","S1",12);
INSERT INTO Pupil VALUES ("69","Smiley","Simon","1","S2",13);
INSERT INTO Pupil VALUES ("70","Wilson","Erin","4","S6",17);
INSERT INTO Pupil VALUES ("71","MacKinnon","Angus","4","S6",17);
INSERT INTO Pupil VALUES ("72","Irving","Rowan","4","S4",15);
INSERT INTO Pupil VALUES ("73","Blackie","Lincoln","4","S4",14);
INSERT INTO Pupil VALUES ("74","Campbell","Craig","2","S5",16);
INSERT INTO Pupil VALUES ("75","Brown","John","3","S1",12);
INSERT INTO Pupil VALUES ("76","MacArthur","Innes","4","S3",14);
INSERT INTO Pupil VALUES ("77","Robertson","James","3","S6",17);
INSERT INTO Pupil VALUES ("78","Robertson","Robbie","1","S6",17);
INSERT INTO Pupil VALUES ("79","Blake","Ava","3","S4",15);
INSERT INTO Pupil VALUES ("80","MacDonald","Aonghas","1","S5",16);
INSERT INTO Pupil VALUES ("81","Nicholson","Innes","4","S4",15);
INSERT INTO Pupil VALUES ("82","Friend","Ian","4","S4",15);
INSERT INTO Pupil VALUES ("83","MacArthur","Alanna","1","S1",12);
INSERT INTO Pupil VALUES ("84","Johnson","Ross","2","S6",17);
INSERT INTO Pupil VALUES ("85","Daly","Oliver","3","S4",15);
INSERT INTO Pupil VALUES ("86","MacDougall","Oliver","1","S6",17);
INSERT INTO Pupil VALUES ("87","Blackie","Innes","2","S5",16);
INSERT INTO Pupil VALUES ("88","Daly","Dominic","3","S5",16);
INSERT INTO Pupil VALUES ("89","Henderson","Niamh","1","S3",14);
INSERT INTO Pupil VALUES ("90","Blake","Stewart","2","S1",12);
INSERT INTO Pupil VALUES ("91","Smyth","James","3","S6",17);
INSERT INTO Pupil VALUES ("92","Nicholson","Ian","2","S4",15);
INSERT INTO Pupil VALUES ("93","Holby","Sally","4","S4",11);
INSERT INTO Pupil VALUES ("94","Ferguson","Julia","1","S3",14);
INSERT INTO Pupil VALUES ("95","Clark","Aonghas","3","S3",14);
INSERT INTO Pupil VALUES ("96","Young","Jamie","1","S5",16);
INSERT INTO Pupil VALUES ("97","Blake","Simon","1","S2",13);
INSERT INTO Pupil VALUES ("98","Millar","Oliver","3","S2",13);
INSERT INTO Pupil VALUES ("99","MacNeil","Sophie","2","S2",13);
INSERT INTO Pupil VALUES ("100","Kearney","Rachel","4","S5",16);
INSERT INTO Pupil VALUES ("101","Grant","Caralisa","3","S4",15);
INSERT INTO Pupil VALUES ("102","Grant","Alexander","3","S5",16);
INSERT INTO Pupil VALUES ("103","Smith","Aonghas","1","S5",16);
INSERT INTO Pupil VALUES ("104","Thomson","Mairi","2","S2",13);
INSERT INTO Pupil VALUES ("105","Ferguson","Dominic","2","S4",15);
INSERT INTO Pupil VALUES ("106","Boyd","Roderick","2","S3",14);
INSERT INTO Pupil VALUES ("107","Blackie","Rowan","4","S6",17);
INSERT INTO Pupil VALUES ("108","Galbraith","Domhnall","4","S1",12);
INSERT INTO Pupil VALUES ("109","Jones","Simon","3","S3",14);
INSERT INTO Pupil VALUES ("110","Thomson","Lincoln","3","S6",17);
INSERT INTO Pupil VALUES ("111","MacIsaac","Craig","2","S4",15);
INSERT INTO Pupil VALUES ("112","MacDougall","Anthony","4","S3",14);
INSERT INTO Pupil VALUES ("113","Galbraith","John","2","S4",15);
INSERT INTO Pupil VALUES ("114","Thomson","Liam","4","S4",15);
INSERT INTO Pupil VALUES ("115","MacArthur","Ross","1","S6",17);
INSERT INTO Pupil VALUES ("116","Mitchell","Liam","4","S6",17);
INSERT INTO Pupil VALUES ("117","Docherty","Lacey","3","S4",15);
INSERT INTO Pupil VALUES ("118","Thomson","Micheal","3","S4",15);
INSERT INTO Pupil VALUES ("119","Stewart","Andrew","3","S4",15);
INSERT INTO Pupil VALUES ("120","Wilson","Innes","1","S6",17);
INSERT INTO Pupil VALUES ("121","MacIsaac","Mairi","2","S4",15);
INSERT INTO Pupil VALUES ("122","Campbell","Robbie","4","S4",16);
INSERT INTO Pupil VALUES ("123","Daly","Thomas","4","S3",14);
INSERT INTO Pupil VALUES ("124","Henderson","Ruairidh","1","S5",16);
INSERT INTO Pupil VALUES ("125","Millar","Oliver","4","S4",15);
INSERT INTO Pupil VALUES ("126","Walker","Domhnall","1","S3",14);
INSERT INTO Pupil VALUES ("127","Docherty","Angus","4","S5",16);
INSERT INTO Pupil VALUES ("128","Young","Maddison","4","S6",17);
INSERT INTO Pupil VALUES ("129","Friend","Jamie","3","S4",15);
INSERT INTO Pupil VALUES ("130","MacDonald","Sophie","1","S6",17);
INSERT INTO Pupil VALUES ("131","Blake","Alanna","2","S3",14);
INSERT INTO Pupil VALUES ("132","Friend","James","2","S3",14);
INSERT INTO Pupil VALUES ("133","Stewart","Anthony","1","S5",16);
INSERT INTO Pupil VALUES ("134","Robertson","Iain","2","S4",15);
INSERT INTO Pupil VALUES ("135","MacLeod","Ross","4","S5",16);
INSERT INTO Pupil VALUES ("136","Boyd","Craig","3","S3",14);
INSERT INTO Pupil VALUES ("137","MacLean","Lacey","1","S5",16);
INSERT INTO Pupil VALUES ("138","Walker","Mairi","2","S5",16);
INSERT INTO Pupil VALUES ("139","MacKinnon","Anthony","1","S3",14);
INSERT INTO Pupil VALUES ("140","Robertson","Seumas","1","S4",15);
INSERT INTO Pupil VALUES ("141","Kearney","Calum","3","S4",15);
INSERT INTO Pupil VALUES ("142","Small","Ross","3","S2",13);
INSERT INTO Pupil VALUES ("143","Simpson","Stewart","4","S4",15);
INSERT INTO Pupil VALUES ("144","MacIsaac","Erin","4","S5",16);
INSERT INTO Pupil VALUES ("145","Grant","Rachel","3","S4",15);
INSERT INTO Pupil VALUES ("146","Brown","Mason","2","S3",14);
INSERT INTO Pupil VALUES ("147","Nicholson","Robbie","4","S2",13);
INSERT INTO Pupil VALUES ("148","Irving","Maddison","2","S4",15);
INSERT INTO Pupil VALUES ("149","Henderson","Ian","4","S2",13);
INSERT INTO Pupil VALUES ("150","Kearney","Ciara","3","S5",16);
INSERT INTO Pupil VALUES ("151","Henderson","Alexander","3","S2",13);
INSERT INTO Pupil VALUES ("152","Boyd","Domhnall","3","S5",16);
INSERT INTO Pupil VALUES ("153","Campbell","Patrick","2","S5",16);
INSERT INTO Pupil VALUES ("154","Ferguson","Seonaidh","4","S1",12);
INSERT INTO Pupil VALUES ("155","McGuire","Alanna","2","S1",12);
INSERT INTO Pupil VALUES ("156","Smyth","James","4","S5",16);
INSERT INTO Pupil VALUES ("157","Mitchell","Ross","4","S3",14);
INSERT INTO Pupil VALUES ("158","Monk","Findlay","3","S4",15);
INSERT INTO Pupil VALUES ("159","MacIain","Wendy","2","S1",12);
INSERT INTO Pupil VALUES ("160","Daly","Ava","3","S2",13);
INSERT INTO Pupil VALUES ("161","Monk","Innes","4","S2",13);
INSERT INTO Pupil VALUES ("162","Irving","Alexander","4","S5",16);
INSERT INTO Pupil VALUES ("163","Docherty","Aonghas","3","S5",16);
INSERT INTO Pupil VALUES ("164","Brown","Miyah","1","S4",15);
INSERT INTO Pupil VALUES ("165","Walker","Erin","2","S6",17);
INSERT INTO Pupil VALUES ("166","Johnson","Ian","3","S3",14);
INSERT INTO Pupil VALUES ("167","Clark","Mairi","3","S2",13);
INSERT INTO Pupil VALUES ("168","Simpson","Patrick","1","S1",12);
INSERT INTO Pupil VALUES ("169","Ferguson","Mason","4","S1",12);
INSERT INTO Pupil VALUES ("170","Kearney","Alanna","2","S4",15);
INSERT INTO Pupil VALUES ("171","Walker","Andrew","3","S6",17);
INSERT INTO Pupil VALUES ("172","Mitchell","Sophie","3","S5",16);
INSERT INTO Pupil VALUES ("173","Smith","Ian","2","S2",13);
INSERT INTO Pupil VALUES ("174","Campbell","Maddison","4","S6",17);
INSERT INTO Pupil VALUES ("175","Millar","Dominic","2","S4",15);
INSERT INTO Pupil VALUES ("176","Jones","Miyah","1","S1",12);
INSERT INTO Pupil VALUES ("177","Blackie","Ian","4","S4",15);
INSERT INTO Pupil VALUES ("178","MacNeil","Alanna","2","S6",17);
INSERT INTO Pupil VALUES ("179","MacKinnon","Lincoln","2","S5",16);
INSERT INTO Pupil VALUES ("180","Johnson","Roderick","3","S1",12);
INSERT INTO Pupil VALUES ("181","Blackie","Caitlin","3","S2",13);
INSERT INTO Pupil VALUES ("182","Wilson","Mason","3","S6",17);
INSERT INTO Pupil VALUES ("183","McGuire","Julia","2","S1",12);
INSERT INTO Pupil VALUES ("184","Thomson","Rowan","2","S1",12);
INSERT INTO Pupil VALUES ("185","Thomson","Darren","4","S5",16);
INSERT INTO Pupil VALUES ("186","Stewart","Dominic","1","S4",15);
INSERT INTO Pupil VALUES ("187","McIntyre","Innes","3","S6",17);
INSERT INTO Pupil VALUES ("188","MacIsaac","Sophie","3","S6",17);
INSERT INTO Pupil VALUES ("189","Millar","Roderick","3","S4",15);
INSERT INTO Pupil VALUES ("190","Smyth","Donald","1","S2",13);
INSERT INTO Pupil VALUES ("191","Brown","Angus","2","S2",13);
INSERT INTO Pupil VALUES ("192","Clark","Findlay","4","S5",16);
INSERT INTO Pupil VALUES ("193","Walker","Dominic","3","S4",15);
INSERT INTO Pupil VALUES ("194","Ferguson","Rowan","2","S2",13);
INSERT INTO Pupil VALUES ("195","MacLeod","Lacey","3","S1",12);
INSERT INTO Pupil VALUES ("196","MacNeil","Lewis","4","S6",17);
INSERT INTO Pupil VALUES ("197","Monk","Jamie","4","S5",16);
INSERT INTO Pupil VALUES ("198","Henderson","Owen","1","S6",17);
INSERT INTO Pupil VALUES ("199","Ferguson","Robbie","2","S5",16);
INSERT INTO Pupil VALUES ("200","Thomson","Miyah","1","S2",13);
INSERT INTO Pupil VALUES ("201","MacLean","Aonghas","3","S6",17);
INSERT INTO Pupil VALUES ("202","Wilson","Miyah","3","S2",13);
INSERT INTO Pupil VALUES ("203","Simpson","Ross","3","S1",12);
INSERT INTO Pupil VALUES ("204","Nicholson","Wendy","2","S3",14);
INSERT INTO Pupil VALUES ("205","Fifth","Colin","1","S5",13);
INSERT INTO Pupil VALUES ("206","Paterson","Liam","4","S4",15);
INSERT INTO Pupil VALUES ("207","McIntyre","Thomas","2","S1",12);
INSERT INTO Pupil VALUES ("208","MacLean","Donald","4","S5",16);
INSERT INTO Pupil VALUES ("209","Walker","Ava","2","S1",12);
INSERT INTO Pupil VALUES ("210","Galbraith","Callum","2","S5",16);
INSERT INTO Pupil VALUES ("211","MacIain","Simon","2","S5",16);
INSERT INTO Pupil VALUES ("212","Walker","Lewis","4","S4",17);
INSERT INTO Pupil VALUES ("213","MacIain","Aimee","1","S1",12);
INSERT INTO Pupil VALUES ("214","MacIsaac","Sophie","3","S5",16);
INSERT INTO Pupil VALUES ("215","MacArthur","Liam","4","S5",16);
INSERT INTO Pupil VALUES ("216","Ferguson","Seumas","3","S5",16);
INSERT INTO Pupil VALUES ("217","Docherty","Erin","4","S5",16);
INSERT INTO Pupil VALUES ("218","Simpson","Craig","3","S6",17);
INSERT INTO Pupil VALUES ("219","Millar","Innes","2","S6",17);
INSERT INTO Pupil VALUES ("220","MacLean","John","3","S1",12);
INSERT INTO Pupil VALUES ("221","Kearney","Micheal","3","S5",16);
INSERT INTO Pupil VALUES ("222","Grant","Ava","3","S3",14);
INSERT INTO Pupil VALUES ("223","Young","Sam","4","S2",13);
INSERT INTO Pupil VALUES ("224","MacArthur","Liam","2","S4",15);
INSERT INTO Pupil VALUES ("225","McIntyre","John","2","S2",13);
INSERT INTO Pupil VALUES ("226","MacDonald","Ruairidh","1","S4",15);
INSERT INTO Pupil VALUES ("227","Walker","Iain","1","S3",14);
INSERT INTO Pupil VALUES ("228","Daly","Simon","4","S6",17);
INSERT INTO Pupil VALUES ("229","Smiley","Darren","3","S5",16);
INSERT INTO Pupil VALUES ("230","Paterson","Callum","3","S3",14);
INSERT INTO Pupil VALUES ("231","Nicholson","Innes","2","S4",15);
INSERT INTO Pupil VALUES ("232","Thomson","Jamie","4","S3",14);
INSERT INTO Pupil VALUES ("233","Davidson","Lewis","3","S5",16);
INSERT INTO Pupil VALUES ("234","Smyth","Niamh","3","S6",17);
INSERT INTO Pupil VALUES ("235","MacLean","Ruairidh","2","S4",15);
INSERT INTO Pupil VALUES ("236","Jones","Simon","3","S1",12);
INSERT INTO Pupil VALUES ("237","Grant","Mason","3","S6",17);
INSERT INTO Pupil VALUES ("238","Mitchell","Seumas","2","S5",16);
INSERT INTO Pupil VALUES ("239","Galbraith","Wendy","4","S5",16);
INSERT INTO Pupil VALUES ("240","Smith","Darren","4","S2",13);
INSERT INTO Pupil VALUES ("241","Blackie","Calum","2","S1",12);
INSERT INTO Pupil VALUES ("242","Mitchell","Kieran","1","S3",14);
INSERT INTO Pupil VALUES ("243","Blackie","Liam","2","S1",12);
INSERT INTO Pupil VALUES ("244","MacLeod","Vincent","1","S4",15);
INSERT INTO Pupil VALUES ("245","Campbell","Angus","1","S5",16);
INSERT INTO Pupil VALUES ("246","Campbell","Ruairidh","1","S2",13);
INSERT INTO Pupil VALUES ("247","McIntyre","Alanna","1","S5",16);
INSERT INTO Pupil VALUES ("248","Mitchell","Rowan","2","S4",15);
INSERT INTO Pupil VALUES ("249","Blake","Seumas","1","S2",13);
INSERT INTO Pupil VALUES ("250","Docherty","Kieran","1","S2",13);
INSERT INTO Pupil VALUES ("251","Smiley","Ethan","1","S4",15);
INSERT INTO Pupil VALUES ("252","Young","Caralisa","2","S5",16);
INSERT INTO Pupil VALUES ("253","Ferguson","Julia","1","S6",17);
INSERT INTO Pupil VALUES ("254","Henderson","Anthony","3","S6",17);
INSERT INTO Pupil VALUES ("255","MacDougall","Miyah","4","S5",16);
INSERT INTO Pupil VALUES ("256","Clark","Simon","1","S2",13);
INSERT INTO Pupil VALUES ("257","McGuire","Ciara","4","S3",14);
INSERT INTO Pupil VALUES ("258","Young","Calum","1","S5",16);
INSERT INTO Pupil VALUES ("259","MacLeod","Erin","3","S5",16);
INSERT INTO Pupil VALUES ("260","MacLeod","Liam","3","S6",17);
INSERT INTO Pupil VALUES ("261","MacLean","Erin","1","S4",15);
INSERT INTO Pupil VALUES ("262","Daly","Robbie","3","S1",12);
INSERT INTO Pupil VALUES ("263","Blackie","Aonghas","4","S4",15);
INSERT INTO Pupil VALUES ("264","MacDougall","Seonaidh","2","S2",13);
INSERT INTO Pupil VALUES ("265","MacIsaac","John","2","S6",17);
INSERT INTO Pupil VALUES ("266","McGuire","Mairi","1","S2",13);
INSERT INTO Pupil VALUES ("267","Ferguson","Aonghas","2","S5",16);
INSERT INTO Pupil VALUES ("268","Kearney","Micheal","2","S6",17);
INSERT INTO Pupil VALUES ("269","Millar","Erin","2","S6",17);
INSERT INTO Pupil VALUES ("270","Wilson","Rowan","4","S4",15);
INSERT INTO Pupil VALUES ("271","Brown","Stewart","1","S6",17);
INSERT INTO Pupil VALUES ("272","Brown","Andrew","1","S6",17);
INSERT INTO Pupil VALUES ("273","Kearney","Donald","4","S4",15);
INSERT INTO Pupil VALUES ("274","Daly","Robbie","1","S1",12);
INSERT INTO Pupil VALUES ("275","Robertson","Callum","1","S4",15);
INSERT INTO Pupil VALUES ("276","Docherty","Ciara","2","S3",14);
INSERT INTO Pupil VALUES ("277","Robertson","Craig","3","S5",16);
INSERT INTO Pupil VALUES ("278","Bull","John","2","S1",11);
INSERT INTO Pupil VALUES ("279","MacIain","Angus","3","S6",17);
INSERT INTO Pupil VALUES ("280","Clark","Ruairidh","3","S2",13);
INSERT INTO Pupil VALUES ("281","MacArthur","Stewart","2","S4",15);
INSERT INTO Pupil VALUES ("282","Davidson","Anthony","4","S2",13);
INSERT INTO Pupil VALUES ("283","Small","Domhnall","1","S1",12);
INSERT INTO Pupil VALUES ("284","McGuire","Seumas","4","S5",15);
INSERT INTO Pupil VALUES ("285","MacArthur","Innes","4","S6",17);
INSERT INTO Pupil VALUES ("286","Smyth","Calum","3","S2",13);
INSERT INTO Pupil VALUES ("287","Jones","Rowan","2","S4",15);
INSERT INTO Pupil VALUES ("288","Campbell","Scott","4","S5",14);
INSERT INTO Pupil VALUES ("289","Nicholson","Ethan","3","S6",17);
INSERT INTO Pupil VALUES ("290","Campbell","Ava","4","S6",17);
INSERT INTO Pupil VALUES ("291","Paterson","Shelly","1","S1",12);
INSERT INTO Pupil VALUES ("292","Stewart","Thomas","1","S3",14);
INSERT INTO Pupil VALUES ("293","Young","Jamie","3","S6",17);
INSERT INTO Pupil VALUES ("294","Docherty","Maddison","4","S2",13);
INSERT INTO Pupil VALUES ("295","Simpson","Miyah","1","S6",17);
INSERT INTO Pupil VALUES ("296","Thomson","Roderick","3","S6",17);
INSERT INTO Pupil VALUES ("297","Simpson","Anthony","3","S4",15);
INSERT INTO Pupil VALUES ("298","Small","Jamie","3","S6",17);
INSERT INTO Pupil VALUES ("299","Walker","Rowan","1","S3",14);
INSERT INTO Pupil VALUES ("300","Daly","Mason","2","S6",17);
