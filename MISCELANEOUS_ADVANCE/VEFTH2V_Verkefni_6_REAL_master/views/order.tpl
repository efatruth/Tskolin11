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
  <h1 style="text-align: center;">Pöntunin er tilbúin!</h1>
  <section class="wrapper" style="display:grid; grid-template-columns: 1fr 1fr;">
    <div class="col-1">
      <h2 style="text-decoration: underline;">Kaupandi</h2>
      <p>Fullt nafn:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{fullname}}</p>
      <p>Heimilisfang:&nbsp;&nbsp;{{heimili}}</p>
      <p>Netfang:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{netfang}}</p>
      <p>Símanúmer:&nbsp;&nbsp;&nbsp;{{simi}}</p>
    </div>
    <div class="col-2">
      <h2 style="text-decoration: underline;">Pizza</h2>
      <p>Stærð: {{pizzasize}}"</p>
      <p>Álegg:
      % if len(alegg) == 0:
        ekkert
      % else:
      % for item in range(len(alegg) - 1):
        {{alegg[item]}},&nbsp;
      % end
      {{alegg[-1]}}
    </p>
    <p>Verð: {{verd}},-</p>
    <p>Vsk: {{int(verd * vsk)}},-</p>
    <p>Heildarverð: {{int(verd * (1 + vsk))}},-</p>
    </div>
  </section>
  <a href="/" style="display:block;text-align: center;">Aftur heim</a>
</body>

</html>
