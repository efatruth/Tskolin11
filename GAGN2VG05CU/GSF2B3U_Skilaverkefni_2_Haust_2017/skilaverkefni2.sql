-- 1: 
-- Design extensions to the ProgressTracker database so that it becomes possible to register students 
-- and they can choose a track(within a division).

USE 0301865919_progressTracker_V1;
DROP TABLE IF EXISTS Students;

CREATE TABLE Students
(
	studentID INT NOT NULL AUTO_INCREMENT,
	studentName VARCHAR(140),
    studentSSN VARCHAR(10),
    trackID INT NOT NULL,
    CONSTRAINT student_Track FOREIGN KEY(trackID) references Tracks(trackID),
	CONSTRAINT student_PK PRIMARY KEY(studentID)
);

INSERT INTO Students(studentName, studentSSN, trackID)
VALUES
('Petur Emilson','1509868653',9),
('Daniel Benediktsson','0204918934',9),
('Konrað Gunnasson','1001967123', 6),
('Guarún Larusdóttir','1107890786',6),
('Sigurður Ingvarsson','0405974192',9);


DELIMITER //
DROP PROCEDURE IF EXISTS AddStudent //
CREATE PROCEDURE AddStudent (
  param_studentName VARCHAR(140),
  param_studentSSN VARCHAR(10),
  param_trackID INT 
)
BEGIN
  INSERT INTO Students (
	 studentName,
     studentSSN,
     trackID
)
VALUES(
  param_studentName,
  param_studentSSN,
  param_trackID
);

END //
DELIMITER ;
CALL Addstudent('Daniel','Levinson', 2);

SELECT * FROM Students;



-- 2:
-- Create a trigger for the insert operation on the table Restrictors.  
-- The trigger prevents the case of the courseNumber and restrictorID 
-- being the same(a course cannot be a restrictor on it self).  
-- If this is the case then the trigger prevents the insert by throwing and
-- error and writes a error message. Example of an insert operation that the trigger stops:
DELIMITER //
DROP TRIGGER IF EXISTS DetectSameRestrictorInsert //
CREATE TRIGGER DetectSameRestrictorInsert
BEFORE INSERT ON Restrictors
FOR EACH ROW
BEGIN
  IF (new.courseNumber = new.restrictorID) THEN
	signal sqlstate '45000' set message_text = 'A course cannot be a restrictor on it it self';
  END IF;
END //
DELIMITER ;



-- 3. 
-- Write an identical trigger for the update operation on the table Restrictors.
DELIMITER //
DROP TRIGGER IF EXISTS DetectSameRestrictorUpdate //
CREATE TRIGGER DetectSameRestrictorUpdate
BEFORE UPDATE ON Restrictors
FOR EACH ROW
BEGIN
  IF (new.courseNumber = new.restrictorID) THEN
	signal sqlstate '45000' set message_text = 'A course cannot be a restrictor on it self';
  END IF;
END //
DELIMITER ;


-- 4:
-- Write a stored procedure that sums up the course credits that a student has finished arranged 
-- by the divisions offering these courses. 

-- NOTE
-- The general courses(physics, mathematics, sociology, etc.) actually belong 
-- to the General Study Division(Tæknimenntaskólinn NTT13). 
-- This in fact means that if the student has completed four, three credit courses of general 
-- studies(say math and physics) and five, three credit courses at 
-- the computer division(Tölvubraut TBR16) the results would look something like this: 

-- NTT13 12
-- TBR16 15
-- Only courses that are graded >= 5 or are graded ‘passed’ should be chosen.
DROP TABLE IF EXISTS StudentCourses;
CREATE TABLE StudentCourses
(
	studentID INT NOT NULL,
	trackID INT NOT NULL,
    courseNumber CHAR(10),
    grade FLOAT,
    semester CHAR(10),
    CONSTRAINT FK_studentID_StudentCourses FOREIGN KEY(studentID) REFERENCES Students(StudentID),
	CONSTRAINT FK_trackID_StudentCourses FOREIGN KEY(trackID) REFERENCES Tracks(trackID),
    CONSTRAINT FK_courseNumber_StudentCourses FOREIGN KEY(courseNumber) REFERENCES Course(courseNumber)
);

