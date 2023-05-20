from bottle import run, route

@route('/')
def index():
    return """
<!DOCTYPE html>
<html>
    <head>
	    <title>index sida</title>
    </head>
<body>
    <h1> Hérna er index síðan. </h1>
    <ul>
        <li> <a href="/jobs/">Steve Jobs</a> </li>
        <li> <a href="/biography/"> Um hann (Biography)</a> </li>
        <li> <a href="/pictures/"> Myndir </a> </li>
    </ul>
</body>
</html>
"""

@route('/jobs/')
def jobs():
    return """
    <!DOCTYPE html>
<html>
    <head>
	    <title>Steve</title>
    </head>
<body>
    <p>Steve jobs er gaurinn sem gerði eplið.</p>
    <a href="/"> Til baka </a>
</body>
</html>
    """

@route('/biography/')
def biography():
    return """
    <!DOCTYPE html>
<html>
    <head>
	    <title>Biography</title>
    </head>
<body>
    <p>Hann var ungur og var svo frægur eftir á o.s.frv.</p>
    <a href="/"> Til baka </a>
</body>
</html>
    """

@route('/pictures/')
def pictures():
    return """
    <!DOCTYPE html>
<html>
    <head>
	    <title>Steve</title>
    </head>
<body>
    <p>Hér á myndir af steve jobb að vera.</p>
    <a href="/"> Til baka </a>
</body>
</html>
    """

run(host='localhost', port='8080')