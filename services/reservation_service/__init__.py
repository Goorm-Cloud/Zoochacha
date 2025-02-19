import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ✅ 현재 디렉토리에 config.py가 있는지 확인하고 경로 추가
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# ✅ config.py 가져오기
from services.reservation_service.config import Config

# 기존 ORM 모델 사용
from services.common.models import db

def create_app():
    app = Flask(__name__)

    # ✅ 환경설정 로드 (config.py 활용)
    app.config.from_object(Config)

    # ✅ 데이터베이스 및 마이그레이션 초기화
    db.init_app(app)
    Migrate(app, db)

    # ✅ 블루프린트 등록
    from services.reservation_service.routes import parkinglot_bp
    app.register_blueprint(parkinglot_bp)

    from services.reservation_service.reservation_route import reservation_bp
    app.register_blueprint(reservation_bp)

    return app