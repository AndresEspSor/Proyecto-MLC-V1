from flask import Blueprint

from .chat_routes import chat_routes
from .html_routes import html_routes

routes = Blueprint('routes', __name__)

# Register all routes
routes.register_blueprint(chat_routes, url_prefix='/chat')
routes.register_blueprint(html_routes, url_prefix='/')