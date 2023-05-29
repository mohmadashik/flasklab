from flask import Flask 

app = Flask(__name__)

@app.route("/hello",methods=['GET'])
def hello_view():
    return {"message":"Hello Monarch Tractor!"}