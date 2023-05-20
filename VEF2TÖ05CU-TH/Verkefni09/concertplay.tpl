<!DOCTYPE html>
<html>
<head>
	<title>Concerts happening</title>
</head>
<body>
<h1>Hey biches</h1>
% for i in data['results']:
        <img src="{{i['imageSource']}}">
        <br>
        <b>Name:</b> {{i['eventDateName']}}
        <br>
        <b>Placement:</b> {{i['eventHallName']}}
        <br>
        <b>Time:</b> {{i['dateOfShow']}}
        <br>
% end
</body>
</html>