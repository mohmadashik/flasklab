#WORKING

from flask import *  
from flask_mail import *  
  
app = Flask(__name__)  
  
#Flask mail configuration  
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'ashikm@dckap.com'  
app.config['MAIL_PASSWORD'] = 'dckap@123'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
#instantiate the Mail class  
mail = Mail(app)  
message = """ Greetings Arka Media,
                    I hope this email finds you well. This is Mohmad Ashik M A. I am an aspiring screenwriter. I want to make great and wonderful films with my stories. I need producers. 
                    I have seen you have made so many great films. I would like to pitch my stories to you. Kindly give me the email id to which I can send my synopsis. You can choose a suitable director for the film. I will do the screenplay writer's job. 
                    I can write great stories. But I need you. kindly let me know where I can send my story synopsis. Give me a chance, I will give you a BLOCKBUSTER.
               Thanks and regards,
               Mohmad Ashik M A
               +91 8074157082
               Screenplay writer
               Nagari - 517 590
               Chittoor, Andhra Pradesh"""
#configure the Message class object and send the mail from a URL  
@app.route('/mail')  
def index():  
    msg = Message('subject', sender = 'imashikg@gmail.com', recipients=['ashikg8coder@gmail.com'])  
#     msg.body = 'hi, this is the mail sent by using the flask web application'  
    msg.body = message
    try:
         mail.send(msg)
         return 'mail sent!kindly check'
    except Exception as e:
         print(e)
         return 'mail not sent!'


@app.route('/')
def home():
   return 'the site is up'

if __name__ == '__main__':  
    app.run(debug = True,port =9009)  