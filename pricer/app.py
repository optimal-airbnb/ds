"""Main app/routing file for Pricer."""
from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    
    # ... TODO make the app!
    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app