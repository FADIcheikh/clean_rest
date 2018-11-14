from sqlalchemy import Column, String, Integer,  ForeignKey
from app.main import db
from sqlalchemy.orm import relationship, backref
from article import Article
from user import User



class Commentaire(db.Model):
    __tablename__ = 'commentaire'
    id_article = Column(Integer, ForeignKey('article.id'), primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'), primary_key=True)
    com = Column(String(500))
    article = relationship(Article, backref=backref("article_assoc"))
    user = relationship(User, backref=backref("user_assoc"))