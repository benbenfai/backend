from flask_restful import Resource
from flask import request
from schema.user_schema import UserSchema,registerSchema
from unitity.unitity import Tool,Model
from database.user import UserModel,RevokedTokenModel
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

user_schema = UserSchema(many=False)
register_schema = registerSchema(many=False)
encrypt = Model()
getdata = Tool()

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}

class Userlogin(Resource):

    def post(self,username):

        result = user_schema.load(getdata.get_param())
        user = UserModel.get_user(result['username'])
        if user == None:
            return {
                'message': 'username not exist!'
            }, 403
        else:
            if encrypt.verify_hash(result['password'],user.password):
                access_token = create_access_token(identity = result['username'])
                refresh_token = create_refresh_token(identity = result['username'])
                return {
                    'message': '',
                    'user': user_schema.dump(user),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            else:
                return {
                    'message': 'password not match'
                }

    def put(self):

        result = user_schema.load(getdata.get_param())
        user = UserModel.get_user(result['username'])

        if user != None:
            user = UserModel(result['username'], result['email'], result ['password'])
            user.update_user()
            return {
                'message': 'Update user success',
                'user': user_schema.dump(user),
            }
        else:
            return {
                'message': 'Can not update!',
                'user': UserModel.username
            }

class UserRegistration(Resource):

    def post(self):

        result = register_schema.load(getdata.get_param())
        user = UserModel.get_user(result['username'])
        if user != None:
            return {
                'message': 'username {0} is exist!'.format(result['username'])
            }, 403
        else:
            try:
                user = UserModel(result['username'],result['email'],encrypt.generate_hash(result['password']))
                user.add_user()
                access_token = create_access_token(identity = result['username'])
                refresh_token = create_refresh_token(identity = result['username'])
                return {
                    'message': 'Registration success',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                    }
            except:
                return {
                    'message': 'database insert error',
                    }

        return {
            'message': '',
            'user': user_schema.dump(user)
        }

class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500

#class Users(Resource):
#    def get(self):
#        return {
#            'message': '',
#            'users': user_schema.dump(UserModel.get_all_user())
#        }

        