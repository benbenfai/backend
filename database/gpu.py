from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class gpuModel:

    no=''
    gpu =''
    description = ''
    lowprice = ''
    highprice = ''
    icon = ''
    tdp = ''
    vram = ''

    def __init__(self,gpu,description,lowprice,icon,tdp,vram):
        self.gpu = gpu
        self.description = description
        self.lowprice = lowprice
        #self.highprice = highprice
        self.icon = icon
        self.tdp = tdp
        self.vram = vram

    def add_gpu(self):
        cur = mysql.connection.cursor()
        sql = """insert into gpu (gpu,description,lowprice,icon,tdp,vram) 
        values(%s,%s,%s,%s,%s,%s)
        """
        cur.execute(sql,(str(self.gpu),str(self.description),str(self.lowprice),self.icon,str(self.tdp),str(self.vram)))
        mysql.connection.commit()
        cur.close()

    def update_gpu(self):
        cur = mysql.connection.cursor()
        sql = """update gpu set gpu='{0}',description='{1}',
        lowpricen='{2}' highprice='{3}' icon='{4}' tdp='{5}' vram='{6}' where no='{7}'
        """.format(self.gpu,self.description,self.lowprice,self.highprice,self.icon,self.tdp,self.vram,self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_gpu(self):
        cur = mysql.connection.cursor()
        sql = "delete from gpu where no='{0}'".format(self.no)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_gpu(gpu):
        #gpudata = None
        cur = mysql.connection.cursor()
        sql = "select * from gpu where gpu='{0}'".format(gpu)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        getdata = {'no':result[0],'gpu':result[1],'description':result[2],'lowprice':result[3],'highprice':result[4],'icon':result[5],'tdp':result[6],'vram':result[7]}
        cur.close()
        return getdata

    def get_all():
        data = []
        cur = mysql.connection.cursor()
        sql = "select * from gpu"
        cur.execute(sql)
        result = cur.fetchall()
        for e in result:
            getdata = {'no':e[0],'gpu':e[1],'description':e[2],'lowprice':e[3],'highprice':e[4],'icon':e[5],'tdp':e[6],'vram':e[7]}
            data.append(getdata)
        mysql.connection.commit()
        cur.close()
        return data