from bottle import *
from sys import argv

@route('/')
def app():
    return "<h1>Kypler er kominn á Heroku</h1>"

run(host='0.0.0.0', port=argv[1], debug=True, reloader=True)