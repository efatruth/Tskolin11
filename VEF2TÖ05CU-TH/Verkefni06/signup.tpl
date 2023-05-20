<!DOCTYPE html>
<html>
<head>
	<title>Skráningarform</title>
</head>
<body>

<form action="/send" method="post">

	<label>Nafn</label>
	<input type="text" placeholder="Sláðu inn Nafn" name="name" required>
	<br>
	<label>Notandnafn</label>
	<input type="text" placeholder="Sláðu inn Notandanafn" name="username" required>
	<br>
	<label>Netfang</label>
	<input type="email" placeholder="Sláðu inn Netfang" name="email" required>
	<br>
	<label>Lykilorð</label>
	<input type="password" placeholder="Sláðu inn Lykilorð" name="pass" minlength="5" maxlength="16" required>
	<br>
	<label>Sími</label>
	<input type="number" pattern="[0-9]" placeholder="Sláðu inn Símanúmer" maxlength="7" name="phone" required>
	<br><br>
	<input type="checkbox" name="agree" required>
	<label>By signing up you agree to our <a href="http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html">Terms and Conditions.</a></label>
	<br><br>
	<input type="submit" value="Sign Up">
</form>
</body>
</html>