from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
toolbar = DebugToolbarExtension()
db = SQLAlchemy()
flask_bcrypt = Bcrypt()

from .config import config_by_name




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    toolbar.init_app(app)
    return app