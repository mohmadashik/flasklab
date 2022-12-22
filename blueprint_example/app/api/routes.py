from flask import Blueprint,jsonify

api = Blueprint('api',__name__,url_prefix='/api')

@api.route('/profile')
def profile():
    return jsonify({'status':'the site is active'}) 