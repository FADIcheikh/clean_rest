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
    return User.query.filter_by(id=_id).first()