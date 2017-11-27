from flask import Flask
from flask_environments import Environments
from flask_cors import CORS

from app.extensions import db, api


def create_app(config_obj):
    app = Flask(__name__)
    env = Environments(app)
    env.from_object(config_obj)

    # init extensions
    api.init_app(app)
    db.init_app(app)
    CORS(app)

    return app
