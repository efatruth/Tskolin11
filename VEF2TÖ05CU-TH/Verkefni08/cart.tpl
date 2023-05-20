<!DOCTYPE html>
<html>
	<head>
		<title>Your Cart</title>
	</head>
	<body>
	    <h2>Your cart contains:</h2>
	    % for i in pro1:
	        {{ i }}<br>
	    % end
	    <p>
		<form method="get" action="/">
			<input type="submit" name="submit" value="Til Baka">
		</form>
	</body>
</html>