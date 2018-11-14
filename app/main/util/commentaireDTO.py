from flask_restplus import Namespace, fields


class commentaireDTO:
    api = Namespace('commentaires', description='commentaire related operations')
    commentaire = api.model('commentaire', {
        'com': fields.String(required=True, description='commentaire'),
        'id_user': fields.Integer(description='user Identifier'),
        'id_article': fields.Integer(description='article Identifier'),

})