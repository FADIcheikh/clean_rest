from flask import request
from flask_restplus import Resource

from ..util.userDTO import UserDTO
from ..service.user_service import  get_all_users,get_a_user,add_a_user,update_a_user


api = UserDTO.api
_user = UserDTO.user

"""GET ALL"""
@api.route('/')
class UserList(Resource):
    @api.doc('get_all_users')
    @api.marshal_list_with(_user, envelope='data')
    @api.response(204, 'There is no users in the DB.')
    def get(self):
        return get_all_users()

    """ADD"""

    @api.expect(_user, 'new user')
    @api.doc('Add a user')
    @api.response(201, 'User created.')
    @api.response(400, 'email already exists.')
    def post(self):
        data = request.json
        return add_a_user(data=data)


    """PUT"""

    @api.expect(_user, 'user to update')
    @api.doc('update a user')
    @api.response(200, 'User updated.')
    @api.response(201, 'User doesnt exists, the given user is created instead.')
    def put(self):
        data = request.json
        return update_a_user(data=data)


"""GET BY ID"""
@api.route('/<_id>')
@api.param('_id', 'User identifier')
class User(Resource):
    @api.doc('get_user_by_id')
    @api.marshal_with(_user, envelope='data')
    @api.response(404, 'There is no user with the given identifier.')
    def get(self,_id):
        return get_a_user(_id)
