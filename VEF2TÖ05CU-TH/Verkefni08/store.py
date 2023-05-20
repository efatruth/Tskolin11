#Along A. Loftsson
from bottle import *
from beaker.middleware import SessionMiddleware
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
    s['visits'] = s.get('visits', 0) + 1
    s.save()
    return template('storefront.tpl', count=checked, visit=s['visits'])



@route('/', method='POST')
def cart():
    product_list = []
    products1 = request.forms.get('Roll')
    products2 = request.forms.get('Wash')
    products3 = request.forms.get('Towel')
    products4 = request.forms.get('Shampoo')

    checkbox(products1, product_list)
    checkbox(products2, product_list)
    checkbox(products3, product_list)
    checkbox(products4, product_list)
    del checked[:]
    for i in 'Roll', 'Wash', 'Towel', 'Shampoo':
        if request.POST.get(i, False):
            checked.append(i)
        elif request.POST.get(i, True):
            try:
                checked.remove(i)
            except:
                pass

    return template('cart.tpl', pro1=product_list)


run(app=app, host='localhost', port=8080, reloader=True, debug=True)
