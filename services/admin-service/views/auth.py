from flask import render_template, redirect, url_for, session
#from .. import oauth
from flask import current_app

def login():#
    return current_app.oauth.oidc.authorize_redirect('http://localhost:5000/role_check')

def role_check():
    user = session.get('user')
    return f'유저 메인페이지입니다.{user}'

def authorize():
    token = current_app.oauth.oidc.authorize_access_token()
    user = token['userinfo']
    session['user'] = user
    return redirect(url_for('routes.role_check'))

def logout():
    session.pop('user', None)
    return redirect(url_for('routes.index'))
