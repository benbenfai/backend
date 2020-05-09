from flask_restful import Resource
from flask import Flask,request, send_file, jsonify, Response, url_for
from flask.views import MethodView
from schema.hardware_schema import gpuSchema
from unitity.unitity import Tool,Model
from database.gpu import gpuModel
from io import BytesIO
from werkzeug.wsgi import FileWrapper

gpu_schema = gpuSchema(many=False)
getdata = Tool()

class Gpu(Resource):

    def get(self):

        result = gpu_schema.load(getdata.get_param())
        gpu = gpuModel.get_gpu(result['gpu'])
        if gpu == None:
                return {
                    'message': 'gpu not exist'
                }
        else:
            return {
                'message': '',
                'gpu': gpu_schema.dump(gpu),
            }

    def post(self):

        result = gpu_schema.load(getdata.get_param())
        gpu = gpuModel.get_gpu(result['gpu'])
        if gpu == None:
            return {
                'message': 'gpu not exist!'
            }, 403
        else:
            return {
                'message': '',
                'gpu': gpu_schema.dump(gpu),
            }

    def put(self):

        result = gpu_schema.load(getdata.get_param())
        gpu = gpuModel.get_gpu(result['gpu'])

        if gpu != None:
            gpu = gpuModel(result['gpu'], result['description'], result['lowprice'], result['icon'], result['tdp'], result['vram'])
            gpu.update_gpu()
            return {
                'message': 'Update gpu success',
                'gpu': gpu_schema.dump(gpu),
            }
        else:
            return {
                'message': 'Can not update!',
                'gpu': gpuModel.gpu
            }

class GpuImage(MethodView):

    def get(self,name):

        image = gpuModel.get_gpu(name)
        bdata = BytesIO(image['icon'])
        w = FileWrapper(bdata)
        return Response(w, mimetype='image/jpeg', direct_passthrough=True)

class getAllGpu(Resource):

    def get(self):

        getdata = gpuModel.get_all()
        if getdata == None:
                return {
                    'message': 'gpu not exist'
                }
        else:
            alldata = {}

            i = 0

            for e in getdata:
                alldata[i] = {
                    'gpu': e['gpu'],
                    'vram': e['vram'],
                    'highprice': e['highprice'],
                    'tdp': e['tdp'],
                    'description': e['description'],
                    'lowprice': e['lowprice'],
                    'icon': '/hardware/gpuimg/'+str(e['gpu'])
                }
                i= i+1

            return {
                    "data": alldata
                }


