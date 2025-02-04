# /routes/apiRoutes.py
from flask import Blueprint
from controllers.apiController import get_data, post_data

api_routes = Blueprint('api_routes', __name__)

# Define the routes
api_routes.route('/api/get', methods=['GET'])(get_data)
api_routes.route('/api/post', methods=['POST'])(post_data)

