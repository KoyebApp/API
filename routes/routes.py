# routes.py
from flask import Blueprint
from modules import create_tinyurl, generate_qr_code, download_youtube, get_data

api_routes = Blueprint('routes', __name__)

# General API route
api_routes.route('/api/get', methods=['GET'])(get_data)

# Tool routes for TinyURL, QR Code, and YouTube downloader (GET only)
routes.route('/api/tinyurl', methods=['GET'])(create_tinyurl)
routes.route('/api/qrcode', methods=['GET'])(generate_qr_code)
routes.route('/api/ytdl', methods=['GET'])(download_youtube)
