#Along A. Loftsson
import urllib.request, json

with open('myndir.json') as File:
    jsonfile = json.load(File)

jsonfile['imagelist'].append({'imageSource':'https://www.healthline.com/hlcmsresource/images/AN_images/AN74-Banana_smoothie-1296x728-Header.jpg','name':'Banana - 2'})

with open("myndir.json","w") as skra:
    json.dump(jsonfile,skra)

print("The picture and name have been appended.")