INSERT INTO StudentCourses(studenID, trackID, course)
VALUES
(1, 9, 'STÆ203', 8.14, '2018V'),
(2, 9, 'GSF2A3U', 7.4, '2018V'),
(3, 6, 'EDL103', 8.2, '2018V'),
(3, 2, 'STÆ103', 5.6, '2018V'),
(3, 6, 'STÆ203', 3.6, '2018V'),
(3, 6, 'FOR3L3U', 7.5, '2018V'),
(4, 6, 'FOR3D3U', 9.5, '2018V'),
(5, 9, 'STÆ203', 7, '2018V'),
(6, 2, 'STÆ603', 3.3, '2018V');

DELIMITER //
DROP PROCEDURE IF EXISTS StudentCourseCreditSum //
CREATE PROCEDURE StudentCourseCreditSum (
	param_studentID INT
)
BEGIN
  SELECT Tracks, trackNumber, SUM(Courses.courseCredits) AS Credits
  FROM StudentCourses
  INNER JOIN Students ON StudentCourses.studentID = Students.studentID
  INNER JOIN Tracks ON StudentCourses.trackID = Tracks.trackID
  INNER JOIN Courses ON StudentCourses.courseNumber = Courses.courseNumber
  WHERE StudentCourses.studentID = param_studentID
	AND StudentCourses.grade >= 5
  GROUP BY Tracks.trackName;
END //
DELIMITER ;

CALL StudentCourseCreditSum (3);



-- 5:
-- Write a cursor that selects all the mandatory courses for a student and
-- puts them into the table that stores the student courses. 
-- Put this cursor in a stored procedure that can be called “AddMandatoryCourses” 
-- and is run when a student selects courses for the first time. 
-- The selection process could be implemented in another stored procedure, 
-- perhaps called NewStudentCourses.  In that one a check is performed to 
-- see if the student has chosen courses before and 
-- if that is then the AddMandatoryCOurses has already been run and 
-- is NOT run again.
DELIMITER //
DROP PROCEDURE IF EXISTS AddMandatoryCourses //
CREATE PROCEDURE AddMandatoryCourses (
  param_studentID INT,
  param_trackID INT,
  param_currSemester CHAR(10),
  param_nextSemester CHAR(10)
)
BEGIN

-- current course number that the cursor holds on to
DECLARE currCourseNumber CHAR(10);
-- A default grade that a student is initialized with when they choose a class; which is a 0
DECLARE defaultGrade INT DEFAULT 0;
-- the loop is finished
DECLARE finished BOOLEAN DEFAULT FALSE;

-- Gets all mandatory classes that a student is capable of taking next semester
DECLARE cur_nextClasses CURSOR FOR
SELECT TrackCourses.courseNumber -- ,TrackCourses.trackID, TrackCourses.semester, Restrictors....
FROM TrackCourses
LEFT JOIN Restrictors ON TrackCourses.courseNumber = Restrictors.courseNumber
WHERE TrackCourses.courseNumber
-- Ignore classes that a student is already done with, with a grade of >=5 or ignore any class student....
NOT IN (
  SELECT StudentCourses.courseNumber
  FROM StudentCourses
  WHERE StudentCourses.studentID = param_studentID
  AND (StudentCourses.grade >= 5 OR StudentCourses.semester = param_currSemester)
)
-- Get all classes that are flagged as mandatory
AND TrackCourses.Mandatory != 0
-- Get all courses that are for the declared track
AND TrackCourses.trackID = param_trackID
-- Finally without getting for example STÆ303, STÆ313, STÆ403, STÆ503...you only want the one that you have...
-- To do so you've got to look at what is required to take each class, if you're done with what's required the...
-- lets say you are in  STÆ403, you don't need to worry about being assigned again to  STÆ103, STÆ203, STÆ313, STÆ403, STÆ503...
AND
(Restrictors.restrictorID IN (
SELECT StudentCourses.courseNumber
  FROM StudentCourses
  WHERE StudentCourses.studentID = param_studentID
  AND (StudentCourses.grade >= 5 OR StudentCourses.semester = param_currSemester)
)
OR
 Restrictors.restrictorID IS NULL
);
DECLARE CONTINUE HANDLER FOR NOT FOUND SET FINISHED := TRUE;
OPEN cur_nextClasses;

