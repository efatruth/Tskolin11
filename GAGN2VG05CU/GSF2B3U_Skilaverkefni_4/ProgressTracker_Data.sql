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

insert into Tracks(trackName,divisionID)values('Almennt nám Upplýsingatækniskóla - AN UTN',11);
insert into Tracks(trackName,divisionID)values('Bókband',11);
insert into Tracks(trackName,divisionID)values('Grafísk miðlun',11);
insert into Tracks(trackName,divisionID)values('Grunnnám upplýsinga- og fjölmiðlagreina',11);
insert into Tracks(trackName,divisionID)values('K2 Tækni- og vísindaleiðin',11);
insert into Tracks(trackName,divisionID)values('Ljósmyndun',11);
insert into Tracks(trackName,divisionID)values('Prentun',11);
insert into Tracks(trackName,divisionID)values('Stúdentspróf',10);
insert into Tracks(trackName,validFrom,divisionID)values('Tölvubraut TBR16 - stúdentsbraut','2016-08-01',11);
insert into Tracks(trackName,divisionID)values('NTT13 Náttúrufræðibraut tölvutækni',10);

insert into Courses(courseNumber,courseName,courseCredits)
values('GSF2A3U','Gagnasafnsfræði I',5),
	  ('GSF2B3U','Gagnasafnsfræði II',5),
	  ('GSF3A3U','Gagnanotkun',5),
	  ('GSF3B3U','Gagnagreining',5);
insert into Courses(courseNumber,courseName,courseCredits)
values('FOR3G3U','Inngangur að leikjaforritun',5),
	  ('FOR3L3U','Leikjaforritun',5),
	  ('FOR3D3U','3D leikjaforritun',5);
insert into Courses(courseNumber,courseName,courseCredits)
values('STÆ103','Inngangur að stærðfræði',5),
	  ('STÆ203','Algebra',5),
	  ('STÆ303','Rúmfræði',5),
      ('STÆ313','Tölfræði',5),
      ('STÆ403','Vektorar',5),
      ('STÆ503','Diffrun og Heildun',5),
      ('STÆ603','Stærðfræðigreining',5);
insert into Courses(courseNumber,courseName,courseCredits)
values('EÐL103','Eðlisfræði I',5), 
	  ('EÐL203','Eðlisfræði II',5),
	  ('EÐL303','Eðlisfræði III',5),
	  ('EÐL403','Eðlisfræði IV',5);

insert into Student(firstName,lastName,dob)values('Guðrún','Ólafsdóttir','1999-03-31');
insert into Student(firstName,lastName,dob)values('Andri Freyr','Kjartansson','2000-11-01');
insert into Student(firstName,lastName,dob)values('Tinna Líf','Björnsson','1998-08-14');
insert into Student(firstName,lastName,dob)values('Magni Þór','Sigurðsson','2000-05-27');
insert into Student(firstName,lastName,dob)values('Rheza Már','Hamid-Davíðs','2001-09-17');
insert into Student(firstName,lastName,dob)values('Hadríra Gná','Schmidt','1999-007-29');

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

insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(9,'GSF2A3U',4,true);  
insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(9,'FOR3G3U',4,true);
insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(9,'FOR3D3U',5,true);
insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(9,'GSF2B3U',5,true);
insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(9,'GSF3B3U',5,true);
insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(10,'STÆ103',1,true);
insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(10,'EÐL103',1,true);
insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(10,'STÆ203',2,true);
insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(10,'EÐL203',2,true);
insert into TrackCourses(trackID, courseNumber,semester,mandatory)values(10,'STÆ303',3,true);

insert into Registration(studentID,trackID,courseNumber,registrationDate,passed)values(3,10,'STÆ103','2016-07-31',true);
insert into Registration(studentID,trackID,courseNumber,registrationDate,passed)values(3,9,'FOR3G3U','2018-05-16',true); 
insert into Registration(studentID,trackID,courseNumber,registrationDate,passed)values(3,10,'EÐL103','2016-07-31',true);
insert into Registration(studentID,trackID,courseNumber,registrationDate,passed)values(3,9,'GSF2A3U','2018-05-16',true);  
insert into Registration(studentID,trackID,courseNumber,registrationDate,passed)values(3,9,'FOR3D3U','2017-08-08',true);
insert into Registration(studentID,trackID,courseNumber,registrationDate,passed)values(3,10,'STÆ203','2017-01-01',true);
insert into Registration(studentID,trackID,courseNumber,registrationDate,passed)values(3,10,'STÆ303','2018-01-01',false);
