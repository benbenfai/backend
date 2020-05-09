from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class powersupplyModel:

    no=''
    powersupply =''
    description = ''
    lowprice = ''
    highprice = ''
    icon = ''
    power_capacity = ''
    bronze = ''

    def __init__(self,powersupply,description,lowprice,icon,power_capacity,bronze):
        self.powersupply = powersupply
        self.description = description
        self.lowprice = lowprice
        #self.highprice = highprice
        self.icon = icon
        self.power_capacity = power_capacity
        self.bronze = bronze

    def add_powersupply(self):
        cur = mysql.connection.cursor()
        sql = """insert into powersupply (powersupply,description,lowprice,icon,power_capacity,bronze) 
        values(%s,%s,%s,%s,%s,%s)
        """
        cur.execute(sql,(str(self.powersupply),str(self.description),str(self.lowprice),self.icon,str(self.power_capacity),str(self.bronze)))
        mysql.connection.commit()
        cur.close()

    def update_powersupply(self):
        cur = mysql.connection.cursor()
        sql = """update powersupply set powersupply='{0}',description='{1}',
        lowpricen='{2}' highprice='{3}' icon='{4}' power_capacity='{5}' bronze='{6}' where no='{7}'
        """.format(self.powersupply,self.description,self.lowprice,self.highprice,self.icon,self.power_capacity,self.bronze,self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_powersupply(self):
        cur = mysql.connection.cursor()
        sql = "delete from powersupply where no='{0}'".format(self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_powersupply(powersupply):
        powersupplydata = None
        cur = mysql.connection.cursor()
        sql = "select * from powersupply where powersupply='{0}'".format(powersupply)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        getdata = {'no':result[0],'powersupply':result[1],'description':result[2],'lowprice':result[3],'highprice':result[4],'icon':result[5],'power_capacity':result[6],'bronze':result[7]}
        cur.close()
        return getdata

    def get_all():
        data = []
        cur = mysql.connection.cursor()
        sql = "select * from powersupply"
        cur.execute(sql)
        result = cur.fetchall()
        for e in result:
            getdata = {'no':e[0],'powersupply':e[1],'description':e[2],'lowprice':e[3],'highprice':e[4],'icon':e[5],'power_capacity':e[6],'bronze':e[7]}
            data.append(getdata)
        mysql.connection.commit()
        cur.close()
        return data