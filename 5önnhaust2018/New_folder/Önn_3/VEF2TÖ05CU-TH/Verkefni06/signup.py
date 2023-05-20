#Along A. Loftsson
from bottle import run, route, template, static_file, request
import csv, re

@route('/')
def index():
    return template('signup.tpl')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root="./static/")

@route('/send', method="post")
def signedup():
    open_file = open("user.txt", "a+", encoding="utf-8")
    name = request.forms.get('name')
    user = request.forms.get('username')
    email = request.forms.get('email')
    password = request.forms.get('pass')
    phone = request.forms.get('phone')

    re_name = re.sub('\d+', ' ', name).strip()
    re_user = user.replace(' ', '')
    re_pass = password.replace(' ', '')
    re_email = email.replace(' ', '')

    read_file = open('user.txt', 'r')
    reading = read_file.read()
    file_list = reading.split('\n')
    read_file.close()

    userlist = []
    for i in file_list:
        users = i.split(';')
        userlist.append(users)

    userlist.pop()

    info = {}
    info.update({"name":name, "user":user, "email":email, "password":password, "phone":phone})

    for i in userlist:
        if re_user in i:
            return template('error', info, message='ERROR - Notandanafnið ' + re_user + ' er þegar til.')
        elif re_email in i:
            return template('error', info, message='ERROR - Netfang ' + re_email + ' er þegar til.')
        elif len(password) < 6:
            return template('error', info, message='Lykilorð er of stutt.')
        else:
            break
    data = csv.writer(open_file, delimiter=";", lineterminator="\n")
    data.writerow((re_name, re_user, re_email, re_pass, phone))
    open_file.close()
    return template('success', message="Nýskráning tókst, Nýja notandanafnið er " + re_user)

run(host="localhost", port="8080", reloader=True, debug=True)