-- Loop that goes through cur_nextClasses results
nextClassLoop: LOOP

  -- Get the current course number that´s in cur_nextClasses results
  FETCH cur_nextClasses INTO currCourseNumber;
  
  -- if done, then quit
  IF finished THEN 
	LEAVE nextClassLoop;
  END IF;
  
  -- There´s a problem where you can be assigned to the same class because there might be two or more restrictors...
  -- An example of this would be as follows
  
  
  -- courseNumber	trackID		courseNumber	restictorID		restrictorType
  -- STÆ303			9			STÆ303			STÆ203			1
  -- STÆ303			9			STÆ303			STÆ313			2

INSERT IGNORE INTO StudentCourses (studentID, trackID, courseNumber, grade, semester)
VALUES(param_studentID, param_trackID, currCourseNumber, defaultGrade, param_nextsemester);

END LOOP nextClassLoop;

END //
DELIMITER ;

CALL AddMandatoryCourses(3, 9, '2018V','2018H');

SELECT TrackCourses.courseNumber, TrackCourses.trackID, TrackCourses.semester, Restrictors.courseNumber, Restrictors.restrictorID, Restrictors.restrictorType
  FROM TrackCourses
  LEFT JOIN Restrictors ON TrackCourses.courseNumber = Restrictors.courseNumber
  WHERE TrackCourses.courseNumber
  NOT IN (
	SELECT StudentCourses.courseNumber
    FROM StudentCourses
    WHERE StudentCourses.studentID = 1
    AND (StudentCourses.grade >= 5 OR StudentCourses.semester = '2019V')
  )
  AND TrackCourses.mandatory != 0
  AND TrackCourses.trackID = 9
  AND 
  (Restrictors.restrictorID IN (
  SELECT StudentCourses.courseNumber
    FROM StudentCourses
    WHERE StudentCourses.studentID = 1
    AND (StudentCourses.grade >= 5 OR StudentCourses.semester = '2019V')
   )
   OR
   Restrictors.restrictorID IS NULL);

DELIMITER //
DROP PROCEDURE IF EXISTS AddStudentCourses //
CREATE PROCEDURE AddStudentCourses (
  param_studentID INT,
  param_trackID INT,
  param_currSemester CHAR(10),
  param_nextSemester CHAR(10),
  param_courseNumber CHAR(10)
)
BEGIN

DECLARE defaultGrade INT DEFAULT 0;

IF ((SELECT COUNT(StudentCourses.courseNumber) FROM StudentCourses WHERE StudentCourses.studentID = param_studentID AND StudentCourses.semester = param_nextSemester) = 0) THEN
  CALL AddMandatoryCourses(param_studentID, param_trackID, param_currSemester, param_nextSemester);
END IF;

INSERT INTO StudentCourses (studentID, trackID, courseNumber, grade, semester) 
VALUES (param_studentID, param_trackID, param_courseNumber, defaultGrade, param_nextSemester);
END //

DELIMITER ;

-- in order not allow duplicates
ALTER TABLE StudentCourse ADD UNIQUE unique_index_st_tr_cd_se(studentID, trackID, courseNumber, semester);

CALL AddStudentCourses(1, 9, '2019V', '2019H', 'test101');