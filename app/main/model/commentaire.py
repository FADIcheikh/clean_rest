from sqlalchemy import Column, String, Integer, Date
from app.main import db

commentaire=db.Column(db.String(500))


commentaires = db.Table('commentaires',
                        db.Column('id_article', db.Integer, db.ForeignKey('article.id'), primary_key=True),
                        db.Column('id_user', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                        db.Column('com',db.String(500))

)