from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class storageModel:

    no=''
    storage =''
    description = ''
    lowprice = ''
    highprice = ''
    icon = ''
    tdp = ''
    capacity = ''
    port = ''
    size = ''

    def __init__(self,storage,description,lowprice,icon,tdp,capacity,port,size):
        self.storage = storage
        self.description = description
        self.lowprice = lowprice
        #self.highprice = highprice
        self.icon = icon
        self.tdp = tdp
        self.capacity = capacity
        self.port = port
        self.size = size

    def add_storage(self):
        cur = mysql.connection.cursor()
        sql = """insert into storage (storage,description,lowprice,icon,tdp,capacity,port,size) 
        values(%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cur.execute(sql,(str(self.storage),self.description,self.lowprice,self.icon,self.tdp,self.capacity,self.port,str(self.size)))
        mysql.connection.commit()
        cur.close()

    def update_storage(self):
        cur = mysql.connection.cursor()
        sql = """update storage set storage='{0}',description='{1}',
        lowpricen='{2}' highprice='{3}' icon='{4}' tdp='{5}' capacity='{6}' port='{7}' size='{8}' where no='{9}'
        """.format(self.storage,self.description,self.lowprice,self.highprice,self.icon,self.tdp,self.capacity,self.port,self.size,self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_storage(self):
        cur = mysql.connection.cursor()
        sql = "delete from storage where no='{0}'".format(self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_storage(storage):
        #storagedata = None
        cur = mysql.connection.cursor()
        sql = "select * from storage where storage='{0}'".format(storage)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        getdata = {'no':result[0],'storage':result[1],'description':result[2],'lowprice':result[3],'highprice':result[4],'icon':result[5],'tdp':result[6],'capacity':result[7],'port':result[8],'size':result[9]}
        cur.close()
        return getdata

    def get_all():
        data = []
        cur = mysql.connection.cursor()
        sql = "select * from storage"
        cur.execute(sql)
        result = cur.fetchall()
        for e in result:
            getdata = {'no':e[0],'storage':e[1],'description':e[2],'lowprice':e[3],'highprice':e[4],'icon':e[5],'tdp':e[6],'capacity':e[7],'port':e[8],'size':e[9]}
            data.append(getdata)
        mysql.connection.commit()
        cur.close()
        return data