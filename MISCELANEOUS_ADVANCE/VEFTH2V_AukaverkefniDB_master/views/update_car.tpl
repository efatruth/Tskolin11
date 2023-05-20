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
<div class="register_car">
    <form class="" action="/db/update" method="POST">
    <fieldset>
      <legend>Nýskrá bifreið</legend>
      <br>
      <label>Skráningarnúmer</label>
      <input type="text" name="skr_nr" value="{{bill[0]}}" required>
      <br><br>
      <label>Tegund</label>
      <input type="text" name="tegund" value="{{bill[1]}}" required>
      <br><br>
      <label>Verksmiðjunúmer</label>
      <input type="text" name="vrk_nr" value="{{bill[2]}}" required>
      <br><br>
      <label>Skráningardagur</label>
      <input type="text" name="skr_dags" value="{{bill[3]}}" required placeholder="YYYY-MM-DD">
      <br><br>
      <label>CO2 gildi</label>
      <input type="number" name="co2" value="{{bill[4]}}" required>
      <br><br>
      <label>Þyngd</label>
      <input type="number" name="thyngd" value="{{bill[5]}}" required>
      <br><br>
      <label>Skoðunardagur</label>
      <input type="text" name="sko_dags" value="{{bill[6]}}" required placeholder="YYYY-MM-DD">
      <br><br>
      <label>Staða</label>
      <!--input type="text" name="stada" value="" required-->
      <select class="" name="stada" required>
        <!--option value="Í umferð">Í umferð</option-->
        <!--option value="Úr umferð">Úr umferð</option-->
        <option value="{{bill[7]}}" selected>{{bill[7]}}</option>
        % if bill[7] == "Í umferð":
        <option value="Úr umferð">Úr umferð</option>
        % else:
        <option value="Í umferð">Í umferð</option>
        % end
      </select>
      <br><br>
      <input type="submit" name="" value="Submit">
    </fieldset>
  </form>
</div>



  <!--form class="" action="/db/update" method="post">
    <fieldset>
      <legend>Breyta</legend>
      <label>Skráningarnúmer: </label>
      <input type="text" name="skr_nr" value="{{bill[0]}}" required>
      <br><br>
      <label>Tegund: </label>
      <input type="text" name="tegund" value="{{bill[1]}}" required>
      <br><br>
      <label>Verksmiðjunúmer: </label>
      <input type="text" name="vrk_nr" value="{{bill[2]}}" required>
      <br><br>
      <label>Skráningardagur: </label>
      <input type="text" name="skr_dags" value="{{bill[3]}}" required>
      <br><br>
      <label>CO2 gildi: </label>
      <input type="number" name="co2" value="{{bill[4]}}" required>
      <br><br>
      <label>Þyngd: </label>
      <input type="number" name="thyngd" value="{{bill[5]}}" required>
      <br><br>
      <label>Skoðunardagur: </label>
      <input type="text" name="sko_dags" value="{{bill[6]}}" required>
      <br><br>
      <label>Staða: </label>
      <input type="text" name="stada" value="{{bill[7]}}" required>
      <br><br>
      <input type="submit" name="" value="Uppfæra">
    </fieldset>
  </form-->
  <a href="/">Heim</a>
</body>

</html>
