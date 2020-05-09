from flask import Flask
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class casesModel:

    no=''
    cases =''
    description = ''
    lowprice = ''
    highprice = ''
    icon = ''
    size = ''
    mbsize = ''

    def __init__(self,cases,description,lowprice,icon,size,mbsize):

        self.cases = cases
        self.description = description
        self.lowprice = lowprice
        #self.highprice = highprice
        self.icon = icon
        self.size = size
        self.mbsize = mbsize

    def add_cases(self):
        cur = mysql.connection.cursor()
        sql = """insert into cases (cases,description,lowprice,icon,storagesize,mbsize)
        values(%s,%s,%s,%s,%s,%s)
        """
        cur.execute(sql,(str(self.cases),str(self.description),str(self.lowprice),self.icon,str(self.size),str(self.mbsize)))
        mysql.connection.commit()
        cur.close()

    def update_cases(self):
        cur = mysql.connection.cursor()
        sql = """update cases set cases='{0}',description='{1}',
        lowpricen='{2}' highprice='{3}' icon='{4}' storagesize = '{5}'where no='{6}'
        """.format(self.cases,self.description,self.lowprice,self.highprice,self.icon,self.size,self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_cases(self):
        cur = mysql.connection.cursor()
        sql = "delete from cases where no='{0}'".format(self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_cases(cases):
        #casesdata = None
        cur = mysql.connection.cursor()
        sql = "select * from cases where cases='{0}'".format(cases)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        getdata = {'no':result[0],'cases':result[1],'description':result[2],'lowprice':result[3],'highprice':result[4],'icon':result[5],'storagesize':result[6],'mbsize':result[7]}
        cur.close()
        return getdata

    def get_all():
        data = []
        cur = mysql.connection.cursor()
        sql = "select * from cases"
        cur.execute(sql)
        result = cur.fetchall()
        for e in result:
            getdata = {'no':e[0],'cases':e[1],'description':e[2],'lowprice':e[3],'highprice':e[4],'icon':e[5],'storagesize':e[6],'mbsize':e[7]}
            data.append(getdata)
        mysql.connection.commit()
        cur.close()
        return data