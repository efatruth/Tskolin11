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
  <div class="search-block">
    <div class="search">
      <span class="search-caption">Leita&nbsp;&nbsp;|&nbsp;&nbsp;</span>
      <div class="box">
        <div class="container-4">
          <form class="" action="/car_info">
          <input type="search" name="search" id="search" placeholder="Bílnúmer..." required/>
          <button class="icon"><i class="fa fa-search"></i></button>
        </form>
        </div>
      </div>
    </div>
  </div>
  % if len(errormsg) != 0:
  <h3 style="text-align:center;color:#fff;text-transform:uppercase;text-decoration:underline;">{{errormsg}}</h3>
  % end
  <div class="actions">
    <a href="/db/add">Bæta við bíl</a> |
    <a href="/db/list">Listi af öllum bílum</a>
  </div>
</body>

</html>
