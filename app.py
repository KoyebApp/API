# app.py
from flask import Flask
from routes import api_routes  # Import routes from routes.py

app = Flask(__name__)

# Register the routes
app.register_blueprint(api_routes)

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
    
