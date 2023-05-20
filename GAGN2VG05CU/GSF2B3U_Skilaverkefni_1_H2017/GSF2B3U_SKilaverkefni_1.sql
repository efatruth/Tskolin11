

drop database if exists 0301865919_ProgressTracker_V1;

create database 0301865919_ProgressTracker_V1
	default character set utf8
	default collate utf8_general_ci;

set default_storage_engine = innodb;
set sql_mode = 'STRICT_ALL_TABLES';

use 0301865919_ProgressTracker_V1;

-- School information
create table Schools
(
	schoolID int auto_increment,
    schoolName varchar(75),
    constraint school_PK primary key(schoolID)
);

-- Divisions belonging to certain scool(s)
create table Divisions
(
	divisionID int auto_increment,
    divisionName varchar(75) not null,
    schoolID int not null,
    constraint division_PK primary key(divisionID),
    constraint division_school_FK foreign key(schoolID) references Schools(schoolID)
);

-- Each division has at least one track
create table Tracks
(
	trackID int auto_increment,
    trackName varchar(75),
    validFrom date,
    divisionID int not null,
    constraint track_PK primary key(trackID),
    constraint track_division_FK foreign key(divisionID) references Divisions(divisionID)
);

-- All the courses in the database
create table Courses 
(
  courseNumber char(10),
  courseName varchar(75) not null,
  courseCredits tinyint(4) default 3,
  constraint course_PK primary key(courseNumber),
  constraint name_unique unique(courseName)
);

-- A course may or may not have restrictors applied to them
create table Restrictors 
(
  courseNumber char(10) not null,
  restrictorID char(10) not null,
  restrictorType char(1) default '1',
  constraint restrictor_PK primary key (courseNumber,restrictorID),
  constraint course_course_FK foreign key (courseNumber) references Courses (courseNumber),
  constraint restrictor_course_FK foreign key (courseNumber) references Courses (courseNumber)
);

-- Courses belonging to a certain track. A track can belong to more then one track(N:M)
create table TrackCourses
(
	trackID int not null,
    courseNumber char(10) not null,
    semester tinyint unsigned null,
    mandatory tinyint unsigned,
    constraint trackcourse_PK primary key(trackID,courseNumber),
    constraint track_course_tracks_FK foreign key(trackID) references Tracks(trackID),
    constraint track_course_courses_FK foreign key(courseNumber) references Courses(courseNumber)
);

insert into Schools(schoolName) values('Tækniskólinn');

insert into Divisions(divisionName,schoolID)values('Byggingatækniskólinn',1);
insert into Divisions(divisionName,schoolID)values('Endurmenntunarskólinn',1);
insert into Divisions(divisionName,schoolID)values('Flugskóli Íslands',1);
insert into Divisions(divisionName,schoolID)values('Handverksskólinn',1);
insert into Divisions(divisionName,schoolID)values('Margmiðlunarskólinn',1);
insert into Divisions(divisionName,schoolID)values('Meistaraskólinn',1);
insert into Divisions(divisionName,schoolID)values('Raftækniskólinn',1);
insert into Divisions(divisionName,schoolID)values('Skipstjórnarskólinn',1);
insert into Divisions(divisionName,schoolID)values('Tækniakademían',1);
insert into Divisions(divisionName,schoolID)values('Tæknimenntaskólinn',1);
insert into Divisions(divisionName,schoolID)values('Upplýsingatækniskólinn',1);
insert into Divisions(divisionName,schoolID)values('Vefskólinn',1);
insert into Divisions(divisionName,schoolID)values('Véltækniskólinn',1);

insert into Tracks(trackName,divisionID)values('Almennt nám Upplýsingatækniskóla - AN UTN',10);
insert into Tracks(trackName,divisionID)values('Bókband',10);
insert into Tracks(trackName,divisionID)values('Grafísk miðlun',10);
insert into Tracks(trackName,divisionID)values('Grunnnám upplýsinga- og fjölmiðlagreina',10);
insert into Tracks(trackName,divisionID)values('K2 Tækni- og vísindaleiðin',10);
insert into Tracks(trackName,divisionID)values('Ljósmyndun',10);
insert into Tracks(trackName,divisionID)values('Prentun',10);
insert into Tracks(trackName,divisionID)values('Stúdentspróf',10);
insert into Tracks(trackName,validFrom,divisionID)values('Tölvubraut TBR16 - stúdentsbraut','2016-08-01',10);

insert into Courses(courseNumber,courseName,courseCredits)
values('GSF2A3U','Gagnasafnsfræði I',3),
	  ('GSF2B3U','Gagnasafnsfræði II',3),
	  ('GSF3A3U','Gagnanotkun',3),
	  ('GSF3B3U','Gagnagreining',3);
