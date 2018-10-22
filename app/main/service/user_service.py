from app.main import db
from app.main.model.user import User



def get_all_users():
    list_users = User.query.all()
    if not list_users:
        response_object = {
            'status': 'success',
            'message': 'There is no users in the DB.'
        }
        return response_object, 204
    else:
        return list_users


def get_a_user(_id):
    user = User.query.filter_by(id=_id).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'there is no user with the given identifier.',
        }
        return response_object, 404
    else:
        return user



def add_a_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        user_to_add = User(
            email=data['email'],
            nom=data['nom'],
            password=data['password']
        )
        commit(user_to_add)

        response_object = {
            'status': 'success',
            'message': 'user created.',
        }
        return response_object,201
    else:
        response_object = {
            'status': 'fail',
            'message': 'there is already a user with the given email.',
        }
        return response_object, 400


def update_a_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'there is no user with the given email, user created instead.',
        }
        return response_object, 201

    else:


        user.email = data['email']
        user.password=data['password']
        user.nom=data['nom']
        merge(user)

        response_object = {
            'status': 'success',
            'message': 'user updated.',
        }
        return response_object,200




def commit(data):
    db.session.add(data)
    db.session.commit()

def merge(data):
    db.session.merge(data)
    db.session.commit()