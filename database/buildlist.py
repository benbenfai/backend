from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class buildlistModel:

    listno=''
    createDate =''
    cost = ''
    creator = ''

    def __init__(self,createDate,cost,creator):

        self.createDate = createDate
        self.cost = cost
        self.creator = creator

    def add_list(self):
        cur = mysql.connection.cursor()
        sql = """insert into buildlist (createDate,cost,creator) 
        values('{0}','{1}','{2}')
        """.format(self.createDate,self.cost,self.creator)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def update_list(self):
        cur = mysql.connection.cursor()
        sql = """update buildlist set
        costn='{0}'where listno='{1}'
        """.format(self.cost,self.listno)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_list(self):
        cur = mysql.connection.cursor()
        sql = "delete from buildlist where listno='{0}'".format(self.listno)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_list(self):
        listnodata = None
        cur = mysql.connection.cursor()
        sql = "select * from buildlist where listno='{0}'".format(self.listno)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        listnodata = buildlistModel(result[1],result[2],result[3])
        listnodata.no = result[0]
        cur.close()
        return listnodata

    def get_all():
        data = []
        cur = mysql.connection.cursor()
        sql = "select * from buildlist"
        cur.execute(sql)
        result = cur.fetchall()
        for e in result:
            row = buildlistModel(e[1],e[2],e[3])
            row.no = e[0]
            data.append(row)
        mysql.connection.commit()
        cur.close()
        return data