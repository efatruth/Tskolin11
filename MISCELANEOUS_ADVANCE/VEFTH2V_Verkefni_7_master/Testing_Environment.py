'''
import requests
import os
from bottle import route, post, run, static_file, error, request, template, response, redirect, app
from beaker.middleware import SessionMiddleware

@route('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        response.set_cookie("account", username, secret='some-secret-key')
        return template("<p>Welcome {{name}}! You are now logged in.</p>", name=username)
    else:
        return "<p>Login failed.</p>"

def check_login(usr, passwd):
    if usr == "admin" and passwd == "admin": return True
    else: return True

@route('/restricted')
def restricted_area():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        return template("Hello {{name}}. Welcome back.", name=username)
    else:
        return "You are not logged in. Access denied."
run(debug=True, reloader=True)
'''



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

for item in products:
    tmp = "{:,},-".format(item['cost'])
    print(tmp)
