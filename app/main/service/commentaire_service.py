from app.main import db
from app.main.model.commentaire import Commentaire



def get_comments_article(id_article):
    list_comments = Commentaire.query.filter_by(id_article=id_article).all()
    print list_comments
    if not list_comments:
        response_object = {
            'status': 'fail',
            'message': 'There is no comments for the given article in the DB.'
        }
        return response_object, 204
    else:
        return list_comments