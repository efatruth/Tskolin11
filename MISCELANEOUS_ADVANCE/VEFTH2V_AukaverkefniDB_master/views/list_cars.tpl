<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AukaverkefniDB</title>
  <link rel="stylesheet" href="/static/css/master.css">
  <link rel="stylesheet" href="/static/css/normalize.css">
  <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
</head>

<body>
  <div class="head">
    <span class="head-title">Bíla Database</span>
  </div>
  <div class="" style="text-align: center;margin-top:.4em;font-size:2em;">
    <a href="/" style="color:#fff;">Heim</a>
  </div>
  <div class="car-panel">
    % for bill in bilar:
    <div class="">
      % for count, stat in enumerate(bill):
      % if count == 0:
      <p><span>Bílnúmer:</span> {{stat}}</p>
      % elif count == 1:
      <p><span>Tegund:</span> {{stat}}</p>
      % elif count == 2:
      <p><span>Verksmiðjunúmer:</span> {{stat}}</p>
      % elif count == 3:
      <p><span>Skráningardagur:</span> {{stat}}</p>
      % elif count == 4:
      <p><span>Mengun CO<sub>2</sub>:</span> {{stat}}/gr</p>
      % elif count == 5:
      <p><span>Þyngd:</span> {{stat}}</p>
      % elif count == 6:
      <p><span>Skoðun:</span> {{stat}}</p>
      % elif count == 7:
      <p><span>Staða:</span> {{stat}}</p>
      % end
      % end
      <a href="/db/delete/{{bill[0]}}">Eyða bifreið</a>
      <a href="/db/update/{{bill[0]}}">Breyta bifreið</a>
    </div>
    % end
  </div>
</body>
</html>
