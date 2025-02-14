from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from common import config

db = SQLAlchemy()
migrate = Migrate()
app = Flask(__name__)

def create_app():

    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)

    return app

