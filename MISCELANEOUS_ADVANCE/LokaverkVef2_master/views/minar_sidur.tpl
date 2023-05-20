<!DOCTYPE html>
	<html>
	<head>
		<title></title>
		<link rel="stylesheet" type="text/css" href="/static/css/pantanir.css">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
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
						<u>MÍNAR SÍÐUR</u>
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
		<h1>MÍNAR PANTANIR</h1>
		% for i in data:
			<table>
				<tbody>
                    <tr>
                        <td>Notandi</td>
                        <td>{{i[0]}}</td>
                    </tr>
                    <tr>
                        <td>Botn</td>
                        <td>{{i[1]}}</td>
                    </tr>
                    <tr>
                        <td>Stærð</td>
                        <td>{{i[2]}}</td>
                    </tr>
                    <tr>
                        <td>Fjöldi álegg</td>
                        <td>{{i[3]}}</td>
                    </tr>
                    <tr>
                        <td>Heildarverð</td>
                        <td>{{i[4]}}</td>
                    </tr>
				</tbody>
			</table>
			<br><br>
		% end
		</article>
	</body>
</html>