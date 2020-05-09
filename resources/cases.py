from flask_restful import Resource
from flask import Flask,request, send_file, jsonify, Response, url_for
from flask.views import MethodView
from io import BytesIO
from werkzeug.wsgi import FileWrapper
from schema.hardware_schema import casesSchema
from unitity.unitity import Tool,Model
from database.cases import casesModel

cases_schema = casesSchema(many=False)
getdata = Tool()

class Cases(Resource):

    def get(self):

        result = cases_schema.load(getdata.get_param())
        cases = casesModel.get_cases(result['cases'])
        if cases == None:
                return {
                    'message': 'cases not exist'
                }
        else:
            return {
                'message': '',
                'cases': cases_schema.dump(cases),
            }

    def post(self):

        result = cases_schema.load(getdata.get_param())
        cases = casesModel.get_cases(result['cases'])
        if cases == None:
            return {
                'message': 'cases not exist!'
            }, 403
        else:
            return {
                'message': '',
                'cases': cases_schema.dump(cases),
            }

class CasesImage(MethodView):

    def get(self,name):

        image = casesModel.get_cases(name)
        bdata = BytesIO(image['icon'])
        w = FileWrapper(bdata)
        return Response(w, mimetype='image/jpeg', direct_passthrough=True)

class getAllCases(Resource):

    def get(self):

        getdata = casesModel.get_all()
        if getdata == None:
                return {
                    'message': 'cases not exist'
                }
        else:
            alldata = {}

            i = 0

            for e in getdata:
                alldata[i] = {
                    'cases': e['cases'],
                    'highprice': e['highprice'],
                    'description': e['description'],
                    'lowprice': e['lowprice'],
                    'icon': '/hardware/casesimg/'+str(e['cases']),
                    'storagesize':e['storagesize'],
                    'mbsize':e['mbsize']
                }
                i= i+1

            return {
                    "data": alldata
                }


