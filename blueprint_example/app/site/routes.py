from flask import Blueprint

site = Blueprint('site',__name__)

@site.route('/')
def index():
    return "<h1>The site is Active</h1>" 