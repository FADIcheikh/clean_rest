from sqlalchemy import Column, String, Integer, Date
from app.main import db
from sqlalchemy.orm import relationship

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    body = db.Column(db.String(1000))
    #navigation prop
    users = relationship(
        'User',
        secondary='commentaire'
    )

    def __init__(self, title, body,*args, **kwargs):
        self.title = title
        self.body = body

    def toString(self):
        return "article: "+self.body




