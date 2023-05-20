<!DOCTYPE html>
<html>
	<head>
		<title></title>
	</head>
	<body>
	    <h2>Kerra</h2>
	    % for i in pro1:
	        {{ i }}<br>
	    % end
	    <p>
		<form method="get" action="/">
			<input type="submit" name="submit" value="Til Baka">
		</form>
	</body>
</html>