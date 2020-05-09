from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class listhardwareModel:

    listno=''
    hardware =''
    htype = ''

    def __init__(self,hardware,htype):

        self.hardware = hardware
        self.htype = htype

    def add_listhardware(self):
        cur = mysql.connection.cursor()
        sql = """insert into listhardware (hardware,htype,creator) 
        values('{0}','{1}','{2}')
        """.format(self.listno,self.hardware,self.htype)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def update_listhardware(self):
        cur = mysql.connection.cursor()
        sql = """update listhardware set hardware='{0}',
        htype='{1}' where listno='{3}'
        """.format(self.hardware,self.htype,self.listno)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_listhardware(self):
        cur = mysql.connection.cursor()
        sql = "delete from listhardware where listno='{0}' and hardware='{1}'".format(self.listno,self.hardware)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_listhardware(self):
        listnodata = None
        cur = mysql.connection.cursor()
        sql = "select * from listhardware where listno='{0}'".format(self.listno)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        listnodata = listhardwareModel(result[1],result[2])
        listnodata.no = result[0]
        cur.close()
        return listnodata

    def get_all():
        data = []
        cur = mysql.connection.cursor()
        sql = "select * from listhardware"
        cur.execute(sql)
        result = cur.fetchall()
        for e in result:
            row = listhardwareModel(e[1],e[2])
            row.no = e[0]
            data.append(row)
        mysql.connection.commit()
        cur.close()
        return data