from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, send_from_directory
from flask_restful import Api
from flask_mysqldb import MySQL
from resources.user import Userlogin,UserRegistration,UserLogoutAccess,UserLogoutRefresh,TokenRefresh
from resources.cpu import Cpu,getAllCpu,addAllCpu,CpuImage
from resources.gpu import Gpu,getAllGpu,GpuImage
from resources.motherboard import Motherboard,getAllMotherboard,MotherboardImage
from resources.powersupply import Powersupply,getAllPowersupply,PowersupplyImage
from resources.ram import Ram,getAllRam,RamImage
from resources.storage import Storage,getAllStorage,StorageImage
from resources.cases import Cases,getAllCases,CasesImage
from resources.buildlist import List,getAlllist
from resources.listhardware import Listhardware,getAllListhardware
from resources.hardware import addHardware
from common.ma import ma
from common.jwt import jwt
from flask_cors import CORS
from database.user import RevokedTokenModel

app = Flask(__name__)
api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = 'azbycxdwevfugthsirjqkplomn' 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt.init_app(app)
CORS(app)

mysql = MySQL(app)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)

@app.route('/')
def index():
    return render_template('index.html')

api.add_resource(Userlogin, '/user/<string:username>')
api.add_resource(UserRegistration, '/user/register')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefresh, '/logout/refresh')
api.add_resource(TokenRefresh, '/token/refresh')
#api.add_resource(Users, '/users')
api.add_resource(addHardware, '/hardware/add')
api.add_resource(Cpu,'/hardware/cpu')
api.add_resource(getAllCpu, '/hardware/allcpu')
api.add_resource(CpuImage, '/hardware/cpuimg/<string:name>')
api.add_resource(Gpu, '/hardware/gpu')
api.add_resource(getAllGpu, '/hardware/allgpu')
api.add_resource(GpuImage, '/hardware/gpuimg/<string:name>')
api.add_resource(Motherboard, '/hardware/motherboard')
api.add_resource(getAllMotherboard, '/hardware/allmotherboard')
api.add_resource(MotherboardImage, '/hardware/motherboardimg/<string:name>')
api.add_resource(Powersupply, '/hardware/powersupply')
api.add_resource(getAllPowersupply, '/hardware/allpowersupply')
api.add_resource(PowersupplyImage, '/hardware/powersupplyimg/<string:name>')
api.add_resource(Ram, '/hardware/ram')
api.add_resource(getAllRam, '/hardware/allram')
api.add_resource(RamImage, '/hardware/ramimg/<string:name>')
api.add_resource(Storage, '/hardware/storage')
api.add_resource(getAllStorage, '/hardware/allstorage')
api.add_resource(StorageImage, '/hardware/storageimg/<string:name>')
api.add_resource(Cases, '/hardware/cases')
api.add_resource(getAllCases, '/hardware/allcases')
api.add_resource(CasesImage, '/hardware/casesimg/<string:name>')

if __name__ == "__main__":
    ma.init_app(app)
    app.run()