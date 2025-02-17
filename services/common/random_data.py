import sqlite3
import pandas as pd
import random
import faker
import os


# 데이터베이스 연결
db_path = os.path.abspath("parking.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# # Faker 라이브러리로 가짜 사용자 데이터 생성
# fake = faker.Faker()
# users = []
# for _ in range(50):
#     user_id = random.randint(1000, 9999)  # user_id를 INTEGER 값으로 생성
#     name = fake.name()[:20]  # VARCHAR(20) 제한
#     gender = random.choice(["Male", "Female"])
#     email = fake.email()[:50]  # VARCHAR(50) 제한
#     age = random.randint(18, 65)
#     phone = fake.phone_number()[:20] if random.random() > 0.2 else None  # VARCHAR(20) 제한
#     role = random.choice(["admin", "user"])  # VARCHAR(5) 제한

#     users.append((user_id, name, gender, email, age, phone, role))
#     cursor.execute("""
#         INSERT INTO user (user_id, name, gender, email, age, phone, role)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#     """, (user_id, name, gender, email, age, phone, role))

# print("50명의 가짜 사용자 데이터를 삽입 완료")

# 기존 사용자 ID 가져오기
cursor.execute("SELECT user_id FROM user")
user_ids = [row[0] for row in cursor.fetchall()]

# Faker 라이브러리 초기화
fake = faker.Faker()

# 예약 데이터 생성
reservations = []
for _ in range(50):
    reservation_id = random.randint(10000, 99999)  # 랜덤 예약 ID
    parkinglot_id = random.randint(1, 10)  # 주차장 ID (1~10 범위 내에서 랜덤)
    user_id = random.choice(user_ids)  # 기존 사용자 ID에서 선택
    reservation_status = random.choice(["reserved", "canceled", "completed"])  # 예약 상태
    modified_type = random.choice(["created", "updated", "deleted"])  # 수정 유형
    modified_at = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")  # 수정 시간
    modified_by = random.choice(user_ids)  # 예약 수정한 사용자

    reservations.append((reservation_id, parkinglot_id, user_id, reservation_status, modified_type, modified_at, modified_by))

    cursor.execute("""
        INSERT INTO reservation (reservation_id, parkinglot_id, user_id, reservation_status, modified_type, modified_at, modified_by)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (reservation_id, parkinglot_id, user_id, reservation_status, modified_type, modified_at, modified_by))

print("50개의 랜덤 예약 데이터를 삽입 완료")

# 변경 사항 저장 및 연결 종료
conn.commit()
conn.close()

print("데이터 삽입 완료 및 DB 연결 종료")