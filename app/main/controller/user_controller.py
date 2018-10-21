from flask import request
from flask_restplus import Resource

from ..util.userDTO import UserDTO
from ..service.user_service import  get_all_users

api = UserDTO.api
_user = UserDTO.user

"""GET ALL"""
@api.route('/')
class UserList(Resource):
    @api.doc('get_all_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        return get_all_users()