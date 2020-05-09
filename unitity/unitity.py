from flask import request
from passlib.hash import pbkdf2_sha256 as sha256

class Tool:

    def get_param(self):

        data = request.get_json(force=False)
        if data is None:
            data = request.form
        return data

class Model:

    def generate_hash(self,password):
        return sha256.hash(password)

    def verify_hash(self,password, hash):
        return sha256.verify(password, hash)
