from flask_restful import Resource
from flask import request
from schema.build_schema import  listhardwareSchema,listnoSchema
from unitity.unitity import Tool,Model
from database.listhardware import listhardwareModel

listhardware_schema =  listhardwareSchema(many=False)
listno_schema = listnoSchema(many=False)
getdata = Tool()

class Listhardware(Resource):

    def get(self):

        result = listhardware_schema.load(getdata.get_param())
        listinf = listhardwareModel.get_listhardware(result['listno'])
        if listinf == None:
                return {
                    'message': 'hardware not exist'
                }
        else:
            return {
                'message': '',
                'list': listhardware_schema.dump(listinf),
            }

    def post(self):

        result = listhardware_schema.load(getdata.get_param())

        try:
            listinf = listhardwareModel(result['hardware'],result['htype'])
            listinf.add_listhardware()
            return {
                'message': 'Create build success',
                'list': listhardware_schema.dump(listinf),
            }
        except:
            return {
                'message': 'database error',
            }

    def put(self):

        result = listhardware_schema.load(getdata.get_param())

        try:
            listinf = listhardwareModel(result['hardware'],result['htype'])
            listhardwareModel.listno = result['listno']
            listinf.update_listhardware()
            return {
                'message': 'Update build hardware success',
                'list': listhardware_schema.dump(listinf),
            }
        except:
            return {
                'message': 'build hardware can not update!',
            }
    
    def delete(self):

        result = listhardware_schema.load(getdata.get_param())
        listinf = listhardwareModel.get_listhardware(result['listno'])
        if listinf == None:
                return {
                    'message': 'build hardware not exist'
                }
        else:
            listhardwareModel.delete_listhardware(result['listno'])
            return {
                'message': "build hardware '{0}' deleted".format(result['hardware'])
            }

class getAllListhardware(Resource):

    def get(self):

        getdata = listhardwareModel.get_all()
        if getdata == None:
                return {
                    'message': 'list not exist'
                }
        else:
            alldata = {}

            for e in range(len(getdata)):
                alldata[e] = listhardware_schema.dump(e)

            return {
                    "data": alldata
                }

