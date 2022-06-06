from mongoengine import *
from celery import Celery

connect('messages', host='mongodb', port=27017)


class Message(Document):
    name = StringField()
    message = StringField()


app = Celery('tasks',
             broker='amqp://user:pass@rabbit:5672',
             backend='mongodb://mongodb:27017/backdb')
@app.task()
def Send_Message(user, mess):
    Message(name=user, message=mess).save()
    print(user,mess)
    return "Send message"


@app.task()
def Get_Message():
    res = ""
    for obj in Message.objects():
        res += str(obj.name + ": " + obj.message + " <br>")
    return res

if __name__ == '__main__':
    app.start(["worker"])