insert into Courses(courseNumber,courseName,courseCredits)
values('FOR3G3U','Inngangur að leikjaforritun',3),
	  ('FOR3L3U','Leikjaforritun',3),
	  ('FOR3D3U','3D leikjaforritun',3);
insert into Courses(courseNumber,courseName,courseCredits)
values('STÆ103','Inngangur að stærðfræði',3),
	  ('STÆ203','Algebra',3),
	  ('STÆ303','Rúmfræði',3),
      ('STÆ313','Tölfræði',3),
      ('STÆ403','Ve0301865919orar',3),
      ('STÆ503','Diffrun og Heildun',3),
      ('STÆ603','Stærðfræðigreining',3);
insert into Courses(courseNumber,courseName,courseCredits)
values('EÐL103','Eðlisfræði I',3), 
	  ('EÐL203','Eðlisfræði II',3),
	  ('EÐL303','Eðlisfræði III',3),
	  ('EÐL403','Eðlisfræði IV',3);

insert into Restrictors(courseNumber,restrictorID,restrictorType)values('GSF2B3U','GSF2A3U',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('GSF3A3U','GSF2B3U',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('GSF3A3U','GSF3B3U',2);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('GSF3B3U','GSF3A3U',3);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ203','STÆ103',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ303','STÆ203',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ303','STÆ313',2);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ313','STÆ203',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ403','STÆ303',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ503','STÆ403',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('STÆ603','STÆ503',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('EÐL103','STÆ103',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('EÐL203','EÐL103',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('EÐL303','EÐL203',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('EÐL403','EÐL303',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('FOR3G3U','STÆ403',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('FOR3L3U','FOR3G3U',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('FOR3L3U','EÐL203',1);
insert into Restrictors(courseNumber,restrictorID,restrictorType)values('FOR3L3U','FOR3D3U',2);


-- ********************** -- Skrifið eftirfarandi stored procedures: --**********************

-- 1:	CourseList()
-- Birtir lista(yfirlit) af öllum áföngum sem geymdir eru í gagnagrunninum.
-- Áfangarnir eru birtir í stafrófsröð 
	
	DELIMITER //
    DROP PROCEDURE IF EXISTS CourseList //
    
	CREATE PROCEDURE CourseList()
	BEGIN
	  SELECT courseName, courseNumber 
      FROM Courses 
      ORDER BY courseName;
	END //
	DELIMITER ;
    
    CALL CourseList();
    
    DROP PROCEDURE CourseList;


-- 2:	SingleCourse()
-- 	Birtir upplýsingar um einn ákveðin kúrs.
--  Færibreytan er áfanganúmerið
	DELIMITER $$
    DROP PROCEDURE IF EXISTS SingleCourse $$
    
	CREATE PROCEDURE SingleCourse
    (
		IN afangaNumer CHAR(10)
    )
	BEGIN
	  SELECT *
      FROM Courses 
      WHERE afangaNumer = courseNumber;
	END $$
	DELIMITER ;
    
    CALL SingleCourse('ICE');

-- 3:   NewCourse()
--  Nýskráir áfanga í gagnagrunninn.
--  Skoðið ERD myndina til að finna út hvaða gögn á að vista(hvaða færibreytur á að nota)
--  NewCourse er með out parameterinn number_of_inserted_rows sem skilar fjölda þeirra
--  raða sem vistaðar voru í gagnagrunninum.  Til þess notið þið MySQL function: row_count()
	DELIMITER //
    DROP PROCEDURE IF EXISTS NewCourse //
	CREATE PROCEDURE NewCourse
    (
		IN afangaNumer CHAR(10),
        IN course_name VARCHAR(20),
        IN course_credits tinyint(4),
		OUT number_of_inserted_rows INT(20)
    )
	BEGIN
		INSERT INTO Courses  (courseNumber, courseName, courseCredits)
        Values(afangaNumer, course_name, course_credits);
        SET number_of_inserted_rows = row_count();
        
	END //
	DELIMITER ;
    
    CALL NewCourse('ICE', 'ICE103', 5 ,@test);

-- 4:	UpdateCourse()
--  Hér eru notaðar sömu færibreytur og í lið 3.  Áfanganúmerið er notað til að uppfæra réttan kúrs.
-- row_count( fallið er hér notað líka.
	SET FOREIGN_KEY_CHECKS=0;

	DELIMITER //
    DROP PROCEDURE IF EXISTS UpdateCourse //
	CREATE PROCEDURE UpdateCourse
    (
		IN newAfangaNumer CHAR(10),
        IN oldAfangaNumer char(10),
        IN course_name VARCHAR(75),
        IN course_credits tinyint(4),
		OUT number_of_inserted_rows INT(20)
    )
	BEGIN
	
		UPDATE Courses

            SET 
            courseNumber = newAfangaNumer,
            courseName = course_name,
            courseCredits = course_credits
            WHERE courseNumber = oldAfangaNumer;
            SET number_of_inserted_rows = row_count();
	END //
	DELIMITER ;
    
    CALL UpdateCourse('FIRE', 'ICE' , 'X',  5 , @test);
    
    SELECT * FROM Courses;
    
    SET FOREIGN_KEY_CHECKS=1;

-- 5:	DeleteCourse()
-- Áfanganúmer(courseNumber) er notað hérna til að eyða réttum kúrs.
-- ATH: Ef verið er að nota kúrsinn einhversstaðar(sé hann skráður á TrackCourses) þá má EKKI eyða honum.
-- Sé hins vegar hvergi verið að nota hann má eyða honum úr Courses töflunni og einnig Restrictors töflunni.alter
-- sem fyrr er out parameter notaður til að "skila" fjölda þeirra raða sem eytt var úr töflunni COurses
	SET SQL_SAFE_UPDATES = 0 -- Safe Update OFF ,það er hægt að nota safe update haka við þá þarf að logout og login eða reconnecta server
	
	DELIMITER //
    DROP PROCEDURE IF EXISTS DeleteCourse //
	CREATE PROCEDURE DeleteCourse
    (
		IN afangaNumer CHAR(10)
    )
	BEGIN
	  DELETE FROM Courses WHERE afangaNumer LIKE courseNumber;
	END //
	DELIMITER ;
    
    CALL DeleteCourse('AMMA');
    
    SET SQL_SAFE_UPDATES = 1 -- Set safe update on for security reasons / also may have to make a reset
    
    SELECT * FROM Courses
    
-- ********************** -- Skrifið eftirfarandi functions: --**********************

-- 6:	NumberOfCourses()
-- fallið skilar heildarfjölda allra áfanga í grunninum
DELIMITER $$

	DROP FUNCTION IF EXISTS NumberOfCourses $$
    
	CREATE FUNCTION NumberOfCourses()
    RETURNS INT(10)
    
    BEGIN
		DECLARE outcome INTEGER;
		SELECT COUNT(courseNumber) as Number_Of_Courses INTO outcome 
		FROM Courses;
    RETURN outcome;
    END $$
    
DELIMITER ;
SELECT NumberOfCourses();

-- 7:	TotalTRackCredits()
--  Fallið skilar heildar einingafjölda ákveðinnar námsbrautar(track)
--  Senda þarf trackID inn sem færibreytu

DELIMITER $$

	DROP FUNCTION IF EXISTS TotalTrackCredits $$
    
	CREATE FUNCTION TotalTrackCredits()
    RETURNS INT(10)
    
    BEGIN
		DECLARE outcome INTEGER;
		SELECT SUM(courseCredits) as Eininga_Fjoldi INTO outcome
		FROM Courses;
    RETURN outcome;
    END $$
    
DELIMITER ;

SELECT TotalTrackCredits();

-- 8:   HighestCredits()
-- Fallið skilar einingafjölda þess námskeiðs(þeirra námskeiða) sem hafa flestar einingar.
-- ATH:  Það geta fleiri en einn kúrs verið með sama einingafjöldann. :að á ekki að hafa 
-- áhfri á niðurstöðuna.
DELIMITER $$

	DROP FUNCTION IF EXISTS HighestCredits $$
    
	CREATE FUNCTION HighestCredits()
    RETURNS INT(10)
    
    BEGIN
		DECLARE outcome INTEGER;
		SELECT MAX(courseCredits) as Flestar_Eininga_Fjold INTO outcome 
		FROM Courses;
    RETURN outcome;
    END $$
    
DELIMITER ;

SELECT HighestCredits();

-- 9:  TopTracksDivision()
-- Fallið skilað toppfjölda námsbrauta(tracks) sem tilheyra námsbrautum(Divisions)
DELIMITER $$

	DROP FUNCTION IF EXISTS TopTrackDivision $$
    
	CREATE FUNCTION TopTrackDivision()
    RETURNS INT(10)
    
    BEGIN
		DECLARE outcome INTEGER;
		SELECT COUNT(trackName) INTO outcome 
		FROM Tracks;
    RETURN outcome;
    END $$
    
DELIMITER ;

SELECT TopTrackDivision();


-- 10: leastRestrictedCourseNumber()
-- Fallið skilar minnsta fjölda kúrsa í Restrictors töflunni.
-- ATH:  Ef kúrs eða kúrsar eru t.d. með einn undanfara þog ekkert meir þá myndi fallið skila 1 

-- NUMER 10 KENNARA SEGJA ÞURFUM AÐ SLEPPA AF
