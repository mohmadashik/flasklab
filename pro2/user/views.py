from config import app


@app.route("/login")
def login():
    return "user login page"