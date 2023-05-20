<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title>Verkefni - 5</title>
  <link rel="stylesheet" href="static/master.css">
</head>

<body>
  <div class="top-bar">
    <p>Fáðu miða í dag!</p>
  </div>
  <section class="wrapper">
    % for event in data['results']:
    <div class="event">
      <div class="top">
        <h2 class="date">{{event['eventDateName']}}</h2>
        <h3>{{event['eventHallName']}}</h3>
        <p>Dags. {{event['dateOfShow'][:10]}} Kl: {{event['dateOfShow'][11:16]}}</p>
      </div>
      <img src="{{event['imageSource']}}" alt="">
    </div>
    % end
  </section>
</body>

</html>