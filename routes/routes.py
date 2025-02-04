# /routes/apiRoutes.py
from flask import Blueprint
from controllers.apiController import get_data, post_data

api_routes = Blueprint('routes', __name__)

# Define the routes
routes.route('/api/get', methods=['GET'])(get_data)
routes.route('/api/post', methods=['POST'])(post_data)

