from config import app
from flask import render_template


@app.route('/')
def index():
    return render_template('user/base.html')


@app.route('/user')
def user():
    return render_template('user/user.html',name='Ashik')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
