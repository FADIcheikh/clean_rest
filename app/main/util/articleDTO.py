from flask_restplus import Namespace, fields


class articleDTO:
    api = Namespace('article', description='Article related operations')
    user = api.model('article', {
        'title': fields.String( description='title of the article'),
        'body': fields.String(required=True, description='body of the article'),
        'id': fields.Integer(description='article Identifier')
})