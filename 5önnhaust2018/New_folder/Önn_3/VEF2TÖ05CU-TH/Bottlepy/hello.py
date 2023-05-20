"""
from bottle import route, run

@route('/hello')
def hello():
    return "Get out"

run(host='localhost', port=8080, debug=True)
"""
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)

# http://localhost:8080/hello/YourName