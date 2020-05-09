from flask_restful import Resource
from flask import request
from schema.build_schema import buildlistSchema,listnoSchema
from unitity.unitity import Tool,Model
from database.buildlist import buildlistModel

build_schema = buildlistSchema(many=False)
listno_schema = listnoSchema(many=False)
getdata = Tool()

class List(Resource):

    def get(self):

        result = build_schema.load(getdata.get_param())
        listinf = buildlistModel.get_list(result['listno'])
        if listinf == None:
                return {
                    'message': 'build not exist'
                }
        else:
            return {
                'message': '',
                'list': build_schema.dump(listinf),
            }

    def post(self):

        result = build_schema.load(getdata.get_param())

        try:
            listinf = buildlistModel(result['createDate'],result['cost'],result['creator'])
            listinf.add_list()
            return {
                'message': 'Create build success',
                'list': build_schema.dump(listinf),
            }
        except:
            return {
                'message': 'database error',
            }

    def put(self):

        result = build_schema.load(getdata.get_param())

        try:
            listinf = buildlistModel(result['createDate'],result['cost'],result['creator'])
            buildlistModel.listno = result['listno']
            listinf.update_list()
            return {
                'message': 'Update build success',
                'list': build_schema.dump(listinf),
            }
        except:
            return {
                'message': 'Can not update!',
            }
    
    def delete(self):

        result = build_schema.load(getdata.get_param())
        listinf = buildlistModel.get_list(result['listno'])
        if listinf == None:
                return {
                    'message': 'build not exist'
                }
        else:
            buildlistModel.delete_list(result['listno'])
            return {
                'message': 'build deleted',
            }

class getAlllist(Resource):

    def get(self):

        getdata = buildlistModel.get_all()
        if getdata == None:
                return {
                    'message': 'list not exist'
                }
        else:
            alldata = {}

            for e in range(len(getdata)):
                alldata[e] = build_schema.dump(e)

            return {
                    "data": alldata
                }

