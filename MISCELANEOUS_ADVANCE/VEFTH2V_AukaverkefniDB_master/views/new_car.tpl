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
  % if len(errormsg) != 0:
  <h3 style="text-align:center;color:#fff;text-transform:uppercase;text-decoration:underline;">{{errormsg}}</h3>
  % end
  <div class="register_car">
    <form class="" action="/db/add" method="POST">
      <fieldset>
        <legend>Nýskrá bifreið</legend>
        <br>
        <label>Skráningarnúmer</label>
        <input type="text" name="skr_nr" value="" required>
        <br><br>
        <label>Tegund</label>
        <input type="text" name="tegund" value="" required>
        <br><br>
        <label>Verksmiðjunúmer</label>
        <input type="text" name="vrk_nr" value="" required>
        <br><br>
        <label>Skráningardagur</label>
        <input type="text" name="skr_dags" value="" required placeholder="YYYY-MM-DD">
        <br><br>
        <label>CO2 gildi</label>
        <input type="number" name="co2" value="" required>
        <br><br>
        <label>Þyngd</label>
        <input type="number" name="thyngd" value="" required>
        <br><br>
        <label>Skoðunardagur</label>
        <input type="text" name="sko_dags" value="" required placeholder="YYYY-MM-DD">
        <br><br>
        <label>Staða</label>
        <!--input type="text" name="stada" value="" required-->
        <select class="" name="stada" required>
          <option value="Í umferð" selected>Í umferð</option>
          <option value="Úr umferð">Úr umferð</option>
        </select>
        <br><br>
        <input type="submit" name="" value="Submit">
      </fieldset>
    </form>
  </div>
  <a href="/">Heim</a>
</body>

</html>
