from flask import Flask
from flask_mongoengine import MongoEngine
from .holder import Memory
from .models.user import User

memory = Memory()
user = User("asd@asd.com", "asd")
memory.add_user(user)


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["MONGODB_SETTINGS"] = {
        "db": "daiky"
    }
    db = MongoEngine(app)

    from . import auth
    app.register_blueprint(auth.blueprint)

    @app.route("/")
    def home(name: str = "Filip") -> str:
        return "<h1>Welcome!</h1>"
        #return f"<h1>Welcome, {escape(name)}</h1>"
    
    return app