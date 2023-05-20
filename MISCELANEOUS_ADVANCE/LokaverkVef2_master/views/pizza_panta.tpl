<!DOCTYPE html>
	<html>
	<head>
		<title></title>
		<link rel="stylesheet" type="text/css" href="/static/css/pizza.css">
	</head>
	<body>
		<div class="logout_takki">
			<a href="/">&#8592;</a>
			<a href="/heimasida">&#8962;</a>
		</div>
		<nav>
			<div class="first_last">
				<div class="first">
					<img class="logo" src="/static/img/logo.png">
				</div>
				<div class="mid">
					<div class="minar_sidur_takki">
						<a href="/minar"><u>MÍNAR SÍÐUR</u></a>
					</div>
				</div>
				<div class="last">
					<div class="panta_takki">
						<a href="/panta">PANTA</a>
					</div>
				</div>
			</div>
		</nav>
		<article>
			<section>
				<form method="post" action="/panta">
					<h3>Botn</h3>
					Hvernig botn má bjóða þér?<p>
					<input type="radio" name="bottom" value="Klassiskur">Klassískur<br>
					<input type="radio" name="bottom" value="Italskur">Ítalskur<br>
					<input type="radio" name="bottom" value="Lauflettur">Laufléttur<br>
					<input type="radio" name="bottom" value="Ponnu">Pönnu

					<h3>Pizzustærð</h3>
					Hvaða stærð má bjóða þér?<p>
					<input type="radio" name="size" value="1000">9 tomma - 1000 kr.<br>
					<input type="radio" name="size" value="1500">12 tomma - 1500 kr.<br>
					<input type="radio" name="size" value="2000">18 tomma - 2000 kr.

					<h3>Val um álegg</h3>
					Hvaða álegg má bjóða þér?<p>
					Hvert álegg kostar 200 kr.<p>
					<input type="checkbox" name="topping" value="200">Skinka<br>
					<input type="checkbox" name="topping" value="200">Ananas<br>
					<input type="checkbox" name="topping" value="200">Pepperoni
					<br><br>

					<input type="submit" name="submit_takki" value="PANTA">
				</form>
			</section>
		</article>
	</body>
</html>