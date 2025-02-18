import os
from flask import Flask
from dotenv import load_dotenv

# 📌 프로젝트의 BASE_DIR 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")
ENV_PATH = os.path.join(BASE_DIR, "..", ".env")  # 프로젝트 루트의 .env 파일 로드

# ✅ .env 파일 로드
load_dotenv(ENV_PATH)

def create_app():
    app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # 📌 KAKAO API KEY 로드
    app.config['KAKAO_API_KEY'] = os.getenv("KAKAO_API_KEY")
    if not app.config['KAKAO_API_KEY']:
        raise ValueError("❌ KAKAO_API_KEY가 설정되지 않았습니다! .env 파일을 확인하세요.")

    # 📌 블루프린트 등록
    from .routes import main
    app.register_blueprint(main)

    from .auth.routes import auth  # 🔥 회원가입 & 로그인 블루프린트 추가
    app.register_blueprint(auth, url_prefix="/auth")

    return app
