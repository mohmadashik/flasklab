from flask_mail import Mail, Message
from flask import Flask
 
app = Flask(__name__)
mail = Mail(app)
 
@app.route('/mail')
def email():
   msg = Message( 'Hello Message', sender='ashikg8coder@gmail.com', recipients=['as8ashikg@gmail.com'])
   mail.send(msg)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=3330,debug=True)