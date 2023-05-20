#Kypler Lloyd Espiritu
#Skilaverkefni 7 - Veftækni
#13.10.17

from bottle import route, run, template, request
from beaker.middleware import SessionMiddleware
from sys import argv
import beaker
import bottle


session_opts = {
    'session.type': 'file',
    # 'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)

checked = []

def checkbox(product, list):
    list.append(product)
    for i in list:
        if i is None:
            list.remove(i)

@route('/')
def index():
    s = request.environ.get('beaker.session')
    s['test'] = s.get('test', 0) + 1
    s.save()

    return template('shop_1st', telja=checked, oft=s['test'])


@route('/', method='POST')
def cart():
    product_list = []
    products1 = request.forms.get('vara1')
    products2 = request.forms.get('vara2')
    products3 = request.forms.get('vara3')
    products4 = request.forms.get('vara4')

    checkbox(products1, product_list)
    checkbox(products2, product_list)
    checkbox(products3, product_list)
    checkbox(products4, product_list)
    del checked[:]
    for i in 'vara1', 'vara2', 'vara3', 'vara4':
        if request.POST.get(i, False):
            checked.append(i)
        elif request.POST.get(i, True):
            try:
                checked.remove(i)
            except:
                pass

    return template('shopping_cart', pro1=product_list)


run(app=app, host='0.0.0.0', port=argv[1], reloader=True, debug=True)