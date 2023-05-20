<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>Verkefni - 6 REAL</title>
  <link rel="stylesheet" href="/static/css/master.css">
  <link rel="stylesheet" href="/static/css/normalize.css">
</head>

<body>
  <div class="head">
    <p>Robba Pítsur</p>
  </div>
  <h1 style="text-align: center;">Skráður í Robba Pítsur</h1>
  <section class="wrapper">
    % if userExists == True:
    <div class="center">Email nú þegar í notkun!</div>
    % else:
    <div class="center">
      <p>Velkomin/nn: {{nafn}}</p>
    </div>
    % end
    <a href="/" style="display:block;text-align: center;">Aftur heim</a>
  </section>
</body>

</html>
