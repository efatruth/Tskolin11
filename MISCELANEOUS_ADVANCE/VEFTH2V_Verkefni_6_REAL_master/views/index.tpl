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
  <section class="wrapper">
  <form class="" action="/order" method="get">
    <section class="wrapper-order-form">
      <div class="about">
        <h3>Hvert á að senda?</h3>
        <label>&nbsp;Nafn</label><input type="text" name="name" class="order-label" required pattern="(?=.*[a-z])(?=.*[A-Z]).{4,}">
        <label>&nbsp;Heimilisfang</label><input type="text" name="heimili" class="order-label" required>
        <label>&nbsp;Netfang</label><input type="email" name="netfang" class="order-label" required pattern="[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-z]+">
        <label>&nbsp;Símanúmer</label><input type="text" name="simi" class="order-label" pattern="\d{3}-?\d{4}" required title="Dæmi: 123-4567 eða 1234567">
        <input type="submit" name="order" value="Panta" class="submit-form" style="display: block;">
      </div>
      <div class="pizzasize">
        <h3>Stærð pizzu</h3>
        <span><input type="radio" name="pizzasize" class="order-label" value="9" id="9tommur" required><label for="9tommur">&nbsp;9"</label></span>
        <span><input type="radio" name="pizzasize" class="order-label" value="12" id="12tommur"><label for="12tommur">&nbsp;12"</label></span>
        <span><input type="radio" name="pizzasize" class="order-label" value="18" id="18tommur"><label for="18tommur">&nbsp;18"</label></span>
      </div>
      <div class="toppings">
        <h3>Hvað má bjóða þér?</h3>
        <span><input type="checkbox" name="pepperoni" class="order-label" value="pepperoni" id="pepperoni"><label for="pepperoni">&nbsp;Pepperoni</label></span>
        <span><input type="checkbox" name="beikonkurl" class="order-label" value="beikonkurl" id="beikonkurl"><label for="beikonkurl">&nbsp;Beikonkurl</label></span>
        <span><input type="checkbox" name="piparostur" class="order-label" value="piparostur" id="piparostur"><label for="piparostur">&nbsp;Piparostur</label></span>
        <span><input type="checkbox" name="rjomaostur" class="order-label" value="rjomaostur" id="rjomaostur"><label for="rjomaostur">&nbsp;Rjómaostur</label></span>
        <span><input type="checkbox" name="svarolifur" class="order-label" value="svartar ólífur" id="svarolifur"><label for="svarolifur">&nbsp;Svartar ólífur</label></span>
        <span><input type="checkbox" name="nachos" class="order-label" value="nachos" id="nachos"><label for="nachos">&nbsp;Nachos flögur</label></span>
      </div>
    </section>
  </form>
  <form class="sign-up" action="sign_up" method="get">
    <p>Elskaru pizzur xdd</p>
    <input type="submit" name="sign_up" value="Skrá mig" class="signup">
  </form>
</section>
</body>

</html>
