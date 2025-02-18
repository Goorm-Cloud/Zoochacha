import os
from flask import Flask
from .routes import admin_bp, login_bp
from services.common import config, db, migrate
from services.common.oauth import oauth

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = os.urandom(24)  # 임시 키 설정
    #app.config.from_object(config)


    # OAuth 초기화
    oauth.init_app(app)
    oauth.register(
        name='oidc',
        authority='https://cognito-idp.ap-northeast-2.amazonaws.com/ap-northeast-2_HroMsatHG',
        client_id='77g5eu474omofv1t6ss848gn9u',
        client_secret=app.config['CLIENT_SECRET'],
        server_metadata_url='https://cognito-idp.ap-northeast-2.amazonaws.com/ap-northeast-2_HroMsatHG/.well-known/openid-configuration',
        client_kwargs={'scope': 'phone openid email'}
    )

    #ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from services.common import models


    # 블루프린트 등록
    app.register_blueprint(admin_bp)
    app.register_blueprint(login_bp)


    return app


