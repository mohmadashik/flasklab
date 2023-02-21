from flask import Flask
app = Flask(__name__)
### DO NOT WRITE ANY CODE IN THIS FILE

@app.route('/')
def index():
    g.example =  'g example variable'
    return 'The test flask application is up'


if __name__== '__main__':
    app.run(debug=True,port=7860)
