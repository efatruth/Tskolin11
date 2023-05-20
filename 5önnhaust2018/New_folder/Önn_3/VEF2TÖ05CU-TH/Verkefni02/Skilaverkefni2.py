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
        <li> <a href="/verkefni21/">Verkefni 2.1</a> </li>
        <li> <a href="/verkefni22/">Verkefni 2.2</a> </li>
        <li> <a href="/verkefni23/">Verkefni 2.3</a> </li>
        <li> <p> Verkefni 4 getur þú farið í gegnum með því að bæta við "/1-9" í URL address.
    </ul>
</body>
</html>
"""

#-------------------Verkefni 1---------------------
@route('/verkefni21/')
def verkefni21():
    return """<p> Hvað er beining (e.route) og hvernig gagnast það við vefsíðugerð? Útskýrðu með eigin orðum. </p>

<p> <b>Svar:</b> Það tengir efni við síðuna beint í það sem þú sérð í vefsíðunni. Það sparar bæði tíma og pening. </p>

<a href="/"> Til baka </a>
"""
#-------------------Verkefni 2---------------------
@route('/verkefni22/')
def verkefni22():
    return """
        Halló heimur!
        <a href="/">Til baka</a>
        """

#-------------------Verkefni 3---------------------
@route('/verkefni23/')
def verkefni23():
    return """
<!DOCTYPE html>
<html>
    <head>
	    <title>verkefni 2.3</title>
    </head>
<body>
    <p> Halló heimur! </p>
    <a href="/"> Til baka </a>
</body>
</html>
"""

#-------------------Verkefni 4---------------------

@route('/<id:int>')
def callback(id):
    if id == 1:
        return """
        <!DOCTYPE html>
<html>
    <head>
	    <title>id1</title>
    </head>
<body>
        <p> Gunnar </p>
        <a href="/"> Til baka </a>
</body>
</html>

        """
    elif id == 2:
        return """
        <!DOCTYPE html>
<html>
    <head>
	    <title>id2</title>
    </head>
<body>
        <p> Daníel </p>
        <a href="/"> Til baka </a>
</body>
</html>
        """
    elif id == 3:
        return """
        <!DOCTYPE html>
<html>
    <head>
	    <title>id3</title>
    </head>
<body>
        <p> Þórarinn </p>
        <a href="/"> Til baka </a>
</body>
</html>
        """
    else:
        return """
        <!DOCTYPE html>
<html>
    <head>
	    <title>id4+</title>
    </head>
<body>
        <p> Einhver stöðluð skilaboð. (Þetta var brandari) </p>
               <a href="/"> Til baka </a>
</body>
</html>
        """

run(host='localhost', port='8080')
