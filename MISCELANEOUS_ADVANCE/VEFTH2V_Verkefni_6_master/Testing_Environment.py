import json, requests

response = requests.get("http://apis.is/petrol")

data = response.json()
all_stations = list()
odyrt_bensin = dict()
odyrt_disel = dict()
for i in data['results']:
    i['bensin95'] = str(i['bensin95'])
    i['diesel'] = str(i['diesel'])
    i['bensin95_discount'] = str(i['bensin95_discount'])
    i['diesel_discount'] = str(i['diesel_discount'])
    if i['bensin95_discount'] == "None":
        i['bensin95_discount'] = "Ekkert"
    if i['diesel_discount'] == "None":
        i['diesel_discount'] = "Ekkert"




#for i in data['results']:
#    print(i['geo']['lon'])
#    print(i['geo']['lat'])


for i in data['results']:
    print(i)

#print(data['results']['geo'])


'''

for i in data['results']:
    i['bensin95'] = str(i['bensin95'])
    i['diesel'] = str(i['diesel'])
    i['bensin95_discount'] = str(i['bensin95_discount'])
    i['diesel_discount'] = str(i['diesel_discount'])
    if i['bensin95_discount'] == None:
        i['bensin95_discount'] = "Ekkert"
    else:
        i['bensin95_discount'] += " kr,-"
    if i['diesel_discount'] == None:
        i['diesel_discount'] = "Ekkert"
    else:
        i['diesel_discount'] += " kr,-"
    i['bensin95'] += " kr,-"
    i['diesel'] += " kr,-"

for i in data['results']:
    print(i)
'''
