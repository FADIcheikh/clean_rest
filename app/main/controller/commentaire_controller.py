from flask import request
from flask_restplus import Resource

from ..util.commentaireDTO import commentaireDTO
from ..service.commentaire_service import get_comments_article


api = commentaireDTO.api
_commentaire = commentaireDTO.user
"""GET ALL"""
@api.route('/<_id>')
class CommentaireList(Resource):
    @api.param('_id', 'article identifier')
    @api.doc('get_all_commentaires')
    @api.marshal_list_with(_commentaire, envelope='data_comments')
    @api.response(204, 'There is no comments for the given article in the DB.')
    def get(self,_id):
        return get_comments_article(_id)