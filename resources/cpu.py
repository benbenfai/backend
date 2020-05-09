from flask_restful import Resource
from flask import Flask,request, send_file, jsonify, Response, url_for
from flask.views import MethodView
from schema.hardware_schema import cpuSchema
from unitity.unitity import Tool,Model
from database.cpu import cpuModel
import os
#from werkzeug.utils import secure_filename
from imgurpython import ImgurClient
#from resources.config import client_id, client_secret,access_token,refresh_token
import json
import requests
import base64
import logging
from requests.packages import urllib3
from io import BytesIO
from werkzeug.wsgi import FileWrapper
#import werkzeug
#import jsonpickle
import base64
import urllib.request

logging.captureWarnings(True)
urllib3.disable_warnings()

cpu_schema = cpuSchema(many=False)
getdata = Tool()

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploadimage')
os.makedirs(uploads_dir,exist_ok=True)

#client = ImgurClient(client_id, client_secret, access_token, refresh_token)

class Cpu(Resource):

    def get(self):

        result = cpu_schema.load(getdata.get_param())
        cpu = cpuModel.get_cpu(result['cpu'])
        if cpu == None:
                return {
                    'message': 'cpu not exist'
                }
        else:
            return {
                'message': '',
                'cpu': cpu_schema.dump(cpu),
            }

    def post(self):

        result = cpu_schema.load(getdata.get_param())
        cpu = cpuModel.get_cpu(result['cpu'])
        if cpu == None:
            return {
                'message': 'cpu not exist!'
            }, 403
        else:
            return {
                'message': '',
                'cpu': cpu_schema.dump(cpu),
            }

    def put(self):

        result = cpu_schema.load(getdata.get_param())
        cpu = cpuModel.get_cpu(result['cpu'])

        if cpu != None:
            cpu = cpuModel(result['cpu'], result['description'], result['lowprice'],
                  result['icon'], result['tdp'], result['socket'],
                  result['ramtype'])
            cpu.update_cpu()
            return {
                'message': 'Update cpu success',
                'cpu': cpu_schema.dump(cpu),
            }
        else:
            return {
                'message': 'Can not update!',
                'cpu': cpuModel.cpu
            }

class CpuImage(MethodView):

    def get(self,name):

        image = cpuModel.get_cpu(name)
        bdata = BytesIO(image['icon'])
        w = FileWrapper(bdata)
        return Response(w, mimetype='image/jpeg', direct_passthrough=True)

class getAllCpu(Resource):

    def get(self):

        getdata = cpuModel.get_all()

        if getdata == None:
                return {
                    'message': 'cpu not exist'
                }
        else:
            alldata = {}

            i = 0

            for e in getdata:

                #alldata[i] = cpu_schema.dump(e)
                #print(e['icon'])
                #img = str(e['icon'])

                #bdata = BytesIO(e['icon'])
                #w = FileWrapper(bdata)
                #img = Response(w, mimetype='image/jpeg', direct_passthrough=True)
                #url = url_for(img)
                #print(url)
                alldata[i] = {
                    'cpu': e['cpu'],
                    'ramtype': e['ramtype'],
                    'socket': e['socket'],
                    'highprice': e['highprice'],
                    'tdp': e['tdp'],
                    'description': e['description'],
                    'lowprice': e['lowprice'],
                    'icon': '/hardware/cpuimg/'+str(e['cpu'])
                }
                i= i+1

            #print(alldata)

            return {
                    "data": alldata
                }

class addAllCpu(Resource):

    def post(self):

        result = cpu_schema.load(request.form.to_dict())
        cpu = cpuModel.get_cpu(result['name'])
        uimage = request.files['icon']
        print(uimage)
        print(result)

        if cpu == None:

            simagename=secure_filename(uimage.filename)

            uimage.save(os.path.join(uploads_dir, simagename))

            #path = os.path.join(uploads_dir, simagename)

            #uimage = client.upload_from_path(path, config=None, anon=True)

            img = base64.b64encode(uimage.read())
            print(img)

            cpudata = cpuModel(
                result['name'],
                result['description'],
                result['price'],
                uimage,
                result['tdp'],
                result['socket'],
                result['ramtype']
            )

            cpudata.add_cpu()

            return {
                'message': 'insert success',
                'cpu': cpu_schema.dump(result),
                'icon': simagename
            }
        else:
            return {
                'message': 'cpu already exist!',
                'cpu': cpu_schema.dump(result),
            },403

