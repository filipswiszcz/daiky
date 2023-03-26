import os

from flask import Flask
from flask import escape


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route("/")
    def home(name: str = "Filip") -> str:
        return f"<h1>Welcome, {escape(name)}</h1>"
    
    return app