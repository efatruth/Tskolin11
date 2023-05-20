import os, json
from bottle import route, run, static_file, error, request, template

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./resources')

with open('resources/bekkur.json', 'r', encoding='UTF-8') as file:
    bekkur = json.load(file)

@route('/')
def index():
    return template('index', bekkur = bekkur)

@route('/nemandi/<n>')
def nemandi(n):
    for nemandi in bekkur['nemendur']:
        if nemandi['kt'] == n:
            return template('user', nemandi = nemandi)
    else:
        return error500()


@error(404)
def error404(error):
    return '''<h1>Úps...</h1><h3>Síðan sem þú baðst um finnst ekki.</h3>
           <h3><a href="/">Á heimasíðu</a></h3>
           '''
@error(500)
def error500(error):
    return '''<h1>Úps...</h1><h3>Síðan sem þú baðst um finnst ekki.</h3>
           <h3><a href="/">Á heimasíðu</a></h3>
           '''

run(host="0.0.0.0", port=os.environ.get('PORT'))










