#Along A. Loftsson
from bottle import route, template, run
import urllib.request, json

with open('myndir.json') as File:
    jsonfile = json.load(File)


for i in jsonfile:
    variables = jsonfile[i]

@route('/')
def index():
    return template('sida.tpl', data = variables)

run(host="localhost", port="8080", reloader=True, debug=True)