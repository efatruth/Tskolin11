﻿CREATE DATABASE KENNITALA_hopverkefni2;
USE KENNITALA_hopverkefni2;

#Daemi 1
CREATE TABLE Customer(
	CUS_CODE INT,
    CUS_LNAME VARCHAR(30),
    CUS_FNAME VARCHAR(30),
    CUS_INITIAL VARCHAR(30),
    CUS_AREACODE VARCHAR(10),
    CUS_PHONE VARCHAR(15),
    CUS_BALANCE VARCHAR(7)
);

CREATE TABLE Invoice(
	INV_NUMBER INT,
    CUS_CODE INT,
    INV_DATE DATE
);

CREATE TABLE Line(
	LIN_NUMBER INT,
    LINE_UNITS INT,
    LINE_PRICE VARCHAR(10)
);

CREATE TABLE Product(
	PROD_CODE VARCHAR(20),
    PROD_DESCRIPT VARCHAR(200),
    PROD_PRICE VARCHAR(6),
    PROD_ON_HAND BOOLEAN
);

CREATE TABLE Vendor(
	VEND_CODE INT,
    VEND_CONTACT VARCHAR(10),
    VEND_AREACODE INT(6),
    VEND_PHONE VARCHAR(10)
);

#Daemi 2
ALTER TABLE customer ADD CONSTRAINT PRIMARY KEY(CUS_CODE);

ALTER TABLE invoice ADD CONSTRAINT PRIMARY KEY(INV_NUMBER);

ALTER TABLE line ADD CONSTRAINT PRIMARY KEY(LIN_NUMBER);

ALTER TABLE product ADD CONSTRAINT PRIMARY KEY(PROD_CODE);

ALTER TABLE vendor ADD CONSTRAINT PRIMARY KEY(VEND_CODE);

ALTER TABLE invoice MODIFY COLUMN cus_code INT NOT NULL;
ALTER TABLE line ADD COLUMN INV_NUMBER INT NOT NULL;
ALTER TABLE line ADD COLUMN PROD_CODE VARCHAR(20) NOT NULL;
ALTER TABLE product ADD COLUMN VEND_CODE INT NOT NULL;

ALTER TABLE invoice ADD CONSTRAINT FK_CUS_CODE FOREIGN KEY (CUS_CODE) REFERENCES customer(CUS_CODE);
ALTER TABLE line ADD CONSTRAINT FK_INV_NUMBER FOREIGN KEY (INV_NUMBER) REFERENCES invoice(INV_NUMBER);

ALTER TABLE line ADD CONSTRAINT FK_PROD_CODE FOREIGN KEY (PROD_CODE) REFERENCES product(PROD_CODE);
ALTER TABLE product ADD CONSTRAINT FK_VEND_CODE FOREIGN KEY (VEND_CODE) REFERENCES vendor(VEND_CODE);

#Daemi 3
ALTER TABLE customer ALTER COLUMN CUS_BALANCE SET DEFAULT 0.00;
ALTER TABLE customer ALTER COLUMN CUS_AREACODE SET DEFAULT "0181";
ALTER TABLE line ALTER COLUMN LINE_UNITS SET DEFAULT 0.00;
ALTER TABLE line ALTER COLUMN LINE_PRICE SET DEFAULT 0.00;

ALTER TABLE `invoice` ADD INDEX `CUS_CODEX` (`CUS_CODE`);

ALTER TABLE `line` ADD INDEX `INV_NUMBER` (`INV_NUMBER`);
ALTER TABLE `line` ADD INDEX `P-CODE` (`PROD_CODE`);

ALTER TABLE `product` ADD COLUMN `P_INDATE` DATE NOT NULL;
ALTER TABLE `product` ADD INDEX `P_INDATEX` (`P_INDATE`);

CREATE INDEX `VENPRODX` ON product(`VEND_CODE`, `PROD_CODE`);
CREATE INDEX `PROD_PRICEX` ON product(`PROD_PRICE` DESC);

ALTER TABLE product DROP INDEX `PROD_PRICEX`;

