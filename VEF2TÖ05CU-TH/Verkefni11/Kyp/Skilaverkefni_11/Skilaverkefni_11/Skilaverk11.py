#Kypler L. Espiritu
#Skilaverkefni 11 - Veftækni
#08.11.17

from bottle import *
import pymysql

db = pymysql.connect(host="tsuts.tskoli.is",
                     user="2910003120",
                     passwd="kypler00",
                     db="2910003120_vef2Verk11")

cur = db.cursor()

allt_data = cur.execute('SELECT * FROM BILAR')
allt = cur.fetchall()

listi = []
for i in allt:
    listi.append(i)

row_1 = listi[0]
row_2 = listi[1]
row_3 = listi[2]


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/')
def index():
    return template('bilar.tpl', data_1=row_1, data_2=row_2, data_3=row_3)

run(host='localhost', port=8080, reloader=True, debug=True)

