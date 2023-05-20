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
      </div>    </div>
    <div class="links-place">
      <ul>
        % from bottle import request
        <li><a href="/">Heim</a></li>
        % if request.get_cookie("account", secret='some-secret-key'):
        <li><a href="/signout">Skrá út</a></li>
        % else:
        <li><a href="#">Skrá inn</a></li>
        % end
        % if request.get_cookie("account", secret='some-secret-key') == "admin":
        <li><a href="/restricted">Restricted area</a></li>
        % end
      </ul>
    </div>
  </div>
  <div class="wrapper">
    <div class="login-view">
      <h4>Það eru engir almennir notendur hér, kennari!</h4>
      <h4>Aðeins er admin notandi og login credentials eru: <span style="font-weight: 300;">admin:admin</span></h4>
      <form class="" action="/login" method="post">
        <label>Notandanafn: <input type="text" class="sign-up-label" name="username" required></label><!--pattern="(?=.*[a-z])(?=.*[A-Z]).{4,}"-->
        <label>Lykilorð: <input type="password" class="sign-up-label" name="password" required></label> <!-- pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{4,}$"-->
        <input type="submit" name="sign_up" value="Skrá mig">
      </form>
    </div>
  </div>
  <footer>
    <section class="footer-content">
      <div class=""></div>
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
