from flask import Flask, jsonify, request, json
from flask_mysqldb import MySQL
from datetime import datetime
from flask_restful import Resource, reqparse, Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from schema.user_schema import UserSchema
from common.jwt import jwt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token)

app = Flask(__name__)

api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = 'azbycxdwevfugthsirjqkplomn' 
jwt.init_app(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

user_schema = UserSchema(many=False)

class login (Resource):

    result = user_schema.load(request.form)
    name = result['username']
    email = result['email']
    password = result['password']

    @app.route('/register', methods=['POST'])
    def register(self):
        cur = mysql.connection.cursor()
        username = request.get_json()['username']
        email = request.get_json()['email']
        password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
        
        cur = mysql.connection.cursor()
        sql = "insert into user values('{0}','{1}','{2}')".format(email,username,password)
        cur.execute(sql)
        cur.commit()
        cur.close()
        
        result = {
            'username' : username,
            'email' : email,
            'password' : password,
        }

        return jsonify({'result' : result})
        

    @app.route('/login', methods=['POST'])
    def login(self):
        cur = mysql.connection.cursor()
        email = request.get_json()['email']
        password = request.get_json()['password']
        result = ""
        
        cur.execute("SELECT * FROM user where email = '" + str(email) + "'")
        data = cur.fetchone()
        
        if bcrypt.check_password_hash(data['password'], password):
            access_token = create_access_token(identity = {'username': data['username'],'email': data['email']})
            result = access_token
        else:
            result = jsonify({"error":"Invalid username and password"})
        
        return result
	
