from flask_restful import Resource
from flask import Flask,request, send_file, jsonify, Response, url_for
from flask.views import MethodView
from io import BytesIO
from werkzeug.wsgi import FileWrapper
from schema.hardware_schema import powersupplySchema
from unitity.unitity import Tool,Model
from database.powersupply import powersupplyModel

powersupply_schema = powersupplySchema(many=False)
getdata = Tool()

class Powersupply(Resource):

    def get(self):

        result = powersupply_schema.load(getdata.get_param())
        powersupply = powersupplyModel.get_powersupply(result['powersupply'])
        if powersupply == None:
                return {
                    'message': 'powersupply not exist'
                }
        else:
            return {
                'message': '',
                'powersupply': powersupply_schema.dump(powersupply),
            }

    def post(self):

        result = powersupply_schema.load(getdata.get_param())
        powersupply = powersupplyModel.get_powersupply(result['powersupply'])
        if powersupply == None:
            return {
                'message': 'powersupply not exist!'
            }, 403
        else:
            return {
                'message': '',
                'powersupply': powersupply_schema.dump(powersupply),
            }

    def put(self):

        result = powersupply_schema.load(getdata.get_param())
        powersupply = powersupplyModel.get_powersupply(result['powersupply'])

        if powersupply != None:
            powersupply = powersupplyModel(result['powersupply'], result['description'], result['lowprice'], result['highprice'], result['icon'], result['power_capacity'], result['bronze'])
            powersupply.update_powersupply()
            return {
                'message': 'Update powersupply success',
                'powersupply': powersupply_schema.dump(powersupply),
            }
        else:
            return {
                'message': 'Can not update!',
                'powersupply': powersupplyModel.powersupply
            }

class PowersupplyImage(MethodView):

    def get(self,name):

        image = powersupplyModel.get_powersupply(name)
        bdata = BytesIO(image['icon'])
        w = FileWrapper(bdata)
        return Response(w, mimetype='image/jpeg', direct_passthrough=True)

class getAllPowersupply(Resource):

    def get(self):

        getdata = powersupplyModel.get_all()
        if getdata == None:
                return {
                    'message': 'powersupply not exist'
                }
        else:
            alldata = {}

            i = 0

            for e in getdata:
                alldata[i] = {
                    'powersupply': e['powersupply'],
                    'highprice': e['highprice'],
                    'description': e['description'],
                    'lowprice': e['lowprice'],
                    'icon': '/hardware/powersupplyimg/'+str(e['powersupply']),
                    'power_capacity':e['power_capacity'],
                    'bronze':e['bronze']
                }
                i= i+1

            return {
                    "data": alldata
                }

