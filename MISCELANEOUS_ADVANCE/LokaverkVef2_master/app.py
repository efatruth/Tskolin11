#Kypler L. Espiritu
#Lokaverkefni - Forritun
#22.11.17


from bottle import *
from sys import argv
import pymysql

db = pymysql.connect(host="tsuts.tskoli.is",
                     user="2910003120",
                     passwd="kypler00",
                     db="2910003120_vef2lokaverk")


cur = db.cursor()


cur.execute('CREATE TABLE IF NOT EXISTS USER(username varchar(32) PRIMARY KEY, password varchar(32))')
cur.execute('CREATE TABLE IF NOT EXISTS ORDERS(Username varchar(32), Botn varchar(32), Staerd varchar(32), FjoldiAlegg varchar(32), Verd varchar(32))')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/')
def sign_in():

    try:
        cur.execute('SELECT * FROM USER')
        users = cur.fetchall()
    except (pymysql.InterfaceError):
        pass

    notenda_listi = []
    for i, x in users:
        notenda_listi.append([i, x])

    if len(notenda_listi) == 0:
        cur.execute('INSERT INTO USER VALUES("kypler", "admin")')
    return template('sign_in.tpl')

@route('/', method='POST')
def sign_in_info():

    cur.execute('SELECT * FROM USER')
    users = cur.fetchall()

    notenda_listi = []
    for i, x in users:
        notenda_listi.append([i, x])

    global signinUser
    signinUser = request.forms.get('SignIn_username')
    signinPass = request.forms.get('SignIn_password')

    signIn = list((signinUser, signinPass))

    for notandanafn, lykilord in notenda_listi:
        if signIn[0] == notandanafn and signIn[1] == lykilord:
            redirect('/heimasida')
            break
    else:
        return template('sign_in_error.tpl', message="Innskráning hefur ekki staðist")


@route('/signup')
def sign_up():
    return template('sign_up.tpl')

@route('/signup', method="POST")
def sign_up_info():
    cur.execute('SELECT * FROM USER')
    users = cur.fetchall()

    notenda_listi = []
    for i, x in users:
        notenda_listi.append([i, x])

    signupUser = request.forms.get('SignUp_username')
    signUpPass = request.forms.get('SignUp_password')

    signUp = list((signupUser, signUpPass))

    for notendanafn, lykilord in notenda_listi:
        if signUp[0] != notendanafn:
            try:
                cur.execute('INSERT INTO USER VALUES(%s, %s)', (signupUser, signUpPass))
                db.commit()
                return template('sign_up_message', message="Nýskráning hefur staðist")
            except (pymysql.IntegrityError):
                return template('sign_up_message', message="Nýskráning hefur ekki staðist")
        else:
            return template('sign_up_message', message="Nýskráning hefur ekki staðist")

@route('/heimasida')
def heimasida():
    return template('heimasida.tpl')

@route('/panta')
def panta():
    return template('pizza_panta.tpl')

@route('/panta', method="POST")
def panta_info():
    tomma = 0
    botn = request.forms.get('bottom')
    staerd = request.forms.get('size')
    topping = request.forms.getall('topping')

    if int(staerd) == 1000:
        tomma = "9"
    elif int(staerd) == 1500:
        tomma = "12"
    elif int(staerd) == 2000:
        tomma = "18"

    topping = list(map(int, topping))
    verd_allt = str(sum(topping) + int(staerd))
    cur.execute('INSERT INTO ORDERS VALUES(%s, %s, %s, %s, %s)', (signinUser, botn, str(tomma), str(len(topping)), verd_allt))
    db.commit()
    redirect('/heimasida')

@route('/minar')
def minar_sidur():
    cur.execute('SELECT * FROM ORDERS WHERE USERNAME = %s', (signinUser))
    orders = cur.fetchall()

    listi = []
    for i in orders:
        listi.append(list(i))

    return template('minar_sidur.tpl', data=listi)



run(host='0.0.0.0', port=argv[1], reloader=True, debug=True)
