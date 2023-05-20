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
  <h1 style="text-align: center;">Skrá mig í Robba Pítsur</h1>
  <section class="wrapper">
    <form class="sign-up-form" action="/sign_up/check" method="post">
      <label>Username: </label><input type="text" class="sign-up-label" name="nafn" value="" required pattern="(?=.*[a-z])(?=.*[A-Z]).{4,}">
      <label>Netfang: </label><input type="email" class="sign-up-label" name="netfang" value="" pattern="[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-z]+" required>
      <label>Password: </label><input type="password" class="sign-up-label" name="password" value="" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{4,}$" required>
      <input type="submit" name="sign_up" value="Skrá mig" style="display:block;margin-top:1em;">
    </form>
    <a href="/" style="display:block;text-align: center;">Aftur heim</a>
  </section>
</body>

</html>
