from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class ramModel:

    no=''
    ram =''
    description = ''
    lowprice = ''
    highprice = ''
    icon = ''
    capacity = ''
    frequency = ''
    ramtype = ''

    def __init__(self,ram,description,lowprice,icon,capacity,frequency,ramtype):
        self.ram = ram
        self.description = description
        self.lowprice = lowprice
        #self.highprice = highprice
        self.icon = icon
        self.capacity = capacity
        self.frequency = frequency
        self.ramtype = ramtype

    def add_ram(self):
        cur = mysql.connection.cursor()
        sql = """insert into ram (ram,description,lowprice,icon,capacity,frequency,ramtype)
        values(%s,%s,%s,%s,%s,%s,%s)
        """
        cur.execute(sql,(str(self.ram),str(self.description),str(self.lowprice),self.icon,str(self.capacity),str(self.frequency),str(self.ramtype)))
        mysql.connection.commit()
        cur.close()

    def update_ram(self):
        cur = mysql.connection.cursor()
        sql = """update ram set ram='{0}',description='{1}',
        lowpricen='{2}' highprice='{3}' icon='{4}' capacity='{5}' frequency='{6}' where no='{7}'
        """.format(self.ram,self.description,self.lowprice,self.highprice,self.icon,self.capacity,self.frequency,self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_ram(self):
        cur = mysql.connection.cursor()
        sql = "delete from ram where no='{0}'".format(self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_ram(ram):
        #ramdata = None
        cur = mysql.connection.cursor()
        sql = "select * from ram where ram='{0}'".format(ram)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        getdata = {'no':result[0],'ram':result[1],'description':result[2],'lowprice':result[3],'highprice':result[4],'icon':result[5],'capacity':result[6],'frequency':result[7],'ramtype':result[8]}
        cur.close()
        return getdata

    def get_all():
        data = []
        cur = mysql.connection.cursor()
        sql = "select * from ram"
        cur.execute(sql)
        result = cur.fetchall()
        for e in result:
            getdata = {'no':e[0],'ram':e[1],'description':e[2],'lowprice':e[3],'highprice':e[4],'icon':e[5],'capacity':e[6],'frequency':e[7],'ramtype':e[8]}
            data.append(getdata)
        mysql.connection.commit()
        cur.close()
        return data