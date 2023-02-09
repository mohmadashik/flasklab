from celery import Celery
from time import sleep
app = Celery('tasks',broker="amqps://lnhevdvi:FifkWbCjM7B8bp-IbZVT-ipUr1HM1Naj@puffin.rmq2.cloudamqp.com/lnhevdvi",backend='db+sqlite:///db.sqlite3')

@app.task()
def reverse(text):
    sleep(5)
    return text[::-1]

"""
    open two terminals
    in one
    open the celery log by 
    celery -A tasks worker --loglevel=info
    here tasks in the module name
    in another one
    start python console
    run reverse.delay('some text')
    now check the first terminal
"""