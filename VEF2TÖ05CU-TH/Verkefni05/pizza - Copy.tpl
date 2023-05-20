<!DOCTYPE html>
<html>
<head>
	<title>Jæja krakkar...</title>
</head>
<body>

<section>
<fieldset>
	<legend>Pizzupöntun</legend>
	<label>
		<form action="/" method="post">
			<p>Nafn <br> <input type="text" placeholder="Fullt Nafn" name="name" required></p>

			<p>Heimilisfang <br> <input type="text" placeholder="Heimilisfang" name="address" required></p>

			<p>Símanúmer <br> <input type="number" placeholder="58-12345" name="phone" required></p>

			<h3>Veldu stærð.</h3>

			<p>
				<label>
				<input type="radio" name="price" value="1000">
				09 tomma - 1000 kr.
				</label>
				<br>
			    <label>
				<input type="radio" name="price" value="1500">
				12 tomma - 1500 kr.
				</label>
				<br>
				<label>
				<input type="radio" name="price" value="2000">
				18 tomma - 2000 kr.
				</label>
			</p>
			<hr>
			<h3>Veldu álegg.</h3>
			<p>
			<input type="checkbox" name="price" value="200"> Skinka <br>
			<input type="checkbox" name="price" value="200"> Pepperoni <br>
			<input type="checkbox" name="price" value="200"> Hakk
			</p>
			<input class="takki" type="submit" value="PANTA">
		</form>

	</label>

</fieldset>
</section>


</body>
</html>