import pymysql
from bottle import *


@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./resources')

@route('/')
def index():
    errormsg = ''
    return template('views/index', errormsg=errormsg)

@route('/db/list')
def list_cars():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0408982209', passwd='mypassword', db='0408982209_AukaverkefniDB')
    c = conn.cursor()
    c.execute('SELECT * FROM bilar;')
    records = c.fetchall()
    print(records)
    conn.close()
    c.close()

    return template('views/list_cars', bilar=records)

@route('/car_info')
def car_info():
    num = request.query.get('search')
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0408982209', passwd='mypassword', db='0408982209_AukaverkefniDB')
    c = conn.cursor()
    c.execute('SELECT * FROM bilar WHERE skraningarnumer = "{}"'.format(num))
    result = c.fetchone()
    conn.close()
    c.close()
    print(result)
    errormsg = '{} er ekki skráð!'.format(num)
    if result:
        return template('views/car_info', result=result, num=num)
    else:
        return template('views/index', errormsg=errormsg)

@route('/db/add')
def add_to_db():
    errormsg = ''
    return template('new_car', errormsg=errormsg)

@route('/db/add', method='POST')
def submit_record():
    skr_nr = request.forms.skr_nr.upper() # Til að ekki sé hægt að stimpla inn lower case og fá 500 villu útaf duplicate primary key
    tegund = request.forms.tegund
    vrk_nr = request.forms.vrk_nr
    skr_dags = request.forms.skr_dags
    co2 = request.forms.co2
    thyngd = request.forms.thyngd
    sko_dags = request.forms.sko_dags
    stada = request.forms.stada

    co2 = int(co2)
    thyngd = int(thyngd)

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0408982209', passwd='mypassword', db='0408982209_AukaverkefniDB')
    c = conn.cursor()

    c.execute('SELECT * FROM bilar;')
    records = c.fetchall()
    if any(skr_nr in r for r in records):
        conn.close()
        c.close()
        errormsg = '{} nú þegar skráð!'.format(skr_nr)
        return template('new_car', errormsg=errormsg)

    else:
        c.execute("INSERT INTO bilar VALUES ('{}', '{}', '{}', '{}', '{:d}', '{:d}', '{}', '{}')"
                  .format(skr_nr, tegund, vrk_nr, skr_dags, co2, thyngd, sko_dags, stada))
        conn.commit()
        conn.close()
        c.close()
        return redirect('/')

@route('/db/delete/<nr>')
def del_from_db(nr):
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0408982209', passwd='mypassword', db='0408982209_AukaverkefniDB')
    c = conn.cursor()
    c.execute("DELETE FROM bilar WHERE skraningarnumer = %s", (nr))
    conn.commit()
    conn.close()
    c.close()

    return redirect('/')

@route('/db/update/<nr>')
def update_db(nr):
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0408982209', passwd='mypassword', db='0408982209_AukaverkefniDB')
    c = conn.cursor()

    c.execute('SELECT * FROM bilar WHERE skraningarnumer = %s', (nr))
    bill = c.fetchone()
    conn.close()
    c.close()

    return template('views/update_car', bill=bill)

@route('/db/update', method='POST')
def submit_update():
    skr_nr = request.forms.skr_nr
    tegund = request.forms.tegund
    vrk_nr = request.forms.vrk_nr
    skr_dags = request.forms.skr_dags
    co2 = request.forms.co2
    thyngd = request.forms.thyngd
    sko_dags = request.forms.sko_dags
    stada = request.forms.stada

    co2 = int(co2)
    thyngd = int(thyngd)

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0408982209', passwd='mypassword', db='0408982209_AukaverkefniDB')
    c = conn.cursor()

    c.execute("UPDATE bilar SET skraningarnumer = '{}', tegund='{}', verksmidjunumer = '{}',"
              " skraningardagur = '{}', co2 = '{}', þyngd = '{}', skodun = '{}', stada = '{}'"
              " WHERE skraningarnumer = '{}'".format(skr_nr, tegund, vrk_nr, skr_dags, co2, thyngd, sko_dags,
                                                     stada, skr_nr))
    conn.commit()
    conn.close()
    c.close()

    return redirect('/db/list')





#run(debug=True, reloader=True)
run(host="0.0.0.0", port=os.environ.get('PORT'))

