from app import app

@app.route("/")
def index():
    return {"data":"index page is up"}