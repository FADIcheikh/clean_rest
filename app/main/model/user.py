from sqlalchemy import Column, String, Integer, Date
import  json
from app.main import db
import flask_bcrypt

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    # hash password
    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __init__(self, nom,email,password,*args, **kwargs):
        self.nom = nom
        self.email = email
        self.password = password


    def toString(self):
        return  "user: "+self.nom + " email : "+self.email

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def getUserById(self,_id):
        if self.id == _id:
            return self

    def equalsTo(self,User):
        if self.id == User.id:
            return True
        else:
            return False




