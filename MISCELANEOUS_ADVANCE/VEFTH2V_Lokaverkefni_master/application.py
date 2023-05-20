from bottle import *
#from beaker.middleware import SessionMiddleware
from Database.HotelConnect import *
Common = CommonPS()
Customer = Customer()
Address = Address()

# Upsetning á hótelum
result = Common.HotelAbout()
hotels = list()
for i in result:
    item = dict()
    item['name'] = i[2]
    item['postcode'] = i[4]
    item['folder'] = i[5].lower()
    item['border'] = str(i[5].lower() + '.jpg')
    hotels.append(item)
for i in hotels:
    print(i)






cookei = ['account', 'fname', 'lname', 'SSN', 'phone', 'mail', 'checkin', 'checkout', 'herbegi']
account = {'user':'nonni2000','passwd':'nonni','fname':'Nonni','lname':'Manni','SSN':'4567892345','simi':'5678903','mail':'manni@gmail.com'}

@route('/')
def index():

    for x in cookei:
        response.set_cookie('{}'.format(x), "", expires=0)
    return template('views/index')

@route('/Hotel/<hotelid>')
def index_hotel(hotelid):
    for x in hotels:
        print(x)
        print('{}---{}'.format(x['name'],hotelid))
        if x['name']==hotelid:
            temp_hotel = x

    return template('views/index-hotel', hotel=temp_hotel)

@route('/Hotel/<hotelid>/orde')
def order(hotelid):
    checkin = request.query.checkin
    checkout = request.query.ckeckout
    herbegi = request.query.Herbergi
    response.set_cookie('checkin', checkin, secret='my_secret_code')
    response.set_cookie('checkout', checkout, secret='my_secret_code')
    response.set_cookie('herbegi', herbegi, secret='my_secret_code')
    hotelid = hotelid

    return redirect('/Hotel/{}/order'.format(hotelid))


@route('/Hotel/<hotelid>/order')
def orderroom(hotelid):
    villa = ''

    for x in hotels:
        print(x)
        print('{}---{}'.format(x['name'],hotelid))
        if x['name']==hotelid:
            temp_hotel = x
    user = request.get_cookie('account', secret='my_secret_code')
    if (user):
        fname = request.get_cookie('fname', secret='my_secret_code')
        lname = request.get_cookie('lname', secret='my_secret_code')
        ssn = request.get_cookie('SSN', secret='my_secret_code')
        phone = request.get_cookie('phone', secret='my_secret_code')
        mail = request.get_cookie('mail', secret='my_secret_code')
        user = {'name':user,'fname':fname,'lname':lname,'ssn':ssn,'phone':phone,'mail':mail}
        ifuser = True
    else:
        ifuser =False

    checkin = request.get_cookie('checkin', secret='my_secret_code')
    checkout = request.get_cookie('checkout', secret='my_secret_code')
    herbergi = request.get_cookie('herbegi', secret='my_secret_code')

    herbergi_uppl = {'checkin':checkin,'checkout':checkout,'herbergi':herbergi}
    print(herbergi_uppl)

    return template('order', villa= villa,hotel=temp_hotel,user=user, herbergi_uppl=herbergi_uppl,ifuser=ifuser)

@route('/Hotel/<stadur>/login', method='post')
def login(stadur):
    username = request.forms.get('user')
    password = request.forms.get('password')

    if username == account['user'] and password == account['passwd']:
        response.set_cookie('account', username, secret='my_secret_code')
        response.set_cookie('fname', account['fname'], secret='my_secret_code')
        response.set_cookie('lname',account['lname'], secret='my_secret_code')
        response.set_cookie('SSN', account['SSN'], secret='my_secret_code')
        response.set_cookie('phone', account['simi'], secret='my_secret_code')
        response.set_cookie('mail', account['mail'], secret='my_secret_code')

        return redirect('/Hotel/{}/order'.format(stadur))


    else:
        return "Login failed. <br> <a href='/'>Login</a>"


@route('/checkoreder', method='post')
def klaraorder():
    for x in cookei:
        response.set_cookie('{}'.format(x), "", expires=0)
    username = request.forms.get('user')
    # tékkar hvort notandi sé til ef svo þá þarf hann ekki að sækja upplýsingar um hann
    # = request.forms.get('user')
    password = request.forms.get('password')
    username = request.forms.get('user')
    password = request.forms.get('password')
    password = request.forms.get('password')




@route('/bokun')
def bokun():
    return template('bokun')

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./resources')

#session_options = {
#    'session.type': 'file',
#    'session.data_dir':'./data'
#}

#my_session = SessionMiddleware(app(), session_options)

#run(host='localhost', port='8080', debug='True', reloader='True')
run(host="0.0.0.0", port=os.environ.get('PORT'))
