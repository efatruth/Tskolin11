import os, json
from bottle import route, post, run, static_file, error, request, template

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./resources')

@route('/')
def index():
    return template('views/index')

@route('/order')
def order():

    alegg = list()
    alegg_legit = list()
    fullname = request.query.name
    heimili = request.query.heimili
    netfang = request.query.netfang
    simi = request.query.simi
    verd = int()
    vsk = 0.25

    pizzasize = request.query.pizzasize

    print(pizzasize)
    if pizzasize == "9":
        print("Hún er 9tommu")
        verd += 1000
    elif pizzasize == "12":
        print("Hún er 12tommu")
        verd += 1500

    elif pizzasize == "18":
        print("Hún er 18tommu")
        verd += 2000



    alegg.append(request.query.pepperoni)
    alegg.append(request.query.beikonkurl)
    alegg.append(request.query.piparostur)
    alegg.append(request.query.rjomaostur)
    alegg.append(request.query.svarolifur)
    alegg.append(request.query.nachos)

    for i in alegg:
        if len(i) > 2:
            alegg_legit.append(i)
            verd += 200
    return template('views/order', fullname=fullname, heimili=heimili, netfang=netfang, simi=simi, pizzasize=pizzasize, alegg=alegg_legit, verd=verd, vsk=vsk)

@route('/sign_up')
def sign_up():
    return template('sign_up')

@route('/sign_up/check', method='POST')
def sign_up_check():
    nafn = request.forms.nafn
    netfang = request.forms.netfang
    password = request.forms.password

    with open('resources/pls_dont_look_here/users.json', 'r') as file:
        reader = json.load(file)
        users = reader
        newuser = {"username": nafn, "netfang": netfang, "pass": password}
        userExists = False
        print(users)
        for user in users["users"]:
            if user["netfang"] == netfang:
                userExists = True
            print(user)
        if not userExists:
            users["users"].append(newuser)
    if not userExists:
        with open('resources/pls_dont_look_here/users.json', 'w') as file:
            json.dump(users, file)

    return template('check', nafn=nafn, netfang=netfang, userExists=userExists)

run(host="0.0.0.0", port=os.environ.get('PORT'))
#run(debug=True, reloader=True)
