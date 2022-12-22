from config import app
from user.views import login
from flask import make_response
@app.route('/')
def index():
    return make_response("welcome to the index page")

@app.route('/profile')
def profile():
    # return request.remote_addr
    return "This is a profile page"

@app.route('/check',methods=['GET','POST'])
def check():
    output = login()
    return output + " added extra"
