<!DOCTYPE html>
<html>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <title>Verkefni - 7</title>
  <link rel="stylesheet" href="/static/css/master.css">
  <link rel="stylesheet" href="/static/css/normalize.css">
  <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
</head>

<body>
  <div class="head">
    <div class="logo-place">
      <div class="info-logo"><img src="static/img/starbucks.svg"></div>
    </div>
    <div class="search-place">
      <div class="search">
        <span class="search-caption">Leita&nbsp;&nbsp;|&nbsp;&nbsp;</span>
        <div class="box">
          <div class="container-4">
            <form class="" action="#">
            <input type="search" name="q" id="search" placeholder="Vara A, B, C" />
            <button class="icon"><i class="fa fa-search"></i></button>
          </form>
          </div>
        </div>
      </div>
    </div>
    <div class="links-place">
      <ul>
        <li><a href="/">Heim</a></li>
        % from bottle import request
        % if request.get_cookie("account", secret='some-secret-key'):
        <li><a href="/signout">Skrá út</a></li>
        % else:
        <li><a href="/signin">Skrá inn</a></li>
        % end
        % if request.get_cookie("account", secret='some-secret-key') == "admin":
        <li><a href="/restricted">Restricted area</a></li>
        % end
      </ul>
    </div>
  </div>
  <div class="wrapper">
    <div class="login-view"> <!-- Ikr lazy programming smh-->
      <h4>Verkefni - 7</h4>
      <h5>Pétur Steinn</h5>
      <p><a href="/shop">Shop</a> | <a href="/signin">Login</a></p>
    </div>
  </div>
  <footer>
    <section class="footer-content">
      <div class="">
      </div>
      <div class="github">
        <a href="https://github.com/PeturSteinn/VEFTH2V-Verkefni_7">
          <div class=""><img src="/static/img/github.svg" alt=""></div>
          <div class="">GitHub</div>
        </a>
      </div>
      <div class="signature">
        <p>© Pétur Steinn Guðmundsson</p>
      </div>
    </section>
  </footer>

</body>

</html>
