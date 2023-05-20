#Kypler L. Espiritu
#Lokaverkefni - Forritun
#22.11.17


from bottle import *
from sys import *
import pymysql

db = pymysql.connect(host="tsuts.tskoli.is",
                     user="2910003120",
                     passwd="kypler00",
                     db="2910003120_lokaverkvef12")


cur = db.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS USER(username varchar(32) PRIMARY KEY, password varchar(32))')
cur.execute('CREATE TABLE IF NOT EXISTS ORDERS(Username varchar(32), texti varchar(500))')


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/')
def sign_in():
    try:
        cur.execute('SELECT * FROM USER')
        users = cur.fetchall()
    except pymysql.InterfaceError:
        pass

    notenda_listi = []
    for i, x in users:
        notenda_listi.append([i, x])

    if len(notenda_listi) == 0:
        cur.execute('INSERT INTO USER VALUES("kypler", "admin")')
        db.commit()
    else:
        pass
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
        return template('sign_in_error', message="Innskráning hefur ekki staðist")


@route('/signup')
def sign_up():
    return template('sign_up')

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
            cur.execute('INSERT INTO USER VALUES(%s, %s)', (signupUser, signUpPass))
            db.commit()
            return template('sign_up_message', message="Nýskráning hefur staðist")
        else:
            return template('sign_up_message', message="Nýskráning hefur ekki staðist")

@route('/heimasida')
def heimasida():

    return template('heimasida')

@route('/panta')
def panta():
    return template('to_do')

@route('/panta', method="POST")
def panta_info():
    texti = request.forms.get('comment')

    cur.execute('INSERT INTO ORDERS VALUES(%s, %s)', (signinUser, texti))
    db.commit()
    redirect('/heimasida')

@route('/minar')
def minar_sidur():
    cur.execute('SELECT * FROM ORDERS WHERE USERNAME = %s', (signinUser))
    orders = cur.fetchall()

    listi = []
    for i, x in orders:
        listi.append([i, x.encode('latin-1').decode('utf-8')])

    return template('minar_sidur', data=listi, nafn=signinUser)



run(host="0.0.0.0", port=os.environ.get('PORT', 5000), reloader=True, debug=True)