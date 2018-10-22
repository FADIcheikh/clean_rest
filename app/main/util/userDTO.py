from flask_restplus import Namespace, fields


class UserDTO:
    api = Namespace('user', description='User related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'nom': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'id': fields.String(description='user Identifier')
})