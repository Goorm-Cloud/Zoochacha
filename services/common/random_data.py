import sqlite3
import pandas as pd
import random
import faker
import os


# 데이터베이스 연결
#db_path = os.path.abspath("parking.db")
db_path = os.path.abspath("services/admin/parking.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Faker 라이브러리로 가짜 사용자 데이터 생성
fake = faker.Faker()
users = []
for _ in range(50):
    user_id = random.randint(1000, 9999)  # user_id를 INTEGER 값으로 생성
    name = fake.name()[:20]  # VARCHAR(20) 제한
    gender = random.choice(["Male", "Female"])
    email = fake.email()[:50]  # VARCHAR(50) 제한
    age = random.randint(18, 65)
    phone = fake.phone_number()[:20] if random.random() > 0.2 else None  # VARCHAR(20) 제한
    role = random.choice(["admin", "user"])  # VARCHAR(5) 제한

    users.append((user_id, name, gender, email, age, phone, role))
    # cursor.execute("""
    #     INSERT INTO user (user_id, name, gender, email, age, phone, role)
    #     VALUES (?, ?, ?, ?, ?, ?, ?)
    # """, (user_id, name, gender, email, age, phone, role))
    
    # id중복 발생 가능성으로 인해, 아래 코드로 수정
    cursor.execute("""
        INSERT OR REPLACE INTO user (user_id, name, gender, email, age, phone, role)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, name, gender, email, age, phone, role))

print("50명의 가짜 사용자 데이터를 삽입 완료")

# 변경 사항 저장 및 연결 종료
conn.commit()
conn.close()

print("데이터 삽입 완료 및 DB 연결 종료")