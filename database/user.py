from flask import Flask
from flask_mysqldb import MySQL
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)

class RevokedTokenModel:

    jti = ''
    
    def add(self):
        cur = mysql.connection.cursor()
        sql = "insert into revoked_tokens (jti) values('{0}')".format(self.jti)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()
    
    def is_jti_blacklisted(self):
        cur = mysql.connection.cursor()
        sql = "select * from revoked_tokens where jti ='{0}'".format(self.jti)
        cur.execute(sql)
        result = cur.fetchone()
        mysql.connection.commit()
        cur.close()
        return result[1]

class UserModel:
    username = ''
    email = ''
    password = ''
    userID = ''

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def add_user(self):
        cur = mysql.connection.cursor()
        sql = "insert into user (email,username,password) values('{0}','{1}','{2}')".format(self.email,self.username,self.password)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def update_user(self):
        cur = mysql.connection.cursor()
        sql = "update user set email='{0}',username='{1}',password='{2}' where userID='{3}'".format(self.email,self.username,self.password,self.userID)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def delete_user(self):
        cur = mysql.connection.cursor()
        sql = "delete from user where userID='{0}'".format(self.userID)
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

    def get_user(username):
        user = None
        cur = mysql.connection.cursor()
        sql = "select * from user where username='{0}'".format(username)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        user = UserModel(result[2],result[1],result[3])
        user.userID = result[0]
        cur.close()
        return user

    def get_email(email):
        user = None
        cur = mysql.connection.cursor()
        sql = "select * from user where email='{0}'".format(email)
        cur.execute(sql)
        result = cur.fetchone()
        if result is None:
            return None
        user = UserModel(result[2],result[1],result[3])
        user.userID = result[0]
        cur.close()
        return user

    def get_all_user(self):

        users = []

        cur = mysql.connection.cursor()
        sql = "select * from user"
        result = cur.execute(sql)
        for item in result:
            user = UserModel(item[1], item[2], item[3])
            user.id = item[0]
            users.append(user)
        cur.close()
        return users

    
    