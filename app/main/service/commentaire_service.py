from app.main import db
from app.main.model.article import Article




def get_comments_article(id_article):
    list_comments = Article.query.filter_by(id=id_article).first().commentaires
    print type(list_comments)
    print list_comments
    return list_comments
    """
    if not list_comments:
        response_object = {
            'status': 'fail',
            'message': 'There is no comments for the given article in the DB.'
        }
        return response_object, 204
    else:
        return list_comments
    """