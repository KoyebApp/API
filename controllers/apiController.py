# /controllers/apiController.py
from flask import request, jsonify

# Handler for GET requests
def get_data():
    return jsonify({"message": "This is a GET response"})

# Handler for POST requests
def post_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    return jsonify({
        "message": "This is a POST response",
        "data": data
    })
  
