from functools import wraps
from flask import request, jsonify
from flask import json
from marvel_api.models import User
import secrets
import decimal



def token_required(flask_function):
    @wraps(flask_function)
    def decorated(*args, **kwargs):
        owner_token = None
        print(owner_token)
        if 'access-token' in request.headers:
            owner_token = request.headers['access-token'].split(" ")[1]
        if not owner_token:
            print(owner_token)
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            current_user_token = User.query.filter_by(owner_token = owner_token).first()
            print(owner_token)
        except:
            owner = User.query.filter_by(owner_token = owner_token).first()

            if owner_token != owner.owner_token and secrets.compare_digest(owner_token, owner.owner_token):
                return jsonify({'message': 'Invalid Token!'})
        return flask_function(current_user_token, *args, **kwargs)
    return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return (JSONEncoder,self).default(obj)