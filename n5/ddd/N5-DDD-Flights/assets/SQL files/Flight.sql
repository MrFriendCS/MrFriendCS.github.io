CREATE TABLE Flight (
    flightID VARCHAR(5) NOT NULL,
    depDate DATE NOT NULL,
    depTime TIME NOT NULL,
    arrDate DATE NOT NULL,
    arrTime TIME NOT NULL,
    capacity INT NOT NULL,
    routeID INT NOT NULL,
    FOREIGN KEY (routeID)
        REFERENCES Route (routeID),
    PRIMARY KEY (flightID)
);

INSERT INTO Flight VALUES ("AY478","2018-03-27","17:00:00","2018-03-27","22:00:00",310,6982);
INSERT INTO Flight VALUES ("CV981","2018-03-30","04:45:00","2018-03-30","08:10:00",326,1329);
INSERT INTO Flight VALUES ("DB191","2018-04-05","15:00:00","2018-04-05","15:55:00",220,9214);
INSERT INTO Flight VALUES ("DC439","2018-03-31","22:45:00","2018-04-01","06:50:00",378,4551);
INSERT INTO Flight VALUES ("DG182","2018-03-27","16:00:00","2018-03-27","23:00:00",320,5281);
INSERT INTO Flight VALUES ("DG199","2018-03-26","16:00:00","2018-03-26","23:00:00",320,5281);
INSERT INTO Flight VALUES ("DP198","2018-03-28","16:00:00","2018-03-28","23:00:00",320,5281);
INSERT INTO Flight VALUES ("DQ182","2018-04-03","13:00:00","2018-04-03","15:30:00",250,7120);
INSERT INTO Flight VALUES ("DQ583","2018-03-25","13:00:00","2018-03-25","15:30:00",250,7120);
INSERT INTO Flight VALUES ("DS126","2018-03-27","12:30:00","2018-03-27","13:20:00",60,6232);
INSERT INTO Flight VALUES ("DS129","2018-03-29","12:30:00","2018-03-29","13:20:00",60,6232);
INSERT INTO Flight VALUES ("GD845","2018-03-23","10:35:00","2018-03-23","14:49:00",350,1279);
INSERT INTO Flight VALUES ("GR737","2018-04-01","07:14:00","2018-04-01","10:55:00",396,1924);
INSERT INTO Flight VALUES ("GR738","2018-03-25","07:14:00","2018-03-25","10:55:00",396,1924);
INSERT INTO Flight VALUES ("GS740","2018-03-30","12:15:00","2018-03-30","20:50:00",312,1902);
INSERT INTO Flight VALUES ("HJ983","2018-04-02","11:45:00","2018-04-02","15:10:00",298,3187);
INSERT INTO Flight VALUES ("IK209","2018-03-30","16:35:00","2018-03-30","19:15:00",224,2716);
INSERT INTO Flight VALUES ("JK201","2018-03-29","16:35:00","2018-03-29","19:15:00",224,2716);
INSERT INTO Flight VALUES ("JS177","2018-03-26","05:25:00","2018-03-26","12:15:00",286,3976);
INSERT INTO Flight VALUES ("JS391","2018-03-29","05:25:00","2018-03-29","12:15:00",286,3976);
INSERT INTO Flight VALUES ("JV902","2018-03-27","08:50:00","2018-03-27","11:44:00",312,4153);
INSERT INTO Flight VALUES ("KJ292","2018-03-28","16:35:00","2018-03-28","19:15:00",224,2716);
INSERT INTO Flight VALUES ("KK919","2018-03-28","06:18:00","2018-03-28","09:48:00",376,1902);
INSERT INTO Flight VALUES ("KL118","2018-03-27","15:05:00","2018-03-27","17:10:00",270,4871);
INSERT INTO Flight VALUES ("KL720","2018-03-23","15:05:00","2018-03-23","17:10:00",270,4871);
INSERT INTO Flight VALUES ("KL989","2018-03-29","06:18:00","2018-03-29","09:48:00",376,4871);
INSERT INTO Flight VALUES ("LK001","2018-03-24","14:12:00","2018-03-24","17:24:00",240,7625);
INSERT INTO Flight VALUES ("MK990","2018-03-31","07:14:00","2018-03-31","10:55:00",396,1924);
INSERT INTO Flight VALUES ("NK923","2018-03-30","06:18:00","2018-03-30","09:48:00",376,4871);
INSERT INTO Flight VALUES ("QH128","2018-03-30","09:50:00","2018-03-30","14:55:00",288,3187);
INSERT INTO Flight VALUES ("QH182","2018-03-24","09:50:00","2018-03-24","14:55:00",288,2847);
INSERT INTO Flight VALUES ("QH199","2018-04-01","09:50:00","2018-04-01","14:55:00",288,2847);
INSERT INTO Flight VALUES ("QL015","2018-04-01","07:50:00","2018-04-01","11:30:00",240,7625);
INSERT INTO Flight VALUES ("QS730","2018-03-26","21:30:00","2018-03-26","01:00:00",244,5765);
INSERT INTO Flight VALUES ("QS739","2018-03-24","21:30:00","2018-03-24","01:00:00",244,5765);
INSERT INTO Flight VALUES ("QV100","2018-03-28","07:20:00","2018-03-28","08:50:00",178,3651);
INSERT INTO Flight VALUES ("QV102","2018-03-30","07:20:00","2018-03-30","08:50:00",178,3651);
INSERT INTO Flight VALUES ("QY171","2018-03-31","09:50:00","2018-03-31","14:55:00",288,2847);
INSERT INTO Flight VALUES ("QZ583","2018-04-02","13:00:00","2018-04-02","15:30:00",250,7120);
INSERT INTO Flight VALUES ("RS403","2018-03-24","12:15:00","2018-03-24","20:50:00",312,1902);
INSERT INTO Flight VALUES ("SA981","2018-04-04","04:45:00","2018-04-04","08:10:00",326,1329);
INSERT INTO Flight VALUES ("SD026","2018-03-29","22:45:00","2018-03-20","06:50:00",378,4551);
INSERT INTO Flight VALUES ("SJ938","2018-03-25","08:50:00","2018-03-25","11:44:00",312,4153);
INSERT INTO Flight VALUES ("SK000","2018-03-28","14:12:00","2018-03-28","17:24:00",240,7625);
INSERT INTO Flight VALUES ("SW126","2018-04-03","12:30:00","2018-04-03","13:20:00",60,6232);
INSERT INTO Flight VALUES ("TY531","2018-03-23","17:00:00","2018-03-23","22:00:00",310,6982);
INSERT INTO Flight VALUES ("TY753","2018-03-30","17:00:00","2018-03-30","22:00:00",310,6982);
INSERT INTO Flight VALUES ("UP984","2018-03-26","10:35:00","2018-03-26","14:49:00",350,1279);
INSERT INTO Flight VALUES ("WS101","2018-03-29","07:20:00","2018-03-29","08:50:00",178,3651);
INSERT INTO Flight VALUES ("WS192","2018-03-26","07:20:00","2018-03-26","08:50:00",178,3651);
INSERT INTO Flight VALUES ("YH827","2018-03-25","09:25:00","2018-03-25","14:35:00",268,3976);