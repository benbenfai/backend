from flask_restful import Resource
from flask import Flask,request, send_file, jsonify, Response, url_for
from flask.views import MethodView
from io import BytesIO
from werkzeug.wsgi import FileWrapper
from schema.hardware_schema import ramSchema
from unitity.unitity import Tool,Model
from database.ram import ramModel

ram_schema = ramSchema(many=False)
getdata = Tool()

class Ram(Resource):

    def get(self):

        result = ram_schema.load(getdata.get_param())
        ram = ramModel.get_ram(result['ram'])
        if ram == None:
                return {
                    'message': 'ram not exist'
                }
        else:
            return {
                'message': '',
                'ram': ram_schema.dump(ram),
            }

    def post(self):

        result = ram_schema.load(getdata.get_param())
        ram = ramModel.get_ram(result['ram'])
        if ram == None:
            return {
                'message': 'ram not exist!'
            }, 403
        else:
            return {
                'message': '',
                'ram': ram_schema.dump(ram),
            }

    def put(self):

        result = ram_schema.load(getdata.get_param())
        ram = ramModel.get_ram(result['ram'])

        if ram != None:
            ram = ramModel(result['ram'], result['description'], result['lowprice'], result['highprice'], result['icon'], result['capacity'], result['frequency'])
            ram.update_ram()
            return {
                'message': 'Update ram success',
                'ram': ram_schema.dump(ram),
            }
        else:
            return {
                'message': 'Can not update!',
                'ram': ramModel.ram
            }

class RamImage(MethodView):

    def get(self,name):

        image = ramModel.get_ram(name)
        bdata = BytesIO(image['icon'])
        w = FileWrapper(bdata)
        return Response(w, mimetype='image/jpeg', direct_passthrough=True)

class getAllRam(Resource):

    def get(self):

        getdata = ramModel.get_all()
        if getdata == None:
                return {
                    'message': 'ram not exist'
                }
        else:
            alldata = {}

            i = 0

            for e in getdata:
                alldata[i] = {
                    'ram': e['ram'],
                    'highprice': e['highprice'],
                    'description': e['description'],
                    'lowprice': e['lowprice'],
                    'icon': '/hardware/ramimg/'+str(e['ram']),
                    'capacity':e['capacity'],
                    'frequency':e['frequency'],
                    'ramtype':e['ramtype']
                }
                i= i+1

            return {
                    "data": alldata
                }

