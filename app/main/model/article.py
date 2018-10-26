from sqlalchemy import Column, String, Integer, Date
from app.main import db
from commentaire import commentaires


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    body = db.Column(db.String(1000))

    def __init__(self, title, body,*args, **kwargs):
        self.title = title
        self.body = body
        self.commentaires = []

    def toString(self):
        return "article: "+self.body


    #naviagtion props
    commentaires = db.relationship('User', secondary=commentaires, lazy='select',
                                     backref=db.backref('Article', lazy=True))


