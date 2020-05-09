from flask_restful import Resource
from flask import Flask,request, send_file, jsonify, Response, url_for
from flask.views import MethodView
from schema.hardware_schema import motherboardSchema
from unitity.unitity import Tool,Model
from database.motherboard import motherboardModel
from io import BytesIO
from werkzeug.wsgi import FileWrapper

motherboard_schema = motherboardSchema(many=False)
getdata = Tool()

class Motherboard(Resource):

    def get(self):

        result = motherboard_schema.load(getdata.get_param())
        motherboard = motherboardModel.get_motherboard(result['motherboard'])
        if motherboard == None:
                return {
                    'message': 'motherboard not exist'
                }
        else:
            return {
                'message': '',
                'motherboard': motherboard_schema.dump(motherboard),
            }

    def post(self):

        result = motherboard_schema.load(getdata.get_param())
        motherboard = motherboardModel.get_motherboard(result['motherboard'])
        if motherboard == None:
            return {
                'message': 'motherboard not exist!'
            }, 403
        else:
            return {
                'message': '',
                'motherboard': motherboard_schema.dump(motherboard),
            }

    def put(self):

        result = motherboard_schema.load(getdata.get_param())
        motherboard = motherboardModel.get_motherboard(result['motherboard'])

        if motherboard != None:
            motherboard = motherboardModel(result['motherboard'], result['description'], result['lowprice'], result['highprice'], result['icon'], result['socket'])
            motherboard.update_motherboard()
            return {
                'message': 'Update motherboard success',
                'motherboard': motherboard_schema.dump(motherboard),
            }
        else:
            return {
                'message': 'Can not update!',
                'motherboard': motherboardModel.motherboard
            }

class MotherboardImage(MethodView):

    def get(self,name):

        image = motherboardModel.get_motherboard(name)
        bdata = BytesIO(image['icon'])
        w = FileWrapper(bdata)
        return Response(w, mimetype='image/jpeg', direct_passthrough=True)

class getAllMotherboard(Resource):

    def get(self):

        getdata = motherboardModel.get_all()
        if getdata == None:
                return {
                    'message': 'motherboard not exist'
                }
        else:
            alldata = {}

            i = 0

            for e in getdata:
                alldata[i] = {
                    'motherboard': e['motherboard'],
                    'highprice': e['highprice'],
                    'description': e['description'],
                    'lowprice': e['lowprice'],
                    'icon': '/hardware/motherboardimg/'+str(e['motherboard']),
                    'socket':e['socket'],
                    'ramtype':e['ramtype'],
                    'm2':e['m2'],
                    'mbsize':e[ 'mbsize']
                }
                i= i+1

            #print(alldata)

            return {
                    "data": alldata
                }

