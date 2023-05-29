#NOT YET WORKING CHECK WHY?


from flask_mail import Mail, Message
from flask import Flask
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'lshglshduwiwkhskjdhgw8742'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT']= 465  
app.config['MAIL_USERNAME'] = 'agentravik@gmail.com'  
app.config['MAIL_PASSWORD'] = 'uamlfkddxkchujrs'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  

mail = Mail(app)
@app.route('/mail')
def email_send():
   # for recipient in receivers:
      msg = Message( 'Hi subject', sender='noreply@mailpro.com',recipients = ['as8ashikg@gmail.com'] )
      msg.body = 'this is a simple single mail check!'
      try:
         mail.send(msg)
         return 'mail sent!'
      except Exception as e:
         print(e)
         return 'mail not sent'

@app.route('/')
def home():
   return 'the site is app'
if __name__=='__main__':
    app.run(port=3370,debug=True)


# mail = Mail(app)
# receivers=['as8ashikg@gmail.com','ashikg8coder@gmail.com'] 
# @app.route('/mail')
# def email_send():
#    # for recipient in receivers:
#       msg = Message( 'Hello Message', sender='noreply@mailpro.com',recipients = receivers )
#       msg.body = 'this is from noreply mail!'
#       try:
#          mail.send(msg)
#          return 'mail sent!'
#       except Exception as e:
#          print(e)
#          print('hi bro')
#          print('the vars are ',vars(e))
#          return 'mail not sent\n'

# @app.route('/')
# def home():
#    return 'the site is app'
# if __name__=='__main__':
#     app.run(port=3370,debug=True)