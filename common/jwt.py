from flask_jwt_extended import JWTManager

jwt = JWTManager()

def login(self, username):

    access_token = create_access_token(identity=username)
    return {
        'access_token': access_token
    }, 200