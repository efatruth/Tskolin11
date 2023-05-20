<!DOCTYPE html>
<html>
	<head>
		<title></title>
		<link rel="stylesheet" type="text/css" href="/static/css/shop.css">
	</head>
	<body>
	    <h2>Vörur</h2>
		<form method="post", action="/">
			<input type="checkbox" name="vara1" value="Vara 1" {{"checked" if 'vara1' in telja else ''}} id="vara1"/>Vara 1<p>

			<input type="checkbox" name="vara2" value="Vara 2" {{"checked" if 'vara2' in telja else ''}} id="vara2"/>Vara 2<p>

			<input type="checkbox" name="vara3" value="Vara 3" {{"checked" if 'vara3' in telja else ''}} id="vara3"/>Vara 3<p>

			<input type="checkbox" name="vara4" value="Vara 4" {{"checked" if 'vara4' in telja else ''}} id="vara4"/>Vara 4<p>


			<input type="submit" name="submit" value="Kerra">
		</form>
		<br>
		Þú hefur komið á þessa síðu {{oft}} sinnum.
	</body>
</html>