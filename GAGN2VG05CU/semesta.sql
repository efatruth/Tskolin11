create table Semesters
(
	semesterID int auto_increment,
    semesterName char(10) not null,
    semesterStarts date not null,
    semesterEnds date not null,
    academicYear char(10) null,
    constraint semester_PK primary key(semesterID)
);

insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Haust2015','2015-08-01','2015-12-31','2015-2016');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Vor2016','2016-01-01','2016-05-31','2015-2016');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Haust2016','2016-08-01','2016-12-31','2016-2017');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Vor2017','2017-01-01','2017-05-31','2016-2017');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Haust2017','2017-08-01','2017-12-31','2017-2018');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Vor2018','2018-01-01','2018-05-31','2017-2018');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Haust2018','2018-08-01','2018-12-31','2018-2019');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Vor2019','2019-01-01','2019-05-31','2018-2019');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Haust2019','2019-08-01','2019-12-31','2019-2020');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Vor2020','2020-01-01','2020-05-31','2019-2020');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Haust2020','2020-08-01','2020-12-31','2020-2021');
insert into Semesters(semesterName,semesterStarts,semesterEnds)values('Vor2021','2021-01-01','2021-05-31','2020-2021');