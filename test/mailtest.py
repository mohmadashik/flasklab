import smtplib
s = smtplib.SMTP("localhost")
tolist = ['as8ashikg@gmail.com','ashikg8coder@gmail.com','ramu@mail.com']
msg = '''\\
         ... From: ashikm@dckap.com
         ... Subject: testin'...
         ...
         ... This is a test '''
s.sendmail("ashikm@dckap.com",tolist,msg)