#Along A. Loftsson
from bottle import route, run, template, redirect
import urllib.request, json

with urllib.request.urlopen('http://apis.is/concerts') as url:
    gigs = json.loads(url.read().decode())


@route('/')
def index():
    return template('concertplay.tpl', data = gigs)

run(host="localhost", port="8080", reloader=True, debug=True)