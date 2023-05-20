<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="/static/master.css">
  <title>Verkefni - 4</title>

</head>

<body>
  <div class="limiter">
    <div class="container-table100">
      <div class="wrap-table100">
        <div class="table100">
          <table>
            <thead>
              <tr class="table100-head">
                <th>Kennitala</th>
                <th>Nafn</th>
                <th>Braut</th>
              </tr>
            </thead>
            <tbody>
              % for nemandi in bekkur['nemendur']:
              <tr>
                <td><a href="/nemandi/{{nemandi['kt']}}">{{nemandi['kt']}}</a></td>
                <td>{{nemandi['nafn']}}</td>
                <td>{{nemandi['braut']}}</td>
              </tr>
              % end
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</body>

</html>