from flask import Flask,g
app = Flask(__name__)
'''#g.example =  'g example variable'  - this line will throw error as 

RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.'''

@app.route('/')
def index():
    g.example =  'g example variable'
    return 'The test flask application is up' + g.example


if __name__== '__main__':
    app.run(debug=True,port=7860)
