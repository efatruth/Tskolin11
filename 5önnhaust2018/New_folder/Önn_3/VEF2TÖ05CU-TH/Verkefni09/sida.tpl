<!DOCTYPE html>
<html>
<head>
	<title>Pictures with json</title>
</head>
<body>

<h1>Hey biches</h1>
<br>
<table>
% for i in data:
    <tr>
        <td><h2> {{i['name']}} </h2>
        <td><img src="{{i['imageSource']}}" width="400px" height="400px"></td>
     </tr>
% end
</table>
</body>
</html>