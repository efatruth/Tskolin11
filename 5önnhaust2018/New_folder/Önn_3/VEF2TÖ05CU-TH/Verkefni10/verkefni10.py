#Along A. Loftsson

from bottle import route, run, template, request, redirect
import pymysql

db = pymysql.connect(host="tsuts.tskoli.is",
                     user="1101003610",
                     passwd="CHANGE THIS PASSSORD THANK YOU LOOK OVER HERE OVER HERE LOOK REMEMBER CHANGE HELLO",
                     db="1101003610_vefVerk10")

@route("/"):
