#Along A. Loftsson

from bottle import route, run, template, static_file, debug, response, request, redirect
import datetime
"""
@route('/test')
def hello():
    if request.get_cookie("name"):
        return "Hello: {0}".format(request.get_cookie("name"))
    else:
        response.set_cookie("name", "paul")
        return "Welcome !"

debug(True)
run(reloader=True)


@route('/')
def page():
    return template('mainpage.tpl')

@route('/signin')
def login():
    if request.get_cookie("name"):
        return template('secretsite.tpl')
    else:
        return template('login.tpl')

@route('/logged')
def secretsite():
    user = request.forms.get('username')
    password = request.forms.get('pass')
    re_user = user.replace(' ', '')
    re_pass = password.replace(' ', '')
    if request.get_cookie("name"):
        return template('secret.tpl')
    else:
        response.set_cookie("name", user)
        return template('secret.tpl')
"""

expire_date = datetime.datetime.now()
expire_date = expire_date + datetime.timedelta(days=90)


@route('/')
def page():
    if request.get_cookie("name", secret="secret-site"):
        return template('secretsite.tpl')
    else:
        return template('mainpage.tpl')

@route('/logout', method="post")
def logout():
    user = request.forms.get('username')
    password = request.forms.get('pass')
    name = user
    response.set_cookie("visited", "yes", max_age=0)
    response.set_cookie("name", name, secret="secret-site", max_age=0)
    redirect('/')

@route('/site', method="post")
def login():
    user = request.forms.get('username')
    password = request.forms.get('pass')
    name = user
    if user == "admin" and password == "admin":
        response.set_cookie("name", name, secret="secret-site", expires=expire_date)
        redirect('/')
    elif request.get_cookie("visited"):
        return template('error.tpl', message="Innskráning tókst ekki.")
    else:
        response.set_cookie("visited", "yes", max_age=60*60*24)
        return template('login.tpl')

run(host="localhost", port="8080", reloader=True, debug=True)
