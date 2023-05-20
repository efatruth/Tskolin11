#Along A. Loftsson
from bottle import *
import pymysql

connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='1101003610',
                             password='Alongal9',
                             db='1101003610_vef2verk11')

conn_cur = connection.cursor()

all_data = conn_cur.execute('SELECT * FROM BILAR')
everything = conn_cur.fetchall()

dblist = []
for i in everything:
    dblist.append(i)

row_1 = dblist[0]
row_2 = dblist[1]
row_3 = dblist[2]


@route('/')
def site():
    return template('normaluser.tpl', data_1=row_1, data_2=row_2, data_3=row_3)

run(host='localhost', port=8080, reloader=True, debug=True)














