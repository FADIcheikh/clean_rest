from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.article_controller import api as article_ns
from .main.controller.commentaire_controller import api as comments_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API ',
          version='1.0',
          description='test flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(article_ns, path='/article')
api.add_namespace(comments_ns, path='/comments')