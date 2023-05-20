#livinus felix bassey
#Skilaverkefni_6
#20.11.2018

import mysql.connector
from mysql.connector import Error
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='tsuts.tskoli.is',
                                       database='0301865919_afangaskraning',
                                       user='0301865919',
                                       password='mypassword')

        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
        else:
            print("not connected")

    except Error as e:
        print("villa",e)
        conn.close()
cnx=connect()#kallað í aðferðina connect()
cursor = cnx.cursor()


class Skraning:
    def nyr_medLimur(self,nafn):
        try:
            sql = "INSERT INTO notendur(nafn) VALUES ('"+nafn+"')"
            cursor.execute(sql)
            cnx.commit()
        except Error as e:
            print("villa",e)
            cnx.close()

    def prenta(self,nafntoflu):
        try:
            cursor.execute("select * from "+nafntoflu)
            result = cursor.fetchall()
            print(result)
        except Error as e:
            print("villa",e)

    def nyr_afangi(self,afangaheiti):
        try:
            sql = "INSERT INTO namskeid(afangaheiti) VALUES ('"+afangaheiti+"')"
            cursor.execute(sql)
            cnx.commit()
        except Error as e:
            print("villa",e)
            cnx.close()

    def skradurIafanga(self,nafn):
        sql="select afangaheiti from namskeid join skradir" \
            " on namskeid.namskeid_id = skradir.namskeid_id join notendur" \
            " on notendur.notandi_id = skradir.notandi_id where notendur.nafn='"+nafn+"'";
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        except Error as e:
            print("villa",e)
            cnx.close()

    def skraning(self,nafn,afangaheiti):
        try:
            sql = "select notandi_id from notendur where nafn='"+nafn+"'"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result[0][0])
            notandi_id=result[0][0]
            sql = "select namskeid_id from namskeid where afangaheiti='"+afangaheiti+"'"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result[0][0])
            namskeid_id=result[0][0]
            sql = "insert into skradir(notandi_id,namskeid_id) VALUES("+str(notandi_id)+","+str(namskeid_id)+")"
            cursor.execute(sql)
            cnx.commit()
        except IndexError as e:
            print("viðkomandi ekki skráður notandi eða áfangaheiti rangt\n",e)
            cnx.close()





try:
    vinna=Skraning()
    #vinna.nyr_medLimur("livinus felix")
    #vinna.nyr_afangi("STÆ3R05CT")
    #vinna.prenta("notendur")
    #vinna.prenta("namskeid")
    #vinna.skraning("livinus felix","KEST1TR05AU")
    #vinna.prenta("skradir")
    #vinna.skradurIafanga("livinus felix")
except Error as e:
            print("villa",e)


