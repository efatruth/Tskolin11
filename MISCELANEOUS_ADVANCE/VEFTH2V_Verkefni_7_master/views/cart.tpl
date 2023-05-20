<!DOCTYPE html>
<html>

<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta charset="utf-8">
  <title>Verkefni - 7</title>
  <link rel="stylesheet" href="/static/css/master.css">
  <link rel="stylesheet" href="/static/css/normalize.css">
  <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
</head>

<body>
  <div class="head">
    <div class="logo-place">
      <div class="info-logo"><img src="static/img/starbucks.svg"></div>
    </div>
    <div class="search-place">
      <div class="search">
        <span class="search-caption">Leita&nbsp;&nbsp;|&nbsp;&nbsp;</span>
        <div class="box">
          <div class="container-4">
            <form class="" action="#">
              <input type="search" name="q" id="search" placeholder="Vara A, B, C" />
            <button class="icon"><i class="fa fa-search"></i></button>
          </form>
          </div>
        </div>
      </div>    </div>
    <div class="links-place">
      <ul>
        % from bottle import request
        <li><a href="/">Heim</a></li>
        % if request.get_cookie("account", secret='some-secret-key'):
        <li><a href="/signout">Skrá út</a></li>
        % else:
        <li><a href="/signin">Skrá inn</a></li>
        % end
        % if request.get_cookie("account", secret='some-secret-key') == "admin":
        <li><a href="/restricted">Restricted area</a></li>
        % end
      </ul>
    </div>
  </div>
  <div class="wrapper">
    <div class="shop-container">
      <div class="side-panel">
        <ul>
          <li><a href="/shop">Shop</a></li>
          <li><a href="#">Category&nbsp;1</a></li>
          <li><a href="#">Category&nbsp;2</a></li>
          <li><a href="#">Category&nbsp;3</a></li>
          <li><a href="#">Category&nbsp;4</a></li>
          <li><a href="#">Category&nbsp;5</a></li>
          <li><a href="#">Category&nbsp;6</a></li>
          <li><a href="#">Category&nbsp;7</a></li>
          <li><a href="#">Category&nbsp;8</a></li>
          <li><a href="#">Category&nbsp;9</a></li>
        </ul>
      </div>
      <div class="product-panel">
        % if len(cart) <= 0:
        <h4 style="text-align:center;">Engu hefur verið bætt við í körfuna...</h4>
        % else:
        <h3 style="text-align:center;">Karfan mín</h3>
        <table>
          <thead>
            <tr>
              <th scope="col">Vöruheiti</th>
              <th scope="col">Vörunúmer</th>
              <th scope="col">Verð</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            % for item in cart:
            <tr>
              <td data-label="Vöruheiti">{{item['name']}}</td>
              <td data-label="Vörunúmer">{{item['pid']}}</td>
              <td data-label="Verð">
                % tmp = "{:,},-".format(item['cost'])
                {{tmp}}
              </td>
              <td><a href="/cart/remove/{{item['pid']}}" style="text-decoration:none;color:grey;">X</a></td>
            </tr>
            % end
          </tbody>
          <tfoot>
            <tr>
              <td data-label="">Heildarverð</td>
              <td></td>
              % heildarverd = 0
              % for item in cart:
              %   heildarverd += item['cost']
              % end
              <td>
                % tmp = "{:,},-".format(heildarverd)
                {{tmp}}
              </td>
              <td></td>
            </tr>
          </tfoot>
        </table>
        <h3 style="text-align:center;"><a href="/cart/remove" style="color:#fff;">Hreinsa allt úr körfu</a></h3>
      </div>
    </div>
  </div>
  <footer>
    <section class="footer-content">
      <div class="">

      </div>
      <div class="github">
        <a href="https://github.com/PeturSteinn/VEFTH2V-Verkefni_7">
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
