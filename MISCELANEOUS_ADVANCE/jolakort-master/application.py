import os
from bottle import route, run, static_file, error, template

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./resources')

@route('/')
def index():
    return template('views/index')

@error(404)
def error404(error):
    return template('views/error404')


run(host="0.0.0.0", port=os.environ.get('PORT'))
# run(debug=True, reloader=True)
