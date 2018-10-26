from app.main import db
from app.main.model.article import Article



def get_all_articles():
    list_articles = Article.query.all()
    if not list_articles:
        response_object = {
            'status': 'fail',
            'message': 'There is no articles in the DB.'
        }
        return response_object, 204
    else:
        return list_articles


def get_an_article(_id):
    article = Article.query.filter_by(id=_id).first()
    if not article:
        response_object = {
            'status': 'fail',
            'message': 'there is no articles with the given identifier.',
        }
        return response_object, 404
    else:
        return article



def add_an_article(data):
    article = Article.query.filter_by(title=data['title']).first()
    if not article:
        article_to_add = Article(
            title=data['title'],
            body=data['body']
        )
        commit(article_to_add)

        response_object = {
            'status': 'success',
            'message': 'article added.',
        }
        return response_object,201
    else:
        response_object = {
            'status': 'fail',
            'message': 'there is already an article with the given title.',
        }
        return response_object, 400


def update_an_article(data):
    article = Article.query.filter_by(id=data['id']).first()
    if not article:
        response_object = {
            'status': 'fail',
            'message': 'there is no article with the given identifier, article created instead.',
        }
        return response_object, 201

    else:

        article.body = data['body']
        article.title=data['title']
        merge(article)

        response_object = {
            'status': 'success',
            'message': 'article updated.',
        }
        return response_object,200

def delete_an_article(_id):
    article = Article.query.filter_by(id=_id).first()
    if not article:
        response_object = {
            'status': 'fail',
            'message': 'there is no article with the given identifier',
        }
        return response_object,400
    else:
        db.session.delete(article)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'article deleted',
        }
        return response_object,200




# put them in a seperate class

def commit(data):
    db.session.add(data)
    db.session.commit()

def merge(data):
    db.session.merge(data)
    db.session.commit()
