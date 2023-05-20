<!DOCTYPE html>
<html>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <title>Stöð - {{stod[0]['company']}}</title>
  <link rel="stylesheet" href="/static/css/master.css">
  <link rel="stylesheet" href="/static/css/normalize.css">
  <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
  <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
</head>

<body>
  <div class="nav-bar">
    <div class="selection">
      <label for="toggle"></label>
      <input class="menu-input" type="checkbox" id="toggle">
      <div class="menu-slide-in">
        <ul>
          <li><a href="/">&nbsp;&nbsp;Forsíða&nbsp;&nbsp;</a></li>
          <li><a href="/stodvar">&nbsp;&nbsp;Bensínstöðvar&nbsp;&nbsp;</a></li>
          <li><a href="/about">&nbsp;&nbsp;Um #síða&nbsp;&nbsp;</a></li>
        </ul>
      </div>
    </div>
    <div class="search">
      <span>Leita&nbsp;&nbsp;|&nbsp;&nbsp;</span>
      <div class="box">
        <div class="container-4">
          <input type="search" id="search" placeholder="Olís, N1, Orkan..." />
          <button class="icon"><i class="fa fa-search"></i></button>
        </div>
      </div>
    </div>
    <div class="about">
      <a href="/about">About</a>
    </div>
  </div>
  <section class="wrapper-result">
    <section class="logo-container">
      <img src="/static/img/{{stod[0]['key'][:2]}}.svg" class="station-logo">
    </section>
    <div class="intro-with-logo">
      <p>{{stod[0]['company']}}</p>
    </div>
    <h3>Fjöldi stöðva: {{len(stod)}}</h3>
    <section class="stodvar-specific">
      % for i in stod:
      <div class="stod-uppl-block">
        <div class="header">
          {{i['name']}}
        </div>
        <div class="content">
          <p><b>Bensín:</b>&nbsp;{{i['bensin95']}}</p>
          <p><b>Diesel:</b>&nbsp;&nbsp;{{i['diesel']}}</p>
          <p><b>Afsláttarverð á bensíni:</b>&nbsp;{{i['bensin95_discount']}}</p>
          <p><b>Afsláttarverð á diesel:</b>&nbsp;&nbsp;{{i['diesel_discount']}}</p>
          <a href="/stod/{{i['company']}}/{{i['key']}}">Skoða á korti</a>
        </div>
      </div>
      % end
    </section>
    <p class="last-update">Síðast uppfært: {{lastPriceCheck[0]}} kl: {{lastPriceCheck[1]}}</p>
  </section>
  <footer>
    <section class="footer-content">
      <div class=""></div>
      <div class="github">
        <a href="https://github.com/PeturSteinn/VEFTH2V-Verkefni_6">
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
