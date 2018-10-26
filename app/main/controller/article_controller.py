from flask import request
from flask_restplus import Resource

from ..util.articleDTO import articleDTO
from ..service.article_service import get_all_articles, add_an_article, update_an_article, get_an_article, delete_an_article


api = articleDTO.api
_article = articleDTO.article

"""GET ALL"""
@api.route('/')
class ArticleList(Resource):
    @api.doc('get_all_articles')
    @api.marshal_list_with(_article, envelope='data_articles')
    @api.response(204, 'There is no articles in the DB.')
    def get(self):
        return get_all_articles()


    """ADD"""

    @api.expect(_article, 'new article')
    @api.doc('Add an article')
    @api.response(201, 'article added.')
    @api.response(400, 'title already exists.')
    def post(self):
        data = request.json
        return add_an_article(data=data)


    """PUT"""

    @api.expect(_article, 'article to update')
    @api.doc('update an article')
    @api.response(200, 'article updated.')
    @api.response(201, 'article doesnt exists, the given article is created instead.')
    def put(self):
        data = request.json
        return update_an_article(data=data)


"""GET BY ID"""
@api.route('/<_id>')
@api.param('_id', 'article identifier')
class User(Resource):
    @api.doc('get_article_by_id')
    @api.marshal_with(_article, envelope='data_articles')
    @api.response(404, 'There is no articles with the given identifier.')
    @api.response(200, 'success')
    def get(self,_id):
        return get_an_article(_id)

    """DELETE"""
    @api.doc('delete an article')
    @api.response(200, 'article deleted.')
    @api.response(400, 'there is no articles with the given identifier.')
    def delete(self,_id):
        return delete_an_article(_id)