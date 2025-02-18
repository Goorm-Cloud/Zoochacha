import os
import json
import sqlite3
import pandas as pd
from flask import render_template, send_from_directory, jsonify, current_app

# 📌 주차장 데이터 불러오기 함수 (DB 사용)
def load_parking_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DB_PATH = os.path.join(BASE_DIR, "common", "parking.db")

    if not os.path.exists(DB_PATH):
        print(f"❌ 데이터베이스 파일이 존재하지 않습니다! 경로: {DB_PATH}")
        return []

    try:
        # 데이터베이스 연결
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = """
        SELECT 
            parkinglot_id AS id, 
            parkinglot_name AS name, 
            parkinglot_add AS address, 
            latitude AS lat, 
            longitude AS lng, 
            parkinglot_div AS division,
            parkinglot_type AS type,
            parkinglot_num AS capacity,
            parkinglot_cost AS is_paid,
            parkinglot_day AS available_days,
            parkinglot_time AS hours
        FROM parkinglot
        """
        df = pd.read_sql_query(query, conn)

        # pandas 데이터프레임을 JSON으로 변환
        df = df.fillna("")  # NaN 값이 있으면 빈 문자열로 변환
        parking_data = df.to_dict(orient="records")

        conn.close()
        print("✅ 주차장 데이터 로드 성공!")
        return parking_data

    except Exception as e:
        print(f"❌ DB 데이터 로드 중 오류 발생: {e}")
        return []

# 📌 홈 페이지 렌더링
def home_view():
    kakao_api_key = current_app.config['KAKAO_API_KEY']
    return render_template("index.html", kakao_api_key=kakao_api_key)

# 📌 정적 파일 제공
def static_files(filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    STATIC_DIR = os.path.join(BASE_DIR, "map-service", "static")
    return send_from_directory(STATIC_DIR, filename)

# 📌 주차장 데이터 API
def get_parking_lots():
    parking_data = load_parking_data()
    return json.dumps(parking_data, ensure_ascii=False, default=str)
