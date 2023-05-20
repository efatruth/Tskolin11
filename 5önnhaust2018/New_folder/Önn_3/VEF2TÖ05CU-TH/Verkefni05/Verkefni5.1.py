#Along A. Loftsson 20.09.2017
from bottle import run, route, template, static_file, request
@route('/')
def index():
    return template('pizza.tpl')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./')


@route('/', method='post')
def site():
    name = request.forms.get('name')
    address = request.forms.get('address')
    phone = request.forms.get('phone')
    price = request.forms.getall('price')
    price = sum(list(map(int, price)))
    skattur = price*1.25
    skattur = str(skattur)
    price = str(price)
    return template('midi.tpl', name=name, address=address, phone=phone, price=price, skattur=skattur)


run(host='localhost', port=8080, reloader=True, debug=True)


