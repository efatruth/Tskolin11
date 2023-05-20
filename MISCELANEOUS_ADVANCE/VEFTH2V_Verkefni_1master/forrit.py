import os
from bottle import route, run

@route('/')
def index():
    return '<a href=\'/about\'>About</a> <a href=\'/bio\'>Biography</a> <a href=\'/picture\'>Pictures</a><h2>' \
           '<a href=\'https://github.com/PeturSteinn/VEFTH2V-Verkefni_1\'>Github!</a></h2>'

@route('/about')
def about():
    return '<h3>lorem...</h3><h1><a href=\'/\'>Til baka</a></h1>'

@route('/bio')
def bio():
    return '<h3>😂😂😂lorem...😂😂😂</h3><h1><a href=\'/\'>Til baka</a></h1>'

@route('/picture')
def picture():
    return '<img src=\'https://i.pinimg.com/originals/d8/d5/fe/d8d5fe9cd4e61f864032aac6c737eae5.jpg\' width=\'300px\'>' \
           '</img><h1><a href=\'/\'>Til baka</a></h1>'

run(host="0.0.0.0", port=os.environ.get('PORT'))
