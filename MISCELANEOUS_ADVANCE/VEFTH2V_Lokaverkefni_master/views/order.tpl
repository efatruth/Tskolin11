<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <title>HraunHotel - order</title>
  <link rel="stylesheet" href="/static/css/main.css">
  <link rel="stylesheet" href="/static/css/normalize.css">
  <link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
</head>
<body>
	<header>
    <div class="navbar">
      <div class="box"><img src="/static/img/mynd.png" style="width: 82px;"></div>
      <div class="box2"><ul><li><a href="#viðburðir">Viðburðir</a></li><li><a href="#staff">Starfsfólk</a></li><li><a href="#umokkuer">Um okkur</a></li><li><a href="#pnata">Panta</a></li</ul></div>
      
  </header>

  <div class="wrapper-oreder">
  	<div class="login" id=id01>
  		<div class="contaner">
	  		<form action="/Hotel/{{hotel['name']}}/login" method="post">
	  			<div class="fyrstidalkur">
	  				<span onclick="document.getElementById('id01').style.display='none'" class="close" title="Close Modal">&times;</span>
	  				<div class="mynd"><img src="/static/img/mynd.png"></div>
	  			</div>
	  			<div class="seinni">
					<input type="text" placeholder="Notandanafn:" name="user" required>
					<input type="password" placeholder="Lykilorð:" name="password" required>
				    <input type="submit" name="submit" value="Skrá sig inn">
				</div>
  			</form>
  		</div>
  		
  	</div>
  	% if len(villa) != 0:
	  	<div class="alert">
	  		<span class="closebtn">&times;</span>  
	  		<strong>Villa!</strong>{{villa}}
	  	</div>
	% end
  	<div class="order">
  		<h1>Order</h1>
  			<div class="dalkar">
		  		<div class="fyrsti">
		  			<div class="textbox">
		  				<p>Ef þú átt notanda nú þegar getur skráð þig inn með því að ýta á takkan hér fyrir neðann. Þá sleppuru við að þurfa að skryfa upllýsingarnar sem eru beðnar um. Ef ekki slærð þú upllýsingarnar inn og færð notandaaðgang á sama tíma.</p>
		  				<button onclick="document.getElementById('id01').style.display='block'">Skrá sig inn</button>
		  			</div>
	  				<form action="/orderfinal" method="post">
		  			<div>
		  			<label>Hotel:</label>
		  			<select>
		  			% if hotel['name'] == 'Reykavik': 
		  			  <option selected value="Reykjavik">Hraun Hotel Reykjavík</soption>
		  			% else:
		  				<option  value="Reykjavik">Hraun Hotel Reykjavík</soption>
		  			% end

		  			% if hotel['name'] == 'Akureyri': 
		  			  <option selected value="Akureyri">Hraun Hotel Akureyri</soption>
		  			% else:
		  				<option value="Akureyri">Hraun Hotel Akureyri</soption>
		  			% end

		  			% if hotel['name'] == 'Selfoss': 
		  			  <option selected value="Selfoss">Hraun Hotel Selfoss</soption>
		  			% else:
		  				<option  value="Selfoss">Hraun Hotel Selfoss</soption>
		  			% end
		  			</select>
		  			</div>
		  			<p></p>
		  			<div>
		  			<select>
		  			  % if 	herbergi_uppl['herbergi'] == 'Guset':
			  			  % for x in range(10):
			  			  % if x+1 == 1:
			  			  	<option selected value="(x+1)">{{x+1}} Herbegi</option>
			  			  % else:
			  			  	<option  value="x+1">{{x+1}} Herbegi</option>
			  			  % end
			  			  % end
			  		  % else:
			  		   % for x in range(10):
			  			  	<option  value="x">{{x}} Herbegi</option>
			  			  % end
			  		  % end
					</select>
		  			<p>Guset(queen):</p>
		  			</div>
		  			<div>
		  			<select>
		  			  % if 	herbergi_uppl['herbergi'] == 'Suites':
			  			 % for x in range(10):
			  			  % if x+1 == 1:
			  			  	<option selected value="(x+1)">{{x+1}} Herbegi</option>
			  			  % else:
			  			  	<option  value="x+1">{{x+1}} Herbegi</option>
			  			  % end
			  			  % end
			  		  % else:
			  		   % for x in range(10):
			  			  	<option  value="x">{{x}} Herbegi</option>
			  			  % end
			  		  % end
					</select>

		  			<p>Suites(queen+bead):</p>
		  			</div>
		  			<div>
		  			<select>
		  			  % if 	herbergi_uppl['herbergi'] == 'Executive':
			  			 % for x in range(10):
			  			  % if x+1 == 1:
			  			  	<option selected value="(x+1)">{{x+1}} Herbegi</option>
			  			  % else:
			  			  	<option  value="x+1">{{x+1}} Herbegi</option>
			  			  % end
			  			  % end
			  		  % else:
			  		   % for x in range(10):
			  			  	<option  value="x">{{x}} Herbegi</option>
			  			  % end
			  		  % end
					</select>

		  			<p>Executive(King+queen):</p>
		  			</div>
		  			<input id="date" placeholder="checkin: " type="date" value="{{herbergi_uppl['checkin']}}" name="checkin" required readonly >
		  	</div>
		  	<div class="eftir">
		  		% if ifuser:
		  			<label>Notandanafn:</label>
			  		<input type="text" name="user" value="{{user['name']}}" readonly required>
			  		<label>Lykilorð:</label>
			  		<input type="password" name="password" value="blblblb" readonly required>
			  		<label>Fornafn:</label>
			   		<input type="text" name="fname" value="{{user['fname']}}" readonly required>
			  		<label>Eftirnafn:</label>
			  		<input type="text" name="lname" value="{{user['lname']}}" readonly required>
			  		<label>Kennitala:</label>
			  		<input type="text" name="ssn" value="{{user['ssn']}}" readonly required>
			  		<label>Phone:</label>
			  		<input type="Phone" name="phone" value="{{user['phone']}}" pattern="\d{3}(?:[\-\s]?)\d{4}" title="Sláðu inn 7 tölustafi" readonly required>
			  		<label>Mail:</label>
			  		<input type="mail" name="mail" value="{{user['mail']}}" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$" readonly required >
			  		
			  	% else: 
			  		<label>Notandanafn:</label>
			  		<input type="text" name="user" required>
			  		<label>Lykilorð:</label>
			  		<input type="password" name="password" required>
			  		<label>Fornafn:</label>
			  		<input type="text" name="fname" required>
			  		<label>Eftirnafn:</label>
			  		<input type="text" name="lname" required>
			  		<label>Kennitala:</label>
			  		<input type="text" name="ssn" required>
			  		<label>Phone:</label>
			  		<input type="Phone" name="phone" pattern="\d{3}(?:[\-\s]?)\d{4}" title="Sláðu inn 7 tölustafi" required>
			  		<label>Mail:</label>
			  		<input type="mail" name="mail" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$" required >
			  		
			  	% end
			  	<input placeholder="checkout: " id="date" type="date" name="checkout" value="{{herbergi_uppl['checkout']}}" required readonly style="margin-top: 1em"; > 

		  		
		  	</div>
		</div>
		<input type="submit" name="Klára pöntun" value="Klára pöntun">
		</form>
  	</div>
  </div>

  <footer>
  <div class="wrapper">
    <div class="box"><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    </p></div>
    <div class="box"><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    </p></div>
    <div class="box"><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    </p></div>
  </div>
  <div class="footer"><p>Róbert Ingi - Pétur Steinn - Helgi Tuan</p></div>
</footer>
  
</body>
</html>
<script>
var login = document.getElementById('id01');

window.onclick = function(event) {
    if (event.target == login) {
        login.style.display = "none";
    }
}
</script>

</body>


<script>
	var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
    close[i].onclick = function(){

        var div = this.parentElement;

        div.style.opacity = "0";


        setTimeout(function(){ div.style.display = "none"; }, 600);
    }
}
</script>