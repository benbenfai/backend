from flask_restful import Resource
from flask import Flask,request
from schema.hardware_schema import Schema
from unitity.unitity import Tool,Model
from database.cpu import cpuModel
from database.gpu import gpuModel
from database.motherboard import motherboardModel
from database.powersupply import powersupplyModel
from database.ram import ramModel
from database.storage import storageModel
from database.cases import casesModel
import os
from werkzeug.utils import secure_filename
from imgurpython import ImgurClient
#from resources.config import client_id, client_secret,access_token,refresh_token
import json
import requests
import base64
import logging
from requests.packages import urllib3

logging.captureWarnings(True)
urllib3.disable_warnings()

schema = Schema(many=False)
getdata = Tool()

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploadimage')
os.makedirs(uploads_dir,exist_ok=True)

#def convertToBinaryData(filename):
    #with open(filename, 'rb') as file:
        #binaryData = file.read()
    #return binaryData

class addHardware(Resource):

    def post(self):

        rtype = request.form['type']
        #print(rtype)

        if rtype == 'cpu':

            result = schema.load(request.form.to_dict())
            #print(result)
            check = cpuModel.get_cpu(result['name'])
            #print(check)
            #print(request.files['icon'])
            #bolbdata=convertToBinaryData(request.files['icon'])
            #print(bolbdata)
            #print(uimage)
            #image.decode(uimage)
            #print(image)

            if check == None:

                #simagename=secure_filename(uimage.filename)

                #uimage.save(os.path.join(uploads_dir, simagename))

                #path = os.path.join(uploads_dir, simagename)

                #uimage = client.upload_from_path(path, config=None, anon=True)

                #img = base64.b64encode(uimage.read())
                #print(img)

                insertdata = cpuModel(
                    result['name'],
                    result['description'],
                    int(round(float(result['price']))),
                    request.files['icon'].read(),
                    result['tdp'],
                    result['socket'],
                    result['ramtype']
                )

                insertdata.add_cpu()

                return {
                    'message': 'insert success'
                }
            else:
                return {
                    'message': 'cpu already exist!'
                },403

        if rtype == 'gpu':

            result = schema.load(request.form.to_dict())
            #print(result)
            check = gpuModel.get_gpu(result['name'])
            #print(check)
            #print(request.files['icon'])

            if check == None:

                insertdata = gpuModel(
                    result['name'],
                    result['description'],
                    int(round(float(result['price']))),
                    request.files['icon'].read(),
                    result['tdp'],
                    result['vram']
                )

                insertdata.add_gpu()

                return {
                    'message': 'insert success'
                }
            else:
                return {
                    'message': 'gpu already exist!'
                },403

        if rtype == 'motherboard':

            result = schema.load(request.form.to_dict())
            #print(result)
            check = motherboardModel.get_motherboard(result['name'])
            #print(check)
            #print(request.files['icon'])

            if check == None:

                insertdata = motherboardModel(
                    result['name'],
                    result['description'],
                    int(round(float(result['price']))),
                    request.files['icon'].read(),
                    result['socket'],
                    result['ramtype'],
                    result['m2'],
                    result['mbsize']
                )

                insertdata.add_motherboard()

                return {
                    'message': 'insert success'
                }
            else:
                return {
                    'message': 'motherboard already exist!'
                },403
                
        if rtype == 'powersupply':

            result = schema.load(request.form.to_dict())
            #print(result)
            check = powersupplyModel.get_powersupply(result['name'])
            #print(check)
            #print(request.files['icon'])

            if check == None:

                insertdata = powersupplyModel(
                    result['name'],
                    result['description'],
                    int(round(float(result['price']))),
                    request.files['icon'].read(),
                    int(round(float(result['pcapacity']))),
                    result['bronze']
                )

                insertdata.add_powersupply()

                return {
                    'message': 'insert success'
                }
            else:
                return {
                    'message': 'powersupply already exist!'
                },403
        
        if rtype == 'ram':

            result = schema.load(request.form.to_dict())
            #print(result)
            check = ramModel.get_ram(result['name'])
            #print(check)
            #print(request.files['icon'])

            if check == None:

                insertdata = ramModel(
                    result['name'],
                    result['description'],
                    int(round(float(result['price']))),
                    request.files['icon'].read(),
                    int(round(float(result['rcapacity']))),
                    result['frequency'],
                    result['ramtype']
                )

                insertdata.add_ram()

                return {
                    'message': 'insert success'
                }
            else:
                return {
                    'message': 'ram already exist!'
                },403

        if rtype == 'storage':

            result = schema.load(request.form.to_dict())
            #print(result)
            check = storageModel.get_storage(result['name'])
            #print(check)
            #print(request.files['icon'])

            if check == None:

                insertdata = storageModel(
                    result['name'],
                    result['description'],
                    int(round(float(result['price']))),
                    request.files['icon'].read(),
                    int(result['tdp']),
                    result['scapacity'],
                    result['port'],
                    result['size']
                )

                insertdata.add_storage()

                return {
                    'message': 'insert success'
                }
            else:
                return {
                    'message': 'storage already exist!'
                },403

        if rtype == 'cases':

            result = schema.load(request.form.to_dict())
            #print(result)
            check = casesModel.get_cases(result['name'])
            #print(check)
            #print(request.files['icon'])

            if check == None:

                insertdata = casesModel(
                    result['name'],
                    result['description'],
                    int(round(float(result['price']))),
                    request.files['icon'].read(),
                    result['size'],
                    result['mbsize']
                )

                insertdata.add_cases()

                return {
                    'message': 'insert success'
                }
            else:
                return {
                    'message': 'cases already exist!'
                },403