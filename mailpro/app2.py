from flask import *  
from flask_mail import *  
  
app = Flask(__name__)  
  
#Flask mail configuration  
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'admin@gmail.com'  
app.config['MAIL_PASSWORD'] = '******'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
#instantiate the Mail class  
mail = Mail(app)  
  
#configure the Message class object and send the mail from a URL  
@app.route('/mail')  
def index():  
    msg = Message('subject', sender = 'imashikg@gmail.com', recipients=['ashikg8coder@gmail.com'])  
    msg.body = 'hi, this is the mail sent by using the flask web application'  
    return "Mail Sent@, Please check the mail id"  

@app.route('/')
def home():
   return 'the site is app'

if __name__ == '__main__':  
    app.run(debug = True,port =9009)  