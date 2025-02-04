
# /app.py
from flask import Flask
from routes.apiRoutes import api_routes

app = Flask(__name__)

# Register the API routes
app.register_blueprint(api_routes)

# Serve static files (like your HTML interface)
app.static_folder = 'static'

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
  
