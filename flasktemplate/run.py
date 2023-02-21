from flask import Flask,g
app = Flask(__name__)
'''#g.example =  'g example variable'  - this line will throw error as 

RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.'''

@app.route('/')
def index():
    return 'The test flask application is up'

@app.route('/global_variable')
def global_check():
    g.foo =  'g global variable example '
    return_g_value  = get_g_value()
    return "this is a global variable ---->"+return_g_value
def get_g_value():
    return g.foo

if __name__== '__main__':
    app.run(debug=True,port=7860)
