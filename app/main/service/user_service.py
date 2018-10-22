from app.main import db
from app.main.model.user import User



def get_all_users():
    return User.query.all()


def get_a_user(_id):
    return User.query.filter_by(id=_id).first()