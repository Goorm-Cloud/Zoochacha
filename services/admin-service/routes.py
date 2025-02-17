from flask import Blueprint
from .views.auth import login, role_check, authorize, logout
from .views.admin import admin_dashboard
from .views.reservation import add_reservation, edit_reservation, delete_reservation, reservation_detail


# bp 생성
admin_bp = Blueprint('routes', __name__, url_prefix='/admin')


# 로그인 관련 라우트
@admin_bp.route('/login')
def login_route():
    return login()

@admin_bp.route('/role_check')
def role_check_route():
    return role_check()

@admin_bp.route('/authorize')
def authorize_route():
    return authorize()

@admin_bp.route('/logout')
def logout_route():
    return logout()



# 예약 관련 라우트
@admin_bp.route('/')
def admin_dashboard_route():
    return admin_dashboard()

@admin_bp.route('/reservation/add', methods=['GET', 'POST'])
def add_reservation_route():
    return add_reservation()

@admin_bp.route('/reservation/edit/<int:reservation_id>', methods=['GET', 'POST'])
def edit_reservation_route(reservation_id):
    return edit_reservation(reservation_id)

@admin_bp.route('/reservation/delete/<int:reservation_id>', methods=['GET', 'POST'])
def delete_reservation_route(reservation_id):
    return delete_reservation(reservation_id)


@admin_bp.route('/reservation/<int:reservation_id>', methods=['GET'])
def reservation_detail_route(reservation_id):
    return reservation_detail(reservation_id)


