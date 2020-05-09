from flask_restful import Resource
from flask import Flask,request, send_file, jsonify, Response, url_for
from flask.views import MethodView
from io import BytesIO
from werkzeug.wsgi import FileWrapper
from schema.hardware_schema import storageSchema
from unitity.unitity import Tool,Model
from database.storage import storageModel

storage_schema = storageSchema(many=False)
getdata = Tool()

class Storage(Resource):

    def get(self):

        result = storage_schema.load(getdata.get_param())
        storage = storageModel.get_storage(result['storage'])
        if storage == None:
                return {
                    'message': 'storage not exist'
                }
        else:
            return {
                'message': '',
                'storage': storage_schema.dump(storage),
            }

    def post(self):

        result = storage_schema.load(getdata.get_param())
        storage = storageModel.get_storage(result['storage'])
        if storage == None:
            return {
                'message': 'storage not exist!'
            }, 403
        else:
            return {
                'message': '',
                'storage': storage_schema.dump(storage),
            }

    def put(self):

        result = storage_schema.load(getdata.get_param())
        storage = storageModel.get_storage(result['storage'])

        if storage != None:
            storage = storageModel(result['storage'], result['description'], result['lowprice'], result['highprice'], result['icon'], result['tdp'], result['capacity'], result['port'])
            storage.update_storage()
            return {
                'message': 'Update storage success',
                'storage': storage_schema.dump(storage),
            }
        else:
            return {
                'message': 'Can not update!',
                'storage': storageModel.storage
            }

class StorageImage(MethodView):

    def get(self,name):

        image = storageModel.get_storage(name)
        bdata = BytesIO(image['icon'])
        w = FileWrapper(bdata)
        return Response(w, mimetype='image/jpeg', direct_passthrough=True)

class getAllStorage(Resource):

    def get(self):

        getdata = storageModel.get_all()
        if getdata == None:
                return {
                    'message': 'storage not exist'
                }
        else:
            alldata = {}

            i = 0

            for e in getdata:
                alldata[i] = {
                    'storage': e['storage'],
                    'highprice': e['highprice'],
                    'description': e['description'],
                    'lowprice': e['lowprice'],
                    'icon': '/hardware/storageimg/'+str(e['storage']),
                    'tdp':e['tdp'],
                    'capacity':e['capacity'],
                    'port':e['port'],
                    'size':e['size']
                }
                i= i+1

            return {
                    "data": alldata
                }

