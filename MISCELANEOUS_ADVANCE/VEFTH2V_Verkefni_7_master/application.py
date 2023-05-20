import os
from bottle import route, post, run, static_file, error, request, template, response, redirect, app
from beaker.middleware import SessionMiddleware

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./resources')

cart_item_id = 0
session_options = {
    'session.type': 'file',
    'session.data_dir': './data'
}

products = [
    {
        "name": "Vara A",
        "pid": "000554",
        "cost": 2995
    },
    {
        "name": "Vara B",
        "pid": "000555",
        "cost": 3495
    },
    {
        "name": "Vara C",
        "pid": "000556",
        "cost": 5995
    },
    {
        "name": "Vara D",
        "pid": "666666",
        "cost": 2455995
    },
    {
        "name": "Vara E",
        "pid": "043340",
        "cost": 55995
    },
    {
        "name": "Vara F",
        "pid": "033101",
        "cost": 9995
    },
    {
        "name": "Vara G",
        "pid": "400104",
        "cost": 80320995
    },
    {
        "name": "Vara H",
        "pid": "550443",
        "cost": 500450100995
    },
    {
        "name": "Vara I",
        "pid": "330203",
        "cost": 20995
    },
    {
        "name": "Vara J",
        "pid": "002259",
        "cost": 1995
    }
]

my_session = SessionMiddleware(app(), session_options)

@route('/')
def index():
    return template('views/index')


@route('/starfsfolk')
def starfsfolk():
    return template('staff.tpl')


@route('/login', method="POST")
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        response.set_cookie("account", username, secret='some-secret-key')
        return template("<p>Welcome {{name}}! You are now logged in.<br> <a href='/'>Home</a></p>", name=username)
    else:
        return "<p>Login failed.<br> <a href='/'>Home</a></p>"

def check_login(usr, passwd):
    if usr == "admin" and passwd == "admin": return True
    else: return False

@route('/signin')
def signin():
    return template('sign_in')

@route('/signout')
def signout():
    response.set_cookie('account',"", expires=0)
    return "You have been signed out" "<br> <a href='/'>Home</a>"

@route('/restricted')
def restricted_area():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        return template("Hello {{name}}. Welcome back.", name=username)
    else:
        return "You are not logged in. Access denied."

@route('/shop')
def shop():
    return template('shop', products=products)

@route('/cart')
def cart():
    session = request.environ.get('beaker.session')
    cart =  list()
    for i in products:
        for x in session:
            if i['pid'] == session[x]:
                cart.append(i)
    return template('cart', cart=cart)

@route('/cart/add/<item>')
def add_to_cart(item):
    global cart_item_id
    session = request.environ.get('beaker.session')
    for i in products:
        if str(i['pid']) == str(item):
            cart_item_id += 1

            session["ID_" + str(cart_item_id)] = i['pid']

    session.save()
    return redirect('/cart')


@route('/cart/remove')
def remove_cart():
    session = request.environ.get('beaker.session')
    session.delete()
    return redirect('/shop')

@route('/cart/remove/<item>')
def remove_item_from_cart(item):
    session = request.environ.get('beaker.session')
    for i in session:
        if session[i] == str(item):
            session.pop(i)
            break

    session.save()
    return redirect('/cart')


@error(404)
def error404(error):
    return template('views/error404')



run(host="0.0.0.0", port=os.environ.get('PORT'), app=my_session)
#run(debug=True, reloader=True, app=my_session)
