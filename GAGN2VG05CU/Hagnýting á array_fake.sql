-- =========================================================DATABASE===================================================================
-- SmÃ­Ã°um database og setjum Ã­ hann smÃ¡ gÃ¶gn
drop database if exists Binna;
create database Binna;
use Binna;

create table Students
(
	studentID int auto_increment,
	studentName varchar(55),
	constraint student_PK primary key(studentID)
);

create table Courses
(
	courseID char(7),
	courseName varchar(55),
	constraint course_PK primary key(courseID),
	constraint course_name_unique unique(courseName)
);

create table StudentRegistration
(
	registrationNumber int auto_increment,
	studentID int,
	courseID char(7),
	constraint registration_PK primary key(registrationNumber),
	constraint registration_student_FK foreign key(studentID) references Students(studentID),
    constraint registration_course_FK foreign key(courseID) references Courses(courseID),
	constraint student_course_unique unique(studentID,courseID)
);

insert into Students(studentName)
values('Snorri Emilson'),
	  ('EirÃ­kur Benediktsson'),
	  ('KonrÃ¡Ã° GuÃ°mundsson'),
	  ('GuÃ°rÃºn LÃ¡rusdÃ³ttir'),
	  ('SigurÃ°ur R Ragnarsson');

insert into Courses(courseID,courseName)
values('GSF2A3U','GagnasafnsfrÃ¦Ã°i 1'),
      ('GSF2B3U','GagnasafnsfrÃ¦Ã°i 2'),
	  ('GSF3A3U','GagnasafnsfrÃ¦Ã°i 3'),
	  ('GSF3B3U','HugbÃºnaÃ°argerÃ°'),
      ('FOR3G3U','Inngangur aÃ° leikjaforritun'),
      ('FOR3A3U','Hlutbundin forritun');

-- ======================================================================SP===============================================================
-- SmÃ­Ã°um stored procedure fyrir skrÃ¡ningu nemanda Ã­ Ã¡fanga
DELIMITER $$

DROP PROCEDURE IF EXISTS studentCourseRegistration $$

CREATE PROCEDURE studentCourseRegistration(student_id int,student_courses TEXT)
BEGIN
    DECLARE currentPosition INT; 
    DECLARE workingArray TEXT; 
    DECLARE currentCourse VARCHAR(255);

    SET workingArray = student_courses; 
    SET currentPosition = 1;

    WHILE CHAR_LENGTH(workingArray) > 0 AND currentPosition > 0 DO 
        SET currentPosition = INSTR(workingArray, ','); 
        IF currentPosition = 0 THEN 
            SET currentCourse = workingArray; 
        ELSE 
            SET currentCourse = LEFT(workingArray, currentPosition - 1); 
        END IF; 

        IF TRIM(currentCourse) != '' THEN 
            INSERT INTO StudentRegistration(studentID,courseID)VALUES(student_id,currentCourse);
        END IF; 

        SET workingArray = SUBSTRING(workingArray, currentPosition + 1); 
    END WHILE;
END $$

DELIMITER ;

-- Snorri settur Ã­ Ã¡fanga:
-- call studentCourseRegistration(1,'GSF2A3U,GSF2B3U,GSF3A3U');

-- select * from Students;
-- select * from Courses;