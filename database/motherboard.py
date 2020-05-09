from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class motherboardModel:

    no=''
    motherboard =''
    description = ''
    lowprice = ''
    highprice = ''
    icon = ''
    socket = ''
    ramtype = ''
    m2 = ''
    mbsize = ''

    def __init__(self,motherboard,description,lowprice,icon,socket,ramtype,m2,mbsize):
        self.motherboard = motherboard
        self.description = description
        self.lowprice = lowprice
        #self.highprice = highprice
        self.icon = icon
        self.socket = socket
        self.ramtype = ramtype
        self.m2 = m2
        self.mbsize = mbsize


    def add_motherboard(self):
        cur = mysql.connection.cursor()
        sql = """insert into motherboard (motherboard,description,lowprice,icon,socket,ramtype,m2,mbsize) 
        values(%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cur.execute(sql,(str(self.motherboard),str(self.description),str(self.lowprice),self.icon,str(self.socket),str(self.ramtype),str(self.m2),str(self.mbsize)))
        mysql.connection.commit()
        cur.close()

    def update_motherboard(self):
        cur = mysql.connection.cursor()
        sql = """update motherboard set motherboard='{0}',description='{1}',
        lowpricen='{2}' highprice='{3}' icon='{4}' socket='{5}' where no='{6}'
        """.format(self.motherboard,self.description,self.lowprice,self.highprice,self.icon,self.socket,self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_motherboard(self):
        cur = mysql.connection.cursor()
        sql = "delete from motherboard where no='{0}'".format(self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_motherboard(mb):
        #motherboarddata = None
        cur = mysql.connection.cursor()
        sql = "select * from motherboard where motherboard='{0}'".format(mb)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        getdata = {'no':result[0],'motherboard':result[1],'description':result[2],'lowprice':result[3],'highprice':result[4],'icon':result[5],'socket':result[6],'m2':result[7],'mbsize':result[8]}
        cur.close()
        return getdata

    def get_all():
        data = []
        cur = mysql.connection.cursor()
        sql = "select * from motherboard"
        cur.execute(sql)
        result = cur.fetchall()
        for e in result:
            getdata = {'no':e[0],'motherboard':e[1],'description':e[2],'lowprice':e[3],'highprice':e[4],'icon':e[5],'socket':e[6],'ramtype':e[7],'m2':e[8],'mbsize':e[9]}
            data.append(getdata)
        mysql.connection.commit()
        cur.close()
        return data