from flask import Flask
from flask_mysqldb import MySQL
import MySQLdb
from io import BytesIO
import gzip

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class cpuModel:

    no=''
    cpu =''
    description = ''
    lowprice = ''
    highprice = ''
    icon = ''
    tdp = ''
    socket = ''
    ramtype = ''

    def __init__(self,cpu,description,lowprice,icon,tdp,socket,ramtype):

        self.cpu = cpu
        self.description = description
        self.lowprice = lowprice
        #self.highprice = highprice
        self.icon = icon
        self.tdp = tdp
        self.socket = socket
        self.ramtype = ramtype

    def add_cpu(self):
        cur = mysql.connection.cursor()
        sql = """insert into cpu (cpu,description,lowprice,icon,tdp,socket,ramtype) 
        values(%s,%s,%s,%s,%s,%s,%s)
        """
        cur.execute(sql,(self.cpu,self.description,self.lowprice,self.icon,self.tdp,self.socket,self.ramtype))
        mysql.connection.commit()
        cur.close()

    def update_cpu(self):
        cur = mysql.connection.cursor()
        sql = """update cpu set cpu='{0}',description='{1}',
        lowpricen='{2}' highprice='{3}' icon='{4}' tdp='{5}' socket='{6}' ramtype='{7}' where no='{7}'
        """.format(self.cpu,self.description,self.lowprice,self.highprice,self.icon,self.tdp,self.socket,self.ramtype,self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_cpu(self):
        cur = mysql.connection.cursor()
        sql = "delete from cpu where no='{0}'".format(self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_cpu(cpu):
        #cpudata = []
        cur = mysql.connection.cursor()
        sql = "select * from cpu where cpu='{0}'".format(cpu)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        #cpudata = cpuModel(result[1],result[2],result[3],result[5],result[6],result[7],result[8])
        #cpudata.no = result[0]
        #print(result[0])
        getdata = {'no':result[0],'cpu':result[1],'description':result[2],'lowprice':result[3],'highprice':result[4],'icon':result[5],'tdp':result[6],'socket':result[7],'ramtype':result[8]}
        #print(getdata)
        #cpudata.append(getdata)
        cur.close()
        return getdata

    def get_all():
        data = []
        cur = mysql.connection.cursor()
        sql = "select * from cpu"
        cur.execute(sql)
        result = cur.fetchall()
        for e in result:
            #row = cpuModel(e[1],e[2],e[3],e[5],e[6],e[7],e[8])
            #row.no = e[0]
            #row.highprice = e[4]
            getdata = {'no':e[0],'cpu':e[1],'description':e[2],'lowprice':e[3],'highprice':e[4],'icon':e[5],'tdp':e[6],'socket':e[7],'ramtype':e[8]}
            data.append(getdata)
            #print(BytesIO(e[5]))
            #print(e[5][0])
            #fout = open('image.png','wb')
            #fout.write(e[5])
        mysql.connection.commit()
        cur.close()
        return data