#Daemi 5
ALTER TABLE Customer MODIFY CUS_BALANCE DECIMAL NOT NULL;
ALTER TABLE Line MODIFY LINE_PRICE DECIMAL NOT NULL;
ALTER TABLE vendor MODIFY VEND_CONTACT VARCHAR(30) NOT NULL;
ALTER TABLE Product MODIFY PROD_PRICE DECIMAL NOT NULL;

#Daemi 6
INSERT INTO Customer VALUES
	(10010,'Ramas','Alfred','A','0181','844-2573', 0),
	(10011,'Dunne','Leona','K','0161','894-1238', 0),
	(10012,'Smith','Kathy','W','0181','894-2285', 345.86);

INSERT INTO Invoice VALUES
	(1001,10010,'2008-01-16'),
	(1002,10011,'2008-01-16'),
	(1003,10012,'2008-01-16');

INSERT INTO Vendor VALUES
	(21225,'Bryson, Inc.','0181','223-3234'),
	(21226,'SuperLoo, Inc.','0113','215-8995'),
	(21231,'D\&E Supply','0181','228-3245');

INSERT INTO Product VALUES
	('11QER/31','Power painter. 15 psi. 3-nozzle', 109.99, 8, 21225,'2007-11-07'),
    ('13-Q2/P2','7.25-cm. pwr. saw blade’', 14.99, 32, 21226,'2007-12-14'),
    ('14-Q1/L3','9.00-cm. pwr. saw blade', 17.49, 18, 21226,'2007-11-13');

INSERT INTO Line VALUES
	(1001,1, 14.99, 1001,'13-Q2/P2'),
	(1002,2, 9.95, 1001,'11QER/31'),
	(1003,1, 4.99, 1002,'14-Q1/L3');

#Daemi 7
CREATE TABLE Employee(

	EMP_NUM INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 

	EMP_TITLE CHAR(10), 

	EMP_LNAME VARCHAR(15), 

	EMP_FNAME VARCHAR(15), 

	EMP_INITIAL CHAR(1), 

	EMP_DOB DATETIME, 

	EMP_HIR_DATE DATETIME, 

	EMP_AREACODE CHAR(5), 

	EMP_PHONE CHAR(8)
);

INSERT INTO Employee(EMP_TITLE, EMP_LNAME, EMP_FNAME, EMP_INITIAL, EMP_DOB, EMP_HIR_DATE, EMP_AREACODE, EMP_PHONE)

VALUES

('SalePerson', 'Flassbender', 'Rannigan', 'R', '1967-04-13', '2009-06-21', '89044', '798-2132'),

('SalePerson', 'Warhol', 'Candy', 'C', '1979-07-25', '2005-03-13', '48458', '663-1294'),

('SalePerson', 'Amadeus', 'Benny', 'B', '1993-11-01', '2016-05-18', '66000', '954-8565');

ALTER TABLE CUSTOMER ADD EMP_NUM INT NOT NULL;
ALTER TABLE PRODUCT ADD EMP_NUM INT NOT NULL;

UPDATE CUSTOMER SET EMP_NUM = 1 WHERE CUS_CODE = 10010;

UPDATE CUSTOMER SET EMP_NUM = 2 WHERE CUS_CODE = 10011;

UPDATE CUSTOMER SET EMP_NUM = 3 WHERE CUS_CODE = 10012;

UPDATE PRODUCT SET EMP_NUM = 1 WHERE PROD_CODE = "11QER/31";

UPDATE PRODUCT SET EMP_NUM = 2 WHERE PROD_CODE = "13-Q2/P2";

UPDATE PRODUCT SET EMP_NUM = 3 WHERE PROD_CODE = "14-Q1/L3";

ALTER TABLE CUSTOMER ADD FOREIGN KEY (EMP_NUM) REFERENCES EMPLOYEE(EMP_NUM);
ALTER TABLE PRODUCT ADD FOREIGN KEY (EMP_NUM) REFERENCES EMPLOYEE(EMP_NUM);