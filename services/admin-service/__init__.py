from flask import Flask
from .routes import admin_bp
from authlib.integrations.flask_client import OAuth
import os

def create_app():
    app = Flask(__name__)
    # config.py 파일 로드
    app.config.from_pyfile('config.py')

    # OAuth 등록
    oauth = OAuth(app)
    oauth.register(
        name='oidc',
        authority='https://cognito-idp.ap-northeast-2.amazonaws.com/ap-northeast-2_HroMsatHG',
        client_id='77g5eu474omofv1t6ss848gn9u',
        client_secret= app.config['CLIENT_SECRET'],
        server_metadata_url='https://cognito-idp.ap-northeast-2.amazonaws.com/ap-northeast-2_HroMsatHG/.well-known/openid-configuration',
        client_kwargs={'scope': 'phone openid email'}
    )

    # 블루프린트 등록
    app.register_blueprint(admin_bp)

    return app


