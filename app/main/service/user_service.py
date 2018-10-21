from app.main import db
from app.main.model.user import User



def get_all_users():
    return User.query.all()


