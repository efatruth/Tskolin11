use ProgressTracker_V5;
/*
	Skrifið stored procedure sem leggur saman allar einingar sem nemandinn hefur lokið á ákv.
	námskeiðum.
	ATH:
	Á tölvubrautinni tilheyra almennu fögin strangt til tekið Tæknimenntaskólanum(NTT13
	Náttúrufræðibraut tölvutækni). Það þýðir að hafi nemandi lokið fjórum þriggja eininga áföngum í
	t.d. eðlisfræði og stærðfræði og fimm þriggja eininga kúrsum á tölvubraut þá fæst eitthvað svona:
	NTT13 12  BR16  15
	Aðeins skal velja áfanga þar sem einkunn er >= 5.
	Sé verið að nota staðið/fallið þá skal velja "staðið".
*/
select R.trackID, sum(C.courseCredits)
from Registration R 
inner join TrackCourses on R.trackID = TrackCourses.TrackID and R.courseNumber = TrackCourses.courseNumber  -- ATH þessa línu vegna samsett FK.
inner join Courses C on TrackCourses.courseNumber = C.courseNumber
and R.studentID = 3
and R.passed = true
group by R.trackID;
