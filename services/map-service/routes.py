from flask import Blueprint
from .views.map_view import home_view, static_files, get_parking_lots

main = Blueprint("main", __name__)

# 📌 URL과 뷰 연결
main.route("/", endpoint="index")(home_view)
main.route("/static/<path:filename>")(static_files)
main.route("/api/parking-lots")(get_parking_lots)
