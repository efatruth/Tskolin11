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
              <tr>
                <td>{{nemandi['kt']}}</td>
                <td>{{nemandi['nafn']}}</td>
                <td>{{nemandi['braut']}}</td>
              </tr>
            </tbody>
            <tfoot>
              <tr>
                <td colspan="3"><a href="/">Til baka</a></td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>
    </div>
  </div>
</body>

</html>

<!--{{nemandi['kt']}} {{nemandi['nafn']}} {{nemandi['braut']}}-->