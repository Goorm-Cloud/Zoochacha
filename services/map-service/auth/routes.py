from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/signup")
def signup():
    return render_template("signup.html")  # ✅ 회원가입 페이지 렌더링

@auth.route("/login")
def login():
    return render_template("login.html")  # ✅ 로그인 페이지 렌더링
