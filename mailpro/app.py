from flask_mail import Mail, Message
from flask import Flask
 
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'admin@gmail.com'  
app.config['MAIL_PASSWORD'] = '******'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  


mail = Mail(app)
 
@app.route('/mail')
def email_send():
   msg = Message( 'Hello Message', sender='ashikg8coder@gmail.com', recipients=['as8ashikg@gmail.com'])
   msg.body = 'message body example!'
   mail.send(msg)
   return 'mail sent!'

@app.route('/')
def home():
   return 'the site is app'
if __name__=='__main__':
    app.run(port=3370,debug=True)