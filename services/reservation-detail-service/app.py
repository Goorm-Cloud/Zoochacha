from flask import Flask
from common import config, db, migrate


def create_app():
    app = Flask(__name__, template_folder="services/common/templates")
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from common import models
    return